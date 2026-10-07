import sys, os
HERE  = os.path.dirname(os.path.abspath(__file__))              # repo/codes/ce1qN
REPO  = os.path.abspath(os.path.join(HERE,'..','..'))           # repo
sys.path.insert(0, os.path.join(REPO,'CoordGeo'))
FIGS  = os.path.join(REPO,'figs'); os.makedirs(FIGS,exist_ok=True)
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import shlex
import subprocess
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

#Q39 : plane frame and bending moment diagram
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

A = np.array([[0],[0]]); C = np.array([[0],[3]]); E = np.array([[2],[3]])
D = np.array([[4],[3]]); B = np.array([[4],[0]])
F_C = np.array([[50],[0]]); F_E = np.array([[0],[-90]])

cross2 = lambda r,F: (r[0]*F[1]-r[1]*F[0]).item()      # r x F in 2D  (1.1.12.1)

#Equilibrium  [H_A V_A V_B]
rhs = np.array([[-(F_C+F_E)[0,0]], [-(F_C+F_E)[1,0]], [-(cross2(C-A,F_C)+cross2(E-A,F_E))]])
Mat = np.array([[1,0,0],[0,1,1],[0,0,4]])
H_A,V_A,V_B = LA.solve(Mat,rhs).flatten()
R_A = np.array([[H_A],[V_A]]);  R_B = np.array([[0],[V_B]])

#Bending moments (1.1.12.2)
M_C = abs(cross2(A-C,R_A))
M_E = abs(cross2(B-E,R_B))
M_D = abs(cross2(B-D,R_B))
s = 1/300                                         # plotting scale

x_frame = np.block([A,C,D,B])
x_col = np.block([A, C + np.array([[-M_C*s],[0]])])
x_beam = np.block([C + M_C*s*e2, E + M_E*s*e2, D + M_D*s*e2])

plt.figure(figsize=(8,6))
plt.plot(x_frame[0,:],x_frame[1,:],'k',lw=3)
plt.arrow(E[0,0],E[1,0],0,-0.8,color='b',width=0.02,head_width=0.12,head_length=0.15,length_includes_head=True)
plt.plot(x_col[0,:],x_col[1,:],'m',lw=1)
plt.plot([-M_C*s,0],[3,3],'m--',lw=1)
plt.plot(x_beam[0,:],x_beam[1,:],'m',lw=1)
plt.annotate('A (Hinge)',(0,0),textcoords='offset points',xytext=(4,-10))
plt.annotate('B (Roller)',(4,0),textcoords='offset points',xytext=(4,-10))
for txt,pt in (('C',C),('E',E),('D',D)):
    plt.annotate(txt,(pt[0,0],pt[1,0]),textcoords='offset points',xytext=(0,4),fontsize=7)

h = [Line2D([0],[0],color='k',lw=3,label='Plane Frame'),
     mpatches.Patch(color='b',label='90 kN Vertical'),
     Line2D([0],[0],color='m',lw=1,label='BM Diagram')]
plt.legend(handles=h,loc='upper right',fontsize=7)
plt.xlim(-1.5,5.5); plt.ylim(-0.5,4.7)
plt.gca().set_aspect('equal',adjustable='box')
plt.grid(alpha=0.4,ls=':')
plt.title('Frame Loading and Bending Moment Diagram',fontsize=9)
plt.savefig(os.path.join(FIGS,'q39.pdf'))


#if using termux
plt.savefig('../../figs/q39.pdf')
plt.savefig('../../figs/q39.png')
#subprocess.run(shlex.split("termux-open ../../figs/q39.pdf"))

#plt.savefig('../../figs/q39.pdf')
#plt.savefig('../../figs/q39.eps')
#subprocess.run(shlex.split("termux-open ../../figs/q39.pdf"))
#else
#plt.show() #opening the plot window
plt.show()
