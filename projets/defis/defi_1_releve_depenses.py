#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DÉFI 1 — Analyser un relevé de dépenses
(à faire après les modules 01 à 04)

──────────────────────────────────────────────────────────────────────
 LE PROJET
 Tu as un fichier releve.csv : tes dépenses du mois, une par ligne.
 Tu vas écrire le programme qui le lit, calcule les totaux, classe les
 catégories et enregistre un rapport. C'est un vrai petit outil, que tu
 pourras ensuite lancer sur le relevé de ta propre banque.

 CE QUE TU RÉUTILISES
   module 01 : boucles, conditions, f-strings
   module 02 : listes, dictionnaires
   module 03 : fonctions, tri avec key
   module 04 : lire et écrire un fichier
──────────────────────────────────────────────────────────────────────

 COMMENT AVANCER
   • Fais les étapes DANS L'ORDRE : chacune se sert du résultat de la
     précédente. Lance le fichier après chaque étape et compare.
   • Un projet ne se réussit pas d'une traite. Bloquer 20 minutes sur
     une étape est normal : reviens au cours du module concerné.
   • Conseil : écris une fonction par étape (lire_releve, total, …).
     Ce n'est pas obligatoire, mais c'est comme ça qu'on garde un
     programme lisible quand il grandit.

 Lancer :   python3 defi_1_releve_depenses.py
 Corrigé :  defi_1_releve_depenses_solution.py  (après avoir essayé !)

 💡 Sur ton PC : la plupart des banques proposent un export CSV. Remplace
    "releve.csv" par ton fichier et adapte les noms de colonnes.
"""

# Le fichier de départ. On l'écrit sur le disque : ouvre-le dans un éditeur
# de texte pour voir à quoi ressemble un CSV (des valeurs séparées par des virgules).
CONTENU = """date,categorie,libelle,montant
2026-03-02,courses,Supermarché,54
2026-03-03,transport,Métro,22
2026-03-05,loisirs,Cinéma,12
2026-03-09,courses,Boulangerie,8
2026-03-12,logement,Loyer,700
2026-03-15,transport,Essence,45
2026-03-21,courses,Supermarché,62
2026-03-27,loisirs,Concert,35
"""
with open("releve.csv", "w", encoding="utf-8") as f:
    f.write(CONTENU)


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 1 — Lire le fichier
# ══════════════════════════════════════════════════════════════════════
#  Lis releve.csv et construis  depenses : une LISTE de DICTIONNAIRES, un
#  par ligne du fichier, avec les clés "categorie", "libelle" et "montant".
#  Attention à deux choses :
#    - la 1re ligne du fichier est l'en-tête : elle ne doit pas devenir
#      une dépense ;
#    - le montant doit être un NOMBRE, pas un texte.
#  Affiche le nombre de dépenses, puis la première.
#  🧰 Outils : with open, .readlines(), .strip(), .split(","), int()
#
#  👀 Résultat attendu :
#     8 dépenses
#     {'categorie': 'courses', 'libelle': 'Supermarché', 'montant': 54}

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 2 — Le total du mois
# ══════════════════════════════════════════════════════════════════════
#  Additionne les montants de toutes les dépenses.
#
#  👀 Résultat attendu :
#     Total : 938 €

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 3 — Le total par catégorie
# ══════════════════════════════════════════════════════════════════════
#  Construis un dictionnaire {catégorie: total dépensé} et affiche-le.
#
#  👀 Résultat attendu :
#     {'courses': 124, 'transport': 67, 'loisirs': 47, 'logement': 700}

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 4 — Le classement des catégories
# ══════════════════════════════════════════════════════════════════════
#  Affiche les catégories de la plus coûteuse à la moins coûteuse, une
#  par ligne.
#  🧰 Outils : .items(), sorted avec key et reverse=True
#
#  👀 Résultat attendu :
#     logement : 700 €
#     courses : 124 €
#     transport : 67 €
#     loisirs : 47 €

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 5 — Enregistrer le rapport
# ══════════════════════════════════════════════════════════════════════
#  Écris dans le fichier rapport.txt : un titre, le classement de
#  l'étape 4, puis le total. Ensuite relis le fichier et affiche son
#  contenu, pour vérifier ce qui a vraiment été enregistré.
#
#  👀 Résultat attendu :
#     RAPPORT DE MARS
#     logement : 700 €
#     courses : 124 €
#     transport : 67 €
#     loisirs : 47 €
#     TOTAL : 938 €

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  🚀 POUR ALLER PLUS LOIN (sans corrigé : c'est ton projet maintenant)
# ══════════════════════════════════════════════════════════════════════
#   • Affiche la dépense la plus élevée, avec son libellé.
#   • Ajoute au rapport la part de chaque catégorie en pourcentage.
#   • Que se passe-t-il si une ligne du fichier a un montant vide ?
#     Rends la lecture robuste avec try / except.
