import numpy as np
import matplotlib.pyplot as plt
from coordgeo import line_gen

# grid
x = np.linspace(-3, 2, 400)

# parabolas
y1 = x**2
y2 = -x**2 - 2*x - 1

# common line using coordgeo: x + y = -0.5
A = np.array([[-3], [2.5]])
B = np.array([[2], [-2.5]])
x_line = line_gen(A, B)

# plot
plt.figure(figsize=(10, 8))
plt.plot(x, y1, label=r'$y = x^2$', color='blue')
plt.plot(x, y2, label=r'$y = -x^2 - 2x - 1$', color='red')
plt.plot(x_line[0, :], x_line[1, :], '--', label=r'$x + y = -1/2$', color='green')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.title('Two Parabolas and Common Line')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('figs/q03.pdf')
plt.close()
