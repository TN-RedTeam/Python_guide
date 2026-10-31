#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 03 : fonctions & modules

Le corrigé des exercices, avec le code complet et commenté.
Lance-le (python3 solutions.py) pour voir tous les résultats attendus.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""


# ── EXERCICE 1 — Calculer un prix TTC ────────────────────────────────
def prix_ttc(prix_ht):
    return prix_ht * 1.2      # +20 % de TVA ; « return » renvoie le résultat

print(prix_ttc(100))          # ici prix_ht vaut 100 (c'est TOI qui le donnes) -> 120.0


# ── EXERCICE 2 — Paramètre avec valeur par défaut ────────────────────
def saluer(nom, politesse="Bonjour"):
    return f"{politesse} {nom} !"

print(saluer("Ada"))          # politesse non donnée -> "Bonjour" -> Bonjour Ada !
print(saluer("Ada", "Salut")) # politesse = "Salut"            -> Salut Ada !


# ── EXERCICE 3 — Compter les mots d'un message ───────────────────────
def compter_mots(message):
    return len(message.split())   # split() -> liste de mots ; len() les compte

print(compter_mots("merci pour ton aide"))   # 4


# ── EXERCICE 4 — La moyenne des notes (*args) ────────────────────────
def moyenne(*notes):
    if not notes:                     # aucune note -> on évite la division par zéro
        return 0
    return sum(notes) / len(notes)

print(moyenne(12, 16, 14))   # (12 + 16 + 14) / 3 -> 14.0
print(moyenne())             # aucune note         -> 0


# ── EXERCICE 5 — Trier des fichiers par longueur de nom (lambda) ─────
def trier_par_longueur(fichiers):
    return sorted(fichiers, key=lambda nom: len(nom))
    # key=lambda nom: len(nom) : trie en comparant la LONGUEUR de chaque nom

print(trier_par_longueur(["rapport.pdf", "cv.pdf", "presentation.pptx"]))
# -> ['cv.pdf', 'rapport.pdf', 'presentation.pptx']  (6, 11, 18 caractères)
