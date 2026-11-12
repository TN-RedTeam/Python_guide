#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DÉFI 2 — L'inventaire d'un disque
(à faire après les modules 05 à 07)

──────────────────────────────────────────────────────────────────────
 LE PROJET
 Ton disque est plein et tu veux savoir ce qui prend de la place. Tu
 vas modéliser tes fichiers avec deux classes : Fichier (un fichier) et
 Inventaire (la collection de fichiers, qui sait répondre à tes
 questions : combien ? quel poids ? lesquels sont énormes ?).

 CE QUE TU RÉUTILISES
   module 02 : listes, dictionnaires
   module 05 : classes, __init__, self, méthodes
   module 06 : compréhension de liste, générateur (yield)
   « Penser comme un dev » : le pattern champion
──────────────────────────────────────────────────────────────────────

 COMMENT AVANCER
   • Les étapes 2 à 6 ajoutent chacune une méthode à la MÊME classe
     Inventaire : tu fais grandir ta classe petit à petit, comme dans
     un vrai projet.
   • Lance le fichier après chaque étape et compare au résultat attendu.

 Lancer :   python3 defi_2_inventaire.py
 Corrigé :  defi_2_inventaire_solution.py  (après avoir essayé !)
"""

# Les données de départ : des couples (nom du fichier, taille en Mo).
DONNEES = [
    ("film.mp4", 700),
    ("photo.jpg", 4),
    ("cv.pdf", 1),
    ("vacances.jpg", 6),
    ("jeu.iso", 2300),
    ("notes.txt", 1),
]


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 1 — La classe Fichier
# ══════════════════════════════════════════════════════════════════════
#  Écris une classe  Fichier  (nom, taille en Mo) avec une méthode
#  extension()  qui renvoie l'extension du fichier, point compris.
#  Affiche l'extension du fichier "film.mp4" de 700 Mo.
#  🧰 Outils : class, __init__, .split("."), l'index [-1]
#
#  👀 Résultat attendu :
#     .mp4

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 2 — La classe Inventaire
# ══════════════════════════════════════════════════════════════════════
#  Écris une classe  Inventaire  qui démarre VIDE, avec :
#    - ajouter(fichier)  : range un objet Fichier dans l'inventaire ;
#    - nombre()          : le nombre de fichiers ;
#    - taille_totale()   : la somme des tailles, en Mo.
#  Crée un inventaire et remplis-le avec un Fichier pour chaque couple
#  de DONNEES, puis affiche le bilan.
#
#  👀 Résultat attendu :
#     6 fichiers, 3012 Mo

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 3 — Le plus gros fichier
# ══════════════════════════════════════════════════════════════════════
#  Ajoute à Inventaire une méthode  plus_gros()  qui renvoie le Fichier
#  (l'objet) le plus lourd. Affiche son nom.
#
#  👀 Résultat attendu :
#     jeu.iso

# ✏️ ton code ici (complète la classe au-dessus, puis affiche ici) :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 4 — Les fichiers d'un certain type
# ══════════════════════════════════════════════════════════════════════
#  Ajoute une méthode  par_extension(extension)  qui renvoie la liste des
#  NOMS des fichiers ayant cette extension. Écris-la en une compréhension.
#  Affiche les fichiers ".jpg".
#
#  👀 Résultat attendu :
#     ['photo.jpg', 'vacances.jpg']

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 5 — Parcourir les gros fichiers
# ══════════════════════════════════════════════════════════════════════
#  Ajoute une méthode  gros_fichiers(seuil)  qui est un GÉNÉRATEUR : elle
#  produit, un par un, les fichiers de plus de  seuil  Mo.
#  Parcours les fichiers de plus de 100 Mo et affiche chacun.
#
#  👀 Résultat attendu :
#     film.mp4 (700 Mo)
#     jeu.iso (2300 Mo)

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 6 — Le poids de chaque type de fichier
# ══════════════════════════════════════════════════════════════════════
#  Ajoute une méthode  bilan_par_type()  qui renvoie un dictionnaire
#  {extension: poids total en Mo}. Affiche-le.
#
#  👀 Résultat attendu :
#     {'.mp4': 700, '.jpg': 10, '.pdf': 1, '.iso': 2300, '.txt': 1}

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  🚀 POUR ALLER PLUS LOIN (sans corrigé : c'est ton projet maintenant)
# ══════════════════════════════════════════════════════════════════════
#   • Ajoute une méthode supprimer(nom) et vérifie que le total baisse.
#   • Ajoute une méthode __str__ à Fichier pour que print(fichier)
#     affiche directement « film.mp4 (700 Mo) ».
#   • Après le module 10 : remplis l'inventaire avec les VRAIS fichiers
#     d'un dossier de ton PC (iterdir, .name, .stat().st_size).
