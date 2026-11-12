#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Défi 4 : renommer des photos en série

Une solution possible. La tienne peut être différente et tout aussi juste.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé.
"""

from pathlib import Path
import tempfile

# Le dossier de test (créé dans un dossier temporaire).
dossier = Path(tempfile.mkdtemp())
for nom in ["IMG_4821.jpg", "IMG_4822.jpg", "DSC_0007.jpg", "notes.txt"]:
    (dossier / nom).write_text("x", encoding="utf-8")


# ── ÉTAPE 1 — Trouver les photos ─────────────────────────────────────
def photos(dossier):
    """Renvoie la liste triée des noms des fichiers .jpg du dossier."""
    return sorted(e.name for e in dossier.iterdir() if e.suffix == ".jpg")


print(photos(dossier))


# ── ÉTAPE 2 — Préparer le plan, sans rien toucher ────────────────────
def plan_de_renommage(dossier, prefixe):
    """Renvoie une liste de couples (ancien nom, nouveau nom)."""
    plan = []
    numero = 1
    for ancien in photos(dossier):
        nouveau = f"{prefixe}_{numero:03d}.jpg"     # :03d -> le nombre sur 3 chiffres : 001, 002…
        plan.append((ancien, nouveau))
        numero = numero + 1
    return plan


for ancien, nouveau in plan_de_renommage(dossier, "vacances"):
    print(f"{ancien} -> {nouveau}")


# ── ÉTAPE 3 — Appliquer le plan ──────────────────────────────────────
for ancien, nouveau in plan_de_renommage(dossier, "vacances"):
    (dossier / ancien).rename(dossier / nouveau)    # .rename(nouveau_chemin) renomme sur le disque

print(sorted(e.name for e in dossier.iterdir()))


# ── ÉTAPE 4 — En faire un outil, avec un mode simulation ─────────────
def renommer(dossier, prefixe, simulation=True):
    """Affiche le plan ; ne renomme vraiment que si simulation vaut False."""
    for ancien, nouveau in plan_de_renommage(dossier, prefixe):
        print(f"{ancien} -> {nouveau}")
        if not simulation:
            (dossier / ancien).rename(dossier / nouveau)
    if simulation:
        print("Simulation : rien n'a été modifié")


dossier_ete = Path(tempfile.mkdtemp())
for nom in ["b.jpg", "a.jpg"]:
    (dossier_ete / nom).write_text("x", encoding="utf-8")

renommer(dossier_ete, "ete")                        # simulation=True par défaut : le choix prudent
print(sorted(e.name for e in dossier_ete.iterdir()))

# Ce qu'il faut remarquer : on a séparé « décider quoi faire » (le plan) et
# « le faire » (rename). Grâce à ça, on peut MONTRER le plan avant d'agir.
# Tout script qui modifie ou supprime des fichiers devrait avoir un mode
# simulation — et l'avoir activé par défaut.
