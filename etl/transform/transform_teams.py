import json

DATA_DIR = "etl/data"

def transform_teams():
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
        print(f"File {file_path} not found. Please run extract.py first.")
        return []

if __name__ == "__main__":
    transformed_data = transform_teams()
    print("Transformed data:", transformed_data)
