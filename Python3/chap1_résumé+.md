# Résumé Chapitre 1 Python 3
## Commandes de base
- `print()` — affiche dans le terminal
- `del` — supprime une variable

## Opérateurs arithmétiques
- `+` — addition
- `-` — soustraction
- `*` — multiplication
- `/` — division
- `%` — modulo (reste de la division)
- `**` — puissance
- `abs()` — valeur absolue d'un nombre, renvoie la distance à zéro.
- `3.6e-5` — notation scientifique pour représenter 3.6 × 10⁻⁵, utile pour les très petits nombres.
- `divmod(a, b)` — renvoie un tuple contenant le quotient et le reste de la division de `a` par `b`.
- `().img` — renvoie la partie imaginaire d'un nombre complexe. Par exemple, pour un nombre complexe `z = 3 + 4j`, `z.imag` renverra `4`.
- `().real` — renvoie la partie réelle d'un nombre complexe. Par exemple, pour un nombre complexe `z = 3 + 4j`, `z.real` renverra `3`.

## Fonctions de conversion
- `float()` — convertit une valeur en nombre à virgule flottante.
- `str()` — convertit une valeur en chaîne de caractères.

## Fonctions mathématiques (NumPy)
- `np.log()` — logarithme naturel
- `np.log2()` — logarithme en base 2
- `np.log10()` — logarithme en base 10
- `np.exp()` — exponentielle
- `np.sqrt()` — racine carrée
- `np.sin()` — sinus
- `np.cos()` — cosinus
- `np.tan()` — tangente
- `np.abs()` — valeur absolue
- `np.ceil()` — arrondi vers le haut
- `np.floor()` — arrondi vers le bas
- `np.round()` — arrondi au plus proche

Opérateurs et fonctions mathématiques de base (NumPy).

## Fonctions avancées (Numpy)
- `np.linspace()` — Renvoie un tableau NumPy de valeurs également espacées entre un début et une fin. Ex : `np.linspace(start, stop, num=50, endpoint=True)` (par défaut inclut `stop`).

## Indexation et Slicing (Numpy)

**L'indexation** accède à des éléments individuels, tandis que le **slicing** extrait des sous-ensembles du tableau.

### Opérations détaillées

| Opération     | Résultat      | Explication                                                                 |
|---------------|---------------|-----------------------------------------------------------------------------|
| `x[0]`        | Scalaire      | Premier élément (l'indexation commence toujours à **0**)                   |
| `x[-1]`       | Scalaire      | Dernier élément (index négatif = comptage depuis la fin)                   |
| `x[0:3]`      | Sous-tableau  | Éléments d'index 0, 1, 2 (l'index final est **exclus**)                   |
| `x[:3]`       | Sous-tableau  | Équivalent à `x[0:3]` - omettant le début signifie "depuis le début"      |
| `x[3:]`       | Sous-tableau  | De l'index 3 jusqu'à la fin (3 est **inclus**)                            |
| `x[4:12:2]`   | Sous-tableau  | De 4 à 12 avec un **pas de 2** (éléments 4, 6, 8, 10)                     |
| `x[::2]`      | Sous-tableau  | Tous les éléments avec pas de 2 (1 sur 2)                                  |
| `x[::-1]`     | Sous-tableau  | Tableau **inversé** (pas = -1)                                            |

### Règle d'or du slicing

`x[start:stop:step]` → `[start, stop)` où stop est exclus

### Exemple courant ⚠️

`x[0:3]` retourne 3 éléments (indices 0, 1, 2), PAS 4 ! Le comportement "stop exclus" surprend souvent les débutants.

### Exemple de code

```python
import numpy as np

x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

print(x)              # [10 20 30 40 50 60 70 80 90]
print(type(x))        # <class 'numpy.ndarray'>
print(len(x))         # 9 - Longueur du vecteur
print(x[0])           # 10 - premier indice vaut toujours 0
print(x[0:3])         # [10 20 30] - indices 0 à 2 (3 non compris!!!)
print(x[:3])          # [10 20 30] - Idem
print(x[3:])          # [40 50 60 70 80 90] - Indice 3 compris jusqu'à la fin
print(x[-1])          # 90 - Dernière valeur de x
print(x[4:12:2])      # [50 70 90] - De l'élément 4 jusqu'à l'élément 12 non compris, par pas de 2
print(x[::2])         # [10 30 50 70 90] - 1 valeur sur 2 sur tout le vecteur
print(x[::-1])        # [90 80 70 60 50 40 30 20 10] - Vecteur dans l'autre sens
```

### Règle d'or du slicing

`x[start:stop:step]` → `[start, stop)` où stop est exclus

### Exemple courant ⚠️

`x[0:3]` retourne 3 éléments (indices 0, 1, 2), PAS 4 ! Le comportement "stop exclus" surprend souvent les débutants.

### Exemple de code

