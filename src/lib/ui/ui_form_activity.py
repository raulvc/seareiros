# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lib/ui/form_activity.ui'
#
# Created: Wed Feb 26 19:33:46 2014
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ActivityForm(object):
    def setupUi(self, ActivityForm):
        ActivityForm.setObjectName("ActivityForm")
        ActivityForm.resize(745, 274)
        ActivityForm.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 743, 272))
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
        self.editTime = QtGui.QTimeEdit(self.groupBox)
        self.editTime.setTime(QtCore.QTime(19, 0, 0))
        self.editTime.setObjectName("editTime")
        self.gridLayout.addWidget(self.editTime, 2, 1, 1, 1)
        self.comboWeekday = QtGui.QComboBox(self.groupBox)
        self.comboWeekday.setObjectName("comboWeekday")
        self.comboWeekday.addItem("")
        self.comboWeekday.addItem("")
        self.comboWeekday.addItem("")
        self.comboWeekday.addItem("")
        self.comboWeekday.addItem("")
        self.comboWeekday.addItem("")
        self.comboWeekday.addItem("")
        self.gridLayout.addWidget(self.comboWeekday, 1, 3, 1, 2)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.comboDescription = QtGui.QComboBox(self.groupBox)
        self.comboDescription.setEditable(False)
        self.comboDescription.setObjectName("comboDescription")
        self.comboDescription.addItem("")
        self.comboDescription.addItem("")
        self.comboDescription.addItem("")
        self.comboDescription.addItem("")
        self.comboDescription.addItem("")
        self.comboDescription.addItem("")
        self.gridLayout.addWidget(self.comboDescription, 0, 1, 1, 4)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
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
        self.gridLayout.addWidget(self.comboRoom, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        ActivityForm.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(ActivityForm)
        QtCore.QMetaObject.connectSlotsByName(ActivityForm)
        ActivityForm.setTabOrder(self.comboDescription, self.comboRoom)
        ActivityForm.setTabOrder(self.comboRoom, self.comboWeekday)
        ActivityForm.setTabOrder(self.comboWeekday, self.editTime)

    def retranslateUi(self, ActivityForm):
        ActivityForm.setWindowTitle(QtGui.QApplication.translate("ActivityForm", "ScrollArea", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setToolTip(QtGui.QApplication.translate("ActivityForm", "Dados Pessoais", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ActivityForm", "Atividade", None, QtGui.QApplication.UnicodeUTF8))
        self.editTime.setDisplayFormat(QtGui.QApplication.translate("ActivityForm", "HH:mm", None, QtGui.QApplication.UnicodeUTF8))
        self.comboWeekday.setItemText(0, QtGui.QApplication.translate("ActivityForm", "Segunda-Feira", None, QtGui.QApplication.UnicodeUTF8))
        self.comboWeekday.setItemText(1, QtGui.QApplication.translate("ActivityForm", "Terça-Feira", None, QtGui.QApplication.UnicodeUTF8))
        self.comboWeekday.setItemText(2, QtGui.QApplication.translate("ActivityForm", "Quarta-Feira", None, QtGui.QApplication.UnicodeUTF8))
        self.comboWeekday.setItemText(3, QtGui.QApplication.translate("ActivityForm", "Quinta-Feira", None, QtGui.QApplication.UnicodeUTF8))
        self.comboWeekday.setItemText(4, QtGui.QApplication.translate("ActivityForm", "Sexta-Feira", None, QtGui.QApplication.UnicodeUTF8))
        self.comboWeekday.setItemText(5, QtGui.QApplication.translate("ActivityForm", "Sábado", None, QtGui.QApplication.UnicodeUTF8))
        self.comboWeekday.setItemText(6, QtGui.QApplication.translate("ActivityForm", "Domingo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ActivityForm", "Descrição:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ActivityForm", "Horário:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ActivityForm", "Sala:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboDescription.setItemText(0, QtGui.QApplication.translate("ActivityForm", "Atendimento Fraterno", None, QtGui.QApplication.UnicodeUTF8))
        self.comboDescription.setItemText(1, QtGui.QApplication.translate("ActivityForm", "Reunião Pública", None, QtGui.QApplication.UnicodeUTF8))
        self.comboDescription.setItemText(2, QtGui.QApplication.translate("ActivityForm", "Reunião de Estudos", None, QtGui.QApplication.UnicodeUTF8))
        self.comboDescription.setItemText(3, QtGui.QApplication.translate("ActivityForm", "Reunião Mediúnica", None, QtGui.QApplication.UnicodeUTF8))
        self.comboDescription.setItemText(4, QtGui.QApplication.translate("ActivityForm", "Desobsessão", None, QtGui.QApplication.UnicodeUTF8))
        self.comboDescription.setItemText(5, QtGui.QApplication.translate("ActivityForm", "Voluntariado", None, QtGui.QApplication.UnicodeUTF8))
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

