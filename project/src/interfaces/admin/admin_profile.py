# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_profilelQYVpr.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

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
        self.admin_first_name_label = QLabel(self.widget)
        self.admin_first_name_label.setObjectName(u"admin_first_name_label")

        self.verticalLayout.addWidget(self.admin_first_name_label)

        self.admin_first_name_input = QLineEdit(self.widget)
        self.admin_first_name_input.setObjectName(u"admin_first_name_input")

        self.verticalLayout.addWidget(self.admin_first_name_input)

        self.admin_last_name_label = QLabel(self.widget)
        self.admin_last_name_label.setObjectName(u"admin_last_name_label")

        self.verticalLayout.addWidget(self.admin_last_name_label)

        self.admin_last_name_input = QLineEdit(self.widget)
        self.admin_last_name_input.setObjectName(u"admin_last_name_input")

        self.verticalLayout.addWidget(self.admin_last_name_input)

        self.admin_email_label = QLabel(self.widget)
        self.admin_email_label.setObjectName(u"admin_email_label")

        self.verticalLayout.addWidget(self.admin_email_label)

        self.admin_email_input = QLineEdit(self.widget)
        self.admin_email_input.setObjectName(u"admin_email_input")

        self.verticalLayout.addWidget(self.admin_email_input)

        self.admin_cnic_label = QLabel(self.widget)
        self.admin_cnic_label.setObjectName(u"admin_cnic_label")

        self.verticalLayout.addWidget(self.admin_cnic_label)

        self.admin_cnic_input = QLineEdit(self.widget)
        self.admin_cnic_input.setObjectName(u"admin_cnic_input")

        self.verticalLayout.addWidget(self.admin_cnic_input)

        self.admin_password_label = QLabel(self.widget)
        self.admin_password_label.setObjectName(u"admin_password_label")

        self.verticalLayout.addWidget(self.admin_password_label)

        self.admin_password_input = QLineEdit(self.widget)
        self.admin_password_input.setObjectName(u"admin_password_input")

        self.verticalLayout.addWidget(self.admin_password_input)


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
        Frame.setWindowTitle(QCoreApplication.translate("Login", u"Admin Profile - Hospital Management System", None))

        self.admin_update_button.setText(QCoreApplication.translate("Frame", u"UPDATE", None))
        self.admin_message_label.setText("")
        self.admin_first_name_label.setText(QCoreApplication.translate("Frame", u"FIRST NAME", None))
        self.admin_last_name_label.setText(QCoreApplication.translate("Frame", u"LAST NAME", None))
        self.admin_email_label.setText(QCoreApplication.translate("Frame", u"EMAIL", None))
        self.admin_cnic_label.setText(QCoreApplication.translate("Frame", u"CNIC", None))
        self.admin_password_label.setText(QCoreApplication.translate("Frame", u"PASSWORD", None))
        self.admin_profile_title.setText(QCoreApplication.translate("Frame", u"ADMIN PROFILE", None))
        self.admin_delete_button.setText(QCoreApplication.translate("Frame", u"DELETE", None))
    # retranslateUi

