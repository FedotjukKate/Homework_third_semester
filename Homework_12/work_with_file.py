# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'work_with_file.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 545)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(30, 80, 211, 41))
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(30, 140, 211, 41))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setGeometry(QtCore.QRect(30, 200, 211, 41))
        self.pushButton_open.setObjectName("pushButton_open")
        self.textEdit_text = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_text.setGeometry(QtCore.QRect(260, 20, 361, 431))
        self.textEdit_text.setObjectName("textEdit_file")
        self.textEdit_file = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_file.setGeometry(QtCore.QRect(30, 20, 211, 41))
        self.textEdit_file.setObjectName("textEdit_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 34))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_create.setText(_translate("MainWindow", "Создать новый"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить файл"))
        self.pushButton_open.setText(_translate("MainWindow", "Открыть файл"))
