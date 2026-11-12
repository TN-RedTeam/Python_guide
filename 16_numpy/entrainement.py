#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 16 : NumPy   (série 2, après exercices.py)

──────────────────────────────────────────────────────────────────────
 Trois façons de travailler la même matière :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier.
   🔧 MODIFIER  : un petit script qui marche déjà. Change-le pour
                 obtenir le nouveau résultat demandé.
   ✍️ ÉCRIRE    : comme dans exercices.py, mais sans indice ni liste
                 d'outils.
──────────────────────────────────────────────────────────────────────

 La règle du jeu ne change pas : AUCUNE boucle for.

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""

import numpy as np


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Trois calculs sur des tableaux
# ══════════════════════════════════════════════════════════════════════
#  Trois valeurs sont affichées : une liste, puis deux nombres.
#  (.tolist() transforme un tableau en liste Python ordinaire.)
#  ✏️ ma prédiction :

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print("LIRE 1 →", (a + b).tolist(), (a * 2).sum(), (b > 15).sum())


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — Par élève, ou par matière ?
# ══════════════════════════════════════════════════════════════════════
#  notes  a une ligne par élève et une colonne par matière. Ce script
#  affiche la moyenne de chaque ÉLÈVE. Modifie-le pour afficher la
#  moyenne de chaque MATIÈRE.
#
#  👀 Résultat attendu APRÈS ta modification :
#     [13. 14. 12.]

notes = np.array([[12, 16, 8],
                  [18, 14, 16],
                  [9, 12, 12]])
print(notes.mean(axis=1))


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — Les bonnes journées de vente
# ══════════════════════════════════════════════════════════════════════
#  ventes  est le chiffre d'affaires de chaque jour d'une semaine.
#  Affiche le NOMBRE de jours à plus de 100 €, puis la MOYENNE de ces
#  jours-là.
#
#  👀 Résultat attendu :
#     4
#     145.0

ventes = np.array([120, 80, 150, 90, 200, 60, 110])

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — La part de chaque poste dans le budget
# ══════════════════════════════════════════════════════════════════════
#  budget  contient trois dépenses (loyer, courses, loisirs). Affiche la
#  part de chacune dans le total, en POURCENTAGE.
#
#  👀 Résultat attendu :
#     [20. 30. 50.]

budget = np.array([200, 300, 500])

# ✏️ ton code ici :

