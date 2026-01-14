# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QSize, Qt, QMetaObject)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1430, 690)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")

        self.widget = QWidget(Frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(400, 300))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        # CNIC
        self.cnic_lable = QLabel(self.widget)
        self.cnic_lable.setObjectName(u"cnic_lable")
        self.verticalLayout_5.addWidget(self.cnic_lable)

        self.cnic_input = QLineEdit(self.widget)
        self.cnic_input.setObjectName(u"cnic_input")
        self.verticalLayout_5.addWidget(self.cnic_input)

        # Password
        self.passoword_lable = QLabel(self.widget)
        self.passoword_lable.setObjectName(u"passoword_lable")
        self.verticalLayout_5.addWidget(self.passoword_lable)

        # Password field with eye button
        self.password_layout = QHBoxLayout()
        self.password_input = QLineEdit(self.widget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setEchoMode(QLineEdit.Password) 
        self.password_layout.addWidget(self.password_input)

        self.eye_button = QPushButton("👁️", self.widget)  
        self.eye_button.setCheckable(True)
        self.eye_button.setMaximumSize(QSize(30, 30))
        self.eye_button.setStyleSheet("border: none; font-size:16px;")
        self.eye_button.clicked.connect(self.toggle_password_visibility)

        self.password_layout.addWidget(self.eye_button)

        self.verticalLayout_5.addLayout(self.password_layout)

        # Login As
        self.login_as_lable = QLabel(self.widget)
        self.login_as_lable.setObjectName(u"login_as_lable")
        self.verticalLayout_5.addWidget(self.login_as_lable)

        self.login_as_input = QComboBox(self.widget)
        self.login_as_input.addItem("")
        self.login_as_input.addItem("")
        self.login_as_input.setObjectName(u"login_as_input")
        self.login_as_input.setMaximumSize(QSize(16777215, 23))
        self.verticalLayout_5.addWidget(self.login_as_input)

        # Error Label
        self.error_label = QLabel(self.widget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setMaximumSize(QSize(16777215, 23))
        self.verticalLayout_5.addWidget(self.error_label)

        # Login Button
        self.login_button = QPushButton(self.widget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5.addWidget(self.login_button)

        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)

        # Title
        self.title_label = QLabel(Frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(400, 50))
        font = QFont()
        font.setPointSize(22)
        self.title_label.setFont(font)
        self.gridLayout.addWidget(self.title_label, 1, 0, 1, 1)

        self.retranslateUi(Frame)
        QMetaObject.connectSlotsByName(Frame)

    def toggle_password_visibility(self):
        if self.eye_button.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)  
        else:
            self.password_input.setEchoMode(QLineEdit.Password)  

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Login", u"Login - Hospital Management System", None))
        self.cnic_lable.setText(QCoreApplication.translate("Frame", u"CNIC", None))
        self.passoword_lable.setText(QCoreApplication.translate("Frame", u"PASSWORD", None))
        self.login_as_lable.setText(QCoreApplication.translate("Frame", u"LOGIN AS", None))
        self.login_as_input.setItemText(0, QCoreApplication.translate("Frame", u"ADMIN", None))
        self.login_as_input.setItemText(1, QCoreApplication.translate("Frame", u"DOCTOR", None))
        self.error_label.setText("")
        self.login_button.setText(QCoreApplication.translate("Frame", u"LOGIN", None))
        self.title_label.setText(QCoreApplication.translate("Frame", u"Hospital Management System", None))
