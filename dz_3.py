 
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout
# from PyQt6.QtGui import QIcon

# class MyButton(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("магазин")
#         self.setGeometry(100, 100, 300, 200)

#         self.setWindowIcon(QIcon("panic-button.ico"))

#         self.radio1 = QRadioButton("Чай", self)
#         self.radio2 = QRadioButton("кофе", self)
#         self.radio3 = QRadioButton("Сок", self)

#         self.label = QLabel("", self)
#         self.label.setWordWrap(True)

#         layout = QVBoxLayout()
#         layout.addWidget(self.radio1)
#         layout.addWidget(self.radio2)
#         layout.addWidget(self.radio3)
#         layout.addWidget(self.label)

#         self.setLayout(layout)

#         self.radio1.toggled.connect(self.radio_changed)
#         self.radio2.toggled.connect(self.radio_changed)
#         self.radio3.toggled.connect(self.radio_changed)

#     def radio_changed(self):
#         if self.radio1.isChecked():
#             self.label.setText("горячи чай!")
#         elif self.radio2.isChecked():
#             self.label.setText("горчи кофе!")
#         elif self.radio3.isChecked():
#             self.label.setText("халодни сок!")
#         self.label.adjustSize()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = MyButton()
#     main.show()
#     sys.exit(app.exec())          


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
import sqlite3

class MainWindow(QMainWindow):
    def _init_(self):
        super()._init_()

        # Создаем соединение с базой данных
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()

        # Создаем таблицу
        self.create_table()

    def create_table(self):
        # SQL-запрос для создания таблицы users
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            city TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        );
        '''
        self.cursor.execute(create_table_query)
        self.connection.commit()
        print("Таблица users успешно создана.")

    def closeEvent(self, event):
        # Закрываем соединение с базой данных при закрытии окна
        self.connection.close()
        event.accept()

if __name__ == "_main_":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Создание таблицы users")
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec())