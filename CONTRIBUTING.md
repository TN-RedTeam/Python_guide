# Contribuer au guide

Merci de contribuer ! Ce dépôt est **à la fois** un cours (fichiers Markdown +
Python) et une plateforme e-learning (`webapp/`). Voici comment ajouter ou
modifier du contenu sans rien casser.

## 🧱 Anatomie d'un module

Chaque module est un dossier `NN_nom` à la racine (ex. `03_fonctions_modules/`) :

```
03_fonctions_modules/
├── README.md        ← le cours (obligatoire)
├── exercices.py     ← exercices à trous (optionnel)
├── solutions.py     ← corrigé des exercices (obligatoire si exercices.py existe)
├── quiz.json        ← QCM auto-corrigé (optionnel)
└── *.py             ← fichiers de démo montrés dans l'onglet « Code du module »
```

- Le **numéro** affiché et l'ordre viennent du préfixe `NN_`.
- Le module de **fondation** `penser_comme_un_dev/` n'a pas de préfixe : il est
  inséré juste après « Démarrer », sans numéro (voir `webapp/build_content.py`).

## ✍️ Écrire le cours (README.md)

Markdown standard, **plus** deux outils propres à la plateforme :

### 1. Encadrés typés

Deux façons de créer un encadré coloré :

- **Bloc `:::`** (recommandé pour du contenu riche) :

  ```markdown
  :::reflexion Réfléchis d'abord : le titre
  Le corps reste du **markdown** normal (listes, `code`, etc.).
  :::
  ```

  Types disponibles : `objectif`, `idee`, `astuce`, `piege`, `etape`,
  `exemple`, `reflexion`, `defi`, `reussi` (variantes FR/EN acceptées).

- **Citation avec emoji** (le style est déduit de l'emoji de tête) :

  ```markdown
  > 🎯 **Objectif** : … (🎯 objectif, 🧠 idée, 💡 astuce, ⚠️ piège, ✅ réussite…)
  ```

### 2. Blocs pseudo-code

Une clôture ```` ```pseudo ```` produit un bloc « raisonnement, pas encore du
Python » (étiqueté, sans bouton *Essayer*). Les blocs ```` ```python ```` ont un
bouton **▶ Essayer** qui envoie le code dans l'IDE.

> Convention utile : ouvrir chaque module par un encadré **`:::reflexion
> Réfléchis d'abord …`** (la logique avant la syntaxe), et le clôturer par une
> section **`## 🔬 Le raisonnement en action`** (problème → pseudo-code → code).

## 🧪 Exercices auto-corrigés

`exercices.py` doit **imprimer un bilan `N/N réussis`** (c'est ce que lit
l'auto-correction). `solutions.py` doit passer à **100 %**. Voir un module
existant pour le format du harnais `verifie(...)`.

## 🧠 Quiz (quiz.json)

Un tableau de questions à choix unique :

```json
[
  {
    "q": "La question (markdown inline autorisé : `code`, **gras**)",
    "options": ["réponse A", "réponse B", "réponse C"],
    "correct": 1,
    "explanation": "Pourquoi c'est la bonne réponse."
  }
]
```

`correct` est l'index (0, 1, 2…) de la bonne option.

## 🔁 Après toute modification

1. **Régénère le contenu embarqué** (obligatoire, sinon le site est périmé) :
   ```bash
   python3 webapp/build_content.py
   ```
2. **Vérifie tout** avant de committer :
   ```bash
   python3 webapp/validate_content.py   # structure, exercices↔solutions, liens, fraîcheur
   python3 webapp/check_solutions.py    # les corrigés passent à 100 %
   ruff check .                         # lint (vrais bugs, pas le style du cours)
   cd webapp/tests && npm install && npx playwright install chromium && node smoke.mjs
   ```

La CI (`.github/workflows/ci.yml`) rejoue exactement ces vérifications.

## 🎨 Style du code du cours

Le code pédagogique est **volontairement** commenté et parfois « non
idiomatique » (imports montrés au fil du texte, variables d'illustration…). On
**ne lui applique pas** de formatage automatique : `ruff format` ne concerne que
l'outillage (`webapp/*.py`). Garde ce style pédagogique.
