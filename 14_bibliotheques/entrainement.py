#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 14 : les bibliothèques   (série 2, après exercices.py)

──────────────────────────────────────────────────────────────────────
 Trois façons de travailler la même matière :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier.
   🔧 MODIFIER  : un petit script qui marche déjà. Change-le pour
                 obtenir le nouveau résultat demandé.
   ✍️ ÉCRIRE    : comme dans exercices.py, mais sans indice ni liste
                 d'outils.
──────────────────────────────────────────────────────────────────────

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Deux façons d'importer
# ══════════════════════════════════════════════════════════════════════
#  math.ceil arrondit à l'entier du DESSUS, math.floor à celui du DESSOUS.
#  Trois valeurs sont affichées. Remarque aussi comment chaque fonction
#  est appelée : avec ou sans « math. » devant — pourquoi ?
#  ✏️ ma prédiction :

import math
from math import floor

print("LIRE 1 →", math.ceil(4.2), floor(4.8), math.pi > 3)


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — N'importer que ce dont on a besoin
# ══════════════════════════════════════════════════════════════════════
#  Ce script importe tout le module statistics pour une seule fonction.
#  Modifie-le pour n'importer QUE les fonctions  mean  et  median, puis
#  affiche la moyenne ET la médiane des notes.
#
#  👀 Résultat attendu APRÈS ta modification :
#     13
#     12

import statistics

notes = [8, 12, 19]
print(statistics.mean(notes))


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — Combien de cartons pour déménager ?
# ══════════════════════════════════════════════════════════════════════
#  Tu as  livres  livres à ranger, et un carton en contient  par_carton.
#  Affiche le nombre de cartons nécessaires. (Un carton à moitié plein
#  reste un carton : il faut arrondir au-dessus.)
#
#  👀 Résultat attendu :
#     5

livres = 50
par_carton = 12

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — Un tirage au sort qu'on peut rejouer
# ══════════════════════════════════════════════════════════════════════
#  Tire au sort un gagnant parmi  participants  avec le module random.
#  Fixe d'abord la graine à 1 : le tirage donnera ainsi toujours le même
#  résultat, ce qui permet de le vérifier. Affiche le gagnant.
#
#  👀 Résultat attendu :
#     Bob

participants = ["Ada", "Bob", "Zoé", "Léo"]

# ✏️ ton code ici :

