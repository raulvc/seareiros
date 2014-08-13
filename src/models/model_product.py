# -*- coding: UTF-8 -*-

from PySide.QtCore import Qt, QLocale
from src.models.model_base import BaseTableModel


class ProductTableModel(BaseTableModel):
    """ Model for product objects """

    ID, DATE, TOTAL, ASSOCIATE, OBS = range(5)

    def __init__(self, parent=None):
        super(ProductTableModel, self).__init__(parent)
        self._sql_statement = "SELECT p_o.id, p_o.date, p_o.total, a.fullname as associate, SUBSTR(p_o.obs,0,50) as obs " \
                "FROM p_order p_o " \
                "LEFT JOIN associate a ON p_o.associate_id = a.id"
        self._name = "populate_product"
        self._locale = QLocale()

    def load(self):
        self.set_query_info(self._name, self._sql_statement)
        super(ProductTableModel, self).load()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0<=index.row()<self.rowCount()):
            # invalid index
            return None
        record = self.get_record(index.row())
        column = index.column()
        if role == Qt.DisplayRole:
            if column == self.ID:
                return record.value("id")
            elif column == self.DATE:
                return record.value("date").toString("dd/MMM - HH:mm")
            elif column == self.TOTAL:
                return self._locale.toString(record.value("total"), 'f', 2).replace('.','')
            elif column == self.ASSOCIATE:
                return record.value("associate")
            elif column == self.OBS:
                return record.value("obs")
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
            elif section == self.DATE:
                return "Data e Hora"
            elif section == self.TOTAL:
                return "Total (R$)"
            elif section == self.ASSOCIATE:
                return "Associado"
            elif section == self.OBS:
                return unicode("Observações".decode('utf-8'))
        return section + 1