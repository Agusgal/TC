import sympy as sp


# ingognitas y parámetros
vout, vp,Aom,w = sp.symbols("vout vp Aom w")
rg, cg, zg, A0, wp = sp.symbols("rg cg zg A0 wp")

eq1 = sp.Eq(vout-(((Aom)/(1+Aom))*(zg/(zg+(1/(cg*sp.I*w))))))
eq2 = sp.Eq(Aom-(A0/(1+sp.I*w/wp)))

h = sp.solve([eq1, eq2], [vout, Aom,w, cg, zg, A0, wp])

#print('$V_{Out}',sp.latex((h[vout]).factor()))
print(sp.pretty(h[vout]))