```python
import numpy as np

x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

print(x)              # [10 20 30 40 50 60 70 80 90]
print(type(x))        # <class 'numpy.ndarray'>
print(len(x))         # 9 - Longueur du vecteur
print(x[0])           # 10 - premier indice vaut toujours 0
print(x[0:3])         # [10 20 30] - indices 0 à 2 (3 non compris!!!)
print(x[:3])          # [10 20 30] - Idem
print(x[3:])          # [40 50 60 70 80 90] - Indice 3 compris jusqu'à la fin
print(x[-1])          # 90 - Dernière valeur de x
print(x[4:12:2])      # [50 70 90] - De l'élément 4 jusqu'à l'élément 12 non compris, par pas de 2
print(x[::2])         # [10 30 50 70 90] - 1 valeur sur 2 sur tout le vecteur
print(x[::-1])        # [90 80 70 60 50 40 30 20 10] - Vecteur dans l'autre sens
```

## Fonctions de matplotlib.pyplot
- `plt.plot()` — trace une courbe ou une ligne à partir de points (x, y). On peut personnaliser la couleur, le style, les marqueurs et d'autres propriétés via des mots-clés.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Exemple avec options courantes
plt.plot(
    x, y,
    color='tab:blue',      # couleur (nom, abbr. 'r', ou hex '#RRGGBB')
    linestyle='--',        # style de ligne: '-', '--', '-.', ':'
    linewidth=2,           # épaisseur de la ligne
    marker='o',            # marqueur: 'o', 's', '^', '.', ','
    markersize=8,          # taille du marqueur
    markerfacecolor='white', # couleur intérieure du marqueur
    markeredgecolor='tab:blue', # couleur du contour du marqueur
    alpha=0.9,             # transparence 0.0 (transparent) → 1.0 (opaque)
    label='Ligne 1'        # étiquette pour la légende
)
plt.xlabel('Axe X')
plt.ylabel('Axe Y')
plt.title('Exemple : couleur et style')
plt.legend()
plt.grid(True)
plt.show()
```

Options courantes (raccourcis entre parenthèses) :
- color / c — couleur ('red', 'r', '#FF0000', 'tab:blue', ...)
- linestyle / ls — style de la ligne ('-', '--', '-.', ':', 'None')
- linewidth / lw — épaisseur de la ligne (float)
- marker — forme du marqueur ('o', 's', '^', 'v', '.', ',', 'x', '+', ...)
- markersize / ms — taille du marqueur (float)
- markerfacecolor / mfc — couleur intérieure du marqueur
- markeredgecolor / mec — couleur du contour du marqueur
- markeredgewidth / mew — largeur du contour du marqueur
- alpha — transparence (0.0–1.0)
- label — étiquette utilisée par plt.legend()
- zorder — ordre de superposition (valeur numérique)
- drawstyle — style de dessin ('default', 'steps-post', ...)

*Astuce rapide : on peut aussi passer une chaîne combinée courte, ex. plt.plot(x, y, 'ro--') => points rouges ('r') avec marqueurs 'o' et ligne en tirets '--'.*

- `plt.scatter()` — affiche des points individuels (nuage de points)
    ```python
    plt.scatter(x, y)
    plt.show()
    ```

- `plt.bar()` — crée un diagramme en barres
    ```python
    plt.bar(x, y)
    plt.show()
    ```

- `plt.hist()` — crée un histogramme pour la distribution de données
    ```python
    data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    plt.hist(data, bins=4)
    plt.show()
    ```

- `plt.xlabel()` — définit le label de l'axe x
    ```python
    plt.xlabel('Axe X')
    ```

- `plt.ylabel()` — définit le label de l'axe y
    ```python
    plt.ylabel('Axe Y')
    ```

- `plt.title()` — ajoute un titre au graphique
    ```python
    plt.title('Mon Graphique')
    ```

- `plt.legend()` — affiche la légende (basée sur les paramètres `label`)
    ```python
    plt.plot(x, y, label='Ligne 1')
    plt.legend()
    ```

- `plt.grid()` — affiche une grille de fond
    ```python
    plt.grid(True)
    ```

- `plt.show()` — affiche le graphique dans une fenêtre
    ```python
    plt.show()
    ```

- `plt.savefig()` — sauvegarde le graphique dans un fichier
    ```python
    plt.savefig('mon_graphique.png')
    ```

- `plt.figure()` — crée une nouvelle figure
    ```python
    plt.figure()
    ```

- `plt.subplot()` — crée plusieurs graphiques dans une même figure
    ```python
    plt.subplot(2, 1, 1)  # 2 lignes, 1 colonne, 1er subplot
    plt.subplot(2, 1, 2)  # 2 lignes, 1 colonne, 2ème subplot
    ```

- `plt.xlim()` — définit les limites de l'axe x
    ```python
    plt.xlim(0, 5)
    ```

- `plt.ylim()` — définit les limites de l'axe y
    ```python
    plt.ylim(0, 35)
    ```

- `plt.axis()` — limites et affichage des axes
    - Bref : définit ou lit [xmin, xmax, ymin, ymax], ou change le mode d'affichage.
    - Usage courant :
        - plt.axis([xmin, xmax, ymin, ymax])
        - plt.axis('equal')   # mêmes unités sur x et y
        - plt.axis('tight')   # ajusté aux données
        - plt.axis('off') / plt.axis('on')
        - limits = plt.axis() # récupère les limites

    ```python
    plt.plot(x, y)
    plt.axis([0, 2*np.pi, -1.5, 1.5])
    plt.show()
    ```
    *Astuce : pour un contrôle précis, utiliser ax = plt.gca(); ax.set_aspect('equal') puis plt.xlim()/plt.ylim() si besoin.*

## Différence entre `def` et `lambda`

- `def` — définit une fonction nommée avec un bloc d'instructions :
    - Peut contenir plusieurs instructions, des boucles, des affectations.
    - Supporte une docstring, des annotations de paramètres/retour et des décorateurs.
    - Plus lisible pour les fonctions complexes.
    - Exemple :
        ```python
        x=np.linspace(-1,1,2001)
        def f(x):
            """Renvoie x au carré"""
            return x * x
        
        y = f(x)
        plt.plot(x,y,"k")
        ```

- `lambda` — crée une fonction anonyme en une seule expression :
    - Limité à une expression (pas d'instructions multiples), pas de docstring ni d'annotations.
    - Utile pour des fonctions courtes et jetables (par ex. `key`, `map`, `filter`).
    - Peut être affectée à une variable mais garde le nom interne `<lambda>`.
    - Exemple :
        ```python
        x=np.linspace(-1,1,2001)
        f = lambda x: x * x
        plt.plot(x,f(x),"k")  
        ```

*Conseil : privilégier `def` pour la clarté et la maintenance ; utiliser `lambda` pour des opérations simples et locales.*



## Fonctions Scipy.optimize

- `scipy.optimize.fmin(func, x0, ...)` — minimise une fonction scalaire sans contrainte :
    - Utilise l'algorithme de Nelder-Mead (simplexe).
    - Ne nécessite pas de dérivée, robuste mais peut converger lentement.
    - `x0` : point de départ (scalaire ou vecteur).
    - Retourne le point minimisant (pas la valeur).
    - Utile pour trouver des extrema locaux sans bornes.
    - Exemple
        ```python
        from scipy.optimize import fmin
        def f(x):
            return (x-1.5)**2 + np.sin(5*x)

        x_min = fmin(f, x0=0)[0]  # ≈ 1.5 ou point proche
        print(f"Minimum en x ≈ {x_min:.4f}, f(x) = {f(x_min):.4f}")
        ```

- `scipy.optimize.fsolve(func, x0, ...)` — résout ( f(x) = 0 ) (système non linéaire) :
    - Utilise une variante de Newton-Raphson ou hybride.
    - `func` doit renvoyer zéro au point solution.
    - `x0` : estimation initiale (scalaire ou tableau).
    - Retourne les racines (zéros de la fonction).
    - Idéal pour résoudre des équations transcendantes.
    - Exemple :
    ```python
    from scipy.optimize import fsolve
    def eq(x):
        return np.sin(x**2) - np.exp(x)/4

    racines = fsolve(eq, x0=[0.5, 1.0, 1.8])
    print("Solutions :", racines)
    ```

    *Conseil : utiliser `fmin` pour l’optimisation locale sans dérivée ; `fsolve` pour résoudre des équations `( f(x)=0 )`.*

## Fonctions Scipy.interpolate

- `scipy.interpolate.interp1d(x, y, kind=... )` — interpolation 1D entre points connus :
    - Crée une fonction interpolante à partir de données ((x_i, y_i)).
    - `kind` : 'linear', 'nearest', 'cubic', 'quadratic', etc.
    - Retourne une fonction callable pour évaluer entre les points.
    - Gère l’extrapolation avec fill_value ou bounds_error.
    - Exemple :
        ```python
        from scipy.interpolate import interp1d
        x_data = [0, 1, 2, 3]
        y_data = [0, 1, 0, 1]
        f_interp = interp1d(x_data, y_data, kind='cubic')

        x_fine = np.linspace(0, 3, 100)
        plt.plot(x_data, y_data, 'o', label='données')
        plt.plot(x_fine, f_interp(x_fine), '-', label='interpolation cubique')
        plt.legend()
        ```

- `scipy.interpolate.griddata(points, values, xi, method=... )` — interpolation sur grille irrégulière (2D/3D) :
    - Interpole des données éparpillées sur une grille régulière.
    - `points` : coordonnées des données ((x_i, y_i)), values : (f(x_i, y_i)).
    - `xi` : points où interpoler (grille).
    - `method` : 'nearest', 'linear', 'cubic'.
    - Utile en visualisation scientifique (ex : nuages de points → surface).
    - Exemple :
        ```python
        from scipy.interpolate import griddata
        points = np.random.rand(50, 2)
        values = np.sin(points[:,0]*5) * np.cos(points[:,1]*5)

        xi = np.mgrid[0:1:100j, 0:1:100j]
        zi = griddata(points, values, xi.T, method='cubic')

        plt.imshow(zi, extent=(0,1,0,1), origin='lower')
        plt.scatter(points[:,0], points[:,1], c=values, edgecolors='k')
        plt.colorbar()
        ```

*Conseil : interp1d pour des courbes 1D simples ; griddata pour des données éparpillées en 2D/3D.*