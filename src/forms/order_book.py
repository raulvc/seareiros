# -*- coding: UTF-8 -*-

from functools import partial
import logging
import operator

from PySide import QtCore
from PySide.QtCore import QLocale
from PySide.QtGui import QMessageBox, QLineEdit, QScrollArea, QTableWidgetItem, QPushButton, QIcon, \
    QHeaderView, QDialog
from PySide.QtSql import QSqlTableModel, QSqlQuery
from src.dialogs.select_associate import AssociateSelectDialog
from src.dialogs.select_book import BookSelectDialog

from src.lib import statics
from src.lib.exceptions import StockOverflowException, RecordNotFoundException, DbUnavailableException
from src.lib.ui.ui_oform_book import Ui_BookOForm

from src.lib.util import ReturnKeySpinBox
from src.lib.validators import NumericValidator
from src.lib.db_util import Db_Instance, submit_and_get_id, log_to_history


logger = logging.getLogger('order_book')

class BookOrderForm(QScrollArea, Ui_BookOForm):
    """ Interface for ordering books """

    column = { 'associate':1, 'obs':3, 'total':4, 'paid':5 }


    def __init__(self, parent=None):
        super(BookOrderForm, self).__init__(parent)
        self.setupUi(self)

        self._access = statics.access_level
        # for currency formatting
        self._locale = QLocale()

        # had to hardcode these, wouldn't work otherwise:
        self.contentsLayout.setAlignment(self.groupBox, QtCore.Qt.AlignTop)
        self.contentsLayout.setAlignment(self.groupBox_2, QtCore.Qt.AlignTop)
        self.contentsLayout.setAlignment(self.groupBox_3, QtCore.Qt.AlignTop)
        self.contentsLayout.setAlignment(self.groupBox_4, QtCore.Qt.AlignTop)


        self.log = logging.getLogger('BookOForm')

        self.setup_model()
        self.setup_fields()

        # associate present flag
        self._associate_id = None
        # book internals
        self._book_list = []
        self._total = 0.0

        # flag to indicate whether there were changes to the fields
        self._dirty = False

    def is_dirty(self):
        return self._dirty

    def setup_model(self):
        db = Db_Instance("oform_book").get_instance()
        if not db.open():
            self.log.error(db.lastError().text())
            message = unicode("Erro de conexão\n\n""Banco de dados indisponível".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Livraria", message)
        else:
            # book order
            self._model = QSqlTableModel(self, db=db)
            self._model.setTable("book_order")
            # book order items
            self._items_model = QSqlTableModel(self, db=db)
            self._items_model.setTable("book_order_item")

    def setup_fields(self):
        """ setting up validators and stuff """
        # validators
        self.edBarcode.setValidator(NumericValidator())
        # hiding associate frame and clean button
        self.frameAssociate.setVisible(False)
        self.btnCleanAssociate.setVisible(False)
        # detect changes on edBarcode for dirtiness and completion
        self.edBarcode.textChanged.connect(self.check_changes)
        self.edBarcode.textChanged.connect(self.check_barcode)

    def check_changes(self, txt):
        if txt != '':
            self._dirty = True

    def check_barcode(self, txt):
        if len(txt) == self.edBarcode.maxLength():
            db = Db_Instance("obook_barcode_search").get_instance()
            try:
                if db.open():
                    query = QSqlQuery(db)
                    query.prepare("SELECT * FROM book WHERE barcode = :barcode")
                    query.bindValue(":barcode", txt)
                    query.exec_()
                    if query.next():
                        self.add_book_from_record(query.record())
                        self.edBarcode.clear()
                    else:
                        raise RecordNotFoundException
                else:
                    raise DbUnavailableException
            except RecordNotFoundException:
                message = unicode("Código de barra inválido!\n\n"""
                              "O código informado não corresponde a nenhum livro cadastrado".decode('utf-8'))
                QMessageBox.critical(self, "Seareiros - Livraria", message)
            except DbUnavailableException:
                self.log.error(db.lastError().text())
                message = unicode("Erro de conexão\n\n""Banco de dados indisponível".decode('utf-8'))
                QMessageBox.critical(self, "Seareiros - Livraria", message)
            self.edBarcode.setFocus()

    def submit_data(self):
        if len(self._book_list) == 0:
            message = unicode("Venda vazia!\n\n"""
                              "É necessário adicionar um livro antes de concluir uma venda".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Livraria", message)
            self.edBarcode.setFocus()
            return False
        data = self.extract_input()
        # filling a book order
        self._model.insertRow(0)
        for key,val in data.items():
            self._model.setData(self._model.index(0, self.column[key]), val)
        order_id = submit_and_get_id(self, self._model, self.log)
        if order_id:
            # order creation success, placing items
            error = False
            for item in self._book_list:
                book_id = item[0]
                book_quantity = item[3]
                self._items_model.insertRow(0)
                self._items_model.setData(self._items_model.index(0,1), order_id)
                self._items_model.setData(self._items_model.index(0,2), book_id)
                self._items_model.setData(self._items_model.index(0,3), book_quantity)
                ok = self._items_model.submitAll()
                if not ok:
                    error = True
                    break
            if error:
                self.log.error(self._items_model.lastError().text())
                message = unicode("Erro\n\n""Venda registrada e contabilizada, porém ocorreu um problema e"
                              " não será possível visualizar seus itens.".decode('utf-8'))
                QMessageBox.warning(self, "Seareiros - Livraria", message)
                return False
            else:
                # all went fine
                # retrieving some brief info of the order to display at the main window
                if 'associate' in data:
                    desc = "Venda da livraria no valor de R$ %s para %s" % \
                           (self._locale.toString(data['total'], 'f', 2).replace('.',''), self.lblNickname.text())
                else:
                    desc = "Venda da livraria no valor de R$ %s" % self._locale.toString(data['total'], 'f', 2).replace('.','')
                if not log_to_history(self._model.database(), "venda_livraria", order_id, desc):
                    self.log.error(self._model.lastError().text())
                message = unicode("Sucesso!\n\n""Venda concluída.".decode('utf-8'))
                QMessageBox.information(self, "Seareiros - Livraria", message)
                return True
        # failed to insert a row
        return False

    def clear(self):
        """ Globally cleans this form """
        self._dirty = False
        for lineEdit in self.findChildren(QLineEdit):
            lineEdit.clear()
        # book
        self.clear_table()
        self.lblTotal.setText("0,00")
        # associate
        self.clear_associate()

        self.edBarcode.setFocus()

    def clear_associate(self):
        # resets associate frame
        self.lblName.clear()
        self.lblNickname.clear()
        self._associate_id = None
        self.frameAssociate.setVisible(False)
        self.btnCleanAssociate.setVisible(False)
        # can't allow an order to be paid later without an associate to relate to
        self.rdNotPaid.setEnabled(False)
        self.rdPaid.setChecked(True)

    @QtCore.Slot()
    def on_btnSelectAssociate_clicked(self):
        associate_dialog = AssociateSelectDialog()
        if associate_dialog.exec_() == QDialog.Accepted:
            record = associate_dialog.get_record()
            self._associate_id = record.value("id")
            self.set_associate_info(record.value("fullname"), record.value("nickname"))
            self.frameAssociate.setVisible(True)
            self.btnCleanAssociate.setVisible(True)
            # a registered associate can pay later
            self.rdNotPaid.setEnabled(True)
            self.edBarcode.setFocus()

    @QtCore.Slot()
    def on_btnSelectBook_clicked(self):
        book_dialog = BookSelectDialog()
        if book_dialog.exec_() == QDialog.Accepted:
            record = book_dialog.get_record()
            self.add_book_from_record(record)

    def add_book_from_record(self, record):
        book_id = record.value("id")
        book_title = record.value("title")
        book_price = record.value("price")
        book_quantity = 1
        book_stock = record.value("stock")
        data = [book_id, book_title, book_price, book_quantity, book_stock]
        try:
            self.add_book(data)
            self.refresh_tableBooks()
            self.edBarcode.clear()
            self.edBarcode.setFocus()
        except StockOverflowException:
            message = unicode("Estoque Insuficiente!\n\n""A quantidade do item excedeu o estoque".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Livraria", message)

    def set_associate_info(self, fullname, nickname):
        self.lblName.setText(fullname)
        self.lblNickname.setText(nickname)

    @QtCore.Slot()
    def on_btnCleanAssociate_clicked(self):
        self.clear_associate()

    def update_total(self, price, add=True):
        if add:
            self._total += price
        else:
            self._total -= price
        txt = self._locale.toString(self._total, 'f', 2).replace('.','')
        if txt == '0':
            txt = txt.replace(txt, "0,00")
        self.lblTotal.setText(txt)

    @QtCore.Slot()
    def on_btnCleanBooks_clicked(self):
        self.clear_table()
        self._total = 0.0
        self.update_total(0.0)
        self.edBarcode.clear()
        self.edBarcode.setFocus()

    def clear_table(self):
        self._book_list = []
        self.tableBooks.clear()
        self.refresh_tableBooks()

    def add_book(self, data):
        """ adds a book to the list then sort it """
        # checking for duplicate
        dup_index = [i for i,x in enumerate(self._book_list) if x[0] == data[0]]
        if not dup_index:
            # not a duplicate
            self._book_list.append(data)
        else:
            # duplicate
            idx = dup_index[0]
            # increment quantity
            new_quantity = self._book_list[idx][3] + 1
            stock = self._book_list[idx][4]
            if new_quantity > stock:
                raise StockOverflowException
            else:
                self._book_list[idx][3] += 1
        self.update_total(data[2], add=True)
        # sorts by title
        self._book_list.sort(key=operator.itemgetter(1))

    def refresh_tableBooks(self):
        if len(self._book_list) > 0:
            self.tableBooks.setColumnCount(len(self._book_list[0])-1)
            col_labels = ["Livro", unicode("Preço (R$)".decode('utf-8')), "Qtd", ""]
            self.tableBooks.setHorizontalHeaderLabels(col_labels)
        else:
            self.tableBooks.setColumnCount(0)
        self.tableBooks.setRowCount(len(self._book_list))
        for i, row in enumerate(self._book_list):
            for j, col in enumerate(row):
                if j == 1:
                    # title
                    item = QTableWidgetItem(col)
                elif j == 2:
                    # price
                    item = QTableWidgetItem(self._locale.toString(col, 'f', 2).replace('.',''))
                elif j == 3:
                    # quantity
                    edQuantity = ReturnKeySpinBox(self)
                    edQuantity.setMinimum(1)
                    edQuantity.setMaximum(row[4])
                    edQuantity.setValue(col)
                    edQuantity.valueChanged.connect(partial(self.update_quantity, book=row))
                    self.tableBooks.setCellWidget(i, j-1, edQuantity)
                if j in [1,2]:
                    # ignoring id
                    self.tableBooks.setItem(i, j-1, item)
            # remove button on last column
            remove_icon = QIcon(":icons/conn_failed.png")
            remove_btn = QPushButton(remove_icon, "")
            remove_btn.clicked.connect(partial(self.remove_book, book=row))
            self.tableBooks.setCellWidget(i, len(row)-2, remove_btn)
        self.tableBooks.resizeColumnsToContents()
        self.tableBooks.horizontalHeader().setResizeMode(0, QHeaderView.Stretch)

    def remove_book(self, book):
        # remove a row based on its value
        subtract_value = book[2] * book[3]
        self._book_list.remove(book)
        self.refresh_tableBooks()
        self.update_total(subtract_value, add=False)

    def update_quantity(self, i, book):
        new_value = i
        old_value = book[3]
        if old_value == new_value:
            # this happens sometimes when refreshing the table
            return
        price = book[1]
        index = self._book_list.index(book)
        book[3] = new_value
        self._book_list[index] = book
        if new_value > old_value:
            # incremented
            self.update_total((new_value - old_value)*book[2], add=True)
        elif new_value < old_value:
            # decremented
            self.update_total((old_value - new_value)*book[2], add=False)

    def extract_input(self):
        data = {}
        if self._associate_id:
            data['associate'] = self._associate_id
        data['obs'] = self.edObs.toPlainText()
        data['total'] = self._total
        if self.rdPaid.isChecked():
            data['paid'] = True
        else:
            data['paid'] = False
        return data
