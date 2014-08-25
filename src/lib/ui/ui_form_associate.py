# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/form_associate.ui'
#
# Created: Mon Aug 25 20:22:26 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AssociateForm(object):
    def setupUi(self, AssociateForm):
        AssociateForm.setObjectName("AssociateForm")
        AssociateForm.resize(760, 617)
        AssociateForm.setWidgetResizable(True)
        self.FormContents = QtGui.QWidget()
        self.FormContents.setGeometry(QtCore.QRect(0, -353, 745, 968))
        self.FormContents.setObjectName("FormContents")
        self.contentsLayout = QtGui.QVBoxLayout(self.FormContents)
        self.contentsLayout.setObjectName("contentsLayout")
        self.groupBox_5 = QtGui.QGroupBox(self.FormContents)
        self.groupBox_5.setMaximumSize(QtCore.QSize(331, 16777215))
        self.groupBox_5.setStyleSheet(" QGroupBox {\n"
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
        self.groupBox_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.rdActive = QtGui.QRadioButton(self.groupBox_5)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/conn_succeeded.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rdActive.setIcon(icon)
        self.rdActive.setChecked(True)
        self.rdActive.setObjectName("rdActive")
        self.radioStatus = QtGui.QButtonGroup(AssociateForm)
        self.radioStatus.setObjectName("radioStatus")
        self.radioStatus.addButton(self.rdActive)
        self.gridLayout_5.addWidget(self.rdActive, 0, 0, 1, 1)
        self.rdInactive = QtGui.QRadioButton(self.groupBox_5)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/conn_failed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rdInactive.setIcon(icon1)
        self.rdInactive.setObjectName("rdInactive")
        self.radioStatus.addButton(self.rdInactive)
        self.gridLayout_5.addWidget(self.rdInactive, 0, 1, 1, 1)
        self.contentsLayout.addWidget(self.groupBox_5)
        self.groupBox = QtGui.QGroupBox(self.FormContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(703, 247))
        self.groupBox.setMaximumSize(QtCore.QSize(703, 231))
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
        self.gridLayout.setObjectName("gridLayout")
        self.comboMaritalStatus = QtGui.QComboBox(self.groupBox)
        self.comboMaritalStatus.setEditable(False)
        self.comboMaritalStatus.setObjectName("comboMaritalStatus")
        self.comboMaritalStatus.addItem("")
        self.comboMaritalStatus.addItem("")
        self.comboMaritalStatus.addItem("")
        self.comboMaritalStatus.addItem("")
        self.gridLayout.addWidget(self.comboMaritalStatus, 3, 2, 1, 1)
        self.edNickname = QtGui.QLineEdit(self.groupBox)
        self.edNickname.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.edNickname.setInputMask("")
        self.edNickname.setPlaceholderText("")
        self.edNickname.setObjectName("edNickname")
        self.gridLayout.addWidget(self.edNickname, 1, 1, 1, 4)
        self.edCPF = QtGui.QLineEdit(self.groupBox)
        self.edCPF.setPlaceholderText("")
        self.edCPF.setObjectName("edCPF")
        self.gridLayout.addWidget(self.edCPF, 2, 4, 1, 1)
        self.edRG = QtGui.QLineEdit(self.groupBox)
        self.edRG.setInputMask("")
        self.edRG.setObjectName("edRG")
        self.gridLayout.addWidget(self.edRG, 2, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edEmail = QtGui.QLineEdit(self.groupBox)
        self.edEmail.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.edEmail.setObjectName("edEmail")
        self.gridLayout.addWidget(self.edEmail, 5, 2, 1, 1)
        self.edFullName = QtGui.QLineEdit(self.groupBox)
        self.edFullName.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.edFullName.setObjectName("edFullName")
        self.gridLayout.addWidget(self.edFullName, 0, 1, 1, 4)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)
        self.contentsLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.FormContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(681, 235))
        self.groupBox_2.setMaximumSize(QtCore.QSize(703, 231))
        self.groupBox_2.setAutoFillBackground(False)
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
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.edStreet = QtGui.QLineEdit(self.groupBox_2)
        self.edStreet.setObjectName("edStreet")
        self.gridLayout_2.addWidget(self.edStreet, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.edComplement = QtGui.QLineEdit(self.groupBox_2)
        self.edComplement.setObjectName("edComplement")
        self.gridLayout_2.addWidget(self.edComplement, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.edDistrict = QtGui.QLineEdit(self.groupBox_2)
        self.edDistrict.setObjectName("edDistrict")
        self.gridLayout_2.addWidget(self.edDistrict, 2, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 2, 1, 1)
        self.comboProvince = QtGui.QComboBox(self.groupBox_2)
        self.comboProvince.setEditable(False)
        self.comboProvince.setObjectName("comboProvince")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.gridLayout_2.addWidget(self.comboProvince, 2, 3, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        self.edCity = QtGui.QLineEdit(self.groupBox_2)
        self.edCity.setObjectName("edCity")
        self.gridLayout_2.addWidget(self.edCity, 3, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 1)
        self.edCEP = QtGui.QLineEdit(self.groupBox_2)
        self.edCEP.setObjectName("edCEP")
        self.gridLayout_2.addWidget(self.edCEP, 4, 1, 1, 1)
        self.contentsLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.FormContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(331, 151))
        self.groupBox_3.setMaximumSize(QtCore.QSize(331, 151))
        self.groupBox_3.setAutoFillBackground(False)
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
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)
        self.edPhoneRes = QtGui.QLineEdit(self.groupBox_3)
        self.edPhoneRes.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.edPhoneRes.setPlaceholderText("")
        self.edPhoneRes.setObjectName("edPhoneRes")
        self.gridLayout_3.addWidget(self.edPhoneRes, 0, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)
        self.edPhoneCom = QtGui.QLineEdit(self.groupBox_3)
        self.edPhoneCom.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.edPhoneCom.setPlaceholderText("")
        self.edPhoneCom.setObjectName("edPhoneCom")
        self.gridLayout_3.addWidget(self.edPhoneCom, 1, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)
        self.edPhonePriv = QtGui.QLineEdit(self.groupBox_3)
        self.edPhonePriv.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.edPhonePriv.setPlaceholderText("")
        self.edPhonePriv.setObjectName("edPhonePriv")
        self.gridLayout_3.addWidget(self.edPhonePriv, 2, 1, 1, 1)
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
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.btnAddActivity = QtGui.QPushButton(self.groupBox_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/activity_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddActivity.setIcon(icon2)
        self.btnAddActivity.setObjectName("btnAddActivity")
        self.gridLayout_4.addWidget(self.btnAddActivity, 0, 0, 1, 1)
        self.btnCleanActivities = QtGui.QPushButton(self.groupBox_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCleanActivities.setIcon(icon3)
        self.btnCleanActivities.setObjectName("btnCleanActivities")
        self.gridLayout_4.addWidget(self.btnCleanActivities, 0, 2, 1, 1)
        self.tableActivities = QtGui.QTableWidget(self.groupBox_4)
        self.tableActivities.setMinimumSize(QtCore.QSize(0, 130))
        self.tableActivities.setAlternatingRowColors(True)
        self.tableActivities.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableActivities.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableActivities.setObjectName("tableActivities")
        self.tableActivities.setColumnCount(0)
        self.tableActivities.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableActivities, 1, 0, 1, 3)
        self.contentsLayout.addWidget(self.groupBox_4)
        AssociateForm.setWidget(self.FormContents)

        self.retranslateUi(AssociateForm)
        self.comboProvince.setCurrentIndex(24)
        QtCore.QMetaObject.connectSlotsByName(AssociateForm)
        AssociateForm.setTabOrder(self.rdActive, self.rdInactive)
        AssociateForm.setTabOrder(self.rdInactive, self.edFullName)
        AssociateForm.setTabOrder(self.edFullName, self.edNickname)
        AssociateForm.setTabOrder(self.edNickname, self.edRG)
        AssociateForm.setTabOrder(self.edRG, self.edCPF)
        AssociateForm.setTabOrder(self.edCPF, self.comboMaritalStatus)
        AssociateForm.setTabOrder(self.comboMaritalStatus, self.edEmail)
        AssociateForm.setTabOrder(self.edEmail, self.edStreet)
        AssociateForm.setTabOrder(self.edStreet, self.edComplement)
        AssociateForm.setTabOrder(self.edComplement, self.edDistrict)
        AssociateForm.setTabOrder(self.edDistrict, self.comboProvince)
        AssociateForm.setTabOrder(self.comboProvince, self.edCity)
        AssociateForm.setTabOrder(self.edCity, self.edCEP)
        AssociateForm.setTabOrder(self.edCEP, self.edPhoneRes)
        AssociateForm.setTabOrder(self.edPhoneRes, self.edPhoneCom)
        AssociateForm.setTabOrder(self.edPhoneCom, self.edPhonePriv)
        AssociateForm.setTabOrder(self.edPhonePriv, self.btnAddActivity)
        AssociateForm.setTabOrder(self.btnAddActivity, self.tableActivities)
        AssociateForm.setTabOrder(self.tableActivities, self.btnCleanActivities)

    def retranslateUi(self, AssociateForm):
        AssociateForm.setWindowTitle(QtGui.QApplication.translate("AssociateForm", "ScrollArea", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setToolTip(QtGui.QApplication.translate("AssociateForm", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("AssociateForm", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.rdActive.setText(QtGui.QApplication.translate("AssociateForm", "Ativo", None, QtGui.QApplication.UnicodeUTF8))
        self.rdInactive.setText(QtGui.QApplication.translate("AssociateForm", "Inativo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setToolTip(QtGui.QApplication.translate("AssociateForm", "Dados Pessoais", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("AssociateForm", "Dados Pessoais", None, QtGui.QApplication.UnicodeUTF8))
        self.comboMaritalStatus.setItemText(0, QtGui.QApplication.translate("AssociateForm", "Solteiro(a)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboMaritalStatus.setItemText(1, QtGui.QApplication.translate("AssociateForm", "Casado(a)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboMaritalStatus.setItemText(2, QtGui.QApplication.translate("AssociateForm", "Divorciado(a)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboMaritalStatus.setItemText(3, QtGui.QApplication.translate("AssociateForm", "Viúvo(a)", None, QtGui.QApplication.UnicodeUTF8))
        self.edCPF.setInputMask(QtGui.QApplication.translate("AssociateForm", "999.999.999-99;_", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AssociateForm", "CPF:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AssociateForm", "Apelido:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AssociateForm", "RG:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AssociateForm", "Estado Civil:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AssociateForm", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.edFullName.setPlaceholderText(QtGui.QApplication.translate("AssociateForm", "Nome completo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("AssociateForm", "E-Mail:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setToolTip(QtGui.QApplication.translate("AssociateForm", "Endereço", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("AssociateForm", "Endereço", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AssociateForm", "Logradouro:", None, QtGui.QApplication.UnicodeUTF8))
        self.edStreet.setPlaceholderText(QtGui.QApplication.translate("AssociateForm", "Rua e numeração", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("AssociateForm", "Complemento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("AssociateForm", "Bairro:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("AssociateForm", "Estado:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(0, QtGui.QApplication.translate("AssociateForm", "AC", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(1, QtGui.QApplication.translate("AssociateForm", "AL", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(2, QtGui.QApplication.translate("AssociateForm", "AP", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(3, QtGui.QApplication.translate("AssociateForm", "AM", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(4, QtGui.QApplication.translate("AssociateForm", "BA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(5, QtGui.QApplication.translate("AssociateForm", "CE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(6, QtGui.QApplication.translate("AssociateForm", "DF", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(7, QtGui.QApplication.translate("AssociateForm", "ES", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(8, QtGui.QApplication.translate("AssociateForm", "GO", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(9, QtGui.QApplication.translate("AssociateForm", "MA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(10, QtGui.QApplication.translate("AssociateForm", "MT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(11, QtGui.QApplication.translate("AssociateForm", "MS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(12, QtGui.QApplication.translate("AssociateForm", "MG", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(13, QtGui.QApplication.translate("AssociateForm", "PA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(14, QtGui.QApplication.translate("AssociateForm", "PB", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(15, QtGui.QApplication.translate("AssociateForm", "PR", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(16, QtGui.QApplication.translate("AssociateForm", "PE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(17, QtGui.QApplication.translate("AssociateForm", "PI", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(18, QtGui.QApplication.translate("AssociateForm", "RJ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(19, QtGui.QApplication.translate("AssociateForm", "RN", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(20, QtGui.QApplication.translate("AssociateForm", "RS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(21, QtGui.QApplication.translate("AssociateForm", "RO", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(22, QtGui.QApplication.translate("AssociateForm", "RR", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(23, QtGui.QApplication.translate("AssociateForm", "SC", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(24, QtGui.QApplication.translate("AssociateForm", "SP", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(25, QtGui.QApplication.translate("AssociateForm", "SE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboProvince.setItemText(26, QtGui.QApplication.translate("AssociateForm", "TO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("AssociateForm", "Cidade:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("AssociateForm", "CEP:", None, QtGui.QApplication.UnicodeUTF8))
        self.edCEP.setInputMask(QtGui.QApplication.translate("AssociateForm", "99.999-999;_", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setToolTip(QtGui.QApplication.translate("AssociateForm", "Telefones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("AssociateForm", "Telefones", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("AssociateForm", "Residencial:", None, QtGui.QApplication.UnicodeUTF8))
        self.edPhoneRes.setToolTip(QtGui.QApplication.translate("AssociateForm", "DDD + Número", None, QtGui.QApplication.UnicodeUTF8))
        self.edPhoneRes.setInputMask(QtGui.QApplication.translate("AssociateForm", "(DD)9999-9999;_", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("AssociateForm", "Comercial:", None, QtGui.QApplication.UnicodeUTF8))
        self.edPhoneCom.setToolTip(QtGui.QApplication.translate("AssociateForm", "DDD + Número", None, QtGui.QApplication.UnicodeUTF8))
        self.edPhoneCom.setInputMask(QtGui.QApplication.translate("AssociateForm", "(DD)9999-9999;_", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("AssociateForm", "Celular:", None, QtGui.QApplication.UnicodeUTF8))
        self.edPhonePriv.setToolTip(QtGui.QApplication.translate("AssociateForm", "DDD + Número", None, QtGui.QApplication.UnicodeUTF8))
        self.edPhonePriv.setInputMask(QtGui.QApplication.translate("AssociateForm", "(DD)99999-9999;_", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setToolTip(QtGui.QApplication.translate("AssociateForm", "Atividades", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("AssociateForm", "Atividades na casa", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddActivity.setText(QtGui.QApplication.translate("AssociateForm", "Adicionar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCleanActivities.setText(QtGui.QApplication.translate("AssociateForm", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.tableActivities.setSortingEnabled(True)

import icons_rc
