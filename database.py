import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # NOTES TABLE
    c.execute('''CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        day INTEGER,
        content TEXT
    )''')

    # PROGRESS TABLE
    c.execute('''CREATE TABLE IF NOT EXISTS progress (
        day INTEGER PRIMARY KEY,
        completed INTEGER DEFAULT 1
    )''')

    # STREAK TABLE
    c.execute('''CREATE TABLE IF NOT EXISTS streak (
        id INTEGER PRIMARY KEY,
        current_streak INTEGER
    )''')

    conn.commit()
    conn.close()