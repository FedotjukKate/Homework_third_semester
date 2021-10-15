import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from Homework2.ui_Qcheckbox import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.checkBox_1.stateChanged.connect(self.cpryatat)
        self.checkBox_2.stateChanged.connect(self.cpryatat)
        self.checkBox_3.stateChanged.connect(self.cpryatat)
        self.checkBox_4.stateChanged.connect(self.cpryatat)

    def cpryatat(self):
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