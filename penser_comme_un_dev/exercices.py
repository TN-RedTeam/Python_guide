#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — 🧭 Penser comme un dev : les 5 patterns

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (3 lignes, lis-les une fois) :
   • Chaque exercice te donne la liste de départ — elle est ÉCRITE, tu la
     VOIS. Rien n'est caché.
   • Tu écris ton code dans l'espace « ✏️ ton code ici ».
   • Tu lances le fichier, tu regardes ce qui s'affiche, et tu compares
     avec le « 👀 Résultat attendu » écrit au-dessus. C'est tout.
──────────────────────────────────────────────────────────────────────

 Ici on entraîne les 5 RÉFLEXES qui reviennent sans arrêt en code :
 accumuler, compter, chercher, filtrer, trouver le champion. Reconnaître
 le bon pattern, c'est 80 % du travail. Pas de correction automatique.

 Lancer :   python3 exercices.py
 Le cours est dans README.md ; le corrigé (si bloqué) dans solutions.py.
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Pattern ACCUMULATEUR (faire un total)
# ══════════════════════════════════════════════════════════════════════
#  Additionne tous les nombres de la liste et affiche le total.
#  Réflexe : total = 0  AVANT la boucle, puis  total = total + n  dedans.
#
#  👀 Résultat attendu (avec nombres = [2, 5, 3]) :
#     10

nombres = [2, 5, 3]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Pattern COMPTEUR (compter ceux qui remplissent une condition)
# ══════════════════════════════════════════════════════════════════════
#  Compte combien de mots ont PLUS de 3 lettres, puis affiche ce nombre.
#  Réflexe : compte = 0  AVANT, puis  if len(mot) > 3:  compte += 1.
#
#  👀 Résultat attendu (avec mots = ["ok", "chien", "a", "table"]) :
#     2

mots = ["ok", "chien", "a", "table"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Pattern RECHERCHE + DRAPEAU (est-ce présent ?)
# ══════════════════════════════════════════════════════════════════════
#  Dis si  cible  est présent dans la liste. Affiche "trouvé" ou "absent".
#  Réflexe : trouve = False  AVANT ; si on tombe sur la cible, trouve = True.
#
#  👀 Résultat attendu (avec valeurs = [4, 8, 15] et cible = 8) :
#     trouvé

valeurs = [4, 8, 15]
cible = 8

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Pattern FILTRE (ne garder que certains)
# ══════════════════════════════════════════════════════════════════════
#  Construis la liste des nombres PAIRS, puis affiche-la.
#  Réflexe : gardes = []  AVANT ; si n % 2 == 0, gardes.append(n).
#
#  👀 Résultat attendu (avec serie = [1, 2, 3, 4]) :
#     [2, 4]

serie = [1, 2, 3, 4]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — Pattern CHAMPION (trouver le plus grand) + cas limite
# ══════════════════════════════════════════════════════════════════════
#  Trouve et affiche le plus grand nombre de la liste.
#  Réflexe : meilleur = liste[0] ; si un nombre est plus grand, il devient
#  le nouveau meilleur. CAS LIMITE : si la liste est vide, affiche None.
#
#  👀 Résultat attendu (avec classement = [3, 9, 2]) :
#     9
#  (change classement en []  ->  doit afficher  None)

classement = [3, 9, 2]

# ✏️ ton code ici :


