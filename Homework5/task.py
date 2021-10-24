import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from Homework5.X_O import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        x = 250
        y = 10
        a, b = 61, 61
        self.lst = []
        self.number = 0
        for i in range(1, 10):
            if (i - 1) % 3 == 0:
                x = 250
                y += 70
            self.pushButton = QPushButton(self)
            self.pushButton.setGeometry(x, y, a, b)
            self.pushButton.setObjectName(f"pushButton_{i}")
            x += 70
            self.lst.append(self.pushButton)
        for button in self.lst:
            button.clicked.connect(self.ok)
        self.pushButton_new.clicked.connect(self.new)
        self.radioButton_X.toggled.connect(self.new)
        self.radioButton_O.toggled.connect(self.new)

    def ok(self):
        lst2 = []
        if self.sender().text() == "":
            if self.radioButton_X.isChecked():
                if self.number % 2 == 0:
                    self.sender().setText("X")
                    self.number += 1
                else:
                    self.sender().setText("O")
                    self.number += 1

            if self.radioButton_O.isChecked():
                if self.number % 2 == 0:
                    self.sender().setText("O")
                    self.number += 1
                else:
                    self.sender().setText("X")
                    self.number += 1
        for button in self.lst:
            lst2.append(str(button.text()))
        for j in range(0, 3):
            if "".join(lst2[j::3]) == "XXX" or "".join(lst2[j * 3: 3 * (j + 1)]) == "XXX":
                self.win("X")
            elif "".join(lst2[0::4]) == "XXX" or "".join(lst2[2:8:2]) == "XXX":
                self.win("X")
            elif "".join(lst2[j::3]) == "OOO" or "".join(lst2[j * 3: 3 * (j + 1)]) == "OOO":
                self.win("O")
            elif "".join(lst2[0::4]) == "OOO" or "".join(lst2[2:8:2]) == "OOO":
                self.win("O")

    def new(self):
        self.number = 0
        self.label.setText("")
        for button in self.lst:
            button.setText("")
            button.setDisabled(False)

    def win(self, st):
        self.label.setText(f"Выиграл {st}!!!")
        for button in self.lst:
            button.setDisabled(True)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())