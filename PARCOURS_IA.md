# Parcours Python pour l'IA — apprendre vite, aller droit au but

> Tu veux faire de l'IA (Machine Learning, Deep Learning, LLM) et tu as besoin
> de Python **rapidement**. Ce parcours te dit **quoi apprendre, dans quel ordre,
> et ce que tu peux sauter** pour l'instant.

---

## La vérité sur Python pour l'IA

En IA, tu n'as **pas besoin** de maîtriser tout Python. Tu as besoin de :

1. **Les bases solides** (variables, boucles, conditions, fonctions) — sans ça, rien ne tient.
2. **Les collections** (listes et dictionnaires) — les données en IA sont TOUJOURS des listes et des dicts.
3. **Les fonctions** — tout en IA s'organise en fonctions.
4. **Lire/écrire des fichiers** (CSV, JSON) — tes données arrivent par là.
5. **Les bibliothèques** (pip install, import) — NumPy, pandas, scikit-learn, PyTorch : tout passe par là.
6. **Les classes (POO)** — les modèles de ML sont des classes. Pas besoin d'en créer, mais tu dois les **lire**.

Ce que tu peux **reporter** (pas ignorer, reporter) :
- asyncio (module 08) — utile pour le web, pas pour l'IA
- les itérateurs/générateurs avancés (module 06) — les comprendre suffit, pas besoin de les maîtriser
- le debugger avancé (module 07) — utile mais pas bloquant
- les tests (module 09) — important en pro, mais pas pour débuter en IA

---

## Ton parcours en 3 phases

### Phase 1 — Les fondations Python (1-2 semaines)

Fais ces modules **dans l'ordre**, en faisant **tous les exercices** :

| # | Module | Pourquoi c'est essentiel pour l'IA |
|---|--------|------------------------------------|
| 0 | [penser_comme_un_dev](./penser_comme_un_dev/) | La méthode de raisonnement. Sans ça, tu tournes en rond. |
| 1 | [01_les_bases](./01_les_bases/) | Variables, boucles, conditions — le squelette de tout programme. |
| 2 | [02_collections](./02_collections/) | Listes et dictionnaires — **80% du code IA** manipule des listes. |
| 3 | [03_fonctions_modules](./03_fonctions_modules/) | Organiser son code. `import` = ta porte vers NumPy, pandas, etc. |
| 4 | [04_exceptions_fichiers](./04_exceptions_fichiers/) | Lire des fichiers de données, gérer les erreurs. |

### Phase 2 — Python appliqué aux données (1 semaine)

| # | Module | Pourquoi |
|---|--------|----------|
| 5 | [05_poo](./05_poo/) | Comprendre les classes — les modèles ML **sont** des classes. |
| 6 | [10_fichiers_dossiers](./10_fichiers_dossiers/) | CSV, JSON — le format de tes datasets. |
| 7 | [13_donnees_rapports](./13_donnees_rapports/) | pandas — **l'outil n°1** pour manipuler des données en IA. |
| 8 | [14_bibliotheques](./14_bibliotheques/) | pip, venv — installer et gérer NumPy, scikit-learn, etc. |

### Phase 3 — Ton premier projet IA (dès que la phase 2 est finie)

Tu n'as pas besoin de finir tout le guide pour commencer l'IA. Avec les phases 1
et 2, tu as **tout ce qu'il faut** pour :

1. **Charger un dataset** (CSV → pandas DataFrame)
2. **Explorer les données** (`.head()`, `.describe()`, `.value_counts()`)
3. **Entraîner un premier modèle** avec scikit-learn
4. **Évaluer le résultat** (accuracy, confusion matrix)

Voici le code minimal d'un projet IA complet — tu devrais **comprendre chaque ligne**
après les phases 1 et 2 :

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Charger les données (CSV → DataFrame)
donnees = pd.read_csv("mon_dataset.csv")

# 2. Séparer les features (X) et la cible (y)
X = donnees.drop("cible", axis=1)    # toutes les colonnes SAUF "cible"
y = donnees["cible"]                  # la colonne à prédire

# 3. Couper en entraînement / test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. Créer et entraîner le modèle (c'est une CLASSE — cf. module 05)
modele = RandomForestClassifier()     # créer l'objet (comme Voiture("Tesla"))
modele.fit(X_train, y_train)          # entraîner (comme .klaxonner())

# 5. Prédire et évaluer
predictions = modele.predict(X_test)
print(f"Précision : {accuracy_score(y_test, predictions):.1%}")
```

**Chaque ligne utilise ce que tu as appris** :
- `import` → module 03
- `pd.read_csv(...)` → une **fonction** qui renvoie un résultat (module 03)
- `donnees["cible"]` → accès par **clé**, comme un dictionnaire (module 02)
- `train_test_split(X, y, test_size=0.2)` → **argument nommé** (module 03)
- `RandomForestClassifier()` → créer un **objet** à partir d'une **classe** (module 05)
- `modele.fit(...)` → appeler une **méthode** sur l'objet (module 05)
- `f"Précision : {accuracy_score(...):.1%}"` → **f-string** (module 01)

---

## Les bibliothèques IA à connaître

Installe-les avec `pip install` (module 14) :

| Bibliothèque | À quoi ça sert | Quand l'apprendre |
|-------------|----------------|-------------------|
| **NumPy** | Calcul sur des tableaux de nombres | Dès la phase 3 |
| **pandas** | Manipuler des tableaux de données (CSV, Excel) | Dès la phase 2 (module 13) |
| **matplotlib** | Tracer des graphiques | Dès la phase 3 |
| **scikit-learn** | Machine Learning classique (classification, régression) | Dès la phase 3 |
| **PyTorch** / **TensorFlow** | Deep Learning (réseaux de neurones) | Après scikit-learn |
| **Hugging Face** (`transformers`) | Utiliser des LLM (GPT, BERT, Llama…) | Après PyTorch |

### L'ordre recommandé pour l'IA :

```
Python de base (ce guide, phases 1-2)
        ↓
   NumPy + pandas
        ↓
    matplotlib
        ↓
   scikit-learn  ← ton premier "vrai" ML
        ↓
     PyTorch     ← Deep Learning
        ↓
  Hugging Face   ← LLM, transformers
```

---

## Conseils de Guido (le créateur de Python)

1. **Ne mémorise pas, comprends.** Si tu comprends que `for x in liste` signifie
   « pour chaque élément de la liste », tu n'as pas besoin de mémoriser la syntaxe.
   Elle viendra naturellement.

2. **Tape le code toi-même.** Ne copie-colle jamais un exemple. Tape-le lettre par
   lettre. Ton cerveau apprend en tapant, pas en lisant.

3. **Fais des erreurs.** Chaque `TypeError` ou `NameError` t'apprend quelque chose.
   Lis le message d'erreur — Python te dit **exactement** ce qui ne va pas.

4. **Un petit programme qui marche > un gros programme dans ta tête.** Écris 3
   lignes, lance, vérifie. Puis 3 lignes de plus. Jamais 50 lignes d'un coup.

5. **Pour l'IA, le Python "suffisant" arrive vite.** Tu n'as pas besoin d'être un
   expert Python pour faire du ML. Tu as besoin de comprendre les bases et de savoir
   lire la documentation. Le reste s'apprend en faisant.
