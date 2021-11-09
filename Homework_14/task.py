import sys
from math import cos, pi, sin, atan, sqrt

from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from Homework_14.cvadrat_2 import Ui_Form


class DrawCvadrat_2(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton_1.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawLines(qp)
            qp.end()

    def drawLines(self, qp):
        num = float(self.textEdit_K.toPlainText())
        pen = QPen(Qt.black)
        angle = 0
        x_1, y_1 = 150, 150
        l = 250
        qp.setPen(pen)
        for i in range(int(self.textEdit_N.toPlainText())):
            new_angle = angle
            for j in range(4):
                new_x = x_1 + l * cos(new_angle * pi / 180)
                new_y = y_1 + l * sin(new_angle * pi / 180)
                qp.drawLine(x_1, y_1, new_x, new_y)
                new_angle += 90
                x_1, y_1 = new_x, new_y
            x_1 += l * (1 - num) * cos(angle * pi / 180)
            y_1 += l * (1 - num) * sin(angle * pi / 180)
            angle += (atan((l * (1 - num)) / (l * num))) / (pi / 180)
            l = sqrt((l * (1 - num)) ** 2 + (l * num) ** 2)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawCvadrat_2()
    ex.show()
    sys.exit(app.exec())
