import numpy as np
import matplotlib.pyplot as plt


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

    data["time"] = []
    data["V(vout)"] = []
    print(lines)

    for i in range(1,len(lines)):
        pnt = 0
        c1 = ""
        c2 = ""
        while lines[i][pnt] != '\t':
            c1 += lines[i][pnt]
            pnt += 1

        while not_num(lines[i][pnt]):
            pnt += 1

        while lines[i][pnt] != '\n':
            c2 += lines[i][pnt]
            pnt += 1
        pnt += 1



        c1 = float(c1)
        c2 = float(c2)


        data["time"].append(c1)
        data["V(vout)"].append(c2)


    return data

R=9000
C=2.2*10**-9
RC=R*C
import pandas as pd
df = pd.read_csv('fresp_5.csv')

tiempo = np.asarray(df['second'])
stepResponse = np.asarray(df['Volt'])-2.5
t = np.arange(-0.1*10**-8, tiempo[len(tiempo)-1], 10**-9)
# evaluo las funciones que calcule en los puntos de t (expresion vectorial)
sr=((2/(np.sqrt(3)))*(np.exp((-2-np.sqrt(3))*t/RC)-np.exp((-2+np.sqrt(3))*t/RC))+1)*5
#sr = [(2/(np.sqrt(3)*R*C))*(np.exp()) for tt in t]
data = read_file_spice("stepResponse.txt")
tensionSpice = np.asarray(data["V(vout)"])
tiempoSpice = np.asarray(data["time"])
plt.plot(t,sr,'g',label = 'Teorico' )
plt.plot(tiempoSpice,tensionSpice,'r',label = 'Simulado' )
plt.plot(tiempo,stepResponse,'b',label = 'Medido')
plt.ylabel("Tension(V)")
plt.xlabel("Segundos (s)")
legend = plt.legend(loc='bottom right', shadow=True, fontsize='x-large')
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
plt.show()











