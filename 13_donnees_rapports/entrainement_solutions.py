#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 13 : données & rapports (pandas)

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit ta prédiction et essayé.
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


# ── 👓 LIRE 1 — Filtrer, puis compter ────────────────────────────────
grands = df[df["surface"] >= 50]
print("LIRE 1 →", len(df), len(grands), grands["ville"].tolist())
# Réponse : 6 3 ['Lyon', 'Paris', 'Lille'].
#   len(df) = 6 lignes de données (la ligne d'en-tête ne compte pas).
#   Surfaces : 30, 25, 60, 45, 50, 70 -> celles >= 50 sont 60, 50 et 70 :
#   3 lignes, dans l'ordre du fichier : Lyon, Paris, Lille.
#   Le filtre ne modifie pas df : il fabrique un NOUVEAU tableau, plus petit.


# ── 🔧 MODIFIER 1 — Du total à la moyenne ────────────────────────────
print(df.groupby("ville")["loyer"].mean())      # .mean() à la place de .sum()
# Le regroupement est le même ; seul le calcul appliqué à chaque groupe change.
# On peut aussi mettre .max(), .min(), .count()…


# ── ✍️ ÉCRIRE 1 — Les deux logements les moins chers ─────────────────
print(df["loyer"].min())
moins_chers = df.sort_values("loyer").head(2)   # tri croissant, puis les 2 premières lignes
print(moins_chers["ville"].tolist())


# ── ✍️ ÉCRIRE 2 — Créer une nouvelle colonne ─────────────────────────
df["loyer_annuel"] = df["loyer"] * 12           # le calcul s'applique à toute la colonne
print(df["loyer_annuel"].tolist())
# Écrire dans df["nom_inexistant"] CRÉE la colonne (comme pour une clé de dictionnaire).
