# Plot the Supertoroid

import numpy as np 
import matplotlib.pyplot as plt

# parametres
n = 10 # n >2, even
t = 3 # natural number

u = np.linspace(0, 2*np.pi, 500)
v = np.linspace(0, 2*np.pi, 500)
U, V = np.meshgrid(u, v)

R = (np.abs(np.cos(V)) ** n + np.abs(np.sin(V)) ** n) ** (-1 / n) # radius

# equation
X = (4 + R * np.cos(t * U + V)) * np.cos(U)
Y = (4 + R * np.cos(t * U + V)) * np.sin(U)
Z = R * np.sin(t * U + V)

# Graph
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(projection="3d")

# plot surface
surf = ax.plot_surface(X, Y, Z, cmap="plasma", edgecolor="black", linewidth=0.3, alpha=0.9)

# titles, labels
ax.set_title('Supertoroid', fontsize=14)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
ax.axis('equal')
ax.set_axis_off()

plt.tight_layout()
plt.show()