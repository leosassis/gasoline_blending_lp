import pyomo.environ as pyo

def octane_lb_in_product(model: pyo.ConcreteModel, p: pyo.Set) -> pyo.Constraint:
    return sum(model.V_QuantityStreamInProduct[s,p]*(model.P_OctaneStream[s] - model.P_MinOctaneProduct[p]) for s in model.S_Streams) >= 0 

def benzene_ub_in_product(model: pyo.ConcreteModel, p: pyo.Set) -> pyo.Constraint:
    return sum(model.V_QuantityStreamInProduct[s,p]*(model.P_BenzeneStream[s] - model.P_MaxBenzeneProduct[p]) for s in model.S_Streams) <= 0

def rvp_lb_in_product(model: pyo.ConcreteModel, p: pyo.Set) -> pyo.Constraint:
    return sum(model.V_QuantityStreamInProduct[s,p]*(model.P_RVPStream[s] - model.P_MinRVPProduct[p]) for s in model.S_Streams) >= 0

def rvp_ub_in_product(model: pyo.ConcreteModel, p: pyo.Set) -> pyo.Constraint:
    return sum(model.V_QuantityStreamInProduct[s,p]*(model.P_RVPStream[s] - model.P_MaxRVPProduct[p]) for s in model.S_Streams) <= 0

def create_constraints(model: pyo.ConcreteModel) -> None:
    model.C_Octane_LB_Limit_In_Product = pyo.Constraint(model.S_Products, rule = octane_lb_in_product)
    model.C_Benzene_UB_Limit_In_Product = pyo.Constraint(model.S_Products, rule = benzene_ub_in_product)
    model.C_RVP_LB_Limit_In_Product = pyo.Constraint(model.S_Products, rule = rvp_lb_in_product)
    model.C_RVP_UB_Limit_In_Product = pyo.Constraint(model.S_Products, rule = rvp_ub_in_product)

