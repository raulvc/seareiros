# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QIcon, QMessageBox, QApplication, QMainWindow
from src.docks.dock_order import OrderDock
from src.forms.order_product import ProductOrderForm
from src.forms.search_product import ProductSearchForm


class OrderProductDock(OrderDock):
    """ Interface for product ordering """

    def __init__(self, parent=None):
        super(OrderProductDock, self).__init__(parent)
        self.setWindowTitle("Vendas do Bazar")
        self.tabWidget.setTabIcon(self.ADD, QIcon(":icons/product_add.png"))

    def setup_add(self):
        self._addForm = ProductOrderForm()
        self._addForm.show()
        self.addPlaceholder.addWidget(self._addForm)

    def setup_search(self):
        self._searchForm = ProductSearchForm()
        self._searchForm.show()
        self.searchPlaceholder.addWidget(self._searchForm)

    def toggle_visibility(self, visible):
        main = [main for main in QApplication.topLevelWidgets() if isinstance(main, QMainWindow)][0]
        actionOrderProduct = main.actionSellProduct
        if visible:
            super(OrderProductDock, self).toggle_visibility(visible)
            actionOrderProduct.setEnabled(False)
            self._addForm.edProductName.setFocus()
        else:
            actionOrderProduct.setEnabled(True)
