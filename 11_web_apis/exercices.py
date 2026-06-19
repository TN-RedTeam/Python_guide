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

▶ LANCER LES TESTS :   python3 exercices.py
  Pour chaque ❌, le test affiche ce qu'il ATTENDAIT et ce que TA fonction
  a renvoyé : compare les deux, ton erreur est dans l'écart.

▶ BLOQUÉ ? Réessaie en relisant l'indice écrit dans la fonction. En tout
  dernier recours, ouvre solutions.py (le corrigé commenté).
"""

import json


def extraire_temperature(reponse_texte):
    """`reponse_texte` est une chaîne JSON, ex. '{"ville": "Paris", "temperature": 18}'.
    Renvoie la valeur de "temperature" (un nombre).
    Indice : json.loads(texte) transforme le TEXTE JSON en dict Python.
    """
    # TODO : json.loads puis accède à la clé
    ...


def noms_des_resultats(reponse):
    """`reponse` est DÉJÀ un dict, de la forme :
        {"results": [{"name": "Ada"}, {"name": "Bob"}]}
    Renvoie la liste des noms : ["Ada", "Bob"].
    """
    # TODO : parcours reponse["results"] et récupère chaque "name"
    ...


def statut_ok(code):
    """Renvoie True si `code` est un code HTTP de succès (entre 200 et 299 inclus).
    Ex : statut_ok(200) -> True ; statut_ok(404) -> False
    """
    # TODO
    ...


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
