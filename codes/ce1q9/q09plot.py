import numpy as np
import matplotlib.pyplot as plt
from coordgeo import circ_gen, line_gen

# 1. State computation (Steps 0 to 8)
steps = 9
N = 7
states = np.zeros((steps, N), dtype=int)
states[0] = [0, 0, 0, 1, 0, 0, 0]  # Initial state: middle bulb ON

# Adjacency matrix
A = np.zeros((N, N), dtype=int)
for i in range(N):
    if i > 0: A[i, i - 1] = 1
    if i < N - 1: A[i, i + 1] = 1

# State transition rules
for k in range(steps - 1):
    s = A @ states[k]
    prev = states[k]
    next_state = prev.copy()
    for j in range(N):
        if prev[j] == 0 and s[j] == 1:
            next_state[j] = 1
        elif prev[j] == 1 and s[j] == 2:
            next_state[j] = 0
    states[k + 1] = next_state

# 2. Plotting using coordgeo geometry
fig, ax = plt.subplots(figsize=(10, 8))
r = 0.3  # bulb radius

for k in range(steps):
    y = -k  # row position for step k
    
    # Horizontal line connecting bulbs in a row using line_gen
    line_pts = line_gen(np.array([[0.5], [y]]), np.array([[N + 0.5], [y]]))
    ax.plot(line_pts[0, :], line_pts[1, :], color='gray', linewidth=1, zorder=1)
    
    for j in range(N):
        x = j + 1
        center = np.array([[x], [y]])
        circ_pts = circ_gen(center, r)
        
        # Color: ON = gold/yellow, OFF = black
        is_on = (states[k, j] == 1)
        fill_color = 'gold' if is_on else 'black'
        
        ax.fill(circ_pts[0, :], circ_pts[1, :], color=fill_color, zorder=2)
        ax.plot(circ_pts[0, :], circ_pts[1, :], color='black', linewidth=1.5, zorder=3)

# Axis styling
ax.set_yticks([-k for k in range(steps)])
ax.set_yticklabels([f'Step {k}' if k > 0 else 'Initial' for k in range(steps)], fontsize=11)
ax.set_xticks(range(1, N + 1))
ax.set_xticklabels([f'B{i}' for i in range(1, N + 1)], fontsize=11)

ax.set_xlim(0, N + 1)
ax.set_ylim(-steps + 0.5, 0.8)
ax.set_aspect('equal')
ax.set_title('Bulb States Across Steps (ON: Gold, OFF: Black)', fontsize=12, pad=12)
ax.grid(False)

plt.tight_layout()
plt.savefig('figs/q09.pdf', bbox_inches='tight')
plt.close(fig)
