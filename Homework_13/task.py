import sys

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from Homework_13.cvadrat_1 import Ui_Form


class DrawCvadrat(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_fractal(qp)
            qp.end()

    def draw_fractal(self, qp):
        n = int(self.textEdit_side.toPlainText())
        x = 100
        y = 200
        qp.setPen(Qt.red)
        for i in range(int(self.textEdit_n.toPlainText())):
            qp.drawRect(x, y, n, n)
            n_new = n * float(self.textEdit_coeff.toPlainText())
            x = x + (n - n_new) / 2
            y = y + (n - n_new) / 2
            n = n_new


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawCvadrat()
    ex.show()
    sys.exit(app.exec())