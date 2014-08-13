# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QMessageBox
from src.docks.dock_generic import GenericDock


class OrderDock(GenericDock):
    """ Common interface for ordering docks """

    def __init__(self, parent=None):
        super(OrderDock, self).__init__(parent)
        # self.tabWidget.setStyleSheet("QTabBar { color : blue; }")
        # hide the second tab
        self.tabWidget.setTabText(self.ADD, "Nova Venda")
        self.tabWidget.setTabText(self.SEARCH, "Vendas Anteriores")
        self.btnSave.setText("Vender")
        # self.btnClear.setVisible(False)

    @QtCore.Slot()
    def on_btnSave_clicked(self):
        ok = self._addForm.submit_data()
        if ok:
            self._addForm._dirty = False
            self.close()

    @QtCore.Slot()
    def on_btnCancel_clicked(self):
        if not self._addForm.is_dirty():
            self.close()
        else:
            message = unicode("Descartar dados não salvos e sair?".decode('utf-8'))
            reply = QMessageBox.question(self, "Seareiros" + message,
                                         message, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self._addForm._dirty = False
                self.close()

    @QtCore.Slot()
    def on_btnClear_clicked(self):
        self._addForm.clear()

    def closeEvent(self, event):
        if not self._addForm.is_dirty():
            super(OrderDock, self).closeEvent(event)
            event.accept()
        else:
            message = unicode("A venda ainda não foi registrada, sair mesmo assim?".decode('utf-8'))
            reply = QMessageBox.question(self, 'Seareiros', message, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                super(OrderDock, self).closeEvent(event)
                event.accept()
            else:
                event.ignore()