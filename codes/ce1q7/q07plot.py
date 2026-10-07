import numpy as np
import matplotlib.pyplot as plt
from coordgeo import line_gen, circ_gen

# setup geometry
r = 1.0
alpha = np.radians(130)
beta = np.radians(50)

O = np.array([[0.0], [0.0]])
P = np.array([[-r], [0.0]])
Q = np.array([[r], [0.0]])
R = r * np.array([[np.cos(alpha)], [np.sin(alpha)]])
S = r * np.array([[np.cos(beta)], [np.sin(beta)]])
T = np.array([[0.0], [2.1445]])

# generate circle and lines using coordgeo
x_circ = circ_gen(O, r)
x_PR = line_gen(P, R)
x_RT = line_gen(R, T)
x_QS = line_gen(Q, S)
x_ST = line_gen(S, T)
x_OR = line_gen(O, R)
x_OS = line_gen(O, S)

# plot
fig, ax = plt.subplots(figsize=(8, 9))

ax.plot(x_circ[0, :], x_circ[1, :], color='blue', linewidth=2)

# secants
ax.plot(x_PR[0, :], x_PR[1, :], color='red', linestyle='-', linewidth=1.5)
ax.plot(x_RT[0, :], x_RT[1, :], color='red', linestyle='--', linewidth=1.5)
ax.plot(x_QS[0, :], x_QS[1, :], color='green', linestyle='-', linewidth=1.5)
ax.plot(x_ST[0, :], x_ST[1, :], color='green', linestyle='--', linewidth=1.5)

# radial lines
ax.plot(x_OR[0, :], x_OR[1, :], color='black', linestyle=':', linewidth=1.2)
ax.plot(x_OS[0, :], x_OS[1, :], color='black', linestyle=':', linewidth=1.2)

# axes
ax.axhline(0, color='black', linewidth=1.2)
ax.axvline(0, color='black', linewidth=1.2)

# plot points & labels
pts = [O, P, Q, R, S, T]
for pt in pts:
    ax.plot(pt[0, 0], pt[1, 0], 'ko', markersize=6)

annotations = {
    r'$O(0)$': (O, (0.05, 0.05)),
    r'$P(-r)$': (P, (-0.35, 0.05)),
    r'$Q(r)$': (Q, (0.05, 0.05)),
    r'$R(re^{i\alpha})$': (R, (-0.45, 0.05)),
    r'$S(re^{i\beta})$': (S, (0.05, 0.05)),
    r'$T$': (T, (0.05, 0.03))
}

for label, (pt, offset) in annotations.items():
    ax.text(pt[0, 0] + offset[0], pt[1, 0] + offset[1], label, fontsize=11, fontweight='bold')

ax.set_title(r'Circle Geometry ($\angle RTS = 50^\circ$)', fontsize=12, fontweight='bold')
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.2, 2.3)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)

plt.savefig('figs/q07.pdf', bbox_inches='tight')
plt.close(fig)
