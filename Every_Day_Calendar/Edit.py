# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormTaskEdit(object):
    def setupUi(self, FormTaskEdit):
        FormTaskEdit.setObjectName("FormTaskEdit")
        FormTaskEdit.resize(541, 144)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(FormTaskEdit)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(FormTaskEdit)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1_edit = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_1_edit.setFont(font)
        self.label_1_edit.setObjectName("label_1_edit")
        self.verticalLayout.addWidget(self.label_1_edit)
        self.label_2_edit = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2_edit.setFont(font)
        self.label_2_edit.setObjectName("label_2_edit")
        self.verticalLayout.addWidget(self.label_2_edit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_task_edit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_task_edit.setObjectName("lineEdit_task_edit")
        self.verticalLayout_2.addWidget(self.lineEdit_task_edit)
        self.dateTimeEdit_edit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_edit.setObjectName("dateTimeEdit_edit")
        self.verticalLayout_2.addWidget(self.dateTimeEdit_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_1_edit = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_1_edit.setFont(font)
        self.pushButton_1_edit.setObjectName("pushButton_1_edit")
        self.horizontalLayout_2.addWidget(self.pushButton_1_edit)
        self.pushButton_2_edit = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2_edit.setFont(font)
        self.pushButton_2_edit.setObjectName("pushButton_2_edit")
        self.horizontalLayout_2.addWidget(self.pushButton_2_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addWidget(self.groupBox)

        self.retranslateUi(FormTaskEdit)
        QtCore.QMetaObject.connectSlotsByName(FormTaskEdit)

    def retranslateUi(self, FormTaskEdit):
        _translate = QtCore.QCoreApplication.translate
        FormTaskEdit.setWindowTitle(_translate("FormTaskEdit", "Изменить задачу"))
        self.groupBox.setTitle(_translate("FormTaskEdit", "Изменить задачу"))
        self.label_1_edit.setText(_translate("FormTaskEdit", "ВВедите описание задачи"))
        self.label_2_edit.setText(_translate("FormTaskEdit", "ВВедите время"))
        self.pushButton_1_edit.setText(_translate("FormTaskEdit", "Отменить"))
        self.pushButton_2_edit.setText(_translate("FormTaskEdit", "Ок"))