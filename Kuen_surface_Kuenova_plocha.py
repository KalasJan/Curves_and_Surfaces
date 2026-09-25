# Plot the Kuen surface

# curvature K = -1

import matplotlib.pyplot as plt
import numpy as np

def equations():
    """
    u in (0, pi), v in any interval
    jmen = 1 + u**2 * sin(v)**2
    x(u,v) = 2(cos(v) + v*sin(v))* sin(u) / jmen
    y(u,v) = 2(sin(v)-v cos(v))*sin(u) / jmen
    z(u,v) = ln(tan(u/2)) + (2cos(u))/jmen
    """
    pass

# parametres
u = np.linspace(0.05, np.pi - 0.05, 150)
v = np.linspace(-4.5, 4.5, 150)
U, V = np.meshgrid(u, v)

# equations
jmen = 1 + U**2 * np.sin(V)**2

X = 2*(np.cos(V) + V*np.sin(V))* np.sin(U) / jmen
Y = 2*(np.sin(V)-V*np.cos(V))*np.sin(U) / jmen
Z = np.log(np.tan(U/2)) + (2*np.cos(U))/jmen

# 3D graph
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# surface
surf = ax.plot_surface(X, Y, Z, cmap="plasma", edgecolor="none", antialiased=True)

# design
ax.set_title("Kuen surface (K = -1)", fontsize=14, pad=20)
ax.set_axis_off()
fig.colorbar(surf, shrink=0.5, aspect=10, label="Height (Z)")

plt.show()