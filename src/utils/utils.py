import pyomo.environ as pyo


def print_set(model: pyo.ConcreteModel, set: pyo.Set) -> None:
    """ 
    Prints the data of a set.     
    
    Args:
        - model (pyo.ConcreteModel): a Pyomo model.
        - set (pyo.Set): a Pyomo set. 
    """
    
    
    print(set.data())