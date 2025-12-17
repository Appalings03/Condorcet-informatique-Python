import numpy as np
a = 10
b = 2

def func(a,b):
    """Fonction qui affiche des opérations sur a et b"""
    try:
        assert a > 0 and b!= 0
    except AssertionError:
        print("Erreur : a doit être > 0 et b doit être différent de 0")
        return
    
    print(f"a={a}")
    print(f"b={b}")
    print(f"a + b = {a+b}")
    print(f"a - b = {a-b}")
    print(f"a * b = {a*b}")
    print(f"a / b = {a/b}")
    print(f"log10(a) = {np.log10(a)}")
    print(f"a^b = {a**b}")
    return

if __name__ == "__main__":
    func(a,b)


    