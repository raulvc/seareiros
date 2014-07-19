# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QApplication, QMainWindow
from src.docks.dock_edit_associate import EditAssociateDock
from src.forms.search_generic import GenericSearchForm
from src.models.model_associate import AssociateTableModel


class AssociateSearchForm(GenericSearchForm):
    """ Search form for associates """

    def __init__(self, parent=None, editable=False):
        super(AssociateSearchForm, self).__init__(AssociateTableModel(), parent)
        self._editable = editable

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

    @QtCore.Slot(QtCore.QModelIndex)
    def on_viewSearch_doubleClicked(self, index):
        # TODO: Permissions
        #if self._editable:
        source_index = self._proxy.mapToSource(index)
        record = self._model.get_record(source_index.row())
        id = record.value(0)
        # getting main window reference
        main = [main for main in QApplication.topLevelWidgets() if isinstance(main, QMainWindow)][0]
        main.show_on_top(EditAssociateDock, param=id)

