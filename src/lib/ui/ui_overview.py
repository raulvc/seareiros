# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/overview.ui'
#
# Created: Thu Jul 31 15:27:05 2014
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
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetLayout = QtGui.QWidget(self.dockWidgetContents)
        self.widgetLayout.setObjectName("widgetLayout")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widgetLayout)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.widgetLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(50, 33))
        self.label.setMaximumSize(QtCore.QSize(50, 33))
        self.label.setBaseSize(QtCore.QSize(50, 33))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dateEdit = QtGui.QDateEdit(self.widgetLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.dateEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dateEdit.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnRefresh = QtGui.QPushButton(self.widgetLayout)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/loading.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefresh.setIcon(icon1)
        self.btnRefresh.setObjectName("btnRefresh")
        self.horizontalLayout.addWidget(self.btnRefresh)
        self.verticalLayout.addWidget(self.widgetLayout)
        self.tableView = QtGui.QTableView(self.dockWidgetContents)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        Dock.setWidget(self.dockWidgetContents)

        self.retranslateUi(Dock)
        QtCore.QMetaObject.connectSlotsByName(Dock)

    def retranslateUi(self, Dock):
        Dock.setToolTip(QtGui.QApplication.translate("Dock", "Últimas Ações", None, QtGui.QApplication.UnicodeUTF8))
        Dock.setWindowTitle(QtGui.QApplication.translate("Dock", "Últimas Ações", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dock", "Dia:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit.setDisplayFormat(QtGui.QApplication.translate("Dock", "ddd dd/MMM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefresh.setText(QtGui.QApplication.translate("Dock", "Atualizar", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
