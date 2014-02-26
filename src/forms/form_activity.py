# -*- coding: UTF-8 -*-
import logging
from PySide import QtCore
from PySide.QtGui import QMessageBox, QComboBox, QScrollArea
from PySide.QtSql import QSqlRelationalTableModel
from src.lib.ui.ui_form_activity import Ui_ActivityForm
from src.lib.db_util import Db_Instance

logger = logging.getLogger('add_activity')

class AddActivityForm(QScrollArea, Ui_ActivityForm):
    """ Interface for activity input """

    ID, DESCRIPTION, ROOM, WEEKDAY, WEEKTIME = range(5)

    def __init__(self, parent=None):
        super(AddActivityForm, self).__init__(parent)
        self.setupUi(self)

        # had to hardcode these, wouldn't work otherwise:
        self.verticalLayout.setAlignment(self.groupBox, QtCore.Qt.AlignTop)

        self.log = logging.getLogger('AddActivityDock')

        self.setup_editing()
        self.setup_model()

    def setup_editing(self):
        # tries to make things easier for user by allowing him to tab with return key
        # or after selecting something from a combobox
        comboBoxList = self.findChildren(QComboBox)
        for comboBox in comboBoxList:
            comboBox.activated.connect(comboBox.focusNextChild)

    def setup_model(self):
        db = Db_Instance("add_activity").get_instance()
        if not db.open():
            self.log.error(db.lastError().text())
            message = unicode("Erro de conexão\n\n""Banco de dados indisponível".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Cadastro de Atividade", message)
        else:
            self._model = QSqlRelationalTableModel(self, db=db)
            self._model.setTable("activity")

    def submit_data(self):
        self._model.insertRow(0)

        self._model.setData(self._model.index(0, self.DESCRIPTION), self.comboDescription.currentText())
        self._model.setData(self._model.index(0, self.ROOM), self.comboRoom.currentIndex())
        self._model.setData(self._model.index(0, self.WEEKDAY), self.comboWeekday.currentIndex())
        self._model.setData(self._model.index(0, self.WEEKTIME), self.editTime.time())

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
        self.comboDescription.setCurrentIndex(0)
        self.comboRoom.setCurrentIndex(0)
        self.comboWeekday.setCurrentIndex(0)
        self.comboDescription.setFocus()
