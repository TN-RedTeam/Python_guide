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

 La ligne « 🧰 Outils » te dit QUOI utiliser, pas comment l'écrire.

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Les données sont écrites ici en dur pour que ce soit simple à tester.
 💡 Sur ton PC : tu obtiendras ces mêmes listes pour de vrai au module 10
    (os.listdir("mon_dossier") renvoie la liste des fichiers d'un dossier).

 Lancer :   python3 exercices.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Le 2e fichier de la liste
# ══════════════════════════════════════════════════════════════════════
#  fichiers  est la liste des fichiers d'un dossier. Affiche le DEUXIÈME.
#  🧰 Outils : l'accès par index  liste[...]
#
#  👀 Résultat attendu :
#     photo.jpg

fichiers = ["rapport.pdf", "photo.jpg", "notes.txt"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — La taille totale du dossier
# ══════════════════════════════════════════════════════════════════════
#  tailles_mo  donne la taille (en Mo) de chaque fichier. Affiche la
#  taille TOTALE du dossier (la somme de toutes les tailles).
#  🧰 Outils : les valeurs d'un dictionnaire, sum
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
#  🧰 Outils : une boucle for, un compteur, la méthode .endswith()
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
#  🧰 Outils : parcourir un dictionnaire avec .items(), if
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
#  🧰 Outils : set, sorted
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
#  🧰 Outils : un dictionnaire vide, une boucle for, la méthode .get()
#
#  👀 Résultat attendu :
#     {'.jpg': 2, '.txt': 1}

extensions = [".jpg", ".txt", ".jpg"]

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : les positions commencent à 0. Le 1er élément est à l'index 0,
#               donc le 2e est à l'index…
#
#  Exercice 2 : tailles_mo.values() donne toutes les tailles ; sum(...) sait
#               additionner une série de nombres.
#
#  Exercice 3 : "photo.jpg".endswith(".jpg") vaut True. Pars d'un compteur
#               à 0 AVANT la boucle, et ajoute 1 à chaque nom qui passe le test.
#
#  Exercice 4 : for nom, taille in tailles.items(): te donne les deux à la
#               fois. Il reste à tester la taille et à afficher le nom.
#
#  Exercice 5 : set(...) enlève les doublons (mais sans ordre) ; sorted(...)
#               trie et renvoie une liste. Enchaîne les deux.
#
#  Exercice 6 : pour chaque extension, il faut « l'ancien compte + 1 ».
#               compteur.get(ext, 0) renvoie le compte actuel, ou 0 si
#               l'extension n'est pas encore dans le dictionnaire.
