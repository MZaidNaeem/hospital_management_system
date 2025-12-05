# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doctor_main_interfacehHPFRv.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1000, 600)
        Frame.setMinimumSize(QSize(1000, 600))
        Frame.setMaximumSize(QSize(10000, 16777215))
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Frame)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.edit_profile_button = QPushButton(self.widget)
        self.edit_profile_button.setObjectName(u"edit_profile_button")
        self.edit_profile_button.setMaximumSize(QSize(10000, 16777215))

        self.gridLayout_2.addWidget(self.edit_profile_button, 0, 0, 1, 1)

        self.appointment_button = QPushButton(self.widget)
        self.appointment_button.setObjectName(u"appointment_button")
        self.appointment_button.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_2.addWidget(self.appointment_button, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Frame", u"DOCTOR PORTAL", None))
        self.edit_profile_button.setText(QCoreApplication.translate("Frame", u"EDIT PROFILE", None))
        self.appointment_button.setText(QCoreApplication.translate("Frame", u"APPOINTMENTS", None))
    # retranslateUi

