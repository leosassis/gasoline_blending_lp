import pyomo.environ as pyo

def create_vars(model: pyo.ConcreteModel) -> None:
    model.V_QuantityStreamInProduct = pyo.Var(model.S_Streams, model.S_Products, domain = pyo.NonNegativeReals)