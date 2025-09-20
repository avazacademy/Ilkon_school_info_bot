import sqlite3

DB_NAME = "school.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
    """)
    conn.commit()
    conn.close()

def add_subject(name: str):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO subjects (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_subjects():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM subjects")
    rows = cur.fetchall()
    conn.close()
    return rows
