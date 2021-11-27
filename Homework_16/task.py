import csv
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from Homework_16.olimp import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable('rez.csv')
        self.initUI()

    def initUI(self):
        self.comboBox_school.addItems(self.school.keys())
        self.comboBox_class.addItems(set(sum(self.school.values(), [])))
        self.pushButton.clicked.connect(self.run)
        self.comboBox_school.currentTextChanged.connect(self.ok)

    def ok(self):
        if self.comboBox_school.currentText() != "Все":
            self.comboBox_class.clear()
            elem = ("Все " + " ".join(self.school[self.comboBox_school.currentText()])).split(" ")
            self.comboBox_class.addItems(elem)
        else:
            self.comboBox_class.clear()
            elem = ("Все " + " ".join(set(sum(self.school.values(), [])))).split(" ")
            self.comboBox_class.addItems(elem)

    def run(self):
        self.reload_Table('rez.csv', self.comboBox_school.currentText(), self.comboBox_class.currentText())

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=',', quotechar='"')
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(["Фамилия", "Результат"])
            self.tableWidget.setRowCount(0)
            self.school = {}
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                if i == 0:
                    row = next(reader)
                if row[2].split("-")[2] not in self.school:
                    self.school[(row[2].split("-")[2])] = []
                if row[2].split("-")[3] not in self.school[(row[2].split("-")[2])]:
                    self.school[(row[2].split("-")[2])].append(row[2].split("-")[3])
                j = 0
                elem = row[1].split(" ")[3]
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(elem))
                j = 1
                elem = row[7]
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()

    def reload_Table(self, table_name, school, clas):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=',', quotechar='"')
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(["Фамилия", "Результат"])
            self.tableWidget.setRowCount(0)
            t = 0
            if school == "Все":
                school = self.school
            if clas == "Все":
                clas = set(sum(self.school.values(), []))
            for i, row in enumerate(reader):
                if i == 0:
                    row = next(reader)
                if row[2].split("-")[2] in school:
                    if row[2].split("-")[3] in clas:
                        self.tableWidget.setRowCount(
                            self.tableWidget.rowCount() + 1)
                        j = 0
                        elem = row[1].split(" ")[3]
                        self.tableWidget.setItem(
                            t, j, QTableWidgetItem(elem))
                        j = 1
                        elem = row[7]
                        self.tableWidget.setItem(
                            t, j, QTableWidgetItem(elem))
                        t += 1
        self.tableWidget.resizeColumnsToContents()




sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

