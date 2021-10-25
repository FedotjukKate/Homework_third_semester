import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from Homework_10.File import Ui_MainWindow

# data.txt целые числа (сработает)
# data_2.txt целые числа (сработает)
# data_3.txt есть числа float (не сработает)
# data_words.txt стих (не сработает)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.numbers)
        self.plainTextEdit_max.setPlainText("0")
        self.plainTextEdit_min.setPlainText("0")
        self.plainTextEdit_middle.setPlainText("0,00")
        with open("output.txt", "w") as t:
            t.write("")

    def numbers(self):
        try:
            open(self.plainTextEdit_File.toPlainText())
        except IOError:
            self.label_file.setText(f'файл {self.plainTextEdit_File.toPlainText()} не найден')
        else:
            with open(self.plainTextEdit_File.toPlainText(), "r", encoding='utf-8') as f:
                lst = [line.strip() for line in f]
                lst1 = []
                P = True
                for i in lst:
                    for number in i.split(" "):
                        try:
                            int(number)
                        except ValueError:
                            self.label_file.setText(f'В файле {self.plainTextEdit_File.toPlainText()} '
                                                    f'содержаться некорректные данные')
                            P = False
                        else:
                            lst1.append(int(number))
                if P:
                    a, b, c = str(max(lst1)), str(min(lst1)), str(round(sum(lst1) / len(lst1), 2))
                    self.plainTextEdit_max.setPlainText(a)
                    self.plainTextEdit_min.setPlainText(b)
                    self.plainTextEdit_middle.setPlainText(c)
                    self.label_file.setText(f'Значения для файла {self.plainTextEdit_File.toPlainText()}')
                    with open("output.txt", "a") as t:
                        t.write(f"{a} {b} {c} \n")


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
