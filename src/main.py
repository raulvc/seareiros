# -*- coding: UTF-8 -*-
from PySide.QtGui import QMainWindow, QTableView
from src.lib.ui.ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """Main interface"""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionExit.activated.connect(self.close)
        