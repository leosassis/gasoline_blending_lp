import pyomo.environ as pyo


def create_vars(model: pyo.ConcreteModel) -> None:
    """ 
    Creates all necessary variables for the optimization problem.     
    
    Args:
        - model (pyo.ConcreteModel): a Pyomo model.
    """
    
    
    # Continuous: defiines the quantity of stream s in product p.
    model.V_QuantityStreamInProduct = pyo.Var(model.S_Streams, model.S_Products, domain = pyo.NonNegativeReals)