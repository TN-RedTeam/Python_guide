#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 05 : la POO   (série 2, après exercices.py)

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
#  👓 LIRE 1 — Deux objets du même moule
# ══════════════════════════════════════════════════════════════════════
#  Deux compteurs sont créés. Que valent-ils à la fin, chacun ?
#  ✏️ ma prédiction :

class Compteur:
    def __init__(self):
        self.valeur = 0

    def incrementer(self):
        self.valeur += 1

a = Compteur()
b = Compteur()
a.incrementer()
a.incrementer()
b.incrementer()
print("LIRE 1 →", a.valeur, b.valeur)


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 2 — Quelle version de la méthode est appelée ?
# ══════════════════════════════════════════════════════════════════════
#  presenter() n'est écrite que dans Animal, mais elle appelle self.cri().
#  Que renvoie-t-elle pour un Animal ? Et pour un Chat ?
#  ✏️ ma prédiction :

class Animal:
    def cri(self):
        return "..."

    def presenter(self):
        return f"Je fais {self.cri()}"

class Chat(Animal):
    def cri(self):
        return "Miaou"

print("LIRE 2 →", Animal().presenter(), "|", Chat().presenter())


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — Ajouter une méthode à une classe
# ══════════════════════════════════════════════════════════════════════
#  Ajoute à la classe Fichier une méthode  est_gros()  qui renvoie True si
#  le fichier dépasse 100 Mo, False sinon. Puis, pour chacun des deux
#  fichiers, affiche le résultat de est_gros() juste après sa description.
#
#  👀 Résultat attendu APRÈS ta modification :
#     video.mp4 (700 Mo)
#     True
#     cv.pdf (1 Mo)
#     False

class Fichier:
    def __init__(self, nom, taille_mo):
        self.nom = nom
        self.taille_mo = taille_mo

    def description(self):
        return f"{self.nom} ({self.taille_mo} Mo)"

video = Fichier("video.mp4", 700)
cv = Fichier("cv.pdf", 1)
print(video.description())
print(cv.description())


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — Une ligne de commande
# ══════════════════════════════════════════════════════════════════════
#  Écris une classe  Produit  (nom, prix à l'unité, quantité) avec une
#  méthode  total()  qui renvoie le prix de la ligne. Crée 10 stylos à
#  2 € pièce et affiche le total.
#
#  👀 Résultat attendu :
#     20

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — Une playlist
# ══════════════════════════════════════════════════════════════════════
#  Écris une classe  Playlist  qui démarre VIDE, avec :
#    - ajouter(titre) : ajoute un titre à la playlist ;
#    - nombre() : renvoie le nombre de titres.
#  Crée une playlist, ajoute-lui "Intro", "Refrain" et "Final", puis
#  affiche le nombre de titres.
#
#  👀 Résultat attendu :
#     3

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 3 — Hériter d'un véhicule
# ══════════════════════════════════════════════════════════════════════
#  Écris une classe  Vehicule  (nom, nombre de roues) avec une méthode
#  description()  qui renvoie par exemple "Vélo : 2 roues".
#  Puis écris  Voiture, qui HÉRITE de Vehicule et se crée avec le nom
#  seul : une voiture a toujours 4 roues.
#  Affiche la description d'un Vehicule "Vélo" à 2 roues, puis celle
#  d'une Voiture "Clio".
#
#  👀 Résultat attendu :
#     Vélo : 2 roues
#     Clio : 4 roues

# ✏️ ton code ici :

