#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 02 : les collections (listes, dictionnaires, sets)

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (lis-les une fois) :
   • Chaque exercice part de données CONCRÈTES et VISIBLES — ici, des
     fichiers de ton ordinateur (noms, tailles, extensions).
   • Tu écris ton code dans l'espace « ✏️ ton code ici », puis print.
   • Tu lances, tu compares l'affichage au « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 Les données sont écrites ici en dur pour que ce soit simple à tester.
 Les notes « 💡 Sur ton PC » montrent comment faire pareil pour de vrai
 (tu le feras au module 10 « fichiers & dossiers »).

 Lancer :   python3 exercices.py
 Cours : README.md   •   Corrigé (si bloqué) : solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Le 2e fichier de la liste
# ══════════════════════════════════════════════════════════════════════
#  fichiers  est la liste des fichiers d'un dossier. Affiche le DEUXIÈME.
#  Rappel : les positions commencent à 0 (donc le 2e est à l'index 1).
#
#  💡 Sur ton PC : cette liste, c'est ce que renvoie os.listdir("mon_dossier").
#
#  👀 Résultat attendu :
#     photo.jpg

fichiers = ["rapport.pdf", "photo.jpg", "notes.txt"]

# ✏️ ton code ici (affiche fichiers[?]) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — La taille totale du dossier
# ══════════════════════════════════════════════════════════════════════
#  tailles_mo  donne la taille (en Mo) de chaque fichier. Affiche la
#  taille TOTALE du dossier (la somme de toutes les tailles).
#  Indice :  tailles_mo.values()  donne les tailles  →  sum(...) les additionne.
#
#  👀 Résultat attendu :
#     705

tailles_mo = {"film.mp4": 700, "photo.jpg": 4, "cv.pdf": 1}

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Compter les photos (.jpg)
# ══════════════════════════════════════════════════════════════════════
#  Dans la liste  fichiers, compte combien se terminent par ".jpg",
#  et affiche ce nombre.
#  Indice :  "photo.jpg".endswith(".jpg")  vaut True. Pars d'un compteur à 0,
#            parcours la liste, et +1 à chaque fichier qui finit par ".jpg".
#
#  👀 Résultat attendu :
#     3

fichiers = ["vacances.jpg", "cv.pdf", "chat.jpg", "notes.txt", "profil.jpg"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Trouver les fichiers vides
# ══════════════════════════════════════════════════════════════════════
#  tailles  donne la taille (en octets) de chaque fichier. Affiche le nom
#  de chaque fichier VIDE (taille 0) — pratique pour faire le ménage.
#  Indice :  for nom, taille in tailles.items():   puis un if.
#
#  👀 Résultat attendu (une ligne par fichier vide) :
#     vide.txt
#     temp.log

tailles = {"notes.txt": 12, "vide.txt": 0, "temp.log": 0}

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — La liste des types de fichiers présents
# ══════════════════════════════════════════════════════════════════════
#  extensions  contient l'extension de chaque fichier (avec des répétitions).
#  Affiche la liste des extensions DISTINCTES, triées par ordre alphabétique.
#  Indice :  set(...) enlève les doublons,  sorted(...) trie et renvoie une liste.
#
#  👀 Résultat attendu :
#     ['.jpg', '.pdf', '.txt']

extensions = [".jpg", ".txt", ".jpg", ".pdf", ".txt"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 6 — Combien de fichiers par type ? (le défi)
# ══════════════════════════════════════════════════════════════════════
#  À partir de  extensions, construis un dictionnaire qui dit combien de
#  fichiers il y a de chaque type, puis affiche-le.
#  Indice : pars d'un dict vide, et pour chaque extension :
#           compteur[ext] = compteur.get(ext, 0) + 1
#           (.get(ext, 0) renvoie le compte actuel, ou 0 si c'est un nouveau type)
#
#  👀 Résultat attendu :
#     {'.jpg': 2, '.txt': 1}

extensions = [".jpg", ".txt", ".jpg"]

# ✏️ ton code ici :


