#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 11 : web & APIs

Le corrigé des exercices de exercices.py, code complet et commenté.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.

Lance-le (python3 solutions.py) : il affiche les résultats attendus.
"""

import json


# ── EXERCICE 1 — Lire une réponse JSON (texte → dict) ────────────────
reponse_texte = '{"ville": "Paris", "temperature": 18}'
donnees = json.loads(reponse_texte)    # texte JSON → dict Python
print(donnees["temperature"])          # 18
# Dans la vraie vie :
#   import requests
#   reponse = requests.get("https://.../meteo")
#   donnees = reponse.json()            # requests fait le json.loads pour toi


# ── EXERCICE 2 — Extraire une liste de champs ────────────────────────
reponse = {"results": [{"name": "Ada"}, {"name": "Bob"}]}
print([item["name"] for item in reponse["results"]])


# ── EXERCICE 3 — Vérifier un code HTTP ───────────────────────────────
code = 404
if 200 <= code <= 299:        # la famille 2xx = succès
    print("OK")
else:
    print("Erreur")


# ── EXERCICE 4 — Parser une réponse complète ─────────────────────────
reponse_texte_2 = '{"count": 2, "results": [{"name": "pikachu"}, {"name": "bulbasaur"}]}'
donnees2 = json.loads(reponse_texte_2)
print(donnees2["count"])
print([item["name"] for item in donnees2["results"]])
