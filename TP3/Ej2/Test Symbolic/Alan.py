import sympy as sp


## ingognitas y parámetros
va,vi,vb = sp.symbols("va vi vb")

h = sp.solve([
    vb-5+vi,vi-va-vb
    ],
    (vi,va)
)
#print('$V_{Out}',sp.latex((h[vout]).factor()))
print(sp.pretty(h))