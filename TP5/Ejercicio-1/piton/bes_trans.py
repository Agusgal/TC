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

data = read_file_spice("../Spice/bessel.txt")

f = list(range(10**2, 10**5, 10))
amp1 = []
pha=[]
for ff in f:
    S = 2 * np.pi * ff * 1j

    amp1.append(
        20*np.log10(abs(

            (
                (1)/(S**6*(9.0334*10**(-27))+S**5*(8.8909*10**(-22))+S**4*(4.1690*10**(-17))+S**3*(1.1731*10**(-12))+S**2*(2.0632*10**(-8))+S*(2.1292*10**(-4))+1)
            )

        )
    ))

    pha.append(

        np.angle(

            (1)/(S**6*(9.0334*10**(-27))+S**5*(8.8909*10**(-22))+S**4*(4.1690*10**(-17))+S**3*(1.1731*10**(-12))+S**2*(2.0632*10**(-8))+S*(2.1292*10**(-4))+1)

        , deg=True)

    )

abss =[]
for abs in data["abs"]:
    abss.append(10**(abs/20))


medido_data=pandas.read_csv("AiChe_bessel.csv")
abs=[]
phase=[]
print(medido_data)
phase = np.asarray(medido_data[['Channel 2 Phase (*)']])
abs=np.asarray(medido_data[['Channel 2 Magnitude (dB)']])
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Ganancia [dB]")
plt.grid()
plt.xscale("log")
plt.plot(f, amp1, color='green', label="Calculado")
plt.plot(data["f"], data["abs"], color = 'blue', label ="Simulado")
plt.plot(medido_data[['Frequency (Hz)']], abs, color = 'red', label ="Medido")
plt.plot([0,1650,1650.01],[-3, -3, -175],color='black')
plt.plot([7850.01,7850,10**5],[3, -40, -40],color='black')
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

