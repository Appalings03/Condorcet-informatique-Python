---
tags:
  - labo
  - physique
  - oscillations
  - T-CINF-011
aliases:
  - Labo oscillations mécaniques
  - T-CINF-011
rapport: 2026-10-21
---

# Labo T-CINF-011 — Oscillations mécaniques

> [!info] Infos clés
> - Rapport **par groupe**, sur Moodle pour le **29 octobre 23h59** (−30 % par jour de retard)
> - Compte pour **35 %** de l'AA T-CINF-011
> - Présence **obligatoire** (absence injustifiée = 0/20)
> - À apporter : **1 portable par groupe** avec **Capstone** et **Excel**
> - Pas d'intro ni de conclusion : répondre aux questions, détailler calculs et méthodes
> - Le fichier Excel (template sur Moodle) doit être **reproductible** : chaque paramètre utilisé est noté et expliqué dans le rapport

## Checklist

**Avant le labo**
- [x] Répondre à Q1–Q6 (section 1) et regarder les vidéos du protocole
- [x] Télécharger le template Excel sur Moodle
- [x] Installer / tester Capstone et Python (`numpy scipy pandas matplotlib`)
- [x] Relire la section 6 (oscillations couplées) : calculer les modes **avant** de venir (valeurs de $m_i$ et $k_i$ données par le prof)

**Pendant le labo**
- [x] Noter **toutes** les valeurs : masses, $\theta$, épaisseurs des plaquettes (pied à coulisse), $k_1,k_2$, avec incertitudes
- [x] Sauvegarder les fichiers Capstone **régulièrement**
- [x] Exporter les données en CSV (Capstone : *File → Export Data*) pour analyser en Python
- [x] Prendre des photos du montage

**Après**
- [ ] Graphes : titre, noms d'axes, unités, lisibles
- [ ] Excel complété et reproductible
- [ ] Déposer sur Moodle

---

# 1. Travail préliminaire (Q1 à Q6)

## Q1 — Ressort statique vertical

Axe $x$ vers le bas, origine à la longueur naturelle du ressort (sans masse).

```
   ═══════  support
      │
      ╱╲╱╲     ressort (raideur k)    ↑ force de rappel  F = -k·x_eq
      │
     ┌┴┐
     │m│  ↓ poids  P = m·g
     └─┘
```

Équilibre statique ($\sum F = 0$) :

$$mg - k\,x_{eq} = 0 \quad\Longrightarrow\quad k = \frac{mg}{x_{eq}}$$

où $x_{eq}$ est l'allongement à l'équilibre.

## Q2 — Ressort oscillant verticalement

**Position de symétrie** : le ressort oscille autour de la **position d'équilibre statique** $x_{eq}=mg/k$ (pas autour de la longueur naturelle). La gravité ne fait que décaler le centre d'oscillation.

**Équation du mouvement** (2e loi de Newton, $x$ depuis la longueur naturelle) :

$$m\ddot x = mg - kx$$

