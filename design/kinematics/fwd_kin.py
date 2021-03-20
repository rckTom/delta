import numpy
import sympy as sp

def sphere(r, p0):
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    z = sp.Symbol('z')

    return (x-p0[0])**2 + (y-p0[1])**2 + (z-p0[2])**2 - r**2

r1 = sp.Symbol('r1', real=True, positive=True)
r2 = sp.Symbol('r2', real=True, positive=True)
r3 = sp.Symbol('r3', real=True, positive=True)

p0_1 = sp.symbols('x1 y1 z1')
p0_2 = sp.symbols('x2 y2 z2')
p0_3 = sp.symbols('x3 y3 z3')

s1 = sphere(r1, p0_1)
s2 = sphere(r2, p0_2)
s3 = sphere(r3, p0_3)

x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')

eq1 = sp.expand(s1) - sp.expand(s3)
eq2 = sp.expand(s2) - sp.expand(s3)

a11 = eq1.coeff(x, 1)
a12 = eq1.coeff(y, 1)
a13 = eq1.coeff(z, 1)

a21 = eq2.coeff(x, 1)
a22 = eq2.coeff(y, 1)
a23 = eq2.coeff(z, 1)

b1 = -eq1.coeff(x,0).coeff(y,0).coeff(z,0)
b2 = -eq2.coeff(x,0).coeff(y,0).coeff(z,0)

eq2 = sp.Symbol('a11') * x + sp.Symbol('a12') * y + sp.Symbol('a13') * z - sp.Symbol('b1')
eq3 = sp.Symbol('a21') * x + sp.Symbol('a22') * y + sp.Symbol('a23') * z - sp.Symbol('b2')

eq4 = sp.solve(eq1, z)[0]
eq5 = sp.solve(eq2, z)[0]
eq6 = eq5 - eq4
print(sp.expand(sp.solve(eq6, y)[0]).coeff(y,0))
