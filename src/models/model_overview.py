# -*- coding: UTF-8 -*-

from PySide.QtCore import Qt
from PySide.QtGui import QColor
from src.models.model_base import BaseTableModel


class OverviewTableModel(BaseTableModel):
    """ Model for overview objects """

    ID, TYPE, DESCRIPTION, DATE, USERNAME = range(5)

    def __init__(self, parent=None):
        # for some wicked reason it won't work when I repeat the same parameter twice in the query
        sql_statement = "SELECT * FROM history WHERE DATE(history.date) >= :date AND DATE(history.date) <= :date_again"
        name = "populate_overview"
        super(OverviewTableModel, self).__init__(sql_statement, name, parent)

    def load_date(self, date):
        params = [["date", "date", date],["date", "date_again", date]]
        self.load(params)

    # def sort(self, col, order):
    #     """ sorts table by given column number (col) """
    #     # self.layoutAboutToBeChanged.emit()
    #     self._data = sorted(self._data, key=lambda record: record.value(col))
    #     if order == Qt.DescendingOrder:
    #         self._data.reverse()
    #     self.reset()
    #     # self.layoutChanged.emit()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0<=index.row()<self.rowCount()):
            # invalid index
            return None

        record = self.get_record(index.row())
        column = index.column()
        if role == Qt.DisplayRole:
            if column == self.ID:
                return record.value("id")
            elif column == self.TYPE:
                return record.value("type")
            elif column == self.DESCRIPTION:
                return record.value("description")
            elif column == self.DATE:
                return record.value("date").toString("dd/MMM - HH:mm")
            elif column == self.USERNAME:
                return record.value("username")

        elif role == Qt.BackgroundRole:
            type = record.value('type')
            if type == 'venda':
                return QColor("yellow")
            else:
                return QColor("white")

            # elif role == Qt.ForegroundRole:
            #     return QColor("white")
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return int(Qt.AlignLeft|Qt.AlignVCenter)
            return int(Qt.AlignRight|Qt.AlignVCenter)

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section == self.TYPE:
                return "Tipo"
            elif section == self.DESCRIPTION:
                return unicode("Descrição".decode('utf-8'))
            elif section == self.DATE:
                return "Data e Hora"
            elif section == self.USERNAME:
                return unicode("Usuário".decode('utf-8'))
        return section + 1