# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QApplication, QMainWindow
from src.forms.search_generic import GenericSearchForm
from src.models.model_book import BookTableModel


class BookSearchForm(GenericSearchForm):
    """ Search form for associates """

    def __init__(self, parent=None, editable=False):
        super(BookSearchForm, self).__init__(BookTableModel(), parent)
        self._editable = editable

    def setup_view(self):
        self.viewSearch.sortByColumn(self._model.TITLE, QtCore.Qt.AscendingOrder)
        self.resize_columns()
        self.viewSearch.selectRow(0)

    @QtCore.Slot(str)
    def on_edKeyword_textChanged(self, text):
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        # Will change this to param searching futurely
        self._proxy.setFilterKeyColumn(self._model.TITLE)
        self._proxy.setFilterRegExp(search)

    # @QtCore.Slot(QtCore.QModelIndex)
    # def on_viewSearch_doubleClicked(self, index):
    #     # TODO: Permissions
    #     #if self._editable:
    #     source_index = self._proxy.mapToSource(index)
    #     record = self._model.get_record(source_index.row())
    #     id = record.value(0)
    #     # getting main window reference
    #     main = [main for main in QApplication.topLevelWidgets() if isinstance(main, QMainWindow)][0]
    #     main.show_on_top(EditBookDock, param=id)

