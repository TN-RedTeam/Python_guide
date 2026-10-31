#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 04 : exceptions & fichiers

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE :
   • Les valeurs de départ sont ÉCRITES et VISIBLES (un nombre, un texte,
     un nom de fichier). Rien n'est caché.
   • Tu écris ton code dans l'espace prévu, puis tu affiches le résultat.
   • Tu lances, tu compares l'affichage au « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 Les exercices sur les fichiers créent un petit fichier dans le dossier
 courant (tu peux le supprimer après). Pas de correction automatique.
 Cours : README.md • Corrigé : solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Division sans planter (try / except)
# ══════════════════════════════════════════════════════════════════════
#  a vaut 10, b vaut 0. Affiche  a / b , mais si b vaut 0, affiche  None
#  au lieu de laisser le programme planter.
#  Indice :   try:  ... a / b ...   except ZeroDivisionError:  ... None
#
#  👀 Résultat attendu (avec b = 0) :
#     None
#  (change b en 2 pour voir 5.0)

a = 10
b = 0

# ✏️ ton code ici (calcule dans un try, affiche le résultat ou None) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Convertir un texte en nombre (sans planter)
# ══════════════════════════════════════════════════════════════════════
#  texte vaut "abc". Essaie de le convertir en entier avec int(texte).
#  Si ça marche, affiche le nombre ; sinon affiche  None.
#  Indice :  int("abc")  lève une  ValueError  → attrape-la.
#
#  👀 Résultat attendu (avec texte = "abc") :
#     None
#  (change texte en "42" pour voir 42)

texte = "abc"

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Écrire puis relire un fichier
# ══════════════════════════════════════════════════════════════════════
#  Écris le texte  contenu  dans le fichier  chemin, puis relis le fichier
#  et affiche ce qu'il contient.
#  Indice :
#     with open(chemin, "w", encoding="utf-8") as f:   # "w" = écrire
#         f.write(contenu)
#     with open(chemin, "r", encoding="utf-8") as f:   # "r" = lire
#         print(f.read())
#
#  👀 Résultat attendu :
#     Salut Python !

chemin = "essai.txt"
contenu = "Salut Python !"

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Lire un fichier qui n'existe peut-être pas
# ══════════════════════════════════════════════════════════════════════
#  Essaie d'ouvrir le fichier  chemin_absent  et d'afficher son nombre de
#  lignes. S'il n'existe pas, affiche  0  (au lieu de planter).
#  Indice :  try: with open(...) as f: print(len(f.readlines()))
#            except FileNotFoundError: print(0)
#
#  👀 Résultat attendu (le fichier n'existe pas) :
#     0

chemin_absent = "ce_fichier_nexiste_pas.txt"

# ✏️ ton code ici :


