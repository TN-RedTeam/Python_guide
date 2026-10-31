#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 03 : fonctions & modules

──────────────────────────────────────────────────────────────────────
 NOUVEAU DANS CE MODULE : tu écris des FONCTIONS (def ...).
 Le point IMPORTANT, celui qui déroute au début :
   → Quand tu écris  def prix_ttc(prix_ht):  le mot « prix_ht » est un
     PARAMÈTRE. Il n'a pas de valeur en soi. C'est TOI qui lui en donnes
     une AU MOMENT OÙ TU APPELLES la fonction :  prix_ttc(100).
     Là, et seulement là, « prix_ht » vaut 100. Rien de magique.
 Donc chaque exercice te demande 2 choses : (1) écrire la fonction,
 (2) l'APPELER toi-même avec une valeur, et afficher le résultat.
──────────────────────────────────────────────────────────────────────

 Tu lances, tu compares l'affichage au « 👀 Résultat attendu ». Pas de
 correction automatique. Cours : README.md • Corrigé : solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Calculer un prix TTC
# ══════════════════════════════════════════════════════════════════════
#  Écris  prix_ttc(prix_ht)  qui RENVOIE (return) le prix avec 20 % de TVA,
#  c'est-à-dire  prix_ht * 1.2.
#  Puis APPELLE-la avec 100 et affiche le résultat :  print(prix_ttc(100))
#
#  👀 Résultat attendu :
#     120.0

# ✏️ ton code ici (d'abord  def prix_ttc(prix_ht):  ...  return ... ,
#    puis en dessous, sans indentation :  print(prix_ttc(100)) ) :



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
#  EXERCICE 3 — Compter les mots d'un message
# ══════════════════════════════════════════════════════════════════════
#  Écris  compter_mots(message)  qui renvoie le nombre de mots.
#  Indice :  "merci pour ton aide".split()  ->  ["merci", "pour", "ton", "aide"]
#            len(...)  compte les éléments.
#  Appelle-la avec "merci pour ton aide" et affiche le résultat.
#
#  👀 Résultat attendu :
#     4

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — La moyenne des notes (*args)
# ══════════════════════════════════════════════════════════════════════
#  Écris  moyenne(*notes)  qui renvoie la moyenne des notes reçues,
#  et 0 s'il n'y en a aucune (sinon division par zéro).
#  Indice :  si not notes: return 0  ;  sinon  return sum(notes) / len(notes).
#  Appelle-la avec (12, 16, 14) puis sans rien : moyenne() .
#
#  👀 Résultat attendu :
#     14.0
#     0

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — Trier des fichiers par longueur de nom (le défi : lambda)
# ══════════════════════════════════════════════════════════════════════
#  Écris  trier_par_longueur(fichiers)  qui renvoie la liste triée du nom
#  le plus COURT au plus long.
#  Indice :  return sorted(fichiers, key=lambda nom: len(nom))
#            key=... dit à sorted « compare les noms par leur longueur ».
#  Appelle-la avec  ["rapport.pdf", "cv.pdf", "presentation.pptx"]  et affiche.
#
#  👀 Résultat attendu :
#     ['cv.pdf', 'rapport.pdf', 'presentation.pptx']

# ✏️ ton code ici :


