#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Défi 5 : un tableau de bord avec pandas et NumPy

Une solution possible. La tienne peut être différente et tout aussi juste.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé.
"""

import numpy as np
import pandas as pd

CONTENU = """mois,categorie,libelle,montant
janvier,courses,Supermarché,62
janvier,transport,Essence,48
janvier,loisirs,Cinéma,11
janvier,logement,Loyer,750
janvier,courses,Marché,24
février,courses,Supermarché,71
février,transport,Train,35
février,loisirs,Concert,45
février,logement,Loyer,750
février,courses,Boulangerie,9
"""
with open("depenses_2mois.csv", "w", encoding="utf-8") as f:
    f.write(CONTENU)


# ── ÉTAPE 1 — Charger et découvrir ───────────────────────────────────
df = pd.read_csv("depenses_2mois.csv")
print(df.shape)                     # (lignes, colonnes)
print(df.columns.tolist())          # les noms des colonnes, en liste


# ── ÉTAPE 2 — Le total par mois ──────────────────────────────────────
print(df.groupby("mois")["montant"].sum())
# groupby classe les groupes par ordre alphabétique : « février » avant « janvier ».


# ── ÉTAPE 3 — Le classement des catégories ───────────────────────────
par_categorie = df.groupby("categorie")["montant"].sum().sort_values(ascending=False)
print(par_categorie)
# On enchaîne : regrouper -> additionner -> trier du plus grand au plus petit.


# ── ÉTAPE 4 — La part de chaque catégorie (NumPy) ────────────────────
valeurs = par_categorie.to_numpy()              # la colonne de totaux, en tableau NumPy
parts = valeurs / valeurs.sum() * 100           # chaque total divisé par le total général
print(np.round(parts, 1))                       # arrondi à 1 chiffre après la virgule
# Même ordre que par_categorie : logement, courses, transport, loisirs.


# ── ÉTAPE 5 — Les dépenses au-dessus de la moyenne ───────────────────
hors_logement = df[df["categorie"] != "logement"]       # le loyer écraserait la moyenne
moyenne = hors_logement["montant"].mean()               # 38.125
au_dessus = hors_logement[hors_logement["montant"] > moyenne]
print(au_dessus["libelle"].tolist())


# ── ÉTAPE 6 — Exporter le tableau de bord ────────────────────────────
par_categorie.to_csv("tableau_de_bord.csv")
with open("tableau_de_bord.csv", "r", encoding="utf-8") as f:
    print(f.read().strip())

# Ce qu'il faut remarquer : c'est le pipeline du module 13 — charger, calculer,
# présenter — avec NumPy pour le calcul des parts. Et l'étape 5 montre un vrai
# réflexe d'analyse : une moyenne se laisse fausser par une valeur énorme (le
# loyer). Avant de calculer, demande-toi toujours « sur quelles lignes ? ».
