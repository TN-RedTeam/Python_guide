# ⚙️ Module 06 : Itérateurs & générateurs

> 🎯 **Objectif** : comprendre **comment** une boucle `for` parcourt les choses (les
> *itérables*), et découvrir les **générateurs** (`yield`) qui produisent des valeurs **une par
> une** sans saturer la mémoire. Concepts avancés mais très utiles dès qu'on manipule beaucoup
> de données.

---

## 1. Itérable vs itérateur (la distinction clé)

- Un **itérable** est tout ce qu'on peut parcourir avec un `for` : liste, tuple, dict, set,
  chaîne de caractères, fichier ouvert…
- Un **itérateur** est l'objet qui **se souvient où il en est** pendant le parcours et donne
  l'élément suivant à la demande.

Sous le capot, `for x in liste:` fait deux choses :

```python
nombres = [10, 20, 30]
it = iter(nombres)     # 1) iter() demande un ITÉRATEUR à l'itérable
print(next(it))        # 2) next() réclame l'élément suivant → 10
print(next(it))        # → 20
print(next(it))        # → 30
print(next(it))        # → StopIteration : il n'y a plus rien (la boucle for s'arrête là)
```

> 🧠 **L'image** : l'itérable est un **livre** ; l'itérateur est le **marque-page** qui retient
> la page courante. `next()` tourne la page ; quand il n'y a plus de page, c'est `StopIteration`.
> Une boucle `for` fait tout ça pour toi, automatiquement.

---

## 2. Les générateurs (`yield`) : produire à la demande

Un **générateur** est une fonction qui, au lieu de tout calculer puis `return`, **livre ses
valeurs une à une** avec `yield`. Elle se met en **pause** après chaque `yield` et reprend là
où elle s'était arrêtée au `next` suivant.

```python
def compter_jusqua(limite):
    n = 0
    while n < limite:
        yield n          # LIVRE n, puis met la fonction EN PAUSE ici
        n += 1           # à la reprise, on continue à partir d'ici

for valeur in compter_jusqua(3):
    print(valeur)        # 0, puis 1, puis 2
```

### `yield` vs `return`

| | `return` | `yield` |
|--|----------|---------|
| effet | **termine** la fonction et rend **une** valeur | **suspend** la fonction et livre une valeur |
| combien de fois | une seule | autant qu'on veut, à la demande |
| mémoire | la valeur (ou la liste entière) est en mémoire | une seule valeur à la fois |

### Pourquoi c'est puissant : la mémoire

```python
def un_milliard():
    n = 0
    while n < 1_000_000_000:
        yield n
        n += 1
```

Mettre un milliard de nombres dans une **liste** ferait exploser la RAM. Le générateur, lui,
**ne garde qu'un nombre à la fois** : il en produit un, tu le traites, il en produit le suivant.
Mémoire quasi nulle, quelle que soit la taille.

> 🔑 **Quand utiliser un générateur ?** Dès que tu parcours une **grande** quantité de données
> que tu n'as pas besoin de garder toutes en même temps : lignes d'un énorme fichier, flux
> réseau, suite infinie. Tu **consommes au fur et à mesure**.

> ⚠️ Un générateur est **à usage unique** : une fois parcouru, il est « vide ». Pour le
> reparcourir, il faut le recréer (rappeler la fonction).

---

## 3. Les compréhensions : transformer/filtrer en une ligne

Une **compréhension de liste** condense un `for` (+ un `if` optionnel) qui construit une liste.

```python
# Version longue
carres = []
for n in nombres:
    if n > 2:
        carres.append(n ** 2)

# Version compréhension (identique, en une ligne)
carres = [n ** 2 for n in nombres if n > 2]
```

On lit dans l'ordre : `[` **ce qu'on garde** `for` **chaque élément** `in` **la source** `if`
**condition** `]`.

```python
[n ** 2 for n in nombres]              # transforme
[n for n in nombres if n % 2 == 0]     # filtre (que les pairs)
[mot.upper() for mot in mots]          # applique une méthode à chacun
```

Ça existe aussi pour les dicts et les sets :

```python
{mot: len(mot) for mot in mots}        # dict en compréhension : {"chat": 4, ...}
{n % 3 for n in nombres}               # set en compréhension (valeurs uniques)
```

### L'expression génératrice : compréhension paresseuse

Avec des **parenthèses** au lieu de crochets, tu obtiens un **générateur** (rien n'est calculé
tant qu'on ne consomme pas) — parfait pour enchaîner sans créer de liste intermédiaire :

```python
total = sum(n ** 2 for n in nombres)   # pas de liste créée : on additionne au vol
```

> 🧠 `[...]` construit **toute** la liste en mémoire ; `(...)` crée un **générateur** qui
> produit à la demande. Pour juste parcourir/agréger, préfère `(...)`.

---

## 🏁 S'entraîner

### 🎯 L'exercice principal — commence par ça

**[`exercices.py`](./exercices.py)** : des fonctions à compléter (filtrer, transformer, et écrire
un **générateur** de nombres pairs), avec **correction automatique** (✅/❌ en direct). C'est
**LE** fichier où tu écris ton code pour ce module.

```bash
python3 06_iterateurs_generateurs/exercices.py
```

Bloqué après un vrai essai ? Le corrigé commenté est dans [`solutions.py`](./solutions.py).

### 🔬 Pour explorer (dans le terminal ou un fichier à toi, sans correction automatique)

1. **Lis et lance** [`generateurs.py`](./generateurs.py) (différence de consommation mémoire).
2. **Filtre par initiale (à coder toi-même)** : à partir de `noms = ["Alice", "Bob", "Anna",
   "Tom"]`, construis la liste de ceux qui commencent par `"A"` (avec une compréhension de liste).

<details>
<summary>💡 Solution — filtre sur l'initiale</summary>

```python
noms = ["Alice", "Bob", "Anna", "Tom"]
en_a = [nom for nom in noms if nom.startswith("A")]   # startswith : commence par
print(en_a)   # ['Alice', 'Anna']
```
</details>

➡️ **Prochaine étape** : [module 07 — débugger](../07_debugger/).
