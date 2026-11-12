#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DÉFI 5 — Un tableau de bord avec pandas et NumPy
(à faire après les modules 13 et 16)

──────────────────────────────────────────────────────────────────────
 LE PROJET
 Tu refais le défi 1 (analyser des dépenses), mais avec les outils des
 données : pandas et NumPy. Tu vas voir la différence : ce qui demandait
 des boucles et des dictionnaires tient maintenant en une ligne — et tu
 peux poser des questions plus fines.

 CE QUE TU RÉUTILISES
   module 13 : pandas (charger, filtrer, trier, regrouper, exporter)
   module 16 : NumPy (calcul sur tout un tableau, sans boucle)
──────────────────────────────────────────────────────────────────────

 COMMENT AVANCER
   • Lance le fichier après chaque étape et compare au résultat attendu.
   • La règle du module 16 s'applique : aucune boucle for.

 Il te faut pandas et NumPy :  pip install pandas numpy
 Lancer :   python3 defi_5_tableau_de_bord.py
 Corrigé :  defi_5_tableau_de_bord_solution.py  (après avoir essayé !)

 💡 Sur ton PC : c'est exactement le traitement à appliquer à un export
    CSV de ta banque. C'est aussi la première étape de tout projet d'IA :
    charger un tableau et comprendre ce qu'il contient.
"""

import numpy as np
import pandas as pd

CONTENU = """mois,categorie,libelle,montant
janvier,courses,Supermarché,62
janvier,transport,Essence,48
janvier,loisirs,Cinéma,11
janvier,logement,Loyer,750
janvier,courses,Marché,24
février,courses,Supermarché,71
février,transport,Train,35
février,loisirs,Concert,45
février,logement,Loyer,750
février,courses,Boulangerie,9
"""
with open("depenses_2mois.csv", "w", encoding="utf-8") as f:
    f.write(CONTENU)


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 1 — Charger et découvrir
# ══════════════════════════════════════════════════════════════════════
#  Charge depenses_2mois.csv dans un DataFrame  df. Affiche sa forme,
#  puis la liste des noms de ses colonnes.
#  🧰 Outils : pd.read_csv, .shape, .columns, .tolist()
#
#  👀 Résultat attendu :
#     (10, 4)
#     ['mois', 'categorie', 'libelle', 'montant']

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 2 — Le total par mois
# ══════════════════════════════════════════════════════════════════════
#  Affiche le total dépensé chaque mois.
#
#  👀 Résultat attendu :
#     mois
#     février    910
#     janvier    895
#     Name: montant, dtype: int64

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 3 — Le classement des catégories
# ══════════════════════════════════════════════════════════════════════
#  Calcule le total par catégorie sur les deux mois, trié de la plus
#  coûteuse à la moins coûteuse. Range-le dans  par_categorie  et
#  affiche-le.
#  🧰 Outils : .groupby, .sum(), puis .sort_values(ascending=False)
#
#  👀 Résultat attendu :
#     categorie
#     logement     1500
#     courses       166
#     transport      83
#     loisirs        56
#     Name: montant, dtype: int64

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 4 — La part de chaque catégorie (NumPy)
# ══════════════════════════════════════════════════════════════════════
#  Transforme les totaux de l'étape 3 en tableau NumPy, puis calcule la
#  part de chaque catégorie dans le total général, en pourcentage,
#  arrondie à 1 chiffre après la virgule.
#  🧰 Outils : .to_numpy(), .sum(), np.round(tableau, 1)
#
#  👀 Résultat attendu :
#     [83.1  9.2  4.6  3.1]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 5 — Les dépenses au-dessus de la moyenne
# ══════════════════════════════════════════════════════════════════════
#  Le loyer est si gros qu'il fausse toute moyenne. Mets-le de côté :
#  parmi les dépenses HORS logement, affiche la liste des libellés de
#  celles qui dépassent la moyenne (de ces dépenses hors logement).
#  🧰 Outils : un filtre avec !=, .mean(), un second filtre, .tolist()
#
#  👀 Résultat attendu :
#     ['Supermarché', 'Essence', 'Supermarché', 'Concert']

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 6 — Exporter le tableau de bord
# ══════════════════════════════════════════════════════════════════════
#  Enregistre  par_categorie  dans "tableau_de_bord.csv", puis relis le
#  fichier et affiche son contenu.
#
#  👀 Résultat attendu :
#     categorie,montant
#     logement,1500
#     courses,166
#     transport,83
#     loisirs,56

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  🚀 POUR ALLER PLUS LOIN (sans corrigé : c'est ton projet maintenant)
# ══════════════════════════════════════════════════════════════════════
#   • Quelle catégorie a le plus augmenté entre janvier et février ?
#   • Ajoute une colonne « part » au tableau exporté.
#   • Trace un graphique en barres des catégories avec matplotlib
#     (par_categorie.plot(kind="bar")) : la suite du PARCOURS_IA.
