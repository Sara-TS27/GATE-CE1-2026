import sympy as sp

# variables
x, t = sp.symbols("x t")
y = sp.Function("y")

# solving y''(t) - y'(t) - 6y(t) = 0 after sub x = e^t
ode = sp.Eq(y(t).diff(t, 2) - y(t).diff(t) - 6 * y(t), 0)

# get general solution in terms of t
sol_t = sp.dsolve(ode, y(t))

# put t = ln(x) to get solution in terms of x
sol_x = sol_t.rhs.subs(t, sp.log(x))

print("Solution y(x):", sp.simplify(sol_x))
print("Matches Option (b): y(x) = a*x^3 + b/(x^2)")
