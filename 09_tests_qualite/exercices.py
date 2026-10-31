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

 Lancer :   python3 exercices.py        Corrigé :  solutions.py
 Bonus : ces assert sont de vrais tests, lançables aussi avec `pytest`.
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — est_palindrome + ses tests
# ══════════════════════════════════════════════════════════════════════
#  1) Écris  est_palindrome(mot)  qui renvoie True si le mot se lit pareil
#     à l'endroit et à l'envers.  Indice : "kayak"[::-1] == "kayak".
#  2) Teste-la toi-même avec au moins 2 assert (un vrai, un faux), puis
#     affiche  "palindrome OK".
#
#  👀 Résultat attendu :
#     palindrome OK

# ✏️ ton code ici (la fonction, puis tes assert, puis le print) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — inverser + ses tests
# ══════════════════════════════════════════════════════════════════════
#  1) Écris  inverser(texte)  qui renvoie le texte à l'envers ([::-1]).
#  2) Teste avec  assert inverser("abc") == "cba"  (et un autre de ton choix),
#     puis affiche  "inverser OK".
#
#  👀 Résultat attendu :
#     inverser OK

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — factorielle + ses tests
# ══════════════════════════════════════════════════════════════════════
#  1) Écris  factorielle(n) = 1 × 2 × … × n.  Cas particulier : factorielle(0)
#     doit valoir 1.  Indice : pars de 1, boucle for i in range(2, n + 1),
#     multiplie (resultat *= i).
#  2) Teste avec  assert factorielle(5) == 120  et  assert factorielle(0) == 1,
#     puis affiche  "factorielle OK".
#
#  👀 Résultat attendu :
#     factorielle OK

# ✏️ ton code ici :


