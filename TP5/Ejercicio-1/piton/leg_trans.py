import numpy as np
import matplotlib.pyplot as plt
import pandas

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

data = read_file_spice("../Spice/legendre.txt")

f = list(range(10**2, 10**6, 10))
amp1 = []
pha=[]
for ff in f:
    S = 2 * np.pi * ff * 1j

    amp1.append(
        20*np.log10(abs(

            (
                (-1)/(S**5*(1.2158*10**(-26))+S**4*(4.0793*10**(-21))+S**3*(1.1452*10**(-15))+S**2*(1.8235*10**(-10))+S*(1.9501*10**(-5))+1)
            )

        )
    ))

    pha.append(

        np.angle(

            (-1)/(S**5*(1.2158*10**(-26))+S**4*(4.0793*10**(-21))+S**3*(1.1452*10**(-15))+S**2*(1.8235*10**(-10))+S*(1.9501*10**(-5))+1)

        , deg=True)

    )

abss =[]
for abs in data["abs"]:
    abss.append(10**(abs/20))


medido_data=pandas.read_csv("leg.csv")
abs=[]
phase=[]
phase = np.asarray(medido_data[['Channel 2 Phase (*)']])
abs=np.asarray(medido_data[['Channel 2 Magnitude (dB)']])+1.67
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Ganancia [dB]")
plt.grid()
plt.xscale("log")
plt.plot(f, amp1, color='green', label="Calculado")
plt.plot(data["f"], data["abs"], color = 'blue', label ="Simulado")
plt.plot(medido_data[['Frequency (Hz)']], abs, color = 'red', label ="Medido")
plt.plot([0,31000,31000.01],[-3, -3, -161],color='black')
plt.legend()
plt.show()

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Fase [Grados]")
plt.grid()
plt.xscale("log")
plt.plot(f, pha, color='green', label="Calculado")
plt.plot(data["f"], data["pha"], color = 'blue', label ="Simulado")
plt.plot(medido_data[['Frequency (Hz)']], phase, color = 'red', label='Medido')
plt.legend()
plt.show()

