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


#Q50 : blocks A and B connected by a rigid rod

theta = np.deg2rad(45);  L = 2
A = L*np.sin(theta)*e2                      # block A on the wall
B = L*np.cos(theta)*e1                      # block B on the floor
O = np.zeros((2,1))

x_rod = line_gen(A,B)
x_wall = line_gen(O,2.5*e2)
x_floor = line_gen(O,2.5*e1)

fig,ax = plt.subplots(figsize=(7,7))
ax.plot(x_wall[0,:],x_wall[1,:],'k',lw=4)
ax.plot(x_floor[0,:],x_floor[1,:],'k',lw=4)
ax.plot(x_rod[0,:],x_rod[1,:],'b',lw=4)
ax.plot([A[0,0],B[0,0]],[A[1,0],B[1,0]],'bo',ms=8)
ax.annotate('Block A',(A[0,0],A[1,0]),textcoords='offset points',xytext=(0,10),ha='center')
ax.annotate('Block B',(B[0,0],B[1,0]),textcoords='offset points',xytext=(24,-16),ha='center')
ax.set_xlim(-0.5,2.5); ax.set_ylim(-0.5,2.5)
ax.grid(alpha=0.4,ls=':')
ax.set_title('Blocks A and B Connected by a Rigid Rod')
plt.savefig(os.path.join(FIGS,'q50.pdf'))
#if using termux
plt.savefig('../../figs/q50.pdf')
plt.savefig('../../figs/q50.png')
#subprocess.run(shlex.split("termux-open ../../figs/q50.pdf"))

#plt.savefig('../../figs/q50.pdf')
#plt.savefig('../../figs/q50.eps')
#subprocess.run(shlex.split("termux-open ../../figs/q50.pdf"))
#else
#plt.show() #opening the plot window
plt.show()
