# Plot the Astroidal sphere
# abs(x)**2/3 + abs(y)**2/3 + abs(z)**2/3 = 1 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# parametres
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-np.pi / 2, np.pi / 2, 100)
U, V = np.meshgrid(u, v)

# equations
X = (np.cos(U) ** 3) * (np.cos(V) ** 3)
Y = (np.sin(U) ** 3) * (np.cos(V) ** 3)
Z = np.sin(V) ** 3

# graph
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap=cm.coolwarm,
                linewidth=0.1, antialiased=True, alpha=0.9)

# titles
ax.set_title(r"Astroidal surface: $|x|^{2/3} + |y|^{2/3} + |z|^{2/3} = 1$", fontsize=14)
ax.set_box_aspect([1, 1, 1])
ax.grid(False)
# ax.set_axis_off()

plt.show()