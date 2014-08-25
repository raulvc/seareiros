# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/generic_select.ui'
#
# Created: Mon Aug 25 20:22:27 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(731, 560)
        Dialog.setMinimumSize(QtCore.QSize(700, 300))
        Dialog.setWindowTitle("")
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(350, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.btnCancel = QtGui.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/conn_failed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.btnCancel, 2, 0, 1, 1)
        self.btnToggleFuncion = QtGui.QPushButton(Dialog)
        self.btnToggleFuncion.setText("")
        self.btnToggleFuncion.setObjectName("btnToggleFuncion")
        self.gridLayout.addWidget(self.btnToggleFuncion, 0, 0, 1, 1)
        self.btnSelect = QtGui.QPushButton(Dialog)
        self.btnSelect.setText("")
        self.btnSelect.setObjectName("btnSelect")
        self.gridLayout.addWidget(self.btnSelect, 2, 2, 1, 1)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.contentsPlaceholder = QtGui.QVBoxLayout(self.frame)
        self.contentsPlaceholder.setObjectName("contentsPlaceholder")
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.btnCancel.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
