# 🏗️ Module 05 : la Programmation Orientée Objet (POO)

> 🎯 **Objectif** : jusqu'ici, données (variables) et actions (fonctions) étaient séparées. La
> **POO** permet de les **réunir** dans un même « objet ». C'est ce qui structure les gros
> programmes. Concepts à maîtriser : **classe**, **objet**, **`self`**, **`__init__`**,
> **héritage**.

:::reflexion Réfléchis d'abord : repère les « objets » de ton problème
La POO, avant d'être de la syntaxe, est une façon de **modéliser**. Dans ton
énoncé, souligne les **noms** (un *client*, un *panier*, une *voiture*) et les
**actions** associées (*ajouter au panier*, *démarrer*). Les noms deviennent des
**classes**, leurs caractéristiques des **attributs**, leurs actions des
**méthodes**. On modélise d'abord sur le papier, on code ensuite.
:::

---

## 1. L'idée : regrouper données + actions

Sans POO, pour gérer un chien tu aurais une variable `nom_chien` et une fonction
`aboyer(nom_chien)`, séparées. Avec la POO, tu crées un **objet** `chien` qui contient **à la
fois** son nom (donnée) et sa capacité à aboyer (action).

> 🧠 **L'image fondatrice** : une **classe** est un **moule** (un plan) ; un **objet** est ce
> qu'on fabrique avec le moule. Le moule `Voiture` permet de fabriquer autant de voitures
> qu'on veut, chacune avec ses propres caractéristiques.

| Terme | Définition | Exemple |
|-------|------------|---------|
| **classe** | le plan / le moule | `Voiture` |
| **objet** (ou **instance**) | un exemplaire fabriqué | *ma* Tesla rouge |
| **attribut** | une **donnée** de l'objet | `marque`, `couleur` |
| **méthode** | une **action** de l'objet | `klaxonner()` |

---

## 2. Définir une classe

```python
class Voiture:                              # convention : nom de classe en MajusculeCamel
    def __init__(self, marque, couleur):    # le "constructeur" : appelé à la création
        self.marque = marque                # on RANGE les données DANS l'objet
        self.couleur = couleur

    def klaxonner(self):                     # une méthode = une fonction DANS la classe
        return f"La {self.marque} fait : POUT POUT !"
```

### `__init__` : le constructeur

