#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 04 : exceptions & fichiers

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE :
   • Les valeurs de départ sont ÉCRITES et VISIBLES (un montant, une
     saisie, un nom de fichier). Rien n'est caché.
   • Tu écris ton code dans l'espace prévu, puis tu affiches le résultat.
   • Tu lances, tu compares l'affichage au « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 Les notes « 💡 Sur ton PC » montrent comment faire la même chose sur tes
 vrais fichiers. Les exercices sur les fichiers créent un petit fichier
 dans le dossier courant (tu peux le supprimer après).

 Lancer :   python3 exercices.py
 Cours : README.md • Corrigé : solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Partager l'addition sans planter (try / except)
# ══════════════════════════════════════════════════════════════════════
#  Une addition de  addition  euros est partagée entre  convives  personnes.
#  Affiche le prix par personne (addition / convives). Mais si convives vaut 0,
#  affiche  None  au lieu de laisser le programme planter (division par zéro).
#  Indice :  try:  ... addition / convives ...   except ZeroDivisionError:  ... None
#
#  👀 Résultat attendu (avec convives = 0) :
#     None
#  (change convives en 4 pour voir 15.0)

addition = 60
convives = 0

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Valider une saisie (sans planter)
# ══════════════════════════════════════════════════════════════════════
#  Un utilisateur a tapé  saisie  pour son âge. Essaie de la convertir en
#  entier avec int(saisie). Si ça marche, affiche le nombre ; sinon  None.
#  Indice :  int("abc")  lève une  ValueError  → attrape-la.
#
#  👀 Résultat attendu (avec saisie = "abc") :
#     None
#  (change saisie en "25" pour voir 25)

saisie = "abc"

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Écrire une note dans un fichier, puis la relire
# ══════════════════════════════════════════════════════════════════════
#  Écris le texte  note  dans le fichier  chemin, puis relis le fichier et
#  affiche son contenu (comme un pense-bête qu'on enregistre).
#  Indice :
#     with open(chemin, "w", encoding="utf-8") as f:   # "w" = écrire
#         f.write(note)
#     with open(chemin, "r", encoding="utf-8") as f:   # "r" = lire
#         print(f.read())
#
#  💡 Sur ton PC : remplace "journal.txt" par un vrai chemin (ex.
#     "/home/toi/notes.txt") pour enregistrer tes notes pour de vrai.
#
#  👀 Résultat attendu :
#     Acheter du pain

chemin = "journal.txt"
note = "Acheter du pain"

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Compter les lignes d'un fichier (0 s'il manque)
# ══════════════════════════════════════════════════════════════════════
#  Essaie d'ouvrir  chemin  et d'afficher son nombre de lignes. S'il n'existe
#  pas, affiche  0  (au lieu de planter).
#  Indice :  try: with open(...) as f: print(len(f.readlines()))
#            except FileNotFoundError: print(0)
#
#  💡 Sur ton PC : mets le chemin d'un vrai fichier texte (un .log, un .csv…)
#     pour compter SES lignes.
#
#  👀 Résultat attendu (ce fichier n'existe pas) :
#     0

chemin = "ce_fichier_nexiste_pas.txt"

# ✏️ ton code ici :


