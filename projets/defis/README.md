# 🎯 Les défis — des projets à faire toi-même

> 🎯 **À quoi sert ce dossier ?** Les exercices d'un module ne travaillent que **ce** module.
> Un défi, lui, te fait **réutiliser plusieurs modules à la fois** dans un vrai petit
> programme, sur de **vrais fichiers**. C'est le moment où les briques s'assemblent — et où
> tu vérifies que ce que tu as appris il y a trois modules est toujours là.

Les mini-projets du dossier parent (`projets/`) sont des programmes **finis, à lire**. Ici
c'est l'inverse : le fichier est **vide**, c'est **toi** qui écris le programme.

---

## 🗺️ Quel défi, à quel moment ?

| Défi | À faire après | Ce que tu construis |
|------|---------------|---------------------|
| **1.** [`defi_1_releve_depenses.py`](./defi_1_releve_depenses.py) | les modules **01 à 04** | Lire un relevé de dépenses (CSV), calculer les totaux, classer les catégories, enregistrer un rapport. |
| **2.** [`defi_2_inventaire.py`](./defi_2_inventaire.py) | les modules **05 à 07** | Un inventaire de fichiers avec deux classes : poids total, plus gros fichier, tri par type. |
| **3.** [`defi_3_comparer_dossiers.py`](./defi_3_comparer_dossiers.py) | le module **10** | Comparer un dossier et sa sauvegarde : fichiers manquants, en trop, modifiés — puis réparer. |
| **4.** [`defi_4_renommer_photos.py`](./defi_4_renommer_photos.py) | le module **10** | Renommer des photos en série, avec un mode « simulation » qui montre le plan avant d'agir. |
| **5.** [`defi_5_tableau_de_bord.py`](./defi_5_tableau_de_bord.py) | les modules **13 et 16** | Refaire le défi 1 avec pandas et NumPy : totaux par mois, parts en %, dépenses hors norme. |

---

## 🧭 Comment travailler un défi

1. **Lis tout l'énoncé d'abord**, sans coder. Repère ce qui entre (le fichier, le dossier) et
   ce qui doit sortir (les résultats attendus). C'est le « temps 1 » de
   [🧭 Penser comme un dev](../../penser_comme_un_dev/).
2. **Avance étape par étape.** Chaque étape a son **👀 résultat attendu** : lance le fichier
   après chacune et compare. Ne passe pas à la suivante tant que celle-ci n'est pas bonne.
3. **Écris une fonction par étape.** Les dernières étapes réutilisent les premières : si tu as
   tout écrit « en vrac », tu devras recopier ; avec des fonctions, tu n'as qu'à les appeler.
4. **Bloqué ?** C'est prévu. Un défi se fait en **plusieurs séances**. Reviens au cours du
   module concerné (il est indiqué en tête de fichier), puis réessaie. Le corrigé
   (`…_solution.py`) ne sert qu'**après** un vrai essai : compare-le à **ta** version.
5. **Termine par « Pour aller plus loin »**, en bas de chaque fichier. Ces extensions n'ont
   **pas de corrigé** : à ce stade, c'est ton programme.

```bash
python3 projets/defis/defi_1_releve_depenses.py
```

> 🛡️ **Sans risque.** Les défis qui touchent à des fichiers fabriquent leur propre dossier de
> test (dans un dossier temporaire ou à côté du script). Ils ne touchent **jamais** à tes
> vrais fichiers tant que tu ne changes pas toi-même les chemins. Chaque défi t'explique, dans
> sa note **💡 Sur ton PC**, comment l'appliquer ensuite à tes propres données — et quelles
> précautions prendre.

---

## ✅ Tu as réussi un défi quand…

- chaque **résultat attendu** s'affiche exactement ;
- tu peux **expliquer chaque ligne** de ton programme à voix haute ;
- tu as changé les données de départ (une ligne en plus dans le CSV, un fichier en plus dans le
  dossier) et ton programme donne toujours un résultat juste.

Ce troisième point est le vrai test : un programme qui ne marche que sur l'exemple n'est pas
fini.
