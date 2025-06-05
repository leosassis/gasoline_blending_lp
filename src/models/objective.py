import pyomo.environ as pyo

def _maximize_profit(model: pyo.ConcreteModel) -> pyo.Objective:
    """ 
    Maximizes the quatity of stream s in product p.
    """
    
    
    return sum(model.V_QuantityStreamInProduct[s,p] for s in model.S_Streams for p in model.S_Products)


def create_objective(model: pyo.ConcreteModel) -> None:
    """ 
    Creates the objective for the optimization problem.     
    
    Args:
        - model (pyo.ConcreteModel): a Pyomo model.
    """
    
    
    model.Objective = pyo.Objective(expr = _maximize_profit, sense = pyo.maximize)