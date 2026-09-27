# Plot of Hopf Torus (Visualization of Hopf Fibration)
# S3 sphere in 4D dimension

import matplotlib.pyplot as plt
import numpy as np

# Parametres
u = np.linspace(0, 2 * np.pi, 120)
v = np.linspace(0, 2 * np.pi, 120)
U, V = np.meshgrid(u, v)

# equation (projection)
s = np.sqrt(2)
X = np.cos(U) * np.cos(V) / (s + np.sin(U))
Y = np.sin(U) * np.cos(V) / (s + np.sin(U))
Z = np.sin(V) / (s + np.sin(U))

# graph
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

surf = ax.plot_surface(X, Y, Z, cmap="coolwarm", edgecolor="none", antialiased=True)

ax.set_title("Hopf Fibration (Hopf Torus)", fontsize=14, pad=20)

ax.set_axis_off()
fig.colorbar(surf, shrink=0.5, aspect=10, label="Height (Z)")

plt.tight_layout()
plt.show()