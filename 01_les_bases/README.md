# 🏗️ Module 01 : Les bases (variables, types & contrôle)

> 🎯 **Objectif** : savoir **stocker** des informations (variables), connaître les **types** de
> base, et **piloter** le déroulement d'un programme avec les conditions et les boucles. Ce sont
> les 4 briques avec lesquelles on construit **tout** le reste.

:::reflexion Réfléchis d'abord : les 4 verbes de tout programme
Avant de retenir *quoi taper*, comprends **pourquoi** ces briques existent. Pour
dérouler n'importe quel raisonnement, un programme n'a besoin que de **4 actions** :

1. **Retenir** une information → une **variable**.
2. **Calculer / transformer** une valeur → les **types** et les **opérateurs**.
3. **Décider** selon la situation → les **conditions** (`if`).
4. **Répéter** sans se fatiguer → les **boucles** (`for`, `while`).

Garde cette grille en tête : quand tu bloqueras sur un exercice, demande-toi
« il me manque quel verbe : **retenir**, **calculer**, **décider** ou **répéter** ? ».
C'est le premier réflexe de décomposition (revois la méthode dans
[🧭 Penser comme un dev](../penser_comme_un_dev)).
:::

---

## 1. Les variables : donner un nom à une valeur

Une **variable** est une **étiquette** posée sur une valeur, pour pouvoir la réutiliser par son
nom plus tard. On la crée avec le signe `=`, qui se lit « **reçoit** » (et **pas** « égal ») :

```python
age = 25
```

Ça se lit : « la variable `age` **reçoit** la valeur `25` ». À partir de là, écrire `age` dans
le code, c'est écrire `25`.

> 🧠 **L'image** : une variable est une **boîte étiquetée**. `age = 25` met `25` dans une boîte
> étiquetée `age`. Plus tard, `age = 30` jette l'ancien contenu et met `30` à la place.

### Le typage dynamique

En Python, tu n'annonces **pas** le type d'une variable : Python le **devine** d'après la valeur.

```python
age = 25            # un nombre entier        → type int
nom = "Marc"        # du texte                → type str  (string)
taille = 1.75       # un nombre à virgule     → type float (à cause du point décimal)
est_content = True  # vrai ou faux            → type bool (booléen)
```

Pour vérifier le type d'une valeur, utilise la fonction `type()` :

```python
print(type(age))    # <class 'int'>
print(type(nom))    # <class 'str'>
```

> ⚠️ **Python est sensible à la casse** : `age`, `Age` et `AGE` sont **trois variables
> différentes**. Une erreur de majuscule est une cause classique de `NameError`.

### Bien nommer ses variables

Un bon nom explique **ce que contient** la boîte. Conventions Python :

- en **minuscules**, mots séparés par des `_` : `nom_joueur`, `prix_total` (style *snake_case*) ;
- **descriptif** : `vitesse` plutôt que `v`, `nombre_essais` plutôt que `n` ;
- pas d'accents, pas d'espaces, ne commence pas par un chiffre.

---

## 2. Les types de base, en détail

| Type | À quoi ça sert | Exemples |
|------|----------------|----------|
| `int` | nombres **entiers** | `0`, `42`, `-7` |
| `float` | nombres **à virgule** | `1.75`, `-0.5`, `3.0` |
| `str` | **texte** (entre guillemets) | `"bonjour"`, `'A'`, `""` |
| `bool` | **vrai / faux** | `True`, `False` |

### Opérations sur les nombres

```python
print(7 + 3)    # 10   addition
print(7 - 3)    # 4    soustraction
print(7 * 3)    # 21   multiplication
print(7 / 3)    # 2.33...  division (donne TOUJOURS un float)
print(7 // 3)   # 2    division ENTIÈRE (on garde le quotient)
print(7 % 3)    # 1    MODULO : le reste de la division (utile pour "est-ce pair ?")
print(2 ** 10)  # 1024 puissance (2 à la puissance 10)
```

> 🔎 Le **modulo** `%` revient souvent : `nombre % 2 == 0` teste si un nombre est **pair**.
> (Attention : ce même symbole `%` a un autre usage avec le texte — voir
> [`../LES_SYMBOLES.md`](../LES_SYMBOLES.md).)

### Opérations sur le texte

