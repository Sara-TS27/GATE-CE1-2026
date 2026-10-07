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

#Q3 : two parabolas and the common line from the pencil
V  = np.array([[1,0],[0,0]])
u1 = np.array([[0],[-0.5]]);  f1 = 0      # x^2 - y = 0
u2 = np.array([[1],[0.5]]);   f2 = 1      # x^2 + 2x + y + 1 = 0

#Points of a parabola (standard parabola, then x = P x_std + O)
def parab_pts(V,u,f,xmin,xmax):
    n,c,F,O,lam,P,e = conic_param(V,u,f)
    flen = parab_param(lam,P,u).item()
    y = np.linspace(xmin,xmax,200) - O[0,0]      # P swaps the axes
    x = parab_gen(y,flen)
    return P@np.vstack((x,y)) + O

x_par1 = parab_pts(V,u1,f1,-3,2)
x_par2 = parab_pts(V,u2,f2,-3,2)

#Common line x + y = -1/2 (normal form)
n = np.array([[1],[1]]);  c = -0.5
k = 2.5*np.sqrt(2)
x_line = line_norm(n,c,-k,k)

plt.figure(figsize=(8,6.5))
plt.plot(x_par1[0,:],x_par1[1,:],'b',label='$y=x^2$')
plt.plot(x_par2[0,:],x_par2[1,:],'r',label='$y=-x^2-2x-1$')
plt.plot(x_line[0,:],x_line[1,:],'g--',label='$x+y=-1/2$')
plt.axhline(0,color='k',lw=1); plt.axvline(0,color='k',lw=1)
plt.grid(alpha=0.5,ls=':')
plt.xlabel('x'); plt.ylabel('y')
plt.title('Two Parabolas and Common Line',fontsize=9)
plt.legend(loc='upper right',fontsize=7)
plt.savefig(os.path.join(FIGS,'q03.pdf'))
plt.show()   
#if using termux
#plt.savefig('./figs/q3.pdf')
#plt.savefig('./figs/q3.png')
#subprocess.run(shlex.split("termux-open ./figs/q3.pdf"))

#plt.savefig('../figs/q3.pdf')
#plt.savefig('../figs/q3.eps')
#subprocess.run(shlex.split("termux-open ../figs/q3.pdf"))
#else
#plt.show() 
