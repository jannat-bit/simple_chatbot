import sqlite3

def init_db():
    conn = sqlite3.connect("chat_logs.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            bot_response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_interaction(user_input, bot_response):
    conn = sqlite3.connect("chat_logs.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO interactions (user_input, bot_response)
        VALUES (?, ?)
    ''', (user_input, bot_response))
    conn.commit()
    conn.close()

# Make sure to run this once
init_db()

