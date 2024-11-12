import pyomo.environ as pyo

def octane_lb_in_product(model: pyo.ConcreteModel, p) -> pyo.Constraint:
    return sum(model.V_QuantityStreamInProduct[s,p]*(model.P_OctaneStream[s] - model.P_MinOctaneProduct[p]) for s in model.S_Streams) >= 0 

def benzene_ub_in_product(model: pyo.ConcreteModel, p) -> pyo.Constraint:
    return sum(model.V_QuantityStreamInProduct[s,p]*(model.P_BenzeneStream[s] - model.P_MaxBenzeneProduct[p]) for s in model.S_Streams) <= 0

def rvp_lb_in_product(model: pyo.ConcreteModel, p) -> pyo.Constraint:
    return sum(model.V_QuantityStreamInProduct[s,p]*(model.P_RVPStream[s]**1.25 - model.P_MinRVPProduct[p]**1.25) for s in model.S_Streams) >= 0

def rvp_ub_in_product(model: pyo.ConcreteModel, p) -> pyo.Constraint:
    return sum(model.V_QuantityStreamInProduct[s,p]*(model.P_RVPStream[s]**1.25 - model.P_MaxRVPProduct[p]**1.25) for s in model.S_Streams) <= 0

def stream_availability(model, s):
    return sum(model.V_QuantityStreamInProduct[s,p] for p in model.S_Products) <= model.P_AvailStream[s]

def create_constraints(model: pyo.ConcreteModel) -> None:
    model.C_StreamAvailability = pyo.Constraint(model.S_Streams, rule = stream_availability)
    model.C_Octane_LB_Limit_In_Product = pyo.Constraint(model.S_Products, rule = octane_lb_in_product)
    model.C_Benzene_UB_Limit_In_Product = pyo.Constraint(model.S_Products, rule = benzene_ub_in_product)
    model.C_RVP_LB_Limit_In_Product = pyo.Constraint(model.S_Products, rule = rvp_lb_in_product)
    model.C_RVP_UB_Limit_In_Product = pyo.Constraint(model.S_Products, rule = rvp_ub_in_product)

