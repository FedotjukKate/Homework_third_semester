import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from Homework6.ui_Mac import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.zakaz)
        self.TextBrowser.setDisabled(True)

    def zakaz(self):
        result = ["Ваш заказ: \n"]
        lst = list(filter(lambda x: x.startswith("checkBox"), dir(self)))
        for check in lst:
            check_1 = self.__getattribute__(check)
            if check_1.isChecked():
                result.append(check_1.text())
        self.TextBrowser.setText("\n".join(result))


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