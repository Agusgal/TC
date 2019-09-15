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
  #      if(c3>0):
  #          c3=c3-360

        data["f"].append(c1)
        data["abs"].append(c2)
        data["pha"].append(c3)

    return data



data = read_file_spice("L.txt")#Bode1
data1 = read_file_spice("Gyr.txt")#Bode1




plt.xscale("log")


plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Transferencia [db]')


modulo = np.asarray(data["abs"])
#modulo = 10**(np.asarray(modulo)/20)
fase = np.asarray(data["pha"])
frec = np.asarray(data["f"])
plt.plot(frec,modulo,"blue",label="Simulacion L [Ohm]")

modulo1 = np.asarray(data1["abs"])
#modulo1 = 10**(np.asarray(modulo1)/20)
fase1 = np.asarray(data1["pha"])
frec1 = np.asarray(data1["f"])
plt.plot(frec1,modulo1,"red",label="Simulación G[Ohm]")


#plt.plot(f,z,"g-o" , label="Modulo medido [Ohm]")


#ph= np.asarray(ph)*-1
#Fase inversor caso 1

#Z = 10**(np.asarray(Z)/20)
plt.title("Filtro High-Pass L vs Gyrator")
plt.grid()
plt.legend()
plt.show()

plt.xscale("log")
#plt.plot(f,ph,"g-o" , label="Gyrator medido [°]")
plt.plot(frec,fase,"blue",label="Inductancia simulada [°]")
plt.plot(frec1,fase1,"red",label="Gyrator simulado [°]")
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Transferencia [°]')
plt.grid()
plt.legend()
plt.show()