#import shutil
#import os.path
#import sys
import pyomo.environ as pyo
#from pyomo.contrib.appsi.solvers import Highs
from model import create_model



if __name__=="__main__":

    model = pyo.ConcreteModel()
    create_model(model)
    solver = pyo.SolverFactory('appsi_highs')
    solver.solve(model)

    

