import pyomo.environ as pyo
from flask import Flask, render_template
from src.models.build_model import create_model


app = Flask(__name__)

def run_optimization() -> None:
    """ 
    Builds, solves, and display the problem.
    
    Returns:
            variable_values: variable results of the optimization problem.
    """
    
    
    # Step 1: Create a model
    model = pyo.ConcreteModel()
    
    # Step 2: Buil the model
    create_model(model)
    
    # Step 3: Solve model
    results = pyo.SolverFactory('appsi_highs').solve(model)
    results.write()
    
    # Step 4: Display variable results
    model.V_QuantityStreamInProduct.display()  
    
    # Step 5:Extract values from the Pyomo variable
    variable_values = {index: round(pyo.value(var), 2) for index, var in model.V_QuantityStreamInProduct.items()}

    return variable_values


@app.route("/")
def show_result():
    """ 
    Flask route to solve the model and render results in an HTML template.
    """
    
    
    variable_values = run_optimization()    
    return render_template("result.html", variable_values=variable_values)
    

if __name__=="__main__":
    """ 
    Main entry point to run the Flask app.
    """
    
    
    app.run(debug=True)
    