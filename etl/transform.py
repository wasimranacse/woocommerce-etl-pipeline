import pandas as pd

def transform_data(df):
    """Cleans and transforms order data."""
    
    # Convert Date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    
    # Standardise Order Status
    df['Status'] = df['Status'].str.lower().str.strip()
    
    # Fill missing values
    df.fillna({'Customer': 'Guest', 'Customer type': 'New'}, inplace=True)
    
    # Extract Year-Month for trend analysis (convert to string)
    df['Year-Month'] = df['Date'].dt.to_period('M').astype(str)
    
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/orders.csv")
    transformed_df = transform_data(df)
    print(transformed_df.head())
