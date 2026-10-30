#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 02 : les collections (listes, dicts, tuples, sets)

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une serie de fonctions A TROUS que tu completes toi-meme. Tu lances le
 fichier, et il TESTE tes reponses : ✅ = reussi, ❌ = encore a corriger.
══════════════════════════════════════════════════════════════════════

▶ LES EXERCICES SONT CLASSES PAR NIVEAU :
    NIVEAU 1 — REPRODUCTION : tu recopies quasi mot pour mot ce que le
               cours a montre. Si tu bloques ici, relis le cours, la
               reponse y est litteralement.
    NIVEAU 2 — ADAPTATION  : meme pattern que le cours, contexte different.
    NIVEAU 3 — COMBINAISON : tu combines deux idees du cours ensemble.
    NIVEAU 4 — DEFI        : tu raisonnes par toi-meme a partir des patterns.

  Chaque exercice a un bloc « RAPPEL DU COURS » : c'est le bout de code
  du README.md dont tu as besoin. Si tu seches, relis-le, la reponse est
  dedans. Tu n'as PAS besoin d'inventer quoi que ce soit de nouveau.

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commente   →  collections_demo.py
  Les exercices ne demandent RIEN de plus que ce qui y est explique.

▶ COMMENT COMPLETER UNE FONCTION :
    - Chaque fonction contient une ligne « ... » (trois points) : c'est le
      TROU a remplir. Efface ce « ... » et ecris ton code a la place.
    - Garde les 4 espaces en debut de ligne (l'indentation).
    - Pense au « return » : une fonction doit RENVOYER son resultat.

  Exemple — au depart, la fonction a un trou :

      def double(n):
          ...

  A toi de remplacer le « ... » par la vraie reponse :

      def double(n):
          return n * 2

▶ 💾 ASTUCE « git pull » (pour ne jamais perdre ton travail) :
  Ne code pas directement dans ce fichier (il est suivi par git). Copie-le :
      cp exercices.py exercices_perso.py      # puis :  python3 exercices_perso.py

▶ LANCER LES TESTS :   python3 exercices.py

▶ BLOQUE ? Relis le RAPPEL DU COURS dans la fonction. En tout dernier
  recours, ouvre solutions.py (le corrige commente).
"""


# ╔════════════════════════════════════════════════════════════════════╗
# ║  NIVEAU 1 — REPRODUCTION (le cours te donne la reponse)          ║
# ╚════════════════════════════════════════════════════════════════════╝

def deuxieme_element(liste):
    """OBJECTIF : renvoyer le DEUXIEME element de `liste`.

    Exemple : deuxieme_element(["a", "b", "c"])  ->  "b"

    ╔══ RAPPEL DU COURS ═══════════════════════════════════════════╗
    ║  Les positions commencent a 0 :                              ║
    ║      fruits = ["pomme", "banane", "cerise"]                  ║
    ║      #          index 0   index 1   index 2                  ║
    ║      print(fruits[0])   # "pomme"  (le 1er)                  ║
    ║      print(fruits[1])   # "banane" (le 2e)                   ║
    ╚══════════════════════════════════════════════════════════════╝

    Comment t'y prendre :
      - le 2e element est a l'index 1 (car on compte depuis 0) ;
      - recupere-le avec  liste[1] ;
      - renvoie-le avec return.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def total_panier(panier):
    """OBJECTIF : `panier` est un dict {produit: prix}. Renvoyer la somme de
    tous les prix (c'est-a-dire la somme des VALEURS du dictionnaire).

    Exemple : total_panier({"pain": 1.2, "lait": 0.8})  ->  2.0

    ╔══ RAPPEL DU COURS ═══════════════════════════════════════════╗
    ║  pilote = {"nom": "Hamilton", "titres": 7}                   ║
    ║  print(pilote.values())   # toutes les valeurs               ║
    ║  # sum(...) additionne tous les elements d'une serie :       ║
    ║  print(sum([1, 2, 3]))    # 6                                ║
    ╚══════════════════════════════════════════════════════════════╝

    Comment t'y prendre :
      - panier.values() donne toutes les valeurs (les prix) ;
      - sum(...) en fait la somme ;
      - renvoie  sum(panier.values()).
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ╔════════════════════════════════════════════════════════════════════╗
# ║  NIVEAU 2 — ADAPTATION (meme pattern, nouveau contexte)          ║
# ╚════════════════════════════════════════════════════════════════════╝

def compter_occurrences(liste, valeur):
    """OBJECTIF : renvoyer combien de fois `valeur` apparait dans `liste`
    (le resultat est un nombre entier).

    Exemple : compter_occurrences([1, 2, 2, 3, 2], 2)  ->  3   (le 2 apparait 3 fois)

    ╔══ RAPPEL DU COURS ═══════════════════════════════════════════╗
    ║  Le pattern COMPTEUR (vu dans « Penser comme un dev ») :     ║
    ║                                                              ║
    ║      compte = 0                                              ║
    ║      for x in nombres:                                       ║
    ║          if x > 10:            # <-- la condition change     ║
    ║              compte = compte + 1                             ║
    ║                                                              ║
    ║  Ici la condition est : « element == valeur ».               ║
    ╚══════════════════════════════════════════════════════════════╝

    Comment t'y prendre :
      1. cree un compteur a 0 ;
      2. parcours `liste` avec une boucle for ;
      3. si l'element est egal a `valeur`, ajoute 1 au compteur ;
      4. a la fin, renvoie le compteur.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def produits_en_rupture(stock):
    """OBJECTIF : `stock` est un dict {produit: quantite}. Renvoyer la LISTE
    des produits dont la quantite vaut 0 (les produits en rupture).

    Exemple : produits_en_rupture({"pommes": 5, "poires": 0, "kiwis": 0})
              ->  ["poires", "kiwis"]

    ╔══ RAPPEL DU COURS (section « N'afficher que certaines paires ») ═╗
    ║  stock = {"pommes": 5, "poires": 0, "kiwis": 3}                 ║
    ║                                                                  ║
    ║  for produit, quantite in stock.items():                         ║
    ║      if quantite == 0:                                           ║
    ║          print(f"{produit} est en rupture")                      ║
    ║                                                                  ║
    ║  C'est le MEME code — sauf qu'au lieu de print, tu AJOUTES      ║
    ║  le produit dans une liste avec .append().                       ║
    ╚══════════════════════════════════════════════════════════════════╝

    Comment t'y prendre :
      1. cree une liste vide :  resultat = [] ;
      2. parcours les paires :  for produit, quantite in stock.items() ;
      3. si quantite == 0, ajoute le produit :  resultat.append(produit) ;
      4. renvoie resultat.
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ╔════════════════════════════════════════════════════════════════════╗
# ║  NIVEAU 3 — COMBINAISON (deux idees du cours ensemble)           ║
# ╚════════════════════════════════════════════════════════════════════╝

def sans_doublons_tries(liste):
    """OBJECTIF : renvoyer la liste des valeurs DISTINCTES de `liste`, triees
    dans l'ordre croissant.

    Exemple : sans_doublons_tries([3, 1, 2, 3, 1])  ->  [1, 2, 3]

    ╔══ RAPPEL DU COURS ═══════════════════════════════════════════╗
    ║  # Un set elimine les doublons :                             ║
    ║  nombres = {1, 2, 2, 3, 3, 3}   # -> {1, 2, 3}             ║
    ║                                                              ║
    ║  # sorted() trie et renvoie une LISTE :                      ║
    ║  sorted({3, 1, 2})               # -> [1, 2, 3]             ║
    ╚══════════════════════════════════════════════════════════════╝

    Comment t'y prendre :
      1. set(liste) enleve les doublons ;
      2. sorted(...) trie ET renvoie une liste ;
      3. renvoie sorted(set(liste)).
    """
    ...   # ⬅️ remplace cette ligne par ton code


def inverser_dictionnaire(d):
    """OBJECTIF : renvoyer un NOUVEAU dictionnaire ou, pour chaque paire de `d`,
    la valeur devient la cle et la cle devient la valeur.

    Exemple : inverser_dictionnaire({"a": 1, "b": 2})  ->  {1: "a", 2: "b"}
    (On suppose que les valeurs sont uniques.)

    ╔══ RAPPEL DU COURS ═══════════════════════════════════════════╗
    ║  # Parcourir un dict avec .items() :                         ║
    ║  for cle, valeur in pilote.items():                          ║
    ║      print(f"{cle} = {valeur}")                              ║
    ║                                                              ║
    ║  # Ajouter une paire a un dict :                             ║
    ║  pilote["points"] = 25                                       ║
    ╚══════════════════════════════════════════════════════════════╝

    Comment t'y prendre :
      1. cree un dictionnaire vide : resultat = {} ;
      2. parcours les paires : for cle, valeur in d.items() ;
      3. range l'inverse : resultat[valeur] = cle ;
      4. renvoie resultat.
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ╔════════════════════════════════════════════════════════════════════╗
# ║  NIVEAU 4 — DEFI (raisonne a partir des patterns du cours)       ║
# ╚════════════════════════════════════════════════════════════════════╝

def compter_mots_liste(mots):
    """OBJECTIF : renvoyer un dictionnaire qui compte combien de fois CHAQUE
    mot apparait dans la liste `mots`.

    Exemple : compter_mots_liste(["a", "b", "a"])  ->  {"a": 2, "b": 1}

    ╔══ RAPPEL DU COURS (section « Le raisonnement en action ») ══╗
    ║  Le pattern COMPTEUR applique a un dict (vu dans le cours) :  ║
    ║                                                              ║
    ║  mots = ["a", "b", "a", "c", "a", "b"]                      ║
    ║  compteur = {}                                               ║
    ║  for mot in mots:                                            ║
    ║      compteur[mot] = compteur.get(mot, 0) + 1                ║
    ║  # -> {'a': 3, 'b': 2, 'c': 1}                              ║
    ║                                                              ║
    ║  .get(mot, 0) = la valeur actuelle, ou 0 si le mot est      ║
    ║  nouveau. On ajoute 1, et on remet dans le dict.             ║
    ╚══════════════════════════════════════════════════════════════╝

    Comment t'y prendre :
      1. cree un dict vide :  compteur = {} ;
      2. parcours `mots` avec une boucle for ;
      3. a chaque mot :  compteur[mot] = compteur.get(mot, 0) + 1 ;
      4. renvoie compteur.
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ════════════════════════════════════════════════════════════════════
#  ▶ ON TESTE TON CODE — lance le fichier pour voir tes ✅ / ❌
#
#  C'est ICI qu'on APPELLE tes fonctions, avec des exemples concrets.
#  → Les valeurs d'exemple ci-dessous (les listes, les dicts...) sont juste
#    des ARGUMENTS qu'on passe a l'appel. Rien de magique ni de cache.
#  C'est normal : en HAUT on DEFINIT les fonctions, et plus bas on les
#  UTILISE (definir une fonction ≠ l'appeler).
#
#  Comment lire une ligne d'essai :
#      verifie(compter_occurrences, [1, 2, 2], 2, attendu=2)
#   ↑  appelle  compter_occurrences([1, 2, 2], 2)  et compare le resultat a 2.
# ════════════════════════════════════════════════════════════════════
import types as _types


def verifie(fonction, *arguments, attendu):
    """Appelle fonction(*arguments) et compare au resultat attendu. (Mecanique du test.)"""
    try:
        obtenu = fonction(*arguments)
        if isinstance(obtenu, _types.GeneratorType):
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

    print("NIVEAU 1 — REPRODUCTION")
    resultats = [
        verifie(deuxieme_element, ["a", "b", "c"],          attendu="b"),
        verifie(total_panier, {"pain": 1.2, "lait": 0.8},   attendu=2.0),
    ]
    print()

    print("NIVEAU 2 — ADAPTATION")
    resultats += [
        verifie(compter_occurrences, [1, 2, 2, 3, 2], 2,    attendu=3),
        verifie(produits_en_rupture, {"pommes": 5, "poires": 0, "kiwis": 0},
                attendu=["poires", "kiwis"]),
    ]
    print()

    print("NIVEAU 3 — COMBINAISON")
    resultats += [
        verifie(sans_doublons_tries, [3, 1, 2, 3, 1],       attendu=[1, 2, 3]),
        verifie(inverser_dictionnaire, {"a": 1, "b": 2},    attendu={1: "a", 2: "b"}),
    ]
    print()

    print("NIVEAU 4 — DEFI")
    resultats += [
        verifie(compter_mots_liste, ["a", "b", "a"],        attendu={"a": 2, "b": 1}),
    ]

    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
