import sympy as sp


vp, vm, vn, vi, vo, R, Rl, Rg, Cg, C, A0, s, wd = sp.symbols('vp vm vn vi vo R Rl Rg Cg C A0 s wd',real=True)
aom = sp.symbols('aom')

H = sp.solve([
                vp-vm,
                (-vp)/Rg-(vp-vo)*(s*Cg),
                (vo-vi)/(R+1/(s*C))-(vp-vo)/(Rl)-(vp-vo)*(s*Cg)],
                [vp, vo, vm])
print(sp.latex(H[vo]))
print(sp.pretty(H[vo]))
