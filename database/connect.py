import sqlite3

# Définir le chemin de la base de données
DB_PATH = "footboard.db"

def connect_db():
    """Connecte à la base SQLite et retourne le curseur."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor

if __name__ == "__main__":
    conn, cursor = connect_db()
    print("✅ Connection to SQLite successful!")
    conn.close()
