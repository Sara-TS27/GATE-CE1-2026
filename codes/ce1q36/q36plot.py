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

#Q36 : upper bound x^2/4 and the optimal f(x) = x/2
x = np.linspace(0,2,200)
f_opt = line_gen_num(np.array([[0],[0]]), np.array([[2],[1]]), 200)   # y = x/2
ub = parab_gen(x,4)                                                   # x^2/4

plt.figure(figsize=(7,5))
plt.plot(f_opt[0,:],f_opt[1,:],'b',lw=2,label='$f(x)=x/2$')
plt.plot(x,ub,'r--',label=r'Upper bound $\frac{x^2}{4}$')
plt.fill_between(x,0,ub,color='red',alpha=0.12)
plt.grid(alpha=0.4,ls=':')
plt.xlabel('x'); plt.ylabel('y')
plt.title('Upper Bound $x^2/4$ and Optimal $f(x)=x/2$')
plt.legend(loc='upper left',fontsize=8)
plt.savefig(os.path.join(FIGS,'q36.pdf'))

#if using termux
plt.savefig('../../figs/q36.pdf')
plt.savefig('../../figs/q36.png')
#subprocess.run(shlex.split("termux-open ../../figs/q36.pdf"))

#else
#plt.show() #opening the plot window
plt.show()

