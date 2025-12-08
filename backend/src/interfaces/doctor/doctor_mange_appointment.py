# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doctor_appointmentYDhjMw.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1000, 600)
        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(Frame)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 140))
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.message_label = QLabel(self.widget_3)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.message_label)

        self.update_button = QPushButton(self.widget_3)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setMaximumSize(QSize(16777215, 23))

        self.verticalLayout.addWidget(self.update_button)


        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget = QWidget(Frame)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 50))
        self.widget_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.search_patient_cnic = QTextEdit(self.widget_4)
        self.search_patient_cnic.setObjectName(u"search_patient_cnic")
        self.search_patient_cnic.setMaximumSize(QSize(250, 20))

        self.horizontalLayout_2.addWidget(self.search_patient_cnic)

        self.search_status = QComboBox(self.widget_4)
        self.search_status.addItem("")
        self.search_status.addItem("")
        self.search_status.addItem("")
        self.search_status.setObjectName(u"search_status")
        self.search_status.setMaximumSize(QSize(250, 20))
        self.search_status.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_2.addWidget(self.search_status)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Frame", u"MANAGE APPOINTMENTS", None))
        self.message_label.setText("")
        self.update_button.setText(QCoreApplication.translate("Frame", u"COMPLETE ASSIGNMENT", None))
        self.label_4.setText(QCoreApplication.translate("Frame", u"SEARCH BY PATIENT CNIC", None))
        self.search_status.setItemText(0, QCoreApplication.translate("Frame", u"Scheduled", None))
        self.search_status.setItemText(1, QCoreApplication.translate("Frame", u"Completed", None))
        self.search_status.setItemText(2, QCoreApplication.translate("Frame", u"Cancelled", None))

    # retranslateUi

