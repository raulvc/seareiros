# -*- coding: UTF-8 -*-

from PySide.QtGui import QDialog, QDialogButtonBox, QMovie, QIcon, QMessageBox
from src.lib.db_util import Db_Query_Thread
from src.lib.ui.ui_login import Ui_Dialog

class Login(QDialog, Ui_Dialog):
    """User validation"""

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.btnBoxLogin.button(QDialogButtonBox.Cancel).setText("Cancelar")
        self.btnBoxLogin.button(QDialogButtonBox.Cancel).clicked.connect(self.close)
        self.btnBoxLogin.button(QDialogButtonBox.Ok).clicked.connect(self.ok_clicked)
        self.load_icon = QMovie(":icons/loading.gif")
        sql_statement = """SELECT username, password, access FROM users WHERE
                      users.username=:username AND users.password=:password"""
        self._validate_job = Db_Query_Thread(name="validation", query=sql_statement)
        self._validate_job.query_finished.connect(self.validate_login)
        self._user_logged = False
        self._username = None
        self._access = None

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
        self._validate_job.set_params(parameters)
        self._validate_job.start()

    def validate_login(self, db_result, error=None):
        self._validate_job.exit()
        if db_result:
            # correct username and password
            self._user_logged = True
            self._username = db_result[0].value(0)
            self._access = db_result[0].value(2)
            self.accept()
        else:
            if error == 'connError':
                message = unicode("Erro de autenticação\n\n""Banco de dados indisponível".decode('utf-8'))
            else:
                message = unicode("Erro de autenticação\n\n""Usuário e/ou Senha inválido(s)".decode('utf-8'))
            QMessageBox.critical(self, "Seareiros - Login", message)
            self.btnBoxLogin.button(QDialogButtonBox.Ok).setText("&OK")
            self.load_icon.frameChanged.disconnect(self.set_loading_icon)
            self.load_icon.stop()
            self.btnBoxLogin.button(QDialogButtonBox.Ok).setIcon(QIcon())
            self.btnBoxLogin.button(QDialogButtonBox.Ok).setEnabled(True)
            self.editUsername.setFocus()
            self.editUsername.selectAll()

    def get_user_data(self):
        if self._user_logged:
            return [self._username, self._access]
        else:
            return None