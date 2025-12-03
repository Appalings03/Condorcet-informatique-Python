import numpy as np

# --- 1) Construire A = I + v v^T ---
v = np.arange(1, 11).reshape(10, 1)   # vecteur colonne
A = np.eye(10) + v @ v.T              # vv^T

# --- 2) Ajouter 2 à A_{23} (indices 1-based → [1,2] en 0-based) ---
A[1, 2] += 2

# --- 3) Vérifier qu'A est inversible ---
detA = np.linalg.det(A)
print("det(A) =", detA)
if abs(detA) > 1e-12:
    print("A est inversible.")
else:
    print("A n'est pas inversible.")

# --- 4) Construire u = w A^3 + 4 v ---
w = (v.flatten() ** 2).reshape(1, 10)   # row vector (1×10)
A3 = A @ A @ A
u = (w @ A3).reshape(10, 1) + 4*v

# --- 5) Remplacer la 3e composante de u par 7 ---
u[2, 0] = 7

# --- 6) Insérer 8 entre la 2e et 3e composante, puis ajouter un 0 ---
u_final = np.insert(u, 2, 8)      # insère 8 à l’indice 2 (entre composante 2 et 3)
u_final = np.append(u_final, 0)   # ajoute un 0 à la fin

print("Vecteur final u :")
print(u_final)
