import numpy as np
from scipy.optimize import fmin

import matplotlib.pyplot as plt

# Définition de la fonction
def f(x):
    return (1 + x) * np.exp(-x**2 + 3 * x * np.cos(x)) - (1 + x**4)**2 * np.sin(x)

# Intervalle de x
x = np.linspace(-3, 3, 2000)
y = f(x)

# Tracer le graphe
plt.plot(x, y, 'r:', label='f(x)')
plt.grid()
# Trouver le minimum
xmin = fmin(f, 3)
# def g(x): return -f(x)
# Trouver le maximum
xmax = fmin(lambda x: -f(x), -3)
# Afficher les résultats
print(f"Le minimum de f(x) est atteint en x = {xmin[0]:.6f}, f(x) = {f(xmin[0]):.6f}")
print(f"Le maximum de f(x) est atteint en x = {xmax[0]:.6f}, f(x) = {f(xmax[0]):.6f}")
# Marquer les points minimum et maximum sur le graphe
plt.plot(xmin[0], f(xmin[0]), 'bx', label='Minimum')
#plt.text(xmax[0]+0.2, f(xmax[0]), "Maximum", color='green')
plt.plot(xmax[0], f(xmax[0]), 'gx', label='Maximum')
plt.title('Graphe de la fonction f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()

