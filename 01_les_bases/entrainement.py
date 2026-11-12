#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 01 : les bases   (série 2, à faire après exercices.py)

──────────────────────────────────────────────────────────────────────
 Trois façons de travailler la même matière :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier. C'est comme ça qu'on apprend à
                 « exécuter le code dans sa tête ».
   🔧 MODIFIER  : un petit script qui marche déjà. Change-le pour
                 obtenir le nouveau résultat demandé.
   ✍️ ÉCRIRE    : comme dans exercices.py, mais sans indice ni liste
                 d'outils. C'est à toi de reconnaître quoi utiliser.
──────────────────────────────────────────────────────────────────────

 MÉTHODE : note d'abord tes prédictions (lignes « ✏️ ma prédiction »),
 PUIS lance le fichier et compare avec les lignes « LIRE … → ».

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Une variable qui change
# ══════════════════════════════════════════════════════════════════════
#  Que vaut  stock  à la fin ? Suis-le ligne par ligne.
#  ✏️ ma prédiction :

stock = 10
stock = stock - 3
stock = stock * 2
print("LIRE 1 →", stock)


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 2 — Une boucle avec une condition
# ══════════════════════════════════════════════════════════════════════
#  Que vaut  total  à la fin ? Écris la valeur de i et de total à chaque tour.
#  ✏️ ma prédiction :

total = 0
for i in range(1, 6):
    if i % 2 == 0:
        total = total + i
print("LIRE 2 →", total)


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — L'ascenseur
# ══════════════════════════════════════════════════════════════════════
#  Ce script fait monter un ascenseur du 1er au 5e étage. Modifie-le pour
#  qu'il monte jusqu'au 6e, et qu'il ne s'arrête qu'aux étages PAIRS.
#
#  👀 Résultat attendu APRÈS ta modification :
#     Étage 2
#     Étage 4
#     Étage 6

for etage in range(1, 6):
    print(f"Étage {etage}")


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — Le prix soldé
# ══════════════════════════════════════════════════════════════════════
#  Un article coûte  prix  euros et il est soldé à  reduction  pour cent.
#  Affiche le prix soldé dans une phrase.
#
#  👀 Résultat attendu :
#     Prix soldé : 60.0 €

prix = 80
reduction = 25

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — La mention
# ══════════════════════════════════════════════════════════════════════
#  Affiche la mention qui correspond à  moyenne :
#     16 ou plus -> Très bien      14 ou plus -> Bien
#     12 ou plus -> Assez bien     10 ou plus -> Passable
#     en dessous -> Recalé
#  Teste aussi avec 9, 10 et 16 en changeant la valeur.
#
#  👀 Résultat attendu :
#     Assez bien

moyenne = 13.5

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 3 — Combien de semaines pour économiser ?
# ══════════════════════════════════════════════════════════════════════
#  Tu as  economies  euros et tu ajoutes  par_semaine  euros chaque semaine.
#  Affiche le nombre de semaines nécessaires pour atteindre AU MOINS
#  objectif  euros. (Ici on ne connaît pas d'avance le nombre de tours.)
#
#  👀 Résultat attendu :
#     6

economies = 20
par_semaine = 15
objectif = 100

# ✏️ ton code ici :

