#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 12 : scripts réutilisables

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit ta prédiction et essayé.
"""

import argparse


# ── 👓 LIRE 1 — Valeur par défaut et type ────────────────────────────
parseur = argparse.ArgumentParser()
parseur.add_argument("--dossier", default="Documents")
parseur.add_argument("--copies", type=int, default=1)
args = parseur.parse_args(["--copies", "3"])
print("LIRE 1 →", args.dossier, args.copies + 1)
# Réponse : Documents 4.
#   --dossier n'est pas dans la liste -> on obtient sa valeur par défaut.
#   --copies vaut "3" dans la liste, mais type=int le convertit en nombre 3 :
#   3 + 1 = 4. SANS type=int, on aurait le texte "3", et "3" + 1 planterait.
#   Tout ce qui vient de la ligne de commande est du texte, sauf si on précise type=.


# ── 🔧 MODIFIER 1 — Ajouter un interrupteur ──────────────────────────
sauvegarde = argparse.ArgumentParser()
sauvegarde.add_argument("--source", required=True)
sauvegarde.add_argument("--compresser", action="store_true")    # un interrupteur, sans valeur
options = sauvegarde.parse_args(["--source", "photos", "--compresser"])

message = f"Sauvegarde de {options.source}"
if options.compresser:              # True parce que --compresser est dans la liste
    message = message + " (compressée)"
print(message)


# ── ✍️ ÉCRIRE 1 — Un script qui calcule avec ses options ─────────────
arguments_1 = ["--nom", "Ada", "--age", "36"]
parseur_1 = argparse.ArgumentParser()
parseur_1.add_argument("--nom", required=True)
parseur_1.add_argument("--age", type=int, default=18)   # type=int : indispensable pour calculer
args_1 = parseur_1.parse_args(arguments_1)
print(f"{args_1.nom} aura {args_1.age + 1} ans l'an prochain")


# ── ✍️ ÉCRIRE 2 — Un générateur de noms de fichiers ──────────────────
arguments_2 = ["--prefixe", "vacances"]
parseur_2 = argparse.ArgumentParser()
parseur_2.add_argument("--prefixe", default="photo")
parseur_2.add_argument("--nombre", type=int, default=3)
args_2 = parseur_2.parse_args(arguments_2)
for numero in range(1, args_2.nombre + 1):      # --nombre absent -> 3 -> 1, 2, 3
    print(f"{args_2.prefixe}_{numero}.jpg")
