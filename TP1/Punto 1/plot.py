import matplotlib.pyplot as plt
import numpy as np

#constantes
f0 = 24*10**3
R = 9*10**3
C = 2.2*10**(-9)
#Solo transferencia
plt.xscale("log")
#aca hayq ue poner la tabla de mediciones
k=1000
fmodmed=[1*k,2*k,2.6*k,3*k,3.5*k,4*k,6*k,7*k,7.5*k,7.8*k,8*k,8.1*k,8.23*k,8.38*k,8.51*k,8.75*k,9.6*k,12.5*k,17.5*k,25.5*k,33.5*k,55.5*k,100*k,400*k]
modmed=[-0.9,-3.1,-4.7,-5.8,-7.2,-8.7,-15.9,-21.6,-26.2,-30.1,-33.6,-35.3,-36.4,-35.1,-33,-29.4,-22.1,-13.5,-8.4,-5,-3.4,-1.5,-0.6,-0.1]
ffaseMed=[100,500,1*k,2*k,2.6*k,3*k,3.5*k,4*k,6*k,7*k,7.5*k,7.8*k,8*k,8.1*k,8.23*k,8.38*k,8.51*k,8.75*k,9.6*k,12.5*k,17.5*k,25.5*k,33.5*k,55.5*k,100*k,400*k]
faseMed=[-3,-14,-27,-45,-54,-57,-63,-68,-76,-75,-69,-60,-42,-27,0,30,45,62,75,75,64,53,45,30,15,2]

#f = np.arange(fmodmed[0],fmodmed[len(fmodmed)-1], (fmodmed[len(fmodmed)-1]-fmodmed[0])/100)
f = np.arange(fmodmed[0],fmodmed[len(fmodmed)-1], 100)
Hs = [ (np.abs(-(2*np.pi*ff)**2+(1/(C*R))**2)/np.sqrt(((-(2*np.pi*ff)**2+(1/(C*R))**2))**2+(4*2*np.pi*ff/(C*R))**2)) for ff in f]
Hs = 20*np.log10(Hs)
plt.title("Comparacion de Modulos")
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Transferencia modulo')
plt.plot(fmodmed,modmed,"bo-" , label="Transferencia Medida [dB]")
plt.plot(f,Hs,"red" , label="Transferencia Teorica [dB]")
plt.legend()
plt.show()
#Solo transferencia fase
plt.xscale("log")
#aca hayq ue poner la tabla de mediciones

fs = np.arange(1*k, 302.32*k,1000 )
Hf = [ - np.arctan((8*np.pi*tt/(C*R))/((1/(C*R)**2 - (4*np.pi**2*tt**2))))*180/(np.pi) for tt in fs]

plt.title("Comparacion de Fases")
plt.xlabel('Frecuencia[Hz]')
plt.ylabel('Transferencia Fase')
plt.plot(ffaseMed,faseMed,'bo--',"blue" , label="Fase Medida [°]")
plt.plot(fs,Hf,"red" , label="Transferencia [°]")
plt.legend()
plt.show()

