import numpy as np

# 1. Définition de la matrice A
A = np.array([
    [2, -1, 0],
    [-1, 2, -1],
    [0, -1, 2]
])
# A = np.array([
#     [2, -1],
#     [-1/2, 2]
# ])

# 2. Calcul et tri des valeurs propres (ω²)
valeurs_propres = np.linalg.eigvalsh(A)
omega_carres = np.sort(valeurs_propres)

# 3. Calcul des pulsations simples ω (racine carrée)
omegas = np.sqrt(omega_carres)

# 4. Définition de votre référence W0² (à ajuster selon votre énoncé)
w0_carre = 1.0  
w0 = np.sqrt(w0_carre)

print("=== TOUS LES MODES PROPRES CALCULÉS ===")

# Affichage des résultats pour les 3 modes
for i in range(3):
    print(f"\n--- MODE {i+1} ---")
    print(f"Carré de la pulsation : ω_{i+1}² = {omega_carres[i]:.4f}")
    print(f"Pulsation simple       : ω_{i+1}  = {omegas[i]:.4f}")
    print(f"Rapport de mode        : W{i+1}² / W0² = {omega_carres[i] / w0_carre:.4f}")

