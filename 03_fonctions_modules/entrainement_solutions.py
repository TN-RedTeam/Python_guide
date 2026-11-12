#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 03 : fonctions & modules

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire, ligne par ligne.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit tes prédictions et essayé.
"""


# ── 👓 LIRE 1 — Une fonction qui RENVOIE ─────────────────────────────
def double(n):
    return n * 2

resultat = double(4) + double(1)    # double(4) est remplacé par 8, double(1) par 2
print("LIRE 1 →", resultat)
# Réponse : 10. Un appel de fonction « devient » la valeur de son return :
# la ligne se lit donc  resultat = 8 + 2.


# ── 👓 LIRE 2 — Une fonction qui AFFICHE ─────────────────────────────
def afficher_double(n):
    print("LIRE 2 (dans la fonction) →", n * 2)    # affiche 10… et c'est tout

valeur = afficher_double(5)         # la fonction n'a pas de return -> elle renvoie None
print("LIRE 2 (après l'appel) →", valeur)
# Réponses : 10, puis None.
# print MONTRE une valeur à l'écran mais ne la donne pas au programme.
# Sans return, il n'y a rien à ranger dans  valeur  : Python y met None.
# C'est pour ça que  afficher_double(5) + 1  planterait.


# ── 🔧 MODIFIER 1 — Ajouter des frais de livraison ───────────────────
def prix_commande(prix, quantite, livraison=5):    # 5 = valeur par défaut
    return prix * quantite + livraison

print(prix_commande(12, 3))         # livraison non précisée -> 5 -> 41
print(prix_commande(12, 3, 0))      # livraison gratuite     -> 0 -> 36


# ── ✍️ ÉCRIRE 1 — Convertir des minutes ──────────────────────────────
def en_heures(minutes):
    heures = minutes // 60          # division entière : 135 // 60 = 2
    reste = minutes % 60            # le reste : 135 % 60 = 15
    return f"{heures} h {reste} min"

print(en_heures(135))


# ── ✍️ ÉCRIRE 2 — Le total d'un ticket de caisse ─────────────────────
def total_ticket(*prix):            # *prix ramasse tous les arguments dans un tuple
    return sum(prix)                # sum d'un tuple vide vaut 0 : pas de cas à part

print(total_ticket(2.5, 4, 1.5))
print(total_ticket())


# ── ✍️ ÉCRIRE 3 — Trier des fichiers par taille ──────────────────────
fichiers = [("film.mp4", 700), ("cv.pdf", 1), ("photo.jpg", 4)]

def trier_par_taille(fichiers):
    return sorted(fichiers, key=lambda fichier: fichier[1])
    # fichier est un couple (nom, taille) ; fichier[1] est la taille :
    # on dit à sorted de comparer les couples par leur 2e élément.

print(trier_par_taille(fichiers))
