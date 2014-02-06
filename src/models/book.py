# -*- coding: UTF-8 -*-
from PySide.QtCore import QAbstractTableModel

class BookTableModel(QAbstractTableModel):
    """ Model for book objects """

    def __init__(self, parent=None):
        super(BookTableModel, self).__init__(parent)