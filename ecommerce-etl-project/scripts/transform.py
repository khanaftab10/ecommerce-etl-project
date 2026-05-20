import pandas as pd


def transform_data(df):

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Convert order date
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    # Rename columns
    df.columns = [
        'order_id',
        'order_date',
        'customer_name',
        'region',
        'product_name',
        'category',
        'sales',
        'quantity',
        'profit',
        'city'
    ]

    return df