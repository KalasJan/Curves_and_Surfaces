# Plot the Clebsch cubic surface
# Smooth cubic surface with 27 lines and icosahedral symmetry
# x**3 + y**3 + z**3 + w**3 + 1 =  if x+y+z+w+1 = 0 or:
def implicitni():
    """
    81 * (X**3 + Y**3 + Z**3) 
    - 189 * (X**2*(Y + Z) + Y**2*(X + Z) + Z**2*(X + Y)) 
    + 54 * (X*Y + X*Z + Y*Z)
    + 9 * (X + Y + Z) 
    - 1.0 = 0
    """
pass

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from skimage.measure import marching_cubes

# parametres
resolution = 100
lim = 1.5
x = np.linspace(-lim, lim, resolution)
y = np.linspace(-lim, lim, resolution)
z = np.linspace(-lim, lim, resolution)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# definition
V = 81 * (X**3 + Y**3 + Z**3) \
    - 189 * (X**2*(Y + Z) + Y**2*(X + Z) + Z**2*(X + Y)) \
    + 54 * (X*Y + X*Z + Y*Z) \
    + 9 * (X + Y + Z) \
    - 1.0

# isosurface (V = 0)
verts, faces, normals, values = marching_cubes(V, level=0.0)

# cartesian
verts = verts / (resolution - 1) * (2 * lim) - lim

# Graph
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# triangles
ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2],
                cmap=cm.inferno, linewidth=0.1, antialiased=True, alpha=0.95)

# title
ax.set_title(r"Clebsch Cubic Surface", fontsize=13)
ax.set_box_aspect([1, 1, 1])
ax.grid(False)
ax.set_axis_off()

plt.show()
