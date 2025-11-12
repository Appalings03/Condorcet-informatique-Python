import numpy as np

import matplotlib.pyplot as plt

# Create x values in the interval [-2, 2]
x = np.linspace(-2, 2, 1000)

# Define sinh and cosh functions
sinh_x = (np.exp(x) - np.exp(-x)) / 2
cosh_x = (np.exp(x) + np.exp(-x)) / 2

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, sinh_x, label='sinh(x)', linewidth=2)
plt.plot(x, cosh_x, label='cosh(x)', linewidth=2)

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fonctions sinh(x) et cosh(x)')
plt.legend(''' upper left''')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

plt.show()