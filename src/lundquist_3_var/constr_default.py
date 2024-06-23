#! /usr/bin/python3

##--------------------------------------------------------------------\
#   bayesian_optimization_python
#    '.src/lundquist_3_var/constr_default.py'
#   Function for default constraints. Called if user does not pass in 
#       constraints for objective function or problem being optimized. 
#
#   Author(s): Jonathan Lundquist, Lauren Linkous
#   Last update: May 30, 2024
##--------------------------------------------------------------------\


import numpy as np

def constr_default(X):
    return True