# Module 13 — Données et rapports automatiques

Le module final, et le plus gratifiant : transformer des **données brutes** (un export CSV
en vrac) en un **rapport propre** (totaux, moyennes, classements, fichier Excel), le tout
automatiquement. C'est ce que font des milliers de gens **à la main** dans Excel chaque jour.

> Fichier du module : `rapport_ventes.py`. Il crée lui-même un jeu de données de démo.
> Nécessite `pandas` et `openpyxl` (`pip install -r requirements.txt`).

:::reflexion Réfléchis d'abord : un rapport, c'est un pipeline
Ne vois pas « le rapport » comme un bloc, mais comme une **chaîne** de 4 étapes :
**charger** les données brutes → les **nettoyer** → **calculer** (totaux, moyennes,
regroupements) → **présenter** (tableau, Excel). Décompose toujours dans cet ordre :
chaque étape prend la sortie de la précédente. C'est la décomposition appliquée aux
données.
:::

---

## 1. Pourquoi `pandas` ?

On pourrait tout faire avec le module `csv` du module 02… mais dès qu'il s'agit de
**calculer, regrouper, filtrer, trier** des milliers de lignes, ça devient vite pénible.

**`pandas`** est la bibliothèque reine de la manipulation de données en Python. Elle
introduit un objet central : le **DataFrame**, qui est **un tableau intelligent**, exactement
comme une feuille Excel — mais pilotable par du code.

> 🧠 Image mentale : un **DataFrame = une feuille Excel dans une variable**. Lignes,
> colonnes, en-têtes… mais sur laquelle tu peux faire des calculs en une ligne de code,
> de façon **reproductible** (même résultat à chaque exécution, sans clic manuel).

---

## 2. Charger des données

`pandas` lit la plupart des formats en **une ligne** :

```python
import pandas as pd          # 'pd' est l'abréviation universelle, par convention

df = pd.read_csv("ventes.csv")     # df = "DataFrame", le nom habituel
# pd.read_excel("ventes.xlsx")     # marche aussi pour Excel
```

Premiers réflexes pour explorer un tableau qu'on découvre :

| Commande | Ce qu'elle montre |
|----------|-------------------|
| `df.head()` | les 5 premières lignes |
| `df.shape` | (nombre de lignes, nombre de colonnes) |
| `df.columns` | les noms des colonnes |
| `df.info()` | type de chaque colonne et valeurs manquantes |
| `df.describe()` | statistiques (moyenne, min, max…) des colonnes numériques |

---

## 3. Sélectionner et filtrer

On accède à une **colonne** par son nom :

```python
df["produit"]            # toute la colonne "produit"
df["prix"].sum()         # la somme de la colonne "prix"
df["prix"].mean()        # la moyenne
```

On **filtre** les lignes avec une condition (comme un « filtre » Excel) :

```python
# Garde seulement les ventes supérieures à 100 €
grosses_ventes = df[df["montant"] > 100]
```

Lis `df[df["montant"] > 100]` comme : *« dans `df`, garde les lignes où la colonne montant
dépasse 100 »*.

On **trie** les lignes selon une colonne avec `sort_values` :

```python
df.sort_values("montant")                    # du plus petit au plus grand
df.sort_values("montant", ascending=False)   # du plus grand au plus petit
df.sort_values("montant", ascending=False).head(3)   # les 3 plus gros montants
```

