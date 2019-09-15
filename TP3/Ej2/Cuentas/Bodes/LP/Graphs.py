import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


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
        if(c3>0):
            c3=c3-360

        data["f"].append(c1)
        data["abs"].append(c2)
        data["pha"].append(c3)

    return data


#df = pd.read_csv('')

#H = np.asarray(df['CH1'])
#f = np.asarray(df['CH1'])
#ph = np.asarray(df['CH1'])

data = read_file_spice("Gyr.txt")
HGy = np.asarray(data["abs"])
HGyp = np.asarray(data["pha"])
fGy = np.asarray(data["f"])


data2 = read_file_spice("L.txt")
HL = np.asarray(data2["abs"])
HLp = np.asarray(data2["pha"])
fL = np.asarray(data2["f"])


fc = np.arange(100,2*10**6,10)
s=2*np.pi*fc
Hcalc = (1/np.sqrt(((s*0.0001448)**2+(1-((s)**2)*8*10**(-9))**2)))
Hcalc = 20*np.log10(Hcalc)

Hphcalc = [np.arctan(-tt*2*np.pi*np.sqrt(8*10**(-9)))*180/(np.pi) for tt in fc]
Hphcalc =np.asarray(Hphcalc)*2


plt.xscale('log')
plt.plot(fGy,HGy,'r',label = 'Gyrator Simulado' )
plt.plot(fL,HL,'g',label = 'Inductor Simulado' )
#plt.plot(f,H,'y',label = 'Gyrator Medido')
plt.plot(fc,Hcalc,'b',label = 'Gyrator Calculado')
plt.ylabel("Transferencia Módulo [dB]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()

plt.xscale('log')
plt.plot(fGy,HGyp,'r',label = 'Gyrator Simulado' )
plt.plot(fL,HLp,'g',label = 'Inductor Simulado' )
#plt.plot(f,ph,'b',label = 'Gyrator Medido')
plt.plot(fc,Hphcalc,'y',label = 'Gyrator Calculado')
plt.ylabel("Transferencia fase [°]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()









