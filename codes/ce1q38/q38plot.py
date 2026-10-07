import numpy as np
import matplotlib.pyplot as plt
from coordgeo import line_gen

# nodal coordinates (2D column vectors)
P = np.array([[0.0], [0.0]])
Q = np.array([[1.0], [1.0]])
R = np.array([[2.0], [0.0]])

# generate lines for truss members using coordgeo
x_PQ = line_gen(P, Q)
x_QR = line_gen(Q, R)

plt.figure(figsize=(6, 4))
plt.plot(x_PQ[0, :], x_PQ[1, :], 'b-', linewidth=2, label='Member PQ')
plt.plot(x_QR[0, :], x_QR[1, :], 'r-', linewidth=2, label='Member QR')

# plot nodes
pts = [P, Q, R]
for pt in pts:
    plt.plot(pt[0, 0], pt[1, 0], 'ko', markersize=6)

# Annotations & DOF arrows at node Q
plt.quiver(Q[0, 0], Q[1, 0], 0.3, 0, angles='xy', scale_units='xy', scale=1, color='green', label='u (Horizontal DOF)')
plt.quiver(Q[0, 0], Q[1, 0], 0, 0.3, angles='xy', scale_units='xy', scale=1, color='purple', label='v (Vertical DOF)')

plt.text(P[0, 0] - 0.1, P[1, 0] - 0.1, 'P (Hinge)', fontsize=11)
plt.text(Q[0, 0], Q[1, 0] + 0.15, 'Q', fontsize=11)
plt.text(R[0, 0] - 0.1, R[1, 0] - 0.1, 'R (Hinge)', fontsize=11)

plt.xlim(-0.5, 2.5)
plt.ylim(-0.5, 1.8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.title('Two-Member Truss with Degrees of Freedom (u, v) at Q')
plt.legend(loc='upper right')

plt.savefig('figs/q38.pdf')
plt.close()
