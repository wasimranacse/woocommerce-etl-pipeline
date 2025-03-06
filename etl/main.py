# Runs the full ETL pipeline

from extract import extract_data
from transform import transform_data
from load import load_data

file_path = "data/orders.csv"

# Run ETL Pipeline
df = extract_data(file_path)
df = transform_data(df)
load_data(df)

