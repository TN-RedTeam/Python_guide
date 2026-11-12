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

 La ligne « 🧰 Outils » te dit QUOI utiliser, pas comment l'écrire.

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Lancer :   python3 exercices.py
"""

from pathlib import Path
import tempfile, json


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Écrire puis relire un fichier
# ══════════════════════════════════════════════════════════════════════
#  chemin  désigne un fichier (dans un dossier temporaire).
#  Écris le texte "Bonjour" dedans, puis relis-le et affiche-le.
#  🧰 Outils : les méthodes .write_text et .read_text d'un Path
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
#  🧰 Outils : Path(...).iterdir(), l'attribut .name, sorted
#
#  💡 Sur ton PC : remplace  dossier  par un vrai chemin, ex.
#     dossier = "/home/toi/Documents" (ou "C:/Users/Toi/Documents"), pour
#     lister TES propres fichiers.
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
#  Construis un dictionnaire {extension: nombre de fichiers} et affiche-le.
#  🧰 Outils : .iterdir(), l'attribut .suffix, un dictionnaire, .get()
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
#  Écris le dictionnaire  donnees  en JSON dans le fichier  chemin_json,
#  puis relis ce fichier et affiche le dictionnaire relu.
#  🧰 Outils : with open(...), json.dump, json.load
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
#  Affiche la liste triée des noms des fichiers ".txt" uniquement.
#  🧰 Outils : .iterdir(), .suffix, .name, sorted (et une compréhension)
#
#  💡 Sur ton PC : pointe  dossier5  vers un vrai dossier pour retrouver, par
#     exemple, tous tes .pdf ou tes .jpg (change ".txt" par l'extension voulue).
#
#  👀 Résultat attendu :
#     ['a.txt', 'b.txt']

dossier5 = tempfile.mkdtemp()
for nom in ["a.txt", "b.txt", "c.csv"]:
    (Path(dossier5) / nom).write_text("x", encoding="utf-8")

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : chemin.write_text("...", encoding="utf-8") écrit ;
#               chemin.read_text(encoding="utf-8") renvoie le contenu.
#
#  Exercice 2 : Path(dossier).iterdir() donne chaque élément du dossier.
#               Pour chacun, element.name est son nom. Construis la liste
#               des noms, puis passe-la à sorted(...).
#
#  Exercice 3 : c'est le compteur par dictionnaire du module 02 : pour
#               chaque élément, ext = element.suffix, puis
#               compteur[ext] = compteur.get(ext, 0) + 1.
#
#  Exercice 4 : écrire :  with open(chemin_json, "w", encoding="utf-8") as f:
#               puis json.dump(donnees, f).  Relire : ouvre en "r" et
#               récupère le résultat de json.load(f).
#
#  Exercice 5 : comme l'exercice 2, avec un filtre : ne garde l'élément que
#               si element.suffix == ".txt".
