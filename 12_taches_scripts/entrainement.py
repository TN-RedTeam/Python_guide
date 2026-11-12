#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 12 : scripts réutilisables   (série 2, après exercices.py)

──────────────────────────────────────────────────────────────────────
 Trois façons de travailler la même matière :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier.
   🔧 MODIFIER  : un petit script qui marche déjà. Change-le pour
                 obtenir le nouveau résultat demandé.
   ✍️ ÉCRIRE    : comme dans exercices.py, mais sans indice ni liste
                 d'outils.
──────────────────────────────────────────────────────────────────────

 Comme dans les exercices : on donne nous-mêmes la liste d'arguments à
 parse_args([...]), au lieu de la taper dans le terminal.

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""

import argparse


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Valeur par défaut et type
# ══════════════════════════════════════════════════════════════════════
#  Deux options, une seule est donnée dans la liste d'arguments.
#  Deux valeurs sont affichées : lesquelles ?
#  ✏️ ma prédiction :

parseur = argparse.ArgumentParser()
parseur.add_argument("--dossier", default="Documents")
parseur.add_argument("--copies", type=int, default=1)
args = parseur.parse_args(["--copies", "3"])
print("LIRE 1 →", args.dossier, args.copies + 1)


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — Ajouter un interrupteur
# ══════════════════════════════════════════════════════════════════════
#  Ce script de sauvegarde n'a qu'une option. Ajoute-lui un interrupteur
#  --compresser  (présent = True, absent = False), active-le dans la liste
#  d'arguments, et fais en sorte que le message se termine par
#  " (compressée)" quand il est activé.
#
#  👀 Résultat attendu APRÈS ta modification :
#     Sauvegarde de photos (compressée)

sauvegarde = argparse.ArgumentParser()
sauvegarde.add_argument("--source", required=True)
options = sauvegarde.parse_args(["--source", "photos"])
print(f"Sauvegarde de {options.source}")


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — Un script qui calcule avec ses options
# ══════════════════════════════════════════════════════════════════════
#  Crée un parseur avec  --nom  (obligatoire) et  --age  (un nombre
#  ENTIER, 18 par défaut). Fais-lui lire  arguments_1  et affiche la
#  phrase ci-dessous (l'âge affiché est l'âge de l'an prochain).
#
#  👀 Résultat attendu :
#     Ada aura 37 ans l'an prochain

arguments_1 = ["--nom", "Ada", "--age", "36"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — Un générateur de noms de fichiers
# ══════════════════════════════════════════════════════════════════════
#  Crée un parseur avec  --prefixe  ("photo" par défaut) et  --nombre
#  (un entier, 3 par défaut). Fais-lui lire  arguments_2  puis affiche
#  les noms de fichiers numérotés à partir de 1, un par ligne.
#
#  👀 Résultat attendu :
#     vacances_1.jpg
#     vacances_2.jpg
#     vacances_3.jpg

arguments_2 = ["--prefixe", "vacances"]

# ✏️ ton code ici :