On pose $y = x - x_{eq}$ (écart à l'équilibre) :

$$m\ddot y = mg - k(x_{eq}+y) = -ky \quad\Longrightarrow\quad \ddot y + \omega_0^2\,y = 0,\qquad \omega_0=\sqrt{\frac km}$$

Solution : $y(t) = A\cos(\omega_0 t+\varphi)$

- $A$ : amplitude (= élongation initiale par rapport à l'équilibre si on lâche sans vitesse, alors $\varphi=0$)
- $\varphi$ : phase initiale
- $\omega_0$ : pulsation propre (rad/s), ne dépend que de $k$ et $m$
- $m\ddot y$ : inertie ; $-ky$ : force de rappel élastique

**Période** :

$$T_0 = \frac{2\pi}{\omega_0} = 2\pi\sqrt{\frac mk} = 2\pi\sqrt{\frac{x_{eq}}{g}}$$

> [!tip] Correction de masse du ressort
> Un ressort réel a une masse $m_s$. En pratique on remplace $m$ par $m + m_s/3$ dans $T_0$. À mentionner si on veut raffiner.

## 3.3 — Association de ressorts (rappel de la preuve en annexe)

- Parallèle (cas a et b, même déplacement $x$, forces qui s'additionnent) : $k_{eq}=k_1+k_2$
- Série (cas c, même force, allongements qui s'additionnent $x=x_1+x_2$, $k_1x_1=k_2x_2=k_{eq}x$) :

$$\frac{1}{k_{eq}}=\frac1{k_1}+\frac1{k_2}\quad\Longleftrightarrow\quad k_{eq}=\frac{k_1k_2}{k_1+k_2}$$

Avec 2 ressorts jaunes de $\approx 2{,}5$ N/m en série : $k_{eq}\approx 1{,}25$ N/m.

## Q3 — Oscillateur harmonique amorti

$$m\ddot x + b\dot x + kx = 0 \quad\Longleftrightarrow\quad \ddot x + 2\gamma\dot x+\omega_0^2x=0,\quad \gamma=\frac{b}{2m}$$

- $m\ddot x$ : inertie
- $b\dot x$ : frottement **visqueux** (ici le freinage magnétique par courants de Foucault, proportionnel à la vitesse et opposé)
- $kx$ : rappel élastique

Polynôme caractéristique ($x = e^{rt}$) :

$$mr^2+br+k=0,\qquad \Delta = b^2-4mk,\qquad r_\pm=\frac{-b\pm\sqrt{\Delta}}{2m}$$

| Cas | Racines | Solution | Comportement |
|---|---|---|---|
| $\Delta<0$ sous-amorti | complexes $-\gamma\pm i\omega_d$ | $e^{-\gamma t}(c_1\cos\omega_dt+c_2\sin\omega_dt)$ | oscillations dont l'amplitude décroît exponentiellement |
| $\Delta>0$ sur-amorti | 2 réelles négatives | $c_1e^{r_+t}+c_2e^{r_-t}$ | pas d'oscillation, retour lent |
| $\Delta=0$ critique | 1 racine double $-\gamma$ | $(c_1+c_2t)e^{-\gamma t}$ | retour à l'équilibre le plus rapide sans oscillation |

## Q4 — Facteur d'amortissement

$$\zeta=\frac{b}{\sqrt{4mk}}=\frac{b}{2\sqrt{mk}}$$

Comme $\Delta<0\Leftrightarrow b<2\sqrt{mk}$ :

- sous-amortissement : $\zeta<1$
- sur-amortissement : $\zeta>1$
- amortissement critique : $\zeta=1$ (donc $b_c = 2\sqrt{mk}$)

## Q5 — Solution sous-amortie et période

$$x(t)=e^{-\gamma t}\big(c_1\cos\omega_dt+c_2\sin\omega_dt\big)=A_0e^{-bt/2m}\cos(\omega_dt+\varphi)$$

avec $c_1=x(0)$ et $c_2=\dfrac{v(0)+\gamma x(0)}{\omega_d}$, et

$$\omega_d=\sqrt{\omega_0^2-\gamma^2}=\sqrt{\frac km-\frac{b^2}{4m^2}}$$

Or $\dfrac{\gamma}{\omega_0}=\dfrac{b}{2m}\sqrt{\dfrac mk}=\dfrac{b}{2\sqrt{mk}}=\zeta$, donc $\omega_d=\omega_0\sqrt{1-\zeta^2}$ et

$$T=\frac{2\pi}{\omega_d}=\frac{2\pi/\omega_0}{\sqrt{1-\zeta^2}}=\frac{T_0}{\sqrt{1-\zeta^2}},\qquad T_0=2\pi\sqrt{\frac mk}$$

La période amortie est donc **un peu plus longue** que $T_0$ (et très proche de $T_0$ si $\zeta\ll1$).

## Q6 — Vitesse limite sur le rail incliné

Le long du rail (axe vers le bas, cart qui descend, $v>0$) :

$$m\dot v = mg\sin\theta - f - bv$$

Vitesse limite : $\dot v=0$

$$\boxed{v_\infty=\frac{mg\sin\theta-f}{b}}$$

**Faut-il $v_0=0$ ? Non.** L'équation est linéaire du premier ordre :

$$v(t)=v_\infty+(v_0-v_\infty)\,e^{-bt/m}$$

Quelle que soit $v_0$, on tend vers $v_\infty$ avec une constante de temps $\tau=m/b$. La vitesse initiale change seulement le temps pour y arriver. Il faut un rail assez long (environ $5\tau$ de parcours), d'où la remarque du protocole : sur 2 m, on n'atteint $v_\infty$ que si le freinage est suffisant.

## 3.5 — Pied à coulisse

1. Fermer les mâchoires : vérifier que le zéro est à zéro (sinon noter l'erreur de zéro)
2. Lire sur la règle fixe les **mm entiers** à gauche du zéro du vernier
3. Repérer la graduation du vernier qui s'aligne le mieux avec une graduation de la règle : numéro $n$
4. Résultat $=$ mm entiers $+\,n\times$ précision (0,02 mm pour un vernier à 50 divisions, 0,05 mm à 20 divisions, 0,1 mm à 10 divisions)

Incertitude typique : 1 graduation du vernier. Pour les plaquettes : mesurer **plusieurs fois** et en plusieurs endroits.

---

# 2. Outils communs (Python)

> [!note] Philosophie
> Le rapport et l'Excel doivent rester reproductibles : utilise Python pour **vérifier** tes résultats Capstone/Excel et produire de beaux graphes, mais les valeurs finales doivent aussi pouvoir être refaites dans Excel (formules en section 6).

```python
# [outil] imports et utilitaires
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from scipy.linalg import eigh

g = 9.81  # m/s²


def charger_capstone(chemin, col_t=0, col_y=1):
    """Lit un CSV exporté de Capstone (séparateur et virgule décimale gérés).
    col_t / col_y : indices des colonnes temps et grandeur voulue."""
    df = pd.read_csv(chemin, sep=None, engine="python")
    t = pd.to_numeric(df.iloc[:, col_t].astype(str).str.replace(",", "."), errors="coerce")
    y = pd.to_numeric(df.iloc[:, col_y].astype(str).str.replace(",", "."), errors="coerce")
    ok = t.notna() & y.notna()
    return t[ok].to_numpy(), y[ok].to_numpy()


def k_statique(masses_kg, allongements_m):
    """Régression F = m g en fonction de l'allongement : pente = k (et son incertitude)."""
    F = np.asarray(masses_kg) * g
    x = np.asarray(allongements_m)
    p, cov = np.polyfit(x, F, 1, cov=True)
    return p[0], np.sqrt(cov[0, 0])


def k_dynamique(m_kg, T_total_s, N, m_ressort_kg=0.0):
    """k = 4π² m_eff / T² avec T mesuré sur N oscillations (chrono)."""
    T = T_total_s / N
    return 4 * np.pi**2 * (m_kg + m_ressort_kg / 3) / T**2


def k_serie(k1, k2):
    return k1 * k2 / (k1 + k2)


def angle_rail(h_m, L_m):
    """θ à partir d'un triangle rectangle (hauteur h, longueur de rail L)."""
    return np.arcsin(h_m / L_m)
```

---

# 3. Partie 1 — Mouvement harmonique amorti (sections 5.1 à 5.4)

## 5.1 Mise en place — points d'attention

1. Tester le roulis de chaque chariot à l'oreille (changer si ça frotte)
2. **Peser le chariot avec les aimants dessus** → $m$ (c'est la masse totale à utiliser partout)
3. Inclinaison $\approx 30^\circ$ : mesurer $\theta$ précisément. Avec la grande règle : $\sin\theta = h/L$ (voir `angle_rail`). Recouper avec le mesureur d'angle Pasco et noter l'incertitude
4. $k_1$ et $k_2$ des 2 ressorts jaunes (≈ 2,5 N/m chacun, sinon **appeler le prof**) : méthode statique (plusieurs masses + régression, meilleure) ou dynamique (chrono sur $N=10$–20 oscillations)
5. $k_{eq}=k_1k_2/(k_1+k_2)$ (≈ 1,25 N/m)
6. Capstone : sélectionner **son** chariot (numéro de série), taux d'acquisition **≥ 100 Hz**
7. Plaquettes : mesurer l'épaisseur au pied à coulisse (les valeurs gravées sont approximatives)

```python
# [exemple] raideur d'un ressort
masses = [0.020, 0.040, 0.060, 0.080, 0.100]      # kg  (jeu 0 à 100 g)
allong = [0.081, 0.160, 0.238, 0.322, 0.398]      # m   (exemple fictif, à remplacer)
k1, dk1 = k_statique(masses, allong)
k2 = 2.52                                          # idem pour le 2e ressort
keq = k_serie(k1, k2)
print(f"k1 = {k1:.2f} ± {dk1:.2f} N/m ; keq = {keq:.2f} N/m")
```

## 5.2 Amortissement par frottements secs

### Théorie

Sans aimants (mais aimants posés sur le chariot pour garder la même masse), l'amortissement est dû au frottement sec cinétique $f$ : la décroissance est **linéaire** (chaque oscillation perd la même amplitude), pas exponentielle.

Le protocole donne :

$$f=\frac14\,k\,\Delta A$$

avec $\Delta A>0$ la diminution d'amplitude entre deux oscillations consécutives.

> [!tip] Astuce pour mesurer $\Delta A$ sans ambiguïté
> $\Delta A$ = différence de hauteur entre **deux maxima consécutifs** (ou deux minima consécutifs) sur le graphe de position. C'est indépendant du choix de l'origine : le décalage dû à la pente (équilibre déplacé de $mg\sin\theta/k$) s'annule. C'est plus sûr que d'utiliser les formules (6) et (7) où il faut bien définir $A_0$, $A_{1/2}$ par rapport à la position naturelle du ressort.

Vérification rapide : à chaque demi-oscillation, le centre d'oscillation est décalé de $\pm f/k$ de part et d'autre de l'équilibre, donc l'amplitude perd $2f/k$ par demi-période, soit $\Delta A=4f/k$ par période. ✔

### Ce qu'il faut faire

1. Retirer les aimants, les poser sur le chariot
2. Tirer, lâcher, enregistrer
3. **5 mesures de $\Delta A$ sur le même graphique**, faire la moyenne
4. Calculer $f$
5. Comparer à $mg\sin\theta$
6. Peut-on négliger $f$ ? (formule 3 et toutes les expériences)

```python
# [outil] frottement sec : f = k ΔA / 4
def frottement_sec(t, x, k, T0, n_max=6):
    """ΔA = baisse de hauteur entre maxima (et minima) consécutifs. Retourne f moyen, écart-type, liste ΔA."""
    fs = 1 / np.median(np.diff(t))
    dist = int(0.7 * T0 * fs)                       # au moins 0,7 période entre 2 pics
    prom = 0.02 * np.ptp(x)
    pics_max, _ = find_peaks(x, distance=dist, prominence=prom)
    pics_min, _ = find_peaks(-x, distance=dist, prominence=prom)
    dA = np.concatenate([
        -np.diff(x[pics_max])[:n_max],              # maxima : x diminue
        np.diff(x[pics_min])[:n_max],               # minima : x augmente
    ])
    f = k * dA.mean() / 4
    return f, k * dA.std(ddof=1) / 4, dA
```

```python
# [exemple] frottement sec
t, x = charger_capstone("frottement_sec.csv", col_t=0, col_y=1)   # position en m
f, df_, dA = frottement_sec(t, x, k=keq, T0=T0_mesure)
m, theta = 0.25, np.radians(30)                                    # à remplacer
print(f"f = {f*1e3:.2f} ± {df_*1e3:.2f} mN ; m g sinθ = {m*g*np.sin(theta):.3f} N")
print(f"rapport f / (m g sinθ) = {f/(m*g*np.sin(theta)):.2%}")
```

> [!question] Peut-on négliger $f$ ?
> Compare $f$ à $mg\sin\theta$ **avec tes valeurs**. En ordre de grandeur, $\Delta A\sim$ quelques mm avec $k\approx1{,}25$ N/m donne $f\sim$ quelques mN, alors que $mg\sin\theta\sim1$ N : $f$ est un effet de l'ordre du %, donc négligeable dans (3) pour un freinage important, mais pas anodin si on veut de la précision (et il explique pourquoi le mouvement « sans aimants » finit par s'arrêter). Conclus avec ton rapport $f/(mg\sin\theta)$ et l'incertitude.

## 5.3 Analyse avec freinage magnétique

### Plan de mesures

1. $T_0$ en régime non amorti (aimants sur le chariot), $m$, $k_{eq}$, $\theta$ dans Excel
2. Repérer **qualitativement** à l'œil les 3 régimes selon la distance aimants–rail
3. Choisir **≈ 10 distances** : 3 sous-amorti (dont 1 à 10 mm d'écart), **4 autour du critique**, 3 sur-amorti
4. Pour chaque distance : (a) oscillation avec le ressort → fit sinus amorti (sous-amorti seulement), (b) lâché sans ressort depuis le haut du rail → $v_\infty$ (si plateau visible ; **réceptionner le chariot en bas du rail** pour ne pas le casser, et ne garder que la zone de vitesse constante)

### Colonnes du template Excel

| Col | Contenu |
|---|---|
| A | distance aimants–rail (mm) |
| B | $v_\infty$ (m/s) |
| C | $b$ via $v_\infty$ : $b=(mg\sin\theta-f)/v_\infty$ |
| D | $b$ via fit Capstone |
| E | $\zeta$ à partir de D |
| F | $\zeta$ à partir de C |
| G | période du fit Capstone |
| H | période théorique $T_0/\sqrt{1-\zeta^2}$ |
| I | figures Capstone utilisées |

### Identifier $b$ dans le fit Capstone

Le fit « sinus amorti » de Capstone a la forme (vérifie bien l'équation affichée dans ta version) :

$$x(t)=A_0\,e^{-\lambda t}\cos(\omega_dt+\varphi)+x_{eq}$$

Par comparaison avec la solution de Q5 : $\lambda=\dfrac{b}{2m}$, donc

$$b=2m\lambda$$

Si Capstone écrit l'exponentielle sous la forme $e^{-t/\tau}$, alors $b=2m/\tau$. Si Capstone donne la fréquence $f_d$, alors $T=1/f_d$.

```python
# [outil] fit sinus amorti et vitesse limite
def sinus_amorti(t, A, lam, T, phi, xeq):
    return A * np.exp(-lam * t) * np.cos(2 * np.pi * t / T + phi) + xeq


def fit_amorti(t, x, m, T_guess):
    """Fit x(t) = A e^{-λt} cos(2πt/T+φ) + xeq. Retourne b = 2mλ, T et leurs incertitudes."""
    t0 = t - t[0]
    xeq0 = x[-max(len(x) // 10, 1):].mean()
    phi0 = 0.0 if x[0] > xeq0 else np.pi
    p0 = [np.ptp(x) / 2, 0.3, T_guess, phi0, xeq0]
    popt, pcov = curve_fit(sinus_amorti, t0, x, p0=p0, maxfev=20000)
    perr = np.sqrt(np.diag(pcov))
    A, lam, T, phi, xeq = popt
    return {"b": 2 * m * lam, "db": 2 * m * perr[1], "T": T, "dT": perr[2],
            "lambda": lam, "popt": popt}


def vitesse_limite(t, v, t1, t2):
    """Moyenne de |v| sur le plateau [t1, t2] choisi à l'œil sur le graphe."""
    mask = (t >= t1) & (t <= t2)
    return np.abs(v[mask]).mean(), np.abs(v[mask]).std(ddof=1)


def v_exp(t, vinf, tau):
    return vinf * (1 - np.exp(-t / tau))


def fit_vitesse(t, v, m):
    """Si le plateau n'est pas atteint : v(t)=v∞(1-e^{-t/τ}) (départ à v=0), τ = m/b."""
    t0 = t - t[0]
    popt, _ = curve_fit(v_exp, t0, np.abs(v), p0=[np.abs(v).max() * 1.2, 0.5])
    return popt[0], popt[1], m / popt[1]       # v∞, τ, b = m/τ


def b_depuis_vinf(m, theta, f, vinf):
    return (m * g * np.sin(theta) - f) / vinf


def zeta(b, m, k):
    return b / np.sqrt(4 * m * k)


def periode_theorique(m, k, z):
    T0 = 2 * np.pi * np.sqrt(m / k)
    return T0 / np.sqrt(1 - z**2) if z < 1 else float("nan")


def b_critique(m, k):
    return 2 * np.sqrt(m * k)
```

```python
# [exemple] une distance aimants-rail
m, k, theta, f = 0.25, keq, np.radians(30), 0.003       # à remplacer par tes valeurs

# (a) avec le ressort (sous-amorti)
t, x = charger_capstone("d12mm_ressort.csv", 0, 1)
res = fit_amorti(t, x, m, T_guess=T0_mesure)
z = zeta(res["b"], m, k)
print(f"b_fit = {res['b']:.3f} ± {res['db']:.3f} kg/s ; ζ = {z:.3f}")
print(f"T_fit = {res['T']:.3f} s ; T_théo = {periode_theorique(m, k, z):.3f} s")

# (b) sans ressort : vitesse limite
t, v = charger_capstone("d12mm_vitesse.csv", 0, 2)       # colonne vitesse
vinf, dvinf = vitesse_limite(t, v, t1=1.5, t2=2.5)       # plateau lu sur le graphe
b_v = b_depuis_vinf(m, theta, f, vinf)
print(f"v∞ = {vinf:.3f} m/s ; b_v = {b_v:.3f} kg/s ; ζ = {zeta(b_v, m, k):.3f}")
print(f"b critique = {b_critique(m, k):.3f} kg/s")
```

### Trouver la distance critique

$b$ diminue très vite quand la distance augmente. Trace $b(d)$ (échelle log en $y$ souvent presque linéaire) et lis $d$ pour lequel $b=b_c=2\sqrt{mk}$ :

```python
# [exemple] b(d) et distance critique
d = np.array([...])        # mm   (colonne A)
b = np.array([...])        # kg/s (D ou C)
bc = b_critique(m, k)
plt.semilogy(d, b, "o-", label="b mesuré")
plt.axhline(bc, ls="--", c="r", label=f"b critique = {bc:.2f} kg/s")
plt.xlabel("Distance aimants–rail (mm)"); plt.ylabel("b (kg/s)"); plt.legend(); plt.grid(True, which="both")
# interpolation de d_critique (b décroissant avec d)
d_crit = np.interp(np.log(bc), np.log(b[::-1]), d[::-1]) if b[0] > b[-1] else np.interp(np.log(bc), np.log(b), d)
print(f"d critique ≈ {d_crit:.1f} mm")
```

### À commenter dans le rapport

- **Comparer $b$ (fit) et $b$ ($v_\infty$)** quand les deux existent (zone de recouvrement vers $\zeta\sim0{,}5$–$0{,}9$). Causes possibles d'écart :
  - frottement sec $f$ (mal connu, négligé ?), alignement des aimants
  - plateau de vitesse pas parfaitement atteint sur 2 m (biais sous-estimant $v_\infty$ donc **surestimant $b$**)
  - force magnétique pas exactement $\propto v$ (non-linéarité)
  - fit sensible à la fenêtre choisie et au bruit, incertitude sur l'épaisseur de plaquette (reproductibilité de la distance)
  - masse des ressorts, angle $\theta$ incertain (surtout pour $b_v$ car $\sin\theta$ intervient)
- **Donner les régimes et distances correspondantes** (sous-amorti : $d>d_{c}$ ; critique : $d\approx d_c$ avec $\zeta\approx1$ ; sur-amorti : $d<d_c$), la plus petite distance donnant le freinage le plus fort

## 5.4 Comparer les 4 régimes sur un même graphe

Setup : ressorts en série, aimants du côté ressort, butée en bas, **zéro** pris contre la butée, **inversion du signe** de la position dans Capstone, démarrage de l'enregistrement quand position $< -5$ mm, arrêt à 10 s.

```python
# [exemple] 4 courbes
courbes = {
    "sans amortissement magnétique": "r54_non_amorti.csv",
    "sous-amorti": "r54_sous.csv",
    "critique": "r54_critique.csv",
    "sur-amorti": "r54_sur.csv",
}
plt.figure(figsize=(9, 5))
for label, fichier in courbes.items():
    t, x = charger_capstone(fichier, 0, 1)
    plt.plot(t - t[0], x, label=label)
plt.xlabel("Temps (s)"); plt.ylabel("Position (m)")
plt.title("Position du chariot pour les 4 régimes d'amortissement")
plt.grid(True); plt.legend(); plt.show()
```

### Réponses attendues

**Comparer $T$ (non amorti) et $T$ (sous-amorti)** : on doit trouver $T_{sous}>T_0$ avec $T_{sous}/T_0=1/\sqrt{1-\zeta^2}$ (formule (2), Q5). Calculer ce rapport avec le $\zeta$ de la section 5.3 et le comparer à la mesure. Si $\zeta\lesssim0{,}3$, l'écart est $<5\%$, donc difficile à voir.

**Quel amortissement est le plus rapide ?** L'amortissement **critique**. Justification : pour $\zeta>1$, la racine lente est

$$r_{lent}=-\omega_0\left(\zeta-\sqrt{\zeta^2-1}\right)\xrightarrow[\zeta\to\infty]{}0^-$$

donc plus on freine, plus le retour est lent (le chariot « rampe »). Pour $\zeta<1$ la décroissance est en $e^{-\zeta\omega_0t}$ avec en plus des oscillations. Le minimum du temps de retour se situe donc à $\zeta=1$ (cohérent avec la théorie et avec la figure 3 du protocole).

---

# 4. Partie 2 — Oscillations couplées (section 6)

Montage : mur — $k_1$ — $m_1$ — $k_2$ — $m_2$ — $k_3$ — $m_3$ — $k_4$ — mur. Les $m_i$ et $k_i$ dépendent du groupe.

## 6.1 Analyse théorique

### 1. Équations du mouvement et modes

Positions $x_i$ mesurées depuis l'équilibre :

$$\begin{aligned}
m_1\ddot x_1&=-k_1x_1+k_2(x_2-x_1)\\
m_2\ddot x_2&=-k_2(x_2-x_1)+k_3(x_3-x_2)\\
m_3\ddot x_3&=-k_3(x_3-x_2)-k_4x_3
\end{aligned}$$

Sous forme matricielle $M\ddot{\vec x}=-K\vec x$ avec

$$M=\begin{pmatrix}m_1&0&0\\0&m_2&0\\0&0&m_3\end{pmatrix},\qquad
K=\begin{pmatrix}k_1+k_2&-k_2&0\\-k_2&k_2+k_3&-k_3\\0&-k_3&k_3+k_4\end{pmatrix}$$

Mode normal : $\vec x=\vec a\cos(\omega t+\varphi)$, tous les chariots oscillent à la même $\omega$ :

$$(K-\omega^2M)\,\vec a=0\quad\Longrightarrow\quad\det(K-\omega^2M)=0$$

C'est une équation cubique en $\omega^2$ : 3 pulsations propres $\omega_1<\omega_2<\omega_3$, et pour chacune on résout $(K-\omega_n^2M)\vec a_n=0$ pour le vecteur propre (à une constante multiplicative près). Si les 3 masses sont égales, c'est le problème aux valeurs propres usuel de $K/m$ (emathhelp.net convient).

> [!example] Cas de contrôle : $m_i=m$ et $k_i=k$
> $\omega_n=2\omega_0\sin\!\left(\dfrac{n\pi}{8}\right)$, $\omega_0=\sqrt{k/m}$, soit $\omega_1=0{,}765\,\omega_0$, $\omega_2=\sqrt2\,\omega_0$, $\omega_3=1{,}848\,\omega_0$.
> Modes : $(1,\sqrt2,1)$, $(1,0,-1)$, $(1,-\sqrt2,1)$.
> Rapports : $\omega_2/\omega_1=1{,}848$, $\omega_3/\omega_1=1+\sqrt2=2{,}414$.
> Utile pour **valider ton code** avant d'entrer les valeurs de ton groupe.

### 2. Orthogonalité des modes

On a $K\vec a_i=\omega_i^2M\vec a_i$. Multiplions par $\vec a_j^{\,T}$ :

$$\vec a_j^{\,T}K\vec a_i=\omega_i^2\,\vec a_j^{\,T}M\vec a_i$$

En échangeant $i\leftrightarrow j$ : $\vec a_i^{\,T}K\vec a_j=\omega_j^2\,\vec a_i^{\,T}M\vec a_j$. Comme $K$ et $M$ sont symétriques, les membres de gauche sont égaux ; en soustrayant :

$$(\omega_i^2-\omega_j^2)\,\vec a_i^{\,T}M\,\vec a_j=0$$

Pour $\omega_i\neq\omega_j$ : $\vec a_i^{\,T}M\vec a_j=0$ (et alors aussi $\vec a_i^{\,T}K\vec a_j=0$). Si $m_1=m_2=m_3$ cela se réduit à $\vec a_i\cdot\vec a_j=0$ (orthogonalité usuelle). Si les masses diffèrent (lestage différent), l'orthogonalité est **au sens de $M$** : à vérifier numériquement avec les vecteurs trouvés.

### 3. Mouvement général

$$\vec x(t)=\sum_{n=1}^{3}\big(C_n\cos\omega_nt+D_n\sin\omega_nt\big)\,\vec a_n=\sum_{n=1}^{3}\alpha_n\cos(\omega_nt+\varphi_n)\,\vec a_n$$

6 constantes fixées par les conditions initiales (3 positions, 3 vitesses). Avec les modes $M$-orthogonaux :

$$C_n=\frac{\vec a_n^{\,T}M\,\vec x(0)}{\vec a_n^{\,T}M\,\vec a_n},\qquad D_n=\frac{\vec a_n^{\,T}M\,\dot{\vec x}(0)}{\omega_n\,\vec a_n^{\,T}M\,\vec a_n}$$

```python
# [outil] modes propres de 3 chariots couplés
def modes_propres(m, k):
    """m = [m1, m2, m3] (kg), k = [k1, k2, k3, k4] (N/m).
    Retourne omega (rad/s), f (Hz), modes (colonnes normalisées : plus grande composante = 1),
    V (colonnes M-orthonormées), M, K."""
    m1, m2, m3 = m
    k1, k2, k3, k4 = k
    M = np.diag([m1, m2, m3])
    K = np.array([[k1 + k2, -k2, 0.0],
                  [-k2, k2 + k3, -k3],
                  [0.0, -k3, k3 + k4]])
    w2, V = eigh(K, M)                       # problème généralisé K a = ω² M a ; VᵀMV = I
    omega = np.sqrt(w2)
    idx = np.argmax(np.abs(V), axis=0)
    modes = V / V[idx, np.arange(3)]         # normalisation : composante dominante = +1
    return omega, omega / (2 * np.pi), modes, V, M, K


def mouvement_general(t, m, k, x0, v0=(0, 0, 0)):
    """x(t) pour des conditions initiales quelconques. Retourne un tableau (3, len(t))."""
    omega, _, _, V, M, _ = modes_propres(m, k)
    q0 = V.T @ M @ np.asarray(x0, float)      # amplitudes modales (cos)
    dq0 = V.T @ M @ np.asarray(v0, float)     # vitesses modales
    t = np.asarray(t)[None, :]
    q = q0[:, None] * np.cos(omega[:, None] * t) + (dq0 / omega)[:, None] * np.sin(omega[:, None] * t)
    return V @ q
```

```python
# [exemple] calcul théorique pour ton groupe
m = [0.30, 0.30, 0.30]          # kg (à remplacer)
k = [2.5, 2.5, 2.5, 2.5]        # N/m (à remplacer par les valeurs mesurées)
omega, f, modes, V, M, K = modes_propres(m, k)
np.set_printoptions(precision=4, suppress=True)
print("ω (rad/s) =", omega)
print("f (Hz)    =", f)
print("rapports f/f1 =", f / f[0])
print("modes (colonnes) =\n", modes)
print("Orthogonalité (VᵀMV) =\n", V.T @ M @ V)          # ≈ identité
print("Orthogonalité des modes normalisés (aᵢᵀ M aⱼ) =\n", modes.T @ M @ modes)  # hors diag ≈ 0
```

## 6.2 Analyse expérimentale

### 6.2.1 Mouvement quelconque + analyse fréquentielle

1. Écarter les chariots de façon **quelconque** (pas selon un mode), lâcher, enregistrer les 3 positions (3 capteurs, même temps)
2. Tracer $x_1(t),x_2(t),x_3(t)$
3. Spectre (Capstone : outil FFT du graphe) ; ou en Python :

```python
# [outil] spectre d'amplitude
def spectre(t, x, zero_pad=8):
    """Amplitude spectrale (fenêtre de Hann). Retourne fréquences (Hz) et amplitude."""
    dt = np.median(np.diff(t))
    x = np.asarray(x) - np.mean(x)            # enlever la composante continue
    w = np.hanning(len(x))
    n = len(x) * zero_pad                      # zero-padding : interpolation, pas plus de résolution
    X = np.abs(np.fft.rfft(x * w, n=n)) * 2 / np.sum(w)
    return np.fft.rfftfreq(n, dt), X


def pics_spectre(freq, X, seuil=0.1, f_max=None):
    mask = np.ones_like(freq, bool) if f_max is None else freq < f_max
    idx, _ = find_peaks(np.where(mask, X, 0), height=seuil * X[mask].max())
    return freq[idx], X[idx]
```

```python
# [exemple] FFT des 3 chariots
fig, ax = plt.subplots(3, 1, sharex=True, figsize=(8, 7))
for i in range(3):
    t, x = charger_capstone("mouvement_quelconque.csv", 0, 1 + i)
    fr, X = spectre(t, x)
    ax[i].plot(fr, X); ax[i].set_ylabel(f"|X{i+1}| (m)")
    print(f"chariot {i+1} : pics à", pics_spectre(fr, X, f_max=3.0)[0].round(3), "Hz")
ax[-1].set_xlabel("Fréquence (Hz)"); ax[0].set_title("Spectres des 3 chariots"); plt.show()
```

**Ce qu'on doit observer et commenter**

- **3 pics** aux mêmes fréquences dans les 3 spectres : ce sont les fréquences propres $f_1,f_2,f_3$ (comparer à la théorie)
- Le poids relatif des pics diffère d'un chariot à l'autre : il reflète la composante du chariot dans chaque mode (ex. le chariot du milieu n'a pas de composante dans le mode $(1,0,-1)$ si les masses/ressorts sont symétriques : pic absent ou très faible)
- Largeur des pics : liée à l'amortissement et à la durée d'acquisition ($\Delta f\approx1/T_{acq}$ : enregistrer assez longtemps, ≥ 20 s si possible)
- Fréquence d'échantillonnage ≥ 50 Hz suffit largement (Nyquist)

### 6.2.2 Modes propres

**Comment visualiser un mode ?** On choisit les conditions initiales **proportionnelles au vecteur propre** : on écarte les chariots de $x_i(0)=\varepsilon\,a_{n,i}$ et on lâche sans vitesse. Alors un seul mode est excité : les 3 chariots oscillent à la **même fréquence**, en phase ou en opposition de phase, avec des amplitudes dans les rapports $a_{n,1}:a_{n,2}:a_{n,3}$.

Pour l'exemple symétrique : mode 1 (1, 1,41, 1) tous dans le même sens ; mode 2 (1, 0, −1) milieu immobile, extrêmes en opposition ; mode 3 (1, −1,41, 1) alternés.

Pratique : prendre $\varepsilon\approx$ 2–3 cm, lire les positions initiales en direct sur Capstone (afficheur numérique) pour régler les écarts.

> [!warning] Imperfections attendues
> L'excitation ne sera jamais parfaite : une petite part des autres modes apparaît (battements). Fitte sur la fenêtre où le mode visé domine, et note-le dans le rapport.

Pour chaque mode : graphe des 3 positions sur la même figure, **fréquence expérimentale** par fit sinusoïdal (ou FFT), rapports $f_2/f_1$ et $f_3/f_1$, comparaison à la théorie.

```python
# [outil] fréquence expérimentale d'un mode (fit sur chaque chariot)
def freq_mode(t, X3, T_guess):
    """X3 : tableau (3, N). Fit sinus amorti sur chaque chariot, retourne f moyenne (Hz) et dispersion."""
    freqs = []
    for x in X3:
        popt, _ = curve_fit(sinus_amorti, t - t[0], x,
                            p0=[np.ptp(x) / 2, 0.05, T_guess, 0.0, np.mean(x)], maxfev=20000)
        freqs.append(1 / abs(popt[2]))
    freqs = np.array(freqs)
    return freqs.mean(), freqs.std(ddof=1)
```

```python
# [exemple] comparaison avec la théorie
f_exp = []
for n, fichier in enumerate(["mode1.csv", "mode2.csv", "mode3.csv"]):
    t, x1 = charger_capstone(fichier, 0, 1)
    _, x2 = charger_capstone(fichier, 0, 2)
    _, x3 = charger_capstone(fichier, 0, 3)
    fm, dfm = freq_mode(t, np.vstack([x1, x2, x3]), T_guess=1 / f[n])
    f_exp.append(fm)
    print(f"mode {n+1} : f_exp = {fm:.4f} ± {dfm:.4f} Hz ; f_théo = {f[n]:.4f} Hz")
f_exp = np.array(f_exp)
print("rapports exp  :", f_exp[1:] / f_exp[0])
print("rapports théo :", f[1:] / f[0])
print("écart relatif (%):", 100 * (f_exp[1:] / f_exp[0] - f[1:] / f[0]) / (f[1:] / f[0]))
```

### Raffiner l'analyse (point 5)

- Peser chaque chariot (avec lest), mesurer **chaque ressort** séparément ($k_1,\dots,k_4$, méthode statique/dynamique) avec incertitudes
- Correction de masse des ressorts : de l'ordre de $m_s/3$ pour un ressort fixé à un mur ; entre deux chariots la répartition est plus subtile. C'est un ordre de grandeur à discuter, pas à faire passer pour exact
- Propager les incertitudes sur les fréquences théoriques (recalculer les modes avec $m_i\pm\delta m_i$, $k_i\pm\delta k_i$ et voir la variation), puis recomparer
- Un petit frottement résiduel décale très peu $\omega_d$ (facteur $\sqrt{1-\zeta^2}$)

---

# 5. Incertitudes (rappel minimal)

- Mesure unique : incertitude = demi-graduation (règle), 1 division du vernier (pied à coulisse), précision de la balance
- Mesures répétées $n$ fois : $u = s/\sqrt n$
- Fonction $y=f(x_1,x_2,\dots)$ : $u_y=\sqrt{\sum\left(\dfrac{\partial f}{\partial x_i}u_i\right)^2}$
- Pour comparer deux valeurs $a$ et $b$ : écart normalisé

$$z=\frac{|a-b|}{\sqrt{u_a^2+u_b^2}}$$

$z<2$ : compatibles ; $z\gg2$ : écart significatif, chercher une cause systématique.

---

# 6. Formules Excel (colonnes du template)

Hypothèse : cellules nommées `m`, `k`, `theta_deg`, `f` (frottement sec), `T0`.

| Grandeur | Formule Excel |
|---|---|
| $k_{eq}$ | `=k1*k2/(k1+k2)` |
| $T_0$ théorique | `=2*PI()*SQRT(m/k)` |
| $b$ via $v_\infty$ (col. C) | `=(m*9.81*SIN(RADIANS(theta_deg))-f)/B2` |
| $b$ via fit (col. D) | `=2*m*lambda` (où `lambda` = coefficient de l'exponentielle dans Capstone) |
| $\zeta$ (col. E, F) | `=D2/SQRT(4*m*k)` , `=C2/SQRT(4*m*k)` |
| $T$ théorique (col. H, si $\zeta<1$) | `=SI(E2<1; T0/RACINE(1-E2^2); "")` |
| $b_c$ | `=2*SQRT(m*k)` |
| $f$ frottement sec | `=k*MOYENNE(plage_dA)/4` |

> [!tip] Reproductibilité
> Mets en haut de la feuille un bloc **Paramètres** (m, k, θ, g, f, T₀ avec leurs unités et incertitudes) et fais pointer toutes les formules dessus. Dans le rapport, explique d'où vient chaque paramètre.

---

# 7. Pièges fréquents

- Oublier de **repeser avec les aimants** (la masse change entre 5.2 et 5.3 si on les enlève)
- Prendre $k$ d'un seul ressort au lieu de $k_{eq}$ (série) pour $\zeta$ et $T_0$
- Confondre $\theta$ en degrés/radians (`np.radians`, `RADIANS` dans Excel)
- Mélanger $b$ (kg/s) et $\lambda=b/2m$ (s⁻¹) en lisant le fit Capstone
- Choisir un plateau de vitesse qui n'en est pas un ; si la zone de vitesse constante n'est pas visible, ne pas utiliser la méthode $v_\infty$ (ou utiliser `fit_vitesse`, avec réserve)
- Fit Capstone sur une fenêtre contenant le démarrage manuel (lâcher) : choisir la zone d'intérêt propre
- Chariots différents sur Capstone (numéro de série !)
- Graphes sans titre, sans unités, trop nombreux : choisir les plus pertinents