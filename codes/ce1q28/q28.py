#GATE CE 2026 Q.28
import numpy as np
import numpy.linalg as LA

#(x+y-7)^2 and (3x+y-13)^2 as conics
V1 = np.array([[1.0,1.0],[1.0,1.0]]); u1 = np.array([[-7.0],[-7.0]]); f1 = 49.0
V2 = np.array([[9.0,3.0],[3.0,1.0]]); u2 = np.array([[-39.0],[-13.0]]); f2 = 169.0

#Member mu = 1 of the pencil
V = V1 + V2
u = u1 + u2
f = f1 + f2
M = np.block([[V,u],[u.T,np.array([[f]])]])
print("M =\n",M)

#M = B^T B
B = np.array([[1.0,1.0,-7.0],
              [3.0,1.0,-13.0]])
#Row reduction : R2 -> 5R2 - 2R1, R3 -> 5R3 + 23R1, R3 -> R3 + 4R2
R = M.copy()
R[1,:] = 5*R[1,:] - 2*R[0,:]
R[2,:] = 5*R[2,:] + 23*R[0,:]
R[2,:] = R[2,:] + 4*R[1,:]
print("reduced M =\n",R)
print("rank M =",LA.matrix_rank(M))

#Row reduction of V : R2 -> R2 - (2/5) R1, pivots 10 and 2/5 (both positive)
W = V.copy()
W[1,:] = W[1,:] - (V[1,0]/V[0,0])*W[0,:]
print("\nreduced V =\n",W)

#Zero norm : ||B xt||^2 = 0 => M xt = 0 => 2y - 8 = 0, 10x + 4y - 46 = 0
y = 8/2
x = (46-4*y)/10
xt = np.array([[x],[y],[1.0]])
print("x, y =",x,y)
print("\n||B*xt|| =",LA.norm(B@xt))
print("\nx^3 + y^3 =",round(x**3+y**3))
