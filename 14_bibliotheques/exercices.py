#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 14 : les bibliothèques

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  explorer_modules.py
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

import importlib.util


def est_disponible(nom_module):
    """OBJECTIF : renvoyer True si le module `nom_module` est installé (importable),
    False sinon.

    Exemples : est_disponible("json")  ->  True   (toujours là, c'est la stdlib)
               est_disponible("module_qui_nexiste_pas_xyz")  ->  False

    Comment t'y prendre :
      - importlib.util.find_spec(nom_module) renvoie une « fiche » si le module
        existe, ou None s'il est introuvable ;
      - renvoie le test  importlib.util.find_spec(nom_module) is not None.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def ligne_requirement(nom, version):
    """OBJECTIF : construire une ligne de requirements.txt qui FIGE la version
    (avec ==).

    Exemple : ligne_requirement("requests", "2.31.0")  ->  "requests==2.31.0"

    Comment t'y prendre :
      - colle le nom, "==" et la version avec une f-string : f"{nom}=={version}" ;
      - renvoie-la.
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ════════════════════════════════════════════════════════════════════
#  ▶ ON TESTE TON CODE — lance le fichier pour voir tes ✅ / ❌
#
#  C'est ICI qu'on APPELLE tes fonctions, avec des exemples concrets.
#  → Les valeurs d'exemple ci-dessous ("json", "requests"...) sont juste des
#    ARGUMENTS qu'on passe à l'appel. Rien de magique ni de caché.
#  C'est normal : en HAUT on DÉFINIT les fonctions, et plus bas on les
#  UTILISE (définir une fonction ≠ l'appeler).
#
#  Comment lire une ligne d'essai :
#      verifie(est_disponible, "json", attendu=True)
#   ↑  appelle  est_disponible("json")  et compare le résultat à True.
# ════════════════════════════════════════════════════════════════════
import types as _types


def verifie(fonction, *arguments, attendu):
    """Appelle fonction(*arguments) et compare au résultat attendu. (Mécanique du test.)"""
    try:
        obtenu = fonction(*arguments)
        if isinstance(obtenu, _types.GeneratorType):   # un générateur → on le déroule en liste
            obtenu = list(obtenu)
    except Exception as e:
        obtenu = f"ERREUR: {e}"
    ok = (obtenu == attendu)
    args_lisibles = ", ".join(a.__name__ if callable(a) else repr(a) for a in arguments)
    print(f"{'✅' if ok else '❌'} {fonction.__name__}({args_lisibles})  ->  {attendu!r}")
    if not ok:
        print(f"     ⚠️  ton code a renvoyé : {obtenu!r}")
    return ok


if __name__ == "__main__":
    print("--- Module 14 : les bibliothèques ---\n")
    resultats = [
        verifie(est_disponible, "json",                            attendu=True),
        verifie(est_disponible, "module_qui_nexiste_pas_xyz",      attendu=False),
        verifie(ligne_requirement, "requests", "2.31.0",           attendu="requests==2.31.0"),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
