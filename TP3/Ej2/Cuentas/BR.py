import sympy as sp


vp, vm, vn, vi, vo, R, R_L, R_g, C_g, C, A0, s, wd = sp.symbols('vp vm vn vi vo R R_L R_g C_g C A0 s wd',real=True)
aom = sp.symbols('aom')

H = sp.solve([
                -(vi-vo)/R-(vn-vo)*s*C,
                s*C*(vn-vo)+vn/(R_g+1/(s*C_g))-(vm-vn)/R_L,
                vp-vm,
                (vp-vn)*(s*C_g)+vp/R_g],
                [vp, vo, vm,vn])
print(sp.latex(H[vo]))
print(sp.pretty(H[vo]))
