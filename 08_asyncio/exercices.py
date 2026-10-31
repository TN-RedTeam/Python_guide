#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 08 : asyncio

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE :
   • Tu écris une fonction asynchrone (async def), puis tu la lances
     TOI-MÊME avec asyncio.run(...) et tu affiches le résultat.
   • Les valeurs d'essai sont écrites dans TON appel — tu les vois.
   • Tu lances le fichier et tu compares l'affichage au « 👀 Résultat
     attendu ». Pas de correction automatique.
──────────────────────────────────────────────────────────────────────

 Rappel : à l'intérieur d'un « async def », un point d'attente s'écrit
 « await » (ex. await asyncio.sleep(0)). On démarre une coroutine depuis
 le dehors avec asyncio.run(ma_coroutine(...)).

 Lancer :   python3 exercices.py        Corrigé :  solutions.py
"""

import asyncio


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Ta première coroutine
# ══════════════════════════════════════════════════════════════════════
#  Écris une fonction  async def addition_async(a, b)  qui :
#     1. attend un instant :  await asyncio.sleep(0)
#     2. puis renvoie a + b
#  Lance-la toi-même et affiche le résultat pour a=2, b=3 :
#     print(asyncio.run(addition_async(2, 3)))
#
#  👀 Résultat attendu :
#     5

# ✏️ ton code ici (la fonction async, puis le print avec asyncio.run) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Dire bonjour, version async
# ══════════════════════════════════════════════════════════════════════
#  Écris  async def saluer(nom)  qui attend (await asyncio.sleep(0)) puis
#  renvoie la chaîne  "Bonjour <nom> !".
#  Lance-la pour nom="Ada" et affiche le résultat.
#
#  👀 Résultat attendu :
#     Bonjour Ada !

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Tout lancer en même temps (gather)
# ══════════════════════════════════════════════════════════════════════
#  En réutilisant addition_async de l'exercice 1, lance DEUX additions
#  ensemble et récupère leurs résultats dans l'ordre.
#  Indice : asyncio.gather(*coroutines) lance tout en parallèle ; le `*`
#  déballe la liste. Il faut l'attendre avec await, donc mets ça dans une
#  petite coroutine que tu lances avec asyncio.run.
#
#     async def tout():
#         return await asyncio.gather(addition_async(1, 1), addition_async(10, 5))
#     print(asyncio.run(tout()))
#
#  👀 Résultat attendu :
#     [2, 15]

# ✏️ ton code ici :


