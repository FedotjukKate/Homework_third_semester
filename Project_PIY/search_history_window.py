# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_history_window_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_history(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 850)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 850))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 850))
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
" background-color:rgb(255, 228, 250)\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"     font: 8pt \"Segoe Script\";\n"
"     color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton\n"
"{    \n"
"     font: 8pt \"Segoe Script\";\n"
"     background-color: rgb(255, 255, 255);\n"
"     border-style: outset;\n"
"     border-width: 3px;\n"
"     border-color: rgb(235, 235, 235);\n"
"     color: black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(247, 214, 239);\n"
"    border-width: 2px;\n"
"    border-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(231, 200, 225);\n"
"    border-width: 2px;\n"
"    border-color: rgb(235, 235, 235);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_search_history = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search_history.setGeometry(QtCore.QRect(800, 770, 171, 41))
        self.pushButton_search_history.setMinimumSize(QtCore.QSize(171, 41))
        self.pushButton_search_history.setMaximumSize(QtCore.QSize(171, 41))
        self.pushButton_search_history.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_search_history.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_search_history.setObjectName("pushButton_search_history")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "История поиска"))
        self.pushButton_search_history.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "История поиска"))