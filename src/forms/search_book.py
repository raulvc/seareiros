# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QApplication, QMainWindow
from src.docks.dock_edit_book import EditBookDock
from src.forms.search_generic import GenericSearchForm
from src.lib import constants
from src.models.model_book import BookTableModel


class BookSearchForm(GenericSearchForm):
    """ Search form for books """

    def __init__(self, parent=None, editable=False, dm=constants.BOOK_ALL):
        self.dm = dm
        super(BookSearchForm, self).__init__(BookTableModel(display_mode=self.dm), parent)
        self._editable = editable

    def setup_view(self):
        if self.dm == constants.BOOK_SELL:
            self.viewSearch.hideColumn(self._model.AVAILABILITY)
        self._proxy.set_filter_columns([1,2,3])
        self.viewSearch.sortByColumn(self._model.TITLE, QtCore.Qt.AscendingOrder)
        self.resize_columns()
        self.viewSearch.selectRow(0)

    @QtCore.Slot(str)
    def on_edKeyword_textChanged(self, text):
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        # Will change this to param searching futurely
        self._proxy.setFilterKeyColumn(self._model.TITLE)
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
        main.show_on_top(EditBookDock, param=id)

