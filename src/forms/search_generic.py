# -*- coding: UTF-8 -*-

from PySide import QtCore
from PySide.QtGui import QWidget, QHeaderView

from src.lib.table_util import CustomSortFilterProxyModel
from src.lib.ui.ui_generic_search import Ui_SearchForm


class GenericSearchForm(QWidget, Ui_SearchForm):
    """ Common interface for search forms """

    def __init__(self, model, parent=None):
        super(GenericSearchForm, self).__init__(parent)
        self.setupUi(self)

        self.viewSearch.setSortingEnabled(True)
        self._model = model
        self._proxy = CustomSortFilterProxyModel()
        self._proxy.setSourceModel(self._model)
        self.viewSearch.setModel(self._proxy)
        self.initialLoad()
        self._record = None

    def initialLoad(self):
        self._model.modelReset.connect(self.setup_view)

    def setup_view(self):
        self.resize_columns()
        self.viewSearch.selectRow(0)

    def resize_columns(self):
        self.viewSearch.resizeColumnsToContents()
        self.viewSearch.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        # for some reason developers made resizemode options all mutually exclusive, you can't
        # stretch columns to fill up the widget AND be able to resize them without this
        for col in range(self.viewSearch.horizontalHeader().count()-1):
            self.viewSearch.horizontalHeader().setResizeMode(col, QHeaderView.Interactive)

    def refresh(self):
        self._model.load()

    def get_record_at(self, index):
        source_index = self._proxy.mapToSource(index)
        return self._model.get_record(source_index.row())

    def get_current_index(self):
        return self.viewSearch.currentIndex()

    @QtCore.Slot()
    def on_btnRefresh_clicked(self):
        self.refresh()
        self.edKeyword.setFocus()

    @QtCore.Slot(str)
    def on_edKeyword_textChanged(self, text):
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        self._proxy.setFilterRegExp(search)

    def resizeEvent(self, event):
        self.resize_columns()
        super(GenericSearchForm, self).resizeEvent(event)
