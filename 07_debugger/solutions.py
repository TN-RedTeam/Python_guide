#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 07 : débugger (les bugs corrigés et EXPLIQUÉS)

Lance :   python3 solutions.py   (affiche les résultats attendus).
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment cherché les bugs toi-même.
"""


# ── EXERCICE 1 — moyenne ─────────────────────────────────────────────
def moyenne(notes):
    total = 0
    for note in notes:
        total += note         # ✔ += ADDITIONNE (au lieu de = qui écrasait à chaque tour)
    return total / len(notes)

print("Exercice 1 :", moyenne([10, 20, 30]))   # 20.0


# ── EXERCICE 2 — maximum ─────────────────────────────────────────────
def maximum(liste):
    plus_grand = liste[0]     # ✔ partir du PREMIER élément, jamais de 0
    for valeur in liste:
        if valeur > plus_grand:
            plus_grand = valeur
    return plus_grand

print("Exercice 2 :", maximum([-5, -2, -9]))   # -2


# ── EXERCICE 3 — compter_voyelles ────────────────────────────────────
def compter_voyelles(mot):
    voyelles = "aeiou"
    total = 0
    for lettre in mot:
        if lettre in voyelles:   # ✔ "in" (et non "not in")
            total += 1
    return total

print("Exercice 3 :", compter_voyelles("bonjour"))   # 3


# ── EXERCICE 4 — somme_1_a_n ─────────────────────────────────────────
def somme_1_a_n(n):
    total = 0
    for i in range(1, n + 1):   # ✔ n + 1 pour INCLURE n (la fin de range est exclue)
        total += i
    return total

print("Exercice 4 :", somme_1_a_n(5))   # 15


# ── EXERCICE 5 — additionner_un ──────────────────────────────────────
def additionner_un(texte):
    return int(texte) + 1       # ✔ int(...) convertit le texte en nombre AVANT d'ajouter 1

print("Exercice 5 :", additionner_un("41"))   # 42
