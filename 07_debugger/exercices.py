#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 07 : débugger (TROUVE ET CORRIGE LES BUGS)

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (différent des autres modules !) :
   • Les fonctions sont DÉJÀ écrites, mais elles contiennent un BUG.
   • Juste en dessous, on les appelle avec une valeur VISIBLE et on
     affiche le résultat — tu vois donc tout de suite le mauvais chiffre.
   • Ton travail : corriger la ligne fautive, relancer, et vérifier que
     l'affichage correspond au « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 Outils de débogage : ajoute un print(...) au milieu du calcul pour voir
 une valeur, ou pose un breakpoint() pour mettre en pause (n = ligne
 suivante, p nom = afficher une variable, c = continuer, q = quitter).

 Lancer :   python3 exercices.py
 Corrigé (en dernier recours) :  solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Corrige la moyenne
# ══════════════════════════════════════════════════════════════════════
#  Avec [10, 20, 30], moyenne() devrait donner 20.0. Elle se trompe.
#  Trouve et corrige le bug dans la fonction.
#
#  👀 Résultat attendu :
#     Exercice 1 : 20.0

def moyenne(notes):
    total = 0
    for note in notes:
        total = note          # 🐞 ici, on ÉCRASE total au lieu de l'additionner
    return total / len(notes)

print("Exercice 1 :", moyenne([10, 20, 30]))


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Corrige le maximum
# ══════════════════════════════════════════════════════════════════════
#  maximum([-5, -2, -9]) devrait donner -2 (le plus grand des négatifs).
#  La fonction renvoie 0 : pourquoi ? Corrige-la.
#
#  👀 Résultat attendu :
#     Exercice 2 : -2

def maximum(liste):
    plus_grand = 0            # 🐞 partir de 0 casse tout si tous les nombres sont négatifs
    for valeur in liste:
        if valeur > plus_grand:
            plus_grand = valeur
    return plus_grand

print("Exercice 2 :", maximum([-5, -2, -9]))


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Corrige le compteur de voyelles
# ══════════════════════════════════════════════════════════════════════
#  compter_voyelles("bonjour") devrait donner 3 (o, o, u). La condition
#  est à l'envers : elle compte les consonnes. Corrige-la.
#
#  👀 Résultat attendu :
#     Exercice 3 : 3

def compter_voyelles(mot):
    voyelles = "aeiou"
    total = 0
    for lettre in mot:
        if lettre not in voyelles:   # 🐞 condition INVERSÉE
            total += 1
    return total

print("Exercice 3 :", compter_voyelles("bonjour"))


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Corrige le compte de 1 à n inclus
# ══════════════════════════════════════════════════════════════════════
#  somme_1_a_n(5) devrait donner 15 (1+2+3+4+5). Elle donne 10 : il manque
#  le 5. C'est le piège classique du range (la fin est EXCLUE). Corrige.
#
#  👀 Résultat attendu :
#     Exercice 4 : 15

def somme_1_a_n(n):
    total = 0
    for i in range(1, n):     # 🐞 range(1, n) s'arrête à n-1 : le n n'est jamais compté
        total += i
    return total

print("Exercice 4 :", somme_1_a_n(5))


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — Corrige l'addition qui plante
# ══════════════════════════════════════════════════════════════════════
#  additionner_un("41") devrait donner 42. Mais le code plante avec une
#  TypeError : on ne peut pas faire "41" + 1 (texte + nombre). Il faut
#  convertir le texte en entier AVANT d'ajouter 1.
#
#  👀 Résultat attendu :
#     Exercice 5 : 42

def additionner_un(texte):
    return texte + 1          # 🐞 "41" est du TEXTE : convertis-le avec int(...) d'abord

print("Exercice 5 :", additionner_un("41"))
