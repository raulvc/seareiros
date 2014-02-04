# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/add_book.ui'
#
# Created: Tue Feb  4 16:36:22 2014
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dock(object):
    def setupUi(self, Dock):
        Dock.setObjectName("Dock")
        Dock.setWindowModality(QtCore.Qt.WindowModal)
        Dock.resize(748, 510)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dock.sizePolicy().hasHeightForWidth())
        Dock.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/book_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dock.setWindowIcon(icon)
        Dock.setFloating(False)
        Dock.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
        Dock.setAllowedAreas(QtCore.Qt.TopDockWidgetArea)
        self.Contents = QtGui.QWidget()
        self.Contents.setObjectName("Contents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.Contents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtGui.QTabWidget(self.Contents)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        Dock.setWidget(self.Contents)

        self.retranslateUi(Dock)
        QtCore.QMetaObject.connectSlotsByName(Dock)

    def retranslateUi(self, Dock):
        Dock.setToolTip(QtGui.QApplication.translate("Dock", "Cadastro de Livros", None, QtGui.QApplication.UnicodeUTF8))
        Dock.setWindowTitle(QtGui.QApplication.translate("Dock", "Cadastro de Livros", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dock", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dock", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
