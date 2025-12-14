# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doctor_profilerLZFjW.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1100, 600)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(500, 500))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.admin_update_button = QPushButton(self.widget)
        self.admin_update_button.setObjectName(u"admin_update_button")

        self.gridLayout_2.addWidget(self.admin_update_button, 3, 0, 1, 1)

        self.admin_message_label = QLabel(self.widget)
        self.admin_message_label.setObjectName(u"admin_message_label")
        self.admin_message_label.setMaximumSize(QSize(16777214, 20))

        self.gridLayout_2.addWidget(self.admin_message_label, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.first_name_label = QLabel(self.widget)
        self.first_name_label.setObjectName(u"first_name_label")

        self.verticalLayout.addWidget(self.first_name_label)

        self.first_name_input = QLineEdit(self.widget)
        self.first_name_input.setObjectName(u"first_name_input")

        self.verticalLayout.addWidget(self.first_name_input)

        self.last_name_label = QLabel(self.widget)
        self.last_name_label.setObjectName(u"last_name_label")

        self.verticalLayout.addWidget(self.last_name_label)

        self.last_name_input = QLineEdit(self.widget)
        self.last_name_input.setObjectName(u"last_name_input")

        self.verticalLayout.addWidget(self.last_name_input)

        self.email_label = QLabel(self.widget)
        self.email_label.setObjectName(u"email_label")

        self.verticalLayout.addWidget(self.email_label)

        self.email_input = QLineEdit(self.widget)
        self.email_input.setObjectName(u"email_input")

        self.verticalLayout.addWidget(self.email_input)

        self.cnic_label = QLabel(self.widget)
        self.cnic_label.setObjectName(u"cnic_label")

        self.verticalLayout.addWidget(self.cnic_label)

        self.cnic_input = QLineEdit(self.widget)
        self.cnic_input.setObjectName(u"cnic_input")

        self.verticalLayout.addWidget(self.cnic_input)

        self.password_label = QLabel(self.widget)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout.addWidget(self.password_label)

        self.password_input = QLineEdit(self.widget)
        self.password_input.setObjectName(u"password_input")

        self.verticalLayout.addWidget(self.password_input)

        self.speciality_label = QLabel(self.widget)
        self.speciality_label.setObjectName(u"speciality_label")

        self.verticalLayout.addWidget(self.speciality_label)

        self.speciality_input = QTextEdit(self.widget)
        self.speciality_input.setObjectName(u"speciality_input")

        self.verticalLayout.addWidget(self.speciality_input)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.contact_number_input = QTextEdit(self.widget)
        self.contact_number_input.setObjectName(u"contact_number_input")

        self.verticalLayout.addWidget(self.contact_number_input)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.admin_profile_title = QLabel(self.widget)
        self.admin_profile_title.setObjectName(u"admin_profile_title")
        self.admin_profile_title.setMaximumSize(QSize(500, 50))
        font = QFont()
        font.setPointSize(23)
        self.admin_profile_title.setFont(font)
        self.admin_profile_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.admin_profile_title, 0, 0, 1, 1)

        self.admin_delete_button = QPushButton(self.widget)
        self.admin_delete_button.setObjectName(u"admin_delete_button")
        self.admin_delete_button.setStyleSheet(u"background-color : \"red\"\n"
"")

        self.gridLayout_2.addWidget(self.admin_delete_button, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Login", u"Doctor Profile - Hospital Management System", None))

        self.admin_update_button.setText(QCoreApplication.translate("Frame", u"UPDATE", None))
        self.admin_message_label.setText("")
        self.first_name_label.setText(QCoreApplication.translate("Frame", u"FIRST NAME", None))
        self.last_name_label.setText(QCoreApplication.translate("Frame", u"LAST NAME", None))
        self.email_label.setText(QCoreApplication.translate("Frame", u"EMAIL", None))
        self.cnic_label.setText(QCoreApplication.translate("Frame", u"CNIC", None))
        self.password_label.setText(QCoreApplication.translate("Frame", u"PASSWORD", None))
        self.speciality_label.setText(QCoreApplication.translate("Frame", u"Speciality", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"Contact Number", None))
        self.admin_profile_title.setText(QCoreApplication.translate("Frame", u"DOCTOR PROFILE", None))
        self.admin_delete_button.setText(QCoreApplication.translate("Frame", u"DELETE", None))
    # retranslateUi

