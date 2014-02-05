# -*- coding: UTF-8 -*-
from PySide.QtGui import QDockWidget
from src.lib.ui.ui_overview import Ui_Dock


class OverviewDock(QDockWidget, Ui_Dock):
    """ Interface for book input """

    def __init__(self, parent=None):
        super(OverviewDock, self).__init__(parent)
        self.setupUi(self)