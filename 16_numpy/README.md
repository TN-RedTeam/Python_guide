# 🔢 Module 16 : NumPy — calculer sur des tableaux de nombres

> 🎯 **Objectif** : savoir créer un **tableau NumPy**, calculer dessus **sans boucle**, le
> filtrer, et lire un tableau à **2 dimensions**. C'est la brique sur laquelle reposent pandas,
> scikit-learn et PyTorch : en IA, **toutes les données finissent en tableaux de nombres**.

:::reflexion Réfléchis d'abord : une valeur à la fois, ou tout le tableau d'un coup ?
Jusqu'ici, pour transformer une liste, tu écrivais une **boucle** : « pour chaque valeur,
fais ceci ». NumPy change la façon de penser : tu décris l'opération **une fois**, sur le
tableau entier (« ajoute 2 à ce tableau »), et NumPy s'occupe de l'appliquer à chaque case.
Quand tu te surprends à écrire un `for` sur un tableau NumPy, arrête-toi : il existe presque
toujours une façon de le dire **sans boucle**.
:::

---

## 1. Pourquoi NumPy, alors qu'on a déjà les listes ?

Avec une liste Python, une opération mathématique ne fait pas ce qu'on croit :

```python
temperatures = [12, 15, 18]
print(temperatures * 2)      # [12, 15, 18, 12, 15, 18]  ← la liste est RÉPÉTÉE, pas doublée
print(temperatures + 2)      # TypeError : on ne peut pas ajouter un nombre à une liste
```

Pour doubler chaque valeur, il faut une boucle ou une compréhension. Avec NumPy, l'opération
s'applique **à chaque case** :

```python
import numpy as np               # 'np' est l'abréviation universelle, par convention

temperatures = np.array([12, 15, 18])
print(temperatures * 2)          # [24 30 36]   ← chaque valeur est doublée
print(temperatures + 2)          # [14 17 20]   ← 2 est ajouté à chaque valeur
```

Deux raisons de l'utiliser :

- **c'est plus court et plus lisible** : la formule s'écrit comme en maths ;
- **c'est beaucoup plus rapide** sur de gros volumes (des millions de valeurs), parce que le
  calcul est fait par du code compilé et non par une boucle Python.

> 🔎 Tu remarques que NumPy affiche `[24 30 36]` **sans virgules** ? C'est sa façon de montrer
> qu'il s'agit d'un tableau NumPy (un `ndarray`) et pas d'une liste. Rien d'anormal.

---

## 2. Créer un tableau et le découvrir

```python
import numpy as np

notes = np.array([12, 15, 9, 18])    # à partir d'une liste

print(notes.shape)     # (4,)     la FORME : 4 valeurs, sur une seule dimension
print(notes.dtype)     # int64    le TYPE des valeurs (toutes du même type)
print(len(notes))      # 4        le nombre de valeurs
print(notes[0])        # 12       l'accès par index marche comme pour une liste
print(notes[1:3])      # [15  9]  les tranches aussi
```

Deux différences avec une liste :

- toutes les valeurs ont **le même type** (que des entiers, ou que des nombres à virgule) ;
- `.shape` et `.dtype` s'écrivent **sans parenthèses** : ce sont des informations rangées
  dans le tableau (des attributs), pas des actions.

Quelques façons de fabriquer un tableau sans tout taper :

```python
np.zeros(3)          # [0. 0. 0.]       trois zéros
np.ones(3)           # [1. 1. 1.]       trois uns
np.arange(0, 10, 2)  # [0 2 4 6 8]      comme range(), mais renvoie un tableau
```

---

## 3. Calculer sur tout le tableau d'un coup

C'est **le** principe de NumPy (on dit *calcul vectorisé*). Une opération entre un tableau et
un nombre s'applique à chaque case ; une opération entre deux tableaux de même taille
s'applique case par case.

```python
prix = np.array([10, 20, 30])
quantites = np.array([2, 1, 3])

print(prix * 1.2)          # [12. 24. 36.]   chaque prix avec 20 % de TVA
print(prix * quantites)    # [20 20 90]      10×2, 20×1, 30×3 : case par case
print(prix > 15)           # [False  True  True]   une comparaison donne des True/False
```

Et les statistiques tiennent en une ligne :

```python
notes = np.array([12, 15, 9, 18])

print(notes.sum())     # 54      la somme
print(notes.mean())    # 13.5    la moyenne
print(notes.max())     # 18      la plus grande
print(notes.min())     # 9       la plus petite
```

---

## 4. Filtrer avec un masque

On a vu qu'une comparaison renvoie un tableau de `True` / `False`. Ce tableau s'appelle un
**masque**. Placé entre les crochets du tableau, il ne garde que les cases où c'est `True` :

```python
notes = np.array([12, 15, 9, 18])

masque = notes >= 12        # [ True  True False  True]
print(notes[masque])        # [12 15 18]   seulement les notes où le masque vaut True
print(notes[notes >= 12])   # [12 15 18]   la même chose, écrite en une ligne
```

Lis `notes[notes >= 12]` comme : *« dans `notes`, garde les valeurs qui sont ≥ 12 »*.

> 🔗 Ça te rappelle quelque chose ? C'est **exactement** le filtre de pandas
> (`df[df["montant"] > 100]`, [module 13](../13_donnees_rapports/)). Normal : une colonne de
> DataFrame **est** un tableau NumPy, avec des étiquettes en plus.

---

