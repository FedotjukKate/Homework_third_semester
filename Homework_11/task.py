import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from Homework_11.chet_nechet_stroki import Ui_MainWindow


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
            lst1 = lst[0::2]
            for i in lst[1::2]:
                lst1.append(i)
            self.textEdit.setPlainText("\n".join(lst1))


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