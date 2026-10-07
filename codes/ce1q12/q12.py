import sympy as sp

# setup free var
x3 = sp.Symbol('x3')

# given mat A
A = sp.Matrix([[1, 1, 1],
               [1, 0, 2]])

# 1. row reduction
R, _ = A.rref()

# 2. sub x3 back to get x1 & x2
# row 1: x1 + 2*x3 = 0 => x1 = -2*x3
# row 2: -x2 + x3 = 0  => x2 = x3
x1 = -R[0, 2] * x3
x2 = R[1, 2] * x3

# 3. soln vec
soln = sp.Matrix([x1, x2, x3])

print("reduced matrix:")
sp.pprint(R)

print("\nsoln vector x:")
sp.pprint(soln)

print(f"\nin dir vec form:\nx = x3 * {list(soln / x3)}")
print("\nline thrugh origin")

