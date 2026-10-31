#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 10 : fichiers & dossiers

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (lis-les une fois) :
   • Chaque exercice prépare un petit dossier de test (tu VOIS le code qui
     le crée) dans un dossier temporaire — rien n'est touché chez toi.
   • Tu écris ton code dans l'espace « ✏️ ton code ici ».
   • Tu lances le fichier, tu regardes ce qui s'affiche, et tu compares
     avec le « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 Pas de correction automatique : juste toi, du code, et ce qui s'affiche.

 Lancer :   python3 exercices.py
 Cours dans README.md ; corrigé (si vraiment bloqué) dans solutions.py.
"""

from pathlib import Path
import tempfile, json


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Écrire puis relire un fichier
# ══════════════════════════════════════════════════════════════════════
#  On te donne un chemin de fichier (dans un dossier temporaire).
#  Écris le texte "Bonjour" dedans, puis relis-le et affiche-le.
#  Indice : chemin.write_text("...", encoding="utf-8")  pour écrire,
#           chemin.read_text(encoding="utf-8")          pour relire.
#
#  👀 Résultat attendu :
#     Bonjour

chemin = Path(tempfile.mkdtemp()) / "note.txt"

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Lister le contenu d'un dossier (par ordre alphabétique)
# ══════════════════════════════════════════════════════════════════════
#  Le dossier contient 3 fichiers : a.txt, b.txt, c.csv.
#  Affiche la liste de leurs noms, triés par ordre alphabétique.
#  Indice : Path(dossier).iterdir() donne les éléments ; element.name = le nom ;
#           sorted(...) trie.
#
#  👀 Résultat attendu :
#     ['a.txt', 'b.txt', 'c.csv']

dossier = tempfile.mkdtemp()
for nom in ["a.txt", "b.txt", "c.csv"]:
    (Path(dossier) / nom).write_text("x", encoding="utf-8")

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Compter les fichiers par extension
# ══════════════════════════════════════════════════════════════════════
#  Le dossier contient a.txt, b.txt, c.csv.
#  Construis un dictionnaire {extension: nombre} et affiche-le.
#  Indice : element.suffix donne ".txt" ;
#           compteur[ext] = compteur.get(ext, 0) + 1
#
#  👀 Résultat attendu (l'ordre des clés peut varier) :
#     {'.txt': 2, '.csv': 1}

dossier3 = tempfile.mkdtemp()
for nom in ["a.txt", "b.txt", "c.csv"]:
    (Path(dossier3) / nom).write_text("x", encoding="utf-8")

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Sauver un dictionnaire en JSON, puis le relire
# ══════════════════════════════════════════════════════════════════════
#  On te donne un dictionnaire et un chemin de fichier.
#  Écris le dictionnaire en JSON dans le fichier (json.dump), puis relis-le
#  (json.load) et affiche le dictionnaire relu.
#  Indice : with open(chemin_json, "w", encoding="utf-8") as f: json.dump(donnees, f)
#           with open(chemin_json, "r", encoding="utf-8") as f: ... = json.load(f)
#
#  👀 Résultat attendu :
#     {'ville': 'Paris', 'jours': 3}

donnees = {"ville": "Paris", "jours": 3}
chemin_json = Path(tempfile.mkdtemp()) / "data.json"

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — Ne garder que les fichiers .txt
# ══════════════════════════════════════════════════════════════════════
#  Le dossier contient a.txt, b.txt, c.csv.
#  Affiche la liste triée des noms qui se terminent par ".txt".
#  Indice : garde l'élément si  element.suffix == ".txt".
#
#  👀 Résultat attendu :
#     ['a.txt', 'b.txt']

dossier5 = tempfile.mkdtemp()
for nom in ["a.txt", "b.txt", "c.csv"]:
    (Path(dossier5) / nom).write_text("x", encoding="utf-8")

# ✏️ ton code ici :


