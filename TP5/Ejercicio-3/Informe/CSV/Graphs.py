import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('BodeSedra.csv')

def not_num(content):
    if content == "0":
        return 0
    if content == "1":
        return 0
    if content == "2":
        return 0
    if content == "3":
        return 0
    if content == "4":
        return 0
    if content == "5":
        return 0
    if content == "6":
        return 0
    if content == "7":
        return 0
    if content == "8":
        return 0
    if content == "9":
        return 0
    if content == "-":
        return 0
    return 1


def read_file_spice(filename):
    file = open(filename,'r')
    lines = file.readlines()

    data = dict()

    data["f"] =   []
    data["abs"] = []
    data["pha"] = []
    #print(lines)

    for i in range(1,len(lines)):
        pnt = 0
        c1 = ""
        c2 = ""
        c3 = ""
        while lines[i][pnt] != '\t':
            c1 += lines[i][pnt]
            pnt += 1

        while not_num(lines[i][pnt]):
            pnt += 1

        while lines[i][pnt] != 'd':
            c2 += lines[i][pnt]
            pnt += 1
        pnt += 1
        while not_num(lines[i][pnt]):
            pnt += 1
        while lines[i][pnt] != '°':
#            if lines[i][pnt]>0:
                c3 += lines[i][pnt]
                pnt += 1


        c1 = float(c1)
        c2 = float(c2)
        c3 = float(c3)
 #       if(c3<360):
#            c3=c3-360

        data["f"].append(c1)
        data["abs"].append(c2)
        data["pha"].append(c3)

    return data

H = np.asarray(df['MAG'])+4
f = np.asarray(df['Frequency'])
ph = np.asarray(df['pha'])

data = read_file_spice("BodeSpice.txt")
#data = read_file_spice("Celda2.txt")
Hs = np.asarray(data["abs"])
Hsp = np.asarray(data["pha"])
fs = np.asarray(data["f"])





fc = np.arange(100,2*10**6,10)
s=fc+1e-23
Hcalc1 = np.abs((4877.97)**2-(s)**2)/np.sqrt(((s)**2-519.84*10**6)**2+(s*5466)**2)
Hcalc2 = np.abs((11139.49)**2-(s)**2)/np.sqrt(((s)**2-1.6*10**9)**2+(s*48182)**2)
Hcalc = Hcalc1 * Hcalc2
Hcalc = 20*np.log10(Hcalc)
Hphcalc1=-np.rad2deg(np.arctan(s*5466/(-(s)**2+(519.84*10**6))))
Hphcalc2=-np.rad2deg(np.arctan(s*48182/(-(s)**2+(1.6*10**9))))
Hphcalc= Hsp * 0.97# (Hphcalc2 +Hphcalc1)


fstop = np.arange(100,11.65*10**3,10)
Astop=fstop*0-40
fpass = np.arange(23.3*10**3,1*10**6,10)
Apass=fpass*0-2
plt.xscale('log')
plt.plot(fs,Hs,'r',label = 'Simulado' )
plt.plot(f,H,'y',label = 'Medido')
plt.plot(fstop,Astop,'-k')
plt.plot(fpass,Apass,'-k')
plt.plot(f,H,'y')
plt.plot(fc,Hcalc,'b',label = 'Calculado')

plt.ylabel("Transferencia Módulo [dB]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()

plt.xscale('log')
plt.plot(f,ph,'y',label = 'Medida')
plt.plot(fs,Hsp,'r',label = 'Simulada' )
plt.plot(fs,Hphcalc,'b',label = 'Calculado' )
plt.ylabel("Transferencia fase [°]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()

