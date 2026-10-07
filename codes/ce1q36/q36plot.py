import numpy as np
import matplotlib.pyplot as plt
from coordgeo import line_gen

# grid for upper bound curve
x = np.linspace(0, 2, 200)
y_bound = x**2 / 4

# line f(x) = x/2 using coordgeo
A = np.array([[0.0], [0.0]])
B = np.array([[2.0], [1.0]])
x_line = line_gen(A, B)

plt.figure(figsize=(6, 4))
plt.plot(x_line[0, :], x_line[1, :], label=r'$f(x) = x/2$', color='blue', linewidth=2)
plt.plot(x, y_bound, '--', label=r'Upper bound $\frac{x^2}{4}$', color='red')

plt.fill_between(x, 0, y_bound, color='red', alpha=0.1)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Upper Bound $x^2/4$ and Optimal $f(x) = x/2$')
plt.legend()

plt.savefig('figs/q36.pdf')
plt.close()
