import pyomo.environ as pyo


def _octane_lb_in_product(model: pyo.ConcreteModel, p: pyo.Any) -> pyo.Constraint:
    """ 
    Lower bound constraint on octane.    
    """

    return sum(model.V_QuantityStreamInProduct[s,p]*(model.P_OctaneStream[s] - model.P_MinOctaneProduct[p]) for s in model.S_Streams) >= 0 


def _benzene_ub_in_product(model: pyo.ConcreteModel, p: pyo.Any) -> pyo.Constraint:
    """ 
    Upper bound constraint on benzene.    
    """

    return sum(model.V_QuantityStreamInProduct[s,p]*(model.P_BenzeneStream[s] - model.P_MaxBenzeneProduct[p]) for s in model.S_Streams) <= 0


def _rvp_lb_in_product(model: pyo.ConcreteModel, p: pyo.Any) -> pyo.Constraint:
    """ 
    Lower bound constraint on rvp.    
    """

    return sum(model.V_QuantityStreamInProduct[s,p]*(model.P_RVPStream[s]**1.25 - model.P_MinRVPProduct[p]**1.25) for s in model.S_Streams) >= 0


def _rvp_ub_in_product(model: pyo.ConcreteModel, p: pyo.Any) -> pyo.Constraint:
    """ 
    Upper bound constraint on rvp.    
    """

    return sum(model.V_QuantityStreamInProduct[s,p]*(model.P_RVPStream[s]**1.25 - model.P_MaxRVPProduct[p]**1.25) for s in model.S_Streams) <= 0


def _stream_availability(model, s: pyo.Any):
    """ 
    Upper bound constraint on stream availability.    
    """

    return sum(model.V_QuantityStreamInProduct[s,p] for p in model.S_Products) <= model.P_AvailStream[s]


def _create_constraints(model: pyo.ConcreteModel) -> None:
    """ 
    Creates all necessary constraints for the optimization problem.     
    
    Args:
        - model (pyo.ConcreteModel): a Pyomo model.
    """

    model.C_StreamAvailability = pyo.Constraint(model.S_Streams, rule = _stream_availability)
    model.C_Octane_LB_Limit_In_Product = pyo.Constraint(model.S_Products, rule = _octane_lb_in_product)
    model.C_Benzene_UB_Limit_In_Product = pyo.Constraint(model.S_Products, rule = _benzene_ub_in_product)
    model.C_RVP_LB_Limit_In_Product = pyo.Constraint(model.S_Products, rule = _rvp_lb_in_product)
    model.C_RVP_UB_Limit_In_Product = pyo.Constraint(model.S_Products, rule = _rvp_ub_in_product)

