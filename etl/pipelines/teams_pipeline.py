import time
from etl.extract.extract_teams import get_teams
from etl.transform.transform_teams import transform_teams
from etl.load.load_teams import insert_teams


from datetime import datetime


GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def run_teams_pipeline():
    start_time = time.time()
    log_lines = []

    print(f"\n{YELLOW}[1/3] Extracting teams from API...{RESET}")
    log_lines.append("[1/3] Extracting teams from API...")
    get_teams()

    print(f"{YELLOW}[2/3] Transforming team data...{RESET}")
    log_lines.append("[2/3] Transforming team data...")
    transformed_teams = transform_teams()

    print(f"{YELLOW}[3/3] Inserting data into the database...{RESET}")
    log_lines.append("[3/3] Inserting data into the database...")
    insert_teams(transformed_teams)

    duration = round(time.time() - start_time, 2)

    print(f"\n{GREEN}Pipeline finished successfully in {duration} seconds!{RESET}\n")
    print(f"{YELLOW}Summary:{RESET}")
    print("-------------------------------")
    print(" Step       | Status")
    print("-------------------------------")
    print(f" Extract    | Done")
    print(f" Transform  | Done")
    print(f" Load       | Done")
    print("-------------------------------")
    print(f"{GREEN}🚀 All operations completed without errors!{RESET}\n")

    log_lines.append(f"\nPipeline completed in {duration} seconds.")
    log_lines.append("All steps executed successfully.")

    write_log(log_lines)


def write_log(lines):
    log_dir = "logs"
    from os import makedirs
    makedirs(log_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"{log_dir}/teams_pipeline_{timestamp}.log"

    with open(log_file, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"Log saved to: {log_file}")








