# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/main.ui'
#
# Created: Wed Aug 13 16:30:15 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAdd = QtGui.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        self.menuOrder = QtGui.QMenu(self.menubar)
        self.menuOrder.setObjectName("menuOrder")
        self.menuReports = QtGui.QMenu(self.menubar)
        self.menuReports.setObjectName("menuReports")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuLibrary = QtGui.QMenu(self.menubar)
        self.menuLibrary.setObjectName("menuLibrary")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.NoToolBarArea)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setIconVisibleInMenu(True)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon2)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAddAssociate = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/associate_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddAssociate.setIcon(icon3)
        self.actionAddAssociate.setIconVisibleInMenu(True)
        self.actionAddAssociate.setObjectName("actionAddAssociate")
        self.actionSellBook = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSellBook.setIcon(icon4)
        self.actionSellBook.setIconVisibleInMenu(True)
        self.actionSellBook.setObjectName("actionSellBook")
        self.actionSellProduct = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/product.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSellProduct.setIcon(icon5)
        self.actionSellProduct.setIconVisibleInMenu(True)
        self.actionSellProduct.setObjectName("actionSellProduct")
        self.actionSellEvent = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/events.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSellEvent.setIcon(icon6)
        self.actionSellEvent.setIconVisibleInMenu(True)
        self.actionSellEvent.setObjectName("actionSellEvent")
        self.actionAddBook = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/book_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddBook.setIcon(icon7)
        self.actionAddBook.setIconVisibleInMenu(True)
        self.actionAddBook.setObjectName("actionAddBook")
        self.actionAddProduct = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/product_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddProduct.setIcon(icon8)
        self.actionAddProduct.setIconVisibleInMenu(True)
        self.actionAddProduct.setObjectName("actionAddProduct")
        self.actionLibLend = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/book_lend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLibLend.setIcon(icon9)
        self.actionLibLend.setIconVisibleInMenu(True)
        self.actionLibLend.setObjectName("actionLibLend")
        self.actionLibReturn = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/book_return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLibReturn.setIcon(icon10)
        self.actionLibReturn.setIconVisibleInMenu(True)
        self.actionLibReturn.setObjectName("actionLibReturn")
        self.actionPreferences = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/preferences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon11)
        self.actionPreferences.setIconVisibleInMenu(True)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon12)
        self.actionCopy.setIconVisibleInMenu(True)
        self.actionCopy.setObjectName("actionCopy")
        self.actionRepSales = QtGui.QAction(MainWindow)
        self.actionRepSales.setObjectName("actionRepSales")
        self.actionRepLibrary = QtGui.QAction(MainWindow)
        self.actionRepLibrary.setObjectName("actionRepLibrary")
        self.actionRepProduct = QtGui.QAction(MainWindow)
        self.actionRepProduct.setObjectName("actionRepProduct")
        self.actionRepBook = QtGui.QAction(MainWindow)
        self.actionRepBook.setObjectName("actionRepBook")
        self.actionSearch = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch.setIcon(icon13)
        self.actionSearch.setObjectName("actionSearch")
        self.actionPendencies = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/pending.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPendencies.setIcon(icon14)
        self.actionPendencies.setObjectName("actionPendencies")
        self.actionAddActivity = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/activity_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddActivity.setIcon(icon15)
        self.actionAddActivity.setIconVisibleInMenu(True)
        self.actionAddActivity.setObjectName("actionAddActivity")
        self.menuFile.addAction(self.actionExit)
        self.menuAdd.addAction(self.actionAddAssociate)
        self.menuAdd.addAction(self.actionAddActivity)
        self.menuAdd.addAction(self.actionAddBook)
        self.menuOrder.addAction(self.actionSellBook)
        self.menuOrder.addAction(self.actionSellProduct)
        self.menuOrder.addAction(self.actionSellEvent)
        self.menuReports.addAction(self.actionRepSales)
        self.menuReports.addAction(self.actionRepBook)
        self.menuReports.addAction(self.actionRepProduct)
        self.menuReports.addAction(self.actionRepLibrary)
        self.menuHelp.addAction(self.actionAbout)
        self.menuLibrary.addAction(self.actionLibLend)
        self.menuLibrary.addAction(self.actionLibReturn)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuOrder.menuAction())
        self.menubar.addAction(self.menuLibrary.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionSellBook)
        self.toolBar.addAction(self.actionSellProduct)
        self.toolBar.addAction(self.actionSellEvent)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSearch)
        self.toolBar.addAction(self.actionPendencies)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Seareiros", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdd.setTitle(QtGui.QApplication.translate("MainWindow", "&Cadastros", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOrder.setTitle(QtGui.QApplication.translate("MainWindow", "&Vendas", None, QtGui.QApplication.UnicodeUTF8))
        self.menuReports.setTitle(QtGui.QApplication.translate("MainWindow", "&Relatórios", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Ajuda", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLibrary.setTitle(QtGui.QApplication.translate("MainWindow", "&Biblioteca", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "&Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "Sobre", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddAssociate.setText(QtGui.QApplication.translate("MainWindow", "Associado", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSellBook.setText(QtGui.QApplication.translate("MainWindow", "Livros", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSellProduct.setText(QtGui.QApplication.translate("MainWindow", "Bazar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSellEvent.setText(QtGui.QApplication.translate("MainWindow", "Eventos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddBook.setText(QtGui.QApplication.translate("MainWindow", "Livro", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddProduct.setText(QtGui.QApplication.translate("MainWindow", "Produto", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLibLend.setText(QtGui.QApplication.translate("MainWindow", "Alugar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLibReturn.setText(QtGui.QApplication.translate("MainWindow", "Devolver", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferências", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copiar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRepSales.setText(QtGui.QApplication.translate("MainWindow", "Vendas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRepLibrary.setText(QtGui.QApplication.translate("MainWindow", "Biblioteca", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRepProduct.setText(QtGui.QApplication.translate("MainWindow", "Bazar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRepBook.setText(QtGui.QApplication.translate("MainWindow", "Livros", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setText(QtGui.QApplication.translate("MainWindow", "Pesquisar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setToolTip(QtGui.QApplication.translate("MainWindow", "Pesquisar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPendencies.setText(QtGui.QApplication.translate("MainWindow", "Pendências", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPendencies.setToolTip(QtGui.QApplication.translate("MainWindow", "Pendências", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddActivity.setText(QtGui.QApplication.translate("MainWindow", "Atividade", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
