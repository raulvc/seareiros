# -*- coding: UTF-8 -*-

from PySide.QtGui import *
from src.lib.db_util import Db_Thread
from src.lib.ui.ui_login import Ui_Dialog


class Login(QDialog, Ui_Dialog):
    """User validation class"""

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.btnBoxLogin.button(QDialogButtonBox.Cancel).setText("Cancelar")
        self.btnBoxLogin.button(QDialogButtonBox.Cancel).clicked.connect(self.closeEvent)
        self.btnBoxLogin.button(QDialogButtonBox.Ok).clicked.connect(self.ok_clicked)
        self.load_icon = QMovie(":icons/loading.gif")
        sql_statement = """SELECT username, password FROM user WHERE
                      user.username=:username AND user.password=:password"""
        self.validate_job = Db_Thread(name="validation", query=sql_statement)
        self.validate_job.query_finished.connect(self.validate_login)

    def set_loading_icon(self, frame=None):
        self.btnBoxLogin.button(QDialogButtonBox.Ok).setIcon(QIcon(self.load_icon.currentPixmap()))

    def ok_clicked(self):
        """Calls validation methods"""
        self.btnBoxLogin.button(QDialogButtonBox.Ok).setEnabled(False)
        self.btnBoxLogin.button(QDialogButtonBox.Ok).setText("")
        self.load_icon.frameChanged.connect(self.set_loading_icon)
        self.load_icon.start()
        username = self.editUsername.text()
        password = self.editPassword.text()
        parameters = [["str", "username", username],["str","password",password]]
        self.validate_job.set_params(parameters)
        self.validate_job.start()

    def validate_login(self, db_result):
        self.validate_job.exit()
        if db_result:
            # correct username and password
            print db_result
        else:
            QMessageBox.critical(self, "Seareiros - Login", unicode("Erro de autenticação\n\n"
                                                                    "Usuário e/ou Senha inválido(s)".decode('utf-8')))
            self.btnBoxLogin.button(QDialogButtonBox.Ok).setText("&OK")
            self.load_icon.frameChanged.disconnect(self.set_loading_icon)
            self.load_icon.stop()
            self.btnBoxLogin.button(QDialogButtonBox.Ok).setIcon(QIcon())
            self.btnBoxLogin.button(QDialogButtonBox.Ok).setEnabled(True)
            self.editUsername.setFocus()
            self.editUsername.selectAll()
