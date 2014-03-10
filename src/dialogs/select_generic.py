# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QDialog, QStackedWidget, QIcon
from src.lib.ui.ui_generic_select import Ui_Dialog

class GenericSelect(QDialog, Ui_Dialog):
    """ Common selection interface """

    ADD, SEARCH = range(2)

    def __init__(self, parent=None):
        super(GenericSelect, self).__init__(parent)
        self.setupUi(self)
        self._stackedWidget = QStackedWidget()
        self.contentsPlaceholder.addWidget(self._stackedWidget)

        self.setup_add()
        self.setup_search()

        self._record = None
        self._searchForm.viewSearch.doubleClicked.connect(self.selected_record)

        self._function = None
        self.toggle_function()

        self.adjustSize()


    def setup_add(self):
        pass

    def setup_search(self):
        pass

    def toggle_function(self):
        """ swaps functionality """
        if self._function == self.SEARCH:
            self._function = self.ADD
            self.btnToggleFuncion.setText("Voltar")
            self.btnToggleFuncion.setIcon(QIcon(":icons/search.png"))
            self.btnSelect.setText("Salvar")
            self.btnSelect.setIcon(QIcon(":icons/save.png"))
            self._stackedWidget.setCurrentWidget(self._addForm)
        else:
            self._function = self.SEARCH
            self.btnToggleFuncion.setText("Cadastrar")
            self.btnSelect.setText("Selecionar")
            self.btnSelect.setIcon(QIcon(":icons/conn_succeeded.png"))
            self._stackedWidget.setCurrentWidget(self._searchForm)
            self._searchForm.refresh()

    def selected_record(self, index):
        self._record = self._searchForm.get_record_at(index)

    def added_record(self):
        self._record = self._addForm.get_added_record()

    def get_record(self):
        return self._record

    @QtCore.Slot()
    def on_btnToggleFuncion_clicked(self):
        self.toggle_function()

    @QtCore.Slot()
    def on_btnCancel_clicked(self):
        self.reject()

    @QtCore.Slot()
    def on_btnSelect_clicked(self):
        if self._function == self.SEARCH:
            index = self._searchForm.get_current_index()
            if index.isValid():
                self.selected_record(index)
                self.accept()
        elif self._function == self.ADD:
            ok = self._addForm.submit_data()
            if ok:
                self.added_record()
                self.accept()


