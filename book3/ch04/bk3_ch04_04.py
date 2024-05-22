from sympy.abc import x, y, z

expr = x ** 3 + 2 * x ** 2 - x - 2

from sympy.utilities.lambdify import lambdify

f_x = lambdify(x, expr)

print(f_x(1))
