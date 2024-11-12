import pyomo.environ as pyo

from input_data import extract_data
from sets import create_sets
from parameters import create_parameters
from variables import create_vars
from constraints import create_constraints
from objective import create_objective

df_products, df_streams = extract_data()

def create_model(model: pyo.ConcreteModel) -> None:
    create_sets(model, df_products, df_streams)
    create_parameters(model, df_products, df_streams)
    create_vars(model)
    create_constraints(model)
    create_objective(model)