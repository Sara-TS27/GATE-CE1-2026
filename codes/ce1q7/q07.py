#GATE CE 2026 Q.7 : angle RTS
import numpy as np
import numpy.linalg as LA

r = 1.0
alpha = np.radians(130.0)
beta = np.radians(50.0)

#Unit vectors w_theta and the points
def w(theta):
    return np.array([[np.cos(theta)],[np.sin(theta)]])
i = np.array([[1.0],[0.0]])
P = -r*i
Q = r*i
R = r*w(alpha)
S = r*w(beta)

#Angle ROS from cos(alpha - beta) = w_alpha^T w_beta
cos_ROS = (w(alpha).T@w(beta)).item()
print("angle ROS =",np.degrees(np.arccos(cos_ROS)))

#Direction vectors of PR and QS
m1 = R-P
m2 = S-Q

#Intersection T : [m1  -m2][k1 k2]^T = Q - P
M = np.block([m1,-m2])
k = LA.solve(M,Q-P)
T = P + k[0,0]*m1
print("T =",T.flatten())

#Angle RTS between TR and TS
a = R-T
b = S-T
cos_RTS = (a.T@b).item()/(LA.norm(a)*LA.norm(b))
print("angle RTS =",np.degrees(np.arccos(cos_RTS)))
