#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 13 : données & rapports (pandas)   (série 2)

──────────────────────────────────────────────────────────────────────
 Trois façons de travailler la même matière :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier.
   🔧 MODIFIER  : un petit script qui marche déjà. Change-le pour
                 obtenir le nouveau résultat demandé.
   ✍️ ÉCRIRE    : comme dans exercices.py, mais sans indice ni liste
                 d'outils.
──────────────────────────────────────────────────────────────────────

 Nouveau jeu de données : logements.csv, des annonces de location (une
 ligne par logement). C'est le genre de tableau qu'on donne à un modèle
 pour lui apprendre à estimer un loyer.

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""

import pandas as pd

CONTENU_CSV = """ville,surface,pieces,loyer
Lyon,30,1,650
Paris,25,1,950
Lyon,60,3,1100
Lille,45,2,620
Paris,50,2,1500
Lille,70,3,900
"""
with open("logements.csv", "w", encoding="utf-8") as f:
    f.write(CONTENU_CSV)

df = pd.read_csv("logements.csv")


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Filtrer, puis compter
# ══════════════════════════════════════════════════════════════════════
#  Trois valeurs sont affichées : le nombre de logements, le nombre de
#  « grands » logements, et la liste des villes de ces grands logements.
#  (Regarde le fichier ci-dessus et fais le filtre à la main.)
#  ✏️ ma prédiction :

grands = df[df["surface"] >= 50]
print("LIRE 1 →", len(df), len(grands), grands["ville"].tolist())


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — Du total à la moyenne
# ══════════════════════════════════════════════════════════════════════
#  Ce script affiche le TOTAL des loyers par ville, ce qui ne veut pas
#  dire grand-chose. Modifie-le pour afficher le loyer MOYEN par ville.
#
#  👀 Résultat attendu APRÈS ta modification :
#     ville
#     Lille     760.0
#     Lyon      875.0
#     Paris    1225.0
#     Name: loyer, dtype: float64

print(df.groupby("ville")["loyer"].sum())


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — Les deux logements les moins chers
# ══════════════════════════════════════════════════════════════════════
#  Affiche le loyer le plus bas du tableau, puis la liste des villes des
#  DEUX logements les moins chers (du moins cher au plus cher).
#
#  👀 Résultat attendu :
#     620
#     ['Lille', 'Lyon']

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — Créer une nouvelle colonne
# ══════════════════════════════════════════════════════════════════════
#  Ajoute au tableau une colonne "loyer_annuel" (le loyer × 12), puis
#  affiche cette colonne sous forme de liste.
#  (Fabriquer une colonne à partir d'autres colonnes : en IA, ça s'appelle
#  créer une « feature ».)
#
#  👀 Résultat attendu :
#     [7800, 11400, 13200, 7440, 18000, 10800]

# ✏️ ton code ici :

