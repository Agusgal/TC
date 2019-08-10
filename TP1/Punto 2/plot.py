import matplotlib.pyplot as plt
import numpy as np


f0 = 24*10**3
R = 660
C = 5.1*10**(-9)
print("Cuantos puntos desea?")
puntos = input()
Xn = []
Yn = []
Fn=[]
for i in range(0, int(puntos)):
    Xn.append(10/((2*i+1)*np.pi))
    Yn.append(10/np.sqrt((2*np.pi**2*f0*(2*i+1)**2*R*C)**2+(2*i+1)**2*np.pi**2))
    Fn.append(f0*(2*i+1))
plt.xlabel('Frecuencia')
plt.ylabel('Magnitud de la componente')
markerline, stemlines, baseline = plt.stem(Fn, Xn, '-', markerfmt='go',linefmt='green',label="Entrada")

markerline2, stemlines2, baseline2 = plt.stem(Fn, Yn, '*', markerfmt='ro',linefmt='red',label = "Salida")
plt.legend()
plt.show()

