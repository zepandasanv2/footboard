import requests
import json
import os
from dotenv import load_dotenv

# 🔑 Ta clé API
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.football-data.org/v4"

# 📂 Dossier où stocker les fichiers JSON
DATA_DIR = "etl/data"
os.makedirs(DATA_DIR, exist_ok=True)  # Crée le dossier si inexistant

# 🔥 Fonction pour récupérer les équipes
def get_teams(competition="PL"):
    url = f"{BASE_URL}/competitions/{competition}/teams"
    headers = {"X-Auth-Token": API_KEY}
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        teams = response.json()
        
        # 💾 Enregistrement automatique en JSON
        with open(f"{DATA_DIR}/teams.json", "w", encoding="utf-8") as f:
            json.dump(teams, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Données des équipes enregistrées dans {DATA_DIR}/teams.json")
        return teams
    else:
        print(f"❌ Erreur API: {response.status_code}")
        return None

if __name__ == "__main__":
    get_teams()

