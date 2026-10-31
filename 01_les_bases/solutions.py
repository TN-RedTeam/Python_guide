#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 01 : les bases

Le corrigé des exercices de exercices.py, avec le code complet et commenté.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.

Tu peux lancer ce fichier (python3 solutions.py) : il affiche, pour chaque
exercice, le résultat attendu. Compare-le à ce que TON code produit.
"""


# ── EXERCICE 1 — Se présenter ────────────────────────────────────────
prenom = "Ada"
print(f"Bonjour {prenom} !")
# La f-string (le f devant les guillemets) remplace {prenom} par sa valeur.


# ── EXERCICE 2 — La catégorie d'âge ──────────────────────────────────
age = 15
if age >= 18:
    print("Majeur")
elif age >= 13:
    print("Adolescent")
else:
    print("Enfant")
# L'ordre compte : on teste d'abord >= 18, puis >= 13, sinon c'est Enfant.
# (Avec age = 15, c'est le elif >= 13 qui gagne -> Adolescent.)


# ── EXERCICE 3 — Pair ou impair ? ────────────────────────────────────
nombre = 7
if nombre % 2 == 0:
    print(f"{nombre} est pair")
else:
    print(f"{nombre} est impair")
# nombre % 2 donne le reste de la division par 2 : 0 = pair, sinon impair.


# ── EXERCICE 4 — Additionner de 1 à n ────────────────────────────────
n = 5
total = 0                      # on part de 0
for i in range(1, n + 1):      # range(1, 6) -> 1, 2, 3, 4, 5
    total = total + i          # on ajoute i au total à chaque tour
print(total)                   # 15, affiché APRÈS la boucle
# range(1, n + 1) : le + 1 sert à inclure n (la fin de range est exclue).


# ── EXERCICE 5 — La table de multiplication ──────────────────────────
table = 7
for i in range(1, 11):         # i prend 1, 2, ..., 10
    print(f"{table} x {i} = {table * i}")
# Une f-string peut contenir un calcul : {table * i} est évalué à chaque tour.


# ── EXERCICE 6 — FizzBuzz ────────────────────────────────────────────
nombre_fb = 15
if nombre_fb % 3 == 0 and nombre_fb % 5 == 0:   # le cas le PLUS précis d'abord
    print("FizzBuzz")
elif nombre_fb % 3 == 0:
    print("Fizz")
elif nombre_fb % 5 == 0:
    print("Buzz")
else:
    print(nombre_fb)
# Piège classique : si on testait "par 3" avant "par 3 ET par 5", le nombre 15
# tomberait dans "Fizz" et on n'afficherait jamais "FizzBuzz". D'où l'ordre.