`__init__` (un *dunder*, voir [`../COMPRENDRE_LE_CODE.md`](../COMPRENDRE_LE_CODE.md)) est une
méthode **spéciale** que Python appelle **automatiquement** quand tu crées un objet. Son rôle :
**initialiser** les attributs (remplir les cases de l'objet).

### `self` : « moi-même »

`self` est **le** mot qui déroute le plus. C'est simplement **l'objet en cours de manipulation**.

- Dans `def klaxonner(self):`, `self` représente *la voiture sur laquelle on appelle la méthode*.
- `self.marque` = « **la** marque **de cet objet-ci** ».
- Tu écris `self` comme **premier paramètre** de chaque méthode, mais tu ne le passes **pas**
  toi-même à l'appel : Python le fournit tout seul.

```python
ma_caisse.klaxonner()    # tu n'écris PAS ma_caisse.klaxonner(ma_caisse) :
                         # Python met automatiquement ma_caisse dans "self"
```

> 🧠 **Traduction** : quand tu écris `ma_caisse.klaxonner()`, Python comprend
> « exécute `klaxonner` **avec** `self = ma_caisse` ». D'où `self.marque` = la marque de
> `ma_caisse`. C'est ça, le lien entre l'objet et ses méthodes.

---

## 3. Créer et utiliser un objet

```python
ma_caisse = Voiture("Tesla", "Rouge")   # APPELLE __init__ → fabrique un objet
                                        # "Tesla"→marque, "Rouge"→couleur (self est implicite)
print(ma_caisse.marque)                 # "Tesla"     ← lire un attribut (avec le point)
print(ma_caisse.klaxonner())             # "La Tesla fait : POUT POUT !"  ← appeler une méthode

autre = Voiture("Renault", "Bleu")      # un AUTRE objet, indépendant : sa propre marque/couleur
```

> 🔎 **Pourquoi pas de `self` à la création ?** Quand tu écris `Voiture("Tesla", "Rouge")`, le
> `self` du `__init__` est l'objet **en train d'être créé**. Tu ne fournis que les arguments qui
> *suivent* `self`.

---

## 4. L'héritage : réutiliser et spécialiser

L'**héritage** permet de créer une classe à partir d'une autre : la classe **enfant** récupère
tout de la classe **parente**, et peut en ajouter ou en modifier.

```python
class Vehicule:                          # la classe PARENTE (générique)
    def __init__(self, nom, vitesse_max):
        self.nom = nom
        self.vitesse_max = vitesse_max

    def se_deplacer(self):
        print(f"Le véhicule {self.nom} avance.")


class Voiture(Vehicule):                 # ENFANT : (Vehicule) = "hérite de Vehicule"
    def __init__(self, nom, vitesse_max, nb_portes):
        super().__init__(nom, vitesse_max)   # appelle le __init__ du PARENT (évite de recopier)
        self.nb_portes = nb_portes           # puis ajoute un attribut propre à l'enfant

    def se_deplacer(self):               # REDÉFINIT (override) la méthode du parent
        print(f"La voiture {self.nom} roule à {self.vitesse_max} km/h.")
```

Deux mécanismes clés :

- **`super()`** = « la classe parente ». `super().__init__(...)` appelle le constructeur du
  parent pour ne **pas recopier** son code. On factorise.
- **La redéfinition (override)** : si l'enfant définit une méthode du même nom que le parent
  (`se_deplacer`), **c'est la version de l'enfant qui gagne** pour les objets enfants.

```python
ma_voiture = Voiture("Peugeot 208", 180, 5)
ma_voiture.se_deplacer()       # version de Voiture : "La voiture Peugeot 208 roule à 180 km/h."
```

> 🧠 **Quand utiliser l'héritage ?** Quand tu peux dire *« X **est un** Y »* : une `Voiture`
> **est un** `Vehicule`, un `Chat` **est un** `Animal`. Si tu dis plutôt *« X **a un** Y »*
> (une voiture **a un** moteur), ce n'est pas de l'héritage : range l'objet `Moteur` dans un
> attribut.

---

## 5. Afficher proprement un objet : `__str__`

Par défaut, `print(mon_objet)` affiche un truc cryptique comme `<__main__.Voiture object at
0x7f...>`. Définis `__str__` pour choisir un affichage lisible :

```python
class Voiture:
    def __init__(self, marque):
        self.marque = marque

    def __str__(self):                 # appelé automatiquement par print(objet)
        return f"Voiture {self.marque}"

print(Voiture("Tesla"))                # "Voiture Tesla"  (au lieu du charabia)
```

---

## 🤖 Pourquoi ce module est essentiel pour l'IA

En IA, **tous les modèles sont des classes**. Quand tu écris :
```python
modele = RandomForestClassifier()   # crée un OBJET (comme Voiture("Tesla"))
modele.fit(X_train, y_train)        # appelle une METHODE (comme .klaxonner())
modele.predict(X_test)              # une autre METHODE
```
C'est exactement ce que tu apprends ici : `__init__` (créer l'objet), `self` (l'objet courant),
et les méthodes (les actions de l'objet). Tu n'as pas besoin de *créer* des classes pour l'IA,
mais tu dois savoir les **lire et les utiliser**.

---

## 🏁 S'entraîner

### 🎯 L'exercice principal — commence par ça

**[`exercices.py`](./exercices.py)** : des classes à compléter, organisées en **niveaux**
de difficulté avec un **RAPPEL DU COURS** dans chaque exercice.

```bash
python3 05_poo/exercices.py
```

Bloqué après un vrai essai ? Le corrigé commenté est dans [`solutions.py`](./solutions.py).

### 🔬 Pour explorer (dans le terminal ou un fichier à toi, sans correction automatique)

1. **Lis et lance** [`poo.py`](./poo.py) : repère `__init__`, `self`, `super()`, l'override.
2. **Classe `Moto` (à coder toi-même)** : ajoute une classe `Moto` qui hérite de `Vehicule`,
   avec un attribut `cylindree` et sa propre version de `se_deplacer`.

<details>
<summary>💡 Solution — Moto</summary>

```python
class Moto(Vehicule):
    def __init__(self, nom, vitesse_max, cylindree):
        super().__init__(nom, vitesse_max)   # réutilise le constructeur du parent
        self.cylindree = cylindree

    def se_deplacer(self):
        print(f"La moto {self.nom} ({self.cylindree} cm³) file à {self.vitesse_max} km/h.")
```
</details>

## 🔬 Le raisonnement en action

**Problème** : modéliser un **compteur** — un objet qui retient une valeur et sait
l'incrémenter.

On repère l'objet (*un compteur*), sa **donnée** (sa valeur, qui démarre à 0) et
son **action** (incrémenter). Donnée + action réunies → une classe.

```pseudo
CLASSE Compteur :
    À LA CRÉATION : valeur ← 0
    MÉTHODE incrementer : valeur ← valeur + 1
```

```python
class Compteur:
    def __init__(self):        # à la création de l'objet
        self.valeur = 0        # la donnée, rangée DANS l'objet
    def incrementer(self):     # une action de l'objet
        self.valeur += 1

c = Compteur()
c.incrementer()
c.incrementer()
print(c.valeur)                # 2
```

:::defi 🧪 Prédis la sortie
Deux objets fabriqués avec le même moule : partagent-ils leur `nom` ? Devine, **puis** ▶ Essayer.
```python
class Chien:
    def __init__(self, nom):
        self.nom = nom

a = Chien("Rex")
b = Chien("Mia")
print(a.nom, b.nom)
```
:::

➡️ **Prochaine étape** : [module 06 — itérateurs & générateurs](../06_iterateurs_generateurs/).
