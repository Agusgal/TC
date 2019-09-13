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
        if(c3>0):
            c3=c3-360

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

#IMPEDANCIA DE ENTRADA gyrator
#f = [100  ,250 ,500 ,750  ,1000,1250 ,1500 ,2000 ,2500  ,3000 ,3500,4000 ,5000,6000 ,7000 ,8000 ,9000 ,10000,15000,17000,20000,25000,30000,35000,40000,42000,43500,45000,47000,50000,51000,53000,55000,56000,57000,58000,60000,65000,70000 ,80000 ,90000 ,100000,110000,120000,130000,150000,200000 ,300000,400000,500000,750000,1000000]
#z = [47.6 ,49.4,55  ,63.18,73  ,84   ,95.57,120.1,145.7 ,171.5,198 ,224.5,278 ,332.7 ,387.8,443.5,500  ,557  ,858  ,983  ,1194 ,1596 ,2071,2657 ,3391 ,3734 ,4024 ,4310 ,4700 ,5310 ,5499 ,5839 ,6100 ,6190 ,6261 ,6297 ,6271 ,5834 ,5154  ,3935  ,3126  ,2589  ,2224  ,1951  ,1745  ,1450  ,1039   ,706   ,563   ,486   ,400   ,366]
#ph =[6.71 ,16.2,30  ,40.76,48.7,54.67,59.2 ,65.5 ,69.55 ,72.3 ,74.3,75.8 ,77.7,78.89,79.5 ,80.01,80.32,80.43,79.93,79.42,77.97,75.42,71.63,66.67,59.6 ,56   ,53   ,50   ,44.86,36.15,32.87,25.91,18.39,14.6 ,10.8 ,6.94 ,-0.37,-16.9,-29.54,-44.62,-52.63,-57   ,-59.67,-61.31,-62.23,-63.1 ,-61.9  ,-56.17,-49.79,-43.96,-32.33,-24]
#ph=np.asarray(ph) -180

#plt.plot(f,z,"g-o" , label="Modulo medido [Ohm]")


#ph= np.asarray(ph)*-1
#Fase inversor caso 1

#Z = 10**(np.asarray(Z)/20)
plt.title("Filtro Low-Pass L vs Gyrator")
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