import numpy as np


def cross2d(r: np.ndarray, F: np.ndarray) -> float:
    """Computes the 2D scalar cross product (z-component): r_x * F_y - r_y * F_x."""
    return float(r[0] * F[1] - r[1] * F[0])


def main():
    # --- 1. Geometry Coordinates (meters) ---
    A = np.array([0.0, 0.0])  # Hinge support
    C = np.array([0.0, 3.0])  # Joint C (Top-Left)
    E = np.array([2.0, 3.0])  # Midpoint E (Load point)
    D = np.array([4.0, 3.0])  # Joint D (Top-Right)
    B = np.array([4.0, 0.0])  # Roller support

    # --- 2. Applied Loads (kN) ---
    F_C = np.array([50.0, 0.0])  # Horizontal load at C
    F_E = np.array([0.0, -90.0])  # Vertical load at E
    F_total = F_C + F_E

    # --- 3. Equilibrium System (S * x = b) ---
    # Unknown vector x = [H_A, V_A, V_B]^T
    unit_VB = np.array([0.0, 1.0])  # Direction of reaction V_B

    S = np.array([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 1.0],
        [0.0, 0.0, cross2d(B - A, unit_VB)],
    ])

    b = np.array([
        -F_total[0],
        -F_total[1],
        -cross2d(C - A, F_C) - cross2d(E - A, F_E),
    ])

    # --- 4. Row Reduction on Augmented Matrix [S | b] ---
    G = np.column_stack([S, b])

    # Row operations: R3 -> R3 / 4, R2 -> R2 - R3
    G[2, :] /= G[2, 2]
    G[1, :] -= G[1, 2] * G[2, :]

    # Extract solution vector x = [H_A, V_A, V_B]
    x = G[:, 3]
    H_A, V_A, V_B = x

    # --- 5. Support Reactions & Bending Moments ---
    R_A = np.array([H_A, V_A])
    R_B = np.array([0.0, V_B])

    M_C = cross2d(A - C, R_A)  # Column AC (forces below section C)
    M_E = cross2d(B - E, R_B)  # Beam CD (forces to the right of section E)
    max_M = max(abs(M_C), abs(M_E), 0.0)



   
    print("\nS =\n", S)
    print("\nb =", b)
    print(np.array2string(G, formatter={"float_kind": lambda v: f"{v:8.2f}"}))
    print(
        f"rank(S) = {np.linalg.matrix_rank(S)}, "
        f"rank([S|b]) = {np.linalg.matrix_rank(G)} (Unique Solution)"
    )

   
    print(f"\nH_A = {H_A:7.2f} kN  (Horizontal at A)")
    print(f"\nV_A = {V_A:7.2f} kN  (Vertical at A)")
    print(f"\nV_B = {V_B:7.2f} kN  (Vertical at B)")
    print(f"\n||S*x - b|| = {np.linalg.norm(S @ x - b):.2e} (Residual Norm)")

   
    print(f"\n|M_C| = {abs(M_C):7.2f} kN·m  (At joint C)")
    print(f"\n|M_E| = {abs(M_E):7.2f} kN·m  (Under load at E)")
if __name__ == "__main__":
    main()