## 5. Les tableaux à 2 dimensions

C'est la forme des données en IA : **un tableau à lignes et colonnes**, avec **une ligne par
exemple** (un élève, une maison, une image…) et **une colonne par mesure**.

```python
notes = np.array([[12, 15, 9],      # élève 0 : maths, français, anglais
                  [18, 14, 16]])    # élève 1

print(notes.shape)     # (2, 3)   2 lignes, 3 colonnes — toujours (lignes, colonnes)
print(notes[0])        # [12 15  9]   la ligne 0 : toutes les notes de l'élève 0
print(notes[0, 1])     # 15           ligne 0, colonne 1
print(notes[:, 0])     # [12 18]      « : » = toutes les lignes, colonne 0 : les maths
```

### Le paramètre `axis` : dans quel sens calculer ?

Sur un tableau 2D, `mean()` seul donne la moyenne de **toutes** les cases. Avec `axis`, tu
choisis le sens :

```python
print(notes.mean())          # 14.0             moyenne de toutes les notes
print(notes.mean(axis=1))    # [12. 16.]        une moyenne par LIGNE  → par élève
print(notes.mean(axis=0))    # [15.  14.5 12.5] une moyenne par COLONNE → par matière
```

> 🧠 **Pour ne pas confondre** : `axis=1` calcule **le long de chaque ligne** (tu obtiens un
> résultat par ligne) ; `axis=0` calcule **le long de chaque colonne** (un résultat par
> colonne). Dans le doute, regarde la taille du résultat : 2 valeurs ici = 2 élèves.

---

## 🤖 Pourquoi ce module est essentiel pour l'IA

Un modèle ne reçoit jamais « des maisons » ou « des images » : il reçoit **un tableau de
nombres**. Par convention, on l'appelle `X` (les données) et `y` (ce qu'on veut prédire) :

```python
X = np.array([[50, 2],       # maison 0 : 50 m², 2 pièces
              [80, 3],       # maison 1
              [120, 5]])     # maison 2
y = np.array([150, 240, 400])    # le prix de chaque maison (en milliers d'euros)

print(X.shape)   # (3, 2) : 3 exemples, 2 mesures chacun
```

Quand tu liras `modele.fit(X, y)` dans scikit-learn, tu sauras exactement ce que sont `X` et
`y`. Et une opération comme **ramener les valeurs entre 0 et 1** (la *normalisation*, que tu
écris dans les exercices) est une préparation de données que tu feras dans presque tous tes
projets. La suite du chemin est dans [`PARCOURS_IA.md`](../PARCOURS_IA.md).

---

## 🏁 S'entraîner

### 🎯 Les exercices — commence par ça

**[`exercices.py`](./exercices.py)** : 6 exercices sur des températures, des notes et des
prix : créer un tableau, calculer dessus, faire des statistiques, filtrer, lire un tableau
2D, normaliser. La règle du jeu : **aucune boucle `for`**. Chaque exercice affiche un
**résultat attendu** : tu lances et tu **compares**. Les indices sont regroupés **en bas du
fichier**, à ne lire que si tu bloques.

```bash
python3 16_numpy/exercices.py
```

Bloqué après un vrai essai ? Le corrigé commenté est dans [`solutions.py`](./solutions.py).

### 🏋️ La série 2 — l'entraînement

**[`entrainement.py`](./entrainement.py)** : à faire **après** les exercices. La même matière,
travaillée de trois façons : 👓 **lire** du code et prédire ce qu'il affiche, 🔧 **modifier** un
script qui marche, ✍️ **écrire** de nouveaux exercices, cette fois **sans indice**. Le corrigé
expliqué est dans [`entrainement_solutions.py`](./entrainement_solutions.py).

```bash
python3 16_numpy/entrainement.py
```

### 🔬 Pour explorer (dans le terminal ou un fichier à toi)

1. Reprends l'exercice des températures et change les valeurs pour celles de ta ville cette
   semaine.
2. Fabrique un tableau 2D de tes dépenses : une ligne par semaine, une colonne par catégorie.
   Calcule le total par semaine (`axis=1`) puis par catégorie (`axis=0`).

## 🔬 Le raisonnement en action

**Problème** : parmi les notes d'une classe, quelle est la moyenne des élèves qui ont eu
**au moins 10** ?

On décompose : d'abord **filtrer** (garder les notes ≥ 10), ensuite **calculer** (la moyenne
de ce qui reste). Deux étapes, deux opérations NumPy, aucune boucle.

```pseudo
notes_valides ← les notes qui sont >= 10
RENVOYER la moyenne de notes_valides
```

```python
import numpy as np

notes = np.array([8, 12, 15, 6, 13])
notes_valides = notes[notes >= 10]     # [12 15 13]
print(notes_valides.mean())            # 13.333333333333334
```

:::defi 🧪 Prédis la sortie
Une liste et un tableau NumPy ne réagissent pas pareil à `* 2`. Devine les deux lignes
affichées, **puis** ▶ Essayer.
```python
import numpy as np

liste = [1, 2, 3]
tableau = np.array([1, 2, 3])
print(liste * 2)
print(tableau * 2)
```
:::

➡️ **Et ensuite ?** Tu as maintenant les deux outils de base des données : NumPy (ce module)
et pandas ([module 13](../13_donnees_rapports/)). La prochaine marche est scikit-learn — le
plan est dans [`PARCOURS_IA.md`](../PARCOURS_IA.md).
