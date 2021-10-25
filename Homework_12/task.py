import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from Homework_12.work_with_file import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton_open.clicked.connect(self.open)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_create.clicked.connect(self.creat)

    def open(self):
        try:
            open(self.textEdit_file.toPlainText())
        except IOError:
            self.textEdit_text.setText(f'Файл {self.textEdit_file.toPlainText()} не найден')
        else:
            with open(self.textEdit_file.toPlainText(), "r", encoding='utf-8') as f:
                lst = [line.strip() for line in f]
                self.textEdit_text.setPlainText("\n".join(lst))

    def save(self):
        with open(self.textEdit_file.toPlainText(), "w", encoding='utf-8') as f:
            f.write(self.textEdit_text.toPlainText())

    def creat(self):
        self.textEdit_text.setPlainText("")
        # когда человек будет нажимать в последующем на кнопку сохранить файл он создастся


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