# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_doctor_manageiIZGpZ.ui'
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
        Frame.resize(1100, 649)
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
        self.title_doctors = QLabel(self.widget_6)
        self.title_doctors.setObjectName(u"title_doctors")
        font = QFont()
        font.setPointSize(23)
        self.title_doctors.setFont(font)
        self.title_doctors.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.title_doctors)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.doctor_first_name_label = QLabel(self.widget_2)
        self.doctor_first_name_label.setObjectName(u"doctor_first_name_label")

        self.verticalLayout_2.addWidget(self.doctor_first_name_label)

        self.doctor_first_name_input = QLineEdit(self.widget_2)
        self.doctor_first_name_input.setObjectName(u"doctor_first_name_input")

        self.verticalLayout_2.addWidget(self.doctor_first_name_input)

        self.doctor_last_name_label = QLabel(self.widget_2)
        self.doctor_last_name_label.setObjectName(u"doctor_last_name_label")

        self.verticalLayout_2.addWidget(self.doctor_last_name_label)

        self.doctor_last_name_input = QTextEdit(self.widget_2)
        self.doctor_last_name_input.setObjectName(u"doctor_last_name_input")
        self.doctor_last_name_input.setMaximumSize(QSize(16777215, 22))

        self.verticalLayout_2.addWidget(self.doctor_last_name_input)

        self.doctor_email_label = QLabel(self.widget_2)
        self.doctor_email_label.setObjectName(u"doctor_email_label")

        self.verticalLayout_2.addWidget(self.doctor_email_label)

        self.doctor_email_input = QTextEdit(self.widget_2)
        self.doctor_email_input.setObjectName(u"doctor_email_input")
        self.doctor_email_input.setMaximumSize(QSize(16777215, 22))

        self.verticalLayout_2.addWidget(self.doctor_email_input)

        self.doctor_cnic_label = QLabel(self.widget_2)
        self.doctor_cnic_label.setObjectName(u"doctor_cnic_label")

        self.verticalLayout_2.addWidget(self.doctor_cnic_label)

        self.doctor_cnic_input = QLineEdit(self.widget_2)
        self.doctor_cnic_input.setObjectName(u"doctor_cnic_input")

        self.verticalLayout_2.addWidget(self.doctor_cnic_input)

        self.doctor_password_label = QLabel(self.widget_2)
        self.doctor_password_label.setObjectName(u"doctor_password_label")

        self.verticalLayout_2.addWidget(self.doctor_password_label)

        self.doctor_password_input = QLineEdit(self.widget_2)
        self.doctor_password_input.setObjectName(u"doctor_password_input")

        self.verticalLayout_2.addWidget(self.doctor_password_input)

        self.doctor_speciality_label = QLabel(self.widget_2)
        self.doctor_speciality_label.setObjectName(u"doctor_speciality_label")

        self.verticalLayout_2.addWidget(self.doctor_speciality_label)

        self.doctor_speciality_input = QLineEdit(self.widget_2)
        self.doctor_speciality_input.setObjectName(u"doctor_speciality_input")

        self.verticalLayout_2.addWidget(self.doctor_speciality_input)

        self.doctor_contact_label = QLabel(self.widget_2)
        self.doctor_contact_label.setObjectName(u"doctor_contact_label")

        self.verticalLayout_2.addWidget(self.doctor_contact_label)

        self.doctor_contact_input = QTextEdit(self.widget_2)
        self.doctor_contact_input.setObjectName(u"doctor_contact_input")
        self.doctor_contact_input.setMaximumSize(QSize(16777215, 22))

        self.verticalLayout_2.addWidget(self.doctor_contact_input)

        self.doctor_branch_label = QLabel(self.widget_2)
        self.doctor_branch_label.setObjectName(u"doctor_branch_label")

        self.verticalLayout_2.addWidget(self.doctor_branch_label)

        self.doctor_branch_dropbox = QComboBox(self.widget_2)
        self.doctor_branch_dropbox.setObjectName(u"doctor_branch_dropbox")

        self.verticalLayout_2.addWidget(self.doctor_branch_dropbox)

        self.doctor_delete_label = QLabel(self.widget_2)
        self.doctor_delete_label.setObjectName(u"doctor_delete_label")

        self.verticalLayout_2.addWidget(self.doctor_delete_label)

        self.doctor_delete_dropbox = QComboBox(self.widget_2)
        self.doctor_delete_dropbox.addItem("")
        self.doctor_delete_dropbox.addItem("")
        self.doctor_delete_dropbox.setObjectName(u"doctor_delete_dropbox")

        self.verticalLayout_2.addWidget(self.doctor_delete_dropbox)

        self.doctor_message_label = QLabel(self.widget_2)
        self.doctor_message_label.setObjectName(u"doctor_message_label")

        self.verticalLayout_2.addWidget(self.doctor_message_label)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.doctor_add_button = QPushButton(self.widget_4)
        self.doctor_add_button.setObjectName(u"doctor_add_button")

        self.horizontalLayout_5.addWidget(self.doctor_add_button)

        self.doctor_update_button = QPushButton(self.widget_4)
        self.doctor_update_button.setObjectName(u"doctor_update_button")

        self.horizontalLayout_5.addWidget(self.doctor_update_button)


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
        self.doctor_search_label = QLabel(self.widget_5)
        self.doctor_search_label.setObjectName(u"doctor_search_label")
        self.doctor_search_label.setMinimumSize(QSize(100, 0))
        self.doctor_search_label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.doctor_search_label)

        self.doctor_search_input = QTextEdit(self.widget_5)
        self.doctor_search_input.setObjectName(u"doctor_search_input")
        self.doctor_search_input.setMinimumSize(QSize(150, 0))
        self.doctor_search_input.setMaximumSize(QSize(300, 22))

        self.horizontalLayout_2.addWidget(self.doctor_search_input)

        self.doctor_search_button = QPushButton(self.widget_5)
        self.doctor_search_button.setObjectName(u"doctor_search_button")

        self.horizontalLayout_2.addWidget(self.doctor_search_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addWidget(self.widget_5, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.title_doctors.setText(QCoreApplication.translate("Frame", u"MANAGE DOCTORS", None))
        self.doctor_first_name_label.setText(QCoreApplication.translate("Frame", u"FIRST NAME", None))
        self.doctor_last_name_label.setText(QCoreApplication.translate("Frame", u"SECOND NAME", None))
        self.doctor_email_label.setText(QCoreApplication.translate("Frame", u"EMAIL", None))
        self.doctor_cnic_label.setText(QCoreApplication.translate("Frame", u"CNIC", None))
        self.doctor_password_label.setText(QCoreApplication.translate("Frame", u"PASSWORD", None))
        self.doctor_speciality_label.setText(QCoreApplication.translate("Frame", u"SPECIALITY", None))
        self.doctor_contact_label.setText(QCoreApplication.translate("Frame", u"CONTACT NUMBER", None))
        self.doctor_branch_label.setText(QCoreApplication.translate("Frame", u"BRANCH", None))
        self.doctor_delete_label.setText(QCoreApplication.translate("Frame", u"DELETE", None))
        self.doctor_delete_dropbox.setItemText(0, QCoreApplication.translate("Frame", u"YES", None))
        self.doctor_delete_dropbox.setItemText(1, QCoreApplication.translate("Frame", u"NO", None))

        self.doctor_message_label.setText("")
        self.doctor_add_button.setText(QCoreApplication.translate("Frame", u"ADD", None))
        self.doctor_update_button.setText(QCoreApplication.translate("Frame", u"UPDATE", None))
        self.doctor_search_label.setText(QCoreApplication.translate("Frame", u"SEARCH BY CNIC", None))
        self.doctor_search_button.setText(QCoreApplication.translate("Frame", u"SEARCH", None))
    # retranslateUi

