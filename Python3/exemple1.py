import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + 25 * x**2)

# Create x values in the range [-1, 1]
x = np.linspace(-1, 1, 10)
y = f(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'k-', linewidth=2, label='f(x) = 1/(1+25x²)')

# Add grid
plt.grid(True, alpha=0.3)

# Label axes and title
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Graphe de la fonction de Runge', fontsize=14)

# Set axis limits (zoom)
plt.xlim(-1, 1)
plt.ylim(0, 1.1)

plt.legend()
plt.tight_layout()
plt.show()