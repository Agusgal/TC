import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


t=np.arange(0,400*10**-6,1*10**-9)
Ve=np.sin(2*np.pi*72500*t)
Vd=np.sin(2*np.pi*72500*t)*np.exp(-t*7250)
Vp=np.sin(2*np.pi*72500*t)*np.exp(t*7250)

plt.plot(t,Ve,label = 'R2/R1=2' )
plt.ylabel("Vo [V]")
plt.xlabel("t [s]")
plt.legend()
plt.grid()
plt.show()
plt.plot(t,Vd,label = 'R2/R1<2' )
plt.ylabel("Vo [V]")
plt.xlabel("t [s]")
plt.legend()
plt.grid()
plt.show()
plt.plot(t,Vp,label = 'R2/R1>2' )

plt.ylabel("Vo [V]")
plt.xlabel("t [s]")
plt.legend()
plt.grid()
plt.show()
