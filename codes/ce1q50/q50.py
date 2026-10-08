import numpy as np


def build_system(mu: float, c: float, s: float, W: float = 1.0):
    """Builds equilibrium matrix S and load vector d for blocks A and B."""
    S = np.array([
        [1.0,  0.0, -c],
        [mu,   0.0,  s],
        [0.0, -mu,   c],
        [0.0,  1.0, -s],
    ])
    d = np.array([0.0, W, 0.0, W])
    return S, d


def main():
    theta = np.radians(45.0)
    c, s = np.cos(theta), np.sin(theta)
    W = 1.0

    # Characteristic polynomial: c * mu^2 + 2 * s * mu - c = 0
    roots = np.roots([c, 2 * s, -c])
    mu = float(roots[roots > 0][0])

    print(f"Polynomial Roots: {roots}")
    print(f"Calculated mu = {mu:.4f}  (Rounded: {mu:.2f})")

    # Verification and consistency check
    S, d = build_system(mu, c, s, W)
    x, _, _, _ = np.linalg.lstsq(S, d, rcond=None)
    N_A, N_B, C = x

    rank_S = np.linalg.matrix_rank(S)
    rank_aug = np.linalg.matrix_rank(np.column_stack([S, d]))
    residual = np.linalg.norm(S @ x - d)

    print("\n--- Verification ---")
    print(f"N_A = {N_A:.4f}, N_B = {N_B:.4f}, C = {C:.4f}")
    print(f"rank(S) = {rank_S}, rank([S|d]) = {rank_aug}")
    print(f"Residual Norm ||S*x - d|| = {residual:.2e}")


if __name__ == "__main__":
    main()
