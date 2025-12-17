import numpy as np
def exo2(n):
    """n est un indice entier >="""
    x = np.sqrt(2)  # x_0
    for _ in range(n):
        x = np.sqrt(2 + x) 
    return x