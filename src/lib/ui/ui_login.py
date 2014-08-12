# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/login.ui'
#
# Created: Mon Aug 11 11:19:02 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(296, 185)
        Dialog.setMinimumSize(QtCore.QSize(296, 185))
        Dialog.setMaximumSize(QtCore.QSize(296, 185))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.editUsername = QtGui.QLineEdit(Dialog)
        self.editUsername.setGeometry(QtCore.QRect(20, 30, 261, 31))
        self.editUsername.setPlaceholderText("")
        self.editUsername.setObjectName("editUsername")
        self.editPassword = QtGui.QLineEdit(Dialog)
        self.editPassword.setGeometry(QtCore.QRect(20, 90, 261, 31))
        self.editPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.editPassword.setObjectName("editPassword")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 85, 21))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 85, 21))
        self.label_2.setObjectName("label_2")
        self.btnBoxLogin = QtGui.QDialogButtonBox(Dialog)
        self.btnBoxLogin.setEnabled(True)
        self.btnBoxLogin.setGeometry(QtCore.QRect(100, 140, 176, 29))
        self.btnBoxLogin.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnBoxLogin.setObjectName("btnBoxLogin")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.editUsername, self.editPassword)
        Dialog.setTabOrder(self.editPassword, self.btnBoxLogin)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Seareiros - Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Usuário", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Senha", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
