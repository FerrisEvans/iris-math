import numpy as np
from sympy import lambdify, sqrt
from sympy.abc import x, y
import numpy as np
from matplotlib import pyplot as plt


def plot_fcn(A, B, dist_AX_zz, dist_BX_zz, distance):
    fig, ax = plt.subplots()

    plt.plot(A[0], A[1], color='k',
             marker='x', markersize=12)

    colorbar = ax.contour(xx, yy, dist_AX_zz,
                          levels=np.arange(0, 15 + 1),
                          cmap='RdYlBu_r')

    plt.plot(B[0], B[1], color='k',
             marker='x', markersize=12)

    colorbar = ax.contour(xx, yy, dist_BX_zz,
                          levels=np.arange(0, 15 + 1),
                          cmap='RdYlBu_r')

    ax.contour(xx, yy, distance,
               levels=0,
               colors='k')

    fig.colorbar(colorbar, ax=ax)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(y=0, color='k', linestyle='-')
    plt.axvline(x=0, color='k', linestyle='-')
    plt.xticks(np.arange(-10, 10, step=2))
    plt.yticks(np.arange(-10, 10, step=2))
    plt.axis('scaled')

    ax.set_xlim(x_array.min(), x_array.max())
    ax.set_ylim(y_array.min(), y_array.max())
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    ax.grid(linestyle='--', linewidth=0.25, color=[0.8, 0.8, 0.8])


A = [4, 2]
B = [0, -2]

num = 301;
# number of mesh grids
x_array = np.linspace(-8, 8, num)
y_array = np.linspace(-8, 8, num)

xx, yy = np.meshgrid(x_array, y_array)

dist_AX = sqrt((x - A[0]) ** 2 + (y - A[1]) ** 2)
dist_BX = sqrt((x - B[0]) ** 2 + (y - B[1]) ** 2)

dist_AX_fcn = lambdify([x, y], dist_AX)
dist_BX_fcn = lambdify([x, y], dist_BX)

dist_AX_zz = dist_AX_fcn(xx, yy)
dist_BX_zz = dist_BX_fcn(xx, yy)

# AX - BX = 0
distance = dist_AX_zz - dist_BX_zz
plot_fcn(A, B, dist_AX_zz, dist_BX_zz, distance)

# AX - BX - 3 = 0
distance = dist_AX_zz - dist_BX_zz - 3
plot_fcn(A, B, dist_AX_zz, dist_BX_zz, distance)

# AX - BX + 3 = 0
distance = dist_AX_zz - dist_BX_zz + 3
plot_fcn(A, B, dist_AX_zz, dist_BX_zz, distance)

# AX - 2*BX = 0
distance = dist_AX_zz - 2 * dist_BX_zz
plot_fcn(A, B, dist_AX_zz, dist_BX_zz, distance)

# BX + AX - 8 = 0
distance = dist_BX_zz + dist_AX_zz - 8
plot_fcn(A, B, dist_AX_zz, dist_BX_zz, distance)
