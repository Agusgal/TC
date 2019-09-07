import sympy as sp


x, y, z = sp.symbols('x, y, z')

eq1 = x + y + z
eq2 = x + y + 2*z*z

h = sp.solve([eq1-1,eq2-3] , (x,y,z))
print(h)