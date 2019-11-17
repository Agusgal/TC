import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd
from SpiceParser import SpiceParser
# from sympy import *

#TEÓRICO
freq_teo = np.logspace(3, 6, 5000)
s = (1j)*2*np.pi*freq_teo

#HAY QUE CAMBIAR ESTOS VALORES Y REPETIR PARA CADA CELDA
r1 = 220*270/(220 + 270)
r2 = 47 + 1.5E3
r3 = 47E3
r4 = r2
r5 = 1.2E3 + 33E3
r6 = (56E3)*(270E3)/(56E3 + 270E3)
r7 = r3
r8 = r3
c1 = 11.5E-9
c2 = 8E-9

h1 = -1*(r6/r8)*((s**2)*(c1*c2*r1*r8*r4/r7) + s*(c2*r1*r8*r4/r2)*((1/r7) - (r2/(r3*r4))) + 1)/((s**2)*(c1*c2*r6*r1*r4/r5) + s*(c2*r6*r1*r4/(r2*r5)) + 1)
h2 = -1*(r6/r8)*((s**2)*(c1*c2*r1*r8*r4/r7) + s*(c2*r1*r8*r4/r2)*((1/r7) - (r2/(r3*r4))) + 1)/((s**2)*(c1*c2*r6*r1*r4/r5) + s*(c2*r6*r1*r4/(r2*r5)) + 1)
h3 = -1*(r6/r8)*((s**2)*(c1*c2*r1*r8*r4/r7) + s*(c2*r1*r8*r4/r2)*((1/r7) - (r2/(r3*r4))) + 1)/((s**2)*(c1*c2*r6*r1*r4/r5) + s*(c2*r6*r1*r4/(r2*r5)) + 1)
h4 = -1*(r6/r8)*((s**2)*(c1*c2*r1*r8*r4/r7) + s*(c2*r1*r8*r4/r2)*((1/r7) - (r2/(r3*r4))) + 1)/((s**2)*(c1*c2*r6*r1*r4/r5) + s*(c2*r6*r1*r4/(r2*r5)) + 1)
h5 = -1*(r6/r8)*((s**2)*(c1*c2*r1*r8*r4/r7) + s*(c2*r1*r8*r4/r2)*((1/r7) - (r2/(r3*r4))) + 1)/((s**2)*(c1*c2*r6*r1*r4/r5) + s*(c2*r6*r1*r4/(r2*r5)) + 1)
h6 = -1*(r6/r8)*((s**2)*(c1*c2*r1*r8*r4/r7) + s*(c2*r1*r8*r4/r2)*((1/r7) - (r2/(r3*r4))) + 1)/((s**2)*(c1*c2*r6*r1*r4/r5) + s*(c2*r6*r1*r4/(r2*r5)) + 1)

H = [h1, h2, h3, h4, h5, h6]

for i in range(1,7):

    #MEDICION
    df = pnd.read_csv('./FT/' + str(i) + '.csv', sep=',')
    freq_m = np.asarray(df["Frequency (Hz)"])
    mag_m = np.asarray(df["Channel 2 Magnitude (dB)"])
    pha_m = np.asarray(df["Channel 2 Phase (*)"])

    lt_parser = SpiceParser()
    data = lt_parser.parse('./FT/' + str(i) + '.txt')
    freq_s = np.array(data[1].index)
    mag_s = np.array(data[0]["V(v0" + str(i) + ") MAG"])
    pha_s = np.array(data[1]["V(v0" + str(i) + ") PHA"])

    plt.title("Bode de la etapa " + str(i) + " en módulo")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Amplitud [dB]")

    plt.plot(freq_teo, 20 * np.log10(np.abs(H[i - 1])), label="Teórico")
    plt.plot(freq_s, mag_s, label="Simulado")
    plt.plot(freq_m, mag_m, label = "Medido")

    plt.xscale('log')
    plt.legend()
    plt.grid()
    plt.show()

    # plt.title("Bode de la etapa " + str(i) + " en fase")
    # plt.xlabel("Frecuencia [Hz]")
    # plt.ylabel("Fase [°]")

    # plt.plot(freq_teo, (360 / (2 * np.pi)) * np.arctan((np.imag(H[i-1])) / (np.real(H[i-1]))), label="Teórico")
    # plt.plot(freq_s, pha_s, label = "Simulado")
    # plt.plot(freq_mt, pha_mt, label = "Medido")

    # plt.xscale('log')
    # plt.legend()
    # plt.grid()
    # plt.show()

