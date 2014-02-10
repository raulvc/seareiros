# -*- coding: UTF-8 -*-
from PySide.QtCore import QAbstractTableModel, Qt
from PySide.QtGui import QItemDelegate


class BookTableModel(QAbstractTableModel):
    """ Model for book objects """

    def __init__(self, parent=None):
        super(BookTableModel, self).__init__(parent)

    def loadData(self):
        pass

    def data(self, index, role):
        if not index.isValid() or not (0<=index.row()<self.rowCount()):
            # invalid index
            return None

    def _finished(self):
        self.endInsertRows()