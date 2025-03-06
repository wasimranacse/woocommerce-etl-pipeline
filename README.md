### Project Name: WooCommerce Sales ETL & Analytics Pipeline

##### This project builds a scalable ETL pipeline for processing WooCommerce sales data, storing it in a PostgreSQL data warehouse, and performing advanced data analysis and reporting for business insights.

📂 woocommerce-sales-etl  
├── 📄 README.md  
├── 📂 data  
│   ├── orders.csv  # WooCommerce orders dataset  
├── 📂 etl  
│   ├── extract.py   # Extract data from CSV  
│   ├── transform.py # Clean & preprocess data  
│   ├── load.py      # Load data into PostgreSQL  
│   ├── main.py      # Runs the full ETL pipeline  
├── 📂 db  
│   ├── schema.sql   # Database Schema (Star Schema)  
│   ├── queries.sql  # SQL Queries for analysis  
├── 📂 airflow  
│   ├── sales_etl_dag.py  # Airflow DAG for automation  
├── 📂 notebooks  
│   ├── sales_analysis.ipynb  # Jupyter Notebook for SQL & Visualisation  
├── 📂 dashboards  
│   ├── power_bi.pbix  # Power BI Dashboard  
│   ├── tableau.twbx   # Tableau Workbook  
├── 📄 requirements.txt  


### 1️. ETL Pipeline Implementation
#####  Extract: Read the WooCommerce Orders Data
#####  File: etl/extract.py

### 2️. Transform – Clean & Prepare the Data
##### transform.py

### 3. Load – Store Data into PostgreSQL
##### load.py

### 4. Orchestrate the ETL Pipeline
##### main.py

### 5. SQL Queries for Sales Analysis



