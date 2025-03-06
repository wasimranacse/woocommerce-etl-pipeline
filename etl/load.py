# Load data into PostgreSQL

import pandas as pd
from sqlalchemy import create_engine
# URL-encoded password for special characters
DATABASE_URL = "postgresql://postgres:Ranadts%401122%23@localhost:5432/woocommerce_db"


def load_data(df):
    """Loads transformed data into PostgreSQL."""
    engine = create_engine(DATABASE_URL)
    df.to_sql("orders", engine, if_exists="replace", index=False)
    print("✅ Data successfully loaded into PostgreSQL!")

if __name__ == "__main__":
    df = pd.read_csv("data/orders.csv")
    load_data(df)


