# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QDockWidget, QHeaderView
from src.lib.table_util import CustomSortFilterProxyModel
from src.lib.ui.ui_pendencies import Ui_Dock
from src.models.model_associate_defaulter import DefaulterTableModel

class PendenciesDock(QDockWidget, Ui_Dock):
    """ Interface for pendencies viewing """

    def __init__(self, parent=None):
        super(PendenciesDock, self).__init__(parent)
        self.setupUi(self)
        self.tableView.setSortingEnabled(True)
        self._model = DefaulterTableModel()
        self._proxy = CustomSortFilterProxyModel()
        self._proxy.setSourceModel(self._model)
        self._proxy.set_filter_columns([1,2,3])

        self.visibilityChanged.connect(self.toggle_visibility)

        self.tableView.setModel(self._proxy)
        # having problem moving sections, had to flag it
        self.__first_load = True
        self._model.modelReset.connect(self.setup_view)

    def refresh(self):
        self._model.load()

    def setup_view(self):
        self.tableView.setColumnHidden(self._model.ID, True)
        # Debt should be the first column
        # (I could do it on the model but I wouldn't be able to subclass and use the parent there)
        if self.__first_load:
            self.__first_load = False
            self.tableView.horizontalHeader().moveSection(8,0)
        self.resize_columns()
        self.tableView.selectRow(0)

    def resize_columns(self):
        self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setResizeMode(1, QHeaderView.Stretch)

    def toggle_visibility(self, visible):
        actionPendencies = self.parent().parent().actionPendencies
        if visible:
            self.refresh()
            actionPendencies.setEnabled(False)
            self.edKeyword.setFocus()
        else:
            actionPendencies.setEnabled(True)

    def closeEvent(self, event):
        self.toggle_visibility(False)
        grandparent = self.parent().parent()
        grandparent.remove_instance(self)

    @QtCore.Slot()
    def on_btnRefresh_clicked(self):
        self.refresh()

    @QtCore.Slot(str)
    def on_edKeyword_textChanged(self, text):
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        self._proxy.setFilterRegExp(search)

    @QtCore.Slot(QtCore.QModelIndex)
    def on_tableView_doubleClicked(self, index):
        source_index = self._proxy.mapToSource(index)
        record = self._model.get_record(source_index.row())
        print record