```python
prenom = "Ada"
nom = "Lovelace"
print(prenom + " " + nom)   # "Ada Lovelace"  : le + COLLE les chaînes (concaténation)
print("ha" * 3)             # "hahaha"        : le * RÉPÈTE une chaîne
print(len(prenom))          # 3               : len() donne la longueur
```

### Les f-strings : mélanger texte et variables

La façon **moderne et lisible** d'insérer des variables dans du texte : on met un `f` juste
avant le guillemet ouvrant, et on place les variables entre **accolades** `{ }`.

```python
nom = "Baba"
score = 100
print(f"Joueur : {nom} | Score : {score}")   # Joueur : Baba | Score : 100
```

> 🧠 **Pourquoi le `f` ?** Il signale à Python : « dans ce texte, ce qui est entre `{ }` n'est
> **pas** du texte littéral, c'est une **expression à calculer** ». Sans le `f`, tu obtiendrais
> littéralement `{nom}` à l'écran.

### Convertir un type en un autre

Les valeurs tapées au clavier ou lues dans un fichier sont du **texte**. Pour calculer avec,
il faut les **convertir** :

```python
age_texte = "25"          # c'est du texte, PAS un nombre
age = int(age_texte)      # int(...) convertit le texte en entier → 25
print(age + 1)            # 26

prix = float("1.75")      # texte → nombre à virgule → 1.75
message = str(42)         # nombre → texte → "42"
```

> ⚠️ Erreur classique : `"25" + 1` plante (`TypeError`) car on ne peut pas additionner du texte
> et un nombre. Il faut d'abord `int("25") + 1`.

---

## 3. Prendre des décisions : `if` / `elif` / `else`

Un programme doit souvent **choisir** quoi faire selon une situation. C'est le rôle du `if`
(« si »).

```python
age = 20

if age >= 18:
    print("Majeur")
elif age >= 13:
    print("Adolescent")
else:
    print("Enfant")
```

Comment ça se lit :

- **`if condition:`** — si la condition est vraie, on exécute le bloc indenté en dessous.
- **`elif autre_condition:`** — « sinon, si… » : testé seulement si le `if` était faux.
  (On peut en mettre plusieurs, ou aucun.)
- **`else:`** — « sinon » : exécuté si **rien** au-dessus n'était vrai. (Facultatif.)

### Le `:` et l'indentation : la règle d'or de Python

Deux choses **obligatoires** ici, et c'est ce qui déroute le plus au début :

1. La ligne du `if` se **termine par deux-points** `:`. Le `:` annonce : « un bloc commence ».
2. Les lignes du bloc sont **décalées vers la droite** (par convention **4 espaces**). C'est
   cette **indentation** qui dit à Python « ces lignes appartiennent au `if` ». D'autres
   langages utilisent des accolades `{ }` ; Python, lui, utilise l'**alignement du texte**.

```python
if age >= 18:
    print("Cette ligne est DANS le if")   # indentée → fait partie du if
    print("Celle-ci aussi")
print("Cette ligne est DEHORS")           # pas indentée → s'exécute toujours
```

> ⚠️ Mélanger espaces et tabulations, ou mal aligner, provoque une `IndentationError`.
> Configure ton éditeur pour insérer **4 espaces** quand tu appuies sur Tab.

### Les opérateurs de comparaison et logiques

```python
==   # égal à        (À NE PAS confondre avec = qui AFFECTE une valeur)
!=   # différent de
<  <=  >  >=          # inférieur, inférieur ou égal, supérieur, supérieur ou égal
```

On combine des conditions avec `and`, `or`, `not` :

```python
if age >= 18 and a_le_permis:     # les DEUX doivent être vraies
    print("Peut conduire")

if est_weekend or est_ferie:      # AU MOINS une des deux
    print("Repos")

if not est_connecte:              # inverse : vrai si est_connecte est faux
    print("Veuillez vous connecter")
```

> 🔑 **`=` vs `==`** : le piège n°1 des débutants. `=` **range** une valeur dans une variable ;
> `==` **compare** deux valeurs et répond `True`/`False`. Dans un `if`, c'est presque toujours `==`.

---

## 4. Répéter des actions : les boucles

### La boucle `for` — « pour chaque… »

On l'utilise pour **parcourir** une série d'éléments, ou **répéter** un nombre **connu** de fois.

