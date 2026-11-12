#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 10 : fichiers & dossiers   (série 2, après exercices.py)

──────────────────────────────────────────────────────────────────────
 Trois façons de travailler la même matière :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier.
   🔧 MODIFIER  : un petit script qui marche déjà. Change-le pour
                 obtenir le nouveau résultat demandé.
   ✍️ ÉCRIRE    : comme dans exercices.py, mais sans indice ni liste
                 d'outils.
──────────────────────────────────────────────────────────────────────

 Les dossiers de test sont créés dans un dossier temporaire (tu vois le
 code qui les fabrique) : rien n'est touché chez toi.

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""

from pathlib import Path
import tempfile


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Découper un chemin
# ══════════════════════════════════════════════════════════════════════
#  Quatre morceaux du chemin sont affichés, séparés par des « | ».
#  (Ce fichier n'a pas besoin d'exister : on ne fait que lire le chemin.)
#  ✏️ ma prédiction :

chemin = Path("documents/2026/rapport_final.pdf")
print("LIRE 1 →", chemin.name, "|", chemin.suffix, "|", chemin.stem, "|", chemin.parent.name)


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — N'afficher que les fichiers qui pèsent
# ══════════════════════════════════════════════════════════════════════
#  Ce script crée 3 fichiers puis affiche leurs noms. Modifie la boucle
#  pour n'afficher que les fichiers de PLUS de 10 octets, avec leur taille.
#
#  👀 Résultat attendu APRÈS ta modification :
#     brouillon.txt : 12 octets
#     rapport.txt : 40 octets

dossier = Path(tempfile.mkdtemp())
(dossier / "notes.txt").write_text("x" * 5, encoding="utf-8")
(dossier / "rapport.txt").write_text("x" * 40, encoding="utf-8")
(dossier / "brouillon.txt").write_text("x" * 12, encoding="utf-8")

for element in sorted(dossier.iterdir()):
    print(element.name)


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — La taille totale d'un dossier
# ══════════════════════════════════════════════════════════════════════
#  Affiche la taille totale (en octets) des fichiers de  dossier_photos.
#
#  💡 Sur ton PC : remplace dossier_photos par Path("/home/toi/Images")
#     pour connaître le poids de TES photos.
#
#  👀 Résultat attendu :
#     350

dossier_photos = Path(tempfile.mkdtemp())
(dossier_photos / "plage.jpg").write_text("x" * 200, encoding="utf-8")
(dossier_photos / "chat.jpg").write_text("x" * 150, encoding="utf-8")

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — Ce fichier existe-t-il ?
# ══════════════════════════════════════════════════════════════════════
#  Pour chaque nom de la liste  a_verifier, affiche s'il est présent ou
#  absent dans  dossier_photos  (le dossier de l'exercice précédent).
#
#  👀 Résultat attendu :
#     plage.jpg : présent
#     montagne.jpg : absent

a_verifier = ["plage.jpg", "montagne.jpg"]

# ✏️ ton code ici :

