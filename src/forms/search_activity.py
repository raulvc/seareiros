# -*- coding: UTF-8 -*-
from PySide import QtCore
from src.forms.generic_search import GenericSearchForm
from src.models.model_activity import ActivityTableModel


class ActivitySearchForm(GenericSearchForm):
    """ Search form for activities """

    def __init__(self, parent=None):
        super(ActivitySearchForm, self).__init__(ActivityTableModel(), parent)
        self.viewSearch.setColumnHidden(self._model.ID, True)

    @QtCore.Slot(str)
    def on_edKeyword_textChanged(self, text):
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        # Will change this to param searching futurely
        self._proxy.setFilterKeyColumn(1)
        self._proxy.setFilterRegExp(search)