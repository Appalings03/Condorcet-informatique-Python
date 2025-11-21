import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import fmin

# Données expérimentales
I = np.array([0.00, 0.07, 0.73, 1.43, 3.41, 6.01, 7.32, 7.59, 7.68, 7.77, 7.81, 7.88, 7.91, 7.92])
U = np.array([745, 744, 736, 729, 696, 615, 460, 331, 258, 187, 151, 98.6, 67.6, 46.4])

# Puissance P = V * I (en µW car V en mV, I en mA)
P = U * I

# Domaine fin pour l'interpolation
I_fine = np.linspace(0, 8, 1000)

# === 1. Graphe brut des 14 points de puissance ===
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(I, P, 'ko', markersize=8, label='Données mesurées (14 points)')
plt.plot(I, P, 'k--', alpha=0.5, linewidth=1)
plt.title('Puissance $P = V \\times I$ en fonction du courant $I$ (données brutes)')
plt.xlabel('Courant $I$ (mA)')
plt.ylabel('Puissance $P$ (µW)')
plt.grid(True, alpha=0.5)
plt.legend()

# === 2. Interpolation : linéaire et spline cubique ===
# Fonction de puissance interpolée
interp_linear = interp1d(I, P, kind='linear')
interp_spline = interp1d(I, P, kind='cubic')

P_linear = interp_linear(I_fine)
P_spline = interp_spline(I_fine)

# === 3. Recherche du maximum avec fmin ===
# Fonction objectif : -P (car fmin minimise)
def neg_power_linear(x):
    return -interp_linear(x)

def neg_power_spline(x):
    return -interp_spline(x)

# Estimation initiale (près du pic visuel ~7.7 mA)
x0 = 7.0

I_max_linear = fmin(neg_power_linear, x0, disp=False)[0]
P_max_linear = interp_linear(I_max_linear)

I_max_spline = fmin(neg_power_spline, x0, disp=False)[0]
P_max_spline = interp_spline(I_max_spline)

# === Affichage des courbes interpolées + maxima ===
plt.subplot(2, 1, 2)
plt.plot(I, P, 'ko', markersize=8, label='Données mesurées', zorder=5)
plt.plot(I_fine, P_linear, 'b-', linewidth=2, label='Interpolation linéaire')
plt.plot(I_fine, P_spline, 'r-', linewidth=2, label='Interpolation spline cubique')

# Marquer les maxima
plt.plot(I_max_linear, P_max_linear, 'bs', markersize=12, markeredgecolor='k', label=f'Max linéaire: $P_{{max}} = {P_max_linear:.1f}$ µW')
plt.plot(I_max_spline, P_max_spline, 'r^', markersize=12, markeredgecolor='k', label=f'Max spline: $P_{{max}} = {P_max_spline:.1f}$ µW')

plt.title('Interpolation et localisation du maximum de puissance')
plt.xlabel('Courant $I$ (mA)')
plt.ylabel('Puissance $P$ (µW)')
plt.grid(True, alpha=0.5)
plt.legend(fontsize=10)
plt.xlim(0, 8)
plt.ylim(0, 2200)

plt.tight_layout()
plt.show()

# === Résultats numériques ===
print("=== RÉSULTATS FINAUX ===")
print(f"Interpolation LINÉAIRE :")
print(f"   I_max = {I_max_linear:.3f} mA")
print(f"   P_max = {P_max_linear:.1f} µW")
print()
print(f"Interpolation SPLINE CUBIQUE :")
print(f"   I_max = {I_max_spline:.3f} mA")
print(f"   P_max = {P_max_spline:.1f} µW")