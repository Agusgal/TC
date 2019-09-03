import matplotlib.pyplot as plt
import numpy as np10
import pandas as pd



med = pd.read_excel("Caso3.xlsx")
teo = pd.read_excel("Caso3Teo.xlsx")

frequencymed=[]
magmed=[]
phamed=[]
for row in range(len(med.values)):
    frequencymed.append(med.values[row][0])
    magmed.append(med.values[row][1])
    phamed.append(med.values[row][2])

frequencyteo=[]
magteo=[]
phateo=[]
for row in range(len(teo.values)):
    frequencyteo.append(teo.values[row][0])
    magteo.append(teo.values[row][1])
    phateo.append(teo.values[row][2])

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

    data["f"] = []
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
            c3 += lines[i][pnt]
            pnt += 1

        c1 = float(c1)
        c2 = float(c2)
        c3 = float(c3)

        data["f"].append(c1)
        data["abs"].append(c2)
        data["pha"].append(c3)

    return data
data = read_file_spice("Caso3enOHM.txt")
print(data["pha"])
magsim=[]
for abbs in data["abs"]:
    abbs=10**((1/20)*abbs)
    magsim.append(abbs)
phasim=[]
for phha in data["pha"]:
    phha=(-1)*phha+180
    phasim.append(phha)

plt.title("Modulo de la Impedancia de Entrada (No Inversor Caso 3)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Impedancia (Ohm)")
plt.xscale("log")
plt.grid(b=True)
plt.plot(frequencymed, magmed, label="Medido")
plt.plot(frequencyteo, magteo, label="Teorico")
plt.plot(data["f"], magsim, label="Simulado")
plt.legend()
plt.show()
plt.title("Fase de la Impedancia de Entrada (No Inversor Caso 3)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Grados (º)")
plt.xscale("log")
plt.grid(b=True)
plt.plot(frequencymed, phamed, label="Medido")
plt.plot(frequencyteo, phateo, label="Teorico")
plt.plot(data["f"], phasim, label="Simulado")
plt.legend()
plt.show()