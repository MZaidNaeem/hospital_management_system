# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginUQWPpR.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

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
        self.cnic_lable = QLabel(self.widget)
        self.cnic_lable.setObjectName(u"cnic_lable")

        self.verticalLayout_5.addWidget(self.cnic_lable)

        self.cnic_input = QLineEdit(self.widget)
        self.cnic_input.setObjectName(u"cnic_input")

        self.verticalLayout_5.addWidget(self.cnic_input)

        self.passoword_lable = QLabel(self.widget)
        self.passoword_lable.setObjectName(u"passoword_lable")

        self.verticalLayout_5.addWidget(self.passoword_lable)

        self.password_input = QLineEdit(self.widget)
        self.password_input.setObjectName(u"password_input")

        self.verticalLayout_5.addWidget(self.password_input)

        self.login_as_lable = QLabel(self.widget)
        self.login_as_lable.setObjectName(u"login_as_lable")

        self.verticalLayout_5.addWidget(self.login_as_lable)

        self.login_as_input = QComboBox(self.widget)
        self.login_as_input.addItem("")
        self.login_as_input.addItem("")
        self.login_as_input.addItem("")
        self.login_as_input.setObjectName(u"login_as_input")

        self.verticalLayout_5.addWidget(self.login_as_input)

        self.error_label = QLabel(self.widget)
        self.error_label.setObjectName(u"error_label")

        self.verticalLayout_5.addWidget(self.error_label)

        self.login_button = QPushButton(self.widget)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout_5.addWidget(self.login_button)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)


        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)

        self.title_label = QLabel(Frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(400, 50))
        font = QFont()
        font.setPointSize(22)
        self.title_label.setFont(font)

        self.gridLayout.addWidget(self.title_label, 1, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.cnic_lable.setText(QCoreApplication.translate("Frame", u"CNIC", None))
        self.passoword_lable.setText(QCoreApplication.translate("Frame", u"PASSWORD", None))
        self.login_as_lable.setText(QCoreApplication.translate("Frame", u"LOGIN AS", None))
        self.login_as_input.setItemText(0, QCoreApplication.translate("Frame", u"ADMIN", None))
        self.login_as_input.setItemText(1, QCoreApplication.translate("Frame", u"DOCTOR", None))
        self.login_as_input.setItemText(2, QCoreApplication.translate("Frame", u"PATIENT", None))

        self.error_label.setText("")
        self.login_button.setText(QCoreApplication.translate("Frame", u"LOGIN", None))
        self.title_label.setText(QCoreApplication.translate("Frame", u"Hospital Management System", None))
    # retranslateUi

