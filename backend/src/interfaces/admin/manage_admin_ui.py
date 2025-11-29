# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_mangeHXLXIs.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

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
        font.setPointSize(23)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.title_label)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.admin_first_name_label = QLabel(self.widget_2)
        self.admin_first_name_label.setObjectName(u"admin_first_name_label")

        self.verticalLayout_2.addWidget(self.admin_first_name_label)

        self.admin_first_name_input = QLineEdit(self.widget_2)
        self.admin_first_name_input.setObjectName(u"admin_first_name_input")

        self.verticalLayout_2.addWidget(self.admin_first_name_input)

        self.admin_last_name_label = QLabel(self.widget_2)
        self.admin_last_name_label.setObjectName(u"admin_last_name_label")

        self.verticalLayout_2.addWidget(self.admin_last_name_label)

        self.admin_last_name_input = QLineEdit(self.widget_2)
        self.admin_last_name_input.setObjectName(u"admin_last_name_input")

        self.verticalLayout_2.addWidget(self.admin_last_name_input)

        self.admin_email_label = QLabel(self.widget_2)
        self.admin_email_label.setObjectName(u"admin_email_label")

        self.verticalLayout_2.addWidget(self.admin_email_label)

        self.admin_email_input = QLineEdit(self.widget_2)
        self.admin_email_input.setObjectName(u"admin_email_input")

        self.verticalLayout_2.addWidget(self.admin_email_input)

        self.admin_cnic_label = QLabel(self.widget_2)
        self.admin_cnic_label.setObjectName(u"admin_cnic_label")

        self.verticalLayout_2.addWidget(self.admin_cnic_label)

        self.admin_cnic_input = QLineEdit(self.widget_2)
        self.admin_cnic_input.setObjectName(u"admin_cnic_input")

        self.verticalLayout_2.addWidget(self.admin_cnic_input)

        self.admin_password_label = QLabel(self.widget_2)
        self.admin_password_label.setObjectName(u"admin_password_label")

        self.verticalLayout_2.addWidget(self.admin_password_label)

        self.admin_password_input = QLineEdit(self.widget_2)
        self.admin_password_input.setObjectName(u"admin_password_input")

        self.verticalLayout_2.addWidget(self.admin_password_input)

        self.admin_message_label = QLabel(self.widget_2)
        self.admin_message_label.setObjectName(u"admin_message_label")

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

        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.title_label.setText(QCoreApplication.translate("Frame", u"Manage Admins", None))
        self.admin_first_name_label.setText(QCoreApplication.translate("Frame", u"FIRST NAME", None))
        self.admin_last_name_label.setText(QCoreApplication.translate("Frame", u"LAST NAME", None))
        self.admin_email_label.setText(QCoreApplication.translate("Frame", u"EMAIL", None))
        self.admin_cnic_label.setText(QCoreApplication.translate("Frame", u"CNIC", None))
        self.admin_password_label.setText(QCoreApplication.translate("Frame", u"PASSWORD", None))
        self.admin_message_label.setText("")
        self.admin_add_button.setText(QCoreApplication.translate("Frame", u"ADD ADMIN", None))
        self.admin_update_button.setText(QCoreApplication.translate("Frame", u"UPDATE ADMIN", None))
        self.admin_delete_button.setText(QCoreApplication.translate("Frame", u"DELETE ADMIN", None))
    # retranslateUi

