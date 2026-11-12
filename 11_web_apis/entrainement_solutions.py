#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 11 : web & APIs

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit ta prédiction et essayé.
"""

import json


# ── 👓 LIRE 1 — Descendre dans une réponse imbriquée ─────────────────
texte = '{"ville": "Lyon", "previsions": [{"jour": "lundi", "temp": 12}, {"jour": "mardi", "temp": 15}]}'
donnees = json.loads(texte)
print("LIRE 1 →", len(donnees["previsions"]), donnees["previsions"][1]["temp"])
# Réponse : 2 15. On descend un étage à la fois :
#   donnees["previsions"]            -> une LISTE de 2 dictionnaires
#   donnees["previsions"][1]         -> le 2e dictionnaire (index 1) : mardi
#   donnees["previsions"][1]["temp"] -> sa température : 15
# Crochets avec un texte = clé de dictionnaire ; avec un nombre = index de liste.


# ── 🔧 MODIFIER 1 — Seulement les produits disponibles ───────────────
reponse = {
    "produits": [
        {"nom": "clavier", "prix": 30, "stock": 4},
        {"nom": "souris", "prix": 15, "stock": 0},
        {"nom": "écran", "prix": 120, "stock": 2},
    ]
}
for produit in reponse["produits"]:
    if produit["stock"] > 0:
        print(f"{produit['nom']} : {produit['prix']} €")
        # dans une f-string entre guillemets doubles, les clés s'écrivent avec des apostrophes


# ── ✍️ ÉCRIRE 1 — La température moyenne ─────────────────────────────
reponse_meteo = '{"releves": [{"temp": 10}, {"temp": 14}, {"temp": 12}]}'
releves = json.loads(reponse_meteo)["releves"]          # la liste des relevés
temperatures = [releve["temp"] for releve in releves]   # [10, 14, 12]
print(sum(temperatures) / len(temperatures))


# ── ✍️ ÉCRIRE 2 — Préparer ce qu'on ENVOIE à une API ─────────────────
commande = {"produit": "clavier", "quantite": 2}
print(json.dumps(commande))     # dumps : dictionnaire -> texte JSON (l'inverse de loads)
# Dans la vraie vie :  requests.post(url, json=commande)  fait cette conversion pour toi.
