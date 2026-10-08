import sys, os
HERE  = os.path.dirname(os.path.abspath(__file__))              # repo/codes/ce1qN
REPO  = os.path.abspath(os.path.join(HERE,'..','..'))           # repo
sys.path.insert(0, os.path.join(REPO,'CoordGeo'))
FIGS  = os.path.join(REPO,'figs'); os.makedirs(FIGS,exist_ok=True)
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
try:                                  # CoordGeo/line/funcs.py , CoordGeo/conics/funcs.py
    from line.funcs import *
    from conics.funcs import *
except ModuleNotFoundError:           # CoordGeo/line.py , CoordGeo/conics.py
    from line import *
    from conics import *
from params import *


#if using termux
import subprocess
import shlex
#end if

#Q7 : circle, diameter PQ, angle ROS = 80 deg, T = PR ∩ QS
r = 1
al = np.deg2rad(130); be = np.deg2rad(50)
w = lambda t: np.array([[np.cos(t)],[np.sin(t)]])     # unit vector w_theta

O = np.zeros((2,1))
P = -r*e1;  Q = r*e1
R = r*w(al); S = r*w(be)

#Intersection of the lines PR and QS : [R-P  -(S-Q)][k1;k2] = Q-P
M = np.block([dir_vec(P,R), -dir_vec(Q,S)])
k = LA.solve(M, Q-P)
T = P + k[0]*dir_vec(P,R)

x_circ = circ_gen(O,r)
x_PR = line_gen(P,R);  x_RT = line_gen(R,T)
x_QS = line_gen(Q,S);  x_ST = line_gen(S,T)
x_OR = line_gen(O,R);  x_OS = line_gen(O,S)

plt.figure(figsize=(8,10))
plt.plot(x_circ[0,:],x_circ[1,:],'b')
plt.plot(x_PR[0,:],x_PR[1,:],'r');   plt.plot(x_RT[0,:],x_RT[1,:],'r--')
plt.plot(x_QS[0,:],x_QS[1,:],'g');   plt.plot(x_ST[0,:],x_ST[1,:],'g--')
plt.plot(x_OR[0,:],x_OR[1,:],'k:');  plt.plot(x_OS[0,:],x_OS[1,:],'k:')

pts = np.block([P,Q,R,S,T,O])
plt.plot(pts[0,:],pts[1,:],'ko',ms=4)
lab = [('$P(-r=re^{i\\pi})$',P,(-4,4),'right'), ('$Q(r=re^{i0})$',Q,(4,4),'left'),
       ('$R(re^{i\\alpha})$',R,(-8,10),'right'), ('$S(re^{i\\beta})$',S,(8,10),'left'),
       ('$T$',T,(6,6),'left'), ('$O(0)$',O,(5,4),'left')]
for txt,pt,off,ha in lab:
    plt.annotate(txt,(pt[0,0],pt[1,0]),textcoords='offset points',xytext=off,ha=ha,fontsize=7)

plt.axhline(0,color='k',lw=1); plt.axvline(0,color='k',lw=1)
plt.grid(alpha=0.4,ls='--',lw=0.5)
plt.gca().set_aspect('equal',adjustable='box')
plt.xlim(-1.6,1.6); plt.ylim(-1.15,2.25)
plt.title('Circle Geometry in Exponential Form ($e^{i\\theta}$)',fontsize=9,fontweight='bold')
plt.savefig(os.path.join(FIGS,'q07.pdf'))

#if using termux
plt.savefig('../../figs/q7.pdf')
plt.savefig('../../figs/q7.png')
#subprocess.run(shlex.split("termux-open ../../figs/q7.pdf"))

plt.savefig('../../figs/q7.pdf')
plt.savefig('../../figs/q7.eps')
#subprocess.run(shlex.split("termux-open ../../figs/q7.pdf"))
#else
#plt.show() #opening the plot window
plt.show()


