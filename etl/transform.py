import json

# 📂 Dossier où sont stockées les données JSON
DATA_DIR = "etl/data"

def transform_teams():
    """Lit le fichier JSON et transforme les données des équipes."""
    file_path = f"{DATA_DIR}/teams.json"

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        transformed = []
        for team in raw_data.get("teams", []):
            transformed.append({
                "id": team["id"],
                "nom": team["name"],
                "short_name": team["shortName"],
                "tla": team["tla"],  
                "fondation": team.get("founded", None),  
                "venue": team.get("venue", None)  
            })

        return transformed

    except FileNotFoundError:
        print(f"❌ Le fichier {file_path} n'existe pas. Exécute d'abord extract.py.")
        return []

if __name__ == "__main__":
    transformed_data = transform_teams()
    print("✅ Données transformées :", transformed_data)
