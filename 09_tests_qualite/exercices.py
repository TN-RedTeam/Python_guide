#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 09 : tests & qualité

──────────────────────────────────────────────────────────────────────
 COMMENT ÇA MARCHE :
   • Pour chaque exercice tu écris UNE fonction, PUIS tu écris toi-même
     quelques  assert  pour la tester (c'est tout l'intérêt du module :
     apprendre à écrire ses tests).
   • Un  assert  qui est faux arrête le programme (AssertionError) : c'est
     le « rouge ». Quand tous passent, ton print final s'affiche : le « vert ».
   • Tu lances et tu compares au « 👀 Résultat attendu ».
──────────────────────────────────────────────────────────────────────

 Rappel :  assert est_palindrome("kayak") == True   ne fait rien si c'est
 vrai, et plante si c'est faux. On enchaîne plusieurs assert, puis un
 print("... OK") pour signaler que tout est bon.

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Lancer :   python3 exercices.py
 Bonus : ces assert sont de vrais tests, lançables aussi avec `pytest`.
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — est_palindrome + ses tests
# ══════════════════════════════════════════════════════════════════════
#  1) Écris  est_palindrome(mot)  qui renvoie True si le mot se lit pareil
#     à l'endroit et à l'envers (comme "kayak"), False sinon.
#  2) Teste-la toi-même avec au moins 2 assert : un mot qui EST un
#     palindrome, un mot qui n'en est PAS un. Puis affiche "palindrome OK".
#  🧰 Outils : def, return, une comparaison ==, assert
#
#  👀 Résultat attendu :
#     palindrome OK

# ✏️ ton code ici (la fonction, puis tes assert, puis le print) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — inverser + ses tests
# ══════════════════════════════════════════════════════════════════════
#  1) Écris  inverser(texte)  qui renvoie le texte à l'envers
#     ("abc" -> "cba").
#  2) Écris au moins 2 assert de ton choix. Pense à un cas limite : que
#     doit renvoyer inverser("") ? Puis affiche "inverser OK".
#  🧰 Outils : def, return, assert
#
#  👀 Résultat attendu :
#     inverser OK

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — factorielle + ses tests (le défi)
# ══════════════════════════════════════════════════════════════════════
#  1) Écris  factorielle(n)  qui renvoie 1 × 2 × … × n.
#     Exemple : factorielle(5) = 1 × 2 × 3 × 4 × 5 = 120.
#     Cas particulier : factorielle(0) doit valoir 1.
#  2) Teste le cas normal ET le cas particulier avec des assert, puis
#     affiche "factorielle OK".
#  🧰 Outils : def, une boucle for avec range, une variable qui accumule,
#              assert
#
#  👀 Résultat attendu :
#     factorielle OK

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : "kayak"[::-1] donne le texte à l'envers. Un mot est un
#               palindrome s'il est égal à son envers. Pour les tests :
#               assert est_palindrome("kayak") == True
#               assert est_palindrome("python") == False
#
#  Exercice 2 : la même astuce [::-1] suffit. Exemples de tests :
#               assert inverser("abc") == "cba"  et  assert inverser("") == ""
#
#  Exercice 3 : c'est le pattern accumulateur, mais avec une multiplication :
#               pars de resultat = 1 (pas 0 !), boucle sur range(2, n + 1),
#               et fais resultat *= i. Avec n = 0 la boucle ne tourne pas et
#               on renvoie bien 1.
