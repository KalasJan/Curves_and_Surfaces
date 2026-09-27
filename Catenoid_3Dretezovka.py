# Plot the Catenoid
# minimal plane
# 3D object, rotation of Catenary (Retezovky)
# u in (0, 2*pi) ; v in (-2, 2)
# x(u,v) = cos(u) * cosh(v)
# y(u,v) = sin(u) * cosh(v)
# z(u,v) = v

import numpy as np
import matplotlib.pyplot as plt

# paramtres
u = np.linspace(0, 2 * np.pi, 150)
v = np.linspace(-2, 2, 150)
U, V = np.meshgrid(u, v)

# equations
X = np.cosh(V) * np.cos(U)
Y = np.cosh(V) * np.sin(U)
Z = V

# 3D Graph
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

surf = ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none", antialiased=True)

# design
ax.set_title("Catenoid (Minimal surface)", fontsize=14, pad=20)
ax.set_axis_off()  # Skrytí os
fig.colorbar(surf, shrink=0.5, aspect=10, label="Height (Z)")

plt.show()