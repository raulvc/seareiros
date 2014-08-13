# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtCore import Signal
from PySide.QtGui import QMainWindow, QStackedWidget, QLabel, QMessageBox, QAction, QMenu

from src.docks.dock_add_activity import AddActivityDock
from src.docks.dock_add_associate import AddAssociateDock
from src.docks.dock_add_book import AddBookDock
from src.docks.dock_order_product import OrderProductDock
from src.docks.overview import OverviewDock
from src.docks.pendencies import PendenciesDock
from src.lib import statics
from src.lib.ui.ui_main import Ui_MainWindow
from src.lib.util import check_access


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main interface"""

    # Custom Signals
    dock_destroyed = Signal(str)

    def __init__(self, user_data, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        message = QLabel(unicode("Usuário: ".decode('utf-8')) + user_data[0])
        self.statusbar.addWidget(message)
        self._docks = []
        self._stackedWidget = QStackedWidget()
        self.setCentralWidget(self._stackedWidget)
        self._overview = OverviewDock()
        self._stackedWidget.addWidget(self._overview)
        self._edit_mode = False
        self._stackedWidget.currentChanged.connect(self.dock_changed)
        # permission stuff
        self.setup_access(user_data[1])

    def dock_changed(self, new_index):
        new_dock = self._stackedWidget.widget(new_index).objectName()
        if "Edit" in new_dock:
            # it's an editing dock
            self.set_editing(True)

    def set_editing(self, state):
        self._edit_mode = state

    def is_editing(self):
        return self._edit_mode

    def setup_access(self, access_level):
        statics.access_level = access_level
        # set availability for QAction objects
        for action in self.findChildren(QAction):
             action.setVisible(check_access(access_level, action.objectName()))
        for menu in self.findChildren(QMenu):
            if menu.isEmpty():
                # no visible actions under this menu
                menu.menuAction().setVisible(False)

    @QtCore.Slot()
    def on_actionExit_activated(self):
        self.close()

    @QtCore.Slot()
    def on_actionAddBook_activated(self):
        self.show_on_top(AddBookDock, self.actionAddBook)

    @QtCore.Slot()
    def on_actionAddAssociate_activated(self):
        self.show_on_top(AddAssociateDock, self.actionAddAssociate)

    @QtCore.Slot()
    def on_actionAddActivity_activated(self):
        self.show_on_top(AddActivityDock, self.actionAddActivity)

    @QtCore.Slot()
    def on_actionPendencies_activated(self):
        self.show_on_top(PendenciesDock, self.actionPendencies)

    @QtCore.Slot()
    def on_actionSellProduct_activated(self):
        self.show_on_top(OrderProductDock, self.actionSellProduct)


    # @QtCore.Slot()
    # def on_actionAddProduct_activated(self):
    #     self.show_on_top(AddProductDock, self.actionAddProduct)

    def show_on_top(self, widget_type, related_action=None, param=None):
        """ makes the dock related to 'widget_type' the central widget of the mainwindow
            (by stacking it on front of other widgets), grays out respective action while visible """
        if self.is_editing():
            # edit dock is being swapped out
            message = unicode("Todos os dados não salvos serão perdidos".decode('utf-8'))
            reply = QMessageBox.warning(self, unicode("Atenção".decode('utf-8')), message, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.No:
                return
            else:
                self.remove_instance(self._stackedWidget.currentWidget())
        # there's a need to gray out the corresponding menu option
        if related_action:
            related_action.setDisabled(True)
        widget = self.get_instance(widget_type)
        if widget is None:
            # create a new instance of referenced widget if it doesn't exist yet
            if param:
                # when a parameter is passed
                widget = widget_type(param)
            else:
                widget = widget_type()
            self._docks.append(widget)
            self._stackedWidget.addWidget(widget)
        # else:
        #     widget.clear()

        # connects a connection cleanup method when needed
        # if hasattr(widget, 'cleanup_conn'):
        #     widget.cleanup_conn.connect(self.clean_connection)
        self._stackedWidget.setCurrentWidget(widget)

    def get_instance(self, type):
        for inst in self._docks:
            if isinstance(inst, type):
                return inst
        return None

    def remove_instance(self, inst):
        if self.is_editing():
            self.set_editing(False)
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



