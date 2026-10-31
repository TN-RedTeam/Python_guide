#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 06 : itérateurs & générateurs

Le corrigé des exercices, avec le code complet et commenté.
Lance-le (python3 solutions.py) pour voir tous les résultats attendus.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""


# ── EXERCICE 1 — Garder seulement les photos ─────────────────────────
fichiers = ["vacances.jpg", "cv.pdf", "chat.jpg", "notes.txt"]
print([f for f in fichiers if f.endswith(".jpg")])   # ['vacances.jpg', 'chat.jpg']
# Lecture : [ ce qu'on garde  for f in source  if condition ]


# ── EXERCICE 2 — Normaliser des noms de fichiers ─────────────────────
noms = ["Rapport.PDF", "CV.Pdf"]
print([nom.lower() for nom in noms])                 # ['rapport.pdf', 'cv.pdf']


# ── EXERCICE 3 — Taille totale des gros fichiers ─────────────────────
tailles = [120, 4, 700, 12]
print(sum(t for t in tailles if t > 10))             # 120 + 700 + 12 -> 832
# Les parenthèses (au lieu de crochets) créent un générateur : aucune liste
# n'est construite, sum additionne au fur et à mesure, en ignorant le 4.


# ── EXERCICE 4 — Lire les lignes non vides (générateur) ──────────────
def lignes_utiles(texte):
    for ligne in texte.splitlines():   # découpe en lignes : ['achat lait', '', 'achat pain']
        if ligne.strip():              # ignore les lignes vides
            yield ligne                # livre la ligne, se met en pause, reprend ensuite

texte = "achat lait\n\nachat pain\n"
print(list(lignes_utiles(texte)))      # ['achat lait', 'achat pain']
# list(...) déroule le générateur jusqu'au bout pour tout afficher.
