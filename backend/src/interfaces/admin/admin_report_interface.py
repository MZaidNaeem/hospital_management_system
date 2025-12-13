# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_report_interfacerfJoWa.ui'
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
    QSizePolicy, QTableView, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1100, 600)
        Frame.setMinimumSize(QSize(1100, 600))
        self.gridLayout_4 = QGridLayout(Frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(Frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(Frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.xlxs_button = QPushButton(Frame)
        self.xlxs_button.setObjectName(u"xlxs_button")

        self.horizontalLayout.addWidget(self.xlxs_button)


        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.label = QLabel(Frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.tableView = QTableView(Frame)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_4.addWidget(self.tableView, 4, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Frame", u"BRANCH", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Frame", u"ROOM", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Frame", u"DOCTOR", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Frame", u"PATIENT", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("Frame", u"ALL", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Frame", u"MONTHLY", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Frame", u"WEEKLY", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Frame", u"DAILY", None))

        self.xlxs_button.setText(QCoreApplication.translate("Frame", u"EXPORT TO XLSX", None))
        self.label.setText(QCoreApplication.translate("Frame", u"REPORTS", None))
    # retranslateUi

