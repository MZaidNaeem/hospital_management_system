# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_room_manageNPldbf.ui'
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
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(800, 500)
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

        self.admin_room_no_label = QLabel(self.widget_2)
        self.admin_room_no_label.setObjectName(u"admin_room_no_label")
        self.admin_room_no_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.admin_room_no_label)

        self.admin_room_input = QLineEdit(self.widget_2)
        self.admin_room_input.setObjectName(u"admin_room_input")

        self.verticalLayout_2.addWidget(self.admin_room_input)

        self.admin_branch_label = QLabel(self.widget_2)
        self.admin_branch_label.setObjectName(u"admin_branch_label")
        self.admin_branch_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.admin_branch_label)

        self.admin_branch_dropbox = QComboBox(self.widget_2)
        self.admin_branch_dropbox.setObjectName(u"admin_branch_dropbox")

        self.verticalLayout_2.addWidget(self.admin_branch_dropbox)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.label)

        self.room_delete_dropbox = QComboBox(self.widget_2)
        self.room_delete_dropbox.addItem("")
        self.room_delete_dropbox.addItem("")
        self.room_delete_dropbox.setObjectName(u"room_delete_dropbox")

        self.verticalLayout_2.addWidget(self.room_delete_dropbox)

        self.admin_message_label = QLabel(self.widget_2)
        self.admin_message_label.setObjectName(u"admin_message_label")
        self.admin_message_label.setMaximumSize(QSize(16777215, 20))

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

        self.gridLayout_2.addWidget(self.tableView, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.room_branch_search_dropbox = QComboBox(self.widget_5)
        self.room_branch_search_dropbox.addItem("")
        self.room_branch_search_dropbox.setObjectName(u"room_branch_search_dropbox")

        self.horizontalLayout_2.addWidget(self.room_branch_search_dropbox)

        self.room_search_button = QPushButton(self.widget_5)
        self.room_search_button.setObjectName(u"room_search_button")

        self.horizontalLayout_2.addWidget(self.room_search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addWidget(self.widget_5, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Login", u"Manage Rooms - Hospital Management System", None))
        self.title_label.setText(QCoreApplication.translate("Frame", u"MANAGE ROOMS", None))
        self.admin_room_no_label.setText(QCoreApplication.translate("Frame", u"ROOM NO", None))
        self.admin_branch_label.setText(QCoreApplication.translate("Frame", u"BRANCH", None))
        self.label.setText(QCoreApplication.translate("Frame", u"DELETED", None))
        self.room_delete_dropbox.setItemText(0, QCoreApplication.translate("Frame", u"YES", None))
        self.room_delete_dropbox.setItemText(1, QCoreApplication.translate("Frame", u"NO", None))

        self.admin_message_label.setText("")
        self.admin_add_button.setText(QCoreApplication.translate("Frame", u"ADD ROOM", None))
        self.admin_update_button.setText(QCoreApplication.translate("Frame", u"UPDATE ROOM", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"SEARCH BY BRANCH", None))
        self.room_branch_search_dropbox.setItemText(0, QCoreApplication.translate("Frame", u"ALL", None))

        self.room_search_button.setText(QCoreApplication.translate("Frame", u"SEARCH", None))
    # retranslateUi

