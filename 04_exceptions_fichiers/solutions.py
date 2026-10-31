#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 04 : exceptions & fichiers

Le corrigé des exercices, avec le code complet et commenté.
Lance-le (python3 solutions.py) pour voir tous les résultats attendus.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""


# ── EXERCICE 1 — Partager l'addition sans planter ────────────────────
addition = 60
convives = 0
try:
    print(addition / convives)   # tenté d'abord
except ZeroDivisionError:
    print(None)                  # exécuté seulement si convives vaut 0
# Avec convives = 0 -> None. Avec convives = 4 -> 15.0.


# ── EXERCICE 2 — Valider une saisie ──────────────────────────────────
saisie = "abc"
try:
    print(int(saisie))           # int("abc") lève une ValueError
except ValueError:
    print(None)
# Avec "abc" -> None. Avec "25" -> 25.


# ── EXERCICE 3 — Écrire une note, puis la relire ─────────────────────
chemin = "journal.txt"
note = "Acheter du pain"
with open(chemin, "w", encoding="utf-8") as f:   # "w" : crée/écrase le fichier
    f.write(note)
with open(chemin, "r", encoding="utf-8") as f:   # "r" : lit le fichier
    print(f.read())              # Acheter du pain
# `with` referme le fichier tout seul à la fin du bloc.


# ── EXERCICE 4 — Compter les lignes d'un fichier (0 s'il manque) ─────
chemin = "ce_fichier_nexiste_pas.txt"
try:
    with open(chemin, "r", encoding="utf-8") as f:
        print(len(f.readlines()))     # readlines() -> liste des lignes
except FileNotFoundError:
    print(0)                          # fichier absent -> 0 au lieu de planter
