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
 réponses d'API fournies en texte (comme si on venait de les recevoir).
 Dans la vraie vie, ces réponses viennent de :
     reponse = requests.get(url)   puis   donnees = reponse.json()

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Lancer :   python3 exercices.py
"""

import json


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Lire une réponse JSON (texte → dictionnaire)
# ══════════════════════════════════════════════════════════════════════
#  Une API météo a renvoyé le texte JSON  reponse_texte.
#  Transforme-le en dictionnaire, puis affiche la température.
#  🧰 Outils : json.loads, l'accès par clé d'un dictionnaire
#
#  👀 Résultat attendu :
#     18

reponse_texte = '{"ville": "Paris", "temperature": 18}'

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Extraire une liste de champs
# ══════════════════════════════════════════════════════════════════════
#  reponse  (déjà en dictionnaire) contient une liste "results".
#  Affiche la liste des "name" de chaque résultat.
#  🧰 Outils : l'accès par clé, une boucle for ou une compréhension de liste
#
#  👀 Résultat attendu :
#     ['Ada', 'Bob']

reponse = {"results": [{"name": "Ada"}, {"name": "Bob"}]}

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Vérifier un code HTTP
# ══════════════════════════════════════════════════════════════════════
#  Un appel a renvoyé le code  code. Affiche "OK" si c'est un succès
#  (entre 200 et 299 inclus), sinon "Erreur".
#  🧰 Outils : if / else, une comparaison
#
#  👀 Résultat attendu (avec code = 404) :
#     Erreur
#  (change code en 200 pour voir OK)

code = 404

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Parser une réponse complète (le défi)
# ══════════════════════════════════════════════════════════════════════
#  Voici la réponse JSON d'une API (en texte). Transforme-la en
#  dictionnaire, puis affiche le nombre total (clé "count") PUIS la
#  liste des noms.
#  🧰 Outils : tout ce que tu as utilisé aux exercices 1 et 2
#
#  👀 Résultat attendu :
#     2
#     ['pikachu', 'bulbasaur']

reponse_texte_2 = '{"count": 2, "results": [{"name": "pikachu"}, {"name": "bulbasaur"}]}'

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : donnees = json.loads(reponse_texte) te donne un dictionnaire
#               ordinaire. La température est sous la clé "temperature".
#
#  Exercice 2 : reponse["results"] est une LISTE de dictionnaires. Pour
#               chaque élément de cette liste, prends sa clé "name" :
#               [item["name"] for item in ...].
#
#  Exercice 3 : Python accepte l'écriture  200 <= code <= 299.
#
#  Exercice 4 : enchaîne les deux premiers exercices : json.loads d'abord,
#               puis la clé "count", puis la liste des "name".
