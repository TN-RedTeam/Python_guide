#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 06 : itérateurs & générateurs

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  generateurs.py
  Les exercices ne demandent RIEN de plus que ce qui y est expliqué.

▶ COMMENT COMPLÉTER UNE FONCTION :
    • Chaque fonction contient une ligne « ... » (trois points) : c'est le
      TROU à remplir. Efface ce « ... » et écris ton code à la place, juste
      sous le commentaire « # TODO ».
    • Garde les 4 espaces en début de ligne : en Python, ce décalage
      (l'indentation) signifie « ce code est À L'INTÉRIEUR de la fonction ».
    • Pense au « return » (ou au « yield » pour un générateur) : une fonction
      doit PRODUIRE son résultat, sinon le test échoue.

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


def filtrer_positifs(nombres):
    """OBJECTIF : renvoyer la liste des nombres STRICTEMENT positifs (> 0).

    Exemple : filtrer_positifs([3, -1, 0, 7, -2])  ->  [3, 7]

    Comment t'y prendre (compréhension de liste, vue dans le cours) :
      - garde chaque n de `nombres` à condition que n > 0 ;
      - en une ligne : renvoie  [n for n in nombres if n > 0].
    """
    ...   # ⬅️ remplace cette ligne par ton code


def noms_en_majuscules(noms):
    """OBJECTIF : renvoyer la liste des noms passés en MAJUSCULES.

    Exemple : noms_en_majuscules(["ada", "bob"])  ->  ["ADA", "BOB"]

    Comment t'y prendre :
      - la méthode "ada".upper() renvoie "ADA" ;
      - applique-la à chaque nom dans une compréhension :
        renvoie  [nom.upper() for nom in noms].
    """
    ...   # ⬅️ remplace cette ligne par ton code


def somme_carres(n):
    """OBJECTIF : renvoyer la somme des carrés des entiers de 0 à n-1.

    Exemple : somme_carres(4)  ->  14   (car 0² + 1² + 2² + 3² = 0 + 1 + 4 + 9)

    Comment t'y prendre :
      - le carré de i s'écrit i ** 2 ;
      - parcours range(n) (= 0, 1, …, n-1) et additionne les carrés ;
      - en une ligne : renvoie  sum(i ** 2 for i in range(n)).
    """
    ...   # ⬅️ remplace cette ligne par ton code


def pairs_jusqua(limite):
    """OBJECTIF : écrire un GÉNÉRATEUR qui PRODUIT les nombres pairs de 0 (inclus)
    jusqu'à `limite` (exclu). Un générateur ne fait pas `return` d'une liste : il
    `yield` (livre) ses valeurs une par une.

    Exemple : list(pairs_jusqua(10))  ->  [0, 2, 4, 6, 8]

    Comment t'y prendre :
      - parcours les pairs avec un pas de 2 : for n in range(0, limite, 2) ;
      - à chaque tour, fais  yield n  (et surtout PAS return d'une liste).
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ════════════════════════════════════════════════════════════════════
#  ▶ ON TESTE TON CODE — lance le fichier pour voir tes ✅ / ❌
#
#  C'est ICI qu'on APPELLE tes fonctions, avec des exemples concrets.
#  → Les valeurs d'exemple ci-dessous sont juste des ARGUMENTS qu'on passe
#    à l'appel. Rien de magique ni de caché.
#  C'est normal : en HAUT on DÉFINIT les fonctions, et plus bas on les
#  UTILISE (définir une fonction ≠ l'appeler).
#
#  Comment lire une ligne d'essai :
#      verifie(somme_carres, 4, attendu=14)
#   ↑  appelle  somme_carres(4)  et compare le résultat à 14.
#  (Pour pairs_jusqua, qui est un générateur, le test le déroule en liste.)
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
    print("--- Module 06 : itérateurs & générateurs ---\n")
    resultats = [
        verifie(filtrer_positifs, [3, -1, 0, 7, -2], attendu=[3, 7]),
        verifie(noms_en_majuscules, ["ada", "bob"],  attendu=["ADA", "BOB"]),
        verifie(somme_carres, 4,                     attendu=14),
        verifie(pairs_jusqua, 10,                    attendu=[0, 2, 4, 6, 8]),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
