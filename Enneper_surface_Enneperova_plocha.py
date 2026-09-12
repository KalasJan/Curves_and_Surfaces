# plot the Enneper surface
# x(u,v) = u - u^3 / 3 + uv^2 // y(u,v) = v - v^3 / 3 + vu^2 // z(u,v) = u^2 - v^2

import numpy as np 
import matplotlib.pyplot as plt

# def the surface
def Enneper(u,v):
    ox = u - u**3 / 3 + u* v**2
    oy = v - v**3 / 3 + v* u**2
    oz = u**2 - v**2
    return ox, oy, oz

u_val = np.linspace(-2, 2, 100)
v_val = np.linspace(-2, 2, 100)
U, V = np.meshgrid(u_val, v_val)

# 3D dimension
X, Y, Z = Enneper(U, V)

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(projection='3d')

# gplot surface
surf = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none', alpha=0.9)

# titles, labels
ax.set_title('Enneperova plocha / Enneper surface', fontsize=14)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# colorbar of z
fig.colorbar(surf, shrink=0.5, aspect=5, label='Z')

plt.tight_layout()
plt.show()