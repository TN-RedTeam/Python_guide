#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DÉFI 3 — Comparer deux dossiers
(à faire après le module 10)

──────────────────────────────────────────────────────────────────────
 LE PROJET
 Tu as un dossier de travail et sa sauvegarde. La sauvegarde est-elle à
 jour ? Tu vas écrire le programme qui répond : quels fichiers manquent,
 lesquels sont en trop, lesquels ont changé — puis qui répare.

 CE QUE TU RÉUTILISES
   module 02 : les ensembles (set) et leurs opérations
   module 03 : fonctions
   module 10 : pathlib (parcourir un dossier, taille d'un fichier)
──────────────────────────────────────────────────────────────────────

 COMMENT AVANCER
   • Écris une fonction par étape : les étapes 4 et 5 réutilisent
     celles d'avant, tu seras content de les avoir.
   • Lance le fichier après chaque étape et compare au résultat attendu.

 Lancer :   python3 defi_3_comparer_dossiers.py
 Corrigé :  defi_3_comparer_dossiers_solution.py  (après avoir essayé !)

 💡 Sur ton PC : remplace  original  et  sauvegarde  par deux vrais
    dossiers. Les étapes 1 à 4 ne font que LIRE : elles sont sans risque.
    L'étape 5 copie des fichiers : teste-la d'abord sur des dossiers
    d'essai.
"""

from pathlib import Path
import shutil
import tempfile

# Les deux dossiers de test, créés dans un dossier temporaire : rien n'est
# touché chez toi. Chaque fichier contient autant de « x » que sa taille.
racine = Path(tempfile.mkdtemp())
original = racine / "original"
sauvegarde = racine / "sauvegarde"
original.mkdir()
sauvegarde.mkdir()

for nom, taille in [("rapport.docx", 300), ("budget.xlsx", 120), ("photo.jpg", 500), ("notes.txt", 40)]:
    (original / nom).write_text("x" * taille, encoding="utf-8")
for nom, taille in [("rapport.docx", 300), ("budget.xlsx", 90), ("photo.jpg", 500), ("vieux.txt", 10)]:
    (sauvegarde / nom).write_text("x" * taille, encoding="utf-8")


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 1 — Lister les deux dossiers
# ══════════════════════════════════════════════════════════════════════
#  Affiche la liste triée des noms de fichiers de chaque dossier.
#  🧰 Outils : .iterdir(), .name, sorted
#
#  👀 Résultat attendu :
#     original : ['budget.xlsx', 'notes.txt', 'photo.jpg', 'rapport.docx']
#     sauvegarde : ['budget.xlsx', 'photo.jpg', 'rapport.docx', 'vieux.txt']

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 2 — Ce qui manque, ce qui est en trop
# ══════════════════════════════════════════════════════════════════════
#  Affiche les fichiers MANQUANTS (dans l'original, absents de la
#  sauvegarde), puis les fichiers EN TROP (dans la sauvegarde, absents de
#  l'original). Listes triées.
#  🧰 Outils : set, la différence d'ensembles (le signe -), sorted
#
#  👀 Résultat attendu :
#     Manquants : ['notes.txt']
#     En trop : ['vieux.txt']

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 3 — Les fichiers modifiés
# ══════════════════════════════════════════════════════════════════════
#  Parmi les fichiers présents des DEUX côtés, affiche ceux dont la
#  taille n'est pas la même (ils ont été modifiés depuis la sauvegarde).
#  🧰 Outils : l'intersection d'ensembles (le signe &), .stat().st_size
#
#  👀 Résultat attendu :
#     Modifiés : ['budget.xlsx']

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 4 — Le verdict
# ══════════════════════════════════════════════════════════════════════
#  Écris une fonction  verdict(original, sauvegarde)  qui renvoie
#  "Sauvegarde à jour" s'il n'y a ni manquant ni modifié, et sinon un
#  message qui les compte. (Un fichier en trop n'empêche pas la
#  sauvegarde d'être à jour.) Affiche le verdict.
#
#  👀 Résultat attendu :
#     Sauvegarde PAS à jour : 1 manquant(s), 1 modifié(s)

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 5 — Réparer la sauvegarde
# ══════════════════════════════════════════════════════════════════════
#  Copie dans la sauvegarde chaque fichier manquant ou modifié, depuis
#  l'original. Puis affiche de nouveau le verdict.
#  🧰 Outils : shutil.copy(chemin_source, chemin_destination)
#
#  👀 Résultat attendu :
#     Sauvegarde à jour

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  🚀 POUR ALLER PLUS LOIN (sans corrigé : c'est ton projet maintenant)
# ══════════════════════════════════════════════════════════════════════
#   • Deux fichiers de même taille peuvent avoir un contenu différent.
#     Compare plutôt leur contenu (read_bytes), ou une empreinte (hashlib).
#   • Après le module 12 : fais-en un vrai script, avec argparse, qui
#     reçoit les deux dossiers en options et un interrupteur --reparer.
