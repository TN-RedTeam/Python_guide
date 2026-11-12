#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 12 : scripts réutilisables (argparse)

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (lis-les une fois) :
   • Les valeurs de départ sont ÉCRITES, tu les VOIS.
   • Tu écris ton code dans l'espace « ✏️ ton code ici ».
   • Tu lances, tu regardes l'affichage, tu compares au « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 Note : argparse lit normalement les arguments tapés dans le terminal
 (python3 sauvegarde.py --source docs). Ici, pour tester facilement, on
 lui donne nous-mêmes la liste d'arguments (visible) :
     args = parseur.parse_args(arguments)

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Lancer :   python3 exercices.py
"""

import argparse


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Construire un nom d'archive
# ══════════════════════════════════════════════════════════════════════
#  Un script de sauvegarde nomme ses archives  <source>_<date>.zip.
#  Affiche le nom d'archive pour la source et la date données.
#  🧰 Outils : une f-string
#
#  👀 Résultat attendu :
#     docs_2026-06-19.zip

source = "docs"
date = "2026-06-19"

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Un parseur avec une option par défaut
# ══════════════════════════════════════════════════════════════════════
#  Crée un parseur qui accepte deux options :
#     --source       obligatoire
#     --destination  facultative, qui vaut "sauvegardes" si on ne la donne pas
#  Fais-lui lire la liste  arguments  (où --destination est ABSENTE), puis
#  affiche la source PUIS la destination.
#  🧰 Outils : argparse.ArgumentParser, .add_argument (required, default),
#              .parse_args
#
#  👀 Résultat attendu :
#     docs
#     sauvegardes

arguments = ["--source", "docs"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Quand l'option est fournie
# ══════════════════════════════════════════════════════════════════════
#  Même parseur, mais cette fois la liste  arguments2  donne --destination.
#  Affiche la source PUIS la destination.
#  🧰 Outils : les mêmes qu'à l'exercice 2
#
#  👀 Résultat attendu :
#     docs
#     sav

arguments2 = ["--source", "docs", "--destination", "sav"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Un interrupteur vrai/faux (--verbose)
# ══════════════════════════════════════════════════════════════════════
#  Crée un parseur avec une option  --verbose  qui est un simple
#  interrupteur : présente -> True, absente -> False (elle ne prend pas
#  de valeur). Fais-lui lire  arguments3  et affiche la valeur de verbose.
#  🧰 Outils : .add_argument avec action="store_true"
#
#  👀 Résultat attendu :
#     True

arguments3 = ["--verbose"]

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : f"{source}_{date}.zip"… il ne reste qu'à l'afficher.
#
#  Exercice 2 : parseur = argparse.ArgumentParser()
#               parseur.add_argument("--source", required=True)
#               parseur.add_argument("--destination", default="sauvegardes")
#               Puis args = parseur.parse_args(arguments) ; les valeurs se
#               lisent avec args.source et args.destination.
#
#  Exercice 3 : tu peux réutiliser le parseur de l'exercice 2 tel quel :
#               seule la liste passée à parse_args change.
#
#  Exercice 4 : un NOUVEAU parseur, avec
#               add_argument("--verbose", action="store_true").
#               La valeur se lit avec args.verbose.
