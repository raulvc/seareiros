# -*- coding: UTF-8 -*-
import logging
from PySide.QtCore import Qt
from PySide.QtGui import QMessageBox, QLineEdit, QComboBox, QScrollArea
from PySide.QtSql import QSqlRelationalTableModel
from src.lib.ui.ui_form_associate import Ui_AssociateForm
from src.lib.validators import UppercaseValidator, EmailValidator, AlphaNumericValidator
from src.lib.db_util import Db_Instance

logger = logging.getLogger('add_associate')

class AddAssociateForm(QScrollArea, Ui_AssociateForm):
    """ Interface for book input """

    def __init__(self, parent=None):
        super(AddAssociateForm, self).__init__(parent)
        self.setupUi(self)

        # had to hardcode these, wouldn't work otherwise:
        self.verticalLayout.setAlignment(self.groupBox, Qt.AlignTop)
        self.verticalLayout.setAlignment(self.groupBox_2, Qt.AlignTop)
        self.verticalLayout.setAlignment(self.groupBox_3, Qt.AlignTop)
        self.verticalLayout.setAlignment(self.groupBox_4, Qt.AlignTop)

        self.log = logging.getLogger('AddAssociateDock')

        self.setup_editing()
        self.setup_model()

        # flag to indicate whether there were changes to the fields
        self._dirty = False

    def is_dirty(self):
        return self._dirty

    def setup_editing(self):
        # tries to make things easier for user by allowing him to tab with return key
        # or after selecting something from a combobox
        self.edFullName.setValidator(UppercaseValidator())
        self.edNickname.setValidator(UppercaseValidator())
        self.edEmail.setValidator(EmailValidator())
        self.edRG.setValidator(AlphaNumericValidator())
        lineEditList = self.findChildren(QLineEdit)
        comboBoxList = self.findChildren(QComboBox)
        for lineEdit in lineEditList:
            lineEdit.returnPressed.connect(lineEdit.focusNextChild)
            # detect changes to the line edits
            lineEdit.textChanged.connect(self.check_changes)
        for comboBox in comboBoxList:
            comboBox.activated.connect(comboBox.focusNextChild)

    def check_changes(self, txt):
        if txt != '':
            self._dirty = True

    def setup_model(self):
        db = Db_Instance("add_associate").get_instance()
        if not db.open():
            self.log.error(db.lastError().text())
            message = unicode("Erro de conexão\n\n""Banco de dados indisponível".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Cadastro de Associado", message)
        else:
            self._model = QSqlRelationalTableModel(self, db=db)
            self._model.setTable("users")

    def submit_data(self):
        self._model.insertRow(0)

        # self._model.setData(self._model.index(0, self.DESCRIPTION), self.comboDescription.currentText())
        # self._model.setData(self._model.index(0, self.ROOM), self.comboRoom.currentIndex())
        # self._model.setData(self._model.index(0, self.WEEKDAY), self.comboWeekday.currentIndex())
        # self._model.setData(self._model.index(0, self.WEEKTIME), self.editTime.time())

        # try to commit a record
        if not self._model.submitAll():
            self.log.error(self._model.lastError().text())
            message = unicode("Erro de transação\n\n""Não foi possível salvar no banco de dados".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Cadastro de Atividade", message)
            return False
        else:
            message = unicode("Sucesso!\n\n""A atividade foi salva com êxito no banco de dados".decode('utf-8'))
            QMessageBox.information(self, "Seareiros - Cadastro de Atividade", message)
            return True

    def clear(self):
        self._dirty = False
        lineEditList = self.findChildren(QLineEdit)
        for lineEdit in lineEditList:
            lineEdit.clear()
        self.comboMaritalStatus.setCurrentIndex(0)
        self.comboProvince.setCurrentIndex(24)
        self.edFullName.setFocus()


    # def toggle_visibility(self, visible):
    #     actionAddAssociate = self.parent().parent().actionAddAssociate
    #     if visible:
    #         actionAddAssociate.setEnabled(False)
    #         self.edFullName.setFocus()
    #     else:
    #         actionAddAssociate.setEnabled(True)
    #
    # def closeEvent(self, event):
    #     if self._dirty:
    #         message = unicode("Deseja mesmo sair?\n\nDados não salvos serão perdidos".decode('utf-8'))
    #         reply = QMessageBox.question(self, 'Seareiros', message, QMessageBox.Yes, QMessageBox.No)
    #         if reply != QMessageBox.Yes:
    #             event.ignore()
    #             # return
    #     self.toggle_visibility(False)
    #     grandparent = self.parent().parent()
    #     grandparent.remove_instance(self)
    #     event.accept()

