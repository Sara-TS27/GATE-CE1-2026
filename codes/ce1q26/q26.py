#GATE CE 2026 Q.26 : Bayes' theorem in vector form
import numpy as np

#Prior and likelihood vectors
pi = np.array([1/2,1/2])
l = np.array([6/10,3/7])

#Total probability of a black ball
PE = pi@l
#Posterior probabilities
post = pi*l/PE

print("Pr(E) =",PE)
print("Pr(B1|E) =",post[0])
print("Pr(B1|E) rounded to two decimals =",round(post[0],2))
