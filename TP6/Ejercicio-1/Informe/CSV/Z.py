import numpy as np
import matplotlib.pyplot as plt
import random


class CNum:
    def __init__(self, mod, phi,color, type):
        self.mod = mod
        self.phi = phi
        self.type = type
        self.color = color
#        self.color = '#' +"%06x" % random.randint(0, 0xFFFFFF)

    def graph(self):
#        plt.yticks([10000,20000,27692, 40000 ,50182,72500,91932])
        plt.thetagrids(range(0,360,30))
#        plt.polar([np.deg2rad(self.phi), 0], [self.mod, 0], c=self.color)
        if(self.type == "Pole"):
            plt.scatter(np.deg2rad(self.phi), self.mod, c=self.color, marker = "x")
        else:
            plt.scatter(np.deg2rad(self.phi), self.mod, c=self.color, marker="o")
#        plt.plot(np.deg2rad(self.phi), self.mod, color=self.color)
#        plt.legend()



def ej1(arrayOfSignals):
    plt.title("Diagrama de polos y ceros")
    for x in arrayOfSignals:
        x.graph()

    plt.show()


def ej2(S):
    S.graph()
    fq = -90
    fp = 0
    if S.phi > 0:
        fq = 90
    if S.phi > 90 or S.phi < -90:
        fp = 180
    Q = CNum(abs(S.mod * np.sin(np.deg2rad(S.phi))), fq,'Potencia Reactiva')
    P = CNum(abs(S.mod * np.cos(np.deg2rad(S.phi))), fp,'Potencia Activa')
    Q.graph()
    P.graph()
    plt.title("Diagrama fasorial de potencias")
    plt.show()


ax = plt.subplot(111, polar=True)
#P1 = CNum(27692.5358, 180, 'blue',"Pole")
#P1c = CNum(189807.46,180, 'blue',"Pole")
P2 = CNum(72499, 75.52, 'blue',"Pole")
P2c = CNum(72500,-75.52, 'blue',"Pole")
Z1 = CNum(27692.53582, 180, 'red',"Zero")
Z1c = CNum(1.898074642*10**5,180 , 'red',"Zero")
#Z2 = CNum(11139, 90, 'red',"Zero")
#Z2c = CNum(11139, -90, 'red',"Zero")
ej1([Z1c,Z1,P2,P2c])

#ej2(Z7)
#ej2(Z8)
#ej2(Z9)



