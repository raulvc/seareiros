# -*- coding: UTF-8 -*-
from PySide import QtCore
import logging
from PySide.QtGui import QDockWidget, QDialogButtonBox, QMessageBox, QComboBox
from PySide.QtSql import QSqlRelationalTableModel
from src.forms.search_activity import ActivitySearchForm
from src.lib.ui.ui_add_activity import Ui_Dock
from src.lib.db_util import Db_Instance

logger = logging.getLogger('add_activity')

class AddActivityDock(QDockWidget, Ui_Dock):
    """ Interface for book input """

    ID, DESCRIPTION, ROOM, WEEKDAY, WEEKTIME = range(5)
    ADD, SEARCH = range(2)

    def __init__(self, parent=None):
        super(AddActivityDock, self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.on_cancel_clicked)
        self.buttonBox.button(QDialogButtonBox.Save).setText("Salvar")
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.on_save_clicked)
        self.buttonBox.button(QDialogButtonBox.Reset).setText("Limpar")
        self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.clear)
        # had to hardcode these, wouldn't work otherwise:
        self.verticalLayout.setAlignment(self.groupBox, QtCore.Qt.AlignTop)

        self.setup_editing()
        self.setup_search()

        self.log = logging.getLogger('AddActivityDock')
        self.visibilityChanged.connect(self.toggle_visibility)

        self.setup_model()
        # flag to indicate whether there were changes to the fields
        self._dirty = False

    def setup_editing(self):
        comboBoxList = self.tabRegister.findChildren(QComboBox)
        for comboBox in comboBoxList:
            comboBox.activated.connect(comboBox.focusNextChild)

    def setup_search(self):
        self._searchForm = ActivitySearchForm()
        self._searchForm.show()
        self.tabSearch.layout().addWidget(self._searchForm)

    def setup_model(self):
        db = Db_Instance("add_activity").get_instance()
        if not db.open():
            self.log.error(db.lastError().text())
            message = unicode("Erro de conexão\n\n""Banco de dados indisponível".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Cadastro de Atividade", message)
        else:
            self._model = QSqlRelationalTableModel(self, db=db)
            self._model.setTable("activity")

    def on_save_clicked(self):
        self._model.insertRow(0)

        self._model.setData(self._model.index(0, self.DESCRIPTION), self.comboDescription.currentText())
        self._model.setData(self._model.index(0, self.ROOM), self.comboRoom.currentIndex())
        self._model.setData(self._model.index(0, self.WEEKDAY), self.comboWeekday.currentIndex())
        self._model.setData(self._model.index(0, self.WEEKTIME), self.editTime.time())

        # try to commit a record
        if not self._model.submitAll():
            self.log.error(self._model.lastError().text())
            message = unicode("Erro de transação\n\n""Não foi possível salvar no banco de dados".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Cadastro de Atividade", message)
        else:
            message = unicode("Sucesso!\n\n""A atividade foi salva com êxito no banco de dados".decode('utf-8'))
            QMessageBox.information(self, "Seareiros - Cadastro de Atividade", message)
            self.clear()

    def on_cancel_clicked(self):
        if not self._dirty:
            self.close()
        else:
            pass

    def clear(self):
        self._dirty = False
        self.comboDescription.setCurrentIndex(0)
        self.comboRoom.setCurrentIndex(0)
        self.comboWeekday.setCurrentIndex(0)
        self.comboDescription.setFocus()


    def toggle_visibility(self, visible):
        actionAddActivity = self.parent().parent().actionAddActivity
        if visible:
            actionAddActivity.setEnabled(False)
            self.comboDescription.setFocus()
        else:
            actionAddActivity.setEnabled(True)

    def closeEvent(self, event):
        self.toggle_visibility(False)
        grandparent = self.parent().parent()
        grandparent.remove_instance(self)

    @QtCore.Slot(int)
    def on_tabWidget_currentChanged(self, index):
        if index == self.SEARCH:
            self._searchForm.refresh()
