import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd

#MEDICION

# df = pnd.read_csv('FiltroFinal.csv', sep=',')
# freq_mt = np.asarray(df["Frequency (Hz)"])
# mag_mt = np.asarray(df["Channel 2 Magnitude (dB)"])
# pha_mt = np.asarray(df["Channel 2 Phase (*)"])

magias = 0.8 #0.765

freq_m =[100, 700, 1.5E3, 2.6E3, 4E3, 5E3, 6E3, 7E3, 8E3, 9E3, 10E3, 10.6E3, 10.9E3, 11E3, 11.1E3, 11.2E3, 11.3E3, 11.4E3, 11.5E3, 11.6E3, 11.7E3, 11.8E3, 11.9E3, 12E3, 12.1E3, 12.2E3, 12.3E3, 12.4E3, 12.5E3, 12.6E3, 12.7E3, 12.8E3, 12.9E3, 13E3, 13.1E3, 13.15E3, 13.2E3, 13.25E3, 13.3E3, 13.5E3, 13.6E3, 13.66E3, 13.76E3, 13.85E3, 13.9E3, 14.2E3, 14.3E3, 14.35E3, 14.45E3, 14.54E3, 14.54E3, 14.6E3, 14.65E3, 14.7E3, 14.75E3, 14.8E3, 14.9E3, 14.95E3, 15E3, 15.5E3, 15.8E3, 16E3, 16.3E3, 16.5E3, 16.55E3, 16.6E3, 16.65E3, 16.7E3, 16.77E3, 16.8E3, 16.85E3, 16.9E3, 17E3, 17.1E3, 17.2E3, 17.3E3, 17.4E3, 17.5E3, 17.6E3, 17.7E3, 17.8E3, 17.9E3, 18E3, 18.1E3, 18.2E3, 18.3E3, 18.4E3, 18.5E3, 18.6E3, 18.7E3, 18.8E3, 18.9E3, 19.1E3, 19.2E3, 19.3E3, 19.5E3, 19.7E3, 20E3, 20.4E3, 20.8E3, 21.5E3, 22.3E3, 23.1E3, 24.7E3, 26.3E3, 29.1E3, 32E3, 39E3, 46E3, 54E3, 68E3, 89E3, 110E3, 140E3, 170E3, 180E3, 192E3]
mag_m = [-0.3, -0.3, -0.4, -0.4, -0.4, -0.4, -0.3, -0.2, -0.1, 0, 0, -0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.8, -1.04, -1.3, -1.7, -2.2, -2.85, -3.71, -4.9, -6.4, -8.2, -9.54, -13.15, -15.74, -19.07, -22.8, -27.2, -32.4, -39.8, -43.7, -47.4, -50.6, -52.3, -54.2, -56.43, -57, -55.88, -54.26, -53.67, -55.2, -57.7, -59.4, -63.6, -66.4, -68.1, -69.1, -68.4, -67.5, -63.6, -60.4, -61.5, -64.1, -68, -58.9, -57.4, -50.3, -47, -53, -45.4, -41.7, -38.6, -34, -31.2, -30.1, -28.4, -26.8, -23.9, -21.3, -18.9, -16.7, -14.6, -12.7, -10.8, -9.1, -7.4, -5.9, -4.5, -3.3, -2.2, -1.4, -0.8, -0.4, -0.1, 0, 0.1, 0.1, 0, -0.1, -0.15, -0.3, -0.5, -0.7, -0.9, -1.1, -1.2, -1.3, -1.4, -1.4, -1.4, -1.4, -1.4, -1.4, -1.4, -1.2, -1, -0.8, -0.6, -0.1, 0.5, 0.6, 0.9]
pha_m = [0, -5, -10, -15, -22, -30, -39.7, -50, -60, -80, -100, -130, -140, -150, -150, -162, -168.61, -176, 170, 167, 157, 151, 134.52, 121.4, 112.2, 92.4, 77.31, 67.11, 43.11, 58.77, 48, 39, 32, 22, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -26, -29, -34, -35, -39, -45, -52, -59, -67, -73, -81, -89, -97, -104, -114, -123, -133, -145, -154, -165, -175, 177, 169, 161, 152, 142, 136, 132, 122, 115, 108, 98, 90, 79, 69, 60, 50, 40, 33, 20, 10, 0, -10, -20, -35, -50, -70, -90, -93, -100]

ap = -1
aa = -45
fpmin = 11.712E3
fpmax = 19.211E3
famin = 13.802E3
famax = 16.301E3

medicion_min = 100
medicion_max = 192E3
at_max = -70

#PASANTE

#Lienas de 0 a fp- y de fp+ a Inf
plt.plot([medicion_min, fpmin], [ap, ap], color = 'red')
plt.plot([fpmax, medicion_max], [ap, ap], color = 'red')
plt.plot([fpmin, fpmin], [ap, at_max], color = 'red')
plt.plot([fpmax, fpmax], [ap, at_max], color = 'red')

#Relleno de 0 a fp- y de fp+ a Inf
plt.fill_between([medicion_min, fpmin], [at_max, at_max], facecolor='red', alpha=0.25)
plt.fill_between([medicion_min, fpmin], [ap, ap], facecolor='white', alpha=1)
plt.fill_between([fpmax, medicion_max], [at_max, at_max], facecolor='red', alpha=0.25)
plt.fill_between([fpmax, medicion_max], [ap, ap], facecolor='white', alpha=1)

#Lineas de fa- a fa+
plt.plot([famin, famax], [aa, aa], color = 'red')
plt.plot([famin, famin], [0, aa], color = 'red')
plt.plot([famax, famax], [0, aa], color = 'red')

#Relleno de fa- a fa+
plt.fill_between([famin, famax], [aa, aa], facecolor='red', alpha=0.25)

plt.title("Plantilla del filtro")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud [dB]")

plt.plot(freq_m, np.asarray(mag_m) + magias, label = "Medido")

plt.xscale('log')
plt.grid()
#plt.legend()
plt.show()

#print("f ", np.size(freq_m))
#print("p ", np.size(pha_m))

plt.title("Fase")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Diagrama de Bode en fase [°]")
plt.plot(freq_m, pha_m, label = "Medido")
plt.xscale('log')
plt.grid()
#plt.legend()
plt.show()