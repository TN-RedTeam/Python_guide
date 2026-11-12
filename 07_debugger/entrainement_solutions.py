#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 07 : débugger

Pour chaque bug : la correction, mais surtout COMMENT on pouvait le trouver.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit ta prédiction et essayé.
"""


# ── 👓 LIRE 1 — Deux noms, combien de listes ? ───────────────────────
prix = [10, 20]
copie = prix            # PAS une copie : un 2e NOM pour la MÊME liste
copie.append(30)        # on modifie l'unique liste… donc prix « change » aussi
print("LIRE 1 →", len(prix))
# Réponse : 3. Le signe = ne copie jamais une liste : il pose une 2e étiquette
# sur la même boîte. Pour une vraie copie indépendante :  copie = prix.copy()
# C'est l'un des bugs les plus fréquents : « ma liste a changé toute seule ».


# ── 🐞 CORRIGER 1 — La remise ────────────────────────────────────────
def appliquer_remise(prix, pourcentage):
    return prix - prix * pourcentage / 100      # 20 % = 20 / 100

print("Corriger 1 :", appliquer_remise(50, 20))
# Comment le trouver : le résultat faux était -950. Or 50 - 50 * 20 = -950 :
# le pourcentage était utilisé comme un nombre « brut » au lieu d'une fraction.


# ── 🐞 CORRIGER 2 — Les mots d'au moins 5 lettres ────────────────────
def compter_mots_longs(mots):
    total = 0
    for mot in mots:
        if len(mot) >= 5:           # « au moins 5 » inclut 5 : >= et non >
            total += 1
    return total

print("Corriger 2 :", compter_mots_longs(["table", "chat", "ordinateur", "lampe"]))
# Comment le trouver : seul "ordinateur" était compté. "table" et "lampe" font
# EXACTEMENT 5 lettres : le bug est donc à la frontière. « Au moins », « au
# plus », « strictement » : c'est toujours là qu'il faut vérifier > contre >=.


# ── 🐞 CORRIGER 3 — Le total du panier ───────────────────────────────
def total_panier(prix):
    somme = 0
    for p in prix:
        somme += p
    return somme                    # le return est sorti de la boucle (désindenté)

print("Corriger 3 :", total_panier([5, 10, 15]))
# Comment le trouver : un print(p) dans la boucle n'affiche que 5 : la boucle
# ne fait qu'un tour. Un return DANS la boucle quitte la fonction dès le
# premier passage. Ici, tout le bug tient à 4 espaces d'indentation.
