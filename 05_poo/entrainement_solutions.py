#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 05 : la POO

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire, ligne par ligne.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit tes prédictions et essayé.
"""


# ── 👓 LIRE 1 — Deux objets du même moule ────────────────────────────
class Compteur:
    def __init__(self):
        self.valeur = 0             # chaque objet a SA propre case « valeur »

    def incrementer(self):
        self.valeur += 1            # self = l'objet sur lequel on appelle la méthode

a = Compteur()                      # a.valeur = 0
b = Compteur()                      # b.valeur = 0 (un autre objet, indépendant)
a.incrementer()                     # self = a -> a.valeur = 1
a.incrementer()                     # self = a -> a.valeur = 2
b.incrementer()                     # self = b -> b.valeur = 1
print("LIRE 1 →", a.valeur, b.valeur)
# Réponse : 2 1. La classe est le moule ; a et b sont deux objets distincts
# qui ne partagent pas leurs données.


# ── 👓 LIRE 2 — Quelle version de la méthode est appelée ? ───────────
class Animal:
    def cri(self):
        return "..."

    def presenter(self):
        return f"Je fais {self.cri()}"      # self.cri() : la version de L'OBJET

class Chat(Animal):
    def cri(self):                          # redéfinit (remplace) le cri du parent
        return "Miaou"

print("LIRE 2 →", Animal().presenter(), "|", Chat().presenter())
# Réponse : Je fais ... | Je fais Miaou.
# Chat hérite de presenter(). Quand elle s'exécute sur un Chat, self EST un
# Chat : self.cri() appelle donc la version de Chat.


# ── 🔧 MODIFIER 1 — Ajouter une méthode à une classe ─────────────────
class Fichier:
    def __init__(self, nom, taille_mo):
        self.nom = nom
        self.taille_mo = taille_mo

    def description(self):
        return f"{self.nom} ({self.taille_mo} Mo)"

    def est_gros(self):
        return self.taille_mo > 100         # la comparaison vaut déjà True ou False

video = Fichier("video.mp4", 700)
cv = Fichier("cv.pdf", 1)
print(video.description())
print(video.est_gros())
print(cv.description())
print(cv.est_gros())


# ── ✍️ ÉCRIRE 1 — Une ligne de commande ──────────────────────────────
class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def total(self):
        return self.prix * self.quantite

stylos = Produit("Stylo", 2, 10)
print(stylos.total())


# ── ✍️ ÉCRIRE 2 — Une playlist ───────────────────────────────────────
class Playlist:
    def __init__(self):
        self.titres = []                    # la playlist démarre vide

    def ajouter(self, titre):
        self.titres.append(titre)           # on modifie la liste rangée dans l'objet

    def nombre(self):
        return len(self.titres)

ma_playlist = Playlist()
ma_playlist.ajouter("Intro")
ma_playlist.ajouter("Refrain")
ma_playlist.ajouter("Final")
print(ma_playlist.nombre())


# ── ✍️ ÉCRIRE 3 — Hériter d'un véhicule ──────────────────────────────
class Vehicule:
    def __init__(self, nom, roues):
        self.nom = nom
        self.roues = roues

    def description(self):
        return f"{self.nom} : {self.roues} roues"

class Voiture(Vehicule):
    def __init__(self, nom):
        super().__init__(nom, 4)            # on fixe le nombre de roues à 4
    # description() est héritée de Vehicule : rien à réécrire.

print(Vehicule("Vélo", 2).description())
print(Voiture("Clio").description())
