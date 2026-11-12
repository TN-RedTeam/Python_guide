#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DÉFI 4 — Renommer des photos en série
(à faire après le module 10)

──────────────────────────────────────────────────────────────────────
 LE PROJET
 Ton appareil photo nomme ses fichiers IMG_4821.jpg, DSC_0007.jpg…
 Tu veux vacances_001.jpg, vacances_002.jpg… Tu vas écrire l'outil qui
 renomme tout un dossier d'un coup — et qui te MONTRE ce qu'il va faire
 avant de le faire, parce qu'un renommage raté ne s'annule pas.

 CE QUE TU RÉUTILISES
   module 01 : boucles, f-strings
   module 02 : listes de couples
   module 03 : fonctions, paramètre avec valeur par défaut
   module 10 : pathlib (lister, filtrer par extension, renommer)
──────────────────────────────────────────────────────────────────────

 COMMENT AVANCER
   • Lance le fichier après chaque étape et compare au résultat attendu.
   • L'idée centrale du projet : séparer « décider quoi faire » (le
     plan, étape 2) de « le faire » (étape 3).

 Lancer :   python3 defi_4_renommer_photos.py
 Corrigé :  defi_4_renommer_photos_solution.py  (après avoir essayé !)

 💡 Sur ton PC : commence TOUJOURS par une COPIE de ton dossier de photos,
    et par le mode simulation de l'étape 4. Ne lance le vrai renommage
    que quand le plan affiché est exactement celui que tu veux.
"""

from pathlib import Path
import tempfile

# Le dossier de test, créé dans un dossier temporaire : rien n'est touché
# chez toi. Il contient 3 photos et un fichier qui n'en est pas une.
dossier = Path(tempfile.mkdtemp())
for nom in ["IMG_4821.jpg", "IMG_4822.jpg", "DSC_0007.jpg", "notes.txt"]:
    (dossier / nom).write_text("x", encoding="utf-8")


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 1 — Trouver les photos
# ══════════════════════════════════════════════════════════════════════
#  Affiche la liste triée des noms des fichiers ".jpg" du dossier (et
#  seulement eux : notes.txt ne doit pas être renommé).
#  🧰 Outils : .iterdir(), .suffix, .name, sorted
#
#  👀 Résultat attendu :
#     ['DSC_0007.jpg', 'IMG_4821.jpg', 'IMG_4822.jpg']

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 2 — Préparer le plan, sans rien toucher
# ══════════════════════════════════════════════════════════════════════
#  Construis le plan de renommage : une liste de couples (ancien nom,
#  nouveau nom), où les nouveaux noms sont vacances_001.jpg,
#  vacances_002.jpg… dans l'ordre de la liste triée. Affiche le plan.
#  Rien ne doit être renommé à cette étape.
#  🧰 Outils : un compteur, une f-string — l'écriture {numero:03d}
#              affiche le nombre sur 3 chiffres (1 devient 001)
#
#  👀 Résultat attendu :
#     DSC_0007.jpg -> vacances_001.jpg
#     IMG_4821.jpg -> vacances_002.jpg
#     IMG_4822.jpg -> vacances_003.jpg

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 3 — Appliquer le plan
# ══════════════════════════════════════════════════════════════════════
#  Renomme vraiment les fichiers en suivant le plan, puis affiche la
#  liste triée de TOUT le contenu du dossier pour vérifier.
#  🧰 Outils : chemin.rename(nouveau_chemin)
#
#  👀 Résultat attendu :
#     ['notes.txt', 'vacances_001.jpg', 'vacances_002.jpg', 'vacances_003.jpg']

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 4 — En faire un outil, avec un mode simulation
# ══════════════════════════════════════════════════════════════════════
#  Écris une fonction  renommer(dossier, prefixe, simulation=True)  qui
#  affiche le plan, et qui :
#    - en mode simulation, ne touche à rien et termine par la phrase
#      "Simulation : rien n'a été modifié" ;
#    - sinon, renomme vraiment les fichiers.
#  Appelle-la sur  dossier_ete  avec le préfixe "ete", en laissant la
#  simulation activée. Puis affiche le contenu trié de dossier_ete pour
#  prouver que rien n'a bougé.
#
#  👀 Résultat attendu :
#     a.jpg -> ete_001.jpg
#     b.jpg -> ete_002.jpg
#     Simulation : rien n'a été modifié
#     ['a.jpg', 'b.jpg']

dossier_ete = Path(tempfile.mkdtemp())
for nom in ["b.jpg", "a.jpg"]:
    (dossier_ete / nom).write_text("x", encoding="utf-8")

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  🚀 POUR ALLER PLUS LOIN (sans corrigé : c'est ton projet maintenant)
# ══════════════════════════════════════════════════════════════════════
#   • Que se passe-t-il si vacances_001.jpg existe déjà ? Refuse de
#     l'écraser et préviens (chemin.exists()).
#   • Traite aussi les .JPG en majuscules et les .png.
#   • Après le module 12 : fais-en un script avec argparse
#     (--dossier, --prefixe, et un interrupteur --pour-de-vrai).
