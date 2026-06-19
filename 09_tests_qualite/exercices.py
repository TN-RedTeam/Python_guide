#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 09 : tests & qualité (approche TDD)

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ? (logique INVERSÉE !)
 Ici, LES TESTS SONT DÉJÀ ÉCRITS (tout en bas du fichier). Ils décrivent
 exactement ce que chaque fonction doit faire. Ton travail : écrire les
 fonctions pour que tous les tests passent au VERT.
 C'est la démarche TDD (Test-Driven Development) : d'abord rouge, puis vert.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  test_demo.py

▶ COMMENT FAIRE :
    • Chaque fonction contient une ligne « ... » (trois points) : c'est le
      TROU à remplir. Efface ce « ... » et écris ton code à la place.
    • Pas sûr de ce qu'on attend ? Va lire les tests en bas du fichier : un
      test comme  assert est_palindrome("kayak") == True  te dit noir sur
      blanc l'entrée et le résultat attendu.
    • Pense au « return » : une fonction doit RENVOYER son résultat.

  Exemple — au départ, la fonction a un trou :

      def double(n):
          ...

  À toi de remplacer le « ... » par la vraie réponse :

      def double(n):
          return n * 2

▶ LANCER :   python3 exercices.py
  Un test qui échoue lève une AssertionError et arrête le programme : c'est
  le « rouge » à transformer en « vert ».
  Bonus : ce sont de vrais asserts, comme pytest. Tu peux aussi mettre ces
  tests dans un fichier test_xxx.py et lancer la commande `pytest`.

▶ BLOQUÉ ? Réessaie d'abord. En dernier recours, ouvre solutions.py.
"""


def est_palindrome(mot):
    """Renvoie True si `mot` se lit pareil à l'endroit et à l'envers.
    Ex : est_palindrome("kayak") -> True ; est_palindrome("python") -> False
    Indice : on peut inverser une chaîne avec mot[::-1].
    """
    # TODO
    ...


def inverser(texte):
    """Renvoie `texte` à l'envers.
    Ex : inverser("abc") -> "cba"
    """
    # TODO
    ...


def factorielle(n):
    """Renvoie n! = 1 × 2 × ... × n.   factorielle(0) vaut 1.
    Ex : factorielle(5) -> 120
    """
    # TODO : une boucle, ou la récursivité
    ...


# ════════════════════════════════════════════════════════════════════
#  Les TESTS (comme pytest) — NE PAS MODIFIER
# ════════════════════════════════════════════════════════════════════
def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Tests — module 09 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("est_palindrome('kayak')", lambda: est_palindrome("kayak"), True)
    essai("est_palindrome('python')", lambda: est_palindrome("python"), False)
    essai("inverser('abc')", lambda: inverser("abc"), "cba")
    essai("factorielle(5)", lambda: factorielle(5), 120)
    essai("factorielle(0)", lambda: factorielle(0), 1)

    print(f"\n{sum(res)}/{len(res)} tests réussis")


if __name__ == "__main__":
    _verifier()
