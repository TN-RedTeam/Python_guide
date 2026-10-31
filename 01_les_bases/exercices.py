#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 01 : les bases

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (3 lignes, lis-les une fois) :
   • Chaque exercice part de valeurs CONCRÈTES et VISIBLES (un prénom, un
     prix, un nombre de jours…). Rien n'est caché.
   • Tu écris ton code dans l'espace « ✏️ ton code ici », puis print.
   • Tu lances le fichier, tu regardes ce qui s'affiche, et tu compares
     avec le « 👀 Résultat attendu ». C'est tout.
──────────────────────────────────────────────────────────────────────

 Pas de fonction, pas de correction automatique. Tu peux changer les
 valeurs de départ pour tester toi-même.

 Lancer :   python3 exercices.py
 Cours : README.md   •   Corrigé (si bloqué) : solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Se présenter
# ══════════════════════════════════════════════════════════════════════
#  prenom vaut "Ada", age vaut 25. Affiche la phrase :
#     Je m'appelle Ada et j'ai 25 ans.
#  Indice : une f-string  f"... {prenom} ... {age} ..."
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
#
#  👀 Résultat attendu (avec age = 15) :
#     Adolescent
#  (change age en 10 -> Enfant, en 20 -> Majeur, pour tester)

age = 15

# ✏️ ton code ici (un if / elif / else, puis print) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Place paire ou impaire ?
# ══════════════════════════════════════════════════════════════════════
#  Au cinéma, tu as la place numéro  place. Affiche "paire" ou "impaire".
#  Rappel : un nombre est pair si  place % 2  vaut 0.
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
#  Indice (voir le cours, section boucles) :
#     total = 0
#     for i in range(1, jours + 1):   # 1, 2, ..., jours
#         total = total + i
#     puis affiche total APRÈS la boucle.
#
#  👀 Résultat attendu (avec jours = 5) :
#     15

jours = 5

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — La grille des prix
# ══════════════════════════════════════════════════════════════════════
#  Un billet coûte  prix  euros. Affiche le prix pour 1 à 10 billets,
#  une ligne par quantité, sous la forme  "3 billets = 21 €".
#  Indice : for i in range(1, 11):   puis   print(f"{i} billets = {prix * i} €")
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
#  Astuce : teste le cas "par 3 ET par 5" EN PREMIER.
#
#  👀 Résultat attendu (avec nombre = 15) :
#     FizzBuzz
#  (change nombre : 9 -> Fizz, 10 -> Buzz, 7 -> 7)

nombre = 15

# ✏️ ton code ici :


