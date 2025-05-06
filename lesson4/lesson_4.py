# "Таблиса relation - строки tuple / столбцы attribute "

# PRIMARY KEY 
# FROELGN KEY 

# SQL _ Strustured Queru Language 

# DDL - Data defeinition language (CREATE, ALTER, DROP TRUNCATE) - Оприделение и изменениее структура СБ(тоблицы инделсы)
# DML - DATE Mainpuilation language (SELECT < INSERT, UPDATE, MERGE) Чтение и измениние данны 

# DCL - Date Control language (GRANT REVOKE) - управления права доступа

# import sqlite3
# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()

# cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS users(
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                name TEXT NOT NULL,
#                age INTEGER
#                 )""")
# conn.commit()

# conn.close()


import sqlite3

def init_db(db_path="my_database.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

def add_user(name, age, db_path="my_database.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

def get_all_users(db_path="my_database.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id, name, age FROM users")
    rows = cur.fetchall()
    conn.close()
    return rows

if __name__ == '__main__':
    init_db()

    add_user(  "John" ,    "25")
    add_user(  "Xanber",  "20")
    add_user("asas"  ,   "  12")
    users = get_all_users()
    for uid , name, age in users:
        print(uid,name,age)
