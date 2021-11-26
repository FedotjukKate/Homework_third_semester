import sys
from math import cos, pi, sin, asin, sqrt

from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QColorDialog
from Homework_15.cvadrat_3 import Ui_Form


class DrawCvadrat_2(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.color = QColorDialog.getColor()
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
        pen = QPen(self.color)
        num = float(self.textEdit_K.toPlainText())
        n = int(self.textEdit_N.toPlainText())
        angle = 0
        x_1, y_1 = 300, 150
        b = (n - 2) * 180 / n
        l = 200 * 0.95 ** n  # чтобы стороны не были слишком длинные у фигур с большим количеством сторон
        qp.setPen(pen)
        for i in range(int(self.textEdit_M.toPlainText())):
            new_angle = angle
            for j in range(n):
                new_x = x_1 + l * cos(new_angle * pi / 180)
                new_y = y_1 + l * sin(new_angle * pi / 180)
                qp.drawLine(x_1, y_1, new_x, new_y)
                new_angle += 180 - b
                x_1, y_1 = new_x, new_y
            x_1 += l * (1 - num) * cos(angle * pi / 180)
            y_1 += l * (1 - num) * sin(angle * pi / 180)
            l = sqrt((l * num) ** 2 + (l * (1 - num)) ** 2 - 2 * (l * num) * (l * (1 - num)) * cos(b * pi / 180))
            angle += (asin(((l * (1 - num)) * sin(b * pi / 180)) / l)) / (pi / 180)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawCvadrat_2()
    ex.show()
    sys.exit(app.exec())