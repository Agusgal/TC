import numpy as np
import matplotlib.pyplot as plt

k=np.sqrt(2)
Q=2
R=25*10**3
c2=3*10**(-9)

r1=R
r1=R
r3=R
r4=R
r8=R
r6= 2*Q*R
r7 = 2*Q*R
c6=(1-(1/(k**2)))*(c2/2)
c7=(1+(1/(k**2)))*(c2/2)

print(R, r6, c6, c7)

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

data = read_file_spice()

f = list(range(10, 10**7, 100))
amp1 = []
amp2=[]
for ff in f:
    S = 2 * np.pi * ff * 1j

    amp1.append(
        20*np.log10(abs(

            (
              ( ((S**2)*(-c6*c2*r1*r3*r4*r6*r7+c7*c2*r1*r3*r6*r7*r8)) + (S*(c2*r1*r3*r6*r8-c2*r1*r3*r4*r7)) + (r4*r6*r7) )
              /
              ( ((S**2)*(c6*c2*r1*r3*r6*r7*r8+c7*c2*r1*r3*r6*r7*r8)) + (S*(c2*r1*r3*r7*r8+c2*r1*r3*r6*r8)) + (r4*r6*r7) )
            )

        )
    ))

plt.xscale("log")
plt.plot(f, amp1, color='red')
plt.show()