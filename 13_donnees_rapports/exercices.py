#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 13 : données & rapports (pandas)

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE :
   • Tu travailles sur un VRAI fichier : depenses.csv (un relevé de
     dépenses). Il est créé juste en dessous, tu vois tout son contenu.
   • Tu écris ton code dans « ✏️ ton code ici », puis tu affiches.
   • Tu lances, tu compares l'affichage au « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Il te faut pandas :  pip install pandas   (déjà fait si tu as installé
 requirements.txt). Lancer :  python3 exercices.py

 💡 Sur ton PC : exporte le relevé de ta banque en CSV, remplace
    "depenses.csv" par ce fichier, adapte les noms de colonnes — et tu
    obtiens les mêmes analyses sur TES vraies dépenses.
"""

import pandas as pd

# Le fichier de départ : on l'écrit sur le disque pour que tu puisses
# l'ouvrir aussi dans un tableur ou un éditeur de texte.
CONTENU_CSV = """date,categorie,libelle,montant
2026-01-03,courses,Supermarché,62.5
2026-01-05,transport,Essence,48.0
2026-01-09,loisirs,Cinéma,11.0
2026-01-12,courses,Marché,23.5
2026-01-15,logement,Loyer,750.0
2026-01-20,transport,Train,35.0
2026-01-27,courses,Supermarché,71.0
"""
with open("depenses.csv", "w", encoding="utf-8") as f:
    f.write(CONTENU_CSV)


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Charger le fichier
# ══════════════════════════════════════════════════════════════════════
#  Charge depenses.csv dans un DataFrame nommé  df, puis affiche sa taille
#  (nombre de lignes, nombre de colonnes).
#  🧰 Outils : pd.read_csv, .shape
#
#  👀 Résultat attendu :
#     (7, 4)

# ✏️ ton code ici (garde bien le nom  df : les exercices suivants s'en servent) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Le total des dépenses
# ══════════════════════════════════════════════════════════════════════
#  Affiche la somme de toute la colonne "montant".
#  🧰 Outils : sélectionner une colonne, .sum()
#
#  👀 Résultat attendu :
#     1001.0

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Les grosses dépenses (filtrer)
# ══════════════════════════════════════════════════════════════════════
#  Garde uniquement les dépenses de PLUS de 50 €, et affiche la liste de
#  leurs libellés.
#  🧰 Outils : un filtre  df[condition], une colonne, .tolist()
#
#  👀 Résultat attendu :
#     ['Supermarché', 'Loyer', 'Supermarché']

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Les 3 plus grosses dépenses (trier)
# ══════════════════════════════════════════════════════════════════════
#  Trie les dépenses de la plus chère à la moins chère, garde les 3
#  premières, et affiche la liste de leurs libellés.
#  🧰 Outils : .sort_values, .head, .tolist()
#
#  👀 Résultat attendu :
#     ['Loyer', 'Supermarché', 'Supermarché']

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — Le total par catégorie (groupby)
# ══════════════════════════════════════════════════════════════════════
#  Calcule le total dépensé dans chaque catégorie. Range le résultat dans
#  une variable  par_categorie  et affiche-la.
#  🧰 Outils : .groupby, une colonne, .sum()
#
#  👀 Résultat attendu (c'est l'affichage normal de pandas) :
#     categorie
#     courses      157.0
#     logement     750.0
#     loisirs       11.0
#     transport     83.0
#     Name: montant, dtype: float64

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 6 — Exporter le rapport (le défi : le pipeline complet)
# ══════════════════════════════════════════════════════════════════════
#  Enregistre  par_categorie  (exercice 5) dans un fichier
#  "rapport_depenses.csv", puis relis ce fichier et affiche son contenu.
#  🧰 Outils : .to_csv, with open(...) en lecture
#
#  👀 Résultat attendu :
#     categorie,montant
#     courses,157.0
#     logement,750.0
#     loisirs,11.0
#     transport,83.0

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : pd.read_csv("nom_du_fichier") renvoie le tableau ; range-le
#               dans df. La taille s'obtient avec df.shape (sans parenthèses).
#
#  Exercice 2 : df["montant"] donne la colonne ; ajoute .sum() derrière.
#
#  Exercice 3 : la condition s'écrit df["montant"] > 50. Mets-la entre les
#               crochets de df[...] pour ne garder que ces lignes, puis prends
#               la colonne "libelle" du résultat et termine par .tolist().
#
#  Exercice 4 : df.sort_values("montant", ascending=False) trie du plus grand
#               au plus petit. Enchaîne .head(3), puis la colonne "libelle".
#
#  Exercice 5 : même forme que dans le cours (section 4) : on regroupe par
#               "categorie", on prend la colonne "montant", on additionne.
#
#  Exercice 6 : par_categorie.to_csv("rapport_depenses.csv") écrit le fichier.
#               Pour le relire : with open(..., "r", encoding="utf-8") as f,
#               puis print(f.read()).
