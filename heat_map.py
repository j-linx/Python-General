# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 01:02:27 2016

@author: linjen
"""

import os
os.chdir(r"C:\Users\linjen\Dropbox\Data Science\Datasets")

import numpy as np
from scipy.optimize import root
from numpy import mgrid, zeros

# parameters
nx, ny = 75, 75
# solve
guess = zeros((nx, ny), float)
sol = root(residual, guess, method='krylov', options={'disp': True})
# residual is the residual from the original root-finding (or whatever) problem

import matplotlib.pyplot as plt
x, y = mgrid[0:1:(nx*1j), 0:1:(ny*1j)]
plt.pcolor(x, y, sol.x)
plt.colorbar()
plt.show()