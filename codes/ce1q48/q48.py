#GATE CE 2026 Q.48 : Newton-Raphson for f(x) = e^{-x} - x
import numpy as np

def f(x):
    return np.exp(-x) - x
def df(x):
    return -np.exp(-x) - 1

x0 = 0.5
x1 = x0 - f(x0)/df(x0)
#Simplified form x1 = (1 + x0)/(1 + e^{x0})
x1s = (1 + x0)/(1 + np.exp(x0))
print(f"First approximation  x0 = {x0:.2f}")
print(f"Second approximation x1 = {x1:.5f}")

#Further iterations converge to 0.567143
x2 = x1 - f(x1)/df(x1)
x3 = x2 - f(x2)/df(x2)
print(f"x2 = {x2:.6f}, x3 = {x3:.6f}")
