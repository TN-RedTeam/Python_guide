#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 10 : fichiers & dossiers (pathlib, json)

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  lire_ecrire.py  (puis csv_json.py)
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

▶ LANCER LES TESTS :   python3 exercices.py
  Pour chaque ❌, le test affiche ce qu'il ATTENDAIT et ce que TA fonction
  a renvoyé : compare les deux, ton erreur est dans l'écart.

▶ BLOQUÉ ? Réessaie en relisant l'indice écrit dans la fonction. En tout
  dernier recours, ouvre solutions.py (le corrigé commenté).
"""

from pathlib import Path
import json


def lister_noms(dossier):
    """Renvoie la liste TRIÉE des noms de fichiers/dossiers présents dans `dossier`.
    `dossier` est un chemin (str ou Path).
    Ex : si le dossier contient a.txt et b.txt -> ["a.txt", "b.txt"]
    Indice : Path(dossier).iterdir() ; l'attribut .name donne le nom court.
    """
    # TODO : parcours iterdir(), récupère .name, renvoie une liste triée
    ...


def compter_par_extension(dossier):
    """Renvoie un dict {extension: nombre} pour les fichiers de `dossier`.
    Ex : pour a.txt, b.txt, c.csv -> {".txt": 2, ".csv": 1}
    Indice : l'attribut .suffix d'un Path donne l'extension (ex. ".txt").
    """
    # TODO : utilise un dict et .get(ext, 0) + 1
    ...


def sauver_puis_charger_json(chemin, donnees):
    """Écrit `donnees` (un dict) en JSON dans `chemin`, puis le recharge et le renvoie.
    Ex : sauver_puis_charger_json("/tmp/x.json", {"a": 1}) -> {"a": 1}
    Indice : json.dump(obj, fichier) pour écrire, json.load(fichier) pour lire.
    """
    # TODO : un with open(..., "w") + json.dump, puis un with open(..., "r") + json.load
    ...


# ════════════════════════════════════════════════════════════════════
#  Auto-vérification — NE PAS MODIFIER
# ════════════════════════════════════════════════════════════════════
import tempfile
import os


def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Vérification — module 10 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    # Prépare un dossier temporaire avec quelques fichiers
    dossier = tempfile.mkdtemp()
    for nom_fichier in ["a.txt", "b.txt", "c.csv"]:
        Path(dossier, nom_fichier).write_text("x", encoding="utf-8")

    essai("lister_noms(...)", lambda: lister_noms(dossier), ["a.txt", "b.txt", "c.csv"])
    essai("compter_par_extension(...)", lambda: compter_par_extension(dossier), {".txt": 2, ".csv": 1})

    chemin_json = os.path.join(dossier, "data.json")
    essai("sauver_puis_charger_json(...)", lambda: sauver_puis_charger_json(chemin_json, {"a": 1}), {"a": 1})

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
