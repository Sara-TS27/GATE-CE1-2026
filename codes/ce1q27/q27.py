#GATE CE 2026 Q.27 : Cholesky decomposition
import numpy as np
import numpy.linalg as LA

A = np.array([[9.0,15.0],
              [15.0,50.0]])

#Row reduction : R2 -> R2 - (5/3) R1, pivots are l11^2 and l22^2
B = A.copy()
B[1,:] = B[1,:] - (A[1,0]/A[0,0])*B[0,:]
print("reduced matrix :\n",B)

#Entry by entry
l11 = np.sqrt(A[0,0])
l21 = A[1,0]/l11
l22 = np.sqrt(A[1,1]-l21**2)
L = np.array([[l11,0.0],[l21,l22]])
print("\nL =\n",L)
print("\nL*L^T =\n",L@L.T)

#Check with numpy
print("\nL =\n",LA.cholesky(A))
print("\n|l22| =",abs(l22))
