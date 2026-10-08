#GATE CE 2026 Q.12
import numpy as np
import numpy.linalg as LA

A = np.array([[1.0,1.0,1.0],
              [1.0,0.0,2.0]])

#Row reduction : R2 -> R2 - R1, R1 -> R1 + R2, R2 -> -R2 gives x1 + 2 x3 = 0, x2 - x3 = 0
B = A.copy()
B[1,:] = B[1,:] - B[0,:]
B[0,:] = B[0,:] + B[1,:]
print("reduced matrix (before scaling R2) :\n",B)
print("rank A =",LA.matrix_rank(A))

#Free variable x3 = 1
x3 = 1.0
x = np.array([[-2*x3],[x3],[x3]])
print("x =",x.flatten()," A*x =",(A@x).flatten())

#Cross product of the rows
v = np.cross(A[0,:],A[1,:])
print("a1 X a2 =",v)
