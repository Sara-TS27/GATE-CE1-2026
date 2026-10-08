#GATE CE 2026 Q.37 : x^2 y'' = 6 y
import sympy as sp

s = sp.symbols("s")
t, x = sp.symbols("t x", positive=True)
a, b = sp.symbols("a b")
y0, dy0 = sp.symbols("y0 dy0")

#x = e^t gives y'' - y' - 6 y = 0 ; Laplace transform
Y = ((s-1)*y0 + dy0)/(s**2 - s - 6)
print("Y(s) =",sp.factor(Y))

#Partial fractions
print("partial fractions :",sp.apart(Y,s))

#Poles of Y(s) : s = 3, s = -2
print("poles :",sp.solve(s**2 - s - 6,s))

#y(t) = a e^{3t} + b e^{-2t}
y_t = a*sp.exp(3*t) + b*sp.exp(-2*t)

#Substituting e^t = x
y_x = a*x**3 + b/x**2
print("y(x) =",y_x)

#Check : x^2 y'' - 6 y = 0
print("residual =",sp.simplify(x**2*sp.diff(y_x,x,2) - 6*y_x))
