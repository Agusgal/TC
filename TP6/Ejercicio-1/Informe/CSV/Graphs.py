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

        while lines[i][pnt] != '\t':
            c2 += lines[i][pnt]
            pnt += 1
        pnt += 1
        while not_num(lines[i][pnt]):
            pnt += 1
        while lines[i][pnt] != '\n':
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




JF1 = read_file_spice("CurvaJfet1.txt")
Vds1 = np.asarray(JF1["abs"])
Id1 = np.asarray(JF1["pha"])*1000

JF2 = read_file_spice("CurvaJfet2.txt")
Vds2 = np.asarray(JF2["abs"])
Id2 = np.asarray(JF2["pha"])*1000

JF3 = read_file_spice("CurvaJfet3.txt")
Vds3 = np.asarray(JF3["abs"])
Id3= np.asarray(JF3["pha"])*1000

JF4 = read_file_spice("CurvaJfet4.txt")
Vds4 = np.asarray(JF4["abs"])
Id4 = np.asarray(JF4["pha"])*1000

JF5 = read_file_spice("CurvaJfet5.txt")
Vds5 = np.asarray(JF5["abs"])
Id5 = np.asarray(JF5["pha"])*1000

JF6 = read_file_spice("CurvaJfet6.txt")
Vds6 = np.asarray(JF6["abs"])
Id6 = np.asarray(JF6["pha"])*1000

JF7 = read_file_spice("CurvaJfet7.txt")
Vds7 = np.asarray(JF7["abs"])
Id7= np.asarray(JF7["pha"])*1000


JF8 = read_file_spice("CurvaJfet8.txt")
Vds8 = np.asarray(JF8["abs"])
Id8 = np.asarray(JF8["pha"])*1000








plt.plot(Vds1,Id1,label = 'Vgs=-3' )
plt.plot(Vds2,Id2,label = 'Vgs=-2.5' )
plt.plot(Vds3,Id3,label = 'Vgs=-2' )
plt.plot(Vds4,Id4,label = 'Vgs=-1.5' )
plt.plot(Vds5,Id5,label = 'Vgs=-1' )
plt.plot(Vds6,Id6,label = 'Vgs=-0.5' )
plt.plot(Vds7,Id7,label = 'Vgs=0' )
plt.plot(Vds8,Id8,label = 'Vgs=0.5' )

plt.ylabel("Ids [mA]")
plt.xlabel("Vds [V]")
plt.legend()
plt.grid()
plt.show()
