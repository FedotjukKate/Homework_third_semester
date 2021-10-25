import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow
from Homework9.ui_stroka import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.ok)

    def ok(self):
        with open("input.txt", "r", encoding='utf-8') as f:
            lst = [line.strip() for line in f]
            self.textEdit.setPlainText(lst[random.randint(0, len(lst) - 1)])


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