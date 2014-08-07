# -*- coding: UTF-8 -*-
from datetime import date
from functools import partial
import logging
import operator
import os

from PySide import QtCore
from PySide.QtCore import Qt, QLocale, QByteArray
from PySide.QtGui import QMessageBox, QLineEdit, QScrollArea, QTableWidgetItem, QPushButton, QIcon, QVBoxLayout, \
    QHeaderView, QPixmap, QImage, QFileDialog
from PySide.QtSql import QSqlQueryModel, QSqlTableModel, QSqlRelationalTableModel, QSqlRelation, QSqlQuery

from src.lib import statics
from src.lib.ui.ui_form_book import Ui_BookForm
from src.lib.util import iterate_model, YearSpinBox, clickable, qpixmap_to_qbytearray, qbytearray_to_qimage, \
    config_completer
from src.lib.validators import UppercaseValidator, CurrencyValidator, NumericValidator
from src.lib.db_util import Db_Instance, submit_and_get_id


logger = logging.getLogger('edit_book')

class BookEditForm(QScrollArea, Ui_BookForm):
    """ Interface for book edit """

    column = {
            'id':0, 'barcode':1, 'title':2, 'author':3, 's_author':4, 'publisher':5, 'year':6, 'price':7,
            'description':8, 'stock':9, 'image':10 }
    IMG_SIZE = (150, 150)

    def __init__(self, record_id, parent=None):
        super(BookEditForm, self).__init__(parent)
        self.setupUi(self)
        # had to subclass this spinbox to support return grabbing
        self.edYear = YearSpinBox(self)
        self.edYearHolder.addWidget(self.edYear)
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

        self._access = statics.access_level
        # for currency formatting
        self._locale = QLocale()
        self._record_id = record_id

        # had to hardcode these, wouldn't work otherwise:
        self.contentsLayout.setAlignment(self.groupBox, QtCore.Qt.AlignTop)
        self.contentsLayout.setAlignment(self.groupBox_2, QtCore.Qt.AlignTop)

        self.log = logging.getLogger('BookEditForm')

        self._subject_list = []

        self._removed_subjects = []
        self._added_subjects = []

        self.setup_model()
        self.fill_form()
        self.setup_fields()
        self._old_data = self.extract_input(text_only=True)

        # flag to indicate whether there were changes to the fields
        self._dirty = False
        # user did input an image
        self._image_set = False
        # image changed during edit
        self._image_changed = False

    def is_dirty(self):
        return self._dirty

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

    def fill_form(self):
        # retrieving book info
        self.edBarcode.setText(self._record.value("barcode"))
        self.edTitle.setText(self._record.value("title"))
        self.edYear.setValue(self._record.value("year"))
        self.edDescription.setPlainText(self._record.value("description"))
        # retrieving image
        ba = QByteArray(self._record.value("image"))
        if ba:
            self._image_set = True
            img = qbytearray_to_qimage(ba)
            self.set_image(img, clean_visible=True)
        # currency
        self.edPrice.setText(self._locale.toString(float(self._record.value("price").replace('$',''))).replace('.',''))
        # qcompleter fields
        self.edAuthor.setText(self._get_name_from_id("author", self._record.value("author_id")))
        self.edSAuthor.setText(self._get_name_from_id("s_author", self._record.value("s_author_id")))
        self.edPublisher.setText(self._get_name_from_id("publisher", self._record.value("publisher_id")))

        # retrieving subjects
        for subj_record in self._subj_records:
            self.add_subject([subj_record.value("id"),subj_record.value("name")])

        # clearing changes
        self._added_subjects[:] = []
        self.refresh_tableSubjects()

    def clear_image(self):
        img = QImage(":icons/no_image.png")
        self.set_image(img, clean_visible=False)
        if self._image_set:
            self._image_set = False
        self._image_changed = True

    def handle_image(self):
        image_path = QFileDialog.getOpenFileName(self, "Escolha uma imagem", os.getenv("HOME"), "Imagens (*.png, *.jpg *.bmp)")[0]
        if os.path.exists(image_path):
            self.set_image(QImage(image_path), clean_visible=True)
            self._image_set = True
            self._image_changed = True

    def set_image(self, img, clean_visible=False):
        pix = QPixmap.fromImage(img)
        pix = pix.scaled(self.IMG_SIZE[0], self.IMG_SIZE[1], Qt.KeepAspectRatio)
        self.edImage.setPixmap(pix)
        self.edImage.setScaledContents(True)
        self.btnCleanImage.setVisible(clean_visible)

    def check_changes(self, txt):
        # getting sender info
        sender = self.sender().objectName().split('ed')[1].lower()
        if sender != 'subject' and self._old_data[sender] != txt:
            self._dirty = True

    def check_barcode(self, txt):
        if len(txt) == self.edBarcode.maxLength():
            self.edBarcode.focusNextChild()

    def extract_input(self, text_only=False):
        data = {}
        data['barcode'] = self.edBarcode.text()
        data['title'] = self.edTitle.text()

        # completer fields
        for c_field, line_edit in [("author", self.edAuthor), ("s_author", self.edSAuthor), ("publisher", self.edPublisher)]:
            if not text_only:
                data[c_field] = self._get_cfield_value(c_field, line_edit.text())
            else:
                data[c_field] = line_edit.text()
        data['year'] = self.edYear.value()
        data['price'] = self._locale.toDouble(self.edPrice.text())[0]
        data['description'] = self.edDescription.toPlainText()
        if not text_only and self._image_changed and self._image_set:
            data['image'] = qpixmap_to_qbytearray(self.edImage.pixmap())

        return data

    def setup_model(self):
        db = Db_Instance("edit_book").get_instance()
        if not db.open():
            self.log.error(db.lastError().text())
            message = unicode("Erro de conexão\n\n""Banco de dados indisponível".decode('utf-8'))
            QMessageBox.critical(self, unicode("Seareiros - Edição de Livro".decode('utf-8')), message)
        else:
            # book
            self._model = QSqlRelationalTableModel(self, db=db)
            self._model.setTable("book")
            self._model.setFilter("id = " + str(self._record_id))
            # self._model.setRelation(self.column["author"], QSqlRelation("author", "id", "name"))
            # self._model.setRelation(self.column["s_author"], QSqlRelation("s_author", "id", "name"))
            # self._model.setRelation(self.column["publisher"], QSqlRelation("publisher", "id", "name"))
            self._model.select()
            self._record = self._model.record(0)
            # models for setting up qcompleters:
            # book_in_subject
            self._book_in_subj_model = QSqlTableModel(self, db=db)
            self._book_in_subj_model.setTable("book_in_subject")
            # subject
            self._subject_model = QSqlTableModel(self, db=db)
            self._subject_model.setTable("subject")
            self._subject_model.select()
            # author
            self._author_model = QSqlTableModel(self, db=db)
            self._author_model.setTable("author")
            self._author_model.select()
            # s_author
            self._s_author_model = QSqlTableModel(self, db=db)
            self._s_author_model.setTable("s_author")
            self._s_author_model.select()
            # publisher
            self._publisher_model = QSqlTableModel(self, db=db)
            self._publisher_model.setTable("publisher")
            self._publisher_model.select()

            # retrieving current subjects, should probably place this elsewhere but it's related to models
            self._subject_records = []
            sql_statement = """SELECT id, name FROM subject s, book_in_subject b_s
                               WHERE s.id = b_s.subject_id AND b_s.book_id = %s
                            """ % str(self._record_id)
            read_only_subject_model = QSqlQueryModel()
            read_only_subject_model.setQuery(sql_statement, db)
            # checking query validity
            if not read_only_subject_model.lastError().isValid():
                self._subj_records = iterate_model(read_only_subject_model)

    def update_data(self):
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
        for key,val in data.items():
            self._model.setData(self._model.index(0, self.column[key]), val)
        print 'image' in data
        print self._image_changed
        if 'image' not in data and self._image_changed:
            # user cleared the image
            ok = self._model.setData(self._model.index(0, self.column['image']), None)
            print ok

        # try to commit changes
        if not self._model.submitAll():
            self.log.error(self._model.lastError().text())
            message = unicode("Erro de transação\n\n""Não foi possível salvar no banco de dados".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Edição de Livro", message)
            return False
        else:
            # updating subjects
            error = False
            # added subjects
            for subj in self._added_subjects:
                # the list has the format [id, text] for existing subjects or [None, text] otherwise
                if not subj[0]:
                    # need to insert the subject before associating it with the book
                    self._subject_model.insertRow(0)
                    self._subject_model.setData(self._subject_model.index(0,1), subj[1])
                    subj[0] = submit_and_get_id(self, self._subject_model, self.log)
                    if not subj[0]:
                        error = True
                        break
                # have a valid record id for the subject to be associated
                self._book_in_subj_model.insertRow(0)
                self._book_in_subj_model.setData(self._book_in_subj_model.index(0,0), self._record_id)
                self._book_in_subj_model.setData(self._book_in_subj_model.index(0,1), subj[0])
                ok = self._book_in_subj_model.submitAll()
                if not ok:
                    error = True
                    self.log.error(self._book_in_subj_model.setLastError().text())
                    break
            # removed subjects
            for removed_id in self._removed_subjects:
                self._book_in_subj_model.setFilter("book_id = %s AND subject_id = %s" % (str(self._record_id),str(removed_id)))
                self._book_in_subj_model.select()
                self._book_in_subj_model.removeRow(0)
                if self._book_in_subj_model.lastError().isValid():
                    error = True
                    self.log.error(self._book_in_subj_model.lastError().text())
                    break
            if not error:
                message = unicode("Sucesso!\n\n""O livro foi atualizado com êxito no banco de dados".decode('utf-8'))
                QMessageBox.information(self, unicode("Seareiros - Edição de Livro".decode('utf-8')), message)
            else:
                message = unicode("Erro\n\n""Associado alterado, "
                                  "porém ocorreu um problema ao salvar suas atividades".decode('utf-8'))
                QMessageBox.warning(self, unicode("Seareiros - Edição de Livro".decode('utf-8')), message)
            # if I don't set this flag here it'll trigger a warning for altering data on the form
            self._dirty = False
            return True

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

    def _get_name_from_id(self, table, id):
        db = Db_Instance(table + "_fetch_" + str(id) + "_name").get_instance()
        if not db.open():
            return None
        else:
            query = QSqlQuery(db)
            query.prepare("SELECT name FROM %s WHERE id = :id" % table)
            query.bindValue(":name", id)
            query.exec_()
            if query.next():
                return query.record().value("name")
            else:
                return None

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
        # can't directly change activity_list here
        itens = [i for i in self._subject_list]
        for item in itens:
            self.remove_subject(item)
        self._added_subjects[:] = []

    def add_subject(self, data):
        """ adds a subject to the list except for duplicates """
        if data in self._subject_list:
            return False
        else:
            if self.is_in_del_queue(data[0]):
                self._removed_subjects.remove(data[0])
            else:
                self._added_subjects.append(data)
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

    def is_in_del_queue(self, id):
        return id in self._removed_subjects

    def is_in_add_queue(self, data):
        return data in self._added_subjects

    def remove_subject(self, subject):
        # remove a row based on its value
        self._subject_list.remove(subject)
        if self.is_in_add_queue(subject):
             # unqueue previously added activity
            self._added_subjects.remove(subject)
        else:
            id = subject[0]
            if id:
                self._removed_subjects.append(id)
        self.refresh_tableSubjects()

    def _get_cfield_value(self, c_field, text):
        if text == '':
            return None
        id = self._get_id_from_name(c_field, text)
        if id:
            return id
        else:
            return text