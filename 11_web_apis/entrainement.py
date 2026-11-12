#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 11 : web & APIs   (série 2, après exercices.py)

──────────────────────────────────────────────────────────────────────
 Trois façons de travailler la même matière :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier.
   🔧 MODIFIER  : un petit script qui marche déjà. Change-le pour
                 obtenir le nouveau résultat demandé.
   ✍️ ÉCRIRE    : comme dans exercices.py, mais sans indice ni liste
                 d'outils.
──────────────────────────────────────────────────────────────────────

 Comme dans les exercices : pas de vrai appel réseau. Les réponses d'API
 sont fournies en texte, comme si on venait de les recevoir.

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""

import json


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Descendre dans une réponse imbriquée
# ══════════════════════════════════════════════════════════════════════
#  Une API météo renvoie une LISTE de prévisions à l'intérieur d'un
#  dictionnaire. Deux valeurs sont affichées : lesquelles ?
#  ✏️ ma prédiction :

texte = '{"ville": "Lyon", "previsions": [{"jour": "lundi", "temp": 12}, {"jour": "mardi", "temp": 15}]}'
donnees = json.loads(texte)
print("LIRE 1 →", len(donnees["previsions"]), donnees["previsions"][1]["temp"])


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — Seulement les produits disponibles
# ══════════════════════════════════════════════════════════════════════
#  Ce script affiche le nom de tous les produits renvoyés par l'API d'une
#  boutique. Modifie-le pour n'afficher que ceux qui sont EN STOCK (stock
#  supérieur à 0), avec leur prix.
#
#  👀 Résultat attendu APRÈS ta modification :
#     clavier : 30 €
#     écran : 120 €

reponse = {
    "produits": [
        {"nom": "clavier", "prix": 30, "stock": 4},
        {"nom": "souris", "prix": 15, "stock": 0},
        {"nom": "écran", "prix": 120, "stock": 2},
    ]
}
for produit in reponse["produits"]:
    print(produit["nom"])


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — La température moyenne
# ══════════════════════════════════════════════════════════════════════
#  reponse_meteo  est le texte JSON reçu d'une API. Affiche la moyenne
#  des températures ("temp") de tous les relevés.
#
#  👀 Résultat attendu :
#     12.0

reponse_meteo = '{"releves": [{"temp": 10}, {"temp": 14}, {"temp": 12}]}'

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — Préparer ce qu'on ENVOIE à une API
# ══════════════════════════════════════════════════════════════════════
#  Pour passer une commande, l'API attend un texte JSON. Transforme le
#  dictionnaire  commande  en texte JSON et affiche-le.
#  (C'est l'opération inverse de celle des exercices précédents.)
#
#  👀 Résultat attendu :
#     {"produit": "clavier", "quantite": 2}

commande = {"produit": "clavier", "quantite": 2}

# ✏️ ton code ici :

