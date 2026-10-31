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

 Note : argparse lit normalement les arguments tapés dans le terminal.
 Ici, pour tester facilement, on lui donne nous-mêmes une liste d'arguments
 (visible) avec  parse_args([...]).

 Lancer :   python3 exercices.py
 Cours dans README.md ; corrigé dans solutions.py.
"""

import argparse


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Construire un nom d'archive
# ══════════════════════════════════════════════════════════════════════
#  On te donne un nom de source et une date.
#  Affiche le nom d'archive sous la forme  <source>_<date>.zip
#
#  👀 Résultat attendu :
#     docs_2026-06-19.zip

source = "docs"
date = "2026-06-19"

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Un parseur avec une option par défaut
# ══════════════════════════════════════════════════════════════════════
#  Crée un ArgumentParser avec :
#     --source       (obligatoire : required=True)
#     --destination  (valeur par défaut : "sauvegardes")
#  Teste-le avec la liste d'arguments ci-dessous (--destination est ABSENT)
#  et affiche la source PUIS la destination.
#  Indice : args = parseur.parse_args(arguments)  puis  args.source, args.destination
#
#  👀 Résultat attendu :
#     docs
#     sauvegardes

arguments = ["--source", "docs"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Quand l'option est fournie
# ══════════════════════════════════════════════════════════════════════
#  Reprends le même genre de parseur, mais cette fois --destination est donnée.
#  Affiche la source PUIS la destination.
#
#  👀 Résultat attendu :
#     docs
#     sav

arguments2 = ["--source", "docs", "--destination", "sav"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Un drapeau vrai/faux (--verbose)
# ══════════════════════════════════════════════════════════════════════
#  Crée un parseur avec une option --verbose qui est un simple interrupteur
#  (action="store_true" : présent = True, absent = False).
#  Teste avec la liste ci-dessous et affiche la valeur de verbose.
#
#  👀 Résultat attendu :
#     True

arguments3 = ["--verbose"]

# ✏️ ton code ici :


