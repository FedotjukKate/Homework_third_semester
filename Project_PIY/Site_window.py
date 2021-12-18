import sqlite3

from PyQt5.QtWidgets import QMainWindow
from Project_PIY.site_page import Ui_MainWindow_1
from Project_PIY.Result_and_history import ResultWindow, RequestHistoryWindow
from Project_PIY.For_site_page import ErrorWindow, List_Univ_Window, List_Spec_Window, ErrorWindow_2
from Project_PIY.exit_window import Ui_MainWindow_Exit


class SiteWindow(QMainWindow, Ui_MainWindow_1):
    def __init__(self, user_id):
        super().__init__()
        self.id = int(user_id)
        self.setupUi(self)
        self.initUi()
        connection = sqlite3.connect("Registration_db.db")
        cursor = connection.cursor()
        user_name = cursor.execute(f"""SELECT user_name FROM User WHERE user_id = "{int(self.id)}" """).fetchone()
        user_name = str(user_name)[2: (len(user_name) - 4)]
        self.label_8.setText(user_name)

    def initUi(self):
        self.search_pushButton.clicked.connect(self.search)
        self.exit_pushButton.clicked.connect(self.exit)
        self.available_uni_pushButton.clicked.connect(self.List_univ)
        self.specialty_pushButton.clicked.connect(self.List_spec)
        self.request_history_pushButton.clicked.connect(self.history)

    def search(self):
        town, first_subject = self.town_comboBox.currentText(), self.subject_comboBox_1.currentText(),
        second_subject, third_subject = self.subject_comboBox_2.currentText(), self.subject_comboBox_3.currentText()
        summ = self.sum_textEdit.toPlainText()
        if town != "Любой" or first_subject != "Любой" or second_subject != "Любой"\
                or third_subject != "Любой" or summ != "":
            if summ != "":
                if summ.isdigit():
                    if int(summ) > 0:
                        self.result(town, first_subject, second_subject, third_subject, summ)
                    else:
                        self.sum_textEdit.setText("")
                        self.error_2()
                else:
                    self.sum_textEdit.setText("")
                    self.error_2()
            else:
                self.result(town, first_subject, second_subject, third_subject, summ)
        else:
            self.error()

    def List_univ(self):
        self.wnd_create = List_Univ_Window()
        self.wnd_create.show()

    def List_spec(self):
        self.wnd_create = List_Spec_Window()
        self.wnd_create.show()

    def error(self):
        self.wnd_create = ErrorWindow()
        self.wnd_create.show()

    def error_2(self):
        self.wnd_create = ErrorWindow_2()
        self.wnd_create.show()

    def exit(self):
        self.wnd_create = ExitWindow(self.id)
        self.wnd_create.show()
        self.hide()

    def result(self, t, f_s, s_s, th_s, summ):
        self.wnd_create = ResultWindow(self.id, t, f_s, s_s, th_s, summ)
        self.wnd_create.show()

    def history(self):
        self.wnd_create = RequestHistoryWindow(self.id)
        self.wnd_create.show()


class ExitWindow(QMainWindow, Ui_MainWindow_Exit):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton_exit_cancel.clicked.connect(self.site)
        self.pushButton_exit_yes.clicked.connect(lambda: self.hide())

    def site(self):
        self.hide()
        self.wnd_create = SiteWindow(self.id)
        self.wnd_create.show()