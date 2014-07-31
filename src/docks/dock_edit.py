# -*- coding: UTF-8 -*-
from PySide.QtGui import QLabel, QMessageBox
from src.docks.dock_generic import GenericDock


class EditDock(GenericDock):
    """ Common interface for editing docks """

    def __init__(self, parent=None):
        super(EditDock, self).__init__(parent)
        self.tabWidget.setStyleSheet("QTabBar { color : blue; }")
        # hide the second tab
        self.tabWidget.removeTab(1)
        self.btnSave.setText("Atualizar")
        self.btnClear.setVisible(False)

    def set_label_id(self, id):
        self.tabWidget.setTabText(0, unicode("Registro:".decode('utf-8')) + str(id))

    # overwritten in child
    def setup_edit(self):
        pass

    def closeEvent(self, event):
        if not self._editForm.is_dirty():
            super(EditDock, self).closeEvent(event)
            event.accept()
        else:
            message = unicode("Descartar dados não salvos e sair?".decode('utf-8'))
            reply = QMessageBox.question(self, 'Seareiros', message, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                super(EditDock, self).closeEvent(event)
                event.accept()
            else:
                event.ignore()