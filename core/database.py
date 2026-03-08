import sqlite3

DB_NAME = "railway_alerts.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT,
            severity TEXT,
            action TEXT,
            source TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()


def log_alert(time, severity, action, source, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO alerts (time, severity, action, source, status)
        VALUES (?, ?, ?, ?, ?)
    """, (time, severity, action, source, status))

    conn.commit()
    conn.close()
