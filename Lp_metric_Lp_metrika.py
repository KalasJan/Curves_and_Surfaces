# Plot unit balls in Metric space (L^p norms)
# abs(x)**n + abs(y)**n = 1 f0r different n

# r = 1 / (cos(t)**n + sin(t)**n) **(1/n)

import numpy as np
import matplotlib.pyplot as plt

# parameter
t = np.linspace(0, 2 * np.pi, 1000)

# exponent
ex = [-5, -2, -1, -1/2, 1/2, 1, 2, 10, 20]

# all in 1 result
fig, axes = plt.subplots(3, 3, figsize=(14, 9))
axes = axes.flatten() # 1D plot (iteration)

for i, n in enumerate(ex):
    ax = axes[i]
    
    with np.errstate(divide='ignore', invalid='ignore'):
        r = 1.0 / (np.abs(np.cos(t))**n + np.abs(np.sin(t))**n)**(1/n)    
        r = np.nan_to_num(r, nan=0.0, posinf=np.nan, neginf=np.nan) # if NaN values, inf * 0
    # cartesian
    x = r * np.cos(t)
    y = r * np.sin(t)
    
    # curves
    ax.plot(x, y, color='#1f77b4', linewidth=2.5)
    
    # axes
    ax.axhline(0, color='gray', linewidth=0.6, linestyle='--')
    ax.axvline(0, color='gray', linewidth=0.6, linestyle='--')
    ax.set_aspect('equal', adjustable='box')
    
    if n < 0:
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
    else:
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
    
    # subtitles
    label_n = f"n = {n}" if n != 20 else "n = \u221e (Max metric)"
    ax.set_title(f"${label_n}$", fontsize=11)
    ax.grid(True, alpha=0.3)

# total titles
plt.suptitle(r"Unit balls in ${L^p}$ metric spaces, $x^n + y^n = 1$", fontsize=16, y=0.98)
plt.tight_layout()
plt.show()