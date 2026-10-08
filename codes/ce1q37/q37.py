import sympy as sp

# define symbolic variables
s, t, x = sp.symbols("s t x")
a, b = sp.symbols("a b")

# step 1: characteristic equation s^2 - s - 6 = 0 from Laplace transform Y(s) denominator
denominator = s**2 - s - 6

# step 2: find roots of denominator to get poles
roots = sp.solve(denominator, s)
root1, root2 = roots[0], roots[1]  # roots are 3 and -2

print("Roots of characteristic equation:", roots)

# step 3: form y(t) using inverse laplace form: a * e^(root1 * t) + b * e^(root2 * t)
y_t = a * sp.exp(root1 * t) + b * sp.exp(root2 * t)
print("y(t) =", y_t)

# step 4: substitute e^t = x to get solution in terms of x
y_x = y_t.subs(sp.exp(t), x)

# simplify exponents (e^(-2t) becomes x^(-2) = 1/x^
