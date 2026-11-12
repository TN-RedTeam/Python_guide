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

 La ligne « 🧰 Outils » te dit QUOI utiliser, pas comment l'écrire.

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Lancer :   python3 exercices.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Garder seulement les photos
# ══════════════════════════════════════════════════════════════════════
#  Dans la liste  fichiers, garde seulement ceux qui finissent par ".jpg",
#  et affiche la liste obtenue. Fais-le en UNE ligne.
#  🧰 Outils : une compréhension de liste avec un if, .endswith()
#
#  👀 Résultat attendu :
#     ['vacances.jpg', 'chat.jpg']

fichiers = ["vacances.jpg", "cv.pdf", "chat.jpg", "notes.txt"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Normaliser des noms de fichiers
# ══════════════════════════════════════════════════════════════════════
#  Mets chaque nom de la liste  noms  en minuscules (pour uniformiser),
#  et affiche la liste. En UNE ligne aussi.
#  🧰 Outils : une compréhension de liste, la méthode .lower()
#
#  👀 Résultat attendu :
#     ['rapport.pdf', 'cv.pdf']

noms = ["Rapport.PDF", "CV.Pdf"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Taille totale des gros fichiers
# ══════════════════════════════════════════════════════════════════════
#  tailles  est la taille (en Mo) de plusieurs fichiers. Additionne et
#  affiche uniquement la taille des fichiers de PLUS de 10 Mo, sans
#  construire de liste intermédiaire.
#  🧰 Outils : sum, une expression génératrice avec un if
#
#  👀 Résultat attendu :
#     832

tailles = [120, 4, 700, 12]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Lire les lignes non vides (le défi : un générateur)
# ══════════════════════════════════════════════════════════════════════
#  texte  est le contenu d'un fichier (avec des lignes vides). Écris un
#  GÉNÉRATEUR  lignes_utiles(texte)  qui produit seulement les lignes NON
#  vides, une par une. Puis affiche tout ce qu'il produit, sous forme de
#  liste.
#  🧰 Outils : def avec yield, .splitlines(), .strip(), list()
#
#  👀 Résultat attendu :
#     ['achat lait', 'achat pain']

texte = "achat lait\n\nachat pain\n"

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : la forme est [ce_qu_on_garde for f in fichiers if condition].
#               La condition : f.endswith(".jpg").
#
#  Exercice 2 : pas de if cette fois : on TRANSFORME chaque élément.
#               "Rapport.PDF".lower() renvoie "rapport.pdf".
#
#  Exercice 3 : comme une compréhension, mais directement dans les
#               parenthèses de sum(...) : sum(t for t in ... if ...).
#
#  Exercice 4 : texte.splitlines() découpe le texte en lignes. Dans une
#               boucle for, ligne.strip() est « vrai » seulement si la ligne
#               a du contenu : dans ce cas, yield ligne. Pour tout afficher :
#               print(list(lignes_utiles(texte))).
