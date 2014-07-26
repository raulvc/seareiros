# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QIcon, QMessageBox
from src.docks.dock_generic import GenericDock
from src.forms.add_book import BookAddForm
from src.forms.search_book import BookSearchForm


class AddBookDock(GenericDock):
    """ Interface for associate input """

    def __init__(self, parent=None):
        super(AddBookDock, self).__init__(parent)
        self.setWindowTitle("Cadastro de Livros")
        self.tabWidget.setTabIcon(self.ADD, QIcon(":icons/book_add.png"))

    def setup_add(self):
        self._addForm = BookAddForm()
        self._addForm.show()
        self.addPlaceholder.addWidget(self._addForm)

    def setup_search(self):
        self._searchForm = BookSearchForm()
        self._searchForm.show()
        self.searchPlaceholder.addWidget(self._searchForm)

    @QtCore.Slot()
    def on_btnSave_clicked(self):
        ok = self._addForm.submit_data()
        if ok:
            self._addForm.clear()

    @QtCore.Slot()
    def on_btnCancel_clicked(self):
        if not self._addForm.is_dirty():
            self.close()
        else:
            message = unicode("Descartar dados não salvos e sair?".decode('utf-8'))
            reply = QMessageBox.question(self, 'Seareiros - Cadastro de Livros',
                                         message, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.close()

    @QtCore.Slot()
    def on_btnClear_clicked(self):
        self._addForm.clear()

    def toggle_visibility(self, visible):
        actionAddBook = self.parent().parent().actionAddBook
        if visible:
            super(AddBookDock, self).toggle_visibility(visible)
            actionAddBook.setEnabled(False)
            self._addForm.edBarcode.setFocus()
        else:
            actionAddBook.setEnabled(True)
