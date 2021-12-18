# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'site_page_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 795)
        MainWindow.setMinimumSize(QtCore.QSize(1130, 795))
        MainWindow.setMaximumSize(QtCore.QSize(1130, 795))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"     border-image:  url(C:/PyQt/ProjectPIY/pythonProject/site_page/4.jpg);\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"     font: 10pt \"Segoe Script\";\n"
"     color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton\n"
"{    \n"
"     font: 10pt \"Segoe Script\";\n"
"     background-color: rgb(255, 255, 255);\n"
"     border-style: outset;\n"
"     border-width: 3px;\n"
"     border-color: rgb(235, 235, 235);\n"
"     color: black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(255, 235, 253);\n"
"    border-width: 2px;\n"
"    border-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(245, 218, 235);\n"
"    border-width: 2px;\n"
"    border-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QComboBox\n"
"{    \n"
"     font: 10pt \"Segoe Script\";\n"
"     background-color: rgb(255, 255, 255);\n"
"     border-style: outset;\n"
"     border-width: 3px;\n"
"     border-color: rgb(235, 235, 235);\n"
"     color: black;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"\n"
"{\n"
"      outline: none;\n"
"      border-color: rgb(235, 235, 235);\n"
"      selection-background-color: rgb(255, 235, 253);\n"
"      selection-color: rgb(155, 135, 153);\n"
"      font: 10pt \"Segoe Script\";\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover\n"
"{\n"
"    selection-background-color:rgb(255, 235, 253);\n"
"    border-width: 2px;\n"
"    color: black;\n"
"    border-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:pressed\n"
"{\n"
"    selection-background-color: rgb(245, 218, 235);\n"
"    border-width: 2px;\n"
"    color: black;\n"
"    border-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 191, 164))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel\n"
"\n"
"{\n"
"    background-color: rgb(241, 189, 255);\n"
"     border-style: outset;\n"
"     border-width: 2px;\n"
"    border-color: rgb(217, 187, 225);\n"
"    color: black;\n"
"}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.available_uni_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.available_uni_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.available_uni_pushButton.setFont(font)
        self.available_uni_pushButton.setStyleSheet("")
        self.available_uni_pushButton.setObjectName("available_uni_pushButton")
        self.verticalLayout_2.addWidget(self.available_uni_pushButton)
        self.specialty_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.specialty_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.specialty_pushButton.setFont(font)
        self.specialty_pushButton.setStyleSheet("")
        self.specialty_pushButton.setObjectName("specialty_pushButton")
        self.verticalLayout_2.addWidget(self.specialty_pushButton)
        self.request_history_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.request_history_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.request_history_pushButton.setFont(font)
        self.request_history_pushButton.setStyleSheet("")
        self.request_history_pushButton.setObjectName("request_history_pushButton")
        self.verticalLayout_2.addWidget(self.request_history_pushButton)
        self.exit_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exit_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.exit_pushButton.setFont(font)
        self.exit_pushButton.setStyleSheet("")
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.verticalLayout_2.addWidget(self.exit_pushButton)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 30, 841, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    font: 14pt \"Segoe Script\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.town_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.town_comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.town_comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.town_comboBox.setStyleSheet("")
        self.town_comboBox.setObjectName("town_comboBox")
        self.town_comboBox.addItem("")
        self.town_comboBox.addItem("")
        self.town_comboBox.addItem("")
        self.town_comboBox.addItem("")
        self.town_comboBox.addItem("")
        self.town_comboBox.addItem("")
        self.town_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.town_comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.subject_comboBox_1 = QtWidgets.QComboBox(self.layoutWidget)
        self.subject_comboBox_1.setMinimumSize(QtCore.QSize(120, 0))
        self.subject_comboBox_1.setObjectName("subject_comboBox_1")
        self.subject_comboBox_1.addItem("")
        self.subject_comboBox_1.addItem("")
        self.subject_comboBox_1.addItem("")
        self.subject_comboBox_1.addItem("")
        self.subject_comboBox_1.addItem("")
        self.subject_comboBox_1.addItem("")
        self.subject_comboBox_1.addItem("")
        self.subject_comboBox_1.addItem("")
        self.subject_comboBox_1.addItem("")
        self.subject_comboBox_1.addItem("")
        self.horizontalLayout_2.addWidget(self.subject_comboBox_1)
        self.subject_comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.subject_comboBox_2.setMinimumSize(QtCore.QSize(120, 0))
        self.subject_comboBox_2.setObjectName("subject_comboBox_2")
        self.subject_comboBox_2.addItem("")
        self.subject_comboBox_2.addItem("")
        self.subject_comboBox_2.addItem("")
        self.subject_comboBox_2.addItem("")
        self.subject_comboBox_2.addItem("")
        self.subject_comboBox_2.addItem("")
        self.subject_comboBox_2.addItem("")
        self.subject_comboBox_2.addItem("")
        self.subject_comboBox_2.addItem("")
        self.subject_comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.subject_comboBox_2)
        self.subject_comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.subject_comboBox_3.setMinimumSize(QtCore.QSize(120, 0))
        self.subject_comboBox_3.setObjectName("subject_comboBox_3")
        self.subject_comboBox_3.addItem("")
        self.subject_comboBox_3.addItem("")
        self.subject_comboBox_3.addItem("")
        self.subject_comboBox_3.addItem("")
        self.subject_comboBox_3.addItem("")
        self.subject_comboBox_3.addItem("")
        self.subject_comboBox_3.addItem("")
        self.subject_comboBox_3.addItem("")
        self.subject_comboBox_3.addItem("")
        self.subject_comboBox_3.addItem("")
        self.horizontalLayout_2.addWidget(self.subject_comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.sum_textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.sum_textEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sum_textEdit.sizePolicy().hasHeightForWidth())
        self.sum_textEdit.setSizePolicy(sizePolicy)
        self.sum_textEdit.setMinimumSize(QtCore.QSize(100, 30))
        self.sum_textEdit.setMaximumSize(QtCore.QSize(100, 30))
        self.sum_textEdit.setObjectName("sum_textEdit")
        self.horizontalLayout_3.addWidget(self.sum_textEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.search_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.search_pushButton.setMinimumSize(QtCore.QSize(171, 41))
        self.search_pushButton.setMaximumSize(QtCore.QSize(171, 41))
        self.search_pushButton.setObjectName("search_pushButton")
        self.horizontalLayout_4.addWidget(self.search_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Поступи или умри"))
        self.label_8.setText(_translate("MainWindow", "Имя пользователя"))
        self.available_uni_pushButton.setText(_translate("MainWindow", "Доступные ВУЗы"))
        self.specialty_pushButton.setText(_translate("MainWindow", "Специальности"))
        self.request_history_pushButton.setText(_translate("MainWindow", "История запросов"))
        self.exit_pushButton.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "Мы поможем Вам  в выборе ВУЗа вашей мечты!"))
        self.label_2.setText(_translate("MainWindow", "Для более точных расчётов выберете поля из выпадающего списка:"))
        self.label_3.setText(_translate("MainWindow", "Город:"))
        self.town_comboBox.setItemText(0, _translate("MainWindow", "Любой"))
        self.town_comboBox.setItemText(1, _translate("MainWindow", "Екатеринбург"))
        self.town_comboBox.setItemText(2, _translate("MainWindow", "Казань"))
        self.town_comboBox.setItemText(3, _translate("MainWindow", "Москва"))
        self.town_comboBox.setItemText(4, _translate("MainWindow", "Новосибирск"))
        self.town_comboBox.setItemText(5, _translate("MainWindow", "Санкт - Петербург"))
        self.town_comboBox.setItemText(6, _translate("MainWindow", "Томск"))
        self.label_4.setText(_translate("MainWindow", "Предметы*:"))
        self.subject_comboBox_1.setItemText(0, _translate("MainWindow", "Любой"))
        self.subject_comboBox_1.setItemText(1, _translate("MainWindow", "математика"))
        self.subject_comboBox_1.setItemText(2, _translate("MainWindow", "физика"))
        self.subject_comboBox_1.setItemText(3, _translate("MainWindow", "информатика и ИКТ"))
        self.subject_comboBox_1.setItemText(4, _translate("MainWindow", "история"))
        self.subject_comboBox_1.setItemText(5, _translate("MainWindow", "биология"))
        self.subject_comboBox_1.setItemText(6, _translate("MainWindow", "обществознание"))
        self.subject_comboBox_1.setItemText(7, _translate("MainWindow", "иностранный язык"))
        self.subject_comboBox_1.setItemText(8, _translate("MainWindow", "химия"))
        self.subject_comboBox_1.setItemText(9, _translate("MainWindow", "география"))
        self.subject_comboBox_2.setItemText(0, _translate("MainWindow", "Любой"))
        self.subject_comboBox_2.setItemText(1, _translate("MainWindow", "математика"))
        self.subject_comboBox_2.setItemText(2, _translate("MainWindow", "физика"))
        self.subject_comboBox_2.setItemText(3, _translate("MainWindow", "информатика и ИКТ"))
        self.subject_comboBox_2.setItemText(4, _translate("MainWindow", "история"))
        self.subject_comboBox_2.setItemText(5, _translate("MainWindow", "биология"))
        self.subject_comboBox_2.setItemText(6, _translate("MainWindow", "обществознание"))
        self.subject_comboBox_2.setItemText(7, _translate("MainWindow", "иностранный язык"))
        self.subject_comboBox_2.setItemText(8, _translate("MainWindow", "химия"))
        self.subject_comboBox_2.setItemText(9, _translate("MainWindow", "география"))
        self.subject_comboBox_3.setItemText(0, _translate("MainWindow", "Любой"))
        self.subject_comboBox_3.setItemText(1, _translate("MainWindow", "математика"))
        self.subject_comboBox_3.setItemText(2, _translate("MainWindow", "физика"))
        self.subject_comboBox_3.setItemText(3, _translate("MainWindow", "информатика и ИКТ"))
        self.subject_comboBox_3.setItemText(4, _translate("MainWindow", "история"))
        self.subject_comboBox_3.setItemText(5, _translate("MainWindow", "биология"))
        self.subject_comboBox_3.setItemText(6, _translate("MainWindow", "обществознание"))
        self.subject_comboBox_3.setItemText(7, _translate("MainWindow", "иностранный язык"))
        self.subject_comboBox_3.setItemText(8, _translate("MainWindow", "химия"))
        self.subject_comboBox_3.setItemText(9, _translate("MainWindow", "география"))
        self.label_5.setText(_translate("MainWindow", "*Русский язык учитывается как обязательный предмет"))
        self.label_6.setText(_translate("MainWindow", "Сумма баллов**:"))
        self.label_7.setText(_translate("MainWindow", "** Предполагаемые или уже полученные"))
        self.search_pushButton.setText(_translate("MainWindow", "Поиск"))