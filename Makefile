VENV_DIR=venv

.PHONY: help setup run teams freeze clean test menu

help:
	@echo "Available commands:"
	@echo "  make setup     - Create venv and install dependencies"
	@echo "  make run       - Run the full ETL pipeline"
	@echo "  make teams     - Run only the teams pipeline"
	@echo "  make freeze    - Export requirements.txt"
	@echo "  make clean     - Delete the virtual environment"
	@echo "  make test      - Test DB and API connectivity"
	@echo "  make menu      - Interactive menu"

setup:
	@echo "Creating and configuring the virtual environment..."
	@if [ ! -d "$(VENV_DIR)" ]; then python -m venv $(VENV_DIR); fi
	@source $(VENV_DIR)/Scripts/activate && python -m pip install --upgrade pip && pip install -r requirements.txt
	@echo "Setup complete."

run:
	@echo "Running full ETL pipeline..."
	@source $(VENV_DIR)/Scripts/activate && PYTHONPATH=. python -m etl.run_pipeline

teams:
	@echo "Running teams pipeline only..."
	@source $(VENV_DIR)/Scripts/activate && PYTHONPATH=. python -m etl.pipelines.teams_pipeline

freeze:
	@source $(VENV_DIR)/Scripts/activate && pip freeze > requirements.txt
	@echo "requirements.txt updated."

clean:
	@echo "Removing virtual environment..."
	@rm -rf $(VENV_DIR)
	@echo "venv removed."

test:
	@echo "Testing DB connection and API key..."
	@source $(VENV_DIR)/Scripts/activate && PYTHONPATH=. python etl/tests/validate_env.py

menu:
	@echo ""
	@echo "ETL PIPELINE MENU"
	@echo "----------------------------"
	@echo "1) Setup"
	@echo "2) Run Full Pipeline"
	@echo "3) Run Teams Pipeline"
	@echo "4) Test Connectivity"
	@echo "5) Clean"
	@echo "----------------------------"
	@read -p "Choose an option [1-5]: " option; \
	case $$option in \
		1) make setup ;; \
		2) make run ;; \
		3) make teams ;; \
		4) make test ;; \
		5) make clean ;; \
		*) echo "Invalid option" ;; \
	esac
