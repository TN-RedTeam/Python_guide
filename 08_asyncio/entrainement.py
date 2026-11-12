#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 08 : asyncio   (série 2, après exercices.py)

──────────────────────────────────────────────────────────────────────
 Trois façons de travailler la même matière :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier.
   🔧 MODIFIER  : un petit script qui marche déjà. Change-le pour
                 obtenir le nouveau résultat demandé.
   ✍️ ÉCRIRE    : comme dans exercices.py, mais sans indice ni liste
                 d'outils.
──────────────────────────────────────────────────────────────────────

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""

import asyncio


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Qui finit en premier ?
# ══════════════════════════════════════════════════════════════════════
#  Deux tâches sont lancées EN MÊME TEMPS. « lente » est lancée la première
#  mais attend 0,2 seconde ; « rapide » attend 0,1 seconde.
#  Dans quel ordre leurs noms s'affichent-ils ?
#  ✏️ ma prédiction :

async def tache(nom, duree):
    await asyncio.sleep(duree)
    print("LIRE 1 →", nom)

async def les_deux():
    await asyncio.gather(tache("lente", 0.2), tache("rapide", 0.1))

asyncio.run(les_deux())


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — L'un après l'autre, ou tous ensemble ?
# ══════════════════════════════════════════════════════════════════════
#  Ce script « télécharge » deux fichiers L'UN APRÈS L'AUTRE. Modifie la
#  coroutine  tout_telecharger  pour lancer les téléchargements EN MÊME
#  TEMPS, et ajoutes-en un troisième : "musique".
#
#  👀 Résultat attendu APRÈS ta modification :
#     ['photo ok', 'video ok', 'musique ok']

async def telecharger(nom):
    await asyncio.sleep(0)
    return f"{nom} ok"

async def tout_telecharger():
    a = await telecharger("photo")
    b = await telecharger("video")
    return [a, b]

print(asyncio.run(tout_telecharger()))


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — Le carré, version async
# ══════════════════════════════════════════════════════════════════════
#  Écris une coroutine  carre_async(n)  qui attend un instant puis renvoie
#  n au carré. Lance-la pour n = 7 et affiche le résultat.
#
#  👀 Résultat attendu :
#     49

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — Tous les carrés en même temps
# ══════════════════════════════════════════════════════════════════════
#  En réutilisant carre_async, calcule EN MÊME TEMPS le carré de chaque
#  nombre de la liste  nombres, et affiche la liste des résultats.
#
#  👀 Résultat attendu :
#     [1, 4, 9]

nombres = [1, 2, 3]

# ✏️ ton code ici :

