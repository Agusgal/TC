import sympy as sp


vp, vm, vi, vo, rf, ri, a0, w, wp = sp.symbols('vp vm vi vo rf ri a0 w wp',real=True)
aom = sp.symbols('aom')

H = sp.solve([
                aom*(-vm)-vo,
                (a0 / (1 + (sp.I*w / wp))) - aom,
                (vi-vm)/ri-(vm-vo)/rf],
                [vm, vo,aom])
#print(sp.latex(H[0][1].factor()))
print(sp.pretty(H[0][1].factor()))
