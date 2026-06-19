#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 11 : web & APIs (traiter une réponse JSON)

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ CONTEXTE : pas besoin d'Internet ici. On s'entraîne à TRAITER une réponse
  d'API, qui arrive presque toujours en JSON — du texte structuré qu'on
  transforme en dict Python avec json.loads(...).

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  appeler_api.py  (puis scraping.py)
  Les exercices ne demandent RIEN de plus que ce qui y est expliqué.

▶ COMMENT COMPLÉTER UNE FONCTION :
    • Chaque fonction contient une ligne « ... » (trois points) : c'est le
      TROU à remplir. Efface ce « ... » et écris ton code à la place, juste
      sous le commentaire « # TODO ».
    • Garde les 4 espaces en début de ligne : en Python, ce décalage
      (l'indentation) signifie « ce code est À L'INTÉRIEUR de la fonction ».
    • Pense au « return » : une fonction doit RENVOYER son résultat. Sans
      « return », elle ne renvoie « rien » (None) et le test échoue.

  Exemple — au départ, la fonction a un trou :

      def double(n):
          ...

  À toi de remplacer le « ... » par la vraie réponse :

      def double(n):
          return n * 2

  Chaque fonction t'explique tout ce qu'il faut : son OBJECTIF, un EXEMPLE, et
  les ÉTAPES pour y arriver. Tu n'as PAS besoin de lire le bas du fichier.

▶ 💾 ASTUCE « git pull » (pour ne jamais perdre ton travail) :
  Ne code pas directement dans ce fichier (il est suivi par git). Copie-le et
  travaille dans la copie — elle est ignorée par git, donc une mise à jour du
  guide (« git pull ») ne touchera jamais ton travail :
      cp exercices.py exercices_perso.py      # puis :  python3 exercices_perso.py

▶ LANCER LES TESTS :   python3 exercices.py
  Pour chaque ❌, le test affiche ce qu'il ATTENDAIT et ce que TA fonction
  a renvoyé : compare les deux, ton erreur est dans l'écart.

▶ BLOQUÉ ? Réessaie en relisant l'indice écrit dans la fonction. En tout
  dernier recours, ouvre solutions.py (le corrigé commenté).
"""

import json


def extraire_temperature(reponse_texte):
    """OBJECTIF : `reponse_texte` est une CHAÎNE de texte au format JSON, ex.
    '{"ville": "Paris", "temperature": 18}'. Renvoyer la valeur de "temperature".

    Exemple : extraire_temperature('{"ville": "Paris", "temperature": 18}')  ->  18

    Comment t'y prendre :
      1. json.loads(reponse_texte) transforme le TEXTE JSON en dict Python ;
      2. accède ensuite à la clé : donnees["temperature"] ;
      3. renvoie cette valeur.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def noms_des_resultats(reponse):
    """OBJECTIF : `reponse` est DÉJÀ un dict, de la forme
        {"results": [{"name": "Ada"}, {"name": "Bob"}]}
    Renvoyer la liste des noms : ["Ada", "Bob"].

    Comment t'y prendre :
      - reponse["results"] est une liste de dicts ;
      - récupère le "name" de chacun ;
      - renvoie  [element["name"] for element in reponse["results"]].
    """
    ...   # ⬅️ remplace cette ligne par ton code


def statut_ok(code):
    """OBJECTIF : renvoyer True si `code` est un code HTTP de succès (entre 200
    et 299 inclus), False sinon.

    Exemples : statut_ok(200)  ->  True       statut_ok(404)  ->  False

    Comment t'y prendre :
      - un code est un succès s'il est >= 200 ET <= 299 ;
      - en Python on peut écrire ça d'un coup : 200 <= code <= 299 ;
      - renvoie ce test.
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ════════════════════════════════════════════════════════════════════
#  Auto-vérification — NE PAS MODIFIER
# ════════════════════════════════════════════════════════════════════
def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Vérification — module 11 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("extraire_temperature(...)",
          lambda: extraire_temperature('{"ville": "Paris", "temperature": 18}'), 18)
    essai("noms_des_resultats(...)",
          lambda: noms_des_resultats({"results": [{"name": "Ada"}, {"name": "Bob"}]}), ["Ada", "Bob"])
    essai("statut_ok(200)", lambda: statut_ok(200), True)
    essai("statut_ok(404)", lambda: statut_ok(404), False)

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
