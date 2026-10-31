#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 02 : les collections

Le corrigé des exercices, avec le code complet et commenté.
Lance-le (python3 solutions.py) pour voir tous les résultats attendus.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""


# ── EXERCICE 1 — Lire un élément d'une liste ─────────────────────────
fruits = ["pomme", "banane", "cerise"]
print(fruits[1])          # index 1 = le 2e élément (on compte à partir de 0)


# ── EXERCICE 2 — Le total d'un panier ────────────────────────────────
panier = {"pain": 1.2, "lait": 0.8}
print(sum(panier.values()))   # .values() -> 1.2 et 0.8 ; sum les additionne -> 2.0


# ── EXERCICE 3 — Compter dans une liste ──────────────────────────────
notes = [1, 2, 2, 3, 2]
compteur = 0
for note in notes:
    if note == 2:
        compteur = compteur + 1
print(compteur)               # 3
# Variante courte : print(notes.count(2))


# ── EXERCICE 4 — Les produits en rupture ─────────────────────────────
stock = {"pommes": 5, "poires": 0, "kiwis": 0}
for produit, quantite in stock.items():   # .items() donne (clé, valeur)
    if quantite == 0:
        print(produit)                     # poires, puis kiwis


# ── EXERCICE 5 — Enlever les doublons et trier ───────────────────────
valeurs = [3, 1, 2, 3, 1]
print(sorted(set(valeurs)))   # set() enlève les doublons, sorted() trie -> [1, 2, 3]


# ── EXERCICE 6 — Compter chaque mot ──────────────────────────────────
mots = ["a", "b", "a"]
compteur_mots = {}
for mot in mots:
    compteur_mots[mot] = compteur_mots.get(mot, 0) + 1
print(compteur_mots)          # {'a': 2, 'b': 1}
# .get(mot, 0) : le compte actuel du mot, ou 0 s'il n'est pas encore dans le dict.
