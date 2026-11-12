#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — 🧭 Penser comme un dev : les 5 patterns

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (lis-les une fois) :
   • Chaque exercice te donne la liste de départ — elle est ÉCRITE, tu la
     VOIS. Rien n'est caché.
   • Tu écris ton code dans l'espace « ✏️ ton code ici ».
   • Tu lances le fichier, tu regardes ce qui s'affiche, et tu compares
     avec le « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 Ici on entraîne les 5 RÉFLEXES qui reviennent sans arrêt en code :
 accumuler, compter, chercher, filtrer, trouver le champion. Reconnaître
 le bon pattern, c'est 80 % du travail. Le titre de chaque exercice te
 donne le pattern : à toi de retrouver comment il s'écrit.

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Lancer :   python3 exercices.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Pattern ACCUMULATEUR (faire un total)
# ══════════════════════════════════════════════════════════════════════
#  Additionne tous les nombres de la liste et affiche le total.
#  Fais-le avec une boucle (sans la fonction sum), pour t'entraîner.
#
#  👀 Résultat attendu (avec nombres = [2, 5, 3]) :
#     10

nombres = [2, 5, 3]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Pattern COMPTEUR (compter ceux qui remplissent une condition)
# ══════════════════════════════════════════════════════════════════════
#  Compte combien de mots ont PLUS de 3 lettres, puis affiche ce nombre.
#
#  👀 Résultat attendu (avec mots = ["ok", "chien", "a", "table"]) :
#     2

mots = ["ok", "chien", "a", "table"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Pattern RECHERCHE + DRAPEAU (est-ce présent ?)
# ══════════════════════════════════════════════════════════════════════
#  Dis si  cible  est présent dans la liste. Affiche "trouvé" ou "absent".
#  Fais-le avec une boucle (sans le mot-clé in sur la liste), pour
#  t'entraîner.
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
#
#  👀 Résultat attendu (avec serie = [1, 2, 3, 4]) :
#     [2, 4]

serie = [1, 2, 3, 4]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — Pattern CHAMPION (trouver le plus grand) + cas limite
# ══════════════════════════════════════════════════════════════════════
#  Trouve et affiche le plus grand nombre de la liste (avec une boucle,
#  sans la fonction max). CAS LIMITE : si la liste est vide, affiche None.
#
#  👀 Résultat attendu (avec classement = [3, 9, 2]) :
#     9
#  (change classement en []  ->  doit afficher  None)

classement = [3, 9, 2]

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : total = 0 AVANT la boucle ; dans la boucle, total = total + n ;
#               le print APRÈS la boucle.
#
#  Exercice 2 : compte = 0 AVANT la boucle ; dans la boucle, un if sur
#               len(mot) > 3 qui fait compte += 1.
#
#  Exercice 3 : trouve = False AVANT la boucle (le « drapeau ») ; dans la
#               boucle, si la valeur est égale à la cible, trouve = True.
#               Après la boucle, un if / else sur trouve choisit le message.
#
#  Exercice 4 : gardes = [] AVANT la boucle ; dans la boucle, si n % 2 == 0,
#               gardes.append(n).
#
#  Exercice 5 : traite d'abord le cas limite : si la liste est vide, affiche
#               None. Sinon meilleur = classement[0], puis dans la boucle,
#               tout nombre plus grand devient le nouveau meilleur.
