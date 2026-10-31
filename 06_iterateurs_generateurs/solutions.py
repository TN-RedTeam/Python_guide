#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 06 : itérateurs & générateurs

Le corrigé des exercices, avec le code complet et commenté.
Lance-le (python3 solutions.py) pour voir tous les résultats attendus.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""


# ── EXERCICE 1 — Filtrer une liste ───────────────────────────────────
nombres = [3, -1, 0, 7, -2]
print([n for n in nombres if n > 0])      # [3, 7]
# Lecture : [ ce qu'on garde  for n in source  if condition ]


# ── EXERCICE 2 — Transformer une liste ───────────────────────────────
noms = ["ada", "bob"]
print([nom.upper() for nom in noms])      # ['ADA', 'BOB']


# ── EXERCICE 3 — Additionner au vol ──────────────────────────────────
n = 4
print(sum(i ** 2 for i in range(n)))      # 0+1+4+9 -> 14
# Les parenthèses (au lieu de crochets) créent un générateur : aucune
# liste n'est construite, sum additionne les carrés au fur et à mesure.


# ── EXERCICE 4 — Écrire un générateur (yield) ────────────────────────
def pairs_jusqua(limite):
    n = 0
    while n < limite:
        yield n          # livre n, met la fonction en pause, reprend ici ensuite
        n += 2

print(list(pairs_jusqua(10)))             # [0, 2, 4, 6, 8]
# list(...) déroule le générateur jusqu'au bout pour tout afficher.
