# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QIcon
from src.docks.dock_generic import GenericDock
from src.forms.add_activity import ActivityForm
from src.forms.search_activity import ActivitySearchForm

class AddActivityDock(GenericDock):
    """ Interface for activity input """

    def __init__(self, parent=None):
        super(AddActivityDock, self).__init__(parent)
        self.setWindowTitle("Cadastro de Atividades")
        self.tabWidget.setTabIcon(self.ADD, QIcon(":icons/activity_add.png"))

    def setup_add(self):
        self._addForm = ActivityForm()
        self._addForm.show()
        self.addPlaceholder.addWidget(self._addForm)

    def setup_search(self):
        self._searchForm = ActivitySearchForm()
        self._searchForm.show()
        self.searchPlaceholder.addWidget(self._searchForm)

    @QtCore.Slot()
    def on_btnSave_clicked(self):
        ok = self._addForm.submit_data()
        if ok:
            self._addForm.clear()

    @QtCore.Slot()
    def on_btnCancel_clicked(self):
        self.close()

    @QtCore.Slot()
    def on_btnClear_clicked(self):
        self._addForm.clear()

    def toggle_visibility(self, visible):
        actionAddActivity = self.parent().parent().actionAddActivity
        if visible:
            super(AddActivityDock, self).toggle_visibility(visible)
            actionAddActivity.setEnabled(False)
            self._addForm.comboDescription.setFocus()
        else:
            actionAddActivity.setEnabled(True)
