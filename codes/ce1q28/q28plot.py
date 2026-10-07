import numpy as np
import matplotlib.pyplot as plt
from coordgeo import line_gen

# matrix solve for intersection point
A = np.array([[1, 1], 
              [3, 1]])
b = np.array([7, 13])
P = np.linalg.solve(A, b)

# line 1: x + y = 7 (using boundary points)
A1 = np.array([[0], [7]])
B1 = np.array([[6], [1]])
x_l1 = line_gen(A1, B1)

# line 2: 3x + y = 13 (using boundary points)
A2 = np.array([[1], [10]])
B2 = np.array([[4.5], [-0.5]])
x_l2 = line_gen(A2, B2)

# plot
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x_l1[0, :], x_l1[1, :], label=r'$x + y = 7$', color='blue')
ax.plot(x_l2[0, :], x_l2[1, :], label=r'$3x + y = 13$', color='green')
ax.plot(P[0], P[1], 'ro', label=f'Intersection ({int(P[0])}, {int(P[1])})')

ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Verification of Line Intersection')
ax.legend()
ax.set_xlim(0, 6)
ax.set_ylim(0, 10)

plt.savefig('figs/q28.pdf', bbox_inches='tight')
plt.close(fig)
