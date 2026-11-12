#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 08 : asyncio

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit ta prédiction et essayé.
"""

import asyncio


# ── 👓 LIRE 1 — Qui finit en premier ? ───────────────────────────────
async def tache(nom, duree):
    await asyncio.sleep(duree)      # pendant cette attente, l'autre tâche avance
    print("LIRE 1 →", nom)

async def les_deux():
    await asyncio.gather(tache("lente", 0.2), tache("rapide", 0.1))

asyncio.run(les_deux())
# Réponse : rapide, puis lente.
# gather lance les deux tâches ensemble. L'ordre de LANCEMENT ne compte pas :
# c'est celle qui attend le moins longtemps qui s'affiche d'abord. Et le tout
# dure 0,2 s (la plus longue), pas 0,3 s (la somme) : c'est tout l'intérêt.


# ── 🔧 MODIFIER 1 — L'un après l'autre, ou tous ensemble ? ───────────
async def telecharger(nom):
    await asyncio.sleep(0)
    return f"{nom} ok"

async def tout_telecharger():
    return await asyncio.gather(        # les trois partent en même temps
        telecharger("photo"),
        telecharger("video"),
        telecharger("musique"),
    )
    # gather renvoie les résultats dans l'ordre où on a écrit les appels.

print(asyncio.run(tout_telecharger()))


# ── ✍️ ÉCRIRE 1 — Le carré, version async ────────────────────────────
async def carre_async(n):
    await asyncio.sleep(0)
    return n * n

print(asyncio.run(carre_async(7)))


# ── ✍️ ÉCRIRE 2 — Tous les carrés en même temps ──────────────────────
nombres = [1, 2, 3]

async def tous_les_carres():
    # la compréhension fabrique une coroutine par nombre ; * les déballe pour gather
    return await asyncio.gather(*[carre_async(n) for n in nombres])

print(asyncio.run(tous_les_carres()))
