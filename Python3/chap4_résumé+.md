# Résumé Chapitre 4 Python 3

## Structures de données

## 4.1 Listes (`list`)
- Une **liste** est une collection **ordonnée** et **modifiable**
- Définie avec des crochets `[]`
- Peut contenir des éléments de types différents

```python
L = [1, 2, 3, "Python", True]
```

### Accès aux éléments
- Indexation commence à `0`
- Index négatifs possibles

```python
L[0]    # 1
L[-1]   # True
```

### Slicing
```python
L[1:4]
L[::2]
L[::-1]
```

## 4.2 Opérations courantes sur les listes
- `len(L)` — longueur
- `L.append(x)` — ajoute un élément à la fin
- `L.insert(i, x)` — insère à l’indice `i`
- `L.remove(x)` — supprime la première occurrence de `x`
- `L.pop(i)` — supprime et retourne l’élément d’indice `i`
- `L.sort()` — trie la liste
- `L.reverse()` — inverse l’ordre
- `L.count(x)` — compte les occurrences
- `L.index(x)` — renvoie l’indice de `x`

```python
L = [3, 1, 2]
L.sort()
```

## 4.3 Boucles sur les listes

```python
for x in L:
    print(x)
```

### Avec indices
```python
for i in range(len(L)):
    print(i, L[i])
```

### Avec `enumerate`
```python
for i, x in enumerate(L):
    print(i, x)
```

## 4.4 Compréhensions de listes
- Syntaxe compacte pour créer des listes

```python
L = [x**2 for x in range(5)]
```

### Avec condition
```python
L = [x for x in range(10) if x % 2 == 0]
```

## 4.5 Tuples (`tuple`)
- Collection **ordonnée** mais **immuable**
- Définie avec des parenthèses `()`

```python
T = (1, 2, 3)
```

## 4.6 Déballage (unpacking)

```python
a, b, c = (1, 2, 3)
x, *reste = [1, 2, 3, 4]
```

## 4.7 Dictionnaires (`dict`)
- Collection de paires clé / valeur
- Clés uniques et immuables

```python
d = {"a": 1, "b": 2}
```

### Méthodes utiles
- `keys()`, `values()`, `items()`, `get()`

```python
for k, v in d.items():
    print(k, v)
```

## 4.8 Ensembles (`set`)
- Collection sans doublons

```python
A = {1, 2, 3}
B = {3, 4}
A & B
```

## À retenir ⚠️
- `list` → modifiable
- `tuple` → immuable
- `dict` → clé / valeur
- `set` → sans doublons
