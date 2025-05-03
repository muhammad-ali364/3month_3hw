import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout 

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        # self.init_ui()
        # Создаем элементы интерфейса
        self.question_label = QLabel("Сколько будет 2 + 3?")
        self.answer_input = QLineEdit()
        self.check_button = QPushButton("Проверить")

        # Устанавливаем менеджер компоновки
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question_label)
        self.layout.addWidget(self.answer_input)
        self.layout.addWidget(self.check_button)

        self.setLayout(self.layout)

        # Подключаем сигнал нажатия кнопки к методу проверки
        self.check_button.clicked.connect(self.check_answer)

    def check_answer(self):
        # Получаем введенное значение
        user_answer = self.answer_input.text()
        # Проверяем ответ
        if user_answer == "5":
            self.question_label.setText("Правильно!")
        else:
            self.question_label.setText("Неправильно!")

        # Очищаем поле ввода для нового ответа
        self.answer_input.clear()

if  __name__ == "_main_":
    app = QApplication(sys.argv)
    window = QuizApp()
    window.setWindowTitle("Викторина")
    window.show()
    sys.exit(app.exec_())


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