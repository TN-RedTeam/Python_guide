#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 13 : données & rapports

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (3 lignes, lis-les une fois) :
   • Chaque exercice te donne les données de départ — elles sont ÉCRITES,
     tu les VOIS (la liste ventes ci-dessous). Rien n'est caché.
   • Tu écris ton code dans l'espace « ✏️ ton code ici ».
   • Tu lances le fichier, tu regardes ce qui s'affiche, et tu compares
     avec le « 👀 Résultat attendu » écrit au-dessus. C'est tout.
──────────────────────────────────────────────────────────────────────

 Pas de fonction imposée, pas de correction automatique : juste toi, du
 code, et ce qui s'affiche. Ici on manipule des données « à la main »
 (boucles + dict) pour COMPRENDRE ce que pandas fait pour toi plus tard.

 Lancer :   python3 exercices.py
 Le cours est dans README.md ; le corrigé (si bloqué) dans solutions.py.
"""


# Les données de départ : une liste de ventes (chaque vente est un dict).
# Elles sont les mêmes pour tous les exercices. Tu les VOIS, tu peux les changer.
ventes = [
    {"produit": "pomme", "montant": 10},
    {"produit": "pomme", "montant": 5},
    {"produit": "poire", "montant": 3},
]


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Le chiffre d'affaires total
# ══════════════════════════════════════════════════════════════════════
#  Additionne le "montant" de TOUTES les ventes, puis affiche le total.
#  Indice : for vente in ventes:  puis utilise  vente["montant"].
#
#  👀 Résultat attendu :
#     18

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Le total par produit (un « groupby » à la main)
# ══════════════════════════════════════════════════════════════════════
#  Construis un dictionnaire {produit: total des montants} et affiche-le.
#  Indice : pars d'un dict vide  totaux = {}  ; pour chaque vente,
#           totaux[produit] = totaux.get(produit, 0) + montant.
#
#  👀 Résultat attendu :
#     {'pomme': 15, 'poire': 3}

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Les grosses ventes (filtrer au-dessus d'un seuil)
# ══════════════════════════════════════════════════════════════════════
#  seuil vaut 4. Affiche la liste des ventes dont le montant dépasse 4.
#  Indice : une compréhension de liste  [v for v in ventes if ...].
#
#  👀 Résultat attendu (avec seuil = 4) :
#     [{'produit': 'pomme', 'montant': 10}, {'produit': 'pomme', 'montant': 5}]

seuil = 4

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Un mini-rapport lisible
# ══════════════════════════════════════════════════════════════════════
#  À partir du total par produit (exercice 2), affiche une ligne par
#  produit sous la forme  "pomme : 15 €".
#  Indice : parcours un dict avec  for produit, total in totaux.items():
#
#  👀 Résultat attendu :
#     pomme : 15 €
#     poire : 3 €

# ✏️ ton code ici (tu peux recalculer totaux, ou réutiliser l'exercice 2) :


