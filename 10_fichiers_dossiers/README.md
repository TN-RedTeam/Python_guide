# Module 10 — Fichiers et dossiers

C'est **le premier vrai super-pouvoir d'automatisation** : faire en sorte que Python lise,
écrive, déplace et range des fichiers à ta place. Plus de copier-coller manuel pendant
des heures.

> Fichiers du module : `lire_ecrire.py`, `csv_json.py`, `ranger_dossier.py`.
> Un dossier `exemples/` contient des fichiers de test pour que tout fonctionne directement.

:::reflexion Réfléchis d'abord : automatiser = décrire une corvée en étapes
Toute automatisation de fichiers se pense pareil : « **pour chaque** fichier du
dossier, **si** telle condition, **alors** telle action ». Reconnais les patterns
de [🧭 Penser comme un dev](../penser_comme_un_dev) : une **boucle** (pour chaque),
un **filtre** (si…), une **action**. Écris cette phrase en français d'abord, et le
programme s'écrit presque tout seul.
:::

---

## 1. Comment l'ordinateur range les fichiers

Ton ordinateur organise les fichiers comme des **dossiers dans des dossiers**, formant une
arborescence (comme un arbre généalogique) :

```
/home/alice/
├── Documents/
│   └── rapport.txt
└── Téléchargements/
    ├── photo.jpg
    └── facture.pdf
```

Pour désigner un fichier, on donne son **chemin** (en anglais *path*) : la suite de dossiers
à traverser pour l'atteindre, par exemple `/home/alice/Documents/rapport.txt`.

Il existe deux sortes de chemins :
- **Chemin absolu** : part de la racine. `C:\Users\Alice\rapport.txt` (Windows) ou
  `/home/alice/rapport.txt` (Mac/Linux).
- **Chemin relatif** : part de l'endroit où tu es. `Documents/rapport.txt`.

> ⚠️ Windows utilise des `\` (antislash) et Mac/Linux des `/` (slash). Pour ne pas s'en
> soucier, on utilise le module **`pathlib`** de Python, qui gère ça automatiquement
> quel que soit le système.

---

## 2. Lire et écrire un fichier texte

L'opération de base. En Python, on **ouvre** un fichier, on travaille avec, puis on le
**ferme**. La bonne pratique est d'utiliser `with`, qui ferme le fichier tout seul :

```python
# Écrire (le "w" = write ; ATTENTION : écrase le contenu existant !)
with open("notes.txt", "w", encoding="utf-8") as fichier:
    fichier.write("Première ligne\n")   # \n = retour à la ligne

