#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 16 : NumPy

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit ta prédiction et essayé.
"""

import numpy as np


# ── 👓 LIRE 1 — Trois calculs sur des tableaux ───────────────────────
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print("LIRE 1 →", (a + b).tolist(), (a * 2).sum(), (b > 15).sum())
# Réponse : [11, 22, 33] 12 2.
#   a + b         -> case par case : 1+10, 2+20, 3+30
#   (a * 2).sum() -> [2 4 6], dont la somme vaut 12
#   (b > 15)      -> [False True True] ; dans une somme, True compte pour 1 et
#                    False pour 0 : .sum() COMPTE donc les True -> 2.
#   Retiens ce dernier réflexe : (condition).sum() = « combien de cases la vérifient ».


# ── 🔧 MODIFIER 1 — Par élève, ou par matière ? ──────────────────────
notes = np.array([[12, 16, 8],
                  [18, 14, 16],
                  [9, 12, 12]])
print(notes.mean(axis=0))       # axis=0 : le long de chaque COLONNE -> une moyenne par matière


# ── ✍️ ÉCRIRE 1 — Les bonnes journées de vente ───────────────────────
ventes = np.array([120, 80, 150, 90, 200, 60, 110])
bonnes = ventes[ventes > 100]   # le masque garde 120, 150, 200 et 110
print(len(bonnes))
print(bonnes.mean())
# Variante pour le nombre : print((ventes > 100).sum())


# ── ✍️ ÉCRIRE 2 — La part de chaque poste dans le budget ─────────────
budget = np.array([200, 300, 500])
print(budget / budget.sum() * 100)      # chaque case divisée par le total (1000), puis × 100
