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
    print("--- Vérification — module 12 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    def dest_par_defaut():
        p = construire_parseur()
        return p.parse_args(["--source", "docs"]).destination

    def source_lue():
        p = construire_parseur()
        return p.parse_args(["--source", "docs", "--destination", "sav"]).source

    essai("destination par défaut", dest_par_defaut, "sauvegardes")
    essai("source lue", source_lue, "docs")
    essai("nom_archive('docs','2026-06-19')", lambda: nom_archive("docs", "2026-06-19"), "docs_2026-06-19.zip")

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
