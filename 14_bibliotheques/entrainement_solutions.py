#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 14 : les bibliothèques

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit ta prédiction et essayé.
"""


# ── 👓 LIRE 1 — Deux façons d'importer ───────────────────────────────
import math                 # importe le MODULE : on écrit math.quelque_chose
from math import floor      # importe UNE fonction : on écrit floor directement

print("LIRE 1 →", math.ceil(4.2), floor(4.8), math.pi > 3)
# Réponse : 5 4 True.
#   math.ceil(4.2) -> 5  (l'entier du dessus)
#   floor(4.8)     -> 4  (l'entier du dessous ; pas de « math. » car importée par son nom)
#   math.pi > 3    -> True (pi vaut 3,14159…)
# « import math » range tout sous le nom math ; « from math import floor »
# pose directement le nom floor dans ton programme.


# ── 🔧 MODIFIER 1 — N'importer que ce dont on a besoin ───────────────
from statistics import mean, median     # plusieurs noms, séparés par des virgules

notes = [8, 12, 19]
print(mean(notes))          # (8 + 12 + 19) / 3 = 13
print(median(notes))        # la valeur du milieu une fois triées : 12


# ── ✍️ ÉCRIRE 1 — Combien de cartons pour déménager ? ────────────────
livres = 50
par_carton = 12
print(math.ceil(livres / par_carton))   # 50 / 12 = 4,17 -> arrondi au-dessus : 5


# ── ✍️ ÉCRIRE 2 — Un tirage au sort qu'on peut rejouer ───────────────
import random

participants = ["Ada", "Bob", "Zoé", "Léo"]
random.seed(1)                          # même graine -> même « hasard » à chaque lancement
print(random.choice(participants))      # choice tire un élément de la liste
