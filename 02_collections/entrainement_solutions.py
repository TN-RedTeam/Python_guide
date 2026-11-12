#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 02 : les collections

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire, ligne par ligne.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit tes prédictions et essayé.
"""


# ── 👓 LIRE 1 — Une liste qu'on modifie ──────────────────────────────
courses = ["pain", "lait", "oeufs"]     # 3 éléments
courses.append("beurre")                # ajoute À LA FIN -> 4 éléments
courses[0] = "baguette"                 # REMPLACE le 1er élément (index 0)
print("LIRE 1 →", len(courses), courses[0], courses[-1])
# Réponse : 4 baguette beurre.
# La liste vaut ["baguette", "lait", "oeufs", "beurre"] ; l'index -1 désigne
# le DERNIER élément.


# ── 👓 LIRE 2 — Un dictionnaire qu'on modifie ────────────────────────
ages = {"Ada": 36, "Bob": 25}           # 2 paires
ages["Bob"] = ages["Bob"] + 1           # la clé existe -> on REMPLACE sa valeur (26)
ages["Zoé"] = 19                        # la clé n'existe pas -> on AJOUTE une paire
print("LIRE 2 →", len(ages), ages["Bob"])
# Réponse : 3 26. La même écriture  d[cle] = valeur  modifie OU ajoute,
# selon que la clé existe déjà ou non.


# ── 🔧 MODIFIER 1 — Des gros fichiers aux petits ─────────────────────
tailles = {"film.mp4": 700, "photo.jpg": 4, "jeu.iso": 2300, "cv.pdf": 1}
for nom, taille in tailles.items():
    if taille < 10:                     # la condition change de sens…
        print(f"{nom} : {taille} Mo")   # …et on affiche aussi la taille


# ── ✍️ ÉCRIRE 1 — Le fichier le plus lourd ───────────────────────────
disque = {"film.mp4": 700, "photo.jpg": 4, "jeu.iso": 2300, "cv.pdf": 1}
plus_lourd = None                       # le nom du champion (aucun au départ)
taille_max = 0                          # sa taille
for nom, taille in disque.items():
    if taille > taille_max:             # ce fichier bat le champion actuel
        taille_max = taille
        plus_lourd = nom
print(plus_lourd)
# Variante courte : print(max(disque, key=disque.get))


# ── ✍️ ÉCRIRE 2 — Les téléchargements en double ──────────────────────
telechargements = ["facture.pdf", "photo.jpg", "facture.pdf", "cv.pdf", "photo.jpg"]
print(len(set(telechargements)))        # set() enlève les doublons ; len() compte


# ── ✍️ ÉCRIRE 3 — Le vote pour le repas d'équipe ─────────────────────
votes = ["pizza", "sushi", "pizza", "tacos", "pizza", "sushi"]
resultats = {}
for plat in votes:
    resultats[plat] = resultats.get(plat, 0) + 1
print(resultats)
