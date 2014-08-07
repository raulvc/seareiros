# -*- coding: UTF-8 -*-
from PySide import QtCore
from PySide.QtGui import QIcon
from src.docks.dock_edit import EditDock
from src.forms.edit_book import BookEditForm


class EditBookDock(EditDock):
    """ Interface for associate input """

    def __init__(self, record_id, parent=None):
        super(EditBookDock, self).__init__(parent)
        self.setWindowTitle(unicode("Edição de Livro".decode('utf-8')))
        self.tabWidget.setTabIcon(self.ADD, QIcon(":icons/book_update.png"))
        self.setObjectName("EditBook")
        self.set_label_id(record_id)
        self._record_id = record_id
        self.setup_edit()

    def setup_edit(self):
        self._editForm = BookEditForm(record_id=self._record_id)
        self._editForm.show()
        self.addPlaceholder.addWidget(self._editForm)

    @QtCore.Slot()
    def on_btnSave_clicked(self):
        ok = self._editForm.update_data()
        if ok:
            self.close()

    @QtCore.Slot()
    def on_btnCancel_clicked(self):
        self.close()