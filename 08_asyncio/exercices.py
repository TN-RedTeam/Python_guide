#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 08 : asyncio

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE :
   • Tu écris une fonction asynchrone (async def), puis tu la lances
     TOI-MÊME et tu affiches le résultat.
   • Les valeurs d'essai sont écrites dans TON appel — tu les vois.
   • Tu lances le fichier et tu compares l'affichage au « 👀 Résultat
     attendu ».
──────────────────────────────────────────────────────────────────────

 Rappel du cours : dans un « async def », un point d'attente s'écrit
 « await ». Ici, pour simuler une attente (un téléchargement, une
 requête…) sans perdre de temps, on utilise  await asyncio.sleep(0).

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Lancer :   python3 exercices.py
"""

import asyncio


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Ta première coroutine
# ══════════════════════════════════════════════════════════════════════
#  Écris une coroutine  addition_async(a, b)  qui attend un instant
#  (await asyncio.sleep(0)) puis renvoie a + b.
#  Lance-la toi-même avec a=2 et b=3, et affiche le résultat.
#  🧰 Outils : async def, await, asyncio.run
#
#  👀 Résultat attendu :
#     5

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Dire bonjour, version async
# ══════════════════════════════════════════════════════════════════════
#  Écris une coroutine  saluer(nom)  qui attend un instant puis renvoie
#  "Bonjour <nom> !". Lance-la pour "Ada" et affiche le résultat.
#  🧰 Outils : async def, await, une f-string, asyncio.run
#
#  👀 Résultat attendu :
#     Bonjour Ada !

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Tout lancer en même temps (le défi)
# ══════════════════════════════════════════════════════════════════════
#  En réutilisant addition_async de l'exercice 1, lance DEUX additions
#  en même temps — (1, 1) et (10, 5) — et affiche la liste de leurs
#  résultats.
#  🧰 Outils : asyncio.gather, une coroutine « chef d'orchestre », asyncio.run
#
#  👀 Résultat attendu :
#     [2, 15]

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : la fonction commence par « async def » au lieu de « def ».
#               Appeler addition_async(2, 3) ne calcule RIEN : ça fabrique
#               une coroutine. C'est asyncio.run(...) qui l'exécute :
#               print(asyncio.run(addition_async(2, 3)))
#
#  Exercice 2 : exactement le même squelette que l'exercice 1 ; seul le
#               return change.
#
#  Exercice 3 : asyncio.gather(coroutine1, coroutine2) les lance ensemble et
#               renvoie leurs résultats dans l'ordre. Mais gather doit être
#               attendu avec await, et await n'est permis que DANS un
#               async def. Écris donc une petite coroutine (par ex. tout())
#               qui fait  return await asyncio.gather(...), et lance-la
#               avec asyncio.run.
