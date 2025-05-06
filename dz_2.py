

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

app = QApplication(sys.argv)

class QuizApp(QWidget):
    def _init_(self):
        super()._init_()
        self.initUI()

    def initUI(self):
        
        self.label = QLabel('Сколько будет 2 + 3?', parent=layout)
        self.input_field = QLineEdit(self)
        self.check_button = QPushButton('Проверить', self)

        
        self.check_button.clicked.connect(self.check_answer)

    
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.check_button)

        self.setLayout(layout)

        self.setWindowTitle('Проверка ответа')
        self.show()

    def check_answer(self):
        answer = self.input_field.text()
        if answer == '5':
            self.label.setText('Правильно!')
        else:
            self.label.setText('Неправильно!')

if __name__ == '_main_':
    app = QApplication(sys.argv)
    ex = QuizApp()
    sys.exit(app.exec_())



# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTabWidget


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Вкладки")
#         self.setGeometry(100, 100, 400, 300)

#         layout = QVBoxLayout()
#         tabs = QTabWidget()

#         tab1 = QWidget("")
#         tab1_layout = QVBoxLayout()
#         tab1_layout.addWidget(QLabel("Это первая вкладка"))
#         tab1.setLayout(tab1_layout)

#         tab2 = QWidget()
#         tab2_layout = QVBoxLayout()
#         tab2_layout.addWidget(QLabel("Это вторая вкладка"))
#         tab2.setLayout(tab2_layout)

#         tab3 = QWidget()
#         tab3_layout = QVBoxLayout()
#         tab3_layout.addWidget(QLabel("Это третья вкладка"))
#         tab3.setLayout(tab3_layout)

#         tabs.addTab(tab1, "Вкладка 1")
#         tabs.addTab(tab2, "Вкладка 2")
#         tabs.addTab(tab3, "Вкладка 3")

#         layout.addWidget(tabs)
#         self.setLayout(layout)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())

