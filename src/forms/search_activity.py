# -*- coding: UTF-8 -*-
from PySide import QtCore

from src.forms.search_generic import GenericSearchForm
from src.models.model_activity import ActivityTableModel


class ActivitySearchForm(GenericSearchForm):
    """ Search form for activities """

    def __init__(self, parent=None):
        super(ActivitySearchForm, self).__init__(ActivityTableModel(), parent)

    def setup_view(self):
        self._proxy.set_filter_columns([1])
        self.viewSearch.sortByColumn(self._model.DESCRIPTION, QtCore.Qt.AscendingOrder)
        self.viewSearch.setColumnHidden(self._model.ID, True)
        self.resize_columns()
        self.viewSearch.selectRow(0)

    @QtCore.Slot(str)
    def on_edKeyword_textChanged(self, text):
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        # Will change this to param searching futurely
        self._proxy.setFilterKeyColumn(self._model.DESCRIPTION)
        self._proxy.setFilterRegExp(search)