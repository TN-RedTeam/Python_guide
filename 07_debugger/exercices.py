#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 07 : débugger (TROUVE ET CORRIGE LES BUGS)

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ? (différent des autres modules !)
 Ici, PAS de trous à remplir. Les fonctions sont DÉJÀ écrites, mais elles
 CONTIENNENT DES BUGS volontaires. Ton travail : les trouver et corriger,
 jusqu'à ce que tous les tests passent au ✅.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  demo_debug.py

▶ LA MÉTHODE, ÉTAPE PAR ÉTAPE :
    1. Lance :   python3 exercices.py   →  tu verras des ❌.
    2. Pour chaque ❌, lis ce que le test ATTENDAIT et ce que la fonction a
       renvoyé. L'écart entre les deux te met sur la piste du bug.
    3. Comprends POURQUOI c'est faux. Deux outils :
         • ajoute un print(...) pour voir une valeur au milieu du calcul ;
         • ou pose un breakpoint() pour mettre le programme en pause et
           inspecter les variables (commandes : n = ligne suivante, c =
           continuer, p nom = afficher une variable, q = quitter).
    4. Corrige la ligne fautive, relance, et recommence jusqu'à 100 % de ✅.

  💡 Astuce : certains bugs sont signalés par un commentaire « 🐞 BUG ».
     Ils ne le seront pas tous dans la vraie vie, mais ici c'est pour
     t'apprendre à reconnaître les erreurs classiques.

▶ 💾 ASTUCE « git pull » (pour ne jamais perdre ton travail) :
  Ne corrige pas directement dans ce fichier (il est suivi par git). Copie-le et
  travaille dans la copie — elle est ignorée par git, donc une mise à jour du
  guide (« git pull ») ne touchera jamais ton travail :
      cp exercices.py exercices_perso.py      # puis :  python3 exercices_perso.py

▶ BLOQUÉ ? Réessaie vraiment d'abord. En dernier recours, ouvre
  solutions.py (le corrigé, avec l'explication de chaque bug).
"""


def moyenne(notes):
    """Devrait renvoyer la moyenne d'une liste de notes.
    moyenne([10, 20, 30]) devrait valoir 20.0
    """
    total = 0
    for note in notes:
        total = note          # 🐞 BUG : à chaque tour, on ÉCRASE total au lieu de l'additionner
    return total / len(notes)


def maximum(liste):
    """Devrait renvoyer le plus grand élément.
    maximum([-5, -2, -9]) devrait valoir -2
    """
    plus_grand = 0            # 🐞 BUG : partir de 0 casse tout si tous les nombres sont négatifs
    for valeur in liste:
        if valeur > plus_grand:
            plus_grand = valeur
    return plus_grand


def compter_voyelles(mot):
    """Devrait compter les voyelles (a, e, i, o, u).
    compter_voyelles("bonjour") devrait valoir 3   (o, o, u)
    """
    voyelles = "aeiou"
    total = 0
    for lettre in mot:
        if lettre not in voyelles:   # 🐞 BUG : la condition est INVERSÉE (compte les consonnes)
            total += 1
    return total


# ════════════════════════════════════════════════════════════════════
#  ▶ ON TESTE TES CORRECTIONS — lance le fichier pour voir tes ✅ / ❌
#
#  C'est ICI qu'on APPELLE les fonctions (avec des exemples concrets) pour
#  révéler les bugs. Les valeurs comme [10, 20, 30] sont juste les ARGUMENTS
#  passés à l'appel. Corrige le code des fonctions plus haut jusqu'à tout ✅.
#
#  Comment lire une ligne d'essai :
#      verifie(moyenne, [10, 20, 30], attendu=20.0)
#   ↑  appelle  moyenne([10, 20, 30])  et compare le résultat à 20.0.
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
        print(f"     ⚠️  le code a renvoyé : {obtenu!r}")
    return ok


if __name__ == "__main__":
    print("--- Module 07 : corrige les bugs ! ---\n")
    resultats = [
        verifie(moyenne, [10, 20, 30],   attendu=20.0),
        verifie(maximum, [-5, -2, -9],   attendu=-2),
        verifie(maximum, [3, 9, 4],      attendu=9),
        verifie(compter_voyelles, "bonjour", attendu=3),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
