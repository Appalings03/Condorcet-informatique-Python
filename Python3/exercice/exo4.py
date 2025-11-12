import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Définition des fonctions
def f(x):
    return np.sin(x**2)

def g(x):
    return np.exp(x) / 4

# Domaine
x = np.linspace(0, 2, 1000)
y_f = f(x)
y_g = g(x)

plt.plot(x, y_f, label='f(x) = sin(x^2)')
plt.plot(x, y_g, label='g(x) = exp(x)/4')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphiques de f et g')
plt.legend()
plt.grid()
h = lambda x: f(x) - g(x)
# Trouver les points d'intersection
x_intersections = fsolve(h, [0.5, 1.5])
y_intersections = f(x_intersections)
print("Points d'intersection :")
i = 1
for xi, yi in zip(x_intersections, y_intersections):
    print(f"Racine {i} x: {xi}, y: {yi}") 
    i += 1
plt.plot(x_intersections, y_intersections, 'ro')  # Points d'intersection
plt.text(x_intersections[0], y_intersections[0], f'({x_intersections[0]:.2f}, {y_intersections[0]:.2f})', fontsize=9, verticalalignment='bottom')
plt.text(x_intersections[1], y_intersections[1], f'({x_intersections[1]:.2f}, {y_intersections[1]:.2f})', fontsize=9, verticalalignment='bottom')
plt.show()