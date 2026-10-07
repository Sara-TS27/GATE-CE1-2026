import numpy as np

# matrix given in qn
P = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
])



#(P^T) ---
P_T = P.T
print("\n--- P Transpose (P^T) ---")
print(P_T)

#(P^T * P) ---
P_trans_P = np.dot(P_T, P)  # or P_T @ P
print("\n--- P Transpose into P (P^T * P) ---")
print(P_trans_P)

#a)Trace == Sum of Eigvals
tr_P = np.trace(P)
eig_vals = np.linalg.eigvals(P)
sum_eig = np.sum(eig_vals)
chk_a = np.isclose(tr_P, sum_eig)
print(f"a) Trace ({tr_P}) == Sum of Eigvals ({sum_eig}) -> {chk_a}")

# b)P^T * P is Identity Matrix (I)
I = np.eye(3)
chk_b = np.array_equal(P_trans_P, I)
print(f"b) P^T * P == Identity Matrix -> {chk_b}")

# c)P is Skew-Symmetric (P^T == -P)
chk_c = np.array_equal(P_T, -P)
print(f"c) P^T == -P -> {chk_c}")

#d)|Eigenvalues| are all 1
abs_eig = np.abs(eig_vals)
chk_d = np.all(np.isclose(abs_eig, 1))
print(f"d) |Eigvals| are all 1 {abs_eig} -> {chk_d}")


print("\nans: Option (a) is TRUE!")
