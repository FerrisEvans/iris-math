from sympy import *
from sympy.plotting import plot_parametric
import math

t = symbols('t')

# parametric equation of unit circle
x1 = cos(t)
x2 = sin(t)

# plot the circle
plot_parametric(x1, x2, (t, 0, 2 * pi), size=(10, 10))
