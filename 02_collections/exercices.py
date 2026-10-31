#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 02 : les collections (listes, dictionnaires, sets)

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (lis-les une fois) :
   • Chaque exercice te donne les données de départ — elles sont ÉCRITES,
     tu les VOIS (une liste, un dict…). Rien n'est caché.
   • Tu écris ton code dans l'espace « ✏️ ton code ici », puis print.
   • Tu lances le fichier, tu regardes ce qui s'affiche, et tu compares
     avec le « 👀 Résultat attendu » écrit au-dessus. C'est tout.
──────────────────────────────────────────────────────────────────────

 Pas de fonction, pas de correction automatique. Tu peux changer les
 données de départ pour tester toi-même.

 Lancer :   python3 exercices.py
 Cours : README.md   •   Corrigé (si bloqué) : solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Lire un élément d'une liste
# ══════════════════════════════════════════════════════════════════════
#  La liste  fruits  contient 3 fruits. Affiche le DEUXIÈME.
#  Rappel : les positions commencent à 0 (donc le 2e est à l'index 1).
#
#  👀 Résultat attendu :
#     banane

fruits = ["pomme", "banane", "cerise"]

# ✏️ ton code ici (affiche fruits[?]) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Le total d'un panier (dictionnaire)
# ══════════════════════════════════════════════════════════════════════
#  Le dict  panier  associe chaque produit à son prix.
#  Affiche la somme de tous les prix.
#  Indice :  panier.values()  donne tous les prix  →  sum(...) les additionne.
#
#  👀 Résultat attendu :
#     2.0

panier = {"pain": 1.2, "lait": 0.8}

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Compter dans une liste
# ══════════════════════════════════════════════════════════════════════
#  Dans la liste  notes, compte combien de fois apparaît la note 2,
#  et affiche ce nombre.
#  Indice : pars d'un compteur à 0, parcours la liste avec un for,
#           et à chaque fois que l'élément vaut 2, ajoute 1.
#
#  👀 Résultat attendu :
#     3

notes = [1, 2, 2, 3, 2]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Les produits en rupture (parcourir un dict)
# ══════════════════════════════════════════════════════════════════════
#  Le dict  stock  associe chaque produit à sa quantité.
#  Affiche le nom de chaque produit dont la quantité vaut 0.
#  Indice :  for produit, quantite in stock.items():   puis un if.
#
#  👀 Résultat attendu (une ligne par produit en rupture) :
#     poires
#     kiwis

stock = {"pommes": 5, "poires": 0, "kiwis": 0}

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — Enlever les doublons et trier
# ══════════════════════════════════════════════════════════════════════
#  La liste  valeurs  contient des doublons. Affiche la liste des valeurs
#  DISTINCTES, triées dans l'ordre croissant.
#  Indice :  set(...) enlève les doublons,  sorted(...) trie et renvoie une liste.
#
#  👀 Résultat attendu :
#     [1, 2, 3]

valeurs = [3, 1, 2, 3, 1]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 6 — Compter chaque mot (le défi)
# ══════════════════════════════════════════════════════════════════════
#  La liste  mots  contient des mots répétés. Construis un dictionnaire
#  qui dit combien de fois chaque mot apparaît, puis affiche-le.
#  Indice : pars d'un dict vide, et pour chaque mot :
#           compteur[mot] = compteur.get(mot, 0) + 1
#           (.get(mot, 0) renvoie le compte actuel, ou 0 si le mot est nouveau)
#
#  👀 Résultat attendu :
#     {'a': 2, 'b': 1}

mots = ["a", "b", "a"]

# ✏️ ton code ici :


