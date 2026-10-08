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


#Q49 : second-degree interpolating polynomial
xd = np.array([-2,1,2]);  yd = np.array([28,4,16])

#Vandermonde system (1.1.11.1)
Vd = np.block([np.ones((3,1)), xd.reshape(-1,1), (xd**2).reshape(-1,1)])
c = LA.solve(Vd,yd.reshape(-1,1))                        # [c0 c1 c2]^T = [2 -3 5]^T

xx = np.linspace(-2.5,2.5,200)
X = np.block([[np.ones((1,200))],[xx],[xx**2]])
yy = (c.T@X).flatten()                                   # P2(x) = c^T [1 x x^2]^T
P20 = (np.array([[1,0,0]])@c).item()                     # P2(0)

plt.figure(figsize=(7,5))
plt.plot(xx,yy,'b',label='$P_2(x)=5x^2-3x+2$')
plt.plot(xd,yd,'ro',label='Data Points')
plt.plot(0,P20,'go',label='$P_2(0)=2$')
plt.axhline(0,color='k',lw=0.8); plt.axvline(0,color='k',lw=0.8)
plt.grid(alpha=0.7,ls=':')
plt.xlabel('x'); plt.ylabel('y')
plt.title('Second-Degree Interpolating Polynomial')
plt.legend(loc='upper right',fontsize=8)
plt.savefig(os.path.join(FIGS,'q49.pdf'))

#if using termux
plt.savefig('../../figs/q49.pdf')
plt.savefig('../../figs/q49.png')
#subprocess.run(shlex.split("termux-open ../../figs/q49.pdf"))

#plt.savefig('../../figs/q49.pdf')
#plt.savefig('../../figs/q49.eps')
#subprocess.run(shlex.split("termux-open ../../figs/q49.pdf"))
#else
#plt.show() #opening the plot window
plt.show()