Et pour récupérer une colonne sous forme de **liste Python** ordinaire (pratique pour
l'afficher ou la réutiliser) : `df["produit"].tolist()`.

---

## 4. Regrouper : le cœur des rapports (`groupby`)

C'est **l'opération clé** d'un rapport : regrouper des lignes par catégorie et calculer un
total/une moyenne par groupe. C'est l'équivalent du **tableau croisé dynamique** d'Excel.

```python
# Chiffre d'affaires total par produit :
ca_par_produit = df.groupby("produit")["montant"].sum()
```

`groupby("produit")` rassemble toutes les lignes d'un même produit, puis `["montant"].sum()`
additionne leurs montants. En une ligne, tu obtiens ce qui prendrait plusieurs manipulations
manuelles dans un tableur.

---

### Créer une colonne, et lire ce que pandas affiche

Un calcul entre colonnes s'applique **à toutes les lignes d'un coup**. Et écrire dans une
colonne qui n'existe pas encore la **crée** (comme pour une clé de dictionnaire) :

```python
# df contient :   produit  quantite  prix
#                 stylo          10     2
#                 cahier          3     5
#                 stylo           4     2

df["montant"] = df["quantite"] * df["prix"]     # nouvelle colonne : 10×2, 3×5, 4×2
print(df["montant"].tolist())                   # [20, 15, 8]
print(df["montant"].min(), df["montant"].max()) # 8 20
print(df[df["produit"] != "stylo"]["produit"].tolist())   # ['cahier']   ← != : « différent de »
```

Quand tu affiches le résultat d'un `groupby`, pandas montre une **Series** : une colonne de
valeurs, chacune avec son **étiquette**.

```python
par_produit = df.groupby("produit")["montant"].sum()
print(par_produit)
```

```
produit                         ← le nom des étiquettes (la colonne du groupby)
cahier    15                    ← étiquette : valeur
stylo     28
Name: montant, dtype: int64     ← le nom de la colonne calculée, et le type des valeurs
```

Les deux dernières informations ne font pas partie des données : c'est pandas qui te décrit ce
qu'il affiche. Les groupes sont rangés par **ordre alphabétique** des étiquettes. Pour aller
plus loin avec ce résultat :

```python
print(par_produit["stylo"])          # 28       une valeur, par son étiquette
print(par_produit.to_numpy())        # [15 28]  les valeurs seules, en tableau NumPy
print(df.columns.tolist())           # ['produit', 'quantite', 'prix', 'montant']  les colonnes
```

---


## 5. Exporter le résultat

Une fois le rapport calculé, on l'enregistre pour le partager :

```python
ca_par_produit.to_csv("rapport.csv")               # en CSV
ca_par_produit.to_excel("rapport.xlsx")            # en Excel (nécessite openpyxl)
```

> 🔁 **La grande idée du module** : tu écris ce code **une fois**. Ensuite, chaque semaine,
> tu remplaces le fichier de données et tu relances le script → ton rapport est régénéré en
> une seconde, sans erreur. C'est ça, l'automatisation des données.

---

## 🏁 S'entraîner

### 🎯 Les exercices — commence par ça

**[`exercices.py`](./exercices.py)** : 6 exercices **avec pandas**, sur un vrai fichier
`depenses.csv` (un relevé de dépenses) : charger, additionner, filtrer, trier, regrouper,
exporter. Le fichier est créé par l'exercice et tu vois tout son contenu. Chaque exercice
affiche un **résultat attendu** : tu lances et tu **compares**. Les indices sont regroupés
**en bas du fichier**, à ne lire que si tu bloques.

```bash
python3 13_donnees_rapports/exercices.py
```

Bloqué après un vrai essai ? Le corrigé commenté est dans [`solutions.py`](./solutions.py).

### 🏋️ La série 2 — l'entraînement

**[`entrainement.py`](./entrainement.py)** : à faire **après** les exercices. La même matière,
travaillée de trois façons : 👓 **lire** du code et prédire ce qu'il affiche, 🔧 **modifier** un
script qui marche, ✍️ **écrire** de nouveaux exercices, cette fois **sans indice**. Le corrigé
expliqué est dans [`entrainement_solutions.py`](./entrainement_solutions.py).

```bash
python3 13_donnees_rapports/entrainement.py
```

### 🔬 Pour explorer (lance la démo commentée du module)

```bash
python3 13_donnees_rapports/rapport_ventes.py
```

Le script génère un faux fichier de ventes, calcule plusieurs indicateurs (chiffre
d'affaires total, CA par produit, meilleur vendeur…) et exporte un rapport `.csv` et `.xlsx`.
Ouvre les fichiers produits dans `exemples/` pour voir le résultat.

🎉 **Bravo, tu maîtrises l'essentiel de l'automatisation des données !** Il reste un dernier
module, transversal et précieux : savoir **quelle bibliothèque** ajouter et **quand**.

## 🔬 Le raisonnement en action

**Problème** : un mini-rapport de ventes. On déroule le **pipeline** — ici en Python
pur pour bien voir chaque étape (`pandas` fait la même chose, à grande échelle).

```pseudo
CHARGER   les ventes
CALCULER  le total, le nombre, le panier moyen
PRÉSENTER une ligne de synthèse
```

```python
ventes = [
    {"produit": "stylo",  "montant": 3},
    {"produit": "cahier", "montant": 5},
    {"produit": "stylo",  "montant": 3},
]

total = sum(v["montant"] for v in ventes)     # accumulateur
nb = len(ventes)
print(f"{nb} ventes | total {total} € | panier moyen {total / nb:.2f} €")
```

:::defi 🧪 Prédis la sortie
Trois synthèses d'un coup. Que s'affiche-t-il ? Devine, **puis** ▶ Essayer.
```python
notes = [12, 15, 9, 18]
print(max(notes), min(notes), sum(notes) / len(notes))
```
:::

➡️ Module suivant : [`14_bibliotheques`](../14_bibliotheques/).
