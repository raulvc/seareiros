# -*- coding: UTF-8 -*-
from functools import partial
import logging
from PySide import QtCore
from PySide.QtGui import QMessageBox, QLineEdit, QComboBox, QScrollArea, QDialog, QTableWidgetItem, QPushButton, QIcon
from PySide.QtSql import QSqlRelationalTableModel, QSqlQuery, QSqlQueryModel
import operator
from src.lib import constants
from src.lib import statics
from src.lib.table_util import WeekdayTableWidgetItem
from src.lib.ui.ui_form_associate import Ui_AssociateForm
from src.lib.util import iterate_model
from src.lib.validators import UppercaseValidator, EmailValidator, AlphaNumericValidator
from src.lib.db_util import Db_Instance
from src.dialogs.select_activity import ActivitySelectDialog

logger = logging.getLogger('add_associate')

class AssociateAddForm(QScrollArea, Ui_AssociateForm):
    """ Interface for associate input """

    column = {
            'fullname':1, 'nickname':2, 'rg':3, 'cpf':4, 'maritalstatus':5, 'email':6, 'streetaddress':7,
            'complement':8, 'district':9, 'province':10, 'city':11, 'cep':12,
            'phoneres':13, 'phonecom':14, 'phonepriv':15 }

    def __init__(self, parent=None, record_id=None):
        super(AssociateAddForm, self).__init__(parent)
        self.setupUi(self)

        self._access = statics.access_level

        # had to hardcode these, wouldn't work otherwise:
        self.contentsLayout.setAlignment(self.groupBox, QtCore.Qt.AlignTop)
        self.contentsLayout.setAlignment(self.groupBox_2, QtCore.Qt.AlignTop)
        self.contentsLayout.setAlignment(self.groupBox_3, QtCore.Qt.AlignTop)
        self.contentsLayout.setAlignment(self.groupBox_4, QtCore.Qt.AlignTop)

        self.log = logging.getLogger('AssociateForm')
        self.setup_fields()

        self._activity_list = []

        self.setup_model()

        # flag to indicate whether there were changes to the fields
        self._dirty = False

    def is_dirty(self):
        return self._dirty

    def setup_fields(self):
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

    def fill_form(self):
        # retrieving associate info
        self.edFullName.setText(self._record.value(1))
        self.edNickname.setText(self._record.value(2))
        self.edRG.setText(self._record.value(3))
        self.edCPF.setText(self._record.value(4))
        self.comboMaritalStatus.setCurrentIndex(self._record.value(5))
        self.edEmail.setText(self._record.value(6))
        self.edStreet.setText(self._record.value(7))
        self.edComplement.setText(self._record.value(8))
        self.edDistrict.setText(self._record.value(9))
        self.comboProvince.setCurrentIndex(self._record.value(10))
        self.edCity.setText(self._record.value(11))
        self.edCEP.setText(self._record.value(12))
        self.edPhoneRes.setText(self._record.value(13))
        self.edPhoneCom.setText(self._record.value(14))
        self.edPhonePriv.setText(self._record.value(15))
        # retrieving associate activities
        for act_record in self._activity_records:
            self.add_activity(act_record)
        self.refresh_tableActivities()

    def check_changes(self, txt):
        if txt != '':
            self._dirty = True

    def setup_model(self, id=None):
        db = Db_Instance("form_associate").get_instance()
        if not db.open():
            self.log.error(db.lastError().text())
            message = unicode("Erro de conexão\n\n""Banco de dados indisponível".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Cadastro de Associado", message)
        else:
            self._model = QSqlRelationalTableModel(self, db=db)
            self._model.setTable("associate")
            self._act_model = QSqlRelationalTableModel(self, db=db)
            self._act_model.setTable("associate_in_activity")

    def submit_data(self):
        self._model.insertRow(0)
        data = self.extract_input()
        for key,val in data.items():
            self._model.setData(self._model.index(0, self.column[key]), val)
        # try to commit a record
        if not self._model.submitAll():
            self.log.error(self._model.lastError().text())
            message = unicode("Erro de transação\n\n""Não foi possível salvar no banco de dados".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Cadastro de Atividade", message)
            return False
        else:
            # successfully added an associate, adding it's activities
            activities = self.extract_activities_input()
            error = False
            if len(activities) > 0:
                associate_id = self.get_added_record().value("id")
                for id in activities:
                    self._act_model.insertRow(0)
                    self._act_model.setData(self._act_model.index(0, 0), associate_id)
                    self._act_model.setData(self._act_model.index(0, 1), id)
                    ok = self._act_model.submitAll()
                    if not ok:
                        error = True
                        self.log.error(self._act_model.lastError().text())
            if not error:
                message = unicode("Sucesso!\n\n""O associado foi salvo com êxito no banco de dados".decode('utf-8'))
                QMessageBox.information(self, "Seareiros - Cadastro de Associado", message)
            else:
                message = unicode("Erro\n\n""Associado cadastrado, "
                                  "porém ocorreu um problema ao salvar suas atividades".decode('utf-8'))
                QMessageBox.warning(self, "Seareiros - Cadastro de Associado", message)

            return True

    def clear(self):
        self._dirty = False
        lineEditList = self.findChildren(QLineEdit)
        for lineEdit in lineEditList:
            lineEdit.clear()
        self.comboMaritalStatus.setCurrentIndex(0)
        self.comboProvince.setCurrentIndex(24)
        self.clear_table()
        self.edFullName.setFocus()

    @QtCore.Slot()
    def on_btnAddActivity_clicked(self):
        activity_dialog = ActivitySelectDialog()
        if activity_dialog.exec_() == QDialog.Accepted:
            record = activity_dialog.get_record()
            not_a_duplicate = self.add_activity(record)
            if not_a_duplicate:
                self.refresh_tableActivities()

    @QtCore.Slot()
    def on_btnCleanActivities_clicked(self):
        self.clear_table()

    def clear_table(self):
        self._activity_list = []
        self.tableActivities.clear()
        self.refresh_tableActivities()

    def refresh_tableActivities(self):
        if len(self._activity_list) > 0:
            self.tableActivities.setColumnCount(len(self._activity_list[0])+1)
            col_labels = ["", unicode("Descrição".decode("utf-8")), "Sala", "Dia", unicode("Horário".decode("utf-8")),""]
            self.tableActivities.setHorizontalHeaderLabels(col_labels)
            self.tableActivities.setColumnHidden(0, True)
        else:
            self.tableActivities.setColumnCount(0)
        self.tableActivities.setRowCount(len(self._activity_list))
        for i, row in enumerate(self._activity_list):
            for j, col in enumerate(row):
                # custom sorting for weekdays
                if j == 3:
                    item = WeekdayTableWidgetItem(col)
                else:
                    item = QTableWidgetItem(col)
                self.tableActivities.setItem(i, j, item)
            # icon to remove rows individually
            remove_icon = QIcon(":icons/conn_failed.png")
            remove_btn = QPushButton(remove_icon, "")
            remove_btn.clicked.connect(partial(self.remove_activity, activity=row))
            self.tableActivities.setCellWidget(i, len(row), remove_btn)
        self.tableActivities.resizeColumnsToContents()

    def is_in_del_queue(self, record):
        return record in self._removed_activities
    def is_in_add_queue(self, record):
        return record in self._added_activities

    def add_activity(self, record):
        """ adds an activity to the list except for duplicates """
        # this brings shame to me but meh, faster to hardcode (see model_activity)
        # id = str(record.value("id"))
        id = record.value("id")
        room = record.value("room")
        if room == 0:
            room = "Nenhuma"
        else:
            room = str(room)
        weekday = constants.days_of_the_week[record.value("weekday")]
        weektime = record.value("weektime").toString("HH:mm")
        entry = (id, record.value("description"), room,
                 weekday, weektime)

        if entry in self._activity_list:
            return False
        else:
            self._activity_list.append(entry)
            # sorts by day/time
            self._activity_list.sort(key=operator.itemgetter(3,4))
            # self._activity_list = sorted(self._activity_list, key=lambda dia_hora: (dia_hora[3], dia_hora[2]))
            return True

    def remove_activity(self, activity):
        # remove a row based on its value
        self._activity_list.remove(activity)
        self.refresh_tableActivities()

    def extract_input(self):
        data = {}
        data['fullname'] = self.edFullName.text()
        data['nickname'] = self.edNickname.text()
        data['rg'] = self.edRG.text()
        data['cpf'] = self.remove_mask_when_empty(self.edCPF.text())
        data['maritalstatus'] = self.comboMaritalStatus.currentIndex()
        data['email'] = self.edEmail.text()
        data['streetaddress'] = self.edStreet.text()
        data['complement'] = self.edComplement.text()
        data['district'] = self.edDistrict.text()
        data['province'] = self.comboProvince.currentIndex()
        data['city'] = self.edCity.text()
        data['cep'] = self.remove_mask_when_empty(self.edCEP.text())
        data['phoneres'] = self.remove_mask_when_empty(self.edPhoneRes.text())
        data['phonecom'] = self.remove_mask_when_empty(self.edPhoneCom.text())
        data['phonepriv'] = self.remove_mask_when_empty(self.edPhonePriv.text())
        return data

    def remove_mask_when_empty(self, text):
        """ I don't want to save a mask when there's no user input """
        if text in ['()-', '.-', '..-']:
            return ''
        else:
            return text

    def extract_activities_input(self):
        # grab id of selected activities
        activity_id_list = []
        for act in self._activity_list:
            activity_id_list.append(act[0])
        return activity_id_list

    def get_added_record(self):
        """ My workaround to get the last inserted id without any postgres specific queries """
        db = Db_Instance("add_associate_last_id").get_instance()
        if not db.open():
            return None
        else:
            query = QSqlQuery(db)
            query.prepare("SELECT * FROM associate WHERE fullname = :fullname")
            query.bindValue(":fullname", self.edFullName.text())
            query.exec_()
            if query.next():
                return query.record()
            else:
                return None

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

