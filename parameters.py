import pandas as pd
import pyomo.environ as pyo

def df_data_to_dictionary(df: pd, flow: str, attribute: str) -> dict:
    return df[[flow,attribute]].set_index(flow).to_dict()[attribute]

def create_parameters(model: pyo.ConcreteModel, df_products: pd, df_streams: pd) -> None:
    model.P_PriceProduct = pyo.Param(model.S_Products, initialize = df_data_to_dictionary(df_products, 'products', 'price')) 
    model.P_MinOctaneProduct = pyo.Param(model.S_Products, initialize = df_data_to_dictionary(df_products, 'products', 'octane'))    
    model.P_MaxBenzeneProduct = pyo.Param(model.S_Products, initialize = df_data_to_dictionary(df_products, 'products', 'max_benzene'))    
    model.P_MaxRVPProduct = pyo.Param(model.S_Products, initialize = df_data_to_dictionary(df_products, 'products', 'RVPmax'))    
    model.P_MinRVPProduct = pyo.Param(model.S_Products, initialize = df_data_to_dictionary(df_products, 'products', 'RVPmin'))    
    
    model.P_CostStream = pyo.Param(model.S_Streams, initialize = df_data_to_dictionary(df_streams, 'stream', 'cost'))    
    model.P_AvailStream = pyo.Param(model.S_Streams, initialize = df_data_to_dictionary(df_streams, 'stream', 'avail'))    
    model.P_RONStream = pyo.Param(model.S_Streams, initialize = df_data_to_dictionary(df_streams, 'stream', 'RON'))    
    model.P_MONStream = pyo.Param(model.S_Streams, initialize = df_data_to_dictionary(df_streams, 'stream', 'MON'))    
    model.P_RVPStream = pyo.Param(model.S_Streams, initialize = df_data_to_dictionary(df_streams, 'stream', 'RVP'))    
    model.P_BenzeneStream = pyo.Param(model.S_Streams, initialize = df_data_to_dictionary(df_streams, 'stream', 'benzene'))    
    model.P_OctaneStream = pyo.Param(model.S_Streams, initialize = df_data_to_dictionary(df_streams, 'stream', 'octane'))    