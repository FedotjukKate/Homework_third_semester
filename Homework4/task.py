import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtGui

from Homework4.ui_test4 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        x = 20  # начальная координата по х
        y = 20  # высота ряда
        a, b = 50, 50  # ширина и длина кнопок
        lst = []
        self.lst1 = []
        self.s = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..',
                  'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                  'Z': '--..'}
        for i in range(1, 27):
            if i == 15:
                y += 55
                x = 20
            self.pushButton = QPushButton(self)
            self.pushButton.setGeometry(x, y, a, b)
            self.pushButton.setText(list(self.s.keys())[i - 1])
            self.pushButton.setObjectName(f"pushButton_{i}")
            x += 55
            lst.append(self.pushButton)
        for button in lst:
            button.clicked.connect(self.ok)

    def ok(self):
        self.lst1.append(self.s[self.sender().text()])
        self.textEdit.setText("".join(self.lst1))


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
