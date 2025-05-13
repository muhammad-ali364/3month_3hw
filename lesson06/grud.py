from PyQt6.QtWidgets import(
    QApplication, QWidget, QPushButton,
      QHBoxLayout, QLineEdit, QLabel,QMessageBox,
      QTextEdit,QInputDialog,QVBoxLayout
)
import sys
import crud_reg

class UserApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User GLU (PyQt6)")
        self.setGeometry(100, 100, 500, 450)

        crud_reg.create_table()

        self.layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.email_input = QLineEdit()
        self.city_input = QLineEdit()
        self.phone_input = QLineEdit()

        self.layout.addWidget(QLabel("Имя:"))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(QLabel("возраст"))
        self.layout.addWidget(self.age_input)
        self.layout.addWidget(QLabel("email"))
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(QLabel("Горот"))
        self.layout.addWidget(self.city_input)
        self.layout.addWidget(QLabel("Телефон номер"))
        self.layout.addWidget(self.phone_input)

        bmn_layout = QHBoxLayout()

        self.add_bmn = QPushButton("Добавить")
        self.update_bmn = QPushButton("Обновит по ID")
        self.list_bmn = QPushButton("Показат всех")
        self.find_bmn = QPushButton("Найти")
        self.delete_bmn = QPushButton("Удалит по ID")

        bmn_layout.addWidget(self.add_bmn)
        bmn_layout.addWidget(self.update_bmn)
        bmn_layout.addWidget(self.list_bmn)
        bmn_layout.addWidget(self.find_bmn)
        bmn_layout.addWidget(self.delete_bmn)

        self.layout.addLayout(bmn_layout)

        self.uotput = QTextEdit()
        self.uotput.setReadOnly(True)
        self.layout.addWidget(self.output)

        self.setLayout(self.layout)

        self.add_bmn.clicked.connect(self.add_user)
        self.update_bmn.clicked.connect(self.update_user)
        self.list_bmn.clicked.connect(self.list_user)
        self.find_bmn.clicked.connect(self.find_user)
        self.delete_bmn.clicked.connect(self.delete_user)

    def add_user(self):
        name = self.name_input.text()
        age = self.age_input.text()
        email = self.email_input.text()
        ciry = self.city_input.text()
        phone = self.phone_input.text()

        if not name or not age:
            QMessageBox.warning(self,"Ошибка","Имя и возраст обизательны")
            return

        try:
            conn = crud_reg.connect_db()
            conn.execute("INSERT INTO users(name, age, email, city ,phone) VALUES (?, ?, ?, ?, ?)",
                         (name, age, email, city, phone))    
            conn.commit()
            conn.close()
            self.output.append()