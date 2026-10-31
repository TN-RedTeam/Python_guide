#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 04 : exceptions & fichiers

Le corrigé des exercices, avec le code complet et commenté.
Lance-le (python3 solutions.py) pour voir tous les résultats attendus.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""


# ── EXERCICE 1 — Division sans planter ───────────────────────────────
a = 10
b = 0
try:
    print(a / b)                 # tenté d'abord
except ZeroDivisionError:
    print(None)                  # exécuté seulement si b vaut 0
# Avec b = 0 -> None. Avec b = 2 -> 5.0.


# ── EXERCICE 2 — Convertir un texte en nombre ────────────────────────
texte = "abc"
try:
    print(int(texte))            # int("abc") lève une ValueError
except ValueError:
    print(None)
# Avec "abc" -> None. Avec "42" -> 42.


# ── EXERCICE 3 — Écrire puis relire un fichier ───────────────────────
chemin = "essai.txt"
contenu = "Salut Python !"
with open(chemin, "w", encoding="utf-8") as f:   # "w" : crée/écrase le fichier
    f.write(contenu)
with open(chemin, "r", encoding="utf-8") as f:   # "r" : lit le fichier
    print(f.read())              # Salut Python !
# `with` referme le fichier tout seul à la fin du bloc.


# ── EXERCICE 4 — Lire un fichier qui n'existe peut-être pas ──────────
chemin_absent = "ce_fichier_nexiste_pas.txt"
try:
    with open(chemin_absent, "r", encoding="utf-8") as f:
        print(len(f.readlines()))     # readlines() -> liste des lignes
except FileNotFoundError:
    print(0)                          # fichier absent -> 0 au lieu de planter
