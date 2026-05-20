from sqlalchemy import create_engine


def load_data(df):

    username = 'postgres'
    password = 'postgrey123'
    host = 'localhost'
    port = '5432'
    database = 'ecommerce_db'

    engine = create_engine(
        f'postgresql://{username}:{password}@{host}:{port}/{database}'
    )

    df.to_sql(
        'sales',
        engine,
        if_exists='append',
        index=False
    )

    print('Data loaded successfully!')