# -*- coding: UTF-8 -*-

from PySide import QtCore
from PySide.QtGui import QWidget, QSortFilterProxyModel
from src.lib.ui.ui_generic_search import Ui_SearchForm

class GenericSearchForm(QWidget, Ui_SearchForm):
    """ Common interface for search forms """

    def __init__(self, model, parent=None):
        super(GenericSearchForm, self).__init__(parent)
        self.setupUi(self)

        self.viewSearch.setSortingEnabled(True)
        self._model = model
        self._proxy = QSortFilterProxyModel()
        self._proxy.setSourceModel(self._model)
        self.viewSearch.setModel(self._proxy)
        self.initialLoad()

    def initialLoad(self):
        self._model.modelReset.connect(self.setup_view)

    def setup_view(self):
        self.resize_columns()
        self.viewSearch.selectRow(0)

    def resize_columns(self):
        self.viewSearch.resizeColumnsToContents()

    def refresh(self):
        self._model.load()

    @QtCore.Slot()
    def on_btnRefresh_clicked(self):
        self.refresh()
        self.edKeyword.setFocus()

    @QtCore.Slot(str)
    def on_edKeyword_textChanged(self, text):
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        self._proxy.setFilterRegExp(search)

    # @QtCore.Slot(QtCore.QModelIndex)
    # def on_tableView_doubleClicked(self, index):
    #     record = self._model.get_record(index.row())
    #     record_id = record.value(self._model.ID)