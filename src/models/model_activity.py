# -*- coding: UTF-8 -*-

from PySide.QtCore import Qt
from src.models.model_base import BaseTableModel


class ActivityTableModel(BaseTableModel):
    """ Model for activity objects """

    ID, DESCRIPTION, ROOM, WEEKDAY, WEEKTIME = range(5)

    def __init__(self, parent=None):
        sql_statement = "SELECT * FROM activity"
        name = "populate_activity"
        super(ActivityTableModel, self).__init__(sql_statement, name, parent)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0<=index.row()<self.rowCount()):
            # invalid index
            return None

        record = self.get_record(index.row())
        column = index.column()
        if role == Qt.DisplayRole:
            if column == self.ID:
                return record.value("id")
            if column == self.DESCRIPTION:
                return record.value("description")
            elif column == self.ROOM:
                room = record.value("room")
                if room != 0:
                    return room
                else:
                    return "Nenhuma"
            elif column == self.WEEKDAY:
                return self.extend_weekday(record.value("weekday"))
            elif column == self.WEEKTIME:
                return record.value("weektime").toString("HH:mm")

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return int(Qt.AlignLeft|Qt.AlignVCenter)
            return int(Qt.AlignRight|Qt.AlignVCenter)

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section == self.DESCRIPTION:
                return unicode("Descrição".decode('utf-8'))
            elif section == self.ROOM:
                return "Sala"
            elif section == self.WEEKDAY:
                return "Dia"
            elif section == self.WEEKTIME:
                return unicode("Horário".decode('utf-8'))
        return section + 1

    def extend_weekday(self, weekday):
        # boy this feels so wrong
        days_of_the_week = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
        return days_of_the_week[weekday]