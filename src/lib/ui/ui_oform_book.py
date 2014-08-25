# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/oform_book.ui'
#
# Created: Mon Aug 25 20:22:26 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BookOForm(object):
    def setupUi(self, BookOForm):
        BookOForm.setObjectName("BookOForm")
        BookOForm.resize(730, 804)
        BookOForm.setWidgetResizable(True)
        BookOForm.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.FormContents = QtGui.QWidget()
        self.FormContents.setGeometry(QtCore.QRect(0, 0, 728, 802))
        self.FormContents.setObjectName("FormContents")
        self.contentsLayout = QtGui.QVBoxLayout(self.FormContents)
        self.contentsLayout.setSpacing(6)
        self.contentsLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.contentsLayout.setContentsMargins(-1, 9, -1, -1)
        self.contentsLayout.setObjectName("contentsLayout")
        self.groupBox = QtGui.QGroupBox(self.FormContents)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(703, 16777215))
        self.groupBox.setStyleSheet(" QGroupBox {\n"
"     font-weight: bold;\n"
"     border: 2px solid gray;\n"
"     border-radius: 5px;\n"
"     margin-top: 25px;\n"
" }\n"
"\n"
" QGroupBox::title {\n"
"     background-color: transparent;\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top left;\n"
" }")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 2, 1, 1)
        self.btnSelectAssociate = QtGui.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/associate_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSelectAssociate.setIcon(icon)
        self.btnSelectAssociate.setObjectName("btnSelectAssociate")
        self.gridLayout_2.addWidget(self.btnSelectAssociate, 2, 0, 1, 1)
        self.btnCleanAssociate = QtGui.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCleanAssociate.setIcon(icon1)
        self.btnCleanAssociate.setAutoDefault(True)
        self.btnCleanAssociate.setObjectName("btnCleanAssociate")
        self.gridLayout_2.addWidget(self.btnCleanAssociate, 2, 3, 1, 1)
        self.frameAssociate = QtGui.QFrame(self.groupBox)
        self.frameAssociate.setEnabled(True)
        self.frameAssociate.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameAssociate.setFrameShadow(QtGui.QFrame.Raised)
        self.frameAssociate.setObjectName("frameAssociate")
        self.gridLayout_3 = QtGui.QGridLayout(self.frameAssociate)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtGui.QLabel(self.frameAssociate)
        self.label_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.lblName = QtGui.QLabel(self.frameAssociate)
        self.lblName.setStyleSheet(" QLabel {\n"
"     color: rgb(0, 0, 255);\n"
" }")
        self.lblName.setText("")
        self.lblName.setObjectName("lblName")
        self.gridLayout_3.addWidget(self.lblName, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.frameAssociate)
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.lblNickname = QtGui.QLabel(self.frameAssociate)
        self.lblNickname.setStyleSheet(" QLabel {\n"
"     color: rgb(0, 0, 255);\n"
" }")
        self.lblNickname.setText("")
        self.lblNickname.setObjectName("lblNickname")
        self.gridLayout_3.addWidget(self.lblNickname, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frameAssociate, 3, 0, 1, 4)
        self.contentsLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.FormContents)
        self.groupBox_2.setMaximumSize(QtCore.QSize(703, 16777215))
        self.groupBox_2.setStyleSheet(" QGroupBox {\n"
"     font-weight: bold;\n"
"     border: 2px solid gray;\n"
"     border-radius: 5px;\n"
"     margin-top: 25px;\n"
" }\n"
"\n"
" QGroupBox::title {\n"
"     background-color: transparent;\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top left;\n"
" }")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtGui.QFrame(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(533, 100))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 33))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.edBarcode = QtGui.QLineEdit(self.frame)
        self.edBarcode.setMaximumSize(QtCore.QSize(16777215, 33))
        self.edBarcode.setMaxLength(13)
        self.edBarcode.setObjectName("edBarcode")
        self.verticalLayout_2.addWidget(self.edBarcode)
        self.horizontalLayout_5.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(140, 100))
        self.frame_2.setMaximumSize(QtCore.QSize(140, 100))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnSelectBook = QtGui.QPushButton(self.frame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSelectBook.setIcon(icon2)
        self.btnSelectBook.setAutoDefault(True)
        self.btnSelectBook.setObjectName("btnSelectBook")
        self.verticalLayout.addWidget(self.btnSelectBook)
        self.btnCleanBooks = QtGui.QPushButton(self.frame_2)
        self.btnCleanBooks.setIcon(icon1)
        self.btnCleanBooks.setAutoDefault(True)
        self.btnCleanBooks.setObjectName("btnCleanBooks")
        self.verticalLayout.addWidget(self.btnCleanBooks)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 2)
        self.tableBooks = QtGui.QTableWidget(self.groupBox_2)
        self.tableBooks.setMinimumSize(QtCore.QSize(0, 130))
        self.tableBooks.setMaximumSize(QtCore.QSize(681, 16777215))
        self.tableBooks.setAlternatingRowColors(True)
        self.tableBooks.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableBooks.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableBooks.setObjectName("tableBooks")
        self.tableBooks.setColumnCount(0)
        self.tableBooks.setRowCount(0)
        self.gridLayout.addWidget(self.tableBooks, 1, 0, 1, 2)
        self.line = QtGui.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.lblTotal = QtGui.QLabel(self.groupBox_2)
        self.lblTotal.setStyleSheet(" QLabel {\n"
"     color: rgb(0, 0, 255);\n"
" }")
        self.lblTotal.setObjectName("lblTotal")
        self.horizontalLayout.addWidget(self.lblTotal)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.contentsLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.FormContents)
        self.groupBox_3.setMaximumSize(QtCore.QSize(703, 16777215))
        self.groupBox_3.setStyleSheet(" QGroupBox {\n"
"     font-weight: bold;\n"
"     border: 2px solid gray;\n"
"     border-radius: 5px;\n"
"     margin-top: 25px;\n"
" }\n"
"\n"
" QGroupBox::title {\n"
"     background-color: transparent;\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top left;\n"
" }")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rdPaid = QtGui.QRadioButton(self.groupBox_3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/money_received.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rdPaid.setIcon(icon3)
        self.rdPaid.setChecked(True)
        self.rdPaid.setObjectName("rdPaid")
        self.radioMoney = QtGui.QButtonGroup(BookOForm)
        self.radioMoney.setObjectName("radioMoney")
        self.radioMoney.addButton(self.rdPaid)
        self.horizontalLayout_2.addWidget(self.rdPaid)
        self.rdNotPaid = QtGui.QRadioButton(self.groupBox_3)
        self.rdNotPaid.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/money_unreceived.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rdNotPaid.setIcon(icon4)
        self.rdNotPaid.setObjectName("rdNotPaid")
        self.radioMoney.addButton(self.rdNotPaid)
        self.horizontalLayout_2.addWidget(self.rdNotPaid)
        self.contentsLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.FormContents)
        self.groupBox_4.setMaximumSize(QtCore.QSize(703, 16777215))
        self.groupBox_4.setStyleSheet(" QGroupBox {\n"
"     font-weight: bold;\n"
"     border: 2px solid gray;\n"
"     border-radius: 5px;\n"
"     margin-top: 25px;\n"
" }\n"
"\n"
" QGroupBox::title {\n"
"     background-color: transparent;\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top left;\n"
" }")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.edObs = QtGui.QPlainTextEdit(self.groupBox_4)
        self.edObs.setObjectName("edObs")
        self.gridLayout_5.addWidget(self.edObs, 0, 0, 1, 1)
        self.contentsLayout.addWidget(self.groupBox_4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.contentsLayout.addItem(spacerItem2)
        BookOForm.setWidget(self.FormContents)

        self.retranslateUi(BookOForm)
        QtCore.QMetaObject.connectSlotsByName(BookOForm)
        BookOForm.setTabOrder(self.btnSelectAssociate, self.btnCleanAssociate)
        BookOForm.setTabOrder(self.btnCleanAssociate, self.edBarcode)
        BookOForm.setTabOrder(self.edBarcode, self.btnSelectBook)
        BookOForm.setTabOrder(self.btnSelectBook, self.btnCleanBooks)
        BookOForm.setTabOrder(self.btnCleanBooks, self.tableBooks)
        BookOForm.setTabOrder(self.tableBooks, self.rdPaid)
        BookOForm.setTabOrder(self.rdPaid, self.rdNotPaid)
        BookOForm.setTabOrder(self.rdNotPaid, self.edObs)

    def retranslateUi(self, BookOForm):
        BookOForm.setWindowTitle(QtGui.QApplication.translate("BookOForm", "ScrollArea", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setToolTip(QtGui.QApplication.translate("BookOForm", "Dados do Associado", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("BookOForm", "Associado (Opcional)", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectAssociate.setText(QtGui.QApplication.translate("BookOForm", "Adicionar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCleanAssociate.setText(QtGui.QApplication.translate("BookOForm", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("BookOForm", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("BookOForm", "Apelido:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setToolTip(QtGui.QApplication.translate("BookOForm", "Livros", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("BookOForm", "Livros", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("BookOForm", "Código de Barras:", None, QtGui.QApplication.UnicodeUTF8))
        self.edBarcode.setPlaceholderText(QtGui.QApplication.translate("BookOForm", "Digite o código de barras ou clique em \"Adicionar\"", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectBook.setToolTip(QtGui.QApplication.translate("BookOForm", "Selecionar livro de uma lista", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectBook.setText(QtGui.QApplication.translate("BookOForm", "Adicionar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCleanBooks.setToolTip(QtGui.QApplication.translate("BookOForm", "Limpar Itens", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCleanBooks.setText(QtGui.QApplication.translate("BookOForm", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.tableBooks.setSortingEnabled(True)
        self.label_7.setText(QtGui.QApplication.translate("BookOForm", "Total (R$):", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTotal.setToolTip(QtGui.QApplication.translate("BookOForm", "Total calculado", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTotal.setText(QtGui.QApplication.translate("BookOForm", "0,00", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("BookOForm", "Situação", None, QtGui.QApplication.UnicodeUTF8))
        self.rdPaid.setText(QtGui.QApplication.translate("BookOForm", "Quitado", None, QtGui.QApplication.UnicodeUTF8))
        self.rdNotPaid.setText(QtGui.QApplication.translate("BookOForm", "A receber", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setToolTip(QtGui.QApplication.translate("BookOForm", "Observações", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("BookOForm", "Observações", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
