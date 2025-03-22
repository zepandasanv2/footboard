import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.football-data.org/v4"

DATA_DIR = "etl/data"
os.makedirs(DATA_DIR, exist_ok=True)

def get_teams(competition="PL"):
    url = f"{BASE_URL}/competitions/{competition}/teams"
    headers = {"X-Auth-Token": API_KEY}
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        teams_data = response.json()

        file_path = f"{DATA_DIR}/teams.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(teams_data, f, indent=2, ensure_ascii=False)
        
        print(f"Team data saved to {file_path}")
        return teams_data
    else:
        print(f"API error: {response.status_code}")
        return None
