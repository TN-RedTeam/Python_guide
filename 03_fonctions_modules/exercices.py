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

 La ligne « 🧰 Outils » te dit QUOI utiliser, pas comment l'écrire.

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Lancer :   python3 exercices.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Calculer un prix TTC
# ══════════════════════════════════════════════════════════════════════
#  Écris une fonction  prix_ttc(prix_ht)  qui RENVOIE le prix avec 20 % de
#  TVA (c'est-à-dire le prix multiplié par 1.2).
#  Puis appelle-la avec 100 et affiche ce qu'elle renvoie.
#  🧰 Outils : def, return, print
#
#  👀 Résultat attendu :
#     120.0

# ✏️ ton code ici (la fonction d'abord, l'appel ensuite, sans indentation) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Un paramètre avec valeur par défaut
# ══════════════════════════════════════════════════════════════════════
#  Écris  saluer(nom, politesse)  qui renvoie  "<politesse> <nom> !".
#  Si on ne donne pas politesse, c'est "Bonjour" qui doit être utilisé.
#  Appelle-la DEUX fois : avec "Ada" seul, puis avec "Ada" et "Salut".
#  🧰 Outils : une valeur par défaut dans le def, une f-string
#
#  👀 Résultat attendu :
#     Bonjour Ada !
#     Salut Ada !

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — Compter les mots d'un message
# ══════════════════════════════════════════════════════════════════════
#  Écris  compter_mots(message)  qui renvoie le nombre de mots.
#  Appelle-la avec "merci pour ton aide" et affiche le résultat.
#  🧰 Outils : la méthode .split(), len
#
#  👀 Résultat attendu :
#     4

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — La moyenne des notes (*args)
# ══════════════════════════════════════════════════════════════════════
#  Écris  moyenne(*notes)  qui accepte autant de notes qu'on veut et
#  renvoie leur moyenne — et 0 s'il n'y en a aucune (sinon ça plante :
#  division par zéro).
#  Appelle-la avec 12, 16 et 14, puis sans aucune note.
#  🧰 Outils : *args, if, sum, len
#
#  👀 Résultat attendu :
#     14.0
#     0

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 5 — Trier des fichiers par longueur de nom (le défi)
# ══════════════════════════════════════════════════════════════════════
#  Écris  trier_par_longueur(fichiers)  qui renvoie la liste triée du nom
#  le plus COURT au plus long.
#  Appelle-la avec  ["rapport.pdf", "cv.pdf", "presentation.pptx"].
#  🧰 Outils : sorted avec son paramètre key, une lambda, len
#
#  👀 Résultat attendu :
#     ['cv.pdf', 'rapport.pdf', 'presentation.pptx']

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : le corps de la fonction tient en une ligne : return suivi du
#               calcul. L'appel s'écrit EN DEHORS de la fonction (collé à
#               gauche) : print(prix_ttc(100)).
#
#  Exercice 2 : la valeur par défaut se met dans la parenthèse du def :
#               def saluer(nom, politesse="Bonjour"):
#
#  Exercice 3 : "le chat dort".split() renvoie ["le", "chat", "dort"].
#               Il reste à compter les éléments de cette liste.
#
#  Exercice 4 : dans la fonction, notes est un tuple. « if not notes: »
#               est vrai quand il est vide. Sinon : somme divisée par nombre.
#
#  Exercice 5 : sorted(liste, key=...) trie selon ce que renvoie la fonction
#               donnée à key. Une lambda qui renvoie la longueur d'un nom :
#               lambda nom: len(nom)
