# -*- coding: UTF-8 -*-

from functools import partial
import logging
import operator

from PySide import QtCore
from PySide.QtCore import QLocale
from PySide.QtGui import QMessageBox, QLineEdit, QScrollArea, QTableWidgetItem, QPushButton, QIcon, \
    QHeaderView, QDialog
from PySide.QtSql import QSqlTableModel
from src.dialogs.select_associate import AssociateSelectDialog

from src.lib import statics

from src.lib.ui.ui_oform_product import Ui_ProductOForm
from src.lib.util import ReturnKeySpinBox
from src.lib.validators import UppercaseValidator, CurrencyValidator
from src.lib.db_util import Db_Instance, submit_and_get_id, log_to_history


logger = logging.getLogger('order_product')

class ProductOrderForm(QScrollArea, Ui_ProductOForm):
    """ Interface for ordering products """

    column = { 'associate':1, 'obs':3, 'total':4, 'paid':5 }


    def __init__(self, parent=None):
        super(ProductOrderForm, self).__init__(parent)
        self.setupUi(self)
        # had to subclass this spinbox to support return grabbing
        self.edQuantity = ReturnKeySpinBox(self)
        self.edQuantityHolder.addWidget(self.edQuantity)

        self._access = statics.access_level
        # for currency formatting
        self._locale = QLocale()

        # had to hardcode these, wouldn't work otherwise:
        self.contentsLayout.setAlignment(self.groupBox, QtCore.Qt.AlignTop)
        self.contentsLayout.setAlignment(self.groupBox_2, QtCore.Qt.AlignTop)
        self.contentsLayout.setAlignment(self.groupBox_3, QtCore.Qt.AlignTop)
        self.contentsLayout.setAlignment(self.groupBox_4, QtCore.Qt.AlignTop)


        self.log = logging.getLogger('ProductOForm')

        self.setup_model()
        self.setup_fields()

        # associate present flag
        self._associate_id = None
        # product internals
        self._product_list = []
        self._total = 0.0

        # flag to indicate whether there were changes to the fields
        self._dirty = False

    def is_dirty(self):
        return self._dirty

    def setup_model(self):
        db = Db_Instance("oform_product").get_instance()
        if not db.open():
            self.log.error(db.lastError().text())
            message = unicode("Erro de conexão\n\n""Banco de dados indisponível".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Vendas do Bazar", message)
        else:
            # product order
            self._model = QSqlTableModel(self, db=db)
            self._model.setTable("product_order")
            # product order items
            self._items_model = QSqlTableModel(self, db=db)
            self._items_model.setTable("product_order_item")

    def setup_fields(self):
        """ setting up validators and stuff """
        # validators
        self.edProductName.setValidator(UppercaseValidator())
        self.edPrice.setValidator(CurrencyValidator(self.edPrice))
        # hiding associate frame and clean button
        self.frameAssociate.setVisible(False)
        self.btnCleanAssociate.setVisible(False)
        # connecting return key to tab
        for lineEdit in self.findChildren(QLineEdit):
            # qspinbox has a C++ originated qlineedit "hidden" in it, we don't wanna mess with that
            if lineEdit.objectName() != 'qt_spinbox_lineedit':
                lineEdit.returnPressed.connect(lineEdit.focusNextChild)
                # detect changes on line edits
                lineEdit.textChanged.connect(self.check_changes)
        self.edQuantity.setMinimum(1)
        self.edQuantity.setMaximum(2000)
        self.edQuantity.setValue(1)
        # fixing tab order
        self.setTabOrder(self.edPrice, self.edQuantity)
        self.setTabOrder(self.edQuantity, self.btnAddProduct)

    def check_changes(self, txt):
        if txt != '':
            self._dirty = True

    def submit_data(self):
        # I should block empty orders I guess
        if len(self._product_list) == 0:
            message = unicode("Venda vazia!\n\n"""
                              "É necessário adicionar um produto antes de concluir uma venda".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Vendas do Bazar", message)
            self.edProductName.setFocus()
            return False
        data = self.extract_input()
        # filling a product order
        self._model.insertRow(0)
        for key,val in data.items():
            self._model.setData(self._model.index(0, self.column[key]), val)
        order_id = submit_and_get_id(self, self._model, self.log)
        if order_id:
            # order creation success, placing items
            error = False
            for item in self._product_list:
                product_name = item[0]
                product_price = item[1]
                product_quantity = item[2]
                self._items_model.insertRow(0)
                self._items_model.setData(self._items_model.index(0,1), order_id)
                self._items_model.setData(self._items_model.index(0,2), product_name)
                self._items_model.setData(self._items_model.index(0,3), product_price)
                self._items_model.setData(self._items_model.index(0,4), product_quantity)
                ok = self._items_model.submitAll()
                if not ok:
                    error = True
                    break
            if error:
                self.log.error(self._items_model.lastError().text())
                message = unicode("Erro\n\n""Venda registrada e contabilizada, porém ocorreu um problema e"
                              " não será possível visualizar seus itens.".decode('utf-8'))
                QMessageBox.warning(self, "Seareiros - Vendas do Bazar", message)
                return False
            else:
                # all went fine
                # retrieving some brief info of the order to display at the main window
                if 'associate' in data:
                    desc = "Venda do bazar no valor de R$ %s para %s" % \
                           (self._locale.toString(data['total'], 'f', 2).replace('.',''), self.lblNickname.text())
                else:
                    desc = "Venda do bazar no valor de R$ %s" % self._locale.toString(data['total'], 'f', 2).replace('.','')
                if not log_to_history(self._model.database(), "venda_bazar", order_id, desc):
                    self.log.error(self._model.lastError().text())
                message = unicode("Sucesso!\n\n""Venda concluída.".decode('utf-8'))
                QMessageBox.information(self, "Seareiros - Vendas do Bazar", message)
                return True
        # failed to insert a row
        return False

    def clear(self):
        """ Globally cleans this form """
        self._dirty = False
        for lineEdit in self.findChildren(QLineEdit):
            lineEdit.clear()
        # product
        # edProduct is a QLineEdit so... already clean
        self.clear_table()
        self.lblTotal.setText("0,00")
        self.edQuantity.setValue(1)
        # associate
        self.clear_associate()

        self.edProductName.setFocus()

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
    def on_btnAddProduct_clicked(self):
        txt = self.edProductName.text()
        price = self._locale.toDouble(self.edPrice.text())[0]
        quantity = self.edQuantity.value()
        if txt != '':
            data = [txt,price,quantity]
            self.add_product(data)
            self.update_total(price * quantity)
            self.refresh_tableProducts()
            # cleaning product related input
            self.edProductName.clear()
            self.edPrice.setText("0,00")
            self.edQuantity.setValue(1)
            self.edProductName.setFocus()

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
            self.edProductName.setFocus()

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
    def on_btnCleanProducts_clicked(self):
        self.clear_table()
        self._total = 0.0
        self.update_total(0.0)
        self.edPrice.setText("0,00")
        self.edQuantity.setValue(1)
        self.edProductName.clear()
        self.edProductName.setFocus()

    def clear_table(self):
        self._product_list = []
        self.tableProducts.clear()
        self.refresh_tableProducts()

    def add_product(self, data):
        """ adds a product to the list then sort it """
        self._product_list.append(data)
        # sorts by name
        self._product_list.sort(key=operator.itemgetter(0))

    def refresh_tableProducts(self):
        if len(self._product_list) > 0:
            self.tableProducts.setColumnCount(len(self._product_list[0])+1)
            col_labels = ["Produto", unicode("Preço (R$)".decode('utf-8')), "Qtd", ""]
            self.tableProducts.setHorizontalHeaderLabels(col_labels)
        else:
            self.tableProducts.setColumnCount(0)
        self.tableProducts.setRowCount(len(self._product_list))
        for i, row in enumerate(self._product_list):
            for j, col in enumerate(row):
                if j == 1:
                    # product price
                    item = QTableWidgetItem(self._locale.toString(col, 'f', 2).replace('.',''))
                elif j == 2:
                    # product quantity
                    item = QTableWidgetItem(str(col))
                else:
                    item = QTableWidgetItem(col)
                self.tableProducts.setItem(i, j, item)
            # icon to remove rows individually
            remove_icon = QIcon(":icons/conn_failed.png")
            remove_btn = QPushButton(remove_icon, "")
            remove_btn.clicked.connect(partial(self.remove_product, product=row))
            self.tableProducts.setCellWidget(i, len(row), remove_btn)
        self.tableProducts.resizeColumnsToContents()
        self.tableProducts.horizontalHeader().setResizeMode(0, QHeaderView.Stretch)

    def remove_product(self, product):
        # remove a row based on its value
        subtract_value = product[1] * product[2]
        self._product_list.remove(product)
        self.refresh_tableProducts()
        self.update_total(subtract_value, add=False)

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