```python
# Parcourir une liste, élément par élément
for fruit in ["pomme", "poire", "kiwi"]:
    print(fruit)        # affiche pomme, puis poire, puis kiwi
```

Ici `fruit` est une **variable que la boucle remplit toute seule** : au 1er tour elle vaut
`"pomme"`, au 2e `"poire"`, au 3e `"kiwi"`. Tu n'écris **jamais** `fruit = ...` toi-même —
c'est le `for` qui met une nouvelle valeur dedans à chaque tour.

#### `range()` : répéter avec un compteur

Quand tu veux répéter un nombre **précis** de fois, tu utilises `range()`, qui fabrique une
suite de nombres :

```python
for i in range(5):          # range(5) → 0, 1, 2, 3, 4  (5 nombres, en partant de 0)
    print(f"Tour numéro {i}")
```

Ce qui s'affiche, **tour par tour** — observe bien que `i` **change de valeur à chaque passage** :

```
Tour numéro 0      ← au 1er tour, i vaut 0
Tour numéro 1      ← au 2e tour, i vaut 1
Tour numéro 2      ← i vaut 2
Tour numéro 3      ← i vaut 3
Tour numéro 4      ← i vaut 4, PUIS la boucle s'arrête (5 est exclu)
```

> 🧠 **`i`, c'est quoi ?** Juste une variable (on aurait pu l'appeler `tour` ou `compteur`). La
> boucle y range **le nombre courant** à chaque tour. C'est ton compteur : tu peux t'en servir
> dans le corps de la boucle, comme ici dans la f-string `{i}`.

> 🔑 **La règle du `range` à retenir** : `range(5)` **commence à 0** et **s'arrête AVANT 5**. Tu
> obtiens `0, 1, 2, 3, 4` — bien **5** valeurs, mais la dernière est **4**, pas 5. C'est le piège
> n°1 des débutants : « pourquoi ça s'arrête à 4 ? » → parce que **la borne de fin est exclue**.

Les façons d'utiliser `range` :

```python
range(5)         # → 0, 1, 2, 3, 4      (de 0 à 5 exclu)
range(2, 6)      # → 2, 3, 4, 5         (de 2 à 6 exclu : on choisit le DÉBUT)
range(1, 11)     # → 1, 2, 3, …, 10     (pratique pour compter de 1 à 10)
range(0, 10, 2)  # → 0, 2, 4, 6, 8      (le 3e nombre = le PAS, ici on avance de 2 en 2)
```

> 💡 Besoin de compter **de 1 à n inclus** (et pas à partir de 0) ? Écris `range(1, n + 1)`. Le
> `+ 1` est là parce que la fin est exclue : pour **inclure** `n`, il faut viser « un cran plus
> loin ». Exemple : pour aller de 1 à 5, on écrit `range(1, 6)`.

#### Se servir de `i` comme position (index) dans une liste

Chaque élément d'une liste a une **position** (un *index*), qui commence à **0**. Avec
`range(len(liste))`, `i` prend justement chaque position, et `liste[i]` donne l'élément à cette
position :

```python
noms = ["Ada", "Bob", "Zoé"]

for i in range(len(noms)):      # len(noms) vaut 3 → i prend 0, puis 1, puis 2
    print(f"Position {i} : {noms[i]}")
```

```
Position 0 : Ada       ← i = 0, noms[0] = "Ada"
Position 1 : Bob       ← i = 1, noms[1] = "Bob"
Position 2 : Zoé       ← i = 2, noms[2] = "Zoé"
```

