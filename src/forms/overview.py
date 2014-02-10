# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QDockWidget
from src.lib.ui.ui_overview import Ui_Dock
from src.models.model_overview import OverviewTableModel


class OverviewDock(QDockWidget, Ui_Dock):
    """ Interface for book input """

    def __init__(self, parent=None):
        super(OverviewDock, self).__init__(parent)
        self.setupUi(self)
        self._model = OverviewTableModel()
        self.tableView.setModel(self._model)
        self.initialLoad()

    def initialLoad(self):
        self._model.modelReset.connect(self.setup_view)
        self.dateEdit.setDate(QtCore.QDate.currentDate())

    def setup_view(self):
        self.tableView.setColumnHidden(self._model.ID, True)
        self.resize_columns()
        #self.tableView.setFocus()
        self.tableView.selectRow(self._model.rowCount() - 1)

    def resize_columns(self):
        self.tableView.resizeColumnsToContents()

    @QtCore.Slot(QtCore.QDate)
    def on_dateEdit_dateChanged(self, date):
        self._model.load(date)

    @QtCore.Slot(QtCore.QModelIndex)
    def on_tableView_doubleClicked(self, index):
        record = self._model.get_record(index.row())
        record_type = record.value(self._model.TYPE)
        record_id = record.value(self._model.ID)

        print record_type
        print record_id
