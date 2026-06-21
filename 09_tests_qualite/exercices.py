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

  Chaque fonction t'explique tout ce qu'il faut : son OBJECTIF, un EXEMPLE, et
  les ÉTAPES pour y arriver.

▶ 💾 ASTUCE « git pull » (pour ne jamais perdre ton travail) :
  Ne code pas directement dans ce fichier (il est suivi par git). Copie-le et
  travaille dans la copie — elle est ignorée par git, donc une mise à jour du
  guide (« git pull ») ne touchera jamais ton travail :
      cp exercices.py exercices_perso.py      # puis :  python3 exercices_perso.py

▶ LANCER :   python3 exercices.py
  Un test qui échoue lève une AssertionError et arrête le programme : c'est
  le « rouge » à transformer en « vert ».
  Bonus : ce sont de vrais asserts, comme pytest. Tu peux aussi mettre ces
  tests dans un fichier test_xxx.py et lancer la commande `pytest`.

▶ BLOQUÉ ? Réessaie d'abord. En dernier recours, ouvre solutions.py.
"""


def est_palindrome(mot):
    """OBJECTIF : renvoyer True si `mot` se lit pareil à l'endroit et à l'envers,
    False sinon.

    Exemples : est_palindrome("kayak")  ->  True       est_palindrome("python")  ->  False

    Comment t'y prendre :
      - mot[::-1] renvoie le mot à l'envers (ex. "kayak"[::-1] == "kayak") ;
      - renvoie le résultat du test  mot == mot[::-1].
    """
    ...   # ⬅️ remplace cette ligne par ton code


def inverser(texte):
    """OBJECTIF : renvoyer `texte` à l'envers.

    Exemple : inverser("abc")  ->  "cba"

    Comment t'y prendre :
      - le découpage [::-1] inverse une chaîne ;
      - renvoie  texte[::-1].
    """
    ...   # ⬅️ remplace cette ligne par ton code


def factorielle(n):
    """OBJECTIF : renvoyer n! = 1 × 2 × … × n.  Cas particulier : factorielle(0) vaut 1.

    Exemple : factorielle(5)  ->  120   (car 1 × 2 × 3 × 4 × 5 = 120)

    Comment t'y prendre :
      1. pars d'un résultat à 1 ;
      2. parcours les nombres de 2 à n : for i in range(2, n + 1) ;
      3. multiplie le résultat par i à chaque tour (resultat *= i) ;
      4. renvoie le résultat (si n vaut 0 ou 1, la boucle ne tourne pas → 1, parfait).
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ════════════════════════════════════════════════════════════════════
#  ▶ LES TESTS — déjà écrits pour toi (lance le fichier : objectif tout ✅)
#
#  C'est ICI qu'on APPELLE tes fonctions avec des exemples : chaque ligne
#  est un TEST (une entrée connue → un résultat attendu). C'est cette liste
#  qui décrit EXACTEMENT ce que tes fonctions doivent faire.
#  → Les valeurs comme "kayak" sont juste les ARGUMENTS passés à l'appel.
#
#  Comment lire une ligne de test :
#      verifie(est_palindrome, "kayak", attendu=True)
#   ↑  appelle  est_palindrome("kayak")  et vérifie que ça renvoie True.
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
    print("--- Module 09 : tests & qualité (TDD) ---\n")
    resultats = [
        verifie(est_palindrome, "kayak",  attendu=True),
        verifie(est_palindrome, "python", attendu=False),
        verifie(inverser, "abc",          attendu="cba"),
        verifie(factorielle, 5,           attendu=120),
        verifie(factorielle, 0,           attendu=1),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} tests réussis ✅")
