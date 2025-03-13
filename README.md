# Football Club Dashboard ⚽📊

## Description
This project is a **Football Club Dashboard** built using **Power BI** to analyze and visualize match statistics and player performance. The data is sourced from multiple inputs, primarily a **relational database**, and processed through **Python ETL scripts** to ensure accuracy and consistency.

## Features
- **Player Performance Analysis:** Track goals, assists, minutes played, and other key metrics.
- **Match Statistics:** View team performances, possession percentages, shots, passes, and more.
- **Automated ETL Pipeline:** Python scripts extract, transform, and load (ETL) data from various sources into a structured database.
- **Database-Driven Insights:** The dashboard is powered by a relational database (MySQL/PostgreSQL) with optimized data structures.
- **Power BI Visualizations:** Interactive charts, tables, and KPIs to gain deeper insights into club and player performance.

## Technology Stack
- **Power BI** (Data Visualization)
- **Python** (ETL - Pandas, SQLAlchemy, API handling)
- **MySQL/PostgreSQL** (Database Management)
- **GitHub** (Version Control)

## Installation & Setup
### 1. Clone the Repository
```sh
git clone https://github.com/your-username/football-dashboard.git
cd football-dashboard
```

### 2. Set Up the Database
- Run the SQL schema provided in the `database/schema.sql` file to create the database structure.

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the ETL Pipeline
```sh
python etl/extract.py
python etl/transform.py
python etl/load.py
```

### 5. Load Data into Power BI
- Connect Power BI to the database and build visualizations.

## License
This project is licensed under the [MIT License](LICENSE).

## Contributions
Contributions are welcome! Feel free to open issues and pull requests.

## Contact
For any questions or suggestions, feel free to reach out via GitHub Issues.



