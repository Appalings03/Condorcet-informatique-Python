import numpy as np

# Variables : I1, I2, I3
# Système :
# N1: I1 + I2 + I3 = 0  
# M1: 16 -4 = -10*I1 + 8*I2 + 0*I3
# M2: 4 +10 = 0*I1 - 8*I2 + 2*I3



A = np.array([
    [1, 1, 1],
    [-10, 8, 0],
    [0, -8, 2],
])

# b = np.array([0, 12, 14])
b = np.transpose(np.array([[0, 12, 14]]))

# Résolution du système linéaire
I = np.linalg.solve(A, b)

for i in range(len(I)):
    print(f"I{i+1} =", "{:.2f}".format(I[i,0]), "A")