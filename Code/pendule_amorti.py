"""Pendule simple amorti (non linéaire) : θ'' + γ θ' + (g/L) sin θ = 0
Compare avec le modèle linéarisé (sin θ ≈ θ) et trace le portrait de phase."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

g, L = 9.81, 1.0
t_eval = np.linspace(0, 15, 3000)


def non_lineaire(t, y, gamma):
    th, om = y
    return [om, -gamma * om - (g / L) * np.sin(th)]


def lineaire(t, y, gamma):
    th, om = y
    return [om, -gamma * om - (g / L) * th]


fig, ax = plt.subplots(1, 3, figsize=(15, 4))

# 1) Grand angle : non linéaire vs linéarisé
gamma = 0.3
y0 = [np.radians(150), 0.0]
s_nl = solve_ivp(non_lineaire, (0, 15), y0, t_eval=t_eval, args=(gamma,), rtol=1e-9)
s_li = solve_ivp(lineaire, (0, 15), y0, t_eval=t_eval, args=(gamma,), rtol=1e-9)
ax[0].plot(t_eval, np.degrees(s_nl.y[0]), label="non linéaire")
ax[0].plot(t_eval, np.degrees(s_li.y[0]), "--", label="linéarisé")
ax[0].set(title="θ0 = 150°, γ = 0.3", xlabel="t [s]", ylabel="θ [°]")
ax[0].legend()

# 2) Différents amortissements
for gam in [0.0, 0.2, 1.0, 2 * np.sqrt(g / L), 8.0]:
    s = solve_ivp(non_lineaire, (0, 15), [np.radians(60), 0], t_eval=t_eval,
                  args=(gam,), rtol=1e-9)
    ax[1].plot(t_eval, np.degrees(s.y[0]), label=f"γ = {gam:.2f}")
ax[1].set(title="Effet de l'amortissement (θ0 = 60°)", xlabel="t [s]", ylabel="θ [°]")
ax[1].legend()

# 3) Portrait de phase
for th0 in [30, 90, 150, 175]:
    s = solve_ivp(non_lineaire, (0, 30), [np.radians(th0), 0],
                  t_eval=np.linspace(0, 30, 4000), args=(0.2,), rtol=1e-9)
    ax[2].plot(s.y[0], s.y[1], label=f"θ0 = {th0}°")
ax[2].set(title="Portrait de phase (γ = 0.2)", xlabel="θ [rad]", ylabel="θ' [rad/s]")
ax[2].legend()

for a in ax:
    a.grid(alpha=0.3)
plt.tight_layout()
plt.show()
