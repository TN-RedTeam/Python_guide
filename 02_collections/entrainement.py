#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 02 : les collections   (série 2, après exercices.py)

──────────────────────────────────────────────────────────────────────
 Trois façons de travailler la même matière :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier.
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
#  👓 LIRE 1 — Une liste qu'on modifie
# ══════════════════════════════════════════════════════════════════════
#  Trois valeurs sont affichées : la longueur, le 1er et le dernier élément.
#  ✏️ ma prédiction :

courses = ["pain", "lait", "oeufs"]
courses.append("beurre")
courses[0] = "baguette"
print("LIRE 1 →", len(courses), courses[0], courses[-1])


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 2 — Un dictionnaire qu'on modifie
# ══════════════════════════════════════════════════════════════════════
#  Deux valeurs sont affichées : le nombre de paires, et l'âge de Bob.
#  ✏️ ma prédiction :

ages = {"Ada": 36, "Bob": 25}
ages["Bob"] = ages["Bob"] + 1
ages["Zoé"] = 19
print("LIRE 2 →", len(ages), ages["Bob"])


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — Des gros fichiers aux petits
# ══════════════════════════════════════════════════════════════════════
#  Ce script affiche le nom des GROS fichiers (plus de 100 Mo). Modifie-le
#  pour qu'il affiche les PETITS fichiers (moins de 10 Mo), avec leur taille.
#
#  👀 Résultat attendu APRÈS ta modification :
#     photo.jpg : 4 Mo
#     cv.pdf : 1 Mo

tailles = {"film.mp4": 700, "photo.jpg": 4, "jeu.iso": 2300, "cv.pdf": 1}
for nom, taille in tailles.items():
    if taille > 100:
        print(nom)


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — Le fichier le plus lourd
# ══════════════════════════════════════════════════════════════════════
#  disque  donne la taille (en Mo) de chaque fichier. Affiche le NOM du
#  fichier le plus lourd. (Avec une boucle : c'est le pattern « champion »
#  du module « Penser comme un dev ».)
#
#  👀 Résultat attendu :
#     jeu.iso

disque = {"film.mp4": 700, "photo.jpg": 4, "jeu.iso": 2300, "cv.pdf": 1}

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — Les téléchargements en double
# ══════════════════════════════════════════════════════════════════════
#  telechargements  contient des fichiers téléchargés plusieurs fois.
#  Affiche combien de fichiers DIFFÉRENTS il y a.
#
#  👀 Résultat attendu :
#     3

telechargements = ["facture.pdf", "photo.jpg", "facture.pdf", "cv.pdf", "photo.jpg"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 3 — Le vote pour le repas d'équipe
# ══════════════════════════════════════════════════════════════════════
#  Chaque élément de  votes  est le choix d'une personne. Construis un
#  dictionnaire {plat: nombre de voix} et affiche-le.
#
#  👀 Résultat attendu :
#     {'pizza': 3, 'sushi': 2, 'tacos': 1}

votes = ["pizza", "sushi", "pizza", "tacos", "pizza", "sushi"]

# ✏️ ton code ici :

