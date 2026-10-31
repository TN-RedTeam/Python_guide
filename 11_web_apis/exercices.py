#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 11 : web & APIs

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (lis-les une fois) :
   • Les valeurs de départ (réponses d'API) sont ÉCRITES, tu les VOIS.
   • Tu écris ton code dans l'espace « ✏️ ton code ici ».
   • Tu lances, tu regardes l'affichage, tu compares au « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 Important : ici on NE fait PAS de vrai appel réseau. On s'entraîne sur des
 réponses d'API fournies en texte (comme si on venait de les recevoir). Le
 vrai appel avec requests est montré en commentaire.

 Lancer :   python3 exercices.py
 Cours dans README.md ; corrigé dans solutions.py.
"""

import json


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Lire une réponse JSON (texte → dict)
# ══════════════════════════════════════════════════════════════════════
#  Une API a renvoyé le texte JSON ci-dessous (reponse_texte).
#  Transforme-le en dictionnaire avec json.loads, puis affiche la température.
#  Indice : donnees = json.loads(reponse_texte)   puis   donnees["temperature"]
#
#  (Dans la vraie vie :  reponse = requests.get(url) ; donnees = reponse.json())
#
#  👀 Résultat attendu :
#     18

reponse_texte = '{"ville": "Paris", "temperature": 18}'

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Extraire une liste de champs
# ══════════════════════════════════════════════════════════════════════
#  La réponse (déjà en dictionnaire) contient une liste "results".
#  Affiche la liste des "name" de chaque résultat.
#  Indice : [item["name"] for item in reponse["results"]]
#
#  👀 Résultat attendu :
#     ['Ada', 'Bob']

reponse = {"results": [{"name": "Ada"}, {"name": "Bob"}]}

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Vérifier un code HTTP
# ══════════════════════════════════════════════════════════════════════
#  Un appel a renvoyé le code ci-dessous.
#  Affiche "OK" si le code est un succès (entre 200 et 299), sinon "Erreur".
#
#  👀 Résultat attendu (avec code = 404) :
#     Erreur
#  (change code en 200 pour voir OK)

code = 404

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Parser une réponse complète
# ══════════════════════════════════════════════════════════════════════
#  Voici la réponse JSON d'une API (en texte).
#  Transforme-la en dict, puis affiche le nombre total (clé "count") PUIS
#  la liste des noms.
#
#  👀 Résultat attendu :
#     2
#     ['pikachu', 'bulbasaur']

reponse_texte_2 = '{"count": 2, "results": [{"name": "pikachu"}, {"name": "bulbasaur"}]}'

# ✏️ ton code ici :


