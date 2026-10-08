#GATE CE 2026 Q.3 : intersection of y = x^2 and y = -x^2 - 2x - 1
import numpy as np
import numpy.linalg as LA

#Orthogonal matrix
omat = np.array([[0,1],[-1,0]])

#x^2 - y = 0
V1 = np.array([[1.0,0.0],[0.0,0.0]])
u1 = np.array([[0.0],[-0.5]])
f1 = 0.0
#x^2 + 2x + y + 1 = 0
V2 = np.array([[1.0,0.0],[0.0,0.0]])
u2 = np.array([[1.0],[0.5]])
f2 = 1.0

#V is singular (rank 1 < 2), so both curves are parabolas
print("rank V1, V2 =",LA.matrix_rank(V1),LA.matrix_rank(V2))

#Coefficient matrix of the pencil
def N(mu):
    V = V1 + mu*V2
    u = u1 + mu*u2
    f = f1 + mu*f2
    return np.block([[V,u],[u.T,np.array([[f]])]])

#Degenerate members : rank < 3
for mu in [-1.0,1.0]:
    print("mu =",mu," rank =",LA.matrix_rank(N(mu)))

#Common chord for mu = -1
n = 2*(u1-u2)
c = -(f1-f2)
print("chord : n^T x =",c)
#direction vector and a point on the chord
m = omat@n
m = m/m[0,0]
h = np.array([[0.0],[-0.5]])
print("n =",n.flatten(),"m =",m.flatten())

#Line-conic intersection on the first parabola
mVm = (m.T@V1@m).item()
mVhu = (m.T@(V1@h+u1)).item()
gh = (h.T@V1@h+2*u1.T@h+f1).item()
Delta = mVhu**2 - gh*mVm
print("m^T*V*m =",mVm,", m^T(Vh+u) =",mVhu,", g(h) =",gh)
print("Delta =",Delta)
kappa = np.roots([mVm,2*mVhu,gh])
print("kappa =",kappa)

#Other degenerate member mu = 1 : 2x^2 + 2x + 1 = 0
print("roots for mu = 1 :",np.roots([2,2,1]))

if Delta > 0:
    print("Number of intersection points: 2")
elif Delta == 0:
    print("Number of intersection points: 1")
else:
    print("Number of intersection points: 0")
