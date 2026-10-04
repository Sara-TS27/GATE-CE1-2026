import numpy as np
import matplotlib.pyplot as plt

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 9))

# --- Define Numerical Values for Plotting Geometry ---
r = 1.0
alpha_deg = 130
beta_deg = 50

alpha = np.radians(alpha_deg)  # Angle for R
beta = np.radians(beta_deg)    # Angle for S

O = np.array([0.0, 0.0])
P = np.array([-r, 0.0])
Q = np.array([r, 0.0])
R = np.array([r * np.cos(alpha), r * np.sin(alpha)])
S = np.array([r * np.cos(beta), r * np.sin(beta)])
T = np.array([0.0, 2.1445])

# --- Plot Circle ---
theta = np.linspace(0, 2 * np.pi, 300)
ax.plot(r * np.cos(theta), r * np.sin(theta), color='blue', linewidth=2)

# --- Plot Secant Lines ---
# P -> R -> T (Red)
ax.plot([P[0], R[0]], [P[1], R[1]], color='red', linestyle='-', linewidth=1.5)
ax.plot([R[0], T[0]], [R[1], T[1]], color='red', linestyle='--', linewidth=1.5)

# Q -> S -> T (Green)
ax.plot([Q[0], S[0]], [Q[1], S[1]], color='green', linestyle='-', linewidth=1.5)
ax.plot([S[0], T[0]], [S[1], T[1]], color='green', linestyle='--', linewidth=1.5)

# Radial lines O-R and O-S (Dotted black)
ax.plot([O[0], R[0]], [O[1], R[1]], color='black', linestyle=':', linewidth=1.2)
ax.plot([O[0], S[0]], [O[1], S[1]], color='black', linestyle=':', linewidth=1.2)

# --- Coordinate Axes ---
ax.axhline(0, color='black', linewidth=1.2)
ax.axvline(0, color='black', linewidth=1.2)

# --- Plot Points ---
points = [O, P, Q, R, S, T]
for pt in points:
    ax.plot(pt[0], pt[1], 'ko', markersize=6)

# --- Annotate Points in Exponential (e^(i*theta)) Form ---
annotations = {
    r'$O(0)$': (O, (0.05, 0.05)),
    r'$P(-r = r e^{i\pi})$': (P, (-0.65, 0.05)),
    r'$Q(r = r e^{i 0})$': (Q, (0.05, 0.05)),
    r'$R(r e^{i\alpha})$': (R, (-0.55, 0.05)),
    r'$S(r e^{i\beta})$': (S, (0.05, 0.05)),
    r'$T$': (T, (0.05, 0.03))
}

for label, (pt, offset) in annotations.items():
    ax.text(pt[0] + offset[0], pt[1] + offset[1], label, fontsize=11, fontweight='bold')

# --- Plot Styling ---
ax.set_title(r'Circle Geometry in Exponential Form ($e^{i\theta}$)', fontsize=12, fontweight='bold', pad=12)
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.2, 2.3)
ax.set_xticks([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5])
ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0])
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

# Save figure directly as a vector PDF
plt.savefig('q07plot.pdf', bbox_inches='tight')
plt.close(fig)
