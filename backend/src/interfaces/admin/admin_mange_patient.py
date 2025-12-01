# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_patient_manageCHYixL.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableView, QTextEdit,
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
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(400, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.title_patient = QLabel(self.widget_6)
        self.title_patient.setObjectName(u"title_patient")
        font = QFont()
        font.setPointSize(23)
        self.title_patient.setFont(font)
        self.title_patient.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.title_patient)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.patient_first_name_label = QLabel(self.widget_2)
        self.patient_first_name_label.setObjectName(u"patient_first_name_label")

        self.verticalLayout_2.addWidget(self.patient_first_name_label)

        self.patient_first_name_input = QLineEdit(self.widget_2)
        self.patient_first_name_input.setObjectName(u"patient_first_name_input")

        self.verticalLayout_2.addWidget(self.patient_first_name_input)

        self.patient_last_name_label = QLabel(self.widget_2)
        self.patient_last_name_label.setObjectName(u"patient_last_name_label")

        self.verticalLayout_2.addWidget(self.patient_last_name_label)

        self.patient_last_name_input = QTextEdit(self.widget_2)
        self.patient_last_name_input.setObjectName(u"patient_last_name_input")
        self.patient_last_name_input.setMaximumSize(QSize(16777215, 22))

        self.verticalLayout_2.addWidget(self.patient_last_name_input)

        self.patient_email_label = QLabel(self.widget_2)
        self.patient_email_label.setObjectName(u"patient_email_label")

        self.verticalLayout_2.addWidget(self.patient_email_label)

        self.patient_email_input = QTextEdit(self.widget_2)
        self.patient_email_input.setObjectName(u"patient_email_input")
        self.patient_email_input.setMaximumSize(QSize(16777215, 22))

        self.verticalLayout_2.addWidget(self.patient_email_input)

        self.patient_cnic_label = QLabel(self.widget_2)
        self.patient_cnic_label.setObjectName(u"patient_cnic_label")

        self.verticalLayout_2.addWidget(self.patient_cnic_label)

        self.patient_cnic_input = QLineEdit(self.widget_2)
        self.patient_cnic_input.setObjectName(u"patient_cnic_input")

        self.verticalLayout_2.addWidget(self.patient_cnic_input)

        self.patient_password_label = QLabel(self.widget_2)
        self.patient_password_label.setObjectName(u"patient_password_label")

        self.verticalLayout_2.addWidget(self.patient_password_label)

        self.patient_password_input = QLineEdit(self.widget_2)
        self.patient_password_input.setObjectName(u"patient_password_input")

        self.verticalLayout_2.addWidget(self.patient_password_input)

        self.patient_gender_label = QLabel(self.widget_2)
        self.patient_gender_label.setObjectName(u"patient_gender_label")

        self.verticalLayout_2.addWidget(self.patient_gender_label)

        self.patient_gender_dropbox = QComboBox(self.widget_2)
        self.patient_gender_dropbox.setObjectName(u"patient_gender_dropbox")

        self.verticalLayout_2.addWidget(self.patient_gender_dropbox)

        self.patient_contact_label = QLabel(self.widget_2)
        self.patient_contact_label.setObjectName(u"patient_contact_label")

        self.verticalLayout_2.addWidget(self.patient_contact_label)

        self.patient_contact_input = QTextEdit(self.widget_2)
        self.patient_contact_input.setObjectName(u"patient_contact_input")
        self.patient_contact_input.setMaximumSize(QSize(16777215, 22))

        self.verticalLayout_2.addWidget(self.patient_contact_input)

        self.patient_message_label = QLabel(self.widget_2)
        self.patient_message_label.setObjectName(u"patient_message_label")

        self.verticalLayout_2.addWidget(self.patient_message_label)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.patient_add_button = QPushButton(self.widget_4)
        self.patient_add_button.setObjectName(u"patient_add_button")

        self.horizontalLayout_5.addWidget(self.patient_add_button)

        self.patient_update_button = QPushButton(self.widget_4)
        self.patient_update_button.setObjectName(u"patient_update_button")

        self.horizontalLayout_5.addWidget(self.patient_update_button)

        self.patient_delete_button = QPushButton(self.widget_4)
        self.patient_delete_button.setObjectName(u"patient_delete_button")

        self.horizontalLayout_5.addWidget(self.patient_delete_button)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableView = QTableView(self.widget_3)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(0, 0))
        self.tableView.setMaximumSize(QSize(1000, 600))

        self.gridLayout_2.addWidget(self.tableView, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.patient_appointments_label = QLabel(self.widget_5)
        self.patient_appointments_label.setObjectName(u"patient_appointments_label")
        self.patient_appointments_label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.patient_appointments_label)

        self.patient_appointment_dropbox = QComboBox(self.widget_5)
        self.patient_appointment_dropbox.addItem("")
        self.patient_appointment_dropbox.addItem("")
        self.patient_appointment_dropbox.setObjectName(u"patient_appointment_dropbox")
        self.patient_appointment_dropbox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_2.addWidget(self.patient_appointment_dropbox)

        self.patient_appointments_input = QTextEdit(self.widget_5)
        self.patient_appointments_input.setObjectName(u"patient_appointments_input")
        self.patient_appointments_input.setMinimumSize(QSize(150, 0))
        self.patient_appointments_input.setMaximumSize(QSize(1000, 22))

        self.horizontalLayout_2.addWidget(self.patient_appointments_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addWidget(self.widget_5, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.title_patient.setText(QCoreApplication.translate("Frame", u"MANAGE PATIENTS", None))
        self.patient_first_name_label.setText(QCoreApplication.translate("Frame", u"FIRST NAME", None))
        self.patient_last_name_label.setText(QCoreApplication.translate("Frame", u"SECOND NAME", None))
        self.patient_email_label.setText(QCoreApplication.translate("Frame", u"EMAIL", None))
        self.patient_cnic_label.setText(QCoreApplication.translate("Frame", u"CNIC", None))
        self.patient_password_label.setText(QCoreApplication.translate("Frame", u"PASSWORD", None))
        self.patient_gender_label.setText(QCoreApplication.translate("Frame", u"GENDER", None))
        self.patient_contact_label.setText(QCoreApplication.translate("Frame", u"CONTACT NUMBER", None))
        self.patient_message_label.setText("")
        self.patient_add_button.setText(QCoreApplication.translate("Frame", u"ADD", None))
        self.patient_update_button.setText(QCoreApplication.translate("Frame", u"UPDATE", None))
        self.patient_delete_button.setText(QCoreApplication.translate("Frame", u"DELETE", None))
        self.patient_appointments_label.setText(QCoreApplication.translate("Frame", u"APPOINTMENTS", None))
        self.patient_appointment_dropbox.setItemText(0, QCoreApplication.translate("Frame", u"GREATER THAN", None))
        self.patient_appointment_dropbox.setItemText(1, QCoreApplication.translate("Frame", u"LESS THAN", None))

    # retranslateUi

