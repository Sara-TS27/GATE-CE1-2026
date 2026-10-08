import numpy as np

# matrix A from question
A = np.array([[9, 15], [15, 50]], dtype=float)

# manual step by step cholesky calculation like in pdf
# L = [[l11, 0], [l21, l22]]
l11 = np.sqrt(A[0, 0])
l21 = A[1, 0] / l11
l22 = np.sqrt(A[1, 1] - l21**2)

print("Calculated L matrix elements:")
print("l11 =", int(l11))
print("l21 =", int(l21))
print("l22 =", int(l22))

# verify using numpy cholesky
L = np.linalg.cholesky(A)
print("\nVerification using numpy:")
print("|l22| =", int(abs(L[1, 1])))
