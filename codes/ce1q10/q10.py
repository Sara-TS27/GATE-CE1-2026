import numpy as np

# System of linear equations:
# P-Q=1
# P+Q=13
# In matrix form Ax = b:
A = np.array([[1, -1], [1, 1]])

b = np.array([1, 13])

# Solve the linear system Ax = b for x = [P, Q]^T
x = np.linalg.solve(A, b)

# Extract integer values for P and Q
P, Q = int(round(x[0])), int(round(x[1]))

# Calculate the pdt PQ
product = P * Q

print(f"P = {P}")
print(f"Q = {Q}")
print(f"Product (P * Q) = {product}")
