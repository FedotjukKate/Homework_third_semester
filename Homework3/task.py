import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from Homework3.cacylator import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.plus)
        self.pushButton_2.clicked.connect(self.minus)
        self.pushButton_3.clicked.connect(self.ymnogit)

    def plus(self):
        pass

    def minus(self):
        pass

    def ymnogit(self):
        pass


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