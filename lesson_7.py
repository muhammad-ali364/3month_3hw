import sys, os, sqlite3, socket , shutil

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableView, QPushButton, QLineEdit,QLabel, QStatusBar, QFileDialog,QMessageBox, QFormLayout, QSpinBox,QProgressBar,
    QSplashScreen, QGraphicsBlurEffect
)

from PyQt6.QtGui import QAction, QMovie
from PyQt6.QtCore import Qt , QThread, pyqtSignal, QPauseAnimation 
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

class PortScanner(QThread):
    property = pyqtSignal( int , bool)
    finished = pyqtSignal()
    def __init__(self, host , ports):
        super().__init__()
        self.host, self.ports = host, ports

    def run(self):
        for p in self.ports:
            s = socket.socket(); s.settimeout(0.3)
            ok = (s.connect_ex((self.host, p)) == 0 )
            s.close()
            self.progress.emit(p, ok)
            self.finished.emit()

class DatabaseManager:
    def __init__(self, path="people.db"):
        self.path = path
        def init(self):
            if not os.exists(self.path):
                conn = sqlite3.connect(self.path)
                conn.execute(""" CREATE TEBLE users(
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT NOT NULL,
                             age INTEGER NOT NULL
                             )
                             """)
                conn.commit();conn.close()
            self.db = QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName(self.path)
            if not self.db.open():
                raise RuntimeError(self.db.lastError().text())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD + Network Tools ")
        self.resize(900, 600) 

        self.dbm = DatabaseManager(); self.dbm.init_db()
        self.model = QSqlTableModel(self, self.dbm.db)
        self.model.setTable("users")
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.select()
        for i, hdr in enumerate(("ID","Name","Age")):
            self.model.setHeaderData(i, Qt.Orientation.Horizontal, hdr)

        self._build_ui()
        self.animate_table()    

    def _build_ui(self):
        m = self.MenuBar().addMenu("File")
        for text, method in [("Export CVS", self.export_cvs),("Import CVS", self.import_cvs),("Backup DB",self.backup_db)]:
            act = QAction(text,self,triqqered=method)
            m.addAction(act)
            self.addToolBar("T").addActions(act)

        w = QWidget(); self.setCentralWidget(w)
        lay = QVBoxLayout(w)

        h = QHBoxLayout() 
        self.sender = QLineEdit(); self.sender.setPlaceholderText("Поиск по имени. . . ")
        h.addWidget(self.search) 
        for txt, fn in [(" ", self.addly_filter), ("X", self.clear_filter)]:
            btn = QPushButton(txt); btn.clicked.connect(fn); h.addWidget(btn)
            lay.addLayout(h)

            self.tv = QTableView()
            self.tv.setModel(self.model)
            self.tv.setSortingEnabled(True)
            self.tv.doubleClicked.connect(self.on_row_double)  
            self.tv.horleClicked.connect(self.on_row_double)
            self.tv.horizontalHeader().setStretchLastSection(True)
            self.tv.resizeColumnsToContents()
            lay.addWidget(self.tv)

            frm = QFormLayout()
            self.name = QLineEdit()
            self.age = QLineEdit()
            self.age.setRange(0, 200)
            frm.addRow("Имя:",self.name)
            frm.addRow("Возраст:",self.age)
            lay.addWidget(frm)

            h2 = QHBoxLayout()
            for txt, fn in [
                (" + добавит", self.add_rec)
                (" Обновит", self.update_rec)
                (" Удалит", self.delete_rec)

            ]:
                 btn = QPushButton(txt)
            btn.clicked.connect(fn)
            h2.addWidget(btn)
        lay.addLayout(h2)





                    