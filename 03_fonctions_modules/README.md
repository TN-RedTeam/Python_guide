# 🛠️ Module 03 : Fonctions & modules

> 🎯 **Objectif** : arrêter de copier-coller le même code. Une **fonction** emballe une suite
> d'instructions sous un **nom** réutilisable ; un **module** regroupe des fonctions dans un
> fichier qu'on peut **importer**. C'est la base de tout code organisé.

:::reflexion Réfléchis d'abord : une fonction = un sous-problème
Souviens-toi de la **décomposition** (revois [🧭 Penser comme un dev](../penser_comme_un_dev)) :
on découpe un gros problème en petites étapes. Une **fonction, c'est exactement
ça, rendu concret** — chaque sous-problème devient une petite machine **nommée**,
qu'on teste et réutilise séparément.

Le bon réflexe : dès qu'une étape de ton pseudo-code mérite un nom
(`calculer_tva`, `est_valide`, `charger_données`), fais-en une fonction. Ton
programme se lit alors comme la **liste de ses étapes**, plus comme un mur de code.
:::

---

## 1. Pourquoi des fonctions ?

Imagine que tu calcules une TVA à dix endroits. Sans fonction, tu réécris (et tu re-bugues) le
calcul dix fois. Avec une fonction, tu l'écris **une fois** et tu l'appelles par son nom.

> 🧠 **L'image** : une fonction est une **machine**. Tu lui donnes des **ingrédients**
> (les arguments), elle fait son travail, et elle te **rend** un résultat (`return`). Une fois
> construite, tu n'as plus à savoir *comment* elle marche : tu l'utilises.

---

## 2. Définir une fonction : `def`

```python
def creer_message(nom, role="Guerrier"):
    """Construit un message de bienvenue (ceci est la docstring)."""
    return f"Bienvenue {nom}, le {role} !"
```

Décortiquons **chaque morceau** de la première ligne — c'est le squelette à connaître par cœur :

