#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 07 : débugger   (série 2, après exercices.py)

──────────────────────────────────────────────────────────────────────
 Deux façons de travailler :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier. Ici, la surprise EST la leçon.
   🐞 CORRIGER  : trois nouvelles fonctions buggées. Aucune ne plante :
                 elles donnent un résultat FAUX, ce qui est plus vicieux.
──────────────────────────────────────────────────────────────────────

 Rappel de la méthode :
   1. Lis le résultat faux : de combien est-il faux ? dans quel sens ?
   2. Ajoute un print(...) DANS la fonction pour voir une valeur évoluer.
   3. Compare ce que tu vois à ce que tu attendais.

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Deux noms, combien de listes ?
# ══════════════════════════════════════════════════════════════════════
#  On « copie » la liste des prix, puis on ajoute un prix à la copie.
#  Combien d'éléments contient  prix  à la fin : 2 ou 3 ?
#  ✏️ ma prédiction :

prix = [10, 20]
copie = prix
copie.append(30)
print("LIRE 1 →", len(prix))


# ══════════════════════════════════════════════════════════════════════
#  🐞 CORRIGER 1 — La remise
# ══════════════════════════════════════════════════════════════════════
#  Un article à 50 € avec 20 % de remise devrait coûter 40 €.
#  La fonction renvoie un prix négatif énorme.
#
#  👀 Résultat attendu :
#     Corriger 1 : 40.0

def appliquer_remise(prix, pourcentage):
    return prix - prix * pourcentage

print("Corriger 1 :", appliquer_remise(50, 20))


# ══════════════════════════════════════════════════════════════════════
#  🐞 CORRIGER 2 — Les mots d'au moins 5 lettres
# ══════════════════════════════════════════════════════════════════════
#  Dans ["table", "chat", "ordinateur", "lampe"], trois mots ont AU MOINS
#  5 lettres (table, ordinateur, lampe). La fonction en compte 1.
#
#  👀 Résultat attendu :
#     Corriger 2 : 3

def compter_mots_longs(mots):
    total = 0
    for mot in mots:
        if len(mot) > 5:
            total += 1
    return total

print("Corriger 2 :", compter_mots_longs(["table", "chat", "ordinateur", "lampe"]))


# ══════════════════════════════════════════════════════════════════════
#  🐞 CORRIGER 3 — Le total du panier
# ══════════════════════════════════════════════════════════════════════
#  5 + 10 + 15 = 30. La fonction renvoie 5 : elle semble s'arrêter après
#  le premier article.
#
#  👀 Résultat attendu :
#     Corriger 3 : 30

def total_panier(prix):
    somme = 0
    for p in prix:
        somme += p
        return somme

print("Corriger 3 :", total_panier([5, 10, 15]))
