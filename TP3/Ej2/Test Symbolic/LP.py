import sympy as sp


vp, vm, vn, vi, vo, R, Rl, Rg, Cg, C, A0, s, wd = sp.symbols('vp vm vn vi vo R Rl Rg Cg C A0 s wd',real=True)
aom = sp.symbols('aom')

H = sp.solve([
                vp-vm,
                (vi-vp)/Rg-(vp-vn)*(s*Cg),
                vo*s*C-(vn-vo)/R,
                (vn-vo)/R-(vm-vn)/Rl-(vp-vn)*s*Cg],
                [vp, vo, vm, vn])
print(sp.latex(H[vo]))
print(sp.pretty(H[vo]))
