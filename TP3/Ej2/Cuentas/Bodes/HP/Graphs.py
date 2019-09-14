import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#df = pd.read_csv('')

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

#H = np.asarray(df['CH1'])
#f = np.asarray(df['CH1'])
#ph = np.asarray(df['CH1'])

data = read_file_spice("Gyr.txt")
HGy = np.asarray(data["abs"])
HGyp = np.asarray(data["pha"])
fGy = np.asarray(data["f"])


L = 10*10**(-3)
C = 68*10**(-9)
rc = 51
R = 750

R2 = 9*10**3
C2 = 2.2*10**(-9)
print(L,C,R,rc)
fc = np.arange(100,2*10**6,10)
s=2*np.pi*fc
Hcalc = (np.sqrt(((s/38348.24)**4+(s/(288350.6))**2)/((s*5.4468*10**-5)**2+(1-(s/38348.24)**2)**2)))
Hcalc = 20*np.log10(Hcalc)


#Hphcalc = [np.arctan(-tt*2*np.pi*2.60768*10**-5)*180/(np.pi) for tt in fc]

#Hphcalc = np.rad2deg(np.arctan((s/(288350.6))/((s/38348.24)**2))-np.arctan((s*5.4468*10**-5)/(1-(s/38348.24)**2)))
#Hphcalc = np.rad2deg() #np.arctan((s*3.468*10**-6)/((-s/38348.24)**2))
#Hphcalc =np.asarray(Hphcalc)*2+180
Hphcalc=np.rad2deg(np.arctan(-rc/(s*L)))-np.rad2deg(np.arctan(s*(rc+R)*C/(-(s**2)*L*C+1)))
#Hphcalc = [if Hphcalc[i] <50:Hphcalc[i]=Hphcalc[i]+360 for i in len(hphcalc)]
for x in range(len(Hphcalc)):
    if(Hphcalc[x] <-50):
        Hphcalc[x]=Hphcalc[x]+180

data2 = read_file_spice("L.txt")
HL = np.asarray(data2["abs"])
HLp = np.asarray(data2["pha"])
fL = np.asarray(data2["f"])
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
#plt.plot(f,ph,'b',label = 'Gyrator Medido')
plt.plot(fc,Hphcalc,'b',label = 'Gyrator Calculado')
plt.plot(fGy,HGyp,'r',label = 'Gyrator Simulado' )
plt.plot(fL,HLp,'g',label = 'Inductor Simulado' )

plt.ylabel("Transferencia fase [°]")
plt.xlabel("Frecuencia [Hz]")
plt.legend()
plt.grid()
plt.show()









