import pyomo.environ as pyo

def maximize_profit(model: pyo.ConcreteModel) -> pyo.Objective:
    return sum(model.V_QuantityStreamInProduct[s,p] for s in model.S_Streams for p in model.S_Products)

def create_objective(model: pyo.ConcreteModel) -> None:
    model.Objective = pyo.Objective(expr = maximize_profit, sense = pyo.maximize)