#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 16 : NumPy

Le corrigé des exercices, avec le code complet et commenté.
Lance-le (python3 solutions.py) pour voir tous les résultats attendus.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""

import numpy as np


# ── EXERCICE 1 — Créer un tableau ────────────────────────────────────
releves = [12, 15, 18, 21, 19, 16, 11]
temperatures = np.array(releves)     # la liste devient un tableau NumPy
print(temperatures.shape)            # (7,) : 7 valeurs, une seule dimension


# ── EXERCICE 2 — Calculer sur tout le tableau d'un coup ──────────────
print(temperatures + 2)              # +2 est appliqué à CHAQUE valeur, sans boucle
# Avec une liste Python, il aurait fallu : [t + 2 for t in releves]


# ── EXERCICE 3 — Des statistiques en une ligne ───────────────────────
print(temperatures.mean())           # la moyenne -> 16.0
print(temperatures.max())            # la plus haute -> 21


# ── EXERCICE 4 — Filtrer avec un masque ──────────────────────────────
print(temperatures[temperatures > 17])
# temperatures > 17 fabrique un tableau de True/False (le « masque ») ;
# mis entre crochets, il ne garde que les cases où c'est True.


# ── EXERCICE 5 — Un tableau à 2 dimensions ───────────────────────────
notes = np.array([[12, 15, 9],
                  [18, 14, 16]])
print(notes.shape)                   # (2, 3) : 2 lignes (élèves), 3 colonnes (matières)
print(notes.mean(axis=1))            # axis=1 : on calcule LE LONG de chaque ligne
# axis=0 aurait donné la moyenne par matière (le long de chaque colonne).


# ── EXERCICE 6 — Normaliser entre 0 et 1 ─────────────────────────────
prix = np.array([10, 20, 30, 40, 50])
print((prix - prix.min()) / (prix.max() - prix.min()))
# (valeur - minimum) / (maximum - minimum) : le plus petit devient 0, le plus
# grand devient 1. C'est une préparation de données très courante en IA.
