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

#Q48 : one Newton-Raphson step for f(x) = e^{-x} - x
f  = lambda x: np.exp(-x) - x
df = lambda x: -np.exp(-x) - 1

x0 = 0.5
x1 = x0 - f(x0)/df(x0)                                   # (1.1.10.1)

x = np.linspace(0,1,200)
A0 = np.array([[x0],[f(x0)]])                            # point of tangency
m  = np.array([[1],[df(x0)]])                            # tangent direction
x_tan = line_dir_pt(m,A0,-0.5,0.5)                       # x = A0 + k m

plt.figure(figsize=(7,5))
plt.plot(x,f(x),'b',label='$f(x)=e^{-x}-x$')
plt.plot(x_tan[0,:],x_tan[1,:],'r--',label='Tangent at $x_0=0.5$')
plt.axhline(0,color='k',lw=0.8)
plt.plot([x0,x1],[f(x0),0],'ko')
plt.annotate('$x_0=0.5$',(x0,f(x0)),textcoords='offset points',xytext=(0,9),ha='center',fontsize=8)
plt.annotate('$x_1\\approx0.57$',(x1,0),textcoords='offset points',xytext=(0,-13),ha='center',fontsize=8)
plt.grid(alpha=0.4,ls=':')
plt.xlabel('x'); plt.ylabel('f(x)')
plt.title('Newton-Raphson Step for $f(x)=e^{-x}-x$')
plt.legend(loc='upper right',fontsize=8)
plt.savefig(os.path.join(FIGS,'q48.pdf'))
plt.show()

#if using termux
plt.savefig('../../figs/q48.pdf')
plt.savefig('../../figs/q48.png')
subprocess.run(shlex.split("termux-open ../../figs/q48.pdf"))

#plt.savefig('../../figs/q48.pdf')
#plt.savefig('../../figs/q48.eps')
#subprocess.run(shlex.split("termux-open ../../figs/q48.pdf"))
#else
#plt.show() #opening the plot window
