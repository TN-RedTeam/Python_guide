#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 08 : asyncio

Lance :   python3 solutions.py   (affiche les résultats attendus).
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""

import asyncio


# ── EXERCICE 1 — ta première coroutine ───────────────────────────────
async def addition_async(a, b):
    await asyncio.sleep(0)      # point d'attente : rend la main à la boucle d'événements
    return a + b

print(asyncio.run(addition_async(2, 3)))          # 5


# ── EXERCICE 2 — dire bonjour, version async ─────────────────────────
async def saluer(nom):
    await asyncio.sleep(0)
    return f"Bonjour {nom} !"

print(asyncio.run(saluer("Ada")))                 # Bonjour Ada !


# ── EXERCICE 3 — tout lancer en même temps (gather) ──────────────────
async def tout():
    # gather lance les deux coroutines ensemble et renvoie leurs résultats dans l'ordre
    return await asyncio.gather(addition_async(1, 1), addition_async(10, 5))

print(asyncio.run(tout()))                        # [2, 15]
