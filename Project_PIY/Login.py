import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from Project_PIY.login_window import Ui_MainWindow
from Project_PIY.Registration import RegistrationWindow
from Project_PIY.Site_window import SiteWindow


class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.registration_push_button.clicked.connect(self.registration)
        self.login_push_button.clicked.connect(self.login)

    def registration(self):
        self.wnd_create = RegistrationWindow()
        self.wnd_create.show()
        self.hide()

    def site(self, id):
        self.wnd_create = SiteWindow(id)
        self.wnd_create.show()

    def login(self):
        if self.login_text_edit.toPlainText() != "" and self.password_text_edit.toPlainText() != "":
            connection = sqlite3.connect("Registration_db.db")
            cursor = connection.cursor()
            user_password = cursor.execute(f"""SELECT password FROM User WHERE login = "{self.login_text_edit.toPlainText()}" """).fetchone()
            user_login = list(map(lambda x: str(x)[2:(len(str(x)) - 3):],
                                  cursor.execute("""SELECT login FROM User""").fetchall()))
            if self.login_text_edit.toPlainText() in user_login:
                password = str(user_password)[2: (len(user_password) - 4)]
                if self.password_text_edit.toPlainText() == password:
                    user_id = cursor.execute(f"""SELECT user_id FROM User WHERE login = "{self.login_text_edit.toPlainText()}" """).fetchone()
                    user_id = str(user_id)[1:(len(str(user_id)) - 2)]
                    self.site(user_id)
                    self.hide()
                else:
                    self.result_entrance_label.setText("Пароль набран неверно")
                    self.password_text_edit.clear()
            else:
                self.result_entrance_label.setText("Логин пользователя набран неверно")
                self.login_text_edit.clear()
        else:
            self.result_entrance_label.setText("Заполните все поля")


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginWindow()
    ex.show()
    sys.exit(app.exec())