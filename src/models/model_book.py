# -*- coding: UTF-8 -*-

from PySide.QtCore import Qt
from src.models.model_base import BaseTableModel


class BookTableModel(BaseTableModel):
    """ Model for associate objects """

    ID, TITLE, AUTHOR, S_AUTHOR, PRICE, STOCK = range(6)

    def __init__(self, parent=None):
        super(BookTableModel, self).__init__(parent)
        self._sql_statement = "SELECT b.id, b.title, a.name, s_a.name, b.price, b.stock " \
                        "FROM book b, author a, s_author s_a " \
                        "WHERE b.author_id = a.id AND b.s_author_id = s_a.id"
        self._name = "populate_book"

    def load(self):
        self.set_query_info(self._name, self._sql_statement)
        super(BookTableModel, self).load()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0<=index.row()<self.rowCount()):
            # invalid index
            return None

        record = self.get_record(index.row())
        column = index.column()
        if role == Qt.DisplayRole:
            if column == self.ID:
                return record.value("id")
            elif column == self.TITLE:
                return record.value("title")
            elif column == self.AUTHOR:
                return record.value("author")
            elif column == self.S_AUTHOR:
                return record.value("s_author")
            elif column == self.PRICE:
                return record.value("price")
            elif column == self.STOCK:
                return record.value("stock")
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return int(Qt.AlignLeft|Qt.AlignVCenter)
            return int(Qt.AlignRight|Qt.AlignVCenter)

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section == self.ID:
                return "Reg."
            elif section == self.TITLE:
                return unicode("Título".decode('utf-8'))
            elif section == self.AUTHOR:
                return "Autor"
            elif section == self.S_AUTHOR:
                return "Autor (Esp.)"
            elif section == self.PRICE:
                return unicode("Preço".decode('utf-8'))
            elif section == self.STOCK:
                return "Estoque"
        return section + 1