import csv
import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from Homework_18.titanic import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable('titanic.csv')
        self.initUI()

    def initUI(self):
        self.textEdit.textChanged.connect(self.run)

    def run(self):
        self.reload_Table('titanic.csv')

    def color(self):
        for i in range(len(self.survive)):
            if self.survive[i] == "0":
                self.color_row(i, QColor(225, 0, 0))
            if self.survive[i] == "1":
                self.color_row(i, QColor(0, 225, 0))

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=',', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            self.survive = []
            self.names = []
            for i, row in enumerate(reader):
                self.survive.append(row[5])
                self.names.append(row[1].lower())
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        self.color()
        self.tableWidget.resizeColumnsToContents()

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)

    def reload_Table(self, table_name):
        if len(self.textEdit.toPlainText()) >= 3:
            with open(table_name, encoding="utf8") as csvfile:
                reader = csv.reader(csvfile,
                                    delimiter=',', quotechar='"')
                title = next(reader)
                self.tableWidget.setColumnCount(len(title))
                self.tableWidget.setHorizontalHeaderLabels(title)
                self.tableWidget.setRowCount(0)
                self.survive = []
                t = 0
                for i, row in enumerate(reader):
                    if self.textEdit.toPlainText().lower() in row[1].lower():
                        self.survive.append(row[5])
                        self.tableWidget.setRowCount(
                            self.tableWidget.rowCount() + 1)
                        for j, elem in enumerate(row):
                            self.tableWidget.setItem(
                                t, j, QTableWidgetItem(elem))
                        t += 1
            self.color()
            self.tableWidget.resizeColumnsToContents()
        if len(self.textEdit.toPlainText()) < 3:
            self.loadTable('titanic.csv')




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
