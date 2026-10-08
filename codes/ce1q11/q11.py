#GATE CE 2026 Q.11
import numpy as np
import numpy.linalg as LA

P = np.array([[1,0,1],
              [0,1,0],
              [1,0,1]])

#lambda is an eigenvalue when lambda*I - P is singular
for lam in [0,1,2]:
    print("lambda =",lam," rank(lambda*I - P) =",LA.matrix_rank(lam*np.eye(3)-P))

eig_vals = LA.eigvals(P)
print("eigenvalues =",np.sort(eig_vals))

#a) trace = sum of eigenvalues
tr_P = np.trace(P)
print("a)",tr_P,np.sum(eig_vals),np.isclose(tr_P,np.sum(eig_vals)))

#b) P^T P = I
print("b)",np.array_equal(P.T@P,np.eye(3)))
print(P.T@P)

#c) skew-symmetric
print("c)",np.array_equal(P.T,-P))

#d) |eigenvalue| = 1
print("d)",np.all(np.isclose(np.abs(eig_vals),1)))


