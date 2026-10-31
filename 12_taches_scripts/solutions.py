#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 12 : scripts réutilisables (argparse)

Le corrigé des exercices de exercices.py, code complet et commenté.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.

Lance-le (python3 solutions.py) : il affiche les résultats attendus.
"""

import argparse


# ── EXERCICE 1 — Construire un nom d'archive ─────────────────────────
source = "docs"
date = "2026-06-19"
print(f"{source}_{date}.zip")


# ── EXERCICE 2 — Un parseur avec une option par défaut ───────────────
parseur = argparse.ArgumentParser(description="Sauvegarde un dossier")
parseur.add_argument("--source", required=True)            # obligatoire
parseur.add_argument("--destination", default="sauvegardes")  # défaut si absent
args = parseur.parse_args(["--source", "docs"])
print(args.source)        # docs
print(args.destination)   # sauvegardes (la valeur par défaut)


# ── EXERCICE 3 — Quand l'option est fournie ──────────────────────────
args2 = parseur.parse_args(["--source", "docs", "--destination", "sav"])
print(args2.source)        # docs
print(args2.destination)   # sav (la valeur donnée remplace le défaut)


# ── EXERCICE 4 — Un drapeau vrai/faux (--verbose) ────────────────────
parseur2 = argparse.ArgumentParser()
parseur2.add_argument("--verbose", action="store_true")   # présent = True
args3 = parseur2.parse_args(["--verbose"])
print(args3.verbose)       # True
