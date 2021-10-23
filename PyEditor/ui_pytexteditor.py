# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pytexteditorKmABJC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 595)
        MainWindow.setStyleSheet(u"background-color:rgb(71, 71, 71);")
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName(u"actionRun")
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionLicenses = QAction(MainWindow)
        self.actionLicenses.setObjectName(u"actionLicenses")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionIncrease_Font_Size = QAction(MainWindow)
        self.actionIncrease_Font_Size.setObjectName(u"actionIncrease_Font_Size")
        self.actionDecrease_Font_Size = QAction(MainWindow)
        self.actionDecrease_Font_Size.setObjectName(u"actionDecrease_Font_Size")
        self.actionh = QAction(MainWindow)
        self.actionh.setObjectName(u"actionh")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.status = QStatusBar(MainWindow)
        self.status.setObjectName(u"status")
        MainWindow.setStatusBar(self.status)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 804, 21))
        self.menubar.setStyleSheet(u"color:rgb(255,255,255); ")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setStyleSheet(u"hover:rgb(53, 53, 53);onclick:rgb(35, 35, 35);")
        self.menuOpen_Recent = QMenu(self.menuFile)
        self.menuOpen_Recent.setObjectName(u"menuOpen_Recent")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuEdit.setStyleSheet(u"hover:rgb(53, 53, 53);onclick:rgb(35, 35, 35);")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuSettings.setStyleSheet(u"hover:rgb(53, 53, 53);onclick:rgb(35, 35, 35);")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuAbout.setStyleSheet(u"hover:rgb(53, 53, 53);onclick:rgb(35, 35, 35);")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.menuOpen_Recent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRun)
        self.menuOpen_Recent.addAction(self.actionh)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuSettings.addAction(self.actionSettings)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionIncrease_Font_Size)
        self.menuSettings.addAction(self.actionDecrease_Font_Size)
        self.menuAbout.addAction(self.actionLicenses)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionLicenses.setText(QCoreApplication.translate("MainWindow", u"License", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Prefercenes", None))
        self.actionIncrease_Font_Size.setText(QCoreApplication.translate("MainWindow", u"Increase Font Size", None))
        self.actionDecrease_Font_Size.setText(QCoreApplication.translate("MainWindow", u"Decrease Font Size", None))
        self.actionh.setText(QCoreApplication.translate("MainWindow", u"h", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOpen_Recent.setTitle(QCoreApplication.translate("MainWindow", u"Open Recent", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

