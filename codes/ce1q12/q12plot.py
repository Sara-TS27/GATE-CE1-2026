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

#Q12 : the two planes and their line of intersection
A = np.array([[1,1,1],[1,0,2]])

#Direction of the line = cross product of the rows (1.1.3.4)
m = np.cross(A[0,:],A[1,:]).reshape(-1,1)
x_line = line_dir_pt(m,np.zeros((3,1)),-1.5,1.5)

#Planes a1 x1 + a2 x2 + a3 x3 = 0  ->  x3 = -(a1 x1 + a2 x2)/a3
g = np.linspace(-3,3,20)
X,Y = np.meshgrid(g,g)
Z1 = -(A[0,0]*X + A[0,1]*Y)/A[0,2]
Z2 = -(A[1,0]*X + A[1,1]*Y)/A[1,2]

fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z1,color='teal',alpha=0.5)
ax.plot_surface(X,Y,Z2,color='orange',alpha=0.5)
ax.plot(x_line[0,:],x_line[1,:],x_line[2,:],color='darkred',lw=3)
ax.set_xlim(-3,3); ax.set_ylim(-3,3); ax.set_zlim(-6,6)
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title('Intersection of Two Planes',fontsize=9)
plt.savefig(os.path.join(FIGS,'q12.pdf'))

#if using termux
plt.savefig('../../figs/q12.pdf')
plt.savefig('../../figs/q12.png')
#subprocess.run(shlex.split("termux-open ../../figs/q12.pdf"))

#plt.savefig('../../figs/q12.pdf')
#plt.savefig('../../figs/q12.eps')
#subprocess.run(shlex.split("termux-open ../../figs/q12.pdf"))
#else
#plt.show() #opening the plot window
plt.show()
