# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_manage_appointmentKmoKtH.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
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
        self.title_label = QLabel(self.widget_6)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(21)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.title_label)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.appointment_branch = QComboBox(self.widget_2)
        self.appointment_branch.setObjectName(u"appointment_branch")

        self.verticalLayout_2.addWidget(self.appointment_branch)

        self.ap_patient_cnic_label = QLabel(self.widget_2)
        self.ap_patient_cnic_label.setObjectName(u"ap_patient_cnic_label")

        self.verticalLayout_2.addWidget(self.ap_patient_cnic_label)

        self.ap_patient_cnic_input = QLineEdit(self.widget_2)
        self.ap_patient_cnic_input.setObjectName(u"ap_patient_cnic_input")

        self.verticalLayout_2.addWidget(self.ap_patient_cnic_input)

        self.ap_doctor_cnic_label = QLabel(self.widget_2)
        self.ap_doctor_cnic_label.setObjectName(u"ap_doctor_cnic_label")

        self.verticalLayout_2.addWidget(self.ap_doctor_cnic_label)

        self.ap_doctor_cnic_input = QLineEdit(self.widget_2)
        self.ap_doctor_cnic_input.setObjectName(u"ap_doctor_cnic_input")

        self.verticalLayout_2.addWidget(self.ap_doctor_cnic_input)

        self.as_room_id_label = QLabel(self.widget_2)
        self.as_room_id_label.setObjectName(u"as_room_id_label")

        self.verticalLayout_2.addWidget(self.as_room_id_label)

        self.ap_room_id_input = QLineEdit(self.widget_2)
        self.ap_room_id_input.setObjectName(u"ap_room_id_input")

        self.verticalLayout_2.addWidget(self.ap_room_id_input)

        self.as_assignment_start_label = QLabel(self.widget_2)
        self.as_assignment_start_label.setObjectName(u"as_assignment_start_label")

        self.verticalLayout_2.addWidget(self.as_assignment_start_label)

        self.ap_assignment_start_input = QDateTimeEdit(self.widget_2)
        self.ap_assignment_start_input.setObjectName(u"ap_assignment_start_input")

        self.verticalLayout_2.addWidget(self.ap_assignment_start_input)

        self.as_assignment_end_label = QLabel(self.widget_2)
        self.as_assignment_end_label.setObjectName(u"as_assignment_end_label")

        self.verticalLayout_2.addWidget(self.as_assignment_end_label)

        self.ap_assignment_end_input = QDateTimeEdit(self.widget_2)
        self.ap_assignment_end_input.setObjectName(u"ap_assignment_end_input")

        self.verticalLayout_2.addWidget(self.ap_assignment_end_input)

        self.ap_status_label = QLabel(self.widget_2)
        self.ap_status_label.setObjectName(u"ap_status_label")

        self.verticalLayout_2.addWidget(self.ap_status_label)

        self.ap_status_dropbox = QComboBox(self.widget_2)
        self.ap_status_dropbox.addItem("")
        self.ap_status_dropbox.addItem("")
        self.ap_status_dropbox.addItem("")
        self.ap_status_dropbox.setObjectName(u"ap_status_dropbox")

        self.verticalLayout_2.addWidget(self.ap_status_dropbox)

        self.admin_message_label = QLabel(self.widget_2)
        self.admin_message_label.setObjectName(u"admin_message_label")
        self.admin_message_label.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_2.addWidget(self.admin_message_label)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.admin_add_button = QPushButton(self.widget_4)
        self.admin_add_button.setObjectName(u"admin_add_button")

        self.horizontalLayout_5.addWidget(self.admin_add_button)

        self.admin_update_button = QPushButton(self.widget_4)
        self.admin_update_button.setObjectName(u"admin_update_button")

        self.horizontalLayout_5.addWidget(self.admin_update_button)

        self.admin_delete_button = QPushButton(self.widget_4)
        self.admin_delete_button.setObjectName(u"admin_delete_button")

        self.horizontalLayout_5.addWidget(self.admin_delete_button)


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
        self.tableView.setMaximumSize(QSize(1300, 1300))

        self.gridLayout_2.addWidget(self.tableView, 2, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout = QVBoxLayout(self.widget_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ap_search_doctor_cnic_label = QLabel(self.widget_5)
        self.ap_search_doctor_cnic_label.setObjectName(u"ap_search_doctor_cnic_label")
        self.ap_search_doctor_cnic_label.setMinimumSize(QSize(100, 0))
        self.ap_search_doctor_cnic_label.setMaximumSize(QSize(1000, 16777215))

        self.horizontalLayout_2.addWidget(self.ap_search_doctor_cnic_label)

        self.ap_search_doctor_cnic_input = QLineEdit(self.widget_5)
        self.ap_search_doctor_cnic_input.setObjectName(u"ap_search_doctor_cnic_input")

        self.horizontalLayout_2.addWidget(self.ap_search_doctor_cnic_input)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.ap_search_patient_cnic_label = QLabel(self.widget_5)
        self.ap_search_patient_cnic_label.setObjectName(u"ap_search_patient_cnic_label")
        self.ap_search_patient_cnic_label.setMinimumSize(QSize(100, 0))
        self.ap_search_patient_cnic_label.setMaximumSize(QSize(1000, 16777215))

        self.horizontalLayout_10.addWidget(self.ap_search_patient_cnic_label)

        self.ap_search_patient_cnic_input = QLineEdit(self.widget_5)
        self.ap_search_patient_cnic_input.setObjectName(u"ap_search_patient_cnic_input")

        self.horizontalLayout_10.addWidget(self.ap_search_patient_cnic_input)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.as_search_room_id_label = QLabel(self.widget_5)
        self.as_search_room_id_label.setObjectName(u"as_search_room_id_label")
        self.as_search_room_id_label.setMinimumSize(QSize(100, 0))
        self.as_search_room_id_label.setMaximumSize(QSize(1000, 16777215))

        self.horizontalLayout_4.addWidget(self.as_search_room_id_label)

        self.ap_search_room_id_input = QLineEdit(self.widget_5)
        self.ap_search_room_id_input.setObjectName(u"ap_search_room_id_input")

        self.horizontalLayout_4.addWidget(self.ap_search_room_id_input)

        self.search_status_dropbox = QComboBox(self.widget_5)
        self.search_status_dropbox.addItem("")
        self.search_status_dropbox.addItem("")
        self.search_status_dropbox.addItem("")
        self.search_status_dropbox.setObjectName(u"search_status_dropbox")

        self.horizontalLayout_4.addWidget(self.search_status_dropbox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addWidget(self.widget_5, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Login", u"Manage Appointments - Hospital Management System", None))
        self.title_label.setText(QCoreApplication.translate("Frame", u"MANAGE APPOINTMENTS", None))
        self.label.setText(QCoreApplication.translate("Frame", u"BRANCH", None))
        self.ap_patient_cnic_label.setText(QCoreApplication.translate("Frame", u"PATIENT CNIC", None))
        self.ap_doctor_cnic_label.setText(QCoreApplication.translate("Frame", u"DOCTOR CNIC", None))
        self.as_room_id_label.setText(QCoreApplication.translate("Frame", u"ROOM ID", None))
        self.as_assignment_start_label.setText(QCoreApplication.translate("Frame", u"ASSIGNMENT START", None))
        self.as_assignment_end_label.setText(QCoreApplication.translate("Frame", u"ASSIGNMENT END", None))
        self.ap_status_label.setText(QCoreApplication.translate("Frame", u"APPOINTMENT STATUS", None))
        self.ap_status_dropbox.setItemText(0, QCoreApplication.translate("Frame", u"Scheduled", None))
        self.ap_status_dropbox.setItemText(1, QCoreApplication.translate("Frame", u"Completed", None))
        self.ap_status_dropbox.setItemText(2, QCoreApplication.translate("Frame", u"Cancelled", None))

        self.admin_message_label.setText("")
        self.admin_add_button.setText(QCoreApplication.translate("Frame", u"ADD ", None))
        self.admin_update_button.setText(QCoreApplication.translate("Frame", u"UPDATE", None))
        self.admin_delete_button.setText(QCoreApplication.translate("Frame", u"DELETE", None))
        self.ap_search_doctor_cnic_label.setText(QCoreApplication.translate("Frame", u"DOCTOR CNIC", None))
        self.ap_search_patient_cnic_label.setText(QCoreApplication.translate("Frame", u"PATIENT CNIC", None))
        self.as_search_room_id_label.setText(QCoreApplication.translate("Frame", u"ROOM ID", None))
        self.search_status_dropbox.setItemText(0, QCoreApplication.translate("Frame", u"Scheduled", None))
        self.search_status_dropbox.setItemText(1, QCoreApplication.translate("Frame", u"Completed", None))
        self.search_status_dropbox.setItemText(2, QCoreApplication.translate("Frame", u"Cancelled", None))

    # retranslateUi

