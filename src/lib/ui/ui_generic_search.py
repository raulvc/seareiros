# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/generic_search.ui'
#
# Created: Thu Jul 17 10:44:50 2014
#      by: pyside-uic 0.2.14 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SearchForm(object):
    def setupUi(self, SearchForm):
        SearchForm.setObjectName("SearchForm")
        SearchForm.resize(695, 363)
        SearchForm.setWindowTitle("")
        self.verticalLayout = QtGui.QVBoxLayout(SearchForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.edKeyword = QtGui.QLineEdit(SearchForm)
        self.edKeyword.setObjectName("edKeyword")
        self.gridLayout.addWidget(self.edKeyword, 0, 1, 1, 1)
        self.viewSearch = QtGui.QTableView(SearchForm)
        self.viewSearch.setAlternatingRowColors(True)
        self.viewSearch.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.viewSearch.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.viewSearch.setObjectName("viewSearch")
        self.gridLayout.addWidget(self.viewSearch, 1, 0, 1, 4)
        self.btnRefresh = QtGui.QPushButton(SearchForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/loading.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefresh.setIcon(icon)
        self.btnRefresh.setObjectName("btnRefresh")
        self.gridLayout.addWidget(self.btnRefresh, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label = QtGui.QLabel(SearchForm)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(SearchForm)
        QtCore.QMetaObject.connectSlotsByName(SearchForm)

    def retranslateUi(self, SearchForm):
        self.edKeyword.setPlaceholderText(QtGui.QApplication.translate("SearchForm", "Digite a palavra-chave", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefresh.setText(QtGui.QApplication.translate("SearchForm", "Atualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SearchForm", "Filtrar:", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
