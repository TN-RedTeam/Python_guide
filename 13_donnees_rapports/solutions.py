#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 13 : données & rapports

Le corrigé des exercices, en code complet et commenté.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.

Lance-le (python3 solutions.py) : il affiche les résultats attendus.
En pandas, on écrirait ça en une ligne (voir les commentaires) ; ici on le
fait à la main pour COMPRENDRE ce que pandas fait pour toi.
"""

ventes = [
    {"produit": "pomme", "montant": 10},
    {"produit": "pomme", "montant": 5},
    {"produit": "poire", "montant": 3},
]


# ── EXERCICE 1 — Chiffre d'affaires total ────────────────────────────
total = 0
for vente in ventes:
    total = total + vente["montant"]
print(total)                      # 18
# En pandas :  df["montant"].sum()


# ── EXERCICE 2 — Total par produit (groupby manuel) ──────────────────
totaux = {}
for vente in ventes:
    produit = vente["produit"]
    totaux[produit] = totaux.get(produit, 0) + vente["montant"]
print(totaux)                     # {'pomme': 15, 'poire': 3}
# .get(produit, 0) = le total actuel, ou 0 si le produit est nouveau.
# En pandas :  df.groupby("produit")["montant"].sum()


# ── EXERCICE 3 — Grosses ventes (filtre) ─────────────────────────────
seuil = 4
grosses = [v for v in ventes if v["montant"] > seuil]
print(grosses)                    # [{'produit': 'pomme', 'montant': 10}, {'produit': 'pomme', 'montant': 5}]
# En pandas :  df[df["montant"] > seuil]


# ── EXERCICE 4 — Mini-rapport lisible ────────────────────────────────
for produit, montant in totaux.items():   # on réutilise totaux de l'exercice 2
    print(f"{produit} : {montant} €")
# pomme : 15 €
# poire : 3 €
