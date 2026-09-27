# Plot the (Steiner) Roman surface

# u, v in (0, pi)
# x(u,v) = 1/2 * sin^2(u) * sin(2v)
# y(u,v) = 1/2 * sin^2(v) * sin(2u)
# z(u,v) = 1/2 * sin(2u) * cos(v)

# def2:
# u, v in (0, pi)
# x(u,v) = r^2 * cos(u) * cos(v) * sin(v)
# y(u,v) = r^2 * sin(u) * cos(v) * sin(v)
# z(u,v) = r^2 * cos(u) * sin(u) * cos^2(v)

import matplotlib.pyplot as plt
import numpy as np

# parametres
u = np.linspace(0, np.pi, 100)
v = np.linspace(0, np.pi, 100)
U, V = np.meshgrid(u, v)
r = 1

# definition of graph(s)
fig = plt.figure(figsize=(14, 7))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# def 1 
X1 = 1/2 * (np.sin(U)**2) * np.sin(2*V)
Y1 = 1/2 * (np.sin(V)**2) * np.sin(2*U)
Z1 = 1/2 * np.sin(2*U) * np.cos(V)

# graph 1
surf1 = ax1.plot_surface(X1, Y1, Z1, cmap="plasma", edgecolor="none")
ax1.set_title(
    r'$x = \frac{1}{2}\cdot\sin^2(u)\cdot\sin(2v)$' + '\n' +
    r'$y = \frac{1}{2}\cdot\sin^2(v)\cdot\sin(2u)$' + '\n' +
    r'$z = \frac{1}{2}\cdot\sin(2u)\cdot\cos(v)$',
    fontsize=12)

ax1.set_axis_off()


# def 2
X2 = (r**2) * np.cos(U) * np.cos(V) * np.sin(V)
Y2 = (r**2) * np.sin(U) * np.cos(V) * np.sin(V)
Z2 = (r**2) * np.cos(U) * np.sin(U) * (np.cos(V) ** 2)

# graph 2
surf2 = ax2.plot_surface(X2, Y2, Z2, cmap="plasma", edgecolor="none")
ax2.set_title(
    r'$x = r^2\cdot\cos(u)\cdot\cos(v)\cdot\sin(v)$' + '\n' +
    r'$y = r^2\cdot\sin(u)\cdot\cos(v)\cdot\sin(v)$' + '\n' +
    fr'$z = r^2\cdot\cos(u)\cdot\sin(u)\cdot\cos^2(v), r = {r}$',
    fontsize=12)

ax2.set_axis_off()

# big title and design
plt.suptitle(r'(Steiner) Roman surface', fontsize=15, weight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.90])
plt.show()
