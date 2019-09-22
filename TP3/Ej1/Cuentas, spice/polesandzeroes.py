import numpy as np
import matplotlib.pyplot as plt

import math
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

################################variables
k=np.sqrt(2)
Q=2
R=5128.3
c2=15*10**(-9)

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
temp=0

cero_roots = np.roots([(-c6*c2*r1*r3*r4*r6*r7+c7*c2*r1*r3*r6*r7*r8), #aca poner coefs de numerador de la transferencia
                  ((c2*r1*r3*r6*r8-c2*r1*r3*r4*r7)),
                       (r4*r6*r7)])

x_cero.append(np.real(cero_roots[0])/(2*np.pi))
x_cero.append(np.real(cero_roots[1])/(2*np.pi))
y_cero.append(np.imag(cero_roots[0])/(2*np.pi))
y_cero.append(np.imag(cero_roots[1])/(2*np.pi))

pole_roots = np.roots([(c6*c2*r1*r3*r6*r7*r8+c7*c2*r1*r3*r6*r7*r8), #aca denominador
                  ((c2*r1*r3*r7*r8+c2*r1*r3*r6*r8)),
                       (r4*r6*r7)])

x_pole.append(np.real(pole_roots[0])/(2*np.pi))
x_pole.append(np.real(pole_roots[1])/(2*np.pi))
y_pole.append(np.imag(pole_roots[0])/(2*np.pi))
y_pole.append(np.imag(pole_roots[1])/(2*np.pi))

fig = plt.figure()
ax = plt.gca()

txtcero_x=x_cero[len(x_cero)-2]
txtcero_y=y_cero[len(y_cero)-2]
txtpole_x=x_pole[len(x_pole)-2]
txtpole_y=y_pole[len(y_pole)-2]

txtcero_ang=np.angle((x_cero[len(x_cero)-2])+1j*(y_cero[len(y_cero)-2]), deg=True)
txtcero_mod=np.abs((x_cero[len(x_cero)-2])+1j*(y_cero[len(y_cero)-2]))
txtpole_ang=np.angle((x_pole[len(x_pole)-2])+1j*(y_pole[len(y_pole)-2]), deg=True) - 90
txtpole_mod=np.abs((x_pole[len(x_pole)-2])+1j*(y_pole[len(y_pole)-2]))

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.text(txtcero_x+20, txtcero_y-200, '(' + str(truncate(txtcero_mod, 1)) + ' ; ' + str(truncate(txtcero_ang, 1))+ '°)' )
plt.text(txtpole_x, txtpole_y-350, '(' + str(truncate(txtpole_mod, 1)) + ' ; ' + str(truncate(txtpole_ang, 1))+ '°)' )
plt.text(txtcero_x+20, ((-1)*txtcero_y-200), '(' + str(truncate(txtcero_mod, 1)) + ' ; ' + str(truncate((-1)*txtcero_ang, 1))+ '°)' )
plt.text(txtpole_x, ((-1)*txtpole_y)-350, '(' + str(truncate(txtpole_mod, 1)) + ' ; ' + str(truncate((-1)*txtpole_ang, 1))+ '°)' )
plt.title("Polos y Ceros del Sistema")
plt.xlabel("Sigma [Rad/Hz]", x=0.7)
plt.ylabel("Omega [Hz]", x=-0.7,  y=0.2)
plt.grid()
plt.scatter((-1)*txtpole_x,0, color=[0,0,0,0])
plt.scatter(x_cero, y_cero)
plt.scatter(x_pole, y_pole, marker='x')
plt.show()

