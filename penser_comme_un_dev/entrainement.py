#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — 🧭 Penser comme un dev   (série 2, après exercices.py)

──────────────────────────────────────────────────────────────────────
 Trois façons de travailler la même matière :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier.
   🔧 MODIFIER  : un petit script qui marche déjà. Change-le pour
                 obtenir le nouveau résultat demandé.
   ✍️ ÉCRIRE    : comme dans exercices.py, mais cette fois le titre ne
                 te dit plus quel pattern utiliser : à toi de le reconnaître.
──────────────────────────────────────────────────────────────────────

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Deux patterns dans la même boucle
# ══════════════════════════════════════════════════════════════════════
#  Fais un tableau à 3 colonnes (n, total, compte) et remplis une ligne
#  par tour de boucle. Que valent  total  et  compte  à la fin ?
#  ✏️ ma prédiction :

nombres = [4, 7, 10]
total = 0
compte = 0
for n in nombres:
    if n > 5:
        total = total + n
        compte = compte + 1
print("LIRE 1 →", total, compte)


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — Du compteur au filtre
# ══════════════════════════════════════════════════════════════════════
#  Ce script COMPTE les jours où il a fait plus de 20 degrés. Modifie-le
#  pour qu'il construise et affiche la LISTE de ces températures.
#
#  👀 Résultat attendu APRÈS ta modification :
#     [22, 25, 21]

temperatures = [18, 22, 25, 19, 21]
jours_chauds = 0
for t in temperatures:
    if t > 20:
        jours_chauds = jours_chauds + 1
print(jours_chauds)


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — La moyenne d'une liste de notes
# ══════════════════════════════════════════════════════════════════════
#  Calcule et affiche la moyenne de  notes, avec une boucle (sans sum).
#  CAS LIMITE : si la liste est vide, affiche "aucune note" au lieu de
#  planter. Teste-le en remplaçant la liste par [].
#
#  👀 Résultat attendu :
#     12.0

notes = [12, 15, 9]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — Le prix le plus bas
# ══════════════════════════════════════════════════════════════════════
#  Trouve et affiche le plus PETIT prix de la liste, avec une boucle
#  (sans la fonction min).
#
#  👀 Résultat attendu :
#     8

prix = [30, 12, 45, 8, 20]

# ✏️ ton code ici :

