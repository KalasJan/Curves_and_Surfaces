# Plot the Borromean surface (Borromean rings as a continuous tube surface)
# Requires parametric definition for surface modeling

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# geometry parameters
R_bor = 5 # radius of the ring
r_min = 1 # radius of tube

# axes parametres
u = np.linspace(0, 2 * np.pi, 150) # ring
v = np.linspace(0, 2 * np.pi, 60) # tube
U, V = np.meshgrid(u, v)

# basic equation
X = (R_bor + r_min * np.cos(V)) * np.cos(3*U)
Y = (R_bor + r_min * np.cos(V + 2*np.pi/3)) * np.sin(3*U)
# Z axis = Entanglement 
Z = r_min * np.sin(V + 4*np.pi/3) * np.cos(3*U)

def note_in_cz():
    """
    Protože jedna smyčka nestačí, musíme pro vizuální efekt
    obvykle generovat tři sady propletených trubic.
    Zde pro jednoduchost vizualizace použijeme jeden
    "kontinuální povrch", který tuto strukturu naznačuje.
    """
    pass

# graph
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# surface
ax.plot_surface(X, Y, Z, rstride=2, cstride=1, cmap=cm.winter,
                linewidth=0.2, antialiased=True, alpha=0.95)

# titles

ax.set_title(r"Borromean surface (propletené tubusy)", fontsize=16)
ax.set_box_aspect([1, 1, 0.6])
ax.grid(False)
ax.set_axis_off()

plt.show()