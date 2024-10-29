import pandas as pd
import pyomo.environ as pyo
from utils import print_set

df_products = pd.read_excel('data/data.xlsx', 'Products')
df_streams = pd.read_excel('data/data.xlsx', 'Streams')

def create_sets(model: pyo.ConcreteModel, df_products: pd, df_streams: pd) -> None:
    
    model.S_Streams = pyo.Set(initialize = list(df_streams['stream']))
    model.S_Products = pyo.Set(initialize = list(df_products['products']))
    print_set(model, model.S_Streams)
    print_set(model, model.S_Products)