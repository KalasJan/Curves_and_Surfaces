# plot the Pluckne's conoid
# z = 2xy / (x2 + y2) 

import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y) #volne promenne

JM = X**2 + Y**2
JM[JM == 0] = 1e-10 # treatment for division by zero in (0,0)
Z = (2*X*Y) / JM

# Graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Surface
ax.plot_surface(X, Y, Z, cmap='hot')

# Title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r"Graph of Pluckner's conoid: $z = \frac{2xy}{x^2 + y^2}$")

plt.show()
