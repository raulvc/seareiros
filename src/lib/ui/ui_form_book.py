# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/form_book.ui'
#
# Created: Mon Aug 25 20:22:26 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BookForm(object):
    def setupUi(self, BookForm):
        BookForm.setObjectName("BookForm")
        BookForm.resize(730, 744)
        BookForm.setWidgetResizable(True)
        BookForm.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.FormContents = QtGui.QWidget()
        self.FormContents.setGeometry(QtCore.QRect(0, 0, 728, 742))
        self.FormContents.setObjectName("FormContents")
        self.contentsLayout = QtGui.QVBoxLayout(self.FormContents)
        self.contentsLayout.setSpacing(6)
        self.contentsLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.contentsLayout.setContentsMargins(-1, 9, -1, -1)
        self.contentsLayout.setObjectName("contentsLayout")
        self.groupBox = QtGui.QGroupBox(self.FormContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(703, 500))
        self.groupBox.setToolTip("")
        self.groupBox.setAutoFillBackground(False)
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
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.edDescription = QtGui.QPlainTextEdit(self.groupBox)
        self.edDescription.setObjectName("edDescription")
        self.gridLayout.addWidget(self.edDescription, 7, 2, 1, 5)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(76, 0))
        self.label.setMaximumSize(QtCore.QSize(76, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 2, 1, 1)
        self.edYearHolder = QtGui.QVBoxLayout()
        self.edYearHolder.setObjectName("edYearHolder")
        self.gridLayout.addLayout(self.edYearHolder, 5, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 4, 1, 1)
        self.edAuthor = QtGui.QLineEdit(self.groupBox)
        self.edAuthor.setObjectName("edAuthor")
        self.gridLayout.addWidget(self.edAuthor, 2, 3, 1, 4)
        self.edSAuthor = QtGui.QLineEdit(self.groupBox)
        self.edSAuthor.setObjectName("edSAuthor")
        self.gridLayout.addWidget(self.edSAuthor, 3, 3, 1, 4)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 2, 1, 1)
        self.edPublisher = QtGui.QLineEdit(self.groupBox)
        self.edPublisher.setObjectName("edPublisher")
        self.gridLayout.addWidget(self.edPublisher, 4, 3, 1, 4)
        self.edBarcode = QtGui.QLineEdit(self.groupBox)
        self.edBarcode.setMaxLength(13)
        self.edBarcode.setObjectName("edBarcode")
        self.gridLayout.addWidget(self.edBarcode, 0, 2, 1, 5)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.edImage = QtGui.QLabel(self.groupBox)
        self.edImage.setMinimumSize(QtCore.QSize(151, 151))
        self.edImage.setMaximumSize(QtCore.QSize(151, 151))
        self.edImage.setFrameShape(QtGui.QFrame.Box)
        self.edImage.setText("")
        self.edImage.setPixmap(QtGui.QPixmap(":/icons/no_image.png"))
        self.edImage.setObjectName("edImage")
        self.gridLayout.addWidget(self.edImage, 1, 0, 5, 1)
        self.edPrice = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edPrice.sizePolicy().hasHeightForWidth())
        self.edPrice.setSizePolicy(sizePolicy)
        self.edPrice.setMinimumSize(QtCore.QSize(100, 0))
        self.edPrice.setMaximumSize(QtCore.QSize(100, 16777215))
        self.edPrice.setObjectName("edPrice")
        self.gridLayout.addWidget(self.edPrice, 5, 5, 1, 1)
        self.edTitle = QtGui.QLineEdit(self.groupBox)
        self.edTitle.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edTitle.setObjectName("edTitle")
        self.gridLayout.addWidget(self.edTitle, 1, 3, 1, 4)
        self.label_2 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(76, 0))
        self.label_2.setMaximumSize(QtCore.QSize(76, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.contentsLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.FormContents)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
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
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rdSell = QtGui.QRadioButton(self.groupBox_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rdSell.setIcon(icon)
        self.rdSell.setChecked(True)
        self.rdSell.setObjectName("rdSell")
        self.radioAvailability = QtGui.QButtonGroup(BookForm)
        self.radioAvailability.setObjectName("radioAvailability")
        self.radioAvailability.addButton(self.rdSell)
        self.gridLayout_2.addWidget(self.rdSell, 0, 0, 1, 1)
        self.rdRent = QtGui.QRadioButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/book_lend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rdRent.setIcon(icon1)
        self.rdRent.setObjectName("rdRent")
        self.radioAvailability.addButton(self.rdRent)
        self.gridLayout_2.addWidget(self.rdRent, 0, 1, 1, 1)
        self.rdInactive = QtGui.QRadioButton(self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/conn_failed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rdInactive.setIcon(icon2)
        self.rdInactive.setObjectName("rdInactive")
        self.radioAvailability.addButton(self.rdInactive)
        self.gridLayout_2.addWidget(self.rdInactive, 0, 2, 1, 1)
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
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableSubjects = QtGui.QTableWidget(self.groupBox_3)
        self.tableSubjects.setMinimumSize(QtCore.QSize(0, 130))
        self.tableSubjects.setAlternatingRowColors(True)
        self.tableSubjects.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableSubjects.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableSubjects.setObjectName("tableSubjects")
        self.tableSubjects.setColumnCount(0)
        self.tableSubjects.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableSubjects, 1, 0, 1, 4)
        self.btnCleanSubjects = QtGui.QPushButton(self.groupBox_3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCleanSubjects.setIcon(icon3)
        self.btnCleanSubjects.setObjectName("btnCleanSubjects")
        self.gridLayout_4.addWidget(self.btnCleanSubjects, 0, 3, 1, 1)
        self.btnAddSubject = QtGui.QPushButton(self.groupBox_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/activity_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddSubject.setIcon(icon4)
        self.btnAddSubject.setObjectName("btnAddSubject")
        self.gridLayout_4.addWidget(self.btnAddSubject, 0, 1, 1, 1)
        self.edSubject = QtGui.QLineEdit(self.groupBox_3)
        self.edSubject.setObjectName("edSubject")
        self.gridLayout_4.addWidget(self.edSubject, 0, 0, 1, 1)
        self.contentsLayout.addWidget(self.groupBox_3)
        BookForm.setWidget(self.FormContents)

        self.retranslateUi(BookForm)
        QtCore.QMetaObject.connectSlotsByName(BookForm)
        BookForm.setTabOrder(self.edBarcode, self.edTitle)
        BookForm.setTabOrder(self.edTitle, self.edAuthor)
        BookForm.setTabOrder(self.edAuthor, self.edSAuthor)
        BookForm.setTabOrder(self.edSAuthor, self.edPublisher)
        BookForm.setTabOrder(self.edPublisher, self.edPrice)
        BookForm.setTabOrder(self.edPrice, self.edDescription)
        BookForm.setTabOrder(self.edDescription, self.rdSell)
        BookForm.setTabOrder(self.rdSell, self.rdRent)
        BookForm.setTabOrder(self.rdRent, self.rdInactive)
        BookForm.setTabOrder(self.rdInactive, self.edSubject)
        BookForm.setTabOrder(self.edSubject, self.btnAddSubject)
        BookForm.setTabOrder(self.btnAddSubject, self.btnCleanSubjects)
        BookForm.setTabOrder(self.btnCleanSubjects, self.tableSubjects)

    def retranslateUi(self, BookForm):
        BookForm.setWindowTitle(QtGui.QApplication.translate("BookForm", "ScrollArea", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("BookForm", "Dados", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("BookForm", "Título:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("BookForm", "Ano:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("BookForm", "Preço (R$):", None, QtGui.QApplication.UnicodeUTF8))
        self.edAuthor.setPlaceholderText(QtGui.QApplication.translate("BookForm", "Autor encarnado", None, QtGui.QApplication.UnicodeUTF8))
        self.edSAuthor.setPlaceholderText(QtGui.QApplication.translate("BookForm", "Autor espírito (se houver)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("BookForm", "Editora:", None, QtGui.QApplication.UnicodeUTF8))
        self.edPublisher.setPlaceholderText(QtGui.QApplication.translate("BookForm", "Nome da Editora", None, QtGui.QApplication.UnicodeUTF8))
        self.edBarcode.setPlaceholderText(QtGui.QApplication.translate("BookForm", "Código de barras, se houver", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("BookForm", "Descrição:", None, QtGui.QApplication.UnicodeUTF8))
        self.edPrice.setText(QtGui.QApplication.translate("BookForm", "0,00", None, QtGui.QApplication.UnicodeUTF8))
        self.edTitle.setPlaceholderText(QtGui.QApplication.translate("BookForm", "Nome da obra", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("BookForm", "Autoria:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("BookForm", "Código de Barras:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setToolTip(QtGui.QApplication.translate("BookForm", "Disponibilidade", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("BookForm", "Disponibilidade", None, QtGui.QApplication.UnicodeUTF8))
        self.rdSell.setText(QtGui.QApplication.translate("BookForm", "Venda", None, QtGui.QApplication.UnicodeUTF8))
        self.rdRent.setText(QtGui.QApplication.translate("BookForm", "Locação", None, QtGui.QApplication.UnicodeUTF8))
        self.rdInactive.setText(QtGui.QApplication.translate("BookForm", "Inativo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setToolTip(QtGui.QApplication.translate("BookForm", "Temas", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("BookForm", "Temas", None, QtGui.QApplication.UnicodeUTF8))
        self.tableSubjects.setSortingEnabled(True)
        self.btnCleanSubjects.setText(QtGui.QApplication.translate("BookForm", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddSubject.setText(QtGui.QApplication.translate("BookForm", "Adicionar", None, QtGui.QApplication.UnicodeUTF8))
        self.edSubject.setPlaceholderText(QtGui.QApplication.translate("BookForm", "Assuntos relacionados ao livro", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
