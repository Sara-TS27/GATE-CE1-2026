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


#Q38 : two-member truss with DOFs u, v at Q
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

P = np.array([[0],[0]]);  Q = np.array([[1],[1]]);  R = np.array([[2],[0]])
x_PQ = line_gen(P,Q);  x_QR = line_gen(Q,R)

d = 0.3
u_vec = d*e1;  v_vec = d*e2          # DOF directions at Q

plt.figure(figsize=(7,5))
plt.plot(x_PQ[0,:],x_PQ[1,:],'b',lw=1.5)
plt.plot(x_QR[0,:],x_QR[1,:],'r',lw=1.5)
pts = np.block([P,Q,R])
plt.plot(pts[0,0],pts[1,0],'bo'); plt.plot(pts[0,1],pts[1,1],'ro'); plt.plot(pts[0,2],pts[1,2],'ro')
plt.arrow(Q[0,0],Q[1,0],u_vec[0,0],u_vec[1,0],color='green',width=0.01,head_width=0.07,head_length=0.1,length_includes_head=True)
plt.arrow(Q[0,0],Q[1,0],v_vec[0,0],v_vec[1,0],color='purple',width=0.01,head_width=0.07,head_length=0.1,length_includes_head=True)
plt.annotate('P (Hinge)',(0,0),textcoords='offset points',xytext=(0,-12),ha='center')
plt.annotate('Q',(1,1),textcoords='offset points',xytext=(6,4))
plt.annotate('R (Hinge)',(2,0),textcoords='offset points',xytext=(0,-12),ha='center')

h = [Line2D([0],[0],color='b',marker='o',label='Member PQ'),
     Line2D([0],[0],color='r',marker='o',label='Member QR'),
     mpatches.Patch(color='green',label='u (Horizontal DOF)'),
     mpatches.Patch(color='purple',label='v (Vertical DOF)')]
plt.legend(handles=h,loc='upper right',fontsize=8)
plt.xlim(-0.5,2.5); plt.ylim(-0.5,1.8)
plt.grid(alpha=0.4,ls=':')
plt.title('Two-Member Truss with Degrees of Freedom (u, v) at Q')
plt.savefig(os.path.join(FIGS,'q38.pdf'))
plt.show()

#if using termux
plt.savefig('./figs/q38.pdf')
plt.savefig('./figs/q38.png')
subprocess.run(shlex.split("termux-open ./figs/q38.pdf"))

#plt.savefig('../figs/q38.pdf')
#plt.savefig('../figs/q38.eps')
#subprocess.run(shlex.split("termux-open ../figs/q38.pdf"))
#else
#plt.show() #opening the plot window
