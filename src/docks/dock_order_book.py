# -*- coding: UTF-8 -*-
from PySide.QtGui import QIcon, QApplication, QMainWindow
from src.docks.dock_order import OrderDock
from src.forms.order_book import BookOrderForm
from src.forms.osearch_book import BookOrderSearchForm


class OrderBookDock(OrderDock):
    """ Interface for book ordering """

    def __init__(self, parent=None):
        super(OrderBookDock, self).__init__(parent)
        self.setWindowTitle("Livraria")
        self.tabWidget.setTabIcon(self.ADD, QIcon(":icons/book_add.png"))

    def setup_add(self):
        self._addForm = BookOrderForm()
        self._addForm.show()
        self.addPlaceholder.addWidget(self._addForm)

    def setup_search(self):
        self._searchForm = BookOrderSearchForm()
        self._searchForm.show()
        self.searchPlaceholder.addWidget(self._searchForm)

    def toggle_visibility(self, visible):
        main = [main for main in QApplication.topLevelWidgets() if isinstance(main, QMainWindow)][0]
        actionOrderBook = main.actionSellBook
        if visible:
            super(OrderBookDock, self).toggle_visibility(visible)
            actionOrderBook.setEnabled(False)
            self._addForm.edBarcode.setFocus()
        else:
            actionOrderBook.setEnabled(True)
