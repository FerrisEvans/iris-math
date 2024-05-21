import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

for num_vertices in [3, 4, 5, 6, 7, 8]:
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    hexagon_inner = RegularPolygon((0, 0), numVertices=num_vertices,
                                   radius=1, alpha=0.2, edgecolor='k')
    ax.add_patch(hexagon_inner)

    plt.axis('off')

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.show()
