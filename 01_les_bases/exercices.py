#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 01 : les bases

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (lis-les une fois) :
   • Chaque exercice part de valeurs CONCRÈTES et VISIBLES (un prénom, un
     prix, un nombre de jours…). Rien n'est caché.
   • Tu écris ton code dans l'espace « ✏️ ton code ici », puis print.
   • Tu lances le fichier, tu regardes ce qui s'affiche, et tu compares
     avec le « 👀 Résultat attendu ». C'est tout.
──────────────────────────────────────────────────────────────────────

 La ligne « 🧰 Outils » te dit QUOI utiliser, pas comment l'écrire.

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Lancer :   python3 exercices.py
 Tu peux changer les valeurs de départ pour tester toi-même.
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Se présenter
# ══════════════════════════════════════════════════════════════════════
#  prenom vaut "Ada", age vaut 25. Affiche la phrase ci-dessous en
#  utilisant les deux variables (pas en recopiant "Ada" et 25 à la main).
#  🧰 Outils : une f-string, print
#
#  👀 Résultat attendu :
#     Je m'appelle Ada et j'ai 25 ans.

prenom = "Ada"
age = 25

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — La catégorie d'âge
# ══════════════════════════════════════════════════════════════════════
#  age vaut 15. Affiche "Enfant", "Adolescent" ou "Majeur" :
#     - moins de 13 ans      -> Enfant
#     - entre 13 et 17 ans   -> Adolescent
#     - 18 ans ou plus       -> Majeur
#  🧰 Outils : if / elif / else
#
#  👀 Résultat attendu (avec age = 15) :
#     Adolescent
#  (change age en 10 -> Enfant, en 20 -> Majeur, pour tester)

age = 15

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Place paire ou impaire ?
# ══════════════════════════════════════════════════════════════════════
#  Au cinéma, tu as la place numéro  place. Affiche "paire" ou "impaire".
#  🧰 Outils : le modulo %, if / else
#
#  👀 Résultat attendu (avec place = 7) :
#     impaire

place = 7

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Le défi d'épargne
# ══════════════════════════════════════════════════════════════════════
#  Tu mets de côté 1 € le 1er jour, 2 € le 2e, 3 € le 3e… bref i € le i-e jour.
#  Pour  jours = 5, calcule et affiche le TOTAL économisé (1+2+3+4+5).
#  🧰 Outils : une boucle for avec range, une variable qui accumule
#
#  👀 Résultat attendu (avec jours = 5) :
#     15

jours = 5

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — La grille des prix
# ══════════════════════════════════════════════════════════════════════
#  Un billet coûte  prix  euros. Affiche le prix pour 1 à 10 billets,
#  une ligne par quantité.
#  🧰 Outils : une boucle for avec range, une f-string avec un calcul dedans
#
#  👀 Résultat attendu (avec prix = 7) :
#     1 billets = 7 €
#     2 billets = 14 €
#     ... (jusqu'à) ...
#     10 billets = 70 €

prix = 7

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 6 — FizzBuzz (le défi classique — prends ton temps)
# ══════════════════════════════════════════════════════════════════════
#  C'est un exercice d'entretien célèbre. Pour le nombre  nombre, affiche :
#     - "FizzBuzz"  s'il est divisible par 3 ET par 5
#     - "Fizz"      s'il est divisible par 3 seulement
#     - "Buzz"      s'il est divisible par 5 seulement
#     - sinon, le nombre lui-même
#  🧰 Outils : le modulo %, and, if / elif / else
#
#  👀 Résultat attendu (avec nombre = 15) :
#     FizzBuzz
#  (change nombre : 9 -> Fizz, 10 -> Buzz, 7 -> 7)

nombre = 15

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : mets un f juste avant le guillemet ouvrant, et écris les
#               variables entre accolades dans le texte : f"... {prenom} ...".
#
#  Exercice 2 : teste d'abord le cas le plus grand (age >= 18), puis
#               elif age >= 13, et le else attrape tout le reste.
#
#  Exercice 3 : place % 2 donne le reste de la division par 2. S'il vaut 0,
#               le nombre est pair.
#
#  Exercice 4 : crée total = 0 AVANT la boucle. Dans la boucle, i doit valoir
#               1, 2, … jusqu'à jours inclus : range(1, jours + 1). Ajoute i
#               au total à chaque tour, et affiche total APRÈS la boucle.
#
#  Exercice 5 : range(1, 11) donne 1 à 10. Dans la f-string, tu peux écrire
#               un calcul entre accolades : {prix * i}.
#
#  Exercice 6 : « divisible par 3 » s'écrit nombre % 3 == 0. Teste le cas
#               « par 3 ET par 5 » EN PREMIER, sinon le cas « par 3 » passe
#               devant et tu n'atteins jamais FizzBuzz.
