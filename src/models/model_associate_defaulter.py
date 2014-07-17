# -*- coding: UTF-8 -*-
from PySide.QtCore import Qt

from src.models.model_associate import AssociateTableModel


class DefaulterTableModel(AssociateTableModel):
    """ Model for defaulter (at fault, associates with debt) objects """

    DEBT = 8

    def __init__(self, parent=None):
        super(DefaulterTableModel, self).__init__(parent)
        self._sql_statement = "SELECT id, fullname, nickname, email, resphone, comphone, privphone, " \
                        "streetaddress, debt FROM associate WHERE debt > '0.0'::MONEY"
        self._name = "populate_defaulter"

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0<=index.row()<self.rowCount()):
            # invalid index
            return None
        record = self.get_record(index.row())
        column = index.column()
        if role == Qt.DisplayRole:
            if column == self.DEBT:
                return record.value("debt")
            else:
                return super(DefaulterTableModel, self).data(index, role)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return int(Qt.AlignLeft|Qt.AlignVCenter)
            return int(Qt.AlignRight|Qt.AlignVCenter)

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section == self.DEBT:
                return unicode("Pendência".decode('utf-8'))
            else:
                return super(DefaulterTableModel, self).headerData(section, orientation, role)
        return section + 1