# Lire (le "r" = read)
with open("notes.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
print(contenu)
```

Les **modes** d'ouverture les plus courants :

| Mode | Rôle |
|------|------|
| `"r"` | Lire (read). Erreur si le fichier n'existe pas. |
| `"w"` | Écrire (write). **Écrase tout** le contenu existant. |
| `"a"` | Ajouter (append). Écrit **à la fin** sans effacer. |

> 💡 `encoding="utf-8"` garantit que les accents (é, à, ç…) et emojis s'écrivent
> correctement. Mets-le toujours.

---

## 3. Le format CSV : les tableaux en texte

Un **CSV** (*Comma-Separated Values*) est un tableau stocké en texte : chaque ligne est une
rangée, et les colonnes sont séparées par des virgules (ou des points-virgules).

```
nom,age,ville
Alice,30,Paris
Bob,25,Lyon
```

C'est le format **roi de l'automatisation** : Excel, les exports de logiciels, les bases
de données… tout sait lire et écrire du CSV. Python possède un module `csv` dédié qui
gère les pièges (virgules à l'intérieur d'une valeur, guillemets…).

---

## 4. Le format JSON : pour les données structurées

Le **JSON** sert à stocker des données plus riches qu'un simple tableau (des listes dans
des objets, des objets dans des listes…). Sa structure ressemble **exactement** aux
dictionnaires et listes Python :

```json
{
  "nom": "Alice",
  "age": 30,
  "loisirs": ["lecture", "vélo"]
}
```

C'est le format universel des **APIs web** (module 03). Le module `json` de Python
convertit en une ligne :
- un dictionnaire Python **→** texte JSON (`json.dump`),
- du texte JSON **→** dictionnaire Python (`json.load`).

---

## 5. Parcourir un dossier

Pour ranger automatiquement, il faut d'abord **lister** le contenu d'un dossier. `pathlib`
le fait élégamment :

```python
from pathlib import Path

dossier = Path("Téléchargements")
for fichier in dossier.iterdir():     # parcourt chaque élément du dossier
    print(fichier.name, "->", fichier.suffix)   # .suffix = l'extension (.pdf, .jpg…)
```

L'idée du mini-projet `ranger_dossier.py` : regarder l'**extension** de chaque fichier
(`.pdf`, `.jpg`, `.csv`…) et le **déplacer** dans un sous-dossier correspondant
(`PDF/`, `Images/`…). Une corvée manuelle transformée en 1 commande.

---

## 6. `pathlib` en détail : ta boîte à outils pour les chemins

Un objet `Path` représente **un chemin** (vers un fichier ou un dossier). Il sait se découper,
dire si la cible existe, lire, écrire, renommer… C'est l'outil à préférer pour tout ce qui
touche aux fichiers.

### Découper un chemin

```python
from pathlib import Path

chemin = Path("documents/2026/rapport_final.pdf")

print(chemin.name)           # rapport_final.pdf   le nom complet du fichier
print(chemin.stem)           # rapport_final       le nom SANS l'extension
print(chemin.suffix)         # .pdf                l'extension, avec son point
print(chemin.parent)         # documents/2026      le dossier qui le contient
print(chemin.parent.name)    # 2026                …et le nom de ce dossier
```

Rien n'est lu sur le disque ici : on ne fait qu'**analyser le texte** du chemin. Le fichier n'a
même pas besoin d'exister.

### Construire un chemin avec `/`

Pour désigner un fichier **dans** un dossier, on « colle » les morceaux avec `/` :

```python
dossier = Path("photos")
fichier = dossier / "plage.jpg"      # → photos/plage.jpg   (un nouveau Path)
```

Cet opérateur `/` fabrique le bon chemin sur tous les systèmes (Windows utilise `\`, Mac et
Linux `/` : `pathlib` s'en occupe).

### Interroger le disque

```python
from pathlib import Path

note = Path("note.txt")                           # un fichier dans le dossier courant

print(note.exists())                              # False : ce fichier n'existe pas encore
note.write_text("Bonjour", encoding="utf-8")      # crée le fichier et écrit dedans
print(note.exists())                              # True
print(note.read_text(encoding="utf-8"))           # Bonjour
print(note.stat().st_size)                        # 7   ← la TAILLE en octets
print(note.is_file())                             # True  (pour un dossier, ce serait False)
```

`write_text` et `read_text` sont des raccourcis pour le `with open(...)` du
[module 04](../04_exceptions_fichiers/) : pratiques quand on écrit ou lit **tout d'un coup**.

### Lister un dossier, trié et filtré

`iterdir()` donne les éléments du dossier **dans un ordre quelconque**. Pour un résultat
prévisible, on trie ; pour ne garder que certains fichiers, on filtre sur `.suffix` :

```python
# le dossier contient : note.txt, b.txt, a.csv
print(sorted(e.name for e in dossier.iterdir()))                        # ['a.csv', 'b.txt', 'note.txt']
print(sorted(e.name for e in dossier.iterdir() if e.suffix == ".txt"))  # ['b.txt', 'note.txt']
```

Lis la 2e ligne comme : *« le nom de chaque élément du dossier, s'il a l'extension .txt — le
tout trié »*. C'est une expression génératrice ([module 06](../06_iterateurs_generateurs/))
donnée à `sorted`.

### Créer, renommer, copier

```python
import shutil

archives = dossier / "archives"
archives.mkdir()                                  # crée le sous-dossier « archives »

note.rename(dossier / "memo.txt")                 # renomme note.txt en memo.txt
shutil.copy(dossier / "memo.txt", archives / "memo.txt")    # COPIE memo.txt dans archives/
```

| Geste | Outil |
|-------|-------|
| créer un dossier | `chemin.mkdir()` |
| renommer (ou déplacer) | `chemin.rename(nouveau_chemin)` |
| copier un fichier | `shutil.copy(source, destination)` |
| supprimer un fichier | `chemin.unlink()` |

> ⚠️ **Ces gestes modifient ton disque et ne s'annulent pas.** `rename` et `copy` **écrasent**
> sans prévenir un fichier qui porterait déjà le nouveau nom. Réflexes de pro : vérifier avec
> `.exists()` avant d'agir, tester sur un dossier d'essai, et **afficher ce qu'on va faire
> avant de le faire** (c'est tout le sujet du [défi 4](../projets/defis/)).

> 🔎 **Et `tempfile.mkdtemp()` dans les exercices ?** Cette fonction crée un **dossier
> temporaire vide** quelque part sur ta machine et renvoie son chemin. Les exercices s'en
> servent pour te fournir un terrain d'essai : tu peux y créer, renommer et supprimer sans
> aucun risque pour tes vrais fichiers.

---

## 7. Écrire et relire du JSON

La section 4 a présenté le format. Voici le geste complet, dans les deux sens :

```python
import json

donnees = {"ville": "Paris", "jours": 3}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(donnees, f)            # dictionnaire Python → texte JSON, écrit dans le fichier
# le fichier contient maintenant :  {"ville": "Paris", "jours": 3}

with open("data.json", "r", encoding="utf-8") as f:
    relu = json.load(f)              # texte JSON du fichier → dictionnaire Python

print(relu)                          # {'ville': 'Paris', 'jours': 3}
print(relu["jours"] + 1)             # 4  ← un VRAI nombre, on peut calculer
```

Ce dernier point est tout l'intérêt du JSON par rapport à un fichier texte ordinaire : les
**types sont conservés**. `3` revient sous forme de nombre, pas du texte `"3"` ; une liste
revient sous forme de liste. C'est le format idéal pour **sauvegarder l'état d'un programme**
et le retrouver au lancement suivant.

> 🔎 `json.dump` / `json.load` travaillent avec un **fichier**. Leurs cousins `json.dumps` /
> `json.loads` (avec un **s**, pour *string*) travaillent avec un **texte** en mémoire — tu les
> retrouveras au [module 11](../11_web_apis/) pour lire les réponses des APIs.

---


## 🏁 S'entraîner

### 🎯 Les exercices — commence par ça

**[`exercices.py`](./exercices.py)** : des petits exercices que tu écris **toi-même**, avec des
données de départ **visibles** et un **résultat attendu** affiché. Pas de correction
automatique : tu lances, tu regardes ce qui s'affiche, tu **compares**.

```bash
python3 10_fichiers_dossiers/exercices.py
```

Bloqué après un vrai essai ? Le corrigé commenté est dans [`solutions.py`](./solutions.py).

### 🏋️ La série 2 — l'entraînement

**[`entrainement.py`](./entrainement.py)** : à faire **après** les exercices. La même matière,
travaillée de trois façons : 👓 **lire** du code et prédire ce qu'il affiche, 🔧 **modifier** un
script qui marche, ✍️ **écrire** de nouveaux exercices, cette fois **sans indice**. Le corrigé
expliqué est dans [`entrainement_solutions.py`](./entrainement_solutions.py).

```bash
python3 10_fichiers_dossiers/entrainement.py
```

### 🔬 Pour explorer (lance les démos commentées du module)

```bash
python3 10_fichiers_dossiers/lire_ecrire.py
python3 10_fichiers_dossiers/csv_json.py
python3 10_fichiers_dossiers/ranger_dossier.py
```

Le script `ranger_dossier.py` travaille sur un dossier de test (`exemples/bazar/`) qu'il
crée lui-même, pour que tu puisses l'exécuter **sans risque pour tes vrais fichiers**.

## 🔬 Le raisonnement en action

**Problème** : écrire 3 lignes dans un fichier, puis le relire et compter ses lignes.

```pseudo
OUVRIR "notes.txt" EN ÉCRITURE : écrire les 3 lignes
OUVRIR "notes.txt" EN LECTURE  : lire toutes les lignes
AFFICHER le nombre de lignes, puis chacune
```

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("pomme\npoire\nkiwi\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()

print(f"{len(lignes)} lignes :")
for ligne in lignes:
    print("-", ligne.strip())      # .strip() enlève le \n de fin
```

:::defi 🧪 Prédis la sortie
`split` découpe une chaîne en liste. Que donne ceci ? Devine, **puis** ▶ Essayer.
```python
texte = "un,deux,trois"
morceaux = texte.split(",")
print(len(morceaux), morceaux[1])
```
:::

➡️ Module suivant : [`11_web_apis`](../11_web_apis/).
