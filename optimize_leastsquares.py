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

# Code for minimization of least squares
from scipy.optimize import least_squares

# y are the dependent vars
y = np.array([1.957e-1, 1.947e-1, 1.735e-1, 1.6e-1, 8.44e-2, 6.27e-2])
# u are the explanatory vars
u = np.array([4.0, 2.0, 1.0, 5.0e-1, 2.5e-1, 1.67e-1, 1.25e-1, 1.0e-1])
# x is unknown vector of parameters
x0 = np.array([2.5, 3.9, 4.15, 3.9])

# The DGP with params x and vars u
def model(x, u):
    return x[0] * (u ** 2 + x[1] * u) / (u ** 2 + x[2] * u + x[3])

# Define the residuals
def fun(x, u, y):
    return model(x, u) - y

# Define closed form Jacobians from own computation
def jac(x, u, y):
    J = np.empty((u.size, x.size))
    den = u ** 2 + x[2] * u + x[3]
    num = u ** 2 + x[1] * u
    J[:, 0] = num / den
    J[:, 1] = x[0] * u / den
    J[:, 2] = -x[0] * num * u / den ** 2
    J[:, 3] = -x[0] * num / den ** 2
    return J

# Least squares estimation
res = least_squares(fun, x0, jac=jac, bounds=(0, 100), args=(u, y), verbose=1)
# Display parameter estimates    
res.x

# Plots the original data vs. the fitted model function
import matplotlib.pyplot as plt
u_test = np.linspace(0, 5)
y_test = model(res.x, u_test)
plt.plot(u, y, 'o', markersize=4, label='data')
plt.plot(u_test, y_test, label='fitted model')
plt.xlabel("u")
plt.ylabel("y")
plt.legend(loc='lower right')
plt.show()
