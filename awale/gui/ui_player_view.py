# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player_view.ui'
#
# Created: Tue Nov 18 18:47:35 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(235, 278)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.player_cmd = QtWidgets.QLineEdit(self.groupBox)
        self.player_cmd.setObjectName("player_cmd")
        self.horizontalLayout.addWidget(self.player_cmd)
        self.browse_btn = QtWidgets.QPushButton(self.groupBox)
        self.browse_btn.setObjectName("browse_btn")
        self.horizontalLayout.addWidget(self.browse_btn)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.victories = QtWidgets.QLabel(self.groupBox)
        self.victories.setObjectName("victories")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.victories)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.defeats = QtWidgets.QLabel(self.groupBox)
        self.defeats.setObjectName("defeats")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.defeats)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.draws = QtWidgets.QLabel(self.groupBox)
        self.draws.setObjectName("draws")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.draws)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.win_percent = QtWidgets.QLabel(self.groupBox)
        self.win_percent.setObjectName("win_percent")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.win_percent)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.moves_played = QtWidgets.QLabel(self.groupBox)
        self.moves_played.setObjectName("moves_played")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.moves_played)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.valid_moves_mean = QtWidgets.QLabel(self.groupBox)
        self.valid_moves_mean.setObjectName("valid_moves_mean")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.valid_moves_mean)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.time_per_turn = QtWidgets.QLabel(self.groupBox)
        self.time_per_turn.setObjectName("time_per_turn")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.time_per_turn)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "PlayerName"))
        self.browse_btn.setText(_translate("Form", "Browse"))
        self.label_4.setText(_translate("Form", "Victories :"))
        self.victories.setText(_translate("Form", "0"))
        self.label_6.setText(_translate("Form", "Defeats :"))
        self.defeats.setText(_translate("Form", "0"))
        self.label_11.setText(_translate("Form", "Draws :"))
        self.draws.setText(_translate("Form", "0"))
        self.label_9.setText(_translate("Form", "Vicotry % :"))
        self.win_percent.setText(_translate("Form", "0%"))
        self.label_10.setText(_translate("Form", "Moves per game :"))
        self.moves_played.setText(_translate("Form", "0"))
        self.label_12.setText(_translate("Form", "Valid moves per turn :"))
        self.valid_moves_mean.setText(_translate("Form", "0"))
        self.label_13.setText(_translate("Form", "Time per turn (in s):"))
        self.time_per_turn.setText(_translate("Form", "0"))

