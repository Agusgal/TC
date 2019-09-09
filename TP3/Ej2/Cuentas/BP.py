import sympy as sp


vp, vm, vn, vi, vo, R, R_L, R_g, C_g, C, A0, s, wd = sp.symbols('vp vm vn vi vo R R_L R_g C_g C A0 s wd',real=True)
aom = sp.symbols('aom')

H = sp.solve([
                vp-vm,
                (vm-vo)/R_L+(vi-vo)/R+(-vo)/(R_g+1/(s*C_g))-(vo)*(s*C),
                (-vp)/R_g-(vp-vo)*s*C_g],
                [vp, vo, vm])
print(sp.latex(H[vo]))
print(sp.pretty(H[vo]))
