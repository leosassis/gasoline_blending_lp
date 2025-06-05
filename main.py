import pyomo.environ as pyo
from src.models.build_model import create_model


def run_optimization() -> None:
    """ 
    Builds, solves, and display the problem.
    """
    
    
    # Step 1: Create a model
    model = pyo.ConcreteModel()
    
    # Step 2: Buil the model
    create_model(model)
    
    # Step 3: Solve model
    pyo.SolverFactory('appsi_highs').solve(model).write()
    
    # Step 4: Display variable results
    model.V_QuantityStreamInProduct.display()    

if __name__=="__main__":
    """ 
    Main function to run the optimization problem.
    """
    
    run_optimization()
    