#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 14 : les bibliothèques

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (lis-les une fois) :
   • Chaque exercice te donne les valeurs de départ — elles sont ÉCRITES,
     tu les VOIS. Rien n'est caché.
   • Tu écris ton code dans l'espace « ✏️ ton code ici ».
   • Tu lances le fichier, tu regardes ce qui s'affiche, et tu compares
     avec le « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 Ici on pratique avec des modules de la bibliothèque STANDARD (déjà
 installés, aucun pip nécessaire) : math, random, statistics…

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Lancer :   python3 exercices.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Importer et utiliser un module
# ══════════════════════════════════════════════════════════════════════
#  Affiche la racine carrée de 16, en te servant du module  math.
#  🧰 Outils : import, la fonction sqrt du module math
#
#  👀 Résultat attendu :
#     4.0

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Importer juste UNE fonction
# ══════════════════════════════════════════════════════════════════════
#  Calcule et affiche la moyenne de la liste  notes  avec la fonction
#  mean  du module  statistics — en n'important QUE cette fonction (pas
#  le module entier).
#  🧰 Outils : from … import …
#
#  👀 Résultat attendu (avec notes = [10, 20, 30]) :
#     20

notes = [10, 20, 30]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Renommer un module à l'import
# ══════════════════════════════════════════════════════════════════════
#  Importe le module  random  sous le nom court  rnd. Fixe sa graine à 0
#  (pour obtenir toujours le même tirage, donc un résultat comparable),
#  puis affiche un lancer de dé : un entier au hasard entre 1 et 6.
#  🧰 Outils : import … as …, les fonctions seed et randint
#
#  👀 Résultat attendu :
#     4

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Fabriquer une ligne de requirements.txt
# ══════════════════════════════════════════════════════════════════════
#  Un fichier requirements.txt fige les versions des paquets à installer,
#  une ligne par paquet, au format  nom==version.
#  Affiche la ligne correspondant à  paquet  et  version.
#  🧰 Outils : une f-string
#
#  👀 Résultat attendu :
#     requests==2.31.0

paquet = "requests"
version = "2.31.0"

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : import math  en première ligne. Une fonction d'un module
#               s'appelle avec le nom du module devant : math.sqrt(16).
#
#  Exercice 2 : from statistics import mean  — ensuite mean(...) s'utilise
#               directement, sans « statistics. » devant.
#
#  Exercice 3 : import random as rnd, puis rnd.seed(0), puis
#               rnd.randint(1, 6) (les deux bornes sont incluses).
#
#  Exercice 4 : le == fait partie du TEXTE à afficher : il se met tel quel
#               dans la f-string, entre les deux accolades.
