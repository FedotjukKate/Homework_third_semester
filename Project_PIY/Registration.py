import sqlite3

from PyQt5.QtWidgets import QMainWindow
from Project_PIY.registration_window import Ui_MainWindow
from Project_PIY.Site_window import SiteWindow


class RegistrationWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton_login.clicked.connect(self.login_in)
        self.click = [0, 0, 0, 0]
        self.name_text_edit.cursorPositionChanged.connect(lambda: self.text_click(0))
        self.create_login_text_edit.cursorPositionChanged.connect(lambda: self.text_click(1))
        self.create_password_text_edit.cursorPositionChanged.connect(lambda: self.text_click(2))
        self.confim_password_text_edit.cursorPositionChanged.connect(lambda: self.text_click(3))

    def login_in(self):
        connection = sqlite3.connect("Registration_db.db")
        cursor = connection.cursor()
        if self.name_text_edit.toPlainText() != "" and self.create_login_text_edit.toPlainText() != ""\
                and self.create_password_text_edit.toPlainText() != ""\
                and self.confim_password_text_edit.toPlainText() != "":
            if self.name_text_edit.toPlainText() != "введите имя" and self.create_login_text_edit.toPlainText() != "придумайте логин"\
                    and self.create_password_text_edit.toPlainText() != "придумайте пароль"\
                    and self.confim_password_text_edit.toPlainText() != "подтвердите пароль":
                if len(self.create_password_text_edit.toPlainText()) >= 8:
                    if self.create_password_text_edit.toPlainText() == self.confim_password_text_edit.toPlainText():
                        try:
                            st = "^-._[]+$/\|"
                            st2 = "@-._[]+/\|()"
                            alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                            P = True
                            Pas = False
                            for sym in self.name_text_edit.toPlainText():
                                if not sym.isalnum() and sym not in st:
                                    P = False
                                    self.result_reg_label.setText("Имя пользователя может содержать"
                                                                  " буквы, цифры, символы ^-._[]+$/\|")
                                    break
                            for sym in self.create_login_text_edit.toPlainText():
                                if ((not sym.isalnum() and sym not in st2) or (sym in alphabet)) and P:
                                    P = False
                                    self.result_reg_label.setText("Логин пользователя может содержать"
                                                                  " буквы латинского алфавита, цифры, символы @-._[]+/\|()")
                                    break
                            for sym in self.create_password_text_edit.toPlainText():
                                if ((not sym.isalnum() and sym not in st) or (sym in alphabet)) and P:
                                    P = False
                                    self.result_reg_label.setText("Пароль пользователя может содержать"
                                                                  " буквы латинского алфавита, цифры, символы @^-._[]+$/\|")
                                    break
                            for sym in self.create_password_text_edit.toPlainText():
                                if sym.isalpha() and P:
                                    Pas = True
                                    break
                            if P:
                                if Pas:
                                    user = (self.name_text_edit.toPlainText(), self.create_login_text_edit.toPlainText(),
                                            self.create_password_text_edit.toPlainText())
                                    query = "INSERT INTO User(user_name, login, password) VALUES (?, ?, ?)"
                                    cursor.execute(query, user)
                                    connection.commit()
                                    user_id = cursor.execute(
                                        f"""SELECT user_id FROM User WHERE login = "{self.create_login_text_edit.toPlainText()}" """).fetchone()
                                    user_id = str(user_id)[1:(len(str(user_id)) - 2)]
                                    self.site(user_id)
                                    self.hide()
                                else:
                                    self.result_reg_label.setText("В пароле должно содержаться не меньше 1 буквы")
                        except sqlite3.IntegrityError:
                            user_names = list(map(lambda x: str(x)[2:(len(str(x)) - 3):],
                                                  cursor.execute("""SELECT user_name FROM User""").fetchall()))
                            user_login = list(map(lambda x: str(x)[2:(len(str(x)) - 3):],
                                                  cursor.execute("""SELECT login FROM User""").fetchall()))
                            if self.name_text_edit.toPlainText() in user_names:
                                self.result_reg_label.setText("Это имя уже занято")
                                self.name_text_edit.clear()
                            elif self.create_login_text_edit.toPlainText() in user_login:
                                self.result_reg_label.setText("Пользователь с этим логином уже зарегестрирован")
                                self.create_login_text_edit.clear()
                    else:
                        self.result_reg_label.setText("Пароли не совпадают")
                else:
                    self.result_reg_label.setText("Пароль должен содержать не меньше 8 символов")
            else:
                self.result_reg_label.setText("Заполните все поля")
        else:
            self.result_reg_label.setText("Заполните все поля")

    def site(self, id):
        self.wnd_create = SiteWindow(id)
        self.wnd_create.show()

    def text_click(self, i):
        if i == 0 and self.click[0] == 0:
            self.click[0] += 1
            self.name_text_edit.clear()

        if i == 1 and self.click[1] == 0:
            self.click[1] += 1
            self.create_login_text_edit.clear()
        if i == 2 and self.click[2] == 0:
            self.click[2] += 1
            self.create_password_text_edit.clear()
        if i == 3 and self.click[3] == 0:
            self.click[3] += 1
            self.confim_password_text_edit.clear()