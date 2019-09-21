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

# r1=r2=r3=r4=r8=5136.1
# r6=r7=20451.21
# c2=15*10**(-9)
# c6=3.77*10**(-9)
# c7=11.2*10**(-9)

#TRANSFERENCE
# ( ((S**2)*(-c6*c2*r1*r3*r4*r6*r7+c7*c2*r1*r3*r6*r7*r8)) + (S*(c2*r1*r3*r6*r8-c2*r1*r3*r4*r7)) + (r4*r6*r7) )
#     /
# ( ((S**2)*(c6*c2*r1*r3*r6*r7*r8+c7*c2*r1*r3*r6*r7*r8)) + (S*(c2*r1*r3*r7*r8+c2*r1*r3*r6*r8)) + (r4*r6*r7) )


cero_roots=[]
pole_roots=[]
x_cero = []
y_cero = []
x_pole = []
y_pole = []
c=[]
for i in range(10000, 10000000, 10000):
    r6 = i

    cero_roots = np.roots([(-c6*c2*r1*r3*r4*r6*r7+c7*c2*r1*r3*r6*r7*r8),
                      ((c2*r1*r3*r6*r8-c2*r1*r3*r4*r7)),
                           (r4*r6*r7)])


    x_cero.append(np.real(cero_roots[0]))
    x_cero.append(np.real(cero_roots[1]))
    y_cero.append(np.imag(cero_roots[0]))
    y_cero.append(np.imag(cero_roots[1]))

    pole_roots = np.roots([(c6*c2*r1*r3*r6*r7*r8+c7*c2*r1*r3*r6*r7*r8),
                      ((c2*r1*r3*r7*r8+c2*r1*r3*r6*r8)),
                           (r4*r6*r7)])


    x_pole.append(np.real(pole_roots[0]))
    x_pole.append(np.real(pole_roots[1]))
    y_pole.append(np.imag(pole_roots[0]))
    y_pole.append(np.imag(pole_roots[1]))



plt.xlabel("Sigma [Hz]")
plt.ylabel("Omega [Hz]")
plt.grid()
plt.scatter(x_cero, y_cero, label="ceros", cmap="plasma", c=x_cero)
plt.legend()
plt.show()


plt.xlabel("Sigma [Hz]")
plt.ylabel("Omega [Hz]")
plt.grid()
plt.scatter(x_pole, y_pole, label="polos", cmap="plasma", c=c)
plt.legend()
plt.show()

