# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/generic_dock.ui'
#
# Created: Wed Feb 26 19:33:46 2014
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dock(object):
    def setupUi(self, Dock):
        Dock.setObjectName("Dock")
        Dock.setWindowModality(QtCore.Qt.WindowModal)
        Dock.resize(774, 445)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dock.sizePolicy().hasHeightForWidth())
        Dock.setSizePolicy(sizePolicy)
        Dock.setStyleSheet("QDockWidget::title\n"
"{\n"
"   font-family: \"Roboto Lt\";\n"
"   font-size: 18pt;\n"
"   background: lightgray;\n"
"   padding-left: 10px; \n"
"   padding-top: 4px;\n"
"}")
        Dock.setFloating(False)
        Dock.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
        Dock.setAllowedAreas(QtCore.Qt.TopDockWidgetArea)
        Dock.setWindowTitle("")
        self.Contents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Contents.sizePolicy().hasHeightForWidth())
        self.Contents.setSizePolicy(sizePolicy)
        self.Contents.setObjectName("Contents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.Contents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtGui.QTabWidget(self.Contents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tabAdd = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabAdd.sizePolicy().hasHeightForWidth())
        self.tabAdd.setSizePolicy(sizePolicy)
        self.tabAdd.setObjectName("tabAdd")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabAdd)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnSave = QtGui.QPushButton(self.tabAdd)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon)
        self.btnSave.setObjectName("btnSave")
        self.gridLayout.addWidget(self.btnSave, 1, 3, 1, 1)
        self.btnClear = QtGui.QPushButton(self.tabAdd)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClear.setIcon(icon1)
        self.btnClear.setObjectName("btnClear")
        self.gridLayout.addWidget(self.btnClear, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.btnCancel = QtGui.QPushButton(self.tabAdd)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/conn_failed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon2)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.btnCancel, 1, 2, 1, 1)
        self.addPlaceholder = QtGui.QVBoxLayout()
        self.addPlaceholder.setObjectName("addPlaceholder")
        self.gridLayout.addLayout(self.addPlaceholder, 0, 0, 1, 4)
        self.verticalLayout_5.addLayout(self.gridLayout)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/activity_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabAdd, icon3, "")
        self.tabSearch = QtGui.QWidget()
        self.tabSearch.setObjectName("tabSearch")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabSearch)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.searchPlaceholder = QtGui.QVBoxLayout()
        self.searchPlaceholder.setObjectName("searchPlaceholder")
        self.verticalLayout_3.addLayout(self.searchPlaceholder)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabSearch, icon4, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        Dock.setWidget(self.Contents)

        self.retranslateUi(Dock)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dock)

    def retranslateUi(self, Dock):
        Dock.setToolTip(QtGui.QApplication.translate("Dock", "Cadastro de Atividades", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("Dock", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setText(QtGui.QApplication.translate("Dock", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("Dock", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAdd), QtGui.QApplication.translate("Dock", "Novo Cadastro", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSearch), QtGui.QApplication.translate("Dock", "Buscar", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
