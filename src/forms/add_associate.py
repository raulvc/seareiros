# -*- coding: UTF-8 -*-

from PySide.QtGui import QDockWidget, QDialogButtonBox
from src.lib.ui.ui_add_associate import Ui_Dock
from src.lib.validators import UppercaseValidator, EmailValidator, AlphaNumericValidator


class AddAssociateDock(QDockWidget, Ui_Dock):
    """ Interface for book input """

    def __init__(self, parent=None):
        super(AddAssociateDock, self).__init__(parent)
        self.setupUi(self)
        self.visibilityChanged.connect(self.toggle_visibility)
        self.edFullName.setValidator(UppercaseValidator())
        self.edNickname.setValidator(UppercaseValidator())
        self.edEmail.setValidator(EmailValidator())
        self.edRG.setValidator(AlphaNumericValidator())
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.save_clicked)

    def clear(self):
        pass

    def toggle_visibility(self, visible):
        actionAddAssociate = self.parent().parent().actionAddAssociate
        if visible:
            actionAddAssociate.setEnabled(False)
            self.edFullName.setFocus()
        else:
            actionAddAssociate.setEnabled(True)

    def closeEvent(self, sender):
        self.toggle_visibility(False)
        grandparent = self.parent().parent()
        grandparent.remove_instance(self)

    def save_clicked(self):
        pass
