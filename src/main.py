# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtCore import Signal
from PySide.QtGui import QMainWindow
from src.forms.add_book import AddBookDock
from src.lib.ui.ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """Main interface"""

    # Custom Signals
    dock_destroyed = Signal(str)

    def __init__(self, username, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.statusbar.showMessage(unicode("Usuário: ".decode('utf-8')) + username)
        self._docks = []

    @QtCore.Slot()
    def on_actionExit_activated(self):
        self.close()

    @QtCore.Slot()
    def on_actionAddBook_activated(self):
        print self._docks
        addBook = self.get_instance(AddBookDock)
        if addBook is None:
            addBook = AddBookDock()
            self._docks.append(addBook)
        else:
            addBook.clear()
        self.actionAddBook.setDisabled(True)
        self.setCentralWidget(addBook)
        addBook.show()

    def get_instance(self, type):
        for inst in self._docks:
            if isinstance(inst, type):
                return inst
        return None

    def remove_instance(self, inst):
        self._docks.remove(inst)




