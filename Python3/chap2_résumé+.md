# Résumé Chapitre 2 Python 3
## Matrice et vecteurs : Syntaxe
On supposera toujours que les matrices et vecteurs sont définis comme des tableaux numpy comme suit :<br/>
Pour définir
\begin{equation*}
A=
\left(
\begin{matrix}
1 & 2\\
3 & 4
\end{matrix}
\right)
\end{equation*}
On code :

```python
A=np.array([[1,2],[3,4]])
print(A)
```
OUTPUT:
```python
[[1 2]
 [3 4]]
 ```

Il est possible de crée des matrices de réels
>  [!tip]
```python
A=np.array([[1.,2.],[3.,4.]])
print(A)
# ou bien
A=np.array([[1,2],[3,4]],dtype=np.float64)    # floating point number sur 64 bits
print(A)
```
## Opérations matricielles versus opérations terme à terme
- `A@B` : Produit matricielle
- `A*B` : Produit terme à terme
- `A/B` : Division terme à terme
- `A**B` : Puissance terme à terme
- Example :
```python
A=np.array([[1,2],[3,4]])
print(A)
# Output
#[[1 2]
# [3 4]]
B=np.array([[5,0],[2,1]])
print(B)
#[[5 0]
# [2 1]]
```
> Produit matricielle
    ```python
    print(A@B)
    #[[ 9  2]
    #[23  4]]
    ```
> [!CAUTION]
> Pour lesopérations termes à termes, les deux matrices doivent avoir la même dimension 

> Produit terme à terme
    ```python
    print(A*B)
    #[[5 0]
    #[6 4]]
    ```
> Quotien terme à terme
    ```python
    print(A/B)
    ```
> Puissance terme à terme
    ```python
    print(A**B)
    ```

> [!TIP]
>pour effectuer `A@A`, utiliser la syntaxe `print(np.linalg.matrix_power(A,2))`

## Manipulation de matricielles de base

```python
A=np.array([[1,1,2],[3,3,5],[4,7,8]])
print(A)
```
### Acces aux éléments d'une matrice
#### Syntaxe
1. Affiche l'élément au milieu de la matrice 
    - `A[1, 1]` : Output => 3 
    - `A[1][1]` : Output => 3 
    

| D3| 0 | 1 | 2 | 
|---|---|---|---|
| 0 | 1 | 1 | 2 |
| 1 | 3 | **3** | 5 |
| 2 | 4 | 7 | 8 |

2. Dimension, nombre élément
    - `A.shape` : Output => (3,3)
        -  `A.shape[0]` : Output nbre de ligne de la matrice => 3
    - `A.size` ou `np.size(A)` : donne le nombre d'élément de la matrice µ
3. Transposée, inverse, déterminant
