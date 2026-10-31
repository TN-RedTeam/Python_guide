#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 10 : fichiers & dossiers

Le corrigé des exercices de exercices.py, code complet et commenté.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.

Lance-le (python3 solutions.py) : il affiche les résultats attendus.
Compare-les à ce que TON code produit.
"""

from pathlib import Path
import tempfile, json


# ── EXERCICE 1 — Écrire puis relire un fichier ───────────────────────
chemin = Path(tempfile.mkdtemp()) / "note.txt"
chemin.write_text("Bonjour", encoding="utf-8")   # écrit le texte dans le fichier
print(chemin.read_text(encoding="utf-8"))        # relit tout le fichier


# ── EXERCICE 2 — Lister le contenu d'un dossier ──────────────────────
dossier = tempfile.mkdtemp()
for nom in ["a.txt", "b.txt", "c.csv"]:
    (Path(dossier) / nom).write_text("x", encoding="utf-8")
print(sorted(e.name for e in Path(dossier).iterdir()))
# iterdir() liste les éléments ; e.name = le nom ; sorted() trie.


# ── EXERCICE 3 — Compter les fichiers par extension ──────────────────
dossier3 = tempfile.mkdtemp()
for nom in ["a.txt", "b.txt", "c.csv"]:
    (Path(dossier3) / nom).write_text("x", encoding="utf-8")
compteur = {}
for e in Path(dossier3).iterdir():
    if e.is_file():                                # on ignore les sous-dossiers
        compteur[e.suffix] = compteur.get(e.suffix, 0) + 1   # +1, ou 1 si nouveau
print(compteur)


# ── EXERCICE 4 — Sauver en JSON puis relire ──────────────────────────
donnees = {"ville": "Paris", "jours": 3}
chemin_json = Path(tempfile.mkdtemp()) / "data.json"
with open(chemin_json, "w", encoding="utf-8") as f:
    json.dump(donnees, f)        # dict Python → texte JSON dans le fichier
with open(chemin_json, "r", encoding="utf-8") as f:
    print(json.load(f))          # texte JSON → dict Python


# ── EXERCICE 5 — Ne garder que les .txt ──────────────────────────────
dossier5 = tempfile.mkdtemp()
for nom in ["a.txt", "b.txt", "c.csv"]:
    (Path(dossier5) / nom).write_text("x", encoding="utf-8")
print(sorted(e.name for e in Path(dossier5).iterdir() if e.suffix == ".txt"))
