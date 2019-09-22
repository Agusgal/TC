import numpy as np
import matplotlib.pyplot as plt

f = list(range(10**1, 10**8, 100))
v=[]
v_sat = 10.7
for ff in f:

    v_slew=(2.01*10**6)/ff

    if(v_slew < v_sat):
        v.append(v_slew)
    else:
        v.append(v_sat)

plt.title("Tensión de Entrada Máxima del Circuito")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Vin Max [V]")
plt.grid()
plt.xscale("log")
plt.plot(f, v, color='orange')
plt.show()

