# -*- coding: UTF-8 -*-
from time import sleep
from PySide.QtCore import QThread, Signal, QObject
from PySide.QtGui import QMessageBox
from PySide.QtSql import QSqlDatabase, QSqlQuery
import sys

class Db_Thread(QThread):
    """
        async access to database
        I got the idea from here: http://www.linuxjournal.com/article/9602
    """
    # Custom Signals
    query_finished = Signal(list)
    ready = Signal(bool)
    progress = Signal(str)
    query_queue = Signal(str, list)

    def __init__(self, name=None, query=None, params=None, parent=None):
        super(Db_Thread, self).__init__(parent)
        self.name = name
        self.query = query
        self.params = params

    def set_query(self, query):
        self.query = query

    def set_params(self, params):
        self.params = params

    def set_name(self, name):
        self.name = name

    def run(self):
        self.ready.emit(False)
        self.progress.emit("Fetching database...")
        worker = Worker(self.name)
        self.query_queue.connect(worker.slot_exec)
        worker.result.connect(self.query_finished)
        worker.cleanup.connect(self.cleanup)
        self.progress.emit("Ready to run a query.")
        self.ready.emit(True)
        self.query_queue.emit(self.query, self.params)
        # start event loop
        self.exec_()

    def cleanup(self, conn_name):
        """ may not be the same connection name as appointed by 'name' argument
        See Worker class '__init__' method bellow """
        QSqlDatabase.removeDatabase(conn_name)

class Worker(QObject):
    """
        Working thread for DB_Thread.
        Due to qt4 db access being synchronous, we must create a new execution loop for each
        queued query.
    """
    # Custom Signals
    result = Signal(list)
    cleanup = Signal(str)

    def __init__(self, name, parent=None):
        super(Worker, self).__init__(parent)
        # avoid overwriting connections that ain't finished yet
        while name in QSqlDatabase.connectionNames():
            if name[-1].isdigit():
                name = name[0:-1] + str( int(name[-1]) + 1 )
            else:
                name = name + str(2)
        self.db = QSqlDatabase.addDatabase("QPSQL", name)
        self.db.setHostName("localhost")
        self.db.setDatabaseName("seareiros_bd")
        self.db.setUserName("seareiros")
        self.db.setPassword("localadm")
        if not self.db.open():
            QMessageBox.warning(None, unicode("Erro de conexão com o banco".decode('utf-8')),
                                unicode("Descrição: \n".decode('utf-8')) + self.db.lastError().text())
            sys.exit(1)

    def slot_exec(self, query, params):
        records = []
        sql = QSqlQuery(self.db)
        sql.prepare(query)
        if params:
            for p in params:
                self.set_value(sql, p)
        sql.exec_()
        while sql.next():
            records.append(sql.record())
        self.result.emit(records)
        self.cleanup.emit(self.db.connectionName())

    def set_value(self, sqlquery, param):
        """ safe param passing to sql statement """
        type = param[0]
        name = param[1]
        value = param[2]
        if type in "str":
            sqlquery.bindValue(name, unicode(value.decode('utf-8')))
        elif type in "int":
            sqlquery.bindValue(name, value)


