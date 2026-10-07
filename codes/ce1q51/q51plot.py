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

#Q51 : spring force versus temperature rise
Ar, E, L, alpha = 500, 60e3, 3000, 12e-6      # mm^2, N/mm^2, mm, 1/degC
k_r = Ar*E/L                                  # rod stiffness (1.1.13.1)
k_s = 2500                                    # spring stiffness N/mm

F = lambda dT: L*alpha*dT/(1/k_r + 1/k_s)/1e3 # kN, from (1.1.14.1) and series relation

A0 = np.array([[0],[F(0)]]);  B0 = np.array([[120],[F(120)]])
x_F = line_gen_num(A0,B0,100)

plt.figure(figsize=(7,5))
plt.plot(x_F[0,:],x_F[1,:],'b',lw=2)
plt.plot(100,F(100),'ro',label='At $\\Delta T=100^\\circ$C: $F_{BC}=%.1f$ kN'%F(100))
plt.grid(alpha=0.4,ls=':')
plt.xlabel('Temperature Rise $\\Delta T$ ($^\\circ$C)')
plt.ylabel('Spring Force $F_{BC}$ (kN)')
plt.title('Spring Force vs. Temperature Rise of Rod AB')
plt.legend(loc='upper left',fontsize=8)
plt.savefig(os.path.join(FIGS,'q51.pdf'))
plt.show()


#if using termux
plt.savefig('../../figs/q51.pdf')
plt.savefig('../../figs/q51.png')
#subprocess.run(shlex.split("termux-open ../../figs/q51.pdf"))

#plt.savefig('../../figs/q51.pdf')
#plt.savefig('../../figs/q51.eps')
#subprocess.run(shlex.split("termux-open ../../figs/q51.pdf"))
#else
#plt.show() #opening the plot window


