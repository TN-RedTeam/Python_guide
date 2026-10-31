#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 09 : tests & qualité

Lance :   python3 solutions.py   (affiche les "... OK" si tout passe).
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""


# ── EXERCICE 1 — est_palindrome + ses tests ──────────────────────────
def est_palindrome(mot):
    return mot == mot[::-1]      # [::-1] renvoie la chaîne inversée

assert est_palindrome("kayak") == True
assert est_palindrome("python") == False
print("palindrome OK")


# ── EXERCICE 2 — inverser + ses tests ────────────────────────────────
def inverser(texte):
    return texte[::-1]

assert inverser("abc") == "cba"
assert inverser("") == ""
print("inverser OK")


# ── EXERCICE 3 — factorielle + ses tests ─────────────────────────────
def factorielle(n):
    resultat = 1
    for i in range(2, n + 1):   # 2, 3, ..., n  (×1 est inutile, on part de 2)
        resultat *= i
    return resultat             # pour n = 0, la boucle ne tourne pas → reste 1

assert factorielle(5) == 120
assert factorielle(0) == 1
print("factorielle OK")