> 🔎 La plupart du temps tu n'as **pas besoin** de la position : `for nom in noms:` suffit et se
> lit plus simplement. Utilise `range(len(...))` **seulement** quand tu as vraiment besoin du
> numéro `i` (pour l'afficher, ou pour comparer deux listes position par position).

### La boucle `while` — « tant que… »

On l'utilise quand on **ne sait pas d'avance** combien de fois répéter : on continue **tant
qu'**une condition reste vraie.

```python
compteur = 3
while compteur > 0:           # tant que compteur est strictement positif
    print(f"{compteur}...")
    compteur -= 1             # compteur = compteur - 1  → IMPORTANT : fait avancer vers la fin
print("Décollage !")
```

> ⚠️ **La boucle infinie** : si tu oublies de faire évoluer la condition (ici `compteur -= 1`),
> le `while` ne s'arrête **jamais**. Pour interrompre un programme bloqué dans le terminal :
> **`Ctrl + C`**.

### `for` ou `while` : lequel choisir ?

| Tu connais le nombre de tours ? | Utilise |
|---------------------------------|---------|
| Oui (parcourir une liste, répéter N fois) | **`for`** |
| Non (attendre une condition, une saisie valide…) | **`while`** |

### Les raccourcis d'affectation

```python
compteur += 1   # compteur = compteur + 1
total   -= 5    # total = total - 5
prix    *= 2    # prix = prix * 2
```

---

## 5. Tout assembler : un mini-programme

```python
# Demande un nombre et dit s'il est pair, impair, ou nul
texte = input("Entre un nombre entier : ")   # input() lit ce que l'utilisateur tape (du TEXTE)
nombre = int(texte)                          # on convertit ce texte en entier pour calculer

if nombre == 0:
    print("C'est zéro.")
elif nombre % 2 == 0:                        # reste nul dans la division par 2 → pair
    print(f"{nombre} est pair.")
else:
    print(f"{nombre} est impair.")
```

Ce court programme réunit **tout le module** : variable, conversion de type, `input`, `if/elif/else`,
modulo, f-string. Relis-le jusqu'à comprendre **chaque** symbole.

---

## 🤖 Pourquoi ce module est essentiel pour l'IA

Tout code IA commence par des **variables** (stocker des données), des **conditions** (si
la prédiction est bonne...) et des **boucles** (parcourir chaque donnée). Exemple concret :
```python
precision = 0.92
if precision > 0.9:
    print("Le modèle est bon !")
for epoch in range(10):
    print(f"Entraînement tour {epoch}...")
```
Sans ce module, tu ne peux rien lire ni écrire en IA.

---

## 🏁 S'entraîner

### 🎯 Les exercices — commence par ça

**[`exercices.py`](./exercices.py)** : 6 petits exercices que tu écris **toi-même**. Pas de
fonction, pas de correction automatique compliquée. Chacun te donne :

- les **valeurs de départ** (elles sont écrites, tu les vois : `nombre = 7`…) ;
- un **résultat attendu** affiché juste à côté ;
- un **espace** où tu écris ton code.

Tu lances, tu regardes ce qui s'affiche, tu **compares** au résultat attendu. Tu peux changer
les valeurs de départ pour tester toi-même.

```bash
python3 01_les_bases/exercices.py
```

Bloqué après un vrai essai ? Le corrigé commenté est dans [`solutions.py`](./solutions.py)
(tu peux le lancer pour voir tous les résultats attendus).

### 🔬 Pour explorer (dans le terminal ou un fichier à toi, sans correction automatique)

1. **Lis et lance** [`bases.py`](./bases.py), puis modifie les valeurs pour observer les
   changements (mets `vie = 10`, change le score…).
2. **Table de multiplication (à coder toi-même)** : écris une boucle qui affiche la table de 7
   (de `7 x 1` à `7 x 10`).

<details>
<summary>💡 Solution — table de 7</summary>

```python
for i in range(1, 11):           # 1 à 10 inclus
    print(f"7 x {i} = {7 * i}")
```
</details>

## 🔬 Le raisonnement en action

**Problème** : afficher, pour chaque nombre de 1 à 20, s'il est **pair** ou **impair**.

On ne se jette pas sur le clavier : on écrit d'abord les **étapes** en français
(pseudo-code), *ensuite* on traduit.

```pseudo
POUR n DE 1 À 20 :
    SI n est pair (n % 2 == 0) :
        afficher "n : pair"
    SINON :
        afficher "n : impair"
```

La traduction est alors quasi mécanique — 1 ligne de pseudo-code ≈ 1 ligne de Python :

```python
for n in range(1, 21):        # 21 exclu → on s'arrête à 20
    if n % 2 == 0:
        print(f"{n} : pair")
    else:
        print(f"{n} : impair")
```

:::defi 🧪 Prédis la sortie
Avant de cliquer sur **▶ Essayer** : que va afficher ce code ? Réfléchis (trace-le
à la main !), **puis** vérifie.
```python
x = 5
x = x + 3
x = x * 2
print(x)
```
:::

➡️ **Prochaine étape** : [module 02 — les collections](../02_collections/) (listes, dictionnaires…).
