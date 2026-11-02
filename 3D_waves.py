# Plot the 3D waves

import numpy as np
import matplotlib.pyplot as plt

# introuce
t = np.linspace(0, 2*np.pi, 1000)
t2 = np.linspace(0, np.pi, 1000)

fig, axes = plt.subplots(2, 4, subplot_kw={"projection": "3d"}, figsize=(18, 9))
axes = axes.flatten()

for ax in axes:
    ax.set_axis_off()

x = np.linspace(-3, 3, 30)
y = np.linspace(-3, 3, 30)
z = np.linspace(-3, 3, 30)

# 1) Gyroid orb
# g = sin(x) * cos(y) + sin(y) * cos(z) + sin(z) * cos(x) ; abs(g) =< 0.18

X1, Y1, Z1 = np.meshgrid(x, y, z, indexing = 'ij')
g = np.sin(X1) * np.cos(Y1) + np.sin(Y1) * np.cos(Z1) + np.sin(Z1) * np.cos(X1)

axes[0].voxels(np.abs(g) <= 0.18, facecolors="teal", edgecolor="none")
axes[0].set_title("1) Gyroid orb", fontsize=11, fontweight="bold")

# ===

# 2) toroidal coil
# x = (2 + 0.65 * cos(24t))*cos(t)
# y = (2+ 0.65*cos(24t))*sin(t)
# z = 0.65 * sin(24t)

X2 = (2 + 0.65 * np.cos(24 * t)) * np.cos(t)
Y2 = (2 + 0.65 * np.cos(24 * t)) * np.sin(t)
Z2 = 0.65 * np.sin(24 * t)

axes[1].plot(X2, Y2, Z2, color="purple", lw=1)
axes[1].set_title("2) Toroidal coil", fontsize=11, fontweight="bold")

# ===

# 3) Woven torus
# x = (2 + 0.8 * cos(13t))*cos(5t)
# y = (2+ 08*cos(13t))*sin(5t)
# z = 0.8 * sin(13t)

X3 = (2 + 0.8 * np.cos(13 * t)) * np.cos(5 * t)
Y3 = (2 + 0.8 * np.cos(13 * t)) * np.sin(5 * t)
Z3 = 0.8 * np.sin(13 * t)

axes[2].plot(X3, Y3, Z3, color="crimson", lw=0.8)
axes[2].set_title("3) Woven torus", fontsize=11, fontweight="bold")

# ===

# 4) Spherical weave
# x = sin(t) * cos(17t)
# y = sin(t) * sin(17t)
# z = cos(t)

X4 = np.sin(t2) * np.cos(17 * t2)
Y4 = np.sin(t2) * np.sin(17 * t2)
Z4 = np.cos(t2)

axes[3].plot(X4, Y4, Z4, color="royalblue", lw=1)
axes[3].set_title("4) Spherical weave", fontsize=11, fontweight="bold")

# ===

# 5) Harmonic bloom
# x = v*(1 + 0.28*cos(8u)) * cos(u)
# y = v*(1 + 0.28*cos(8u)) * sin(u)
# z = 0.35v^2 *sin(8u)

u5 = np.linspace(0, 2 * np.pi, 100)
v5 = np.linspace(0, 1, 100)
U5, V5 = np.meshgrid(u5, v5)

X5 = V5 * (1 + 0.28 * np.cos(8 * U5)) * np.cos(U5)
Y5 = V5 * (1 + 0.28 * np.cos(8 * U5)) * np.sin(U5)
Z5 = 0.35 * (V5**2) * np.sin(8 * U5)

axes[4].plot_surface(X5, Y5, Z5, cmap="plasma", edgecolor="none")
axes[4].set_title("5) Harmonic bloom", fontsize=11, fontweight="bold")

# ===

# 6) Mobius ribbon
# x = (2 + v*cos(t/2))*cos(t)
# y = (2 + v*cos(t/2))*sin(t)
# z = v * sin(t/2) for v in (-0.72, 0.72)

v6 = np.linspace(-0.72, 0.72, 50)
T6, V6 = np.meshgrid(t, v6)

X6 = (2 + V6 * np.cos(T6 / 2)) * np.cos(T6)
Y6 = (2 + V6 * np.cos(T6 / 2)) * np.sin(T6)
Z6 = V6 * np.sin(T6 / 2)

axes[5].plot_surface(X6, Y6, Z6, cmap="viridis", edgecolor="none")
axes[5].set_title("6) Mobius ribbon", fontsize=11, fontweight="bold")

# ===

# 7) Wave ring
# x = (2 + v*cos(8t)) * cos(t)
# y = (2 + v*cos(8t)) * sin(t)
# z = v * sin(8t) 

v7 = np.linspace(-0.3, 0.3, 50)
T7, V7 = np.meshgrid(t, v7)
X7 = (2 + V7 * np.cos(8 * T6)) * np.cos(T6)
Y7 = (2 + V7 * np.cos(8 * T6)) * np.sin(T6)
Z7 = V7 * np.sin(8 * T6)

axes[6].plot_surface(X7, Y7, Z7, cmap="coolwarm", edgecolor="none")
axes[6].set_title("7) Wave ring", fontsize=11, fontweight="bold")

# ===

# 8) Enneper bloom
# x = Re(w - w^9/9)
# y = Im(w + w^9/9)
# z = 2/5 * Re(w^5), for w = u+vi, abs(w) =< 1.18

u8 = np.linspace(-1.18, 1.18, 80)
v8 = np.linspace(-1.18, 1.18, 80)
U8, V8 = np.meshgrid(u8, v8)
W = U8 + 1j * V8
mask = np.abs(W) <= 1.18
W_f = np.where(mask, W, np.nan)

W_sub = W_f - (W_f**9) / 9
X8 = W_sub.real
W_add = W_f + (W_f**9) / 9
Y8 = W_add.imag
W_pow = 0.4 * (W_f**5)
Z8 = W_pow.real

axes[7].plot_surface(X8, Y8, Z8, cmap="magma", edgecolor="none")
axes[7].set_title("8) Enneper bloom", fontsize=11, fontweight="bold")

# ===

# final
plt.suptitle(
    "Gallery of 3D Waves & Complex Surfaces", fontsize=18, weight="bold", y=0.96
)
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()

