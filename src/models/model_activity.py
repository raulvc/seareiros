# -*- coding: UTF-8 -*-

from PySide.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide.QtGui import QMessageBox
from src.lib.db_util import Db_Query_Thread
from src.lib.dialog_util import Loading


class ActivityTableModel(QAbstractTableModel):
    """ Model for activity objects """

    ID, DESCRIPTION, ROOM, WEEKDAY, WEEKTIME = range(5)

    def __init__(self, parent=None):
        super(ActivityTableModel, self).__init__(parent)
        sql_statement = "SELECT * FROM activity"
        self._populate_job = Db_Query_Thread(name="populate_activity", query=sql_statement)
        self._loading_dialog = Loading()
        self._data = []

    def load(self):
        #TODO I will probably repeat those steps a lot, should consider passing methods as parameters for Loading dialogs
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
            self._data = record_list
        else:
            self._data = []
            if error == 'conError':
                message = unicode("Erro de autenticação\n\n""Banco de dados indisponível".decode('utf-8'))
                QMessageBox.critical(self, "Seareiros - Atividades", message)
        self.reset()

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


    def rowCount(self, index=QModelIndex()):
        return len(self._data)

    def columnCount(self, index=QModelIndex()):
        if ( len(self._data) > 0 ):
            return 5
        else:
            return 0

    def extend_weekday(self, weekday):
        # boy this feels so wrong
        days_of_the_week = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
        return days_of_the_week[weekday]