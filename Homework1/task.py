import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from Homework1.window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.fokys)

    def fokys(self):
        if "->" == self.pushButton.text():
            self.pushButton.setText("<-")
            self.textEdit_2.setText(self.textEdit_1.toPlainText())
            self.textEdit_1.setText("")
        else:
            self.pushButton.setText("->")
            self.textEdit_1.setText(self.textEdit_2.toPlainText())
            self.textEdit_2.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())