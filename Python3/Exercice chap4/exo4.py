def factorielle(n):
    """
    Calcule la factorielle d'un entier n.

    Paramètres :
    n (int) : Un entier positif ou nul

    Retour :
    int : n! (factorielle de n)
    None : si n n'est pas un entier positif ou nul

    La factorielle est définie comme suit :
    - 0! = 1
    - n! = 1 * 2 * ... * n pour n >= 1
    """
    try:
        assert type(n) == int and n >= 0
    except AssertionError:
        print("Erreur : Veuillez entrer un entier positif ou nul.")
        return

    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

if __name__ == "__main__":
    # Exemple d'utilisation
    x = int(input("Entrez un entier positif ou nul : "))
    print(f"{x}! = {factorielle(x)}")

    # Pour tester la doc
    help(factorielle)