# -*- coding: UTF-8 -*-
from PySide.QtGui import QIcon
from src.dialogs.select_generic import GenericSelect
from src.forms.add_associate import AssociateAddForm
from src.forms.search_associate import AssociateSearchForm


class AssociateSelectDialog(GenericSelect):
    """ Dialog for selecting an activity """

    def __init__(self, parent=None):
        super(AssociateSelectDialog, self).__init__(parent)
        self.setWindowTitle("Selecionar Associado")
        self.setWindowIcon(QIcon(":icons/associate.png"))

    def setup_add(self):
        self._addForm = AssociateAddForm()
        self._addForm.show()
        self._stackedWidget.addWidget(self._addForm)

    def setup_search(self):
        self._searchForm = AssociateSearchForm(osa=True)
        self._searchForm.show()
        self._stackedWidget.addWidget(self._searchForm)

    def toggle_function(self):
        """ swaps functionality """
        super(AssociateSelectDialog, self).toggle_function()
        if self._function == self.SEARCH:
            self.btnToggleFuncion.setIcon(QIcon(":icons/associate_add.png"))
            self._searchForm.edKeyword.setFocus()
        else:
            self._addForm.edFullName.setFocus()
