#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 03 : fonctions & modules

Le corrigé des exercices, avec le code complet et commenté.
Lance-le (python3 solutions.py) pour voir tous les résultats attendus.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""


# ── EXERCICE 1 — Ta première fonction ────────────────────────────────
def double(n):
    return n * 2          # « return » RENVOIE le résultat à qui a appelé

print(double(5))          # ici n vaut 5 (c'est TOI qui le donnes) -> 10


# ── EXERCICE 2 — Paramètre avec valeur par défaut ────────────────────
def saluer(nom, politesse="Bonjour"):
    return f"{politesse} {nom} !"

print(saluer("Ada"))          # politesse non donnée -> "Bonjour" -> Bonjour Ada !
print(saluer("Ada", "Salut")) # politesse = "Salut"            -> Salut Ada !


# ── EXERCICE 3 — Compter les mots ────────────────────────────────────
def compter_mots(phrase):
    return len(phrase.split())    # split() -> liste de mots ; len() les compte

print(compter_mots("le chat dort"))   # 3


# ── EXERCICE 4 — Nombre variable d'arguments (*args) ─────────────────
def moyenne(*notes):
    if not notes:                     # aucune note -> on évite la division par zéro
        return 0
    return sum(notes) / len(notes)

print(moyenne(10, 20))   # (10 + 20) / 2 -> 15.0
print(moyenne())         # aucune note    -> 0


# ── EXERCICE 5 — Trier par longueur (lambda) ─────────────────────────
def trier_par_longueur(mots):
    return sorted(mots, key=lambda mot: len(mot))
    # key=lambda mot: len(mot) : trie en comparant la LONGUEUR de chaque mot

print(trier_par_longueur(["python", "go", "rust"]))   # ['go', 'rust', 'python']
