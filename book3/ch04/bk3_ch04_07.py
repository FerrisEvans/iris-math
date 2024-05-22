from sympy.solvers import solve
from sympy import Symbol

x = Symbol('x')
roots = solve(-x ** 3 + x, x)

# use numpy to solve
import numpy as np

coeff = [-1, 0, 1, 0]
roots_V2 = np.roots(coeff)
