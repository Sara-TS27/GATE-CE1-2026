#Code by Sara
import numpy as np
def f(x):
    return np.exp(-x) - x
def df(x):
    return -np.exp(-x) - 1
x0=0.5
x1=x0-f(x0)/df(x0)
print(f"First approximation x1 = {x0:.2f}")
print(f"Second approximation x1 = {x1:.2f}")
