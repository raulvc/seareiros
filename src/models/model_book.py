# -*- coding: UTF-8 -*-

from PySide.QtCore import Qt, QLocale
from src.lib import constants
from src.models.model_base import BaseTableModel


class BookTableModel(BaseTableModel):
    """ Model for book objects """

    ID, TITLE, AUTHOR, S_AUTHOR, PRICE, STOCK, AVAILABILITY = range(7)

    def __init__(self, parent=None, display_mode=constants.BOOK_ALL):
        super(BookTableModel, self).__init__(parent)
        self._sql_statement = "SELECT b.id, b.title, a.name as author, s_a.name as s_author, b.price, b.stock, b.availability " \
                "FROM book b " \
                "LEFT JOIN author a ON b.author_id = a.id " \
                "LEFT JOIN s_author s_a ON b.s_author_id = s_a.id"
        if display_mode == constants.BOOK_SELL:
            self._sql_statement += " WHERE b.availability = 0 AND b.stock > 0"
        elif display_mode == constants.BOOK_RENT:
            self._sql_statement += " WHERE b.availability = 1"
        self._name = "populate_book"
        self._locale = QLocale()

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
                return self._locale.toString(record.value("price"), 'f', 2).replace('.','')
            elif column == self.STOCK:
                return record.value("stock")
            elif column == self.AVAILABILITY:
                return self.extend_availability(record.value("availability"))
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
                return unicode("Preço (R$)".decode('utf-8'))
            elif section == self.STOCK:
                return "Estoque"
            elif section == self.AVAILABILITY:
                return "Disponibilidade"
        return section + 1

    def extend_availability(self, availability):
        avail_list = ['Venda', unicode('Locação'.decode('utf-8')), 'Inativo']
        return avail_list[availability]