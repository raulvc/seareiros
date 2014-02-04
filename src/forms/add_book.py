# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QDockWidget
from src.lib.ui.ui_add_book import Ui_Dock


class AddBookDock(QDockWidget, Ui_Dock):
    """ Interface for book input """

    def __init__(self, parent=None):
        super(AddBookDock, self).__init__(parent)
        self.setupUi(self)

    def clear(self):
        pass

    def closeEvent(self, sender):
        self.parent().actionAddBook.setDisabled(False)
        self.parent().remove_instance(self)