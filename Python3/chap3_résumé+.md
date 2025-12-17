# Résumé Chapitre 3 Python 3

## Types de données simples

## 3.1 Identificateurs
- Un **identificateur** est le nom donné à une variable, fonction, classe, etc.
- Règles :
  - Commence par une lettre ou `_`
  - Contient lettres, chiffres et `_`
  - Sensible à la casse (`a` ≠ `A`)
  - Ne doit pas être un mot-clé Python

## 3.2 Mots-clés de Python 3
- Mots réservés du langage
- Ne peuvent pas être utilisés comme identificateurs
- Exemples : `if`, `else`, `for`, `while`, `def`, `return`, `True`, `False`, `None`,
  `import`, `from`, `as`, `class`, `try`, `except`, `finally`

## 3.3 Types de données
- `int` — entiers
- `float` — nombres réels
- `complex` — nombres complexes
- `bool` — booléens (`True`, `False`)
- `str` — chaînes de caractères

```python
x = 3         # int
y = 2.5       # float
z = 2 + 3j    # complex
b = True      # bool
s = "Python"  # str
```

## 3.4 Type `int`

### Base 10 (défaut)
```python
n = 42
```

### Base 2 (binaire → base 10)
- Préfixe `0b`
```python
n = 0b101010  # 42
```

### Base 8 (octale → base 10)
- Préfixe `0o`
```python
n = 0o52  # 42
```

### Base 16 (hexadécimale → base 10)
- Préfixe `0x`
```python
n = 0x2A  # 42
```

### Conversion de base
```python
bin(42)  # '0b101010'
oct(42)  # '0o52'
hex(42)  # '0x2a'
```

## 3.5 Type `float`
- Représente des nombres réels
- Notation décimale ou scientifique

```python
x = 3.14
y = 1.2e-3
```

⚠️ Attention aux **erreurs d'arrondi** :
```python
0.1 + 0.2  # 0.30000000000000004
```

## 3.6 Type `complex`
- Forme : `a + bj`
- `j` représente la partie imaginaire

```python
z = 3 + 4j
z.real   # 3.0
z.imag   # 4.0
abs(z)   # module
```

## 3.7 Type `bool`
- Deux valeurs possibles : `True`, `False`
- Résultat de comparaisons logiques

```python
x = 5
x > 3     # True
x == 10   # False
```

## 3.8 Opérateurs de comparaison
- `==` égal
- `!=` différent
- `<` inférieur
- `<=` inférieur ou égal
- `>` supérieur
- `>=` supérieur ou égal

## 3.9 Opérateurs logiques
- `and` — ET logique
- `or` — OU logique
- `not` — NON logique

```python
x = 5
(x > 0) and (x < 10)
```

## 3.10 Type `str` (chaînes de caractères)
- Délimitées par `' '` ou `" "`
- **Immuables**

```python
s = "Python"
```

### Indexation
```python
s[0]    # 'P'
s[-1]   # 'n'
```

### Slicing
```python
s[0:3]   # 'Pyt'
s[::2]   # 'Pto'
```

## 3.11 Fonctions utiles sur les chaînes
- `len(s)` — longueur
- `s.upper()` — majuscules
- `s.lower()` — minuscules
- `s.strip()` — supprime espaces début/fin
- `s.replace(a, b)` — remplace
- `s.split()` — découpe

```python
s = "  Python  "
s.strip().upper()
```

## 3.12 Conversion de types
- `int()`
- `float()`
- `str()`
- `bool()`

```python
int("42")
float("3.14")
str(10)
```

## 3.13 Type d’une variable
- `type()` permet de connaître le type

```python
type(3.14)
```

## À retenir ⚠️
- Python est **dynamiquement typé**
- Le type est associé à la valeur, pas au nom de variable
- Attention aux erreurs d'arrondi avec les `float`
- Les chaînes sont immuables

*Conseil : utiliser `type()` dès qu’un doute apparaît.*
