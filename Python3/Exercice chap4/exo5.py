def racine_carre(a, tol=1e-6):
    """
    Calcule la racine carrée de a > 0 en utilisant la méthode itérative :
    x_{i+1} = 0.5 * (x_i + a / x_i)
    
    Paramètres :
        a : nombre strictement positif
        tol : tolérance pour la précision relative
        
    Retourne :
        La racine carrée de a
    """
    try:
        assert a>0
    except AssertionError:
        print("Le nombre doit être strictement positif.")
        return
    
    x = 1.0  # valeur initiale x0
    while True:
        x_new = 0.5 * (x + a / x)
        # précision relative
        if abs(x_new - x) / x_new < tol:
            return x_new
        x = x_new



a = float(input("Entrez un nombre strictement positif : "))
racine = racine_carre(a)
print(f"La racine carrée de {a} est approximativement {racine}")
