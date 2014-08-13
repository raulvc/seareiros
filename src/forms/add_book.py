# -*- coding: UTF-8 -*-
from datetime import date
from functools import partial
import logging
import operator
import os

from PySide import QtCore
from PySide.QtCore import QLocale, Qt
from PySide.QtGui import QMessageBox, QLineEdit, QScrollArea, QTableWidgetItem, QPushButton, QIcon, \
    QHeaderView, QFileDialog, QPixmap, QImage, QVBoxLayout
from PySide.QtSql import QSqlTableModel, QSqlQuery

from src.lib import statics
from src.lib.ui.ui_form_book import Ui_BookForm
from src.lib.util import ReturnKeySpinBox, clickable, qpixmap_to_qbytearray, config_completer
from src.lib.validators import UppercaseValidator, NumericValidator, CurrencyValidator
from src.lib.db_util import Db_Instance,  submit_and_get_id


logger = logging.getLogger('add_associate')

class BookAddForm(QScrollArea, Ui_BookForm):
    """ Interface for book input """

    column = {
            'barcode':1, 'title':2, 'author':3, 's_author':4, 'publisher':5, 'year':6, 'price':7,
            'description':8, 'stock':9, 'image':10, 'availability':11 }

    IMG_SIZE = (150, 150)

    def __init__(self, parent=None):
        super(BookAddForm, self).__init__(parent)
        self.setupUi(self)
        # had to subclass this spinbox to support return grabbing
        self.edYear = ReturnKeySpinBox(self)
        self.edYearHolder.addWidget(self.edYear)
        # configuring id's for radio group
        self.radioAvailability.setId(self.rdSell,0)
        self.radioAvailability.setId(self.rdRent,1)
        self.radioAvailability.setId(self.rdInactive,2)

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
        # user did input an image
        self._image_set = False

        # overlaying a clean button over the image (couldn't do it in designer)
        self.btnCleanImage = QPushButton()
        self.btnCleanImage.setIcon(QIcon(":icons/clean.png"))
        self.btnCleanImage.setFixedWidth(35)
        self.btnCleanImage.clicked.connect(self.clear_image)
        self.btnCleanImage.setVisible(False)
        clean_img_layout = QVBoxLayout(self.edImage)
        clean_img_layout.addWidget(self.btnCleanImage)
        clean_img_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        clean_img_layout.setContentsMargins(2,2,0,0)

    def is_dirty(self):
        return self._dirty

    def setup_model(self):
        db = Db_Instance("form_book").get_instance()
        if not db.open():
            self.log.error(db.lastError().text())
            message = unicode("Erro de conexão\n\n""Banco de dados indisponível".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Cadastro de Livro", message)
        else:
            # book
            self._model = QSqlTableModel(self, db=db)
            self._model.setTable("book")
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
            # book subjects
            self._book_in_subj_model = QSqlTableModel(self, db=db)
            self._book_in_subj_model.setTable("book_in_subject")

    def setup_fields(self):
        """ setting up validators and stuff """
        # validators
        # forcing uppercasing on these fields
        self.edTitle.setValidator(UppercaseValidator())
        self.edAuthor.setValidator(UppercaseValidator())
        self.edSAuthor.setValidator(UppercaseValidator())
        self.edPublisher.setValidator(UppercaseValidator())
        self.edPrice.setValidator(CurrencyValidator(self.edPrice))
        self.edBarcode.setValidator(NumericValidator())
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
        # different behaviour for these
        self.edBarcode.textChanged.connect(self.check_barcode)
        self.edSubject.returnPressed.connect(self.on_btnAddSubject_clicked)

        # completers
        config_completer(self.edSubject, self._subject_model, "name")
        config_completer(self.edAuthor, self._author_model, "name")
        config_completer(self.edSAuthor, self._s_author_model, "name")
        config_completer(self.edPublisher, self._publisher_model, "name")

        # making image clickable
        clickable(self.edImage).connect(self.handle_image)

    def clear_image(self):
        img = QImage(":icons/no_image.png")
        self.set_image(img)
        self._image_set = False
        self.btnCleanImage.setVisible(False)

    def handle_image(self):
        image_path = QFileDialog.getOpenFileName(self, "Escolha uma imagem", os.getenv("HOME"), "Imagens (*.png, *.jpg *.bmp)")[0]
        if os.path.exists(image_path):
            self.set_image(QImage(image_path))
            self._image_set = True
            self.btnCleanImage.setVisible(True)

    def set_image(self, img):
        pix = QPixmap.fromImage(img)
        pix = pix.scaled(self.IMG_SIZE[0], self.IMG_SIZE[1], Qt.KeepAspectRatio)
        self.edImage.setPixmap(pix)
        self.edImage.setScaledContents(True)

    def check_changes(self, txt):
        if txt != '':
            self._dirty = True

    def check_barcode(self, txt):
        if len(txt) == self.edBarcode.maxLength():
            self.edBarcode.focusNextChild()

    def _get_id_from_name(self, table, name):
        db = Db_Instance(table + "_fetch_" + name + "_id").get_instance()
        if not db.open():
            return None
        else:
            query = QSqlQuery(db)
            query.prepare("SELECT id FROM %s WHERE name = :name" % table)
            query.bindValue(":name", name)
            query.exec_()
            if query.next():
                return query.record().value("id")
            else:
                return None

    def submit_data(self):
        data = self.extract_input()
        # checking fields that aren't inserted yet
        for val, model in [('author', self._author_model), ('s_author', self._s_author_model),
                           ('publisher', self._publisher_model)]:
            if isinstance(data[val], unicode):
                # needs to be inserted
                model.insertRow(0)
                model.setData(model.index(0,1), data[val])
                data[val] = submit_and_get_id(self, model, self.log)
                if not data[val]:
                    # won't proceed if this fails
                    return False
        # filling a book row
        self._model.insertRow(0)
        for key,val in data.items():
            self._model.setData(self._model.index(0, self.column[key]), val)
        book_id = submit_and_get_id(self, self._model, self.log)
        if book_id:
            # book sucessfully added, now associating related subjects
            subjects, new_subjects = self.extract_subjects_input()
            for subj in new_subjects:
                self._subject_model.insertRow(0)
                self._subject_model.setData(self._subject_model.index(0,1), subj)
                id = submit_and_get_id(self, self._subject_model, self.log)
                if not id:
                    # issue saving new subject
                    return False
                subjects.append(int(id))
            # associating book and it's subjects
            error = False
            for subj_id in subjects:
                self._book_in_subj_model.insertRow(0)
                self._book_in_subj_model.setData(self._book_in_subj_model.index(0,0), book_id)
                self._book_in_subj_model.setData(self._book_in_subj_model.index(0,1), subj_id)
                ok = self._book_in_subj_model.submitAll()
                if not ok:
                    error = True
                    break
            if error:
                self.log.error(self._book_in_subj_model.lastError.text())
                message = unicode("Erro\n\n""Livro cadastrado, porém ocorreu um problema ao"
                              " salvar os temas a que está associado".decode('utf-8'))
                QMessageBox.warning(self, "Seareiros - Cadastro de Livro", message)
                return False
            else:
                message = unicode("Sucesso!\n\n""O livro foi salvo com êxito no banco de dados".decode('utf-8'))
                QMessageBox.information(self, "Seareiros - Cadastro de Livro", message)
                return True
        # failed to insert a row
        return False

    def clear(self):
        self._dirty = False
        lineEditList = self.findChildren(QLineEdit)
        for lineEdit in lineEditList:
            lineEdit.clear()
        self.clear_table()
        self.clear_image()
        self.edBarcode.setFocus()

    @QtCore.Slot()
    def on_btnAddSubject_clicked(self):
        txt = self.edSubject.text()
        if txt != '':
            id = self._get_id_from_name('subject', self.edSubject.text())
            if id:
                # known register
                data = [id, txt]
            else:
                # new data
                data = [None, txt]
            not_a_duplicate = self.add_subject(data)
            if not_a_duplicate:
                self.refresh_tableSubjects()
                self.edSubject.clear()
            self.edSubject.setFocus()

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

        # completer fields
        for c_field, line_edit in [("author", self.edAuthor), ("s_author", self.edSAuthor), ("publisher", self.edPublisher)]:
            data[c_field] = self._get_cfield_value(c_field, line_edit.text())
        data['year'] = self.edYear.value()
        data['price'] = self._locale.toDouble(self.edPrice.text())[0]
        data['description'] = self.edDescription.toPlainText()
        if self._image_set:
            data['image'] = qpixmap_to_qbytearray(self.edImage.pixmap())

        data['availability'] = self.radioAvailability.checkedId()

        return data

    def _get_cfield_value(self, c_field, text):
        if text == '':
            return None
        id = self._get_id_from_name(c_field, text)
        if id:
            return id
        else:
            return text

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
        return (subjects, new_subjects)

