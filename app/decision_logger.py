
import sqlite3

def log_decision(query, decision):
    conn = sqlite3.connect("data/decision_log.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT,
        decision TEXT,
        justification TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute("INSERT INTO logs (query, decision, justification) VALUES (?, ?, ?)",
              (query, decision["Decision"], str(decision["Justification"])))
    conn.commit()
    conn.close()
