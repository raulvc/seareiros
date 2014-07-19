# -*- coding: UTF-8 -*-
from PySide import QtCore
from src.docks.dock_generic import GenericDock


class EditDock(GenericDock):
    """ Common interface for editing docks """

    def __init__(self, parent=None):
        super(EditDock, self).__init__(parent)
        self.tabWidget.setTabText(0, unicode("Modo de Edição".decode('utf-8')))
        # hide the second tab
        self.tabWidget.removeTab(1)
        self.btnSave.setText("Atualizar")
        self.btnClear.setVisible(False)

    # overwritten in child
    def setup_edit(self):
        pass