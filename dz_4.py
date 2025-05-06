
# import sqlite3

# connect = sqlite3.connect("user.db")
# cursor = connect.cursor()

# cursor.execute(""" 
#                 CREATE TABLE IF NOT EXISTS user(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 age INTEGER ,
#                 email TEXT UNIQUE)""")
    

# def register():
#     name = input("Видите Ф И О !")
#     age = int(input("Видите свой возрастc !"))
#     email = input("Видите свой email !")

#     cursor.execute(""" INSERT INTO user
#                    (name, age, email)
#                    VALUES(?,?,?)""",(name , age , email))
#     connect.commit()
# register()
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QLabel

class DrinkSelector(QWidget):
    def _init_(self):
        super()._init_()
        
        self.setWindowTitle("Выбирите тавар")
        self.setGeometry(100,100,200,250)
        # Создаем вертикальный layout
        self.layout = QVBoxLayout()
        self.move(50,50)
        
        self.checkbox = QCheckBox()
        self.move(100,50)
        # Создаем чекбоксы
        self.checkbox = QCheckBox("Чай",self)
        self.coffee_checkbox = QCheckBox("Кофе",self)
        self.juice_checkbox = QCheckBox("Сок",self)

        # self.layout = QVBoxLayout()
        # self.move(50,50)

        # Добавляем чекбоксы в layout
        self.layout.addWidget(self.tea_checkbox)
        self.layout.addWidget(self.coffee_checkbox)
        self.layout.addWidget(self.juice_checkbox)
        self.move(50,70)
        # Создаем кнопку
        self.button = QPushButton("Показать выбор")
        self.button.move(50,60)
        self.button.clicked.connect(self.show_selection)

        # Добавляем кнопку в layout
        self.layout.addWidget(self.button)

        # Создаем метку для отображения результата
        self.label = QLabel("вырвв")
        self.move(50,50)
        self.layout.addWidget(self.label)

        # Устанавливаем layout для окна
        self.setLayout(self.show_selection)

        # Устанавливаем заголовок окна
        self.setWindowTitle("Выбор напитков")

    def show_selection(self):
        selections = []

        # Проверяем состояние каждого чекбокса
        if self.tea_checkbox.isChecked():
            selections.append("Чай")
        if self.coffee_checkbox.isChecked():
            selections.append("Кофе")
        if self.juice_checkbox.isChecked():
            selections.append("Сок")

        # Обновляем текст метки
        if selections:
            self.label.setText(", ".join(selections))
        else:
            self.label.setText("Ничего не выбрано")

        # Подстраиваем размер метки
        self.label.adjustSize()

if __name__ == "_main_":
    app = QApplication(sys.argv)
    window = DrinkSelector()
    window.show()
    sys.exit(app.exec())
