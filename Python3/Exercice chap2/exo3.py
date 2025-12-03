import numpy as np

# Variables : I1, I2 I3 I4 I5 I6
# Système :
# N1: I1 - I2 + I3 = 0
# N2: I2 + I5 + I6 = 0
# N3: I1 + I3 - I4 = 0
# M1: I1 - I3 = 6
# M2: -2*I2 - I3 +3*I5 = 4
# M3: 3*I5 - 4*I6 = -2

A = np.array([
    [1, -1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 1],
    [1, 0, 1, -1, 0, 0],
    [1, 0, -1, 0, 0, 0],
    [0, -2, -1, 0, 3, 0],
    [0, 0, 0, 0, 3, -4]
])

b = np.array([0, 0, 0, 6, 4, -2])
# b = np.transpose(np.array([[0, 0, 0, 6, 4, -2]]))

# Résolution du système linéaire
I = np.linalg.solve(A, b)

for i in range(len(I)):
    print(f"I{i+1} =", "{:.2f}".format(I[i]), "A")


