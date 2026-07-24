#scipy.optimize:Optimization
# scipy optimize is a module provide the numerical optimization algorithem for minimizing or maximizing
# functions, solving equations, curve fitting, and handling constrained optimization problem
# The "best" solution could be:Lowest cost, Highest profit, Shortest distance, Minimum error
# Maximum efficiency, Best machine learning model parameters

# Function In scipy.optimize
# 1) minimize() : Find The Minimum value of a function
# syntax: scipy.optimize.minimize(fun, x0) fun=sunction to minimize, initial guess(starting point)

from scipy.optimize import minimize

def f(x):
    return x**2 + 5
result = minimize(f, 10)
print(result.x)


#scipy.stats	Statistics
#scipy.interpolate	Interpolation
#scipy.linalg	Linear Algebra
#scipy.integrate	Integration
#scipy.fft	Fast Fourier Transform
#scipy.signal	Signal Processing
#scipy.spatial	Spatial algorithms
#scipy.sparse	Sparse matrices
#scipy.ndimage	Image Processing
