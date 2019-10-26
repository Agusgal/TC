import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


fc = np.arange(100,2*10**6,10)
s=fc*2*np.pi
Hcalc1 = np.abs(124088460.2-(s)**2)/np.sqrt(((s)**2-519.84*10**6)**2+(s*5466)**2)
Hcalc2 = np.abs(23794591.32-(s)**2)/np.sqrt(((s)**2-1.6*10**9)**2+(s*48182)**2)
Hcalc = Hcalc1 * Hcalc2
Hcalc = 20*np.log10(Hcalc)
Hphcalc1=-np.rad2deg(np.arctan(5466*s/(519.84*10**6-s**2)))
Hphcalc2=-np.rad2deg(np.arctan(48182*s/(1.6*10**9-s**2)))
Hphcalc=Hphcalc1+Hphcalc2


plt.xscale('log')

plt.plot(fc,Hcalc,'b',label = 'Transferencia Calculada')
plt.ylabel("Transferencia Módulo [dB]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()

plt.xscale('log')
plt.plot(fc,Hphcalc,'b',label = 'Transferencia Calculada')


plt.ylabel("Transferencia fase [°]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()









