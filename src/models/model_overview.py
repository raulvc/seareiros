# -*- coding: UTF-8 -*-

from PySide.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide.QtGui import QColor, QMessageBox
from src.lib.db_util import Db_Thread
from src.lib.dialog_util import Loading


class OverviewTableModel(QAbstractTableModel):
    """ Model for book objects """

    ID, TYPE, DESCRIPTION, DATE, USERNAME = range(5)

    def __init__(self, parent=None):
        super(OverviewTableModel, self).__init__(parent)
        # for some wicked reason it won't work when I repeat the same parameter twice in the query
        sql_statement = "SELECT * FROM history WHERE DATE(history.date) >= :date AND DATE(history.date) <= :date_again"
        self._populate_job = Db_Thread(name="populate_overview", query=sql_statement)
        self._loading_dialog = Loading()
        self._data = []

    def load(self, date):
        #TODO I will probably repeat those steps a lot, should consider passing methods as parameters for Loading dialogs
        self._populate_job.set_params([["date", "date", date],["date", "date_again", date]])
        self._populate_job.progress.connect(self._loading_dialog.setMessage)
        self._populate_job.query_row_num.connect(self._loading_dialog.setMaxRows)
        self._populate_job.query_row_read.connect(self._loading_dialog.incrementReadRows)
        self._populate_job.query_finished.connect(self.loadData)
        self._populate_job.start()
        self._loading_dialog.show()

    def loadData(self, record_list, error=None):
        self._populate_job.exit()
        self._loading_dialog.accept()
        self._loading_dialog.clear()
        if record_list:
            # self.beginInsertRows(QModelIndex(), 0, self.rowCount() - 1)
            self._data = record_list
            # self.endInsertRows()
        else:
            self._data = []
            if error == 'conError':
                message = unicode("Erro de autenticação\n\n""Banco de dados indisponível".decode('utf-8'))
                QMessageBox.critical(self, "Seareiros - Login", message)
        self.reset()

    def sort(self, col, order):
        """ sorts table by given column number (col) """
        # self.layoutAboutToBeChanged.emit()
        self._data = sorted(self._data, key=lambda record: record.value(col))
        if order == Qt.DescendingOrder:
            self._data.reverse()
        self.reset()
        # self.layoutChanged.emit()

    def get_record(self, row):
        return self._data[row]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0<=index.row()<self.rowCount()):
            # invalid index
            return None

        record = self.get_record(index.row())
        column = index.column()
        if role == Qt.DisplayRole:
            if column == self.ID:
                return record.value("id")
            if column == self.TYPE:
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


    def rowCount(self, index=QModelIndex()):
        return len(self._data)

    def columnCount(self, index=QModelIndex()):
        if ( len(self._data) > 0 ):
            return 5
        else:
            return 0