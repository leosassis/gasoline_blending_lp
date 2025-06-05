import pandas as pd


def extract_data() -> pd:
    """ 
    Extracts the data for products and steams.
    
    Returns:
            - df_products (pd): data frame with information for the products. 
            - df_streams (pd): data frame with information for the streams. 
    """
    
    
    df_products = pd.read_excel('input_data/data.xlsx', 'Products')
    df_streams = pd.read_excel('input_data/data.xlsx', 'Streams')

    return df_products, df_streams