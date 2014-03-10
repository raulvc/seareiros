# -*- coding: UTF-8 -*-
from PySide import QtCore
from src.forms.search_generic import GenericSearchForm
from src.models.model_associate import AssociateTableModel


class AssociateSearchForm(GenericSearchForm):
    """ Search form for associates """

    def __init__(self, parent=None):
        super(AssociateSearchForm, self).__init__(AssociateTableModel(), parent)

    def setup_view(self):
        self.viewSearch.sortByColumn(self._model.FULLNAME, QtCore.Qt.AscendingOrder)
        self.viewSearch.setColumnHidden(self._model.ID, True)
        self.resize_columns()
        self.viewSearch.selectRow(0)

    @QtCore.Slot(str)
    def on_edKeyword_textChanged(self, text):
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        # Will change this to param searching futurely
        self._proxy.setFilterKeyColumn(self._model.FULLNAME)
        self._proxy.setFilterRegExp(search)