# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 00:24:56 2016

@author: linjen
"""

import os
os.chdir(r"C:\Users\linjen\Dropbox\Data Science\Datasets")

import pandas as pd
import numpy as np
import scipy.optimize as optimize
from math import *

# Code for minimization of function f wrt 3 vars packed into the c[] array
def f(c):
    return sqrt(c[0]**2 + c[1]**2 + c[2]**2)

result = optimize.minimize(f, [1,1,1])
print(result)


# Maximizing the function 'func' subject to an equality and an inequality constraint
# f(x,y)=2xy+2x−x**2−2y**2
 
def func(x, sign=1.0):
    """ Objective function """
    return sign*(2*x[0]*x[1] + 2*x[0] - x[0]**2 - 2*x[1]**2)

def func_deriv(x, sign=1.0):
    """ Derivative of objective function """
    dfdx0 = sign*(-2*x[0] + 2*x[1] + 2)
    dfdx1 = sign*(2*x[0] - 4*x[1])
    return np.array([ dfdx0, dfdx1 ])
    
# Note: since minimize only minimizes functions, the sign=1.0 param is introduced 
# to multiply the objective function by -1 in order to perform a maximization

# Constraints defined as a sequence of dictionaries, with keys type, fun and jac
# Constraints are, respectively: x**3−y=0 and y−1≥0
# jac is the Jacobian derivative of each constraint wrt x and y
 
cons = ({'type': 'eq',
         'fun' : lambda x: np.array([x[0]**3 - x[1]]),
         'jac' : lambda x: np.array([3.0*(x[0]**2.0), -1.0])},
        {'type': 'ineq',
         'fun' : lambda x: np.array([x[1] - 1]),
         'jac' : lambda x: np.array([0.0, 1.0])})

# Perform unconstrained optimization
res = minimize(func, [-1.0,1.0], args=(-1.0,), jac=func_deriv,
               method='SLSQP', options={'disp': True})
print(res.x)

# Perform constrained optimization
res = minimize(func, [-1.0,1.0], args=(-1.0,), jac=func_deriv,
               constraints=cons, method='SLSQP', options={'disp': True})
print(res.x)
     