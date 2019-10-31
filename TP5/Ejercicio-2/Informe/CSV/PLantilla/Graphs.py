import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('BodeRauch2.csv')

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
#df = pd.read_csv('BodeRauch.csv')
H = np.asarray(df['MAG'])
f = np.asarray(df['Frequency'])
ph = np.asarray(df['pha'])

data = read_file_spice("BodeSpice.txt")
#data = read_file_spice("Celda2.txt")
Hs = np.asarray(data["abs"])
Hsp = np.asarray(data["pha"])
fs = np.asarray(data["f"])
data2 = read_file_spice("BodeSpice2.txt")
Hs2 = np.asarray(data2["abs"])
Hsp2 = np.asarray(data2["pha"])
fs2 = np.asarray(data2["f"])





fc = np.arange(100,2*10**6,10)
s=fc*2*3.1415+1e-23
Hcalc1 = 74995*(s)/np.sqrt((2.7236*10**10-s**2)**2+(51101*s)**2)
Hcalc2 =  1.0449*10**5*(s)/np.sqrt((5.2722*10**10-s**2)**2+(71653*s)**2)
Hcalc = Hcalc1 * Hcalc2
Hcalc = 20*np.log10(Hcalc)
Hphcalc1=90-np.rad2deg(np.arctan(s*51101/((s)**2+(2.7236*10**10))))
Hphcalc2=90-np.rad2deg(np.arctan(s*71653/((s)**-+(5.2722*10**10))))
Hphcalc=Hsp2

fstop1 = np.arange(100,2630,10)
Astop1=fstop1*0-40
fpass = np.arange(26*10**3,29.5*10**3,10)
Apass=fpass*0-3
fstop2 = np.arange(295*10**3,1*10**6,10)
Astop2=fstop2*0-40
Verticals1=[2630,2630]
Avertical1=[-40,3]
Verticals2=[29.5*10**3,29.5*10**3]
Avertical2=[-100,-3]
Verticals3=[26*10**3,26*10**3]
Avertical3=[-100,-3]
Verticals4=[295*10**3,295*10**3]
Avertical4=[-40,3]
plt.plot(Verticals1,Avertical1,'-k')
plt.plot(Verticals2,Avertical2,'-k')
plt.plot(Verticals3,Avertical3,'-k')
plt.plot(Verticals4,Avertical4,'-k')
plt.plot(fstop2,Astop2,'-k')
plt.plot(fpass,Apass,'-k')




plt.xscale('log')
#plt.plot(fs,Hs,'r',label = 'Simulado' )
#plt.plot(fc,Hcalc,'b',label = 'Calculado' )
plt.plot(f,H,'y',label = 'Medido')
plt.plot(fstop1,Astop1,'-k')
plt.plot(f,H,'y')
#plt.plot(fc,Hcalc,'b',label = 'Calculado')

plt.ylabel("Transferencia Módulo [dB]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()

plt.xscale('log')
plt.plot(f,ph,'y',label = 'Medida')
#plt.plot(fs,Hsp,'r',label = 'Simulado' )
#plt.plot(fs2,Hphcalc,'b',label = 'Calculado')
plt.ylabel("Transferencia fase [°]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()

