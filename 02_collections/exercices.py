#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 02 : les collections (listes, dicts, tuples, sets)

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  collections_demo.py
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


def deuxieme_element(liste):
    """OBJECTIF : renvoyer le DEUXIÈME élément de `liste`.

    Exemple : deuxieme_element(["a", "b", "c"])  ->  "b"

    Comment t'y prendre :
      - les positions commencent à 0 : le 1er est à l'index 0, le 2e à l'index 1 ;
      - récupère l'élément à l'index 1 avec les crochets : liste[1] ;
      - renvoie-le avec return.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def compter_occurrences(liste, valeur):
    """OBJECTIF : renvoyer combien de fois `valeur` apparaît dans `liste`
    (le résultat est un nombre entier).

    Exemple : compter_occurrences([1, 2, 2, 3, 2], 2)  ->  3   (le 2 apparaît 3 fois)

    Comment t'y prendre :
      1. crée un compteur à 0 ;
      2. parcours `liste` avec une boucle for ;
      3. si l'élément est égal à `valeur`, ajoute 1 au compteur ;
      4. à la fin, renvoie le compteur.
      (Raccourci tout fait : liste.count(valeur) renvoie déjà ce nombre.)
    """
    ...   # ⬅️ remplace cette ligne par ton code


def sans_doublons_tries(liste):
    """OBJECTIF : renvoyer la liste des valeurs DISTINCTES de `liste`, triées
    dans l'ordre croissant.

    Exemple : sans_doublons_tries([3, 1, 2, 3, 1])  ->  [1, 2, 3]

    Comment t'y prendre :
      1. set(liste) enlève les doublons ;
      2. sorted(...) trie ET renvoie une liste ;
      3. renvoie sorted(set(liste)).
    """
    ...   # ⬅️ remplace cette ligne par ton code


def inverser_dictionnaire(d):
    """OBJECTIF : renvoyer un NOUVEAU dictionnaire où, pour chaque paire de `d`,
    la valeur devient la clé et la clé devient la valeur.

    Exemple : inverser_dictionnaire({"a": 1, "b": 2})  ->  {1: "a", 2: "b"}
    (On suppose que les valeurs sont uniques.)

    Comment t'y prendre :
      1. crée un dictionnaire vide : resultat = {} ;
      2. parcours les paires : for cle, valeur in d.items() ;
      3. range l'inverse : resultat[valeur] = cle ;
      4. renvoie resultat.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def total_panier(panier):
    """OBJECTIF : `panier` est un dict {produit: prix}. Renvoyer la somme de
    tous les prix (c'est-à-dire la somme des VALEURS du dictionnaire).

    Exemple : total_panier({"pain": 1.2, "lait": 0.8})  ->  2.0

    Comment t'y prendre :
      - panier.values() donne toutes les valeurs (les prix) ;
      - sum(...) en fait la somme ;
      - renvoie cette somme.
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ════════════════════════════════════════════════════════════════════
#  ▶ ON TESTE TON CODE — lance le fichier pour voir tes ✅ / ❌
#
#  C'est ICI qu'on APPELLE tes fonctions, avec des exemples concrets.
#  → Les valeurs d'exemple ci-dessous (les listes, les dicts...) sont juste
#    des ARGUMENTS qu'on passe à l'appel. Rien de magique ni de caché.
#  C'est normal : en HAUT on DÉFINIT les fonctions, et plus bas on les
#  UTILISE (définir une fonction ≠ l'appeler).
#
#  Comment lire une ligne d'essai :
#      verifie(compter_occurrences, [1, 2, 2], 2, attendu=2)
#   ↑  appelle  compter_occurrences([1, 2, 2], 2)  et compare le résultat à 2.
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
    print("--- Module 02 : les collections ---\n")
    resultats = [
        verifie(deuxieme_element, ["a", "b", "c"],          attendu="b"),
        verifie(compter_occurrences, [1, 2, 2, 3, 2], 2,    attendu=3),
        verifie(sans_doublons_tries, [3, 1, 2, 3, 1],       attendu=[1, 2, 3]),
        verifie(inverser_dictionnaire, {"a": 1, "b": 2},    attendu={1: "a", 2: "b"}),
        verifie(total_panier, {"pain": 1.2, "lait": 0.8},   attendu=2.0),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
