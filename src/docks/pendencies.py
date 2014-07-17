# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QDockWidget, QSortFilterProxyModel
from src.lib.ui.ui_pendencies import Ui_Dock
from src.models.model_associate_defaulter import DefaulterTableModel

class PendenciesDock(QDockWidget, Ui_Dock):
    """ Interface for pendencies viewing """

    def __init__(self, parent=None):
        super(PendenciesDock, self).__init__(parent)
        self.setupUi(self)
        self.tableView.setSortingEnabled(True)
        self._model = DefaulterTableModel()
        self._proxy = QSortFilterProxyModel()
        self._proxy.setSourceModel(self._model)

        self.visibilityChanged.connect(self.toggle_visibility)

        self.tableView.setModel(self._proxy)
        self.initialLoad()

    def initialLoad(self):
        self._model.modelReset.connect(self.setup_view)
        self.refresh()

    def refresh(self):
        self._model.load()

    def setup_view(self):
        self.tableView.setColumnHidden(self._model.ID, True)
        self.resize_columns()
        self.tableView.selectRow(0)

    def resize_columns(self):
        self.tableView.resizeColumnsToContents()

    def toggle_visibility(self, visible):
        actionPendencies = self.parent().parent().actionPendencies
        if visible:
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

    @QtCore.Slot(QtCore.QModelIndex)
    def on_tableView_doubleClicked(self, index):
        source_index = self._proxy.mapToSource(index)
        record = self._model.get_record(source_index.row())
