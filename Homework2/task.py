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
        if self.sender().text().endswith("1"):
            if self.textBrowser_1.isHidden():
                self.textBrowser_1.show()
            else:
                self.textBrowser_1.hide()
        if self.sender().text().endswith("2"):
            if self.textBrowser_2.isHidden():
                self.textBrowser_2.show()
            else:
                self.textBrowser_2.hide()
        if self.sender().text().endswith("3"):
            if self.textBrowser_3.isHidden():
                self.textBrowser_3.show()
            else:
                self.textBrowser_3.hide()
        if self.sender().text().endswith("4"):
            if self.textBrowser_4.isHidden():
                self.textBrowser_4.show()
            else:
                self.textBrowser_4.hide()


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