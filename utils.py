import pyomo.environ as pyo

def print_set(model: pyo.ConcreteModel, set: pyo.Set) -> None:
    print(set.data())