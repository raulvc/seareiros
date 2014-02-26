# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtCore import Signal
from PySide.QtGui import QMainWindow, QStackedWidget, QLabel, QMessageBox

from src.docks.dock_add_activity import AddActivityDock
from src.docks.dock_add_associate import AddAssociateDock
from src.docks.overview import OverviewDock
from src.lib.ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main interface"""

    # Custom Signals
    dock_destroyed = Signal(str)

    def __init__(self, username, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        message = QLabel(unicode("Usuário: ".decode('utf-8')) + username)
        self.statusbar.addWidget(message)
        self._docks = []
        self._stackedWidget = QStackedWidget()
        self.setCentralWidget(self._stackedWidget)
        self._overview = OverviewDock()
        self._stackedWidget.addWidget(self._overview)

    @QtCore.Slot()
    def on_actionExit_activated(self):
        self.close()

    # @QtCore.Slot()
    # def on_actionAddBook_activated(self):
    #     self.show_on_top(AddBookDock, self.actionAddBook)

    @QtCore.Slot()
    def on_actionAddAssociate_activated(self):
        self.show_on_top(AddAssociateDock, self.actionAddAssociate)

    @QtCore.Slot()
    def on_actionAddActivity_activated(self):
        self.show_on_top(AddActivityDock, self.actionAddActivity)

    # @QtCore.Slot()
    # def on_actionAddProduct_activated(self):
    #     self.show_on_top(AddProductDock, self.actionAddProduct)

    def show_on_top(self, widget_type, related_action):
        """ makes the dock related to 'widget_type' the central widget of the mainwindow
            (by stacking it on front of other widgets), grays out respective action while visible """
        related_action.setDisabled(True)
        widget = self.get_instance(widget_type)
        if widget is None:
            widget = widget_type()
            self._docks.append(widget)
            self._stackedWidget.addWidget(widget)
        # else:
        #     widget.clear()

        # connects a connection cleanup method when needed
        if hasattr(widget, 'cleanup_conn'):
            widget.cleanup_conn.connect(self.clean_connection)
        self._stackedWidget.setCurrentWidget(widget)

    def get_instance(self, type):
        for inst in self._docks:
            if isinstance(inst, type):
                return inst
        return None

    def remove_instance(self, inst):
        self._docks.remove(inst)
        self._stackedWidget.removeWidget(inst)
        self._stackedWidget.setCurrentWidget(self._overview)

    def closeEvent(self, event):
        message = unicode("Deseja mesmo sair?".decode('utf-8'))
        reply = QMessageBox.question(self, 'Seareiros', message, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



