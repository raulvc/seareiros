# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QDockWidget
from src.lib.ui.ui_generic_dock import Ui_Dock


class GenericDock(QDockWidget, Ui_Dock):
    """ Common interface for docks """

    ADD, SEARCH = range(2)

    def __init__(self, parent=None):
        super(GenericDock, self).__init__(parent)
        self.setupUi(self)

        # setup both tabs
        self.setup_add()
        self.setup_search()

        self.visibilityChanged.connect(self.toggle_visibility)

    # overwritten in child
    def setup_add(self):
        pass

    # overwritten in child
    def setup_search(self):
        pass

    # overwritten in child
    def toggle_visibility(self, visible):
        pass

    def closeEvent(self, event):
        self.toggle_visibility(False)
        grandparent = self.parent().parent()
        grandparent.remove_instance(self)

    @QtCore.Slot(int)
    def on_tabWidget_currentChanged(self, index):
        if index == self.SEARCH:
            self._searchForm.refresh()
