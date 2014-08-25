# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/oform_product.ui'
#
# Created: Mon Aug 25 20:22:26 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProductOForm(object):
    def setupUi(self, ProductOForm):
        ProductOForm.setObjectName("ProductOForm")
        ProductOForm.resize(730, 804)
        ProductOForm.setWidgetResizable(True)
        ProductOForm.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
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
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line = QtGui.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 4, 0, 1, 5)
        self.tableProducts = QtGui.QTableWidget(self.groupBox_2)
        self.tableProducts.setMinimumSize(QtCore.QSize(0, 130))
        self.tableProducts.setAlternatingRowColors(True)
        self.tableProducts.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableProducts.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableProducts.setObjectName("tableProducts")
        self.tableProducts.setColumnCount(0)
        self.tableProducts.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableProducts, 3, 0, 1, 5)
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
        self.gridLayout_4.addLayout(self.horizontalLayout, 5, 4, 1, 1)
        self.frame = QtGui.QFrame(self.groupBox_2)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.edProductName = QtGui.QLineEdit(self.frame)
        self.edProductName.setObjectName("edProductName")
        self.gridLayout.addWidget(self.edProductName, 0, 1, 2, 5)
        self.label = QtGui.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 33))
        self.label.setMaximumSize(QtCore.QSize(16777215, 33))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edPrice = QtGui.QLineEdit(self.frame)
        self.edPrice.setMaximumSize(QtCore.QSize(100, 16777215))
        self.edPrice.setMaxLength(7)
        self.edPrice.setObjectName("edPrice")
        self.gridLayout.addWidget(self.edPrice, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setMinimumSize(QtCore.QSize(0, 33))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 33))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 4)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 4)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(0, 33))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 33))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.edQuantityHolder = QtGui.QVBoxLayout()
        self.edQuantityHolder.setObjectName("edQuantityHolder")
        self.gridLayout.addLayout(self.edQuantityHolder, 3, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 1, 0, 2, 4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 5, 0, 1, 4)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtGui.QFrame(self.groupBox_2)
        self.frame_2.setMinimumSize(QtCore.QSize(140, 100))
        self.frame_2.setMaximumSize(QtCore.QSize(140, 100))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAddProduct = QtGui.QPushButton(self.frame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/product_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddProduct.setIcon(icon2)
        self.btnAddProduct.setAutoDefault(True)
        self.btnAddProduct.setObjectName("btnAddProduct")
        self.verticalLayout.addWidget(self.btnAddProduct)
        self.btnCleanProducts = QtGui.QPushButton(self.frame_2)
        self.btnCleanProducts.setIcon(icon1)
        self.btnCleanProducts.setAutoDefault(True)
        self.btnCleanProducts.setObjectName("btnCleanProducts")
        self.verticalLayout.addWidget(self.btnCleanProducts)
        self.verticalLayout_4.addWidget(self.frame_2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 1, 4, 2, 1)
        self.contentsLayout.addWidget(self.groupBox_2)
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
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rdPaid = QtGui.QRadioButton(self.groupBox_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/money_received.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rdPaid.setIcon(icon3)
        self.rdPaid.setChecked(True)
        self.rdPaid.setObjectName("rdPaid")
        self.radioMoney = QtGui.QButtonGroup(ProductOForm)
        self.radioMoney.setObjectName("radioMoney")
        self.radioMoney.addButton(self.rdPaid)
        self.horizontalLayout_2.addWidget(self.rdPaid)
        self.rdNotPaid = QtGui.QRadioButton(self.groupBox_4)
        self.rdNotPaid.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/money_unreceived.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rdNotPaid.setIcon(icon4)
        self.rdNotPaid.setObjectName("rdNotPaid")
        self.radioMoney.addButton(self.rdNotPaid)
        self.horizontalLayout_2.addWidget(self.rdNotPaid)
        self.contentsLayout.addWidget(self.groupBox_4)
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
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.edObs = QtGui.QPlainTextEdit(self.groupBox_3)
        self.edObs.setObjectName("edObs")
        self.gridLayout_5.addWidget(self.edObs, 0, 0, 1, 1)
        self.contentsLayout.addWidget(self.groupBox_3)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.contentsLayout.addItem(spacerItem5)
        ProductOForm.setWidget(self.FormContents)

        self.retranslateUi(ProductOForm)
        QtCore.QMetaObject.connectSlotsByName(ProductOForm)
        ProductOForm.setTabOrder(self.btnSelectAssociate, self.btnCleanAssociate)
        ProductOForm.setTabOrder(self.btnCleanAssociate, self.edProductName)
        ProductOForm.setTabOrder(self.edProductName, self.edPrice)
        ProductOForm.setTabOrder(self.edPrice, self.btnAddProduct)
        ProductOForm.setTabOrder(self.btnAddProduct, self.btnCleanProducts)
        ProductOForm.setTabOrder(self.btnCleanProducts, self.tableProducts)
        ProductOForm.setTabOrder(self.tableProducts, self.edObs)

    def retranslateUi(self, ProductOForm):
        ProductOForm.setWindowTitle(QtGui.QApplication.translate("ProductOForm", "ScrollArea", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setToolTip(QtGui.QApplication.translate("ProductOForm", "Dados do Associado", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ProductOForm", "Associado (Opcional)", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectAssociate.setText(QtGui.QApplication.translate("ProductOForm", "Adicionar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCleanAssociate.setText(QtGui.QApplication.translate("ProductOForm", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ProductOForm", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ProductOForm", "Apelido:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setToolTip(QtGui.QApplication.translate("ProductOForm", "Produtos do Bazar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ProductOForm", "Produtos do Bazar", None, QtGui.QApplication.UnicodeUTF8))
        self.tableProducts.setSortingEnabled(True)
        self.label_7.setText(QtGui.QApplication.translate("ProductOForm", "Total (R$):", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTotal.setText(QtGui.QApplication.translate("ProductOForm", "0,00", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProductOForm", "Produto:", None, QtGui.QApplication.UnicodeUTF8))
        self.edPrice.setText(QtGui.QApplication.translate("ProductOForm", "0,00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ProductOForm", "Quantidade:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ProductOForm", "Preço (R$):", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddProduct.setText(QtGui.QApplication.translate("ProductOForm", "Adicionar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCleanProducts.setText(QtGui.QApplication.translate("ProductOForm", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("ProductOForm", "Situação", None, QtGui.QApplication.UnicodeUTF8))
        self.rdPaid.setText(QtGui.QApplication.translate("ProductOForm", "Quitado", None, QtGui.QApplication.UnicodeUTF8))
        self.rdNotPaid.setText(QtGui.QApplication.translate("ProductOForm", "A receber", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setToolTip(QtGui.QApplication.translate("ProductOForm", "Observações", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ProductOForm", "Observações", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
