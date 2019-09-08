import sympy as sp


vp, vm, vi, vo, Zg, Rg, Cg, A0, s, wd = sp.symbols('vp vm vi vo Zg Rg Cg A0 s wd',real=True)
aom = sp.symbols('aom')

H = sp.solve([
                vo-vm,
                aom*(vp-vm)-vo,
                (A0 / (1 + (s / wd))) - aom,
                vi*(Zg/(Zg+1/(s*Cg)))-vp],
                [vm, vo,aom,vp])
print(sp.latex(H[0][1]))
print(sp.pretty(H[0][1]))
