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
        self.textEdit_3.setDisabled(True)

    def plus(self):
        if self.textEdit.toPlainText() == "":
            self.textEdit.setText("0")
        if self.textEdit_2.toPlainText() == "":
            self.textEdit_2.setText("0")
        a = float(self.textEdit.toPlainText())
        b = float(self.textEdit_2.toPlainText())
        self.textEdit_3.setText(str(a + b))

    def minus(self):
        if self.textEdit.toPlainText() == "":
            self.textEdit.setText("0")
        if self.textEdit_2.toPlainText() == "":
            self.textEdit_2.setText("0")
        a = float(self.textEdit.toPlainText())
        b = float(self.textEdit_2.toPlainText())
        self.textEdit_3.setText(str(a - b))

    def ymnogit(self):
        if self.textEdit.toPlainText() == "":
            self.textEdit.setText("0")
        if self.textEdit_2.toPlainText() == "":
            self.textEdit_2.setText("0")
        a = float(self.textEdit.toPlainText())
        b = float(self.textEdit_2.toPlainText())
        self.textEdit_3.setText(str(a * b))


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