from sympy import *
from sympy.plotting import plot3d_parametric_line
import math

t = symbols('t')

# parametric equation of spiral
x1 = cos(t)
x2 = sin(t)
x3 = t

plot3d_parametric_line(x1, x2, x3, (t, 0, 8 * math.pi))
