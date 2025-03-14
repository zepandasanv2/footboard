import sqlite3
import transform  # On importe les données transformées

DB_PATH = "database/footboard.db"

def insert_teams():
    """Insère les équipes dans la table teams."""
    teams = transform.transform_teams()  # 🔥 Récupère les équipes transformées

    if not teams:
        print("⚠️ Aucune équipe à insérer.")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        for team in teams:
            cursor.execute("""
                INSERT INTO teams (id, nom, short_name, tla, fondation, venue)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO NOTHING
            """, (team["id"], team["nom"], team["short_name"], team["tla"], team["fondation"], team["venue"]))

        conn.commit()
        print(f"✅ {len(teams)} équipes insérées avec succès dans teams !")

        conn.close()
    
    except Exception as e:
        print(f"❌ Erreur lors de l'insertion des équipes : {e}")

if __name__ == "__main__":
    insert_teams()
