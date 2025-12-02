# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_main_interfaceDaLRWQ.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1430, 707)
        self.gridLayout_4 = QGridLayout(Frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(Frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 30))
        self.widget.setMaximumSize(QSize(1100, 650))
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setSpacing(9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.admin_label = QLabel(self.widget)
        self.admin_label.setObjectName(u"admin_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.admin_label.sizePolicy().hasHeightForWidth())
        self.admin_label.setSizePolicy(sizePolicy)
        self.admin_label.setMinimumSize(QSize(0, 30))
        self.admin_label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(23)
        self.admin_label.setFont(font)
        self.admin_label.setStyleSheet(u"")
        self.admin_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.admin_label, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(50)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.admin_mange_admins = QPushButton(self.widget)
        self.admin_mange_admins.setObjectName(u"admin_mange_admins")
        self.admin_mange_admins.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.admin_mange_admins, 0, 1, 1, 1)

        self.admin_my_profile = QPushButton(self.widget)
        self.admin_my_profile.setObjectName(u"admin_my_profile")
        self.admin_my_profile.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.admin_my_profile, 0, 0, 1, 1)

        self.admin_manage_rooms = QPushButton(self.widget)
        self.admin_manage_rooms.setObjectName(u"admin_manage_rooms")
        self.admin_manage_rooms.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.admin_manage_rooms, 1, 0, 1, 1)

        self.admin_manage_patients = QPushButton(self.widget)
        self.admin_manage_patients.setObjectName(u"admin_manage_patients")
        self.admin_manage_patients.setEnabled(True)
        self.admin_manage_patients.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.admin_manage_patients, 0, 3, 1, 1)

        self.admin_manage_doctors = QPushButton(self.widget)
        self.admin_manage_doctors.setObjectName(u"admin_manage_doctors")
        self.admin_manage_doctors.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.admin_manage_doctors, 0, 2, 1, 1)

        self.admin_manage_assignments = QPushButton(self.widget)
        self.admin_manage_assignments.setObjectName(u"admin_manage_assignments")
        self.admin_manage_assignments.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.admin_manage_assignments, 1, 3, 1, 1)

        self.admin_manage_appointments = QPushButton(self.widget)
        self.admin_manage_appointments.setObjectName(u"admin_manage_appointments")
        self.admin_manage_appointments.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.admin_manage_appointments, 1, 2, 1, 1)

        self.admin_manage_branches = QPushButton(self.widget)
        self.admin_manage_branches.setObjectName(u"admin_manage_branches")
        self.admin_manage_branches.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.admin_manage_branches, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Frame)

        self.admin_manage_patients.setDefault(False)


        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.admin_label.setText(QCoreApplication.translate("Frame", u"ADMIN PORTAL", None))
        self.admin_mange_admins.setText(QCoreApplication.translate("Frame", u"Manage Admins", None))
        self.admin_my_profile.setText(QCoreApplication.translate("Frame", u"My Profile", None))
        self.admin_manage_rooms.setText(QCoreApplication.translate("Frame", u"Manage Rooms", None))
        self.admin_manage_patients.setText(QCoreApplication.translate("Frame", u"Manage Patients", None))
        self.admin_manage_doctors.setText(QCoreApplication.translate("Frame", u"Mange Doctors", None))
        self.admin_manage_assignments.setText(QCoreApplication.translate("Frame", u"Assignments", None))
        self.admin_manage_appointments.setText(QCoreApplication.translate("Frame", u"Appointments", None))
        self.admin_manage_branches.setText(QCoreApplication.translate("Frame", u"Manage Branches", None))
    # retranslateUi

