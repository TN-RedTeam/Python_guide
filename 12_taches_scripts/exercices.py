#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 12 : scripts réutilisables (argparse)

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  tache_repetee.py  (puis sauvegarde.py)
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

import argparse


def construire_parseur():
    """OBJECTIF : renvoyer un ArgumentParser configuré avec :
      - un argument OBLIGATOIRE  --source
      - un argument FACULTATIF   --destination, valeur par défaut "sauvegardes"
    (Ici on ne fait QUE construire et renvoyer le parseur — pas de parse_args.)

    Comment t'y prendre :
      1. crée le parseur :   parseur = argparse.ArgumentParser() ;
      2. ajoute l'obligatoire : parseur.add_argument("--source", required=True) ;
      3. ajoute le facultatif : parseur.add_argument("--destination", default="sauvegardes") ;
      4. renvoie parseur.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def nom_archive(source, date):
    """OBJECTIF : renvoyer le nom d'archive au format "<source>_<date>.zip".

    Exemple : nom_archive("docs", "2026-06-19")  ->  "docs_2026-06-19.zip"

    Comment t'y prendre :
      - assemble les morceaux avec une f-string : f"{source}_{date}.zip" ;
      - renvoie-la.
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
#      verifie(nom_archive, "docs", "2026-06-19", attendu="docs_2026-06-19.zip")
#   ↑  appelle  nom_archive("docs", "2026-06-19")  et compare au résultat attendu.
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
    print("--- Module 12 : scripts réutilisables (argparse) ---\n")

    # Pour tester construire_parseur, on construit le parseur puis on simule une
    # ligne de commande avec parse_args([...]) (comme si on tapait : --source docs).
    def destination_par_defaut():
        return construire_parseur().parse_args(["--source", "docs"]).destination

    def source_lue():
        return construire_parseur().parse_args(["--source", "docs", "--destination", "sav"]).source

    resultats = [
        verifie(destination_par_defaut, attendu="sauvegardes"),
        verifie(source_lue,             attendu="docs"),
        verifie(nom_archive, "docs", "2026-06-19", attendu="docs_2026-06-19.zip"),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
