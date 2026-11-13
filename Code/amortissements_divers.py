"""Masse-ressort avec différents types d'amortissement :
 - visqueux       : F = -c v
 - quadratique    : F = -c2 v|v|    (traînée aérodynamique)
 - Coulomb (sec)  : F = -mu N sign(v)
 - hystérétique/structurel approché : amortissement visqueux équivalent c = η k / ω
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

m, k = 1.0, 100.0
x0, v0 = 1.0, 0.0
wn = np.sqrt(k / m)
t_eval = np.linspace(0, 10, 5000)

c_visq = 0.8
c_quad = 0.8
mu_N = 0.8          # mu * N  [N]
eta = 0.05          # facteur de perte structurel
eps = 1e-3          # régularisation de sign(v)


def visqueux(t, y):
    x, v = y
    return [v, (-k * x - c_visq * v) / m]


def quadratique(t, y):
    x, v = y
    return [v, (-k * x - c_quad * v * abs(v)) / m]


def coulomb(t, y):
    x, v = y
    return [v, (-k * x - mu_N * np.tanh(v / eps)) / m]


def structurel(t, y):
    x, v = y
    c_eq = eta * k / wn   # valable autour de la pulsation propre
    return [v, (-k * x - c_eq * v) / m]


modeles = {"visqueux": visqueux, "quadratique": quadratique,
           "Coulomb (sec)": coulomb, "structurel (équivalent)": structurel}

fig, ax = plt.subplots(1, 2, figsize=(13, 4.5))
for nom, f in modeles.items():
    s = solve_ivp(f, (0, 10), [x0, v0], t_eval=t_eval, rtol=1e-9, atol=1e-12, method="LSODA")
    ax[0].plot(t_eval, s.y[0], label=nom)
    ax[1].plot(s.y[0], s.y[1], label=nom, lw=0.8)

ax[0].set(title="Position", xlabel="t [s]", ylabel="x [m]")
ax[1].set(title="Portrait de phase", xlabel="x [m]", ylabel="v [m/s]")
for a in ax:
    a.legend()
    a.grid(alpha=0.3)
plt.tight_layout()
plt.show()
