import pandas as pd
import pyomo.environ as pyo
from src.utils.utils import print_set


def create_sets(model: pyo.ConcreteModel, df_products: pd, df_streams: pd) -> None:
    """ 
    Creates all necessary sets for the optimization problem.     
    
    Args:
        - model (pyo.ConcreteModel): a Pyomo model.
        - df_products (pd): a data frame with data related to products.
        - df_streams (pd): a data frame with data related to streams. 
    """
    
    
    model.S_Streams = pyo.Set(initialize = list(df_streams['stream']))
    model.S_Products = pyo.Set(initialize = list(df_products['products']))