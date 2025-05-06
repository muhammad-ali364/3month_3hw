# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# # import sys
# # from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout 

# class QuizApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         # self.init_ui()
#         # Создаем элементы интерфейса
#         self.question_label = QLabel("Сколько будет 2 + 3?")
#         self.answer_input = QLineEdit()
#         self.check_button = QPushButton("Проверить")

#         # Устанавливаем менеджер компоновки
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.question_label)
#         self.layout.addWidget(self.answer_input)
#         self.layout.addWidget(self.check_button)

#         self.setLayout(self.layout)

#         # Подключаем сигнал нажатия кнопки к методу проверки
#         self.check_button.clicked.connect(self.check_answer)

#     def check_answer(self):
#         # Получаем введенное значение
#         user_answer = self.answer_input.text()
#         # Проверяем ответ
#         if user_answer == "5":
#             self.question_label.setText("Правильно!")
#         else:
#             self.question_label.setText("Неправильно!")

#         # Очищаем поле ввода для нового ответа
#         self.answer_input.clear()

# if  __name__ == "_main_":
#     app = QApplication(sys.argv)
#     window = QuizApp()
#     window.setWindowTitle("Викторина")
#     window.show()
#     sys.exit(app.exec_())


# import sys  # Импортируем системный модуль, который позволит нам взаимодействовать с Python
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# # Определяем класс, который будет представлять наше приложение
# class QuizApp(QWidget):
#     def _init_(self):
#         super()._init_()  # Инициализируем класс родителя

#         # Создаем элементы интерфейса
#         self.question_label = QLabel("Сколько будет 2 + 3?")  # Метка с вопросом
#         self.answer_input = QLineEdit()  # Поле для ввода ответа
#         self.check_button = QPushButton("Проверить")  # Кнопка для проверки ответа

#         # Устанавливаем менеджер компоновки
#         self.layout = QVBoxLayout()  # Создаем вертикальный компоновщик
#         self.layout.addWidget(self.question_label)  # Добавляем метку в компоновщик
#         self.layout.addWidget(self.answer_input)  # Добавляем поле ввода в компоновщик
#         self.layout.addWidget(self.check_button)  # Добавляем кнопку в компоновщик

#         self.setLayout(self.layout)  # Устанавливаем компоновщик для виджета

#         # Подключаем сигнал нажатия кнопки к методу проверки
#         self.check_button.clicked.connect(self.check_answer)

#     def check_answer(self):
#         # Получаем текст, введенный пользователем, из поля ввода
#         user_answer = self.answer_input.text()
#         # Проверяем, был ли введен правильный ответ
#         if user_answer == "5":
#             self.question_label.setText("Правильно!")  # Изменяем текст метки на "Правильно!"
#         else:
#             self.question_label.setText("Неправильно!")  # Изменяем текст метки на "Неправильно!"

#         # Очищаем поле ввода для нового ответа, чтобы пользователь мог ввести новое значение
#         self.answer_input.clear()

# # Основной блок, который запускает приложение
# if __name__ == "_main_":
#     app = QApplication(sys.argv)  # Создаем экземпляр приложения
#     window = QuizApp()  # Создаем экземпляр нашего класса QuizApp
#     window.setWindowTitle("Викторина")  # Устанавливаем заголовок окна
#     window.show()  # Показываем окно
#     sys.exit(app.exec_())

import sys 
from PyQt6.QtWidgets import QApplication, QWidget,QCheckBox,QPushButton,QLabel

class DrinSelektor( QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Магазин")
        self.setGeometry(100,100,300,250)

        self.tea_cd = QCheckBox("Чай")
        self.coffee_cd =QCheckBox("Кофе")
        self.juice_cd = QCheckBox("Сок")

        self.button = QPushButton("Паказать выбор")

        self.button.clicked.connect(self.show_selection)

        self.label = QLabel("",self)

        layout = QApplication()
        layout.allWindows(self.tea_cd)
        layout.allWindows(self.coffee_cd) 
        layout.allWindows(self.juice_cd)
        layout.allWindows(self.button)
        layout.allWindows(self.label)

        self.setLayout(layout)
        self.setWindowTitle("Выбор напиток")

    def show_selection(self):
        selected =[]
        if self.tea_cd.isChecked():
            selected.append("чай")
        elif self.coffee_cd.isChecked():
            selected.append("кофе")
        elif self.juice_cd.isChecked():
            selected.append("сок")

        self.label.setText(",".join(selected)if selected else 
                           "Нечего не выбрано")  
        self.label.adjustSize()   

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = DrinSelektor()
    window.show()
    sys.exit(app.exit())                   


