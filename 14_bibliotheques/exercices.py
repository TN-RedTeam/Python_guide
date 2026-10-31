#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 14 : les bibliothèques

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (3 lignes, lis-les une fois) :
   • Chaque exercice te donne les valeurs de départ — elles sont ÉCRITES,
     tu les VOIS. Rien n'est caché.
   • Tu écris ton code dans l'espace « ✏️ ton code ici ».
   • Tu lances le fichier, tu regardes ce qui s'affiche, et tu compares
     avec le « 👀 Résultat attendu » écrit au-dessus. C'est tout.
──────────────────────────────────────────────────────────────────────

 Pas de correction automatique : juste toi, du code, et ce qui s'affiche.
 Ici on pratique avec des modules de la bibliothèque STANDARD (déjà
 installés, aucun pip nécessaire) : math, random, statistics…

 Lancer :   python3 exercices.py
 Le cours est dans README.md ; le corrigé (si bloqué) dans solutions.py.
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Importer et utiliser un module (math)
# ══════════════════════════════════════════════════════════════════════
#  Importe le module  math  puis affiche la racine carrée de 16
#  avec  math.sqrt(16).
#
#  👀 Résultat attendu :
#     4.0

# ✏️ ton code ici (commence par  import math) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Importer juste UNE fonction (from … import)
# ══════════════════════════════════════════════════════════════════════
#  Avec  from statistics import mean , calcule et affiche la moyenne
#  de la liste  notes.
#
#  👀 Résultat attendu (avec notes = [10, 20, 30]) :
#     20

notes = [10, 20, 30]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Renommer un module à l'import (import … as)
# ══════════════════════════════════════════════════════════════════════
#  Importe  random  sous le nom court  rnd  (import random as rnd), fixe
#  la graine avec  rnd.seed(0)  (pour un résultat reproductible), puis
#  affiche  rnd.randint(1, 6)  (un dé).
#  Note : avec seed(0), le résultat est TOUJOURS le même -> comparable.
#
#  👀 Résultat attendu :
#     4

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Fabriquer une ligne de requirements.txt
# ══════════════════════════════════════════════════════════════════════
#  Un fichier requirements.txt fige les versions des paquets à installer,
#  une ligne par paquet, au format  nom==version.
#  Avec  paquet = "requests"  et  version = "2.31.0", affiche la ligne.
#
#  👀 Résultat attendu :
#     requests==2.31.0

paquet = "requests"
version = "2.31.0"

# ✏️ ton code ici (une f-string avec == au milieu) :


