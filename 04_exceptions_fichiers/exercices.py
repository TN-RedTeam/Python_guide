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

 La ligne « 🧰 Outils » te dit QUOI utiliser, pas comment l'écrire.

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Les exercices sur les fichiers créent un petit fichier dans le dossier
 courant (tu peux le supprimer après).

 Lancer :   python3 exercices.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Partager l'addition sans planter
# ══════════════════════════════════════════════════════════════════════
#  Une addition de  addition  euros est partagée entre  convives  personnes.
#  Affiche le prix par personne. Mais si convives vaut 0, affiche  None
#  au lieu de laisser le programme planter (division par zéro).
#  🧰 Outils : try / except, l'exception ZeroDivisionError
#
#  👀 Résultat attendu (avec convives = 0) :
#     None
#  (change convives en 4 pour voir 15.0)

addition = 60
convives = 0

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Valider une saisie
# ══════════════════════════════════════════════════════════════════════
#  Un utilisateur a tapé  saisie  pour son âge. Essaie de la convertir en
#  nombre entier. Si ça marche, affiche le nombre ; sinon affiche  None.
#  🧰 Outils : int(), try / except, l'exception ValueError
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
#  🧰 Outils : with open(...) en écriture, puis with open(...) en lecture
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
#  Essaie d'ouvrir  chemin  et d'afficher son nombre de lignes. S'il
#  n'existe pas, affiche  0  (au lieu de planter).
#  🧰 Outils : try / except, with open(...), .readlines(), len,
#              l'exception FileNotFoundError
#
#  💡 Sur ton PC : mets le chemin d'un vrai fichier texte (un .log, un .csv…)
#     pour compter SES lignes.
#
#  👀 Résultat attendu (ce fichier n'existe pas) :
#     0

chemin = "ce_fichier_nexiste_pas.txt"

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : mets le calcul ET son print dans le bloc try. Dans le bloc
#               except ZeroDivisionError: , affiche None.
#
#  Exercice 2 : int("abc") lève une ValueError. Même forme que l'exercice 1 :
#               on tente dans le try, on rattrape dans le except.
#
#  Exercice 3 : deux blocs with à la suite. Le premier ouvre en mode "w"
#               (écrire) et fait f.write(note). Le second ouvre en mode "r"
#               (lire) et affiche f.read(). Pense à encoding="utf-8".
#
#  Exercice 4 : le with open(...) va DANS le try. f.readlines() renvoie la
#               liste des lignes : il reste à la compter. Le except
#               FileNotFoundError: affiche 0.
