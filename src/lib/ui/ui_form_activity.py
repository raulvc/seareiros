# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/form_activity.ui'
#
# Created: Sat Aug 30 08:19:34 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ActivityForm(object):
    def setupUi(self, ActivityForm):
        ActivityForm.setObjectName("ActivityForm")
        ActivityForm.resize(745, 510)
        ActivityForm.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 743, 508))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(703, 247))
        self.groupBox.setMaximumSize(QtCore.QSize(703, 231))
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
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.comboRoom = QtGui.QComboBox(self.groupBox)
        self.comboRoom.setObjectName("comboRoom")
        self.comboRoom.addItem("")
        self.comboRoom.addItem("")
        self.comboRoom.addItem("")
        self.comboRoom.addItem("")
        self.comboRoom.addItem("")
        self.comboRoom.addItem("")
        self.comboRoom.addItem("")
        self.comboRoom.addItem("")
        self.comboRoom.addItem("")
        self.comboRoom.addItem("")
        self.comboRoom.addItem("")
        self.comboRoom.addItem("")
        self.comboRoom.addItem("")
        self.gridLayout.addWidget(self.comboRoom, 1, 1, 1, 2)
        self.editTime = QtGui.QTimeEdit(self.groupBox)
        self.editTime.setTime(QtCore.QTime(19, 0, 0))
        self.editTime.setObjectName("editTime")
        self.gridLayout.addWidget(self.editTime, 3, 1, 1, 1)
        self.comboDescription = QtGui.QComboBox(self.groupBox)
        self.comboDescription.setEditable(False)
        self.comboDescription.setObjectName("comboDescription")
        self.comboDescription.addItem("")
        self.comboDescription.addItem("")
        self.comboDescription.addItem("")
        self.comboDescription.addItem("")
        self.comboDescription.addItem("")
        self.comboDescription.addItem("")
        self.gridLayout.addWidget(self.comboDescription, 0, 1, 1, 3)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rd_weekday0 = QtGui.QRadioButton(self.groupBox)
        self.rd_weekday0.setChecked(True)
        self.rd_weekday0.setObjectName("rd_weekday0")
        self.grpWeekday = QtGui.QButtonGroup(ActivityForm)
        self.grpWeekday.setObjectName("grpWeekday")
        self.grpWeekday.addButton(self.rd_weekday0)
        self.horizontalLayout.addWidget(self.rd_weekday0)
        self.rd_weekday1 = QtGui.QRadioButton(self.groupBox)
        self.rd_weekday1.setObjectName("rd_weekday1")
        self.grpWeekday.addButton(self.rd_weekday1)
        self.horizontalLayout.addWidget(self.rd_weekday1)
        self.rd_weekday2 = QtGui.QRadioButton(self.groupBox)
        self.rd_weekday2.setObjectName("rd_weekday2")
        self.grpWeekday.addButton(self.rd_weekday2)
        self.horizontalLayout.addWidget(self.rd_weekday2)
        self.rd_weekday3 = QtGui.QRadioButton(self.groupBox)
        self.rd_weekday3.setObjectName("rd_weekday3")
        self.grpWeekday.addButton(self.rd_weekday3)
        self.horizontalLayout.addWidget(self.rd_weekday3)
        self.rd_weekday4 = QtGui.QRadioButton(self.groupBox)
        self.rd_weekday4.setObjectName("rd_weekday4")
        self.grpWeekday.addButton(self.rd_weekday4)
        self.horizontalLayout.addWidget(self.rd_weekday4)
        self.rd_weekday5 = QtGui.QRadioButton(self.groupBox)
        self.rd_weekday5.setObjectName("rd_weekday5")
        self.grpWeekday.addButton(self.rd_weekday5)
        self.horizontalLayout.addWidget(self.rd_weekday5)
        self.rd_weekday6 = QtGui.QRadioButton(self.groupBox)
        self.rd_weekday6.setObjectName("rd_weekday6")
        self.grpWeekday.addButton(self.rd_weekday6)
        self.horizontalLayout.addWidget(self.rd_weekday6)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 3)
        self.verticalLayout.addWidget(self.groupBox)
        ActivityForm.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(ActivityForm)
        QtCore.QMetaObject.connectSlotsByName(ActivityForm)
        ActivityForm.setTabOrder(self.comboDescription, self.comboRoom)
        ActivityForm.setTabOrder(self.comboRoom, self.editTime)

    def retranslateUi(self, ActivityForm):
        ActivityForm.setWindowTitle(QtGui.QApplication.translate("ActivityForm", "ScrollArea", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ActivityForm", "Atividade", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ActivityForm", "Descrição:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ActivityForm", "Dia da Semana:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(0, QtGui.QApplication.translate("ActivityForm", "Nenhuma", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(1, QtGui.QApplication.translate("ActivityForm", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(2, QtGui.QApplication.translate("ActivityForm", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(3, QtGui.QApplication.translate("ActivityForm", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(4, QtGui.QApplication.translate("ActivityForm", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(5, QtGui.QApplication.translate("ActivityForm", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(6, QtGui.QApplication.translate("ActivityForm", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(7, QtGui.QApplication.translate("ActivityForm", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(8, QtGui.QApplication.translate("ActivityForm", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(9, QtGui.QApplication.translate("ActivityForm", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(10, QtGui.QApplication.translate("ActivityForm", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(11, QtGui.QApplication.translate("ActivityForm", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.comboRoom.setItemText(12, QtGui.QApplication.translate("ActivityForm", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.editTime.setDisplayFormat(QtGui.QApplication.translate("ActivityForm", "HH:mm", None, QtGui.QApplication.UnicodeUTF8))
        self.comboDescription.setItemText(0, QtGui.QApplication.translate("ActivityForm", "Atendimento Fraterno", None, QtGui.QApplication.UnicodeUTF8))
        self.comboDescription.setItemText(1, QtGui.QApplication.translate("ActivityForm", "Reunião Pública", None, QtGui.QApplication.UnicodeUTF8))
        self.comboDescription.setItemText(2, QtGui.QApplication.translate("ActivityForm", "Reunião de Estudos", None, QtGui.QApplication.UnicodeUTF8))
        self.comboDescription.setItemText(3, QtGui.QApplication.translate("ActivityForm", "Reunião Mediúnica", None, QtGui.QApplication.UnicodeUTF8))
        self.comboDescription.setItemText(4, QtGui.QApplication.translate("ActivityForm", "Desobsessão", None, QtGui.QApplication.UnicodeUTF8))
        self.comboDescription.setItemText(5, QtGui.QApplication.translate("ActivityForm", "Voluntariado", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ActivityForm", "Sala:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ActivityForm", "Horário:", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday0.setToolTip(QtGui.QApplication.translate("ActivityForm", "Segunda-Feira", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday0.setText(QtGui.QApplication.translate("ActivityForm", "seg", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday1.setToolTip(QtGui.QApplication.translate("ActivityForm", "Terça-Feira", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday1.setText(QtGui.QApplication.translate("ActivityForm", "ter", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday2.setToolTip(QtGui.QApplication.translate("ActivityForm", "Quarta-Feira", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday2.setText(QtGui.QApplication.translate("ActivityForm", "qua", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday3.setToolTip(QtGui.QApplication.translate("ActivityForm", "Quinta-Feira", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday3.setText(QtGui.QApplication.translate("ActivityForm", "qui", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday4.setToolTip(QtGui.QApplication.translate("ActivityForm", "Sexta-Feira", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday4.setText(QtGui.QApplication.translate("ActivityForm", "sex", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday5.setToolTip(QtGui.QApplication.translate("ActivityForm", "Sábado", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday5.setText(QtGui.QApplication.translate("ActivityForm", "sab", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday6.setToolTip(QtGui.QApplication.translate("ActivityForm", "Domingo", None, QtGui.QApplication.UnicodeUTF8))
        self.rd_weekday6.setText(QtGui.QApplication.translate("ActivityForm", "dom", None, QtGui.QApplication.UnicodeUTF8))

