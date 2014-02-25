# -*- coding: UTF-8 -*-
import logging
from PySide.QtCore import Qt
from PySide.QtGui import QDockWidget, QDialogButtonBox, QMessageBox, QLineEdit, QComboBox
from PySide.QtSql import QSqlRelationalTableModel
from src.lib.ui.ui_add_associate import Ui_Dock
from src.lib.validators import UppercaseValidator, EmailValidator, AlphaNumericValidator
from src.lib.db_util import Db_Instance
from src.forms.generic_search import GenericSearchForm

logger = logging.getLogger('add_associate')

class AddAssociateDock(QDockWidget, Ui_Dock):
    """ Interface for book input """

    def __init__(self, parent=None):
        super(AddAssociateDock, self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close)
        self.buttonBox.button(QDialogButtonBox.Save).setText("Salvar")
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.on_save_clicked)
        self.buttonBox.button(QDialogButtonBox.Reset).setText("Limpar")
        self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.clear)
        # had to hardcode these, wouldn't work otherwise:
        self.verticalLayout.setAlignment(self.groupBox, Qt.AlignTop)
        self.verticalLayout.setAlignment(self.groupBox_2, Qt.AlignTop)
        self.verticalLayout.setAlignment(self.groupBox_3, Qt.AlignTop)

        self.setup_editing()
        self.setup_search()

        self.log = logging.getLogger('AddAssociateDock')
        self.visibilityChanged.connect(self.toggle_visibility)

        self.setup_model()
        # flag to indicate whether there were changes to the fields
        self._dirty = False

    def setup_editing(self):
        self.edFullName.setValidator(UppercaseValidator())
        self.edNickname.setValidator(UppercaseValidator())
        self.edEmail.setValidator(EmailValidator())
        self.edRG.setValidator(AlphaNumericValidator())
        lineEditList = self.tabRegister.findChildren(QLineEdit)
        comboBoxList = self.tabRegister.findChildren(QComboBox)
        for lineEdit in lineEditList:
            lineEdit.returnPressed.connect(lineEdit.focusNextChild)
            lineEdit.textChanged.connect(self.check_changes)
        for comboBox in comboBoxList:
            comboBox.activated.connect(comboBox.focusNextChild)

    def setup_search(self):
        pass

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

    def on_save_clicked(self):
        self._model.insertRow(0)

        # try to commit a record
        if not self._model.submitAll():
            self.log.error(self._model.lastError().text())
            message = unicode("Erro de transação\n\n""Não foi possível salvar no banco de dados".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Cadastro de Associado", message)
        else:
            self.clear()

    def clear(self):
        self._dirty = False
        lineEditList = self.tabRegister.findChildren(QLineEdit)
        for lineEdit in lineEditList:
            lineEdit.clear()
        self.comboMaritalStatus.setCurrentIndex(0)
        self.comboProvince.setCurrentIndex(24)
        self.edFullName.setFocus()


    def toggle_visibility(self, visible):
        actionAddAssociate = self.parent().parent().actionAddAssociate
        if visible:
            actionAddAssociate.setEnabled(False)
            self.edFullName.setFocus()
        else:
            actionAddAssociate.setEnabled(True)

    def closeEvent(self, event):
        if self._dirty:
            message = unicode("Deseja mesmo sair?\n\nDados não salvos serão perdidos".decode('utf-8'))
            reply = QMessageBox.question(self, 'Seareiros', message, QMessageBox.Yes, QMessageBox.No)
            if reply != QMessageBox.Yes:
                event.ignore()
                # return
        self.toggle_visibility(False)
        grandparent = self.parent().parent()
        grandparent.remove_instance(self)
        event.accept()

