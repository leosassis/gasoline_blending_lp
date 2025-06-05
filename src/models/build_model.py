import pyomo.environ as pyo

from src.data.preprocessing import extract_data
from src.models.sets import create_sets
from src.models.parameters import create_parameters
from src.models.variables import create_vars
from src.models.constraints import create_constraints
from src.models.objective import create_objective


def create_model(model: pyo.ConcreteModel) -> None:
    """
    Loads sets, variables, parameters, constraints and objective.
    
    Args:
        - model (ConcreteModel): a Pyomo model. 
    """
    
    df_products, df_streams = extract_data()
    create_sets(model, df_products, df_streams)
    create_parameters(model, df_products, df_streams)
    create_vars(model)
    create_constraints(model)
    create_objective(model)