import sys
import pickle
import datetime

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from Every_Day_Calendar.Best1 import Ui_MainWindow
from Every_Day_Calendar.Create1 import Ui_FormCreateTask
from Every_Day_Calendar.Edit import Ui_FormTaskEdit


class TaskSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # подгрузим данные
        try:
            # из файла data.txt берем дату и задачи
            with open("data.txt", "rb") as f:
                self.data = pickle.load(f)
        except EOFError:
            self.data = []
        # соеденим нажатие на календарь с функцией
        self.calendarWidget.clicked.connect(self.calendar_clicked)
        # кнопка создать
        self.pushButton.clicked.connect(self.create_task)
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.edit_task)

    def calendar_clicked(self, date):
        self.date = date
        date = date.toPyDate()
        date_list_task = list(map(lambda x: f"{x[0]}: {x[1]}",
                                  filter(lambda t: t[0] == date, self.data)))
        self.dateEdit.setDate(self.date)
        self.listView.clear()
        self.listView.addItems(date_list_task)

    def create_task(self):
        # открываем окно для создания заданий
        self.wnd_create = CreateTaskWindow(self.data, self.date)
        self.wnd_create.show()

    def edit_task(self):
        t = [s.text() for s in self.listView.selectedItems()]
        for i in t:
            self.wnd_edit = EditTaskWindow(i, self.data, self.date)
            self.wnd_edit.show()

    def delete(self):
        selected = self.listView.selectedItems()
        names = [s.text() for s in selected]
        for i in names:
            i = i.split(": ")
            for t in range(len(self.data)):
                if i[1] == self.data[t][1]:
                    if self.date == self.data[t][0]:
                        del self.data[t]
                        with open("data.txt", "wb") as f:
                            pickle.dump(self.data, f)
                        self.calendar_clicked(self.date)
                        break


class CreateTaskWindow(QWidget, Ui_FormCreateTask):
    """создание задач"""
    def __init__(self, list_tasks, date):
        super().__init__()
        self.setupUi(self)
        self.data = list_tasks
        self.dateTimeEdit_create.setDate(date)
        self.pushButton_2_create.clicked.connect(self.ok)
        self.pushButton_1_create.clicked.connect(lambda: self.hide())

    def ok(self):
        description = self.lineEdit_task_create.text()
        date_time = self.dateTimeEdit_create.date().toPyDate()
        self.data.append((date_time, description))
        with open("data.txt", "wb") as f:
            pickle.dump(self.data, f)
        self.hide()


class EditTaskWindow(QWidget, Ui_FormTaskEdit):
    def __init__(self, elem, data, date):
        super().__init__()
        self.setupUi(self)
        self.data = data
        self.date = date
        self.task = elem.split(": ")
        self.lineEdit_task_edit.setText(self.task[1])
        self.dateTimeEdit_edit.setDate(self.date)
        self.pushButton_2_edit.clicked.connect(self.ok)
        self.pushButton_1_edit.clicked.connect(lambda: self.hide())

    def ok(self):
        description = self.lineEdit_task_edit.text()
        date_time = self.dateTimeEdit_edit.date().toPyDate()
        self.data.append((date_time, description))
        for t in range(len(self.data)):
            if self.task[1] == self.data[t][1]:
                if self.date == self.data[t][0]:
                    del self.data[t]
                    with open("data.txt", "wb") as f:
                        pickle.dump(self.data, f)
                    break
        self.hide()


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    wnd = TaskSystem()
    wnd.show()
    sys.exit(app.exec())