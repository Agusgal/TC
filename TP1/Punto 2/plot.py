import matplotlib.pyplot as plt
import numpy as np

#constantes
f0 = 24*10**3
R = 705
C = 4.7*10**(-9)
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
t = np.arange(Fn[0]-Fn[0]/2,  10**6, (Fn[len(Fn)-1]-Fn[0])/1000)
#t = np.arange(1,  10**6, 10)
Hs = [1/np.sqrt((((R*C*tt*2*np.pi)**2)+1)) for tt in t]
Hs = 20*np.log10(Hs)
plt.title("Armonicos vs Transferencia")
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud de la componente/Transferencia')
plt.plot(t,Hs,"red" , label="Transferencia Teorica [dB]")
plt.legend()
plt.show()
#Solo transferencia
plt.xscale("log")
#aca hayq ue poner la tabla de mediciones
k=1000
fmed=[1*k,2*k,4.8*k,28.56*k,52.32*k,76.08*k,99.84*k,123.6*k,147.36*k,171.12*k,194.88*k,218.64*k,242.4*k,266.16*k,289.92*k,313.68*k,337.44*k,361.2*k,384.96*k,408.72*k,432.48*k,456.24*k]#,480*k,4800*k]
modmed=[-0.1,-0.1,-0.1,-1.8,-3.8,-4.5,-6.4,-8.2,-9.6,-10.9,-12,-12.9,-13.8,-14.6,-15.4,-16,-16.7,-17.2,-17.8,-18.7,-19.3,-19.6]#,-20,-30]
t = np.arange(fmed[0],fmed[len(fmed)-1], (fmed[len(fmed)-1]-fmed[0])/100)
Hs = [1/np.sqrt((((R*C*tt*2*np.pi)**2)+1)) for tt in t]
Hs = 20*np.log10(Hs)
plt.title("Comparacion de Modulos")
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Transferencia modulo')
plt.plot(fmed,modmed,"blue" , label="Transferencia Medida [dB]")
plt.plot(t,Hs,"red" , label="Transferencia Teorica [dB]")
plt.legend()
plt.show()
#Solo transferencia fase
plt.xscale("log")
#aca hayq ue poner la tabla de mediciones

fMed=[1*k,2*k,4.8*k,7.32*k,14.32*k,20.32*k,32.32*k,48.32*k,59.32*k,83.32*k,125.32*k,302.32*k]

faseMed=[-1,-3,-7,-11,-18,-25,-35,-46,-52,-60,-68,-72]
t = np.arange(1*k, 302.32*k,(301.32*k)/1000 )
Hf = [np.arctan(-tt*2*np.pi*R*C)*180/(np.pi) for tt in t]
plt.title("Comparacion de Fases")
plt.xlabel('Frecuencia[Hz]')
plt.ylabel('Transferencia Fase')
plt.plot(fMed,faseMed,"blue" , label="Transferencia Medida [°]")
plt.plot(t,Hf,"red" , label="Transferencia [°]")
plt.legend()
plt.show()

