# Plot, calculate volume and surface of a Donut (Torus)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 1) Analysis

R = 2 # big radius (center of object - center of tube)
r = 1 # small radius (tube)

vol = 2 * (np.pi ** 2) * R * (r ** 2)
sur = 4 * (np.pi ** 2) * R * r

print (rf'Objem Toru o poloměrech R = {R} a r = {r} je {vol:.2f} a povrch {sur:.2f}')

# =============================================

# 2) 3D graph

u = np.linspace(0, 2 * np.pi, 100) # around hole
v = np.linspace(0, 2 * np.pi, 100) # around tube
U, V = np.meshgrid(u, v)

# equation (parametric)
X = (R + r * np.cos(V)) * np.cos(U)
Y = (R + r * np.cos(V)) * np.sin(U)
Z = r * np.sin(V)

# plotting
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, rstride=3, cstride=3, cmap=cm.plasma,
                linewidth=0.1, antialiased=True, alpha=0.9)

ax.set_title("Donut (Torus)" + "\n" + 
             fr"$R = {R}, r = {r}$" + "\n" +
             fr"$V = {vol:.2f} u^3 ; A = {sur:.2f} u^2$", fontsize=14)
ax.set_box_aspect([1, 1, 0.6]) 
ax.grid(False)
ax.set_axis_off()

plt.show()
