import sympy as sp
from sympy.utilities.lambdify import lambdify, lambdastr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

[a0, a1, a2, a3, a4, a5]= sp.symbols("a0 a1 a2 a3 a4 a5")
t = sp.Symbol('t')
ve = sp.Symbol('ve')
vs = sp.Symbol('vs')
ae = sp.Symbol('ae')
ast = sp.Symbol('ast')
js = sp.Symbol('js')
je = sp.Symbol('je')
te = sp.Symbol('te')


e1 = a5*t**5 + a4*t**4 + a3*t**3 + a2*t**2 + a1*t + a0
e2 = 5*a5*t**4 + 4*a4*t**3 + 3*a3*t**2 + 2*a2*t + a1
e3 = 20*a5*t**3 + 12*a4*t**2 + 6*a3*t + 2*a2
e4 = 60*a5*t**2 + 24*a4*t + 6*a3

eqns = [e1.subs(t, te)-ve, e2.subs(t, te)-ae, e3.subs(t, te)-je, e1.subs(t, 0)-vs, e2.subs(t, 0)-ast, e3.subs(t,0)-js]

coef_sol = sp.solve(eqns,[a0, a1, a2, a3, a4, a5])
print(coef_sol)

#find jmax
psym = 1/6 * a5 * t**6 + 1/5 * a4 * t**5 + 1/4 * a3 * t**4 + 1/3 * a2 * t**3 + 1/2 * a1 * t**2 + a0 * t
vsym = e1
asym = e2
jsym = e3
ssym = e4

for k,v in coef_sol.items():
    psym = psym.subs(k, v)
    vsym = vsym.subs(k, v)
    asym = asym.subs(k, v)
    jsym = jsym.subs(k, v)
    ssym = ssym.subs(k, v)
print(lambdastr([t, ve, vs, ae, ast, je, js, te], vsym))

pnum = lambdify([t, ve, vs, ae, ast, je, js, te], psym)
vnum = lambdify([t, ve, vs, ae, ast, je, js, te], vsym)
anum = lambdify([t, ve, vs, ae, ast, je, js, te], asym)
jnum = lambdify([t, ve, vs, ae, ast, je, js, te], jsym)
snum = lambdify([t, ve, vs, ae, ast, je, js, te], ssym)

for i in np.arange(0, 1, 0.01):
    print(vnum(i, 1, 0, 0, 0, 0, 0, 1))

veval = 1
vsval = 0
aeval = 0
asval = 0
jsval = 0
jeval = 0

fig, ax = plt.subplots()

plt.subplots_adjust(left = 0.1, bottom = 0.45)

axvs = plt.axes([0.1, 0.1, 0.8, 0.03])
axve = plt.axes([0.1, 0.15, 0.8, 0.03])
axas = plt.axes([0.1, 0.2, 0.8, 0.03])
axae = plt.axes([0.1, 0.25, 0.8, 0.03])
axjs = plt.axes([0.1, 0.3, 0.8, 0.03])
axje = plt.axes([0.1, 0.35, 0.8, 0.03])

svs = Slider(axvs, "VS", -10, 10, 0)
sve = Slider(axve, "VE", -10, 10, 0)
sas = Slider(axas, "AS", -100, 100, 0)
sae = Slider(axae, "AE", -100, 100, 0)
sjs = Slider(axjs, "JS", -1000, 1000, 0)
sje = Slider(axje, "JE", -1000, 1000, 0)

def evaluate():
    pseries = []
    vseries = []
    aseries = []
    jseries = []
    sseries = []

    te = 1
    ts = np.arange(0, te, 0.001)
    for t in ts:
        pseries.append(pnum(t, veval, vsval, aeval, asval, jeval, jsval, te))
        vseries.append(vnum(t, veval, vsval, aeval, asval, jeval, jsval, te))    
        aseries.append(anum(t, veval, vsval, aeval, asval, jeval, jsval, te))    
        jseries.append(jnum(t, veval, vsval, aeval, asval, jeval, jsval, te))    
        sseries.append(snum(t, veval, vsval, aeval, asval, jeval, jsval, te))

    return (ts, (pseries, vseries, aseries, jseries, sseries))
lp = None
lv = None
la = None
lj = None
ls = None

def update(val):
    global veval, vsval, aeval, asval, jsval, jeval
    veval = sve.val 
    vsval = svs.val
    aeval = sae.val 
    asval = sas.val
    jsval = sjs.val
    jeval = sje.val

    (t, (pseries, vseries, aseries, jseries, sseries)) = evaluate()
    print(t)
    print(vseries)
    lp.set_ydata(pseries)
    lv.set_ydata(vseries)
    la.set_ydata(aseries)
    lj.set_ydata(jseries)
    ls.set_ydata(sseries)
    ax.relim()
    ax.autoscale_view(True, True, True)

sve.on_changed(update)
svs.on_changed(update)
sae.on_changed(update)
sas.on_changed(update)
sjs.on_changed(update)
sje.on_changed(update)

(t, (pseries, vseries, aseries, jseries, sseries)) = evaluate()
lp, = ax.plot(t, pseries)
lv, = ax.plot(t, vseries)
la, = ax.plot(t, aseries)
lj, = ax.plot(t, aseries)
ls, = ax.plot(t, sseries)
plt.show()
