import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd

#MEDICION

df = pnd.read_csv('FiltroFinal.csv', sep=',')
freq_mt = np.asarray(df["Frequency (Hz)"])
mag_mt = np.asarray(df["Channel 2 Magnitude (dB)"])
pha_mt = np.asarray(df["Channel 2 Phase (*)"])

plt.title("Plantilla del filtro")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud [dB]")

#PASANTE

#Lienas de 0 a fp- y de fp+ a Inf
plt.plot([1E3, 11.712E3], [-6, -6], color = 'red')
plt.plot([19.211E3, 1E6], [-6, -6], color = 'red')
plt.plot([11.712E3, 11.712E3], [-6, -90], color = 'red')
plt.plot([19.211E3, 19.211E3], [-6, -90], color = 'red')

#Relleno de 0 a fp- y de fp+ a Inf
plt.fill_between([1E3, 11.712E3], [-90, -90], facecolor='red', alpha=0.25)
plt.fill_between([1E3, 11.712E3], [-6, -6], facecolor='white', alpha=1)
plt.fill_between([19.211E3, 1E6], [-90, -90], facecolor='red', alpha=0.25)
plt.fill_between([19.211E3, 1E6], [-6, -6], facecolor='white', alpha=1)

#Lineas de fa- a fa+
plt.plot([13.802E3, 16.301E3], [-45, -45], color = 'red')
plt.plot([13.802E3, 13.802E3], [0, -45], color = 'red')
plt.plot([16.301E3, 16.301E3], [0, -45], color = 'red')

#Relleno de fa- a fa+
plt.fill_between([13.802E3, 16.301E3], [-45, -45], facecolor='red', alpha=0.25)

plt.plot(freq_mt, mag_mt, label = "Medido")
plt.xscale('log')
plt.grid()
#plt.legend()
plt.show()