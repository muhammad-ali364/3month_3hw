

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