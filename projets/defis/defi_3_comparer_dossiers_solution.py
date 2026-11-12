#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Défi 3 : comparer deux dossiers

Une solution possible. La tienne peut être différente et tout aussi juste.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé.
"""

from pathlib import Path
import shutil
import tempfile

# Les deux dossiers de test (créés dans un dossier temporaire).
racine = Path(tempfile.mkdtemp())
original = racine / "original"
sauvegarde = racine / "sauvegarde"
original.mkdir()
sauvegarde.mkdir()

for nom, taille in [("rapport.docx", 300), ("budget.xlsx", 120), ("photo.jpg", 500), ("notes.txt", 40)]:
    (original / nom).write_text("x" * taille, encoding="utf-8")
for nom, taille in [("rapport.docx", 300), ("budget.xlsx", 90), ("photo.jpg", 500), ("vieux.txt", 10)]:
    (sauvegarde / nom).write_text("x" * taille, encoding="utf-8")


# ── ÉTAPE 1 — Lister les deux dossiers ───────────────────────────────
def noms(dossier):
    """Renvoie la liste triée des noms de fichiers d'un dossier."""
    return sorted(element.name for element in dossier.iterdir())


print("original :", noms(original))
print("sauvegarde :", noms(sauvegarde))


# ── ÉTAPE 2 — Ce qui manque, ce qui est en trop ──────────────────────
def manquants(original, sauvegarde):
    # ensemble A - ensemble B = ce qui est dans A mais PAS dans B
    return sorted(set(noms(original)) - set(noms(sauvegarde)))


def en_trop(original, sauvegarde):
    return sorted(set(noms(sauvegarde)) - set(noms(original)))


print("Manquants :", manquants(original, sauvegarde))
print("En trop :", en_trop(original, sauvegarde))


# ── ÉTAPE 3 — Les fichiers modifiés ──────────────────────────────────
def modifies(original, sauvegarde):
    communs = set(noms(original)) & set(noms(sauvegarde))    # & = présents des DEUX côtés
    differents = []
    for nom in communs:
        taille_original = (original / nom).stat().st_size
        taille_sauvegarde = (sauvegarde / nom).stat().st_size
        if taille_original != taille_sauvegarde:
            differents.append(nom)
    return sorted(differents)


print("Modifiés :", modifies(original, sauvegarde))


# ── ÉTAPE 4 — Le verdict ─────────────────────────────────────────────
def verdict(original, sauvegarde):
    nb_manquants = len(manquants(original, sauvegarde))
    nb_modifies = len(modifies(original, sauvegarde))
    if nb_manquants == 0 and nb_modifies == 0:
        return "Sauvegarde à jour"
    return f"Sauvegarde PAS à jour : {nb_manquants} manquant(s), {nb_modifies} modifié(s)"


print(verdict(original, sauvegarde))


# ── ÉTAPE 5 — Réparer la sauvegarde ──────────────────────────────────
def reparer(original, sauvegarde):
    # un fichier manquant et un fichier modifié se réparent pareil : on recopie l'original
    a_copier = manquants(original, sauvegarde) + modifies(original, sauvegarde)
    for nom in a_copier:
        shutil.copy(original / nom, sauvegarde / nom)    # copie (et écrase s'il existe déjà)


reparer(original, sauvegarde)
print(verdict(original, sauvegarde))

# Ce qu'il faut remarquer : comparer deux dossiers, c'est comparer deux
# ENSEMBLES de noms. Les opérations sur les sets (- et &) font en une ligne
# ce qui demanderait deux boucles imbriquées avec des listes.
# Limite assumée : on compare les TAILLES. Deux fichiers de même taille mais
# de contenu différent passeraient inaperçus ; les vrais outils comparent une
# empreinte du contenu (voir hashlib).
