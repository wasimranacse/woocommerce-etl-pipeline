# Extract data from CSV

import pandas as pd

def extract_data(file_path="data/orders.csv"):
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())


