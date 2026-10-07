import numpy as np
import matplotlib.pyplot as plt
from coordgeo import line_gen

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection='3d')

# Plane 1: x + y + z = 0 => z = -x - y
# Plane 2: x + 2z = 0    => z = -0.5 * x
x_range = np.linspace(-3, 3, 20)
y_range = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x_range, y_range)

Z1 = -X - Y
Z2 = -0.5 * X

ax.plot_surface(X, Y, Z1, alpha=0.5, color='cyan')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='orange')

# Intersection line using coordgeo line_gen between two end points.
A = np.array([[-3.0], [1.5], [1.5]])
B = np.array([[3.0], [-1.5], [-1.5]])
line_pts = line_gen(A, B)

ax.plot(line_pts[0, :], line_pts[1, :], line_pts[2, :], color='red', linewidth=3, label='Intersection Line')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Intersection of Two Planes')

plt.savefig('figs/q12.pdf')
plt.close()
