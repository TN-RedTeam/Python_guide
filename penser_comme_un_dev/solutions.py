#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — 🧭 Penser comme un dev : les 5 patterns

Le corrigé des exercices, en code complet et commenté.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
L'écart entre TA version et celle-ci, c'est ta leçon.

Lance-le (python3 solutions.py) : il affiche les résultats attendus.
"""


# ── EXERCICE 1 — ACCUMULATEUR ────────────────────────────────────────
nombres = [2, 5, 3]
total = 0                         # le « sac » qui démarre vide
for n in nombres:
    total = total + n             # on ajoute chaque nombre au sac
print(total)                      # 10


# ── EXERCICE 2 — COMPTEUR ────────────────────────────────────────────
mots = ["ok", "chien", "a", "table"]
compte = 0
for mot in mots:
    if len(mot) > 3:              # la condition à compter
        compte = compte + 1
print(compte)                     # 2  (chien, table)


# ── EXERCICE 3 — RECHERCHE + DRAPEAU ─────────────────────────────────
valeurs = [4, 8, 15]
cible = 8
trouve = False                    # le « drapeau » : pas encore vu
for x in valeurs:
    if x == cible:
        trouve = True             # on lève le drapeau
if trouve:
    print("trouvé")
else:
    print("absent")               # trouvé


# ── EXERCICE 4 — FILTRE ──────────────────────────────────────────────
serie = [1, 2, 3, 4]
gardes = []                       # la liste des élus démarre vide
for n in serie:
    if n % 2 == 0:
        gardes.append(n)
print(gardes)                     # [2, 4]


# ── EXERCICE 5 — CHAMPION (max) + cas limite ─────────────────────────
classement = [3, 9, 2]
if not classement:                # CAS LIMITE : liste vide -> pas de champion
    print(None)
else:
    meilleur = classement[0]      # on parie sur le premier
    for n in classement:
        if n > meilleur:          # quelqu'un fait mieux ? il devient champion
            meilleur = n
    print(meilleur)               # 9
