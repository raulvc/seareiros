# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QStackedWidget, QIcon
from src.dialogs.select_generic import GenericSelect
from src.forms.add_activity import ActivityForm
from src.forms.search_activity import ActivitySearchForm

class ActivitySelectDialog(GenericSelect):
    """ Dialog for selecting an activity """

    def __init__(self, parent=None):
        super(ActivitySelectDialog, self).__init__(parent)
        self.setWindowTitle("Seleçionar Atividade")
        self.setWindowIcon(QIcon(":icons/activity.png"))

    def setup_add(self):
        self._addForm = ActivityForm()
        self._addForm.show()
        self._stackedWidget.addWidget(self._addForm)

    def setup_search(self):
        self._searchForm = ActivitySearchForm()
        self._searchForm.show()
        self._stackedWidget.addWidget(self._searchForm)

    def toggle_function(self):
        """ swaps functionality """
        super(ActivitySelectDialog, self).toggle_function()
        if self._function == self.SEARCH:
            self.btnToggleFuncion.setIcon(QIcon(":icons/activity_add.png"))
            self._searchForm.edKeyword.setFocus()
        else:
            self._addForm.comboDescription.setFocus()
