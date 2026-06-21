#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 01 : les bases (variables, conditions, boucles)

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  bases.py
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


def somme_jusqua(n):
    """OBJECTIF : renvoyer la somme de tous les entiers de 1 à n inclus.

    Exemple : somme_jusqua(5)  ->  15   (car 1 + 2 + 3 + 4 + 5 = 15)

    Comment t'y prendre :
      1. crée un total à 0 ;
      2. parcours les nombres de 1 à n avec : for i in range(1, n + 1) ;
         (range(1, n + 1) va de 1 jusqu'à n INCLUS) ;
      3. ajoute i au total à chaque tour ;
      4. renvoie le total.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def est_pair(n):
    """OBJECTIF : renvoyer True si n est pair, False sinon.

    Exemples : est_pair(4)  ->  True       est_pair(7)  ->  False

    Comment t'y prendre :
      - un nombre est pair si le reste de sa division par 2 vaut 0 ;
      - en Python, ce reste s'écrit  n % 2  (l'opérateur « modulo ») ;
      - renvoie le résultat du test  n % 2 == 0  (qui vaut déjà True ou False).
    """
    ...   # ⬅️ remplace cette ligne par ton code


def fizzbuzz(n):
    """OBJECTIF : pour UN nombre n, renvoyer (sous forme de TEXTE) :
      - "FizzBuzz" si n est divisible par 3 ET par 5 ;
      - "Fizz"     si divisible par 3 seulement ;
      - "Buzz"     si divisible par 5 seulement ;
      - sinon, le nombre lui-même converti en texte, ex. "7".

    Exemples : fizzbuzz(15) -> "FizzBuzz"   fizzbuzz(9) -> "Fizz"   fizzbuzz(7) -> "7"

    Comment t'y prendre :
      - « divisible par 3 » s'écrit  n % 3 == 0 ;
      - teste les cas avec if / elif / else, en mettant le cas le PLUS PRÉCIS
        en premier (le ET 3-et-5 AVANT les cas simples), sinon tu n'y arrives jamais ;
      - pour le dernier cas, convertis le nombre en texte avec str(n).
    """
    ...   # ⬅️ remplace cette ligne par ton code


def compte_a_rebours(depart):
    """OBJECTIF : renvoyer une LISTE qui décompte de `depart` jusqu'à 1.

    Exemple : compte_a_rebours(3)  ->  [3, 2, 1]

    Comment t'y prendre :
      1. crée une liste vide : resultat = [] ;
      2. parcours les nombres de `depart` à 1 en DÉCROISSANT :
         for i in range(depart, 0, -1)   (le -1 = on recule d'1 à chaque pas) ;
      3. ajoute i à la liste avec resultat.append(i) ;
      4. renvoie resultat.
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ════════════════════════════════════════════════════════════════════
#  ▶ ON TESTE TON CODE — lance le fichier pour voir tes ✅ / ❌
#
#  C'est ICI qu'on APPELLE tes fonctions, avec des exemples concrets.
#  → Les valeurs d'exemple ci-dessous (comme 5, 4, 15...) sont juste des
#    ARGUMENTS qu'on passe à l'appel. Rien de magique ni de caché.
#  C'est normal : en HAUT on DÉFINIT les fonctions, et plus bas on les
#  UTILISE (définir une fonction ≠ l'appeler).
#
#  Comment lire une ligne d'essai :
#      verifie(somme_jusqua, 5, attendu=15)
#   ↑  appelle  somme_jusqua(5)  et compare le résultat à 15.
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
    print("--- Module 01 : les bases ---\n")
    resultats = [
        verifie(somme_jusqua, 5,     attendu=15),
        verifie(somme_jusqua, 1,     attendu=1),
        verifie(est_pair, 4,         attendu=True),
        verifie(est_pair, 7,         attendu=False),
        verifie(fizzbuzz, 15,        attendu="FizzBuzz"),
        verifie(fizzbuzz, 9,         attendu="Fizz"),
        verifie(fizzbuzz, 10,        attendu="Buzz"),
        verifie(fizzbuzz, 7,         attendu="7"),
        verifie(compte_a_rebours, 3, attendu=[3, 2, 1]),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
