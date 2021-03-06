# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QIcon, QMessageBox
from src.docks.dock_generic import GenericDock
from src.forms.add_associate import AssociateAddForm
from src.forms.search_associate import AssociateSearchForm


class AddAssociateDock(GenericDock):
    """ Interface for associate input """

    def __init__(self, parent=None):
        super(AddAssociateDock, self).__init__(parent)
        self.setWindowTitle("Cadastro de Associados")
        self.tabWidget.setTabIcon(self.ADD, QIcon(":icons/associate_add.png"))

    def setup_add(self):
        self._addForm = AssociateAddForm()
        self._addForm.show()
        self.addPlaceholder.addWidget(self._addForm)

    def setup_search(self):
        self._searchForm = AssociateSearchForm()
        self._searchForm.show()
        self.searchPlaceholder.addWidget(self._searchForm)

    @QtCore.Slot()
    def on_btnSave_clicked(self):
        ok = self._addForm.submit_data()
        if ok:
            self._addForm.clear()

    @QtCore.Slot()
    def on_btnCancel_clicked(self):
        if not self._addForm.is_dirty():
            self.close()
        else:
            message = unicode("Descartar dados não salvos e sair?".decode('utf-8'))
            reply = QMessageBox.question(self, 'Seareiros - Cadastro de Associados',
                                         message, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.close()

    @QtCore.Slot()
    def on_btnClear_clicked(self):
        self._addForm.clear()

    def toggle_visibility(self, visible):
        actionAddAssociate = self.parent().parent().actionAddAssociate
        if visible:
            super(AddAssociateDock, self).toggle_visibility(visible)
            actionAddAssociate.setEnabled(False)
            self._addForm.edFullName.setFocus()
        else:
            actionAddAssociate.setEnabled(True)
