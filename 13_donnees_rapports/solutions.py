#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 13 : données & rapports (pandas)

Le corrigé des exercices, avec le code complet et commenté.
Lance-le (python3 solutions.py) pour voir tous les résultats attendus.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""

import pandas as pd

# Le même fichier de départ que dans exercices.py.
CONTENU_CSV = """date,categorie,libelle,montant
2026-01-03,courses,Supermarché,62.5
2026-01-05,transport,Essence,48.0
2026-01-09,loisirs,Cinéma,11.0
2026-01-12,courses,Marché,23.5
2026-01-15,logement,Loyer,750.0
2026-01-20,transport,Train,35.0
2026-01-27,courses,Supermarché,71.0
"""
with open("depenses.csv", "w", encoding="utf-8") as f:
    f.write(CONTENU_CSV)


# ── EXERCICE 1 — Charger le fichier ──────────────────────────────────
df = pd.read_csv("depenses.csv")     # df = DataFrame : le tableau en mémoire
print(df.shape)                      # (7, 4) : 7 lignes, 4 colonnes


# ── EXERCICE 2 — Le total des dépenses ───────────────────────────────
print(df["montant"].sum())           # df["montant"] = la colonne ; .sum() l'additionne


# ── EXERCICE 3 — Les grosses dépenses (filtrer) ──────────────────────
grosses = df[df["montant"] > 50]     # garde les lignes où montant dépasse 50
print(grosses["libelle"].tolist())   # .tolist() : la colonne sous forme de liste Python


# ── EXERCICE 4 — Les 3 plus grosses dépenses (trier) ─────────────────
tri = df.sort_values("montant", ascending=False)   # du plus grand au plus petit
print(tri.head(3)["libelle"].tolist())             # .head(3) : les 3 premières lignes


# ── EXERCICE 5 — Le total par catégorie (groupby) ────────────────────
par_categorie = df.groupby("categorie")["montant"].sum()
print(par_categorie)
# groupby("categorie") rassemble les lignes d'une même catégorie,
# ["montant"].sum() additionne leurs montants. Le résultat est une « Series » :
# une colonne de valeurs avec une étiquette (ici la catégorie) pour chacune.


# ── EXERCICE 6 — Exporter le rapport, puis le relire ─────────────────
par_categorie.to_csv("rapport_depenses.csv")       # écrit le rapport sur le disque
with open("rapport_depenses.csv", "r", encoding="utf-8") as f:
    print(f.read())
# C'est le pipeline complet : charger -> calculer -> exporter.
