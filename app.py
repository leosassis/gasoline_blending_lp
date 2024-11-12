import pyomo.environ as pyo
from model import create_model

if __name__=="__main__":

    model = pyo.ConcreteModel()
    create_model(model)
    pyo.SolverFactory('appsi_highs').solve(model).write()
    model.V_QuantityStreamInProduct.display()