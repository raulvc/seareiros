# -*- coding: UTF-8 -*-
import logging

from PySide.QtGui import QDockWidget, QDialogButtonBox, QMessageBox
from PySide.QtSql import QSqlRelationalTableModel
from src.lib.ui.ui_add_associate import Ui_Dock
from src.lib.validators import UppercaseValidator, EmailValidator, AlphaNumericValidator
from src.lib.db_util import Db_Instance

logger = logging.getLogger('add_associate')

class AddAssociateDock(QDockWidget, Ui_Dock):
    """ Interface for book input """

    def __init__(self, parent=None):
        super(AddAssociateDock, self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.on_cancel_clicked)
        self.buttonBox.button(QDialogButtonBox.Save).setText("Salvar")
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.on_save_clicked)
        self.buttonBox.button(QDialogButtonBox.Reset).setText("Limpar")
        self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.clear)

        self.log = logging.getLogger('AddAssociateDock')
        self.visibilityChanged.connect(self.toggle_visibility)
        self.edFullName.setValidator(UppercaseValidator())
        self.edNickname.setValidator(UppercaseValidator())
        self.edEmail.setValidator(EmailValidator())
        self.edRG.setValidator(AlphaNumericValidator())

        self.setup_model()

    def setup_model(self):
        self.db = Db_Instance("add_associate").get_instance()
        if not self.db.open():
            self.log.error(self.db.lastError().text())
            message = unicode("Erro de conexão\n\n""Banco de dados indisponível".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Cadastro de Associado", message)
        else:
            self.model = QSqlRelationalTableModel(self, db=self.db)
            self.model.setTable("users")

    def on_save_clicked(self):
        pass

    def on_cancel_clicked(self):
        self.close()

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