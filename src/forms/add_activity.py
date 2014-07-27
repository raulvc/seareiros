# -*- coding: UTF-8 -*-
import logging
from PySide import QtCore
from PySide.QtGui import QMessageBox, QComboBox, QScrollArea, QRadioButton
from PySide.QtSql import QSqlRelationalTableModel, QSqlQuery
from src.lib.ui.ui_form_activity import Ui_ActivityForm
from src.lib.db_util import Db_Instance

logger = logging.getLogger('add_activity')

class ActivityForm(QScrollArea, Ui_ActivityForm):
    """ Interface for activity input """

    def __init__(self, parent=None):
        super(ActivityForm, self).__init__(parent)
        self.setupUi(self)

        # had to hardcode these, wouldn't work otherwise:
        self.verticalLayout.setAlignment(self.groupBox, QtCore.Qt.AlignTop)

        self.log = logging.getLogger('ActivityForm')

        self.setup_fields()
        self.setup_model()

    def setup_fields(self):
        """ setting up validators and stuff """
        comboBoxList = self.findChildren(QComboBox)
        for comboBox in comboBoxList:
            comboBox.activated.connect(comboBox.focusNextChild)

    def setup_model(self):
        db = Db_Instance("form_activity").get_instance()
        if not db.open():
            self.log.error(db.lastError().text())
            message = unicode("Erro de conexão\n\n""Banco de dados indisponível".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Cadastro de Atividade", message)
        else:
            self._model = QSqlRelationalTableModel(self, db=db)
            self._model.setTable("activity")

    def extract_input(self):
        data = {}
        data['description'] = self.comboDescription.currentText()
        data['room'] = self.comboRoom.currentIndex()
        # finding out which radio button is checked in a group
        for i in range(0,6):
            rd_button_name = "rd_weekday" + str(i)
            rd_button = self.findChild(QRadioButton, rd_button_name)
            if rd_button.isChecked():
                data['weekday'] = i
        data['weektime'] = self.editTime.time()
        return data

    def submit_data(self):
        self._model.insertRow(0)

        data = self.extract_input()

        column = {'description':1, 'room':2, 'weekday':3, 'weektime':4}

        for key,val in data.items():
            self._model.setData(self._model.index(0, column[key]), val)

        # self._model.setData(self._model.index(0, DESCRIPTION), data['description'])
        # self._model.setData(self._model.index(0, ROOM), data['room'])
        # self._model.setData(self._model.index(0, WEEKDAY), data['weekday'])
        # self._model.setData(self._model.index(0, WEEKTIME), data['weektime'])

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

    def get_added_record(self):
        """ My workaround to get the last inserted id without any postgres specific queries """
        db = Db_Instance("add_activity_last_id").get_instance()
        if not db.open():
            return None
        else:
            query = QSqlQuery(db)
            query.prepare("SELECT * FROM activity WHERE description = :description AND "
                          "room = :room AND weekday = :weekday AND weektime = :weektime")
            data = self.extract_input()
            for key, val in data.items():
                key = ":" + key
                query.bindValue(key, val)
            query.exec_()
            if query.next():
                return query.record()
            else:
                return None


    def clear(self):
        self.comboDescription.setCurrentIndex(0)
        self.comboRoom.setCurrentIndex(0)
        self.rd_weekday0.setChecked(True)
        self.comboDescription.setFocus()
