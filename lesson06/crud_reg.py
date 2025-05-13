import sqlite3

DB_PATH = "users.db"
 
def connect_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGNA foreign_keys = ON;")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   age INTEGER,
                   email TEXT UNIQUE,
                   city TEXT NOT NULL,
                   phone TEXT
                )
    
                """) 
    conn.commit()
    conn.close()

def update_users(users_id, name, age, email, city, phone):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE users
            SET name = ?, age = ?, email = ? city = ?, phone = ?
                   WHERE id = ?
                   """(name, age, email, city, phone, users_id))
    conn.commit()
    update = cursor.rowcount
    conn.close()
    return update