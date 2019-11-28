import matplotlib.pyplot as plt
import numpy as np
from sympy import *

#TEÓRICO
f = symbols('f')
s = (I)*2*np.pi*f

#HAY QUE CAMBIAR ESTOS VALORES Y REPETIR PARA CADA CELDA
r1 = 33.68E3
r2 = 333.9E3
r3 = 47E3
r4 = r2
r5 = 47E3
r6 = 45E3
r7 = r3
r8 = 54.5E3
c1 = 95E-12
c2 = 95E-12

h1ceros = -1*(r6/r8)*((s**2)*(c1*c2*r1*r8*r4/r7) + s*(c2*r1*r8*r4/r2)*((1/r7) - (r2/(r3*r4))) + 1)
h1ceros = solve(h1ceros, f)
h1polos = ((s**2)*(c1*c2*r6*r1*r4/r5) + s*(c2*r6*r1*r4/(r2*r5)) + 1)
h1polos = solve(h1polos, f)
h1polos[1] = -h1polos[1]
h1ceros[1] = -h1ceros[1]

r1 = 27.027E3
r2 = 371.57E3
r3 = 47E3
r4 = r2
r5 = 52.5E3
r6 = 49.7E3
r7 = r3
r8 = 49.7E3
c1 = 100E-12
c2 = 100E-12
h2ceros = -1*(r6/r8)*((s**2)*(c1*c2*r1*r8*r4/r7) + s*(c2*r1*r8*r4/r2)*((1/r7) - (r2/(r3*r4))) + 1)
h2ceros = solve(h2ceros, f)
h2polos = ((s**2)*(c1*c2*r6*r1*r4/r5) + s*(c2*r6*r1*r4/(r2*r5)) + 1)
h2polos = solve(h2polos, f)
h2polos[1] = -h2polos[1]
h2ceros[1] = -h2ceros[1]

r1 = 27.12E3
r2 = 434.04E3
r3 = 47E3
r4 = r2
r5 = 42.08E3
r6 = 49.77E3
r7 = r3
r8 = 48E3
c1 = 100E-12
c2 = 100E-12
h3ceros = -1*(r6/r8)*((s**2)*(c1*c2*r1*r8*r4/r7) + s*(c2*r1*r8*r4/r2)*((1/r7) - (r2/(r3*r4))) + 1)
h3ceros = solve(h3ceros, f)
h3polos = ((s**2)*(c1*c2*r6*r1*r4/r5) + s*(c2*r6*r1*r4/(r2*r5)) + 1)
h3polos = solve(h3polos, f)
h3polos[1] = -h3polos[1]
h3ceros[1] = -h3ceros[1]

r1 = 10.29E3
r2 = 1.32E6
r3 = 47E3
r4 = r2
r5 = 39.44E3
r6 = 49.77E3
r7 = r3
r8 = 48E3
c1 = 92E-12
c2 = 92E-12

h4ceros = -1*(r6/r8)*((s**2)*(c1*c2*r1*r8*r4/r7) + s*(c2*r1*r8*r4/r2)*((1/r7) - (r2/(r3*r4))) + 1)
h4ceros = solve(h4ceros, f)
h4polos = ((s**2)*(c1*c2*r6*r1*r4/r5) + s*(c2*r6*r1*r4/(r2*r5)) + 1)
h4polos = solve(h4polos, f)
h4polos[1] = -h4polos[1]
h4ceros[1] = -h4ceros[1]

r1 = 10.19E3
r2 = 918.2E3
r3 = 47E3
r4 = r2
r5 = 56E3
r6 = 49.77E3
r7 = 45E3
r8 = 55E3
c1 = 88E-12
c2 = 88E-12

h5ceros = -1*(r6/r8)*((s**2)*(c1*c2*r1*r8*r4/r7) + s*(c2*r1*r8*r4/r2)*((1/r7) - (r2/(r3*r4))) + 1)
h5ceros = solve(h5ceros, f)
h5polos = ((s**2)*(c1*c2*r6*r1*r4/r5) + s*(c2*r6*r1*r4/(r2*r5)) + 1)
h5polos = solve(h5polos, f)
h5polos[1] = -h5polos[1]
h5ceros[1] = -h5ceros[1]

r1 = 27.13E3
r2 = 465.31E3
r3 = 47E3
r4 = r2
r5 = 42.08E3
r6 = 49.77E3
r7 = 46E3
r8 = 53E3
c1 = 70E-12
c2 = 70E-12

h6ceros = -1*(r6/r8)*((s**2)*(c1*c2*r1*r8*r4/r7) + s*(c2*r1*r8*r4/r2)*((1/r7) - (r2/(r3*r4))) + 1)
h6ceros = solve(h6ceros, f)
h6polos = ((s**2)*(c1*c2*r6*r1*r4/r5) + s*(c2*r6*r1*r4/(r2*r5)) + 1)
h6polos = solve(h6polos, f)
h6polos[1] = -h6polos[1]
h6ceros[1] = -h6ceros[1]

Hp = [h1polos, h2polos, h3polos, h4polos, h5polos, h6polos]
Hc = [h1ceros, h2ceros, h3ceros, h4ceros, h5ceros, h6ceros]

for counter, (polos, zeros) in enumerate(zip(Hp, Hc)):
    #print(f"polos: {polos}")
    #print(f"zeros: {zeros}")

    #plt.subplot(projection='polar')
    #plt.title(f'Diagrama de polos y ceros de la etapa {counter+1}')
    plt.xlabel("$\sigma$")
    plt.ylabel("$j\omega$")
    for p in polos:
        plt.scatter(re(p),im(p), color="blue", marker="x")
    for z in zeros:
        plt.scatter(re(z),im(z), color="red", marker="o")

plt.grid()
plt.show()