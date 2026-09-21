# Plot the Cayley cubic surface (Implicit TPMS)
# TPMS - Triply Periodic Minimal Surface (trojperiodická minimální plocha)
# 4(x**3 + y**3 + z**3 + w**3) - (x+y+z+w)**3 = 0

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from skimage.measure import marching_cubes

# parametres
resolution = 60
lim = 2 * np.pi
x = np.linspace(-lim, lim, resolution)
y = np.linspace(-lim, lim, resolution)
z = np.linspace(-lim, lim, resolution)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# function
W = 1
V = 4*(X**3 + Y**3 + Z**3 + W**3) - (X+Y+Z+W)**3

# isosurface (V = 0), using Marching Cubes
verts, faces, normals, values = marching_cubes(V, level=0.0)

# back to cartesian
verts = verts / (resolution - 1) * (2 * lim) - lim

# 3D net
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# triangle surface
ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2],
                cmap=cm.inferno, linewidth=0.1, antialiased=True, alpha=0.95)

# format, title

ax.set_box_aspect([1, 1, 1])
ax.grid(False)
ax.set_axis_off()
