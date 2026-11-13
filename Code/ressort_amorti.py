"""Système masse-ressort-amortisseur : m x'' + c x' + k x = 0
Compare les régimes sous-amorti, critique et sur-amorti (solution analytique)."""
import matplotlib.pyplot as plt
import numpy as np

m, k = 1.0, 100.0            # kg, N/m
x0, v0 = 1.0, 0.0            # conditions initiales
wn = np.sqrt(k / m)          # pulsation propre
c_crit = 2 * np.sqrt(k * m)  # amortissement critique
t = np.linspace(0, 3, 2000)


def reponse(zeta):
    if zeta < 1:    # sous-amorti
        wd = wn * np.sqrt(1 - zeta**2)
        B = (v0 + zeta * wn * x0) / wd
        return np.exp(-zeta * wn * t) * (x0 * np.cos(wd * t) + B * np.sin(wd * t))
    if zeta == 1:   # critique
        return (x0 + (v0 + wn * x0) * t) * np.exp(-wn * t)
    s = wn * np.sqrt(zeta**2 - 1)   # sur-amorti
    r1, r2 = -zeta * wn + s, -zeta * wn - s
    C2 = (v0 - r1 * x0) / (r2 - r1)
    C1 = x0 - C2
    return C1 * np.exp(r1 * t) + C2 * np.exp(r2 * t)


for zeta, nom in [(0.0, "non amorti"), (0.1, "sous-amorti"),
                  (1.0, "critique"), (2.0, "sur-amorti")]:
    plt.plot(t, reponse(zeta), label=f"ζ = {zeta} ({nom})")

plt.axhline(0, color="k", lw=0.5)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("Masse-ressort-amortisseur : effet de ζ")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
