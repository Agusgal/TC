import matplotlib.pyplot as plt
import numpy as np

#constantes
f0 = 24*10**3
R = 660
C = 5.1*10**(-9)
#input de ususario
print("Cuantos puntos desea?")
puntos = input()
print("Frecuencia de la entrada?")
f1 = input()
if f1 != '':
    f0=int(f1)
#calculo de coeficientes
Xn = []
Yn = []
Fn = []
for i in range(0, int(puntos)):
    Xn.append(10/((2*i+1)*np.pi))
    Yn.append(10/np.sqrt((2*np.pi**2*f0*(2*i+1)**2*R*C)**2+(2*i+1)**2*np.pi**2))
    Fn.append(f0*(2*i+1))
#comparacion entrada salida
plt.title("Comparacion de Armonicos")
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud de la componente')
plt.stem(Fn, Xn, '-', markerfmt='go',linefmt='green',label="Entrada")
plt.stem(Fn, Yn, '*', markerfmt='ro',linefmt='red',label = "Salida")
plt.legend()
plt.show()
#Comparacion entrada salido con respuesta en frecuencia
plt.xscale("log")
plt.stem(Fn, Xn, '-', markerfmt='go',linefmt='green',label="Entrada")
plt.stem(Fn, Yn, '*', markerfmt='ro',linefmt='red',label = "Salida")
t = np.arange(Fn[0]-Fn[0]/5, Fn[len(Fn)-1] if Fn[len(Fn)-1]>10**6 else 10**6, (Fn[len(Fn)-1]-Fn[0])/len(Fn))
Hs = [1/np.sqrt(((R*C*tt)**2+1)) for tt in t]
Hs = 20*np.log(Hs)
plt.title("Armonicos vs Transferencia")
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud de la componente/Transferencia')
plt.plot(t,Hs,"red" , label="Transferencia Teorica [dB]")
plt.legend()
plt.show()
#Solo transferencia
plt.xscale("log")
#aca hayq ue poner la tabla de mediciones
fmed=[]
modmed=[]
t = np.arange(Fn[0]-Fn[0]/5, Fn[len(Fn)-1] if Fn[len(Fn)-1]>10**6 else 10**6, (Fn[len(Fn)-1]-Fn[0])/len(Fn))
Hs = [1/np.sqrt(((R*C*tt)**2+1)) for tt in t]
Hs = 20*np.log(Hs)
plt.title("Comparacion de Modulos")
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Transferencia modulo')
plt.plot(t,Hs,"red" , label="Transferencia [dB]")
plt.legend()
plt.show()
#Solo transferencia fase
plt.xscale("linear")
#aca hayq ue poner la tabla de mediciones
fMed=[]
faseMed=[]
t = np.arange((1/(R*C*2*np.pi))-10, (1/(R*C*2*np.pi))+10,1/100 )
Hf = [-np.arctan(tt-(1/(R*C*2*np.pi)))*180/(np.pi) for tt in t]
plt.title("Comparacion de Fases")
plt.xlabel('Frecuencia[Hz]')
plt.ylabel('Transferencia Fase')
plt.plot(t,Hf,"red" , label="Transferencia [°]")
plt.legend()
plt.show()

