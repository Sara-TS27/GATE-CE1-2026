import numpy as np

# prior probability vector pi = [P(B1), P(B2)]
pi = np.array([0.5, 0.5])

# likelihood vector l = [P(E|B1), P(E|B2)]
# bag 1 has 6 black out of 10, bag 2 has 3 black out of 7
l = np.array([6 / 10, 3 / 7])

# total probability Pr(E) = pi_T * l
pr_E = np.dot(pi, l)

# bayes theorem for Pr(B1|E) = (pi[0] * l[0]) / pr_E
pr_B1_given_E = (pi[0] * l[0]) / pr_E

print("Total Pr(E):", round(pr_E, 4))
print("Pr(B1|E):", round(pr_B1_given_E, 4))
print("Rounded answer:", round(pr_B1_given_E, 2))
