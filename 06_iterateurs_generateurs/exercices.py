#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 06 : itérateurs & générateurs

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE :
   • Les données de départ sont ÉCRITES et VISIBLES (des fichiers, des
     tailles, du texte). Tu écris ton code, puis tu affiches le résultat.
   • Tu lances, tu compares l'affichage au « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 Pas de correction automatique. Cours : README.md • Corrigé : solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Garder seulement les photos (compréhension + filtre)
# ══════════════════════════════════════════════════════════════════════
#  Dans la liste  fichiers, garde seulement ceux qui finissent par ".jpg",
#  et affiche la liste obtenue.
#  Indice (compréhension de liste) :  [f for f in fichiers if f.endswith(".jpg")]
#
#  👀 Résultat attendu :
#     ['vacances.jpg', 'chat.jpg']

fichiers = ["vacances.jpg", "cv.pdf", "chat.jpg", "notes.txt"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Normaliser des noms de fichiers (compréhension + transfo)
# ══════════════════════════════════════════════════════════════════════
#  Mets chaque nom de la liste  noms  en minuscules (pour uniformiser),
#  et affiche la liste.
#  Indice :  "Rapport.PDF".lower()  ->  "rapport.pdf"  ;  [x.lower() for x in noms]
#
#  👀 Résultat attendu :
#     ['rapport.pdf', 'cv.pdf']

noms = ["Rapport.PDF", "CV.Pdf"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Taille totale des gros fichiers (expression génératrice)
# ══════════════════════════════════════════════════════════════════════
#  tailles  est la taille (en Mo) de plusieurs fichiers. Additionne et
#  affiche uniquement la taille des fichiers de PLUS de 10 Mo.
#  Indice :  sum(t for t in tailles if t > 10)   (on additionne au vol, sans
#            créer de liste intermédiaire)
#
#  👀 Résultat attendu :
#     832

tailles = [120, 4, 700, 12]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Lire les lignes non vides (écrire un générateur) — défi
# ══════════════════════════════════════════════════════════════════════
#  texte  est le contenu d'un fichier (avec des lignes vides). Écris un
#  GÉNÉRATEUR  lignes_utiles(texte)  qui PRODUIT (yield) seulement les lignes
#  NON vides, une par une.
#  Indice :
#     def lignes_utiles(texte):
#         for ligne in texte.splitlines():   # découpe le texte en lignes
#             if ligne.strip():              # vraie seulement si la ligne a du contenu
#                 yield ligne
#  Puis appelle-le et affiche la liste :  print(list(lignes_utiles(texte)))
#
#  👀 Résultat attendu :
#     ['achat lait', 'achat pain']

texte = "achat lait\n\nachat pain\n"

# ✏️ ton code ici (le générateur, puis le print) :


