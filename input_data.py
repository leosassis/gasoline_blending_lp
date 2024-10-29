import pandas as pd

def extract_data() -> pd:
    df_products = pd.read_excel('data/data.xlsx', 'Products')
    df_streams = pd.read_excel('data/data.xlsx', 'Streams')

    return df_products, df_streams