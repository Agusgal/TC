import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd
# from SpiceParser import SpiceParser
# from sympy import *

for i in range(1,7):
    #MEDICION
    df = pnd.read_csv('./FT/' + str(i) + '.csv', sep=',')
    freq_mt = np.asarray(df["Frequency (Hz)"])
    mag_mt = np.asarray(df["Channel 2 Magnitude (dB)"])
    pha_mt = np.asarray(df["Channel 2 Phase (*)"])

    plt.title("Bode de la etapa " + str(i) + " en módulo")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Amplitud [dB]")
    plt.plot(freq_mt, mag_mt, label = "Medido")
    plt.xscale('log')
    #plt.legend()
    plt.grid()
    plt.show()

    # plt.title("Bode de la etapa " + str(i) + " en fase")
    # plt.xlabel("Frecuencia [Hz]")
    # plt.ylabel("Fase [°]")
    # plt.semilogx(freq_mt, pha_mt, label = "Medido")
    # #plt.legend()
    # plt.grid()
    # plt.show()

