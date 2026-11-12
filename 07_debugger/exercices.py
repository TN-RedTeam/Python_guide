#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 07 : débugger (TROUVE ET CORRIGE LES BUGS)

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (différent des autres modules !) :
   • Les fonctions sont DÉJÀ écrites, mais chacune contient UN bug.
   • Juste en dessous, on les appelle avec une valeur VISIBLE et on
     affiche le résultat — tu vois donc tout de suite le mauvais chiffre.
   • Ton travail : trouver la ligne fautive, la corriger, relancer, et
     vérifier que l'affichage correspond au « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 LA MÉTHODE (c'est elle qu'on apprend ici, plus que la correction) :
   1. Lis le résultat faux : de combien est-il faux ? dans quel sens ?
   2. Ajoute un print(...) DANS la fonction pour voir une valeur évoluer.
   3. Compare ce que tu vois à ce que tu attendais : l'écart désigne la ligne.
 (Ou pose un breakpoint() : n = ligne suivante, p nom = afficher une
 variable, c = continuer, q = quitter.)

 BLOQUÉ ?  les indices sont tout EN BAS de ce fichier ; puis solutions.py.

 Lancer :   python3 exercices.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Corrige la moyenne
# ══════════════════════════════════════════════════════════════════════
#  Avec les notes [10, 20, 30], la moyenne devrait être 20.0.
#  La fonction affiche 10.0. Trouve pourquoi et corrige.
#
#  👀 Résultat attendu :
#     Exercice 1 : 20.0

def moyenne(notes):
    total = 0
    for note in notes:
        total = note
    return total / len(notes)

print("Exercice 1 :", moyenne([10, 20, 30]))


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Corrige le maximum
# ══════════════════════════════════════════════════════════════════════
#  Le plus grand nombre de [-5, -2, -9] est -2.
#  La fonction affiche 0 — un nombre qui n'est même pas dans la liste !
#
#  👀 Résultat attendu :
#     Exercice 2 : -2

def maximum(liste):
    plus_grand = 0
    for valeur in liste:
        if valeur > plus_grand:
            plus_grand = valeur
    return plus_grand

print("Exercice 2 :", maximum([-5, -2, -9]))


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Corrige le compteur de voyelles
# ══════════════════════════════════════════════════════════════════════
#  "bonjour" contient 3 voyelles (o, o, u). La fonction affiche 4.
#
#  👀 Résultat attendu :
#     Exercice 3 : 3

def compter_voyelles(mot):
    voyelles = "aeiou"
    total = 0
    for lettre in mot:
        if lettre not in voyelles:
            total += 1
    return total

print("Exercice 3 :", compter_voyelles("bonjour"))


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Corrige la somme de 1 à n
# ══════════════════════════════════════════════════════════════════════
#  1 + 2 + 3 + 4 + 5 = 15. La fonction affiche 10.
#
#  👀 Résultat attendu :
#     Exercice 4 : 15

def somme_1_a_n(n):
    total = 0
    for i in range(1, n):
        total += i
    return total

print("Exercice 4 :", somme_1_a_n(5))


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — Corrige l'addition qui plante
# ══════════════════════════════════════════════════════════════════════
#  additionner_un("41") devrait donner 42. Ici le programme ne donne pas
#  un mauvais résultat : il PLANTE. Lis le message d'erreur en partant de
#  la DERNIÈRE ligne — elle dit ce qui ne va pas, et sur quelle ligne.
#
#  👀 Résultat attendu :
#     Exercice 5 : 42

def additionner_un(texte):
    return texte + 1

print("Exercice 5 :", additionner_un("41"))



# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : ajoute print(total) dans la boucle. Tu verras 10, 20, 30 :
#               total est REMPLACÉ à chaque tour, alors qu'il devrait
#               grossir (10, 30, 60).
#
#  Exercice 2 : d'où peut venir ce 0 ? Regarde la valeur de départ de
#               plus_grand. Aucun nombre négatif ne peut la dépasser.
#               Pars plutôt du premier élément de la liste.
#
#  Exercice 3 : 4, c'est le nombre de… consonnes de "bonjour". La condition
#               du if garde donc l'inverse de ce qu'on veut.
#
#  Exercice 4 : il manque exactement 5, le dernier nombre. Affiche i dans la
#               boucle : où s'arrête range(1, n) ?
#
#  Exercice 5 : « can only concatenate str (not "int") to str » : "41" est
#               du TEXTE. Il faut le convertir en nombre avant d'ajouter 1.
