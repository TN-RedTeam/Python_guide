#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 03 : fonctions & modules   (série 2, après exercices.py)

──────────────────────────────────────────────────────────────────────
 Trois façons de travailler la même matière :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier.
   🔧 MODIFIER  : un petit script qui marche déjà. Change-le pour
                 obtenir le nouveau résultat demandé.
   ✍️ ÉCRIRE    : comme dans exercices.py, mais sans indice ni liste
                 d'outils. C'est à toi de reconnaître quoi utiliser.
──────────────────────────────────────────────────────────────────────

 MÉTHODE : note d'abord tes prédictions (lignes « ✏️ ma prédiction »),
 PUIS lance le fichier et compare avec les lignes « LIRE … → ».

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Une fonction qui RENVOIE
# ══════════════════════════════════════════════════════════════════════
#  Que vaut  resultat ? Remplace chaque appel par ce qu'il renvoie.
#  ✏️ ma prédiction :

def double(n):
    return n * 2

resultat = double(4) + double(1)
print("LIRE 1 →", resultat)


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 2 — Une fonction qui AFFICHE (le piège n°1)
# ══════════════════════════════════════════════════════════════════════
#  Cette fonction fait un print au lieu d'un return. Deux lignes vont
#  s'afficher : que contient chacune ? Et surtout : que vaut  valeur ?
#  ✏️ ma prédiction :

def afficher_double(n):
    print("LIRE 2 (dans la fonction) →", n * 2)

valeur = afficher_double(5)
print("LIRE 2 (après l'appel) →", valeur)


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — Ajouter des frais de livraison
# ══════════════════════════════════════════════════════════════════════
#  Cette fonction calcule le prix d'une commande. Ajoute-lui un 3e
#  paramètre  livraison, qui vaut 5 si on ne le précise pas, et qui
#  s'ajoute au total. Puis appelle-la deux fois : pour 3 articles à 12 €
#  avec la livraison normale, puis pour la même commande livrée gratuitement.
#
#  👀 Résultat attendu APRÈS ta modification :
#     41
#     36

def prix_commande(prix, quantite):
    return prix * quantite

print(prix_commande(12, 3))


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — Convertir des minutes
# ══════════════════════════════════════════════════════════════════════
#  Écris  en_heures(minutes)  qui renvoie un texte comme "2 h 15 min".
#  Appelle-la avec 135 et affiche le résultat.
#
#  👀 Résultat attendu :
#     2 h 15 min

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — Le total d'un ticket de caisse
# ══════════════════════════════════════════════════════════════════════
#  Écris  total_ticket  qui accepte autant de prix qu'on veut et renvoie
#  leur somme. Appelle-la avec 2.5, 4 et 1.5, puis sans aucun prix.
#
#  👀 Résultat attendu :
#     8.0
#     0

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 3 — Trier des fichiers par taille
# ══════════════════════════════════════════════════════════════════════
#  Chaque élément de  fichiers  est un couple (nom, taille en Mo).
#  Écris  trier_par_taille(fichiers)  qui renvoie la liste triée du plus
#  PETIT fichier au plus gros. Appelle-la et affiche le résultat.
#
#  👀 Résultat attendu :
#     [('cv.pdf', 1), ('photo.jpg', 4), ('film.mp4', 700)]

fichiers = [("film.mp4", 700), ("cv.pdf", 1), ("photo.jpg", 4)]

# ✏️ ton code ici :

