#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 16 : NumPy

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE :
   • Les données de départ sont ÉCRITES et VISIBLES (des températures,
     des notes, des prix).
   • Tu écris ton code dans « ✏️ ton code ici », puis tu affiches.
   • Tu lances, tu compares l'affichage au « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 La règle du jeu de ce module : AUCUNE boucle for. Avec NumPy, on
 calcule sur le tableau entier d'un coup.

 À savoir : NumPy affiche ses tableaux SANS virgules : [14 17 20].
 C'est normal — c'est sa façon de montrer que ce n'est pas une liste.

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Il te faut NumPy :  pip install numpy   (déjà là si tu as pandas).
 Lancer :   python3 exercices.py
"""

import numpy as np


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Créer un tableau
# ══════════════════════════════════════════════════════════════════════
#  releves  est une liste Python : les températures d'une semaine.
#  Transforme-la en tableau NumPy nommé  temperatures, puis affiche sa
#  forme (shape).
#  🧰 Outils : np.array, .shape
#
#  👀 Résultat attendu :
#     (7,)

releves = [12, 15, 18, 21, 19, 16, 11]

# ✏️ ton code ici (garde le nom  temperatures : les exercices 2 à 4 s'en servent) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Calculer sur tout le tableau d'un coup
# ══════════════════════════════════════════════════════════════════════
#  Le thermomètre était mal réglé : il affichait 2 degrés de moins que la
#  réalité. Affiche les températures corrigées (chacune + 2).
#  🧰 Outils : une opération directement sur le tableau
#
#  👀 Résultat attendu :
#     [14 17 20 23 21 18 13]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Des statistiques en une ligne
# ══════════════════════════════════════════════════════════════════════
#  Affiche la température MOYENNE de la semaine, puis la plus HAUTE.
#  🧰 Outils : les méthodes .mean() et .max()
#
#  👀 Résultat attendu :
#     16.0
#     21

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Filtrer avec un masque
# ══════════════════════════════════════════════════════════════════════
#  Affiche uniquement les températures supérieures à 17 degrés.
#  🧰 Outils : une condition sur le tableau, placée entre crochets
#
#  👀 Résultat attendu :
#     [18 21 19]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — Un tableau à 2 dimensions
# ══════════════════════════════════════════════════════════════════════
#  notes  contient les notes de 2 élèves (une LIGNE par élève) dans 3
#  matières (une COLONNE par matière). C'est exactement la forme d'un jeu
#  de données en IA : une ligne par exemple, une colonne par mesure.
#  Affiche la forme du tableau, puis la moyenne de CHAQUE élève.
#  🧰 Outils : .shape, .mean avec le paramètre axis
#
#  👀 Résultat attendu :
#     (2, 3)
#     [12. 16.]

notes = np.array([[12, 15, 9],
                  [18, 14, 16]])

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 6 — Normaliser entre 0 et 1 (le défi)
# ══════════════════════════════════════════════════════════════════════
#  En IA, on ramène souvent les valeurs entre 0 et 1 avant d'entraîner un
#  modèle. La formule, pour chaque valeur :
#       (valeur - minimum) / (maximum - minimum)
#  Applique-la au tableau  prix  entier (toujours sans boucle) et affiche
#  le résultat.
#  🧰 Outils : .min(), .max(), des opérations sur le tableau
#
#  👀 Résultat attendu (les espaces en trop sont l'affichage normal de NumPy) :
#     [0.   0.25 0.5  0.75 1.  ]

prix = np.array([10, 20, 30, 40, 50])

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : temperatures = np.array(releves). La forme se lit avec
#               temperatures.shape, sans parenthèses.
#
#  Exercice 2 : écris simplement l'addition comme si temperatures était un
#               seul nombre. NumPy l'applique à chaque case.
#
#  Exercice 3 : temperatures.mean() et temperatures.max(), chacun dans son
#               print.
#
#  Exercice 4 : temperatures > 17 donne un tableau de True/False. Mets-le
#               entre les crochets : temperatures[...].
#
#  Exercice 5 : axis=1 calcule le long de chaque LIGNE (donc par élève),
#               axis=0 le long de chaque COLONNE (donc par matière).
#
#  Exercice 6 : traduis la formule mot pour mot, en remplaçant « valeur »
#               par le tableau prix, « minimum » par prix.min() et
#               « maximum » par prix.max(). Attention aux parenthèses.
