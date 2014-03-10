# -*- coding: UTF-8 -*-

from PySide.QtCore import Qt
from src.models.model_base import BaseTableModel


class AssociateTableModel(BaseTableModel):
    """ Model for associate objects """

    ID, FULLNAME, NICKNAME, EMAIL, RESPHONE, COMPHONE, PRIVPHONE, STREETADDRESS = range(8)

    def __init__(self, parent=None):
        sql_statement = "SELECT id, fullname, nickname, email, resphone, comphone, privphone, " \
                        "streetaddress FROM associate"
        name = "populate_associate"
        super(AssociateTableModel, self).__init__(sql_statement, name, parent)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0<=index.row()<self.rowCount()):
            # invalid index
            return None

        record = self.get_record(index.row())
        column = index.column()
        if role == Qt.DisplayRole:
            if column == self.ID:
                return record.value("id")
            elif column == self.FULLNAME:
                return record.value("fullname")
            elif column == self.NICKNAME:
                return record.value("nickname")
            elif column == self.EMAIL:
                return record.value("email")
            elif column == self.RESPHONE:
                return record.value("resphone")
            elif column == self.COMPHONE:
                return record.value("comphone")
            elif column == self.PRIVPHONE:
                return record.value("privphone")
            elif column == self.STREETADDRESS:
                return record.value("streetaddress")

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return int(Qt.AlignLeft|Qt.AlignVCenter)
            return int(Qt.AlignRight|Qt.AlignVCenter)

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section == self.FULLNAME:
                return "Nome"
            elif section == self.NICKNAME:
                return "Apelido"
            elif section == self.EMAIL:
                return "E-Mail"
            elif section == self.RESPHONE:
                return "Tel. Residencial"
            elif section == self.COMPHONE:
                return "Tel. Comercial"
            elif section == self.PRIVPHONE:
                return "Celular"
            elif section == self.STREETADDRESS:
                return unicode("Endereço".decode('utf-8'))
        return section + 1