import numpy as np

# Variables : G (gyros), F (frite), B (boisson)
# Système :
# 8G + 10F + 6B = 43
# 0G +  2F + 2B = 9
# 1G +  0F + 1B = 4.5

A = np.array([
    [8, 10, 6],
    [0,  2, 2],
    [1,  0, 1]
])

b = np.array([43, 9, 4.5])

# Résolution du système linéaire
G, F, B = np.linalg.solve(A, b)

print("Prix d'une assiette gyros :", G)
print("Prix d'une frite          :", F)
print("Prix d'une boisson        :", B)

# Prix du repas de Gaston : 1 gyros + 1 frite
prix_gaston = G + F

print("Gaston devra payer :", "{:.2f}".format(prix_gaston), "€")
