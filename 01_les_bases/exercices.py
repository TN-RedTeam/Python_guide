#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 01 : les bases

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE (3 lignes, lis-les une fois) :
   • Chaque exercice te donne les valeurs de départ — elles sont ÉCRITES,
     tu les VOIS (par ex.  nombre = 7). Rien n'est caché.
   • Tu écris ton code dans l'espace « ✏️ ton code ici ».
   • Tu lances le fichier, tu regardes ce qui s'affiche, et tu compares
     avec le « 👀 Résultat attendu » écrit juste au-dessus. C'est tout.
──────────────────────────────────────────────────────────────────────

 Pas de fonction, pas de correction automatique : juste toi, du code,
 et ce qui s'affiche. Tu peux changer les valeurs de départ pour tester.

 Lancer :   python3 exercices.py
 Le cours est dans README.md ; le corrigé (si vraiment bloqué) dans solutions.py.
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Se présenter
# ══════════════════════════════════════════════════════════════════════
#  La variable  prenom  vaut "Ada".
#  Affiche la phrase :   Bonjour Ada !
#
#  👀 Résultat attendu :
#     Bonjour Ada !

prenom = "Ada"

# ✏️ ton code ici (utilise prenom dans une f-string, puis print) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — La catégorie d'âge
# ══════════════════════════════════════════════════════════════════════
#  La variable  age  vaut 15. Affiche "Enfant", "Adolescent" ou "Majeur" :
#     - moins de 13 ans      -> Enfant
#     - entre 13 et 17 ans   -> Adolescent
#     - 18 ans ou plus       -> Majeur
#
#  👀 Résultat attendu (avec age = 15) :
#     Adolescent
#  (change age en 10 -> Enfant, en 20 -> Majeur, pour tester)

age = 15

# ✏️ ton code ici (un if / elif / else, puis print du résultat) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Pair ou impair ?
# ══════════════════════════════════════════════════════════════════════
#  La variable  nombre  vaut 7.
#  Affiche  "7 est pair"  ou  "7 est impair"  selon le cas.
#  Rappel : un nombre est pair si  nombre % 2  vaut 0.
#
#  👀 Résultat attendu (avec nombre = 7) :
#     7 est impair

nombre = 7

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Additionner de 1 à n (une boucle for)
# ══════════════════════════════════════════════════════════════════════
#  La variable  n  vaut 5.
#  Calcule et affiche la somme  1 + 2 + 3 + 4 + 5.
#  Indice (voir le cours, section boucles) :
#     - pars d'un total à 0 :        total = 0
#     - parcours 1 à n inclus :      for i in range(1, n + 1):
#     - ajoute i au total :          total = total + i
#     - affiche total APRÈS la boucle.
#
#  👀 Résultat attendu (avec n = 5) :
#     15

n = 5

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — La table de multiplication
# ══════════════════════════════════════════════════════════════════════
#  La variable  table  vaut 7.
#  Affiche la table de 7, de 7x1 à 7x10, une ligne par multiplication,
#  sous la forme  "7 x 1 = 7".
#  Indice : for i in range(1, 11):   puis   print(f"{table} x {i} = {table * i}")
#
#  👀 Résultat attendu (avec table = 7) :
#     7 x 1 = 7
#     7 x 2 = 14
#     ... (jusqu'à) ...
#     7 x 10 = 70

table = 7

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 6 — FizzBuzz (le défi — prends ton temps)
# ══════════════════════════════════════════════════════════════════════
#  La variable  nombre_fb  vaut 15. Affiche :
#     - "FizzBuzz"  s'il est divisible par 3 ET par 5
#     - "Fizz"      s'il est divisible par 3 seulement
#     - "Buzz"      s'il est divisible par 5 seulement
#     - sinon, le nombre lui-même
#  Astuce : teste le cas "par 3 ET par 5" EN PREMIER.
#
#  👀 Résultat attendu (avec nombre_fb = 15) :
#     FizzBuzz
#  (change nombre_fb : 9 -> Fizz, 10 -> Buzz, 7 -> 7)

nombre_fb = 15

# ✏️ ton code ici :


