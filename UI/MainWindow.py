# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import Share_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setMinimumSize(QSize(800, 450))
        MainWindow.setMaximumSize(QSize(800, 450))
        icon = QIcon()
        icon.addFile(u":/Logo/Share/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_about.setCheckable(False)
        self.action_about.setAutoRepeat(True)
        self.action_about.setVisible(True)
        self.action_about.setIconVisibleInMenu(True)
        self.action_play_selected = QAction(MainWindow)
        self.action_play_selected.setObjectName(u"action_play_selected")
        self.action_play_all = QAction(MainWindow)
        self.action_play_all.setObjectName(u"action_play_all")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 780, 385))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(760, 200))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setTearOffEnabled(False)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menuMenu.addAction(self.action_about)
        self.menu.addAction(self.action_play_selected)
        self.menu.addAction(self.action_play_all)

        self.retranslateUi(MainWindow)
        self.action_about.triggered.connect(MainWindow.About_Window)
        self.action_play_selected.triggered.connect(MainWindow.Play_selected)
        self.action_play_all.triggered.connect(MainWindow.Play_all)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cardinal", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_play_selected.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e\u6240\u9009", None))
        self.action_play_all.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e\u6240\u6709", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u5c5e\u6027", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u64ad\u653e", None))
    # retranslateUi

