import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.colors import ListedColormap
import random
import matplotlib.patches as patches

color_dict = {
    -1: 'gray',
    0: 'red',
    1: 'blue',
    2: 'green',
    3: 'yellow',
    4: 'orange',
    5: 'purple',
    6: 'brown',
    7: 'pink',
    8: 'navy',
    9: 'cyan'
}
colors = [color_dict[key] for key in sorted(color_dict.keys())]
cmap = ListedColormap(colors)

def plot_color_grid(grid, ax):
    grid_array = np.array(grid)

    n_rows, n_cols = grid_array.shape
    for i in range(n_rows):
        for j in range(n_cols):
            color = cmap(grid_array[i, j])
            rect = patches.Rectangle((j, i), 1, 1, linewidth=0.5, edgecolor='black', facecolor=color)
            ax.add_patch(rect)

    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows)
    ax.set_aspect('equal')
    ax.invert_yaxis()
    ax.set_xticks([])
    ax.set_yticks([])