# -*- coding: UTF-8 -*-
from datetime import date
from functools import partial
import logging
from PySide import QtCore
from PySide.QtCore import QLocale, QRegExp, Qt, QModelIndex
from PySide.QtGui import QMessageBox, QLineEdit, QComboBox, QScrollArea, QDialog, QTableWidgetItem, QPushButton, QIcon, \
    QRegExpValidator, QPixmap, QCompleter, QHeaderView
from PySide.QtSql import QSqlRelationalTableModel, QSqlQuery, QSqlTableModel
import operator
from src.lib import constants
from src.lib import statics
from src.lib.table_util import WeekdayTableWidgetItem
from src.lib.ui.ui_form_book import Ui_BookForm
from src.lib.util import YearSpinBox
from src.lib.validators import UppercaseValidator, NumericValidator
from src.lib.db_util import Db_Instance
from src.dialogs.select_activity import ActivitySelectDialog

logger = logging.getLogger('add_associate')

class BookAddForm(QScrollArea, Ui_BookForm):
    """ Interface for associate input """

    column = {
            'barcode':1, 'title':2, 'author':3, 'sauthor':4, 'publisher':5, 'year':6, 'price':7,
            'description':8 }

    def __init__(self, parent=None):
        super(BookAddForm, self).__init__(parent)
        self.setupUi(self)

        self._access = statics.access_level
        # for currency formatting
        self._locale = QLocale()

        # had to hardcode these, wouldn't work otherwise:
        self.contentsLayout.setAlignment(self.groupBox, QtCore.Qt.AlignTop)
        self.contentsLayout.setAlignment(self.groupBox_2, QtCore.Qt.AlignTop)

        self.log = logging.getLogger('BookForm')

        self.setup_model()
        self.setup_fields()

        self._subject_list = []

        # flag to indicate whether there were changes to the fields
        self._dirty = False

    def is_dirty(self):
        return self._dirty

    def setup_model(self):
        db = Db_Instance("form_book").get_instance()
        if not db.open():
            self.log.error(db.lastError().text())
            message = unicode("Erro de conexão\n\n""Banco de dados indisponível".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Cadastro de Livro", message)
        else:
            # subject
            self._subject_model = QSqlTableModel(self, db=db)
            self._subject_model.setTable("subject")
            self._subject_model.select()
            # author
            self._author_model = QSqlTableModel(self, db=db)
            self._author_model.setTable("author")
            self._author_model.select()
            # sauthor
            self._s_author_model = QSqlTableModel(self, db=db)
            self._s_author_model.setTable("s_author")
            self._s_author_model.select()
            # publisher
            self._publisher_model = QSqlTableModel(self, db=db)
            self._publisher_model.setTable("publisher")
            self._publisher_model.select()


    def setup_fields(self):
        """ setting up validators and stuff """
        # validators
        # forcing uppercasing on these fields
        self.edTitle.setValidator(UppercaseValidator())
        self.edAuthor.setValidator(UppercaseValidator())
        self.edSAuthor.setValidator(UppercaseValidator())
        self.edPublisher.setValidator(UppercaseValidator())
        currencyValidator = QRegExpValidator(QRegExp("[0-9]{1,4}[,][0-9]{1,2}"))
        self.edPrice.setValidator(currencyValidator)
        self.edBarcode.setValidator(NumericValidator())
        # had to subclass this spinbox to support return grabbing
        self.edYear = YearSpinBox(self)
        self.edYearHolder.addWidget(self.edYear)
        self.edYear.setMinimum(1900)
        self.edYear.setMaximum(date.today().year)
        self.edYear.setValue(date.today().year)
        # fixing tab order
        self.setTabOrder(self.edPublisher, self.edYear)
        self.setTabOrder(self.edYear, self.edPrice)
        # connecting return key to tab
        lineEditList = self.findChildren(QLineEdit)
        for lineEdit in lineEditList:
            # had some problem with C++ originated objects
            if lineEdit.objectName() not in ['qt_spinbox_lineedit', 'edSubject']:
                lineEdit.returnPressed.connect(lineEdit.focusNextChild)
            # detect changes on line edits
            lineEdit.textChanged.connect(self.check_changes)
        # different behaviour for this one
        self.edSubject.returnPressed.connect(self.on_btnAddSubject_clicked)

        # completers
        self.config_completer(self.edSubject, self._subject_model, "name")
        self.config_completer(self.edAuthor, self._author_model, "name")
        self.config_completer(self.edSAuthor, self._s_author_model, "name")
        self.config_completer(self.edPublisher, self._publisher_model, "name")


    def config_completer(self, line_edit, model, field):
        # sets up a completer based on a QSqlTableModel for the specified field on a QLineEdit
        completer = QCompleter()
        completer.setModel(model)
        completer.setCompletionColumn(model.fieldIndex(field))
        completer.setCompletionMode(QCompleter.PopupCompletion)
        line_edit.setCompleter(completer)


    def check_changes(self, txt):
        if txt != '':
            self._dirty = True

    def submit_data(self):
        # TODO: build a statement so we can get the latest id in a safe way
        pass
    #     self._model.insertRow(0)
    #     data = self.extract_input()
    #     for key,val in data.items():
    #         self._model.setData(self._model.index(0, self.column[key]), val)
    #     # try to commit a record
    #     if not self._model.submitAll():
    #         self.log.error(self._model.lastError().text())
    #         message = unicode("Erro de transação\n\n""Não foi possível salvar no banco de dados".decode('utf-8'))
    #         QMessageBox.critical(self, "Seareiros - Cadastro de Atividade", message)
    #         return False
    #     else:
    #         # successfully added an associate, adding it's activities
    #         activities = self.extract_activities_input()
    #         error = False
    #         if len(activities) > 0:
    #             associate_id = self.get_added_record().value("id")
    #             for id in activities:
    #                 self._act_model.insertRow(0)
    #                 self._act_model.setData(self._act_model.index(0, 0), associate_id)
    #                 self._act_model.setData(self._act_model.index(0, 1), id)
    #                 ok = self._act_model.submitAll()
    #                 if not ok:
    #                     error = True
    #                     self.log.error(self._act_model.lastError().text())
    #         if not error:
    #             message = unicode("Sucesso!\n\n""O associado foi salvo com êxito no banco de dados".decode('utf-8'))
    #             QMessageBox.information(self, "Seareiros - Cadastro de Associado", message)
    #         else:
    #             message = unicode("Erro\n\n""Associado cadastrado, "
    #                               "porém ocorreu um problema ao salvar suas atividades".decode('utf-8'))
    #             QMessageBox.warning(self, "Seareiros - Cadastro de Associado", message)
    #
    #         return True

    def clear(self):
        self._dirty = False
        lineEditList = self.findChildren(QLineEdit)
        for lineEdit in lineEditList:
            lineEdit.clear()
        self.clear_table()
        self.edBarcode.setFocus()

    @QtCore.Slot()
    def on_btnAddSubject_clicked(self):
        txt = self.edSubject.text()
        if txt != '':
            id = self.id_from_completion(self.edSubject)
            if id:
                # known register
                data = [id, txt]
            else:
                # new data
                data = [None, txt]
            not_a_duplicate = self.add_subject(data)
            if not_a_duplicate:
                self.refresh_tableSubjects()
                self.edSubject.setText('')
            self.edSubject.setFocus()

    def id_from_completion(self, line_edit):
        index = line_edit.completer().currentIndex()
        if index.isValid():
            # known register
            row = index.row()
            id = line_edit.completer().completionModel().index(row, 0).data()
            return id
        else:
            return None

    @QtCore.Slot()
    def on_btnCleanSubjects_clicked(self):
        self.clear_table()
        self.edSubject.setFocus()

    def clear_table(self):
        self._subject_list = []
        self.tableSubjects.clear()
        self.refresh_tableSubjects()

    def add_subject(self, data):
        """ adds a subject to the list except for duplicates """
        if data in self._subject_list:
            return False
        else:
            self._subject_list.append(data)
            # sorts by name
            self._subject_list.sort(key=operator.itemgetter(1))
            return True

    def refresh_tableSubjects(self):
        if len(self._subject_list) > 0:
            self.tableSubjects.setColumnCount(len(self._subject_list[0])+1)
            col_labels = ["", "Nome", ""]
            self.tableSubjects.setHorizontalHeaderLabels(col_labels)
            self.tableSubjects.setColumnHidden(0, True)
        else:
            self.tableSubjects.setColumnCount(0)
        self.tableSubjects.setRowCount(len(self._subject_list))
        for i, row in enumerate(self._subject_list):
            for j, col in enumerate(row):
                item = QTableWidgetItem(col)
                self.tableSubjects.setItem(i, j, item)
            # icon to remove rows individually
            remove_icon = QIcon(":icons/conn_failed.png")
            remove_btn = QPushButton(remove_icon, "")
            remove_btn.clicked.connect(partial(self.remove_subject, subject=row))
            self.tableSubjects.setCellWidget(i, len(row), remove_btn)
        self.tableSubjects.resizeColumnsToContents()
        self.tableSubjects.horizontalHeader().setResizeMode(1, QHeaderView.Stretch)

    def remove_subject(self, subject):
        # remove a row based on its value
        self._subject_list.remove(subject)
        self.refresh_tableSubjects()

    def extract_input(self):
        data = {}
        data['barcode'] = self.edBarcode.text()
        data['title'] = self.edTitle.text()
        # author
        if self.id_from_completion(self.edAuthor):
            data['author'] = self.id_from_completion(self.edAuthor)
        else:
            data['author'] = self.edAuthor.text()
        # s_author
        if self.id_from_completion(self.edSAuthor):
            data['s_author'] = self.id_from_completion(self.edSAuthor)
        else:
            data['s_author'] = self.edAuthor.text()
        # publisher
        if self.id_from_completion(self.edPublisher):
            data['publisher'] = self.id_from_completion(self.edPublisher)
        else:
            data['publisher'] = self.edAuthor.text()
        data['year'] = self.edYear.value()
        data['price'] = self._locale.toDouble(self.edPrice.text())[0]
        data['description'] = self.edDescription.toPlainText()
        return data

    def extract_subjects_input(self):
        # grab id of selected activities
        subjects = []
        new_subjects = []
        for subj in self._subject_list:
            if subj[0]:
                # selected from previously added subjects
                subjects.append(subj[0])
            else:
                # new subject
                new_subjects.append(subj[1])
        return [subjects, new_subjects]

    # def get_added_record(self):
        # """ My workaround to get the last inserted id without any postgres specific queries """
        # db = Db_Instance("add_book_last_id").get_instance()
        # if not db.open():
        #     return None
        # else:
        #     query = QSqlQuery(db)
        #     query.prepare("SELECT * FROM book WHERE fullname = :fullname")
        #     query.bindValue(":fullname", self.edFullName.text())
        #     query.exec_()
        #     if query.next():
        #         return query.record()
        #     else:
        #         return None
