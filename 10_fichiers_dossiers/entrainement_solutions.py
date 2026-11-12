#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 10 : fichiers & dossiers

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit ta prédiction et essayé.
"""

from pathlib import Path
import tempfile


# ── 👓 LIRE 1 — Découper un chemin ───────────────────────────────────
chemin = Path("documents/2026/rapport_final.pdf")
print("LIRE 1 →", chemin.name, "|", chemin.suffix, "|", chemin.stem, "|", chemin.parent.name)
# Réponse : rapport_final.pdf | .pdf | rapport_final | 2026
#   .name   = le nom complet du fichier (avec l'extension)
#   .suffix = l'extension seule, avec son point
#   .stem   = le nom SANS l'extension
#   .parent = le dossier qui contient le fichier (documents/2026) ; son .name est 2026


# ── 🔧 MODIFIER 1 — N'afficher que les fichiers qui pèsent ───────────
dossier = Path(tempfile.mkdtemp())
(dossier / "notes.txt").write_text("x" * 5, encoding="utf-8")
(dossier / "rapport.txt").write_text("x" * 40, encoding="utf-8")
(dossier / "brouillon.txt").write_text("x" * 12, encoding="utf-8")

for element in sorted(dossier.iterdir()):
    taille = element.stat().st_size         # .stat().st_size = la taille en octets
    if taille > 10:
        print(f"{element.name} : {taille} octets")


# ── ✍️ ÉCRIRE 1 — La taille totale d'un dossier ──────────────────────
dossier_photos = Path(tempfile.mkdtemp())
(dossier_photos / "plage.jpg").write_text("x" * 200, encoding="utf-8")
(dossier_photos / "chat.jpg").write_text("x" * 150, encoding="utf-8")

total = 0
for element in dossier_photos.iterdir():
    total = total + element.stat().st_size  # le pattern accumulateur, sur des tailles
print(total)
# Variante courte : print(sum(e.stat().st_size for e in dossier_photos.iterdir()))


# ── ✍️ ÉCRIRE 2 — Ce fichier existe-t-il ? ───────────────────────────
a_verifier = ["plage.jpg", "montagne.jpg"]
for nom in a_verifier:
    if (dossier_photos / nom).exists():     # dossier / nom fabrique le chemin complet
        print(f"{nom} : présent")
    else:
        print(f"{nom} : absent")
