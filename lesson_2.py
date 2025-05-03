# 1
# import sys 
# from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# app = QApplication(sys.argv)


# window = QWidget()
# window.setWindowTitle("Привет, PyQt6!")
# window.setGeometry(100, 100, 300, 200)


# label = QLabel("Hello, World!", parent=window)
# label.move(100, 80)
# window.show()

# sys.exit(app.exec())

# 2

# import sys
# from PyQt6.QtWidgets import QApplication, QLabel,QWidget


# class MainWindow(QWidget): 
#     def __init__(self):
#         super().__init__()
#         self.init__ui()

#     def init__ui(self):
#         self.setWindowTitle("Дукомпозиция в PyQt6")
#         self.setGeometry(200, 200, 350, 250)
#         label = QLabel("Это окно создано через класс!",self)
#         label.move(50, 100)

# if __name__== '__main__':   
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())     
# 3

# import sys
# from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         self.setWindowTitle("Ввод текста")
#         self.setGeometry(200, 200, 400, 150)

#         self.label = QLabel("Здесь появится текст", self)
#         self.label.move(20, 20)

#         self.input = QLineEdit(self)
#         self.input.move(20, 50)
#         self.input.setPlaceholderText("Введите что-нибудь...")

#         self.button = QPushButton("Показать", self)
#         self.button.move(250, 47)
#         self.button.clicked.connect(self.show_text)

#     def show_text(self):
#         text = self.input.text()
#         self.label.setText(text)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys,exit(app.exec()) 

# 4

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Работа с Layout")
        self.setGeometry(200, 200 , 300 , 150)

        self.label = QLabel("Пример с Layout" ,self)
        self.button = QPushButton("Изменить текст", self)
        self.button.clicked.connect(self.change_label)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def change_label(self):
        self.label.setText("Текст изменен!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys,exit(app.exec())