| Morceau | Nom | Rôle |
|---------|-----|------|
| `def` | mot-clé | annonce « je **définis** une fonction » |
| `creer_message` | le **nom** | comment on l'appellera ensuite |
| `(nom, role=...)` | les **paramètres** | les ingrédients attendus (entre parenthèses) |
| `:` | deux-points | annonce le bloc indenté qui suit |
| `"""..."""` | docstring | décrit la fonction (s'affiche avec `help`) |
| `return ...` | mot-clé | la **valeur renvoyée** à celui qui appelle |

### Définir ≠ appeler

Définir une fonction ne l'exécute **pas** : c'est juste écrire la recette. Il faut l'**appeler**
(avec des parenthèses) pour qu'elle travaille :

```python
message = creer_message("Baba")    # APPEL → exécute la fonction et récupère le résultat
print(message)                     # "Bienvenue Baba, le Guerrier !"
```

> 🔎 **`creer_message` sans parenthèses** désigne la fonction elle-même (l'objet machine) ;
> **`creer_message(...)`** la **fait tourner**. Les parenthèses = « lance-la ». (Voir
> [`../LES_SYMBOLES.md`](../LES_SYMBOLES.md).)

---

## 3. Paramètres, arguments, valeurs par défaut

- **Paramètre** = le nom dans la définition (`nom`, `role`). C'est la *case à remplir*.
- **Argument** = la valeur réelle qu'on passe à l'appel (`"Baba"`). C'est ce qu'on *met dans la case*.

### Arguments positionnels vs nommés

```python
creer_message("Gandalf", "Mage")            # POSITIONNELS : l'ordre compte (nom, puis role)
creer_message(role="Mage", nom="Gandalf")   # NOMMÉS : l'ordre n'a plus d'importance
```

> 🔑 Les arguments **nommés** (`role="Mage"`) sont précieux : ils rendent l'appel **lisible** et
> évitent de se tromper d'ordre. C'est exactement le `exist_ok=True` que tu vois dans le code
> réel (détaillé dans [`../LES_SYMBOLES.md`](../LES_SYMBOLES.md)).

### Valeur par défaut

`role="Guerrier"` donne une valeur **par défaut** : si l'appelant ne fournit pas `role`, c'est
`"Guerrier"` qui est utilisé. Ça rend un argument **facultatif**.

```python
creer_message("Baba")            # role non fourni → "Guerrier"
creer_message("Baba", "Mage")    # role fourni → "Mage"
```

---

## 4. `return` : rendre un résultat (≠ `print`)

C'est **la** confusion classique du débutant. Les deux sont très différents :

```python
def double(x):
    return x * 2        # REND la valeur à l'appelant (utilisable ensuite)

def double_affiche(x):
    print(x * 2)        # AFFICHE seulement à l'écran (rien n'est récupérable)
```

```python
r = double(5)           # r vaut 10 → je peux le réutiliser : r + 1, etc.
r = double_affiche(5)   # ça affiche 10, mais r vaut None (rien n'a été renvoyé)
```

> 🧠 **`return` = la machine te REND un produit** (tu peux le ranger, le réutiliser).
> **`print` = la machine affiche un panneau** (tu le vois, mais tu ne peux rien en faire après).
> Une fonction qui ne fait que calculer doit **`return`**, pas `print`.
>
> ⚠️ `return` **termine** la fonction immédiatement : le code après n'est pas exécuté.

---

## 5. `*args` et `**kwargs` : un nombre variable d'arguments

Parfois on ne sait pas combien d'arguments seront passés (pense à `print("a", "b", "c", ...)`).
Les étoiles servent à ça.

### `*args` — emballer les arguments **positionnels** dans un tuple

```python
def faire_somme(*nombres):       # le * "ramasse" tous les arguments positionnels
    total = 0
    for n in nombres:            # nombres est un TUPLE : (10, 20, 30)
        total += n
    return total

faire_somme(10, 20, 30)          # → 60
faire_somme(1, 2, 3, 4, 5)       # → 15   (marche avec n'importe combien)
```

### `**kwargs` — emballer les arguments **nommés** dans un dict

```python
def profil(**infos):             # le ** "ramasse" tous les arguments nommés
    for cle, valeur in infos.items():   # infos est un DICT : {"nom": "Ada", "age": 36}
        print(f"{cle} : {valeur}")

profil(nom="Ada", age=36, ville="Londres")
```

### Les étoiles servent aussi à **déballer** (à l'appel)

```python
valeurs = [10, 20, 30]
faire_somme(*valeurs)            # déballe la liste → faire_somme(10, 20, 30)

donnees = {"nom": "Ada", "age": 36}
profil(**donnees)                # déballe le dict → profil(nom="Ada", age=36)
```

> 🔑 **La règle universelle** : `*`/`**` **dans un `def`** = « j'**emballe** ce qui arrive » ;
> `*`/`**` **dans un appel** = « je **déballe** ce que j'envoie ». Les noms `args`/`kwargs` sont
> une **convention** ; seules les étoiles comptent.

---

## 6. Une fonction peut en recevoir une autre (et les `lambda`)

En Python, une fonction est une **valeur comme une autre** : tu peux la ranger dans une variable
et même la **passer en argument** à une autre fonction. (Remarque : on passe le **nom sans les
parenthèses** — `dire_bonjour`, pas `dire_bonjour()` — sinon on passe son *résultat*, pas la
fonction elle-même.)

```python
def dire_bonjour(nom):
    return f"Bonjour {nom}"

def appliquer(fonction, valeur):     # `fonction` est une fonction reçue en argument
    return fonction(valeur)          # on l'APPELLE ici, avec ()

print(appliquer(dire_bonjour, "Ada"))   # "Bonjour Ada"
```

### `lambda` : une mini-fonction écrite en une ligne

Quand la fonction est si courte qu'écrire un `def` complet serait lourd, on peut la créer **à la
volée** avec `lambda`. Ces deux écritures sont **équivalentes** :

```python
def double(x):          # la version classique
    return x * 2

double = lambda x: x * 2   # la version lambda : lambda <paramètres>: <résultat>
```

Lis `lambda x: x * 2` comme : « une fonction qui prend `x` et **renvoie** `x * 2` » (le `return`
est implicite). C'est surtout pratique pour la **passer directement en argument**, sans lui
donner de nom :

```python
nombres = [1, 2, 3]
resultats = [(lambda x: x * 2)(n) for n in nombres]   # [2, 4, 6]

# Cas classique : trier par un critère
mots = ["python", "go", "rust"]
mots.sort(key=lambda mot: len(mot))   # trie par longueur → ["go", "rust", "python"]
```

> 🧠 **À retenir** : `lambda` ne fait rien de plus qu'un `def` ; c'est juste une **écriture
> raccourcie** pour les fonctions d'une ligne. Si la logique est longue, garde un vrai `def`
> (c'est plus lisible).

---

## 7. Les modules : réutiliser du code entre fichiers

Un **module**, c'est simplement **un fichier `.py`**. L'`import` permet d'utiliser les fonctions
d'un fichier dans un autre — ou celles fournies par Python.

### Importer la bibliothèque standard

```python
import math                 # importe TOUT le module math
print(math.sqrt(16))        # 4.0   → on préfixe par "math."

from math import sqrt       # importe SEULEMENT sqrt
print(sqrt(16))             # 4.0   → plus besoin du préfixe

from math import pi as PI   # importe pi sous un autre nom (alias)
print(PI)                   # 3.14159...
```

| Forme | Quand l'utiliser |
|-------|------------------|
| `import math` | tu veux plusieurs choses du module ; garde le préfixe = clair |
| `from math import sqrt` | tu n'utilises qu'une ou deux fonctions précises |
| `import numpy as np` | nom long : on raccourcit avec un alias conventionnel |

> ⚠️ Évite `from math import *` (importe tout sans préfixe) : on ne sait plus d'où vient chaque
> nom, et ça peut écraser tes propres variables.

### Importer TES propres fichiers

Si tu as `outils_math.py` et `usage_module.py` dans le même dossier :

```python
# dans usage_module.py
import outils_math                       # le nom du fichier, SANS le .py
print(outils_math.aire_cercle(2))

from outils_math import aire_cercle      # ou juste la fonction voulue
print(aire_cercle(2))
```

> 🧠 **Comment Python trouve-t-il le fichier ?** Il cherche d'abord dans le dossier du script
> lancé. C'est pourquoi un module à toi, posé à côté, s'importe par son simple nom.

➡️ Pour organiser **plusieurs** modules en *package* (avec `__init__.py`), voir
[`../COMPRENDRE_LE_CODE.md`](../COMPRENDRE_LE_CODE.md#32-__init__py--le-fichier-qui-fait-dun-dossier-un--paquet-).

---

## 🤖 Pourquoi ce module est essentiel pour l'IA

En IA, **tout est fonction** : `model.fit()`, `model.predict()`, `train_test_split()`. Tu passes
des arguments (tes données), la fonction fait le calcul, et elle te renvoie un résultat. Et tu
utilises `import` pour charger NumPy, pandas, scikit-learn... Exemple :
```python
from sklearn.model_selection import train_test_split   # import d'une fonction

X_train, X_test = train_test_split(X, test_size=0.2)  # argument nommé = module 03 !
```

---

## 🏁 S'entraîner

### 🎯 Les exercices — commence par ça

**[`exercices.py`](./exercices.py)** : des petits exercices que tu écris **toi-même** (ici, tu
écris la fonction PUIS tu l'appelles avec une valeur que tu choisis). Pas de correction
automatique : chaque exercice montre un **résultat attendu**, tu lances, tu **compares**.

```bash
python3 03_fonctions_modules/exercices.py
```

Bloqué après un vrai essai ? Le corrigé commenté est dans [`solutions.py`](./solutions.py).

### 🔬 Pour explorer (dans le terminal, sans correction automatique)

1. **Lis et lance** [`fonctions.py`](./fonctions.py) (valeurs par défaut, `*args`).
2. **Lis et lance** [`usage_module.py`](./usage_module.py) : il importe le module
   [`outils_math.py`](./outils_math.py). Repère les **deux** formes d'import.

## 🔬 Le raisonnement en action

**Problème** : écrire une fonction qui dit si un mot est un **palindrome** (se lit
pareil dans les deux sens : *kayak*, *radar*).

Décomposons : « se lit pareil à l'envers » = *le mot est égal à lui-même inversé*.
Petit piège à anticiper (cas limite) : les majuscules — on **normalise** d'abord.

```pseudo
FONCTION est_palindrome(mot) :
    propre ← mot en minuscules
    RENVOYER (propre == propre à l'envers)
```

```python
def est_palindrome(mot):
    propre = mot.lower()          # normalise : "Kayak" -> "kayak"
    return propre == propre[::-1]  # [::-1] = la chaîne à l'envers

print(est_palindrome("Kayak"))    # True
print(est_palindrome("Python"))   # False
```

:::defi 🧪 Prédis la sortie
Une fonction appelée sur son propre résultat : que s'affiche-t-il ? Devine, **puis** ▶ Essayer.
```python
def double(x):
    return x * 2

print(double(double(3)))
```
:::

➡️ **Prochaine étape** : [module 04 — exceptions & fichiers](../04_exceptions_fichiers/).
