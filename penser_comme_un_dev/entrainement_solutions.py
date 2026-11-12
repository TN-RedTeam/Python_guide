#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement de « Penser comme un dev »

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit ta prédiction et essayé.
"""


# ── 👓 LIRE 1 — Deux patterns dans la même boucle ────────────────────
nombres = [4, 7, 10]
total = 0
compte = 0
for n in nombres:
    if n > 5:
        total = total + n       # accumulateur : on additionne ceux qui passent le test
        compte = compte + 1     # compteur : on compte ceux qui passent le test
print("LIRE 1 →", total, compte)
# Réponse : 17 2. Le tableau, tour par tour :
#     n = 4   -> 4 > 5 est faux : rien ne change      total = 0    compte = 0
#     n = 7   -> vrai                                 total = 7    compte = 1
#     n = 10  -> vrai                                 total = 17   compte = 2
# Ce tableau s'appelle une « trace ». C'est LE geste à faire dès qu'un code
# te résiste : une colonne par variable, une ligne par tour.


# ── 🔧 MODIFIER 1 — Du compteur au filtre ────────────────────────────
temperatures = [18, 22, 25, 19, 21]
jours_chauds = []                   # une LISTE vide au lieu d'un compteur à 0
for t in temperatures:
    if t > 20:
        jours_chauds.append(t)      # on GARDE la valeur au lieu d'ajouter 1
print(jours_chauds)
# Compteur et filtre ont exactement la même forme : seuls changent la valeur
# de départ (0 ou []) et ce qu'on fait quand le test est vrai (+1 ou append).


# ── ✍️ ÉCRIRE 1 — La moyenne d'une liste de notes ────────────────────
notes = [12, 15, 9]
if len(notes) == 0:                 # le cas limite d'abord : pas de division par zéro
    print("aucune note")
else:
    somme = 0                       # pattern accumulateur
    for note in notes:
        somme = somme + note
    print(somme / len(notes))       # 36 / 3 = 12.0


# ── ✍️ ÉCRIRE 2 — Le prix le plus bas ────────────────────────────────
prix = [30, 12, 45, 8, 20]
plus_bas = prix[0]                  # pattern champion : on part du premier
for p in prix:
    if p < plus_bas:                # < au lieu de > : on cherche le plus PETIT
        plus_bas = p
print(plus_bas)
