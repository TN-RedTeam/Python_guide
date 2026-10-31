#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 14 : les bibliothèques

Le corrigé des exercices, en code complet et commenté.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.

Lance-le (python3 solutions.py) : il affiche les résultats attendus.
"""


# ── EXERCICE 1 — Importer et utiliser math ───────────────────────────
import math
print(math.sqrt(16))              # 4.0
# import math  charge TOUT le module ; on accède au contenu avec math.xxx


# ── EXERCICE 2 — Importer juste une fonction ─────────────────────────
from statistics import mean
notes = [10, 20, 30]
print(mean(notes))                # 20
# from … import mean  amène SEULEMENT mean dans ton code (pas besoin de statistics.mean)


# ── EXERCICE 3 — Renommer un module (import … as) ────────────────────
import random as rnd
rnd.seed(0)                       # fixe le hasard -> résultat reproductible
print(rnd.randint(1, 6))          # 4  (toujours 4 grâce à seed(0))
# "as rnd" donne un surnom plus court au module (comme numpy as np plus tard)


# ── EXERCICE 4 — Ligne de requirements.txt ───────────────────────────
paquet = "requests"
version = "2.31.0"
print(f"{paquet}=={version}")     # requests==2.31.0
# Le == fige la version : tout le monde installe EXACTEMENT la même.
