import sqlite3
import transform

DB_PATH = "database/footboard.db"

def insert_teams():
    teams = transform.transform_teams()

    if not teams:
        print("No team to insert.")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        for team in teams:
            cursor.execute("""
                INSERT INTO teams (id, nom, short_name, tla, fondation, venue)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO NOTHING
            """, (
                team["id"],
                team["nom"],
                team["short_name"],
                team["tla"],
                team["fondation"],
                team["venue"]
            ))

        conn.commit()
        print(f"{len(teams)} teams successfully inserted into 'teams' table.")

        conn.close()

    except Exception as e:
        print(f"Error inserting teams: {e}")

if __name__ == "__main__":
    insert_teams()

