import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
from Project_PIY.error_window import Ui_MainWindow_Error
from Project_PIY.list_univ import Ui_MainWindow_Univ
from Project_PIY.list_spec import Ui_MainWindow_Spec
from Project_PIY.error_1_window import Ui_MainWindow_Error_2


class ErrorWindow(QMainWindow, Ui_MainWindow_Error):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ErrorWindow_2(QMainWindow, Ui_MainWindow_Error_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class List_Univ_Window(QMainWindow, Ui_MainWindow_Univ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton_list_univ.clicked.connect(lambda: self.hide())
        connection = sqlite3.connect("BD.db")
        cursor = connection.cursor()
        university = cursor.execute(
            f"""SELECT title_university, city FROM university """).fetchall()
        university = list(map(lambda j: str(j)[1:(len(str(j)) - 2):], university))
        text = ""
        for i in range(len(university)):
            elem = university[i].split(", '")
            text += elem[0] + "\n" + elem[1] + "\n"
        self.label_3.setText(text)


class List_Spec_Window(QMainWindow, Ui_MainWindow_Spec):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton_list_spec.clicked.connect(lambda: self.hide())
        connection = sqlite3.connect("BD.db")
        cursor = connection.cursor()
        spec = cursor.execute(
            f"""SELECT code_specialisation, title_specialization FROM specialization """).fetchall()
        spec = list(map(lambda j: str(j)[1:(len(str(j)) - 2):], spec))
        text = ""
        for i in range(len(spec)):
            text += spec[i] + "\n"
        self.label_2.setText(text)