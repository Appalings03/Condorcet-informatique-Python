import numpy as np

def f(x):
    return (np.sqrt(1 + np.pi) * np.sin(np.exp(x**3) + 1)) / ((np.log(x**2) + 1)**(3/2))

x = -1.2
result = f(x)
print(f"f({x}) = {result}")