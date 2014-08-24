# -*- coding: UTF-8 -*-
from PySide.QtGui import QIcon
from src.dialogs.select_generic import GenericSelect
from src.forms.add_book import BookAddForm
from src.forms.search_book import BookSearchForm
from src.lib import constants


class BookSelectDialog(GenericSelect):
    """ Dialog for selecting a book """

    def __init__(self, parent=None, display_mode=constants.BOOK_SELL):
        self.dm = display_mode
        super(BookSelectDialog, self).__init__(parent)
        self.setWindowTitle("Selecionar Livro")
        self.setWindowIcon(QIcon(":icons/book.png"))

    def setup_add(self):
        self._addForm = BookAddForm()
        self._addForm.show()
        self._stackedWidget.addWidget(self._addForm)

    def setup_search(self):
        self._searchForm = BookSearchForm(dm=self.dm)
        self._searchForm.show()
        self._stackedWidget.addWidget(self._searchForm)

    def toggle_function(self):
        """ swaps functionality """
        super(BookSelectDialog, self).toggle_function()
        if self._function == self.SEARCH:
            self.btnToggleFuncion.setIcon(QIcon(":icons/book_add.png"))
            self._searchForm.edKeyword.setFocus()
        else:
            self._addForm.edBarcode.setFocus()
