def pgcd_euclide(a, b):
    """
    Calcule le Plus Grand Commun Diviseur (PGCD) de deux entiers positifs non nuls
    en utilisant l'algorithme d'Euclide.

    Paramètres:
    a (int) : Premier entier positif non nul
    b (int) : Deuxième entier positif non nul

    Retour:
    int : Le PGCD de a et b

    L'algorithme d'Euclide fonctionne de la manière suivante :
    - Tant que b n'est pas nul :
        - Remplacer a par b
        - Remplacer b par le reste de la division entière a // b
    - Quand b devient 0, a contient le PGCD
    """
    try:
        assert type(a) is int and type(b) is int and (a >= 0 and b >= 0) and (a > 0 or b > 0)
    except AssertionError:
        print("Erreur : Veuillez entrer des entiers positifs non nuls.")
        return

    while b != 0:
        a, b = b, a % b
    return a

def pgcd_soustraction(a, b):
    """
    Calcule le PGCD (Plus Grand Commun Diviseur) de deux entiers positifs non nuls
    en utilisant l'algorithme d'Euclide (version récursive).

    Paramètres :
    a (int) : Premier entier positif non nul
    b (int) : Deuxième entier positif non nul

    Retour :
    int : Le PGCD de a et b
    None : Si les entrées ne sont pas valides (non entiers ou <= 0)

    Méthode :
    - Si b == 0, le PGCD est a
    - Sinon, PGCD(a, b) = PGCD(b, a % b)
    """
    if b ==0:
        return a
    elif a == 0:
        return b
    else:
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

def pgcd_factorisation(a, b):
    """
    Calcule le PGCD (Plus Grand Commun Diviseur) de deux entiers positifs non nuls
    en utilisant la factorisation en nombres premiers.

    Paramètres :
    a (int) : Premier entier positif non nul
    b (int) : Deuxième entier positif non nul

    Retour :
    int : Le PGCD de a et b
    None : Si les entrées ne sont pas valides (non entiers ou <= 0)

    Méthode :
    - Factoriser a et b en facteurs premiers
    - Identifier les facteurs communs et prendre la puissance minimale
    - Multiplier les facteurs communs pour obtenir le PGCD
    """
    try:
        assert type(a) is int and type(b) is int and (a >= 0 and b >= 0) and (a > 0 or b > 0)
    except AssertionError:
        print("Erreur : Veuillez entrer des entiers positifs non nuls.")
        return
    
    def facteurs(n):
        i = 2
        f = []
        while i <= n:
            if n % i == 0:
                f.append(i)
                n //= i
            else:
                i += 1
        return f

    f1 = facteurs(a)
    f2 = facteurs(b)
    commun = 1
    for x in set(f1):
        commun *= x ** min(f1.count(x), f2.count(x))
    return commun

def pgcd_recursif(a, b):
    """
    Calcule le PGCD (Plus Grand Commun Diviseur) de deux entiers positifs non nuls
    en utilisant la méthode des soustractions successives.

    Paramètres :
    a (int) : Premier entier positif non nul
    b (int) : Deuxième entier positif non nul

    Retour :
    int : Le PGCD de a et b
    None : Si les entrées ne sont pas valides (non entiers ou <= 0)

    Méthode :
    - Répéter jusqu'à ce que a == b :
        - Soustraire le plus petit du plus grand
    - Quand a == b, la valeur est le PGCD
    """
    try:
        assert type(a) is int and type(b) is int and (a >= 0 and b >= 0) and (a > 0 or b > 0)
    except AssertionError:
        print("Erreur : Veuillez entrer des entiers positifs non nuls.")
        return
    
    if b == 0:
        return a
    else:
        return pgcd_recursif(b, a % b)

if __name__ == "__main__":
    print("Documentation des fonctions PGCD :\n")
    help(pgcd_euclide)
    help(pgcd_soustraction)
    help(pgcd_factorisation)
    help(pgcd_recursif)
    print("--------------------------------------------\n")
    print("Entrez deux entiers positifs non nuls a et b : ")
    a = int(input("a = ")) 
    b = int(input("b = "))
    print(f"\nPGCD de {a} et {b} par l'algorithme d'Euclide : {pgcd_euclide(a, b)}")
    print(f"PGCD de {a} et {b} par soustractions successives : {pgcd_soustraction(a, b)}")
    print(f"PGCD de {a} et {b} par factorisation : {pgcd_factorisation(a, b)}")
    print(f"PGCD de {a} et {b} par méthode récursive : {pgcd_recursif(a, b)}")
    