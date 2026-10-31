#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 06 : itérateurs & générateurs

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE :
   • Les données de départ sont ÉCRITES et VISIBLES (une liste, un nombre).
   • Tu écris ton code dans l'espace prévu, puis tu affiches le résultat.
   • Tu lances, tu compares l'affichage au « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 Pas de correction automatique. Cours : README.md • Corrigé : solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Filtrer une liste (compréhension)
# ══════════════════════════════════════════════════════════════════════
#  Dans la liste  nombres, garde seulement les nombres > 0, et affiche la
#  liste obtenue.
#  Indice (compréhension de liste) :  [n for n in nombres if n > 0]
#
#  👀 Résultat attendu :
#     [3, 7]

nombres = [3, -1, 0, 7, -2]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Transformer une liste (compréhension)
# ══════════════════════════════════════════════════════════════════════
#  Mets chaque nom de la liste  noms  en MAJUSCULES, et affiche la liste.
#  Indice :  "ada".upper()  ->  "ADA"  ;  en compréhension : [x.upper() for x in noms]
#
#  👀 Résultat attendu :
#     ['ADA', 'BOB']

noms = ["ada", "bob"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Additionner au vol (expression génératrice)
# ══════════════════════════════════════════════════════════════════════
#  n vaut 4. Calcule et affiche la somme des carrés de 0 à n-1 :
#  0² + 1² + 2² + 3²  (= 0 + 1 + 4 + 9).
#  Indice :  sum(i ** 2 for i in range(n))   (pas de liste créée, on additionne au vol)
#
#  👀 Résultat attendu :
#     14

n = 4

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Écrire un générateur (yield) — le défi
# ══════════════════════════════════════════════════════════════════════
#  Écris un GÉNÉRATEUR  pairs_jusqua(limite)  qui PRODUIT (yield) les
#  nombres pairs de 0 jusqu'à limite (exclu), un par un.
#  Indice :
#     def pairs_jusqua(limite):
#         n = 0
#         while n < limite:
#             yield n          # livre n, puis se met en pause
#             n += 2
#  Puis appelle-le et affiche la liste :  print(list(pairs_jusqua(10)))
#  (list(...) déroule le générateur pour tout voir d'un coup)
#
#  👀 Résultat attendu :
#     [0, 2, 4, 6, 8]

# ✏️ ton code ici (le générateur, puis le print) :


