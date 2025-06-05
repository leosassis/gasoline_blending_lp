import pandas as pd
import pyomo.environ as pyo


def _df_data_to_dictionary(df: pd, flow: str, attribute: str) -> dict:
    """ 
    Extracts the data related to each parameter.     
    
    Args:
        - df (pd): a data frame with data.
        - flow (str): the flow type.
        - attribute (str): an atrribute that indicates the type of data.
        
    Returns:
        - dict: a dictionary with the data to be loaded in the parameter.
    """
    
    
    return df[[flow,attribute]].set_index(flow).to_dict()[attribute]


def create_parameters(model: pyo.ConcreteModel, df_products: pd, df_streams: pd) -> None:
    """ 
    Creates all necessary parameters for the optimization problem.     
    
    Args:
        - model (pyo.ConcreteModel): a Pyomo model.
        - df_products (pd): a data frame with data related to products.
        - df_streams (pd): a data frame with data related to streams. 
    """
    
    
    model.P_PriceProduct = pyo.Param(model.S_Products, initialize = _df_data_to_dictionary(df_products, 'products', 'price')) 
    model.P_MinOctaneProduct = pyo.Param(model.S_Products, initialize = _df_data_to_dictionary(df_products, 'products', 'min_octane'))    
    model.P_MaxBenzeneProduct = pyo.Param(model.S_Products, initialize = _df_data_to_dictionary(df_products, 'products', 'max_benzene'))    
    model.P_MaxRVPProduct = pyo.Param(model.S_Products, initialize = _df_data_to_dictionary(df_products, 'products', 'RVPmax'))    
    model.P_MinRVPProduct = pyo.Param(model.S_Products, initialize = _df_data_to_dictionary(df_products, 'products', 'RVPmin'))    
    
    model.P_CostStream = pyo.Param(model.S_Streams, initialize = _df_data_to_dictionary(df_streams, 'stream', 'cost'))    
    model.P_AvailStream = pyo.Param(model.S_Streams, initialize = _df_data_to_dictionary(df_streams, 'stream', 'avail'))    
    model.P_RONStream = pyo.Param(model.S_Streams, initialize = _df_data_to_dictionary(df_streams, 'stream', 'RON'))    
    model.P_MONStream = pyo.Param(model.S_Streams, initialize = _df_data_to_dictionary(df_streams, 'stream', 'MON'))    
    model.P_RVPStream = pyo.Param(model.S_Streams, initialize = _df_data_to_dictionary(df_streams, 'stream', 'RVP'))    
    model.P_BenzeneStream = pyo.Param(model.S_Streams, initialize = _df_data_to_dictionary(df_streams, 'stream', 'benzene'))    
    model.P_OctaneStream = pyo.Param(model.S_Streams, initialize = _df_data_to_dictionary(df_streams, 'stream', 'octane'))    