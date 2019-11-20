import matplotlib.pyplot as plt
import numpy as np
from SpiceParser import SpiceParser

for i in range(1,7):

    lt_parser = SpiceParser()
    data = lt_parser.parse('./FT/Real-' + str(i) + '.txt')
    freq = np.array(data[1].index)
    mag = np.array(data[0]["V(fb" + str(i) + ")/V(inm" + str(i) + ") MAG"])
    pha = np.array(data[1]["V(fb" + str(i) + ")/V(inm" + str(i) + ") PHA"])

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Frecuencia [Hz]')
    ax1.set_ylabel('Ganancia [dB]', color=color)
    ax1.plot(freq, mag, label="Ganancia", color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Fase [°]', color=color)  # we already handled the x-label with ax1
    ax2.plot(freq, pha, label="Fase", linestyle='--', color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.xscale("log")
    plt.grid()
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
