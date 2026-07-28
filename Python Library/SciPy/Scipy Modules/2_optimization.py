#scipy.optimize:Optimization
# scipy optimize is a module provide the numerical optimization algorithem for minimizing or maximizing
# functions, solving equations, curve fitting, and handling constrained optimization problem
# The "best" solution could be:Lowest cost, Highest profit, Shortest distance, Minimum error
# Maximum efficiency, Best machine learning model parameters

# Function In scipy.optimize
# 1) minimize() : Find The Minimum value of a function
# syntax: scipy.optimize.minimize(fun, x0) fun=sunction to minimize, initial guess(starting point)
'''
from scipy.optimize import minimize

def f(x):
    return x**2 + 5
result = minimize(f, 10)
print(result.x)
'''
# 2) root(): find the root of an equation
# A root is equal to value of x that makes the equation equal to '0'.

## Equation:
# x^2−9=0   #We need to find the value of x.
# Manual Solution: x^2=9
# Take the square root: x=3 or x=−3
# So the roots are:3 or -3
'''
from scipy.optimize import root
def equation(x):
    return x**2-9
result = root(equation,3)
print(result)
'''
# 3) curve_fit(): is used to fit the mathamatical curve (module) to a set of data points.
# In simple words, it finds the equation that best represents your data
# Syntax: curve_fit(function, xdata, ydata)
'''
import numpy as np
from scipy.optimize import curve_fit

def line(x, a, b):
    return a * x + b

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

params, covariance = curve_fit(line, x, y)

print(params)
'''
# 4) least_square(): find the best solution of a minimizing the sum of squared error (residuls)
# Syntax: least_square(function, x0)
'''
from scipy.optimize import least_squares

def residual(x):
    return x**2 - 4

result = least_squares(residual, 3)
print(result.x)
print(result)
'''
# 5) linprog(): Solver Linear PRogramming Problem
# syntax: linprog(c, A_ub, b_ub)
# c = Objective Function Coefficient, A_ub =  Constraints Coefficient, b_ub = Constrain Limits
# "linprog() solves optimization problems where both the objective function and the constraints
# are linear."
'''
from scipy.optimize import linprog

c = [-5, -3] # maximize 5x + 3y(scipy minimize so negate)

A = [[2, 1],
     [1, 2]]

b = [8, 8]

result =  linprog(c, A_ub=A, b_ub=b)
print(result.x)
print(result)
'''

# 6) minimize_scalar(): finds the minimum value of a function that has only one variable.
# Unlike minimize(), it is specifically designed for scalar (single-variable) functions.
# syntax: minimize_scaler(function)

from scipy.optimize import minimize_scalar

def f(x):
    return (x-4)**2

result = minimize_scalar(f)
print(result.x)

