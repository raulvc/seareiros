# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/pendencies.ui'
#
# Created: Fri Jul 25 16:17:55 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dock(object):
    def setupUi(self, Dock):
        Dock.setObjectName("Dock")
        Dock.setWindowModality(QtCore.Qt.WindowModal)
        Dock.resize(709, 552)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dock.setWindowIcon(icon)
        Dock.setStyleSheet("QDockWidget::title\n"
"{\n"
"   font-family: \"Roboto Lt\";\n"
"   font-size: 18pt;\n"
"   background: lightgray;\n"
"   padding-left: 10px; \n"
"   padding-top: 4px;\n"
"}")
        Dock.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        Dock.setAllowedAreas(QtCore.Qt.TopDockWidgetArea)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.edKeyword = QtGui.QLineEdit(self.dockWidgetContents)
        self.edKeyword.setObjectName("edKeyword")
        self.gridLayout.addWidget(self.edKeyword, 0, 1, 1, 1)
        self.tableView = QtGui.QTableView(self.dockWidgetContents)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 4)
        self.btnRefresh = QtGui.QPushButton(self.dockWidgetContents)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/loading.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefresh.setIcon(icon1)
        self.btnRefresh.setObjectName("btnRefresh")
        self.gridLayout.addWidget(self.btnRefresh, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        Dock.setWidget(self.dockWidgetContents)

        self.retranslateUi(Dock)
        QtCore.QMetaObject.connectSlotsByName(Dock)

    def retranslateUi(self, Dock):
        Dock.setToolTip(QtGui.QApplication.translate("Dock", "Pendências", None, QtGui.QApplication.UnicodeUTF8))
        Dock.setWindowTitle(QtGui.QApplication.translate("Dock", "Pendências", None, QtGui.QApplication.UnicodeUTF8))
        self.edKeyword.setPlaceholderText(QtGui.QApplication.translate("Dock", "Digite a palavra-chave", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefresh.setText(QtGui.QApplication.translate("Dock", "Atualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dock", "Filtrar:", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
