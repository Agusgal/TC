import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv('no_osc0.csv')
plt.title("Respuesta al Escalón")
Vin = np.asarray(df['1'])
Vout = np.asarray(df['3'])
t= np.asarray(df['x-axis'])
plt.plot(t,Vin,'r',label = 'Entrada' )
plt.plot(t,Vout,'g',label = 'Salida' )
plt.legend()
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo [s]")
plt.grid()
plt.show()
