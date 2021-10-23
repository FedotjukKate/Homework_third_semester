import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from Homework7.ui_Mac2 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.zakaz)
        self.TextBrowser.setDisabled(True)
        self.textEdit_1.setDisabled(True)
        self.textEdit_2.setDisabled(True)
        self.textEdit_3.setDisabled(True)
        self.textEdit_4.setDisabled(True)
        self.checkBox.stateChanged.connect(self.colichectvo)
        self.checkBox_2.stateChanged.connect(self.colichectvo)
        self.checkBox_3.stateChanged.connect(self.colichectvo)
        self.checkBox_4.stateChanged.connect(self.colichectvo)
        self.textEdit_1.price = 250
        self.textEdit_2.price = 200
        self.textEdit_3.price = 50
        self.textEdit_4.price = 100

    def colichectvo(self):
        lst = list(filter(lambda x: x.startswith("checkBox"), dir(self)))
        lst2 = list(filter(lambda x: x.startswith("textEdit"), dir(self)))
        for check in lst:
            if self.sender().objectName() == check:
                coll = self.__getattribute__(lst2[lst.index(check)])
                if self.__getattribute__(check).isChecked():
                    coll.setDisabled(False)
                else:
                    coll.setDisabled(True)
                    coll.setText("")

    def zakaz(self):
        result = ["Ваш заказ: \n"]
        lst = list(filter(lambda x: x.startswith("checkBox"), dir(self)))
        lst2 = list(filter(lambda x: x.startswith("textEdit"), dir(self)))
        for check in lst:
            check_1 = self.__getattribute__(check)
            if check_1.isChecked():
                coll = self.__getattribute__(lst2[lst.index(check)])
                if coll.toPlainText() == "":
                    coll.setText("1")
                pric = coll.price * int(coll.toPlainText())
                result.append(f'{check_1.text()}-----{coll.toPlainText()}-----{pric}')
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