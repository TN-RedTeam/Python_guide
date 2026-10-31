#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 02 : les collections

Le corrigé des exercices, avec le code complet et commenté.
Lance-le (python3 solutions.py) pour voir tous les résultats attendus.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""


# ── EXERCICE 1 — Le 2e fichier de la liste ───────────────────────────
fichiers = ["rapport.pdf", "photo.jpg", "notes.txt"]
print(fichiers[1])            # index 1 = le 2e élément (on compte à partir de 0)


# ── EXERCICE 2 — La taille totale du dossier ─────────────────────────
tailles_mo = {"film.mp4": 700, "photo.jpg": 4, "cv.pdf": 1}
print(sum(tailles_mo.values()))   # .values() -> 700, 4, 1 ; sum les additionne -> 705


# ── EXERCICE 3 — Compter les photos (.jpg) ───────────────────────────
fichiers = ["vacances.jpg", "cv.pdf", "chat.jpg", "notes.txt", "profil.jpg"]
compteur = 0
for nom in fichiers:
    if nom.endswith(".jpg"):      # .endswith(...) : True si le nom finit par ".jpg"
        compteur = compteur + 1
print(compteur)                   # 3
# Variante courte : print(sum(1 for n in fichiers if n.endswith(".jpg")))


# ── EXERCICE 4 — Trouver les fichiers vides ──────────────────────────
tailles = {"notes.txt": 12, "vide.txt": 0, "temp.log": 0}
for nom, taille in tailles.items():   # .items() donne (nom, taille)
    if taille == 0:
        print(nom)                     # vide.txt, puis temp.log


# ── EXERCICE 5 — Les types de fichiers présents ──────────────────────
extensions = [".jpg", ".txt", ".jpg", ".pdf", ".txt"]
print(sorted(set(extensions)))    # set() enlève les doublons, sorted() trie -> ['.jpg', '.pdf', '.txt']


# ── EXERCICE 6 — Combien de fichiers par type ? ──────────────────────
extensions = [".jpg", ".txt", ".jpg"]
compteur_types = {}
for ext in extensions:
    compteur_types[ext] = compteur_types.get(ext, 0) + 1
print(compteur_types)             # {'.jpg': 2, '.txt': 1}
# .get(ext, 0) : le compte actuel de ce type, ou 0 si on le voit pour la 1re fois.
