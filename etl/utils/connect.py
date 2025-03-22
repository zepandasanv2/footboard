import sqlite3

DB_PATH = "database/footboard.db"

def connect_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor

if __name__ == "__main__":
    conn, cursor = connect_db()
    print("Connection to SQLite successful!")
    conn.close()
