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

from pathlib import Path
import json


def lister_noms(dossier):
    """OBJECTIF : renvoyer la liste TRIÉE des noms des fichiers/dossiers présents
    dans `dossier` (un chemin, str ou Path).

    Exemple : si le dossier contient a.txt et b.txt  ->  ["a.txt", "b.txt"]

    Comment t'y prendre :
      1. Path(dossier).iterdir() donne chaque élément du dossier (un Path) ;
      2. l'attribut .name donne le nom court (ex. "a.txt") ;
      3. construis la liste des .name, puis renvoie-la triée avec sorted(...).
    """
    ...   # ⬅️ remplace cette ligne par ton code


def compter_par_extension(dossier):
    """OBJECTIF : renvoyer un dict {extension: nombre} comptant les fichiers de
    `dossier` par extension.

    Exemple : pour a.txt, b.txt, c.csv  ->  {".txt": 2, ".csv": 1}

    Comment t'y prendre :
      1. crée un dict vide : compte = {} ;
      2. parcours Path(dossier).iterdir() ; l'attribut .suffix donne l'extension (".txt") ;
      3. incrémente : compte[ext] = compte.get(ext, 0) + 1
         (.get(ext, 0) renvoie 0 si l'extension n'a pas encore été vue) ;
      4. renvoie compte.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def sauver_puis_charger_json(chemin, donnees):
    """OBJECTIF : écrire `donnees` (un dict) au format JSON dans `chemin`, puis
    le recharger depuis le fichier et le renvoyer.

    Exemple : sauver_puis_charger_json("/tmp/x.json", {"a": 1})  ->  {"a": 1}

    Comment t'y prendre :
      1. ÉCRIRE : with open(chemin, "w", encoding="utf-8") as f:  puis  json.dump(donnees, f) ;
      2. LIRE   : with open(chemin, "r", encoding="utf-8") as f:  puis  resultat = json.load(f) ;
      3. renvoie resultat.
    """
    ...   # ⬅️ remplace cette ligne par ton code


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
