#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 03 : fonctions & modules

──────────────────────────────────────────────────────────────────────
 NOUVEAU DANS CE MODULE : tu écris des FONCTIONS (def ...).
 Le point IMPORTANT, celui qui déroute au début :
   → Quand tu écris  def saluer(nom):  le mot « nom » est un PARAMÈTRE.
     Il n'a pas de valeur en soi. C'est TOI qui lui en donnes une AU
     MOMENT OÙ TU APPELLES la fonction :  saluer("Ada").
     Là, et seulement là, « nom » vaut "Ada". Rien de magique.
 Donc chaque exercice te demande 2 choses : (1) écrire la fonction,
 (2) l'APPELER toi-même avec une valeur, et afficher le résultat.
──────────────────────────────────────────────────────────────────────

 Tu lances, tu compares l'affichage au « 👀 Résultat attendu ». Pas de
 correction automatique. Cours : README.md • Corrigé : solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Ta première fonction
# ══════════════════════════════════════════════════════════════════════
#  Écris une fonction  double(n)  qui RENVOIE (return) le double de n.
#  Puis APPELLE-la avec 5 et affiche le résultat :  print(double(5))
#
#  👀 Résultat attendu :
#     10

# ✏️ ton code ici (d'abord  def double(n):  ...  return ... ,
#    puis en dessous, sans indentation :  print(double(5)) ) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Un paramètre avec valeur par défaut
# ══════════════════════════════════════════════════════════════════════
#  Écris  saluer(nom, politesse="Bonjour")  qui renvoie  "<politesse> <nom> !".
#  Si on ne donne pas politesse, c'est "Bonjour" qui est utilisé.
#  Appelle-la DEUX fois :  saluer("Ada")   et   saluer("Ada", "Salut").
#
#  👀 Résultat attendu :
#     Bonjour Ada !
#     Salut Ada !

# ✏️ ton code ici (le def, puis deux print) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Compter les mots d'une phrase
# ══════════════════════════════════════════════════════════════════════
#  Écris  compter_mots(phrase)  qui renvoie le nombre de mots.
#  Indice :  "le chat dort".split()  ->  ["le", "chat", "dort"]  (une liste)
#            len(...)  compte les éléments.
#  Appelle-la avec "le chat dort" et affiche le résultat.
#
#  👀 Résultat attendu :
#     3

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Un nombre variable d'arguments (*args)
# ══════════════════════════════════════════════════════════════════════
#  Écris  moyenne(*notes)  qui renvoie la moyenne des notes reçues,
#  et 0 s'il n'y en a aucune (sinon division par zéro).
#  Indice :  si not notes: return 0  ;  sinon  return sum(notes) / len(notes).
#  Appelle-la avec (10, 20) puis sans rien : moyenne() .
#
#  👀 Résultat attendu :
#     15.0
#     0

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — Trier par longueur (le défi : lambda)
# ══════════════════════════════════════════════════════════════════════
#  Écris  trier_par_longueur(mots)  qui renvoie la liste triée du mot le
#  plus COURT au plus long.
#  Indice :  return sorted(mots, key=lambda mot: len(mot))
#            key=... dit à sorted « compare les mots par leur longueur ».
#  Appelle-la avec  ["python", "go", "rust"]  et affiche le résultat.
#
#  👀 Résultat attendu :
#     ['go', 'rust', 'python']

# ✏️ ton code ici :


