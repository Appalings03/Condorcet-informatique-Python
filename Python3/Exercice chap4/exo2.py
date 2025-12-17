import numpy as np

def x_n(n):
    try:
        assert n >= 0
    except AssertionError:
        print("Erreur : Veuillez entrer un entier naturel (n >= 0).")
        return
    x = np.sqrt(2)  # x_0
    for _ in range(n):
        x = np.sqrt(2 + x)
    return x

if __name__ == "__main__":
    print("Entrez un entier n : ")
    n = int(input())
    result = x_n(n)
    if result is not None:
        print(f"Le résultat de x_{n} est : {result}")
    
    # montre la suite converge vers 2
    print("\nSuite x_n :")
    for i in range(n + 1):
        xi = x_n(i)
        print(f"x_{i} = {xi:.10f} ; Différence avec 2 = {2 - xi:.10f}")

    
    