# -*- coding: UTF-8 -*-
#from time import sleep
from PySide.QtCore import QThread, Signal, QObject
from PySide.QtSql import QSqlDatabase, QSqlQuery
import logging
from src.lib.settings import SettingsParser

# logging.basicConfig(filename="seareiros.log", format="""%(asctime)-15s:
#                     %(name)-18s - %(levelname)-8s - %(module)-15s -
#                     %(funcname)-20s - %(lineno)-6d - %(message)s""")
logger = logging.getLogger('db_util')

class Db_Query_Thread(QThread):
    """
        async access to database
        I got the idea from here: http://www.linuxjournal.com/article/9602
    """
    # Custom Signals
    query_finished = Signal(list, str)
    ready = Signal(bool)
    progress = Signal(str)
    query_queue = Signal(str, list)
    query_row_num = Signal(int)
    query_row_read = Signal()

    def __init__(self, name=None, query=None, params=None, parent=None):
        super(Db_Query_Thread, self).__init__(parent)
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
        self.progress.emit("Conectando ao banco de dados...")
        worker = Worker(self.name)
        if worker._connError:
            self.query_finished.emit([], 'connError')
        else:
            self.query_queue.connect(worker.slot_exec)
            # connecting worker signals to thread slots
            worker.result.connect(self.query_finished)
            worker.cleanup.connect(self.cleanup)
            worker.numRows.connect(self.query_row_num)
            worker.readRow.connect(self.query_row_read)
            self.progress.emit(unicode("Executando transação...".decode('utf-8')))
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
    result = Signal(list, str)
    cleanup = Signal(str)
    numRows = Signal(int)
    readRow = Signal()

    def __init__(self, name, parent=None):
        self.log = logging.getLogger('Worker')
        self._connError = False
        super(Worker, self).__init__(parent)

        self.db = Db_Instance(name).get_instance()

        if not self.db.open():
            self.log.error(self.db.lastError())
            self._connError = True

    def connError(self):
        return self._connError

    def slot_exec(self, query, params):
        records = []
        sql = QSqlQuery(self.db)
        sql.prepare(query)
        if params:
            for p in params:
                self.set_value(sql, p)
        sql.exec_()

        # number of rows returned from query execution
        self.numRows.emit(sql.size())

        while sql.next():
            records.append(sql.record())
            #sleep(1)
            # row read
            self.readRow.emit()
        self.result.emit(records, '')
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
        elif type in "date":
            sqlquery.bindValue(name, value)

class Db_Instance():
    """
        really, this is just so that I don't repeat myself too much
    """
    def __init__(self, name, parent=None):
        settings = SettingsParser()
        # avoid overwriting connections that ain't finished yet
        while QSqlDatabase.contains(name):
            if name[-1].isdigit():
                name = name[0:-1] + str( int(name[-1]) + 1 )
            else:
                name = name + str(2)
        self._db = QSqlDatabase.addDatabase("QPSQL", name)
        self._db.setHostName(settings.get_value("Database", "hostname"))
        self._db.setDatabaseName("seareiros_bd")
        self._db.setUserName("seareiros")
        self._db.setPassword("localadm")
    def get_instance(self):
        return self._db


