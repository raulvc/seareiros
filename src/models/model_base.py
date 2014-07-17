# -*- coding: UTF-8 -*-

from PySide.QtCore import QAbstractTableModel, QModelIndex
from PySide.QtGui import QMessageBox
from src.lib.db_util import Db_Query_Thread
from src.lib.dialog_util import Loading


class BaseTableModel(QAbstractTableModel):
    """ Base Model """

    def __init__(self, parent=None):
        super(BaseTableModel, self).__init__(parent)
        self._loading_dialog = Loading()
        self._data = []
        self._populate_job = Db_Query_Thread()

    def set_query_info(self, name, sql_statement, params=None):
        self._populate_job.set_name(name)
        self._populate_job.set_query(sql_statement)
        if params:
            self._populate_job.set_params(params)

    def load(self):
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
                QMessageBox.critical(self, "Seareiros", message)
        self.reset()

    def get_record(self, row):
        return self._data[row]

    def rowCount(self, index=QModelIndex()):
        return len(self._data)

    def columnCount(self, index=QModelIndex()):
        if ( len(self._data) > 0 ):
            return self._data[0].count()
        else:
            return 0