#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Défi 2 : l'inventaire d'un disque

Une solution possible. La tienne peut être différente et tout aussi juste.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé.
"""

DONNEES = [
    ("film.mp4", 700),
    ("photo.jpg", 4),
    ("cv.pdf", 1),
    ("vacances.jpg", 6),
    ("jeu.iso", 2300),
    ("notes.txt", 1),
]


# ── ÉTAPE 1 — La classe Fichier ──────────────────────────────────────
class Fichier:
    def __init__(self, nom, taille_mo):
        self.nom = nom
        self.taille_mo = taille_mo

    def extension(self):
        # "film.mp4".split(".") -> ["film", "mp4"] ; [-1] = le dernier morceau
        return "." + self.nom.split(".")[-1]


print(Fichier("film.mp4", 700).extension())


# ── ÉTAPES 2 à 6 — La classe Inventaire ──────────────────────────────
class Inventaire:
    def __init__(self):
        self.fichiers = []                      # l'inventaire démarre vide

    # étape 2
    def ajouter(self, fichier):
        self.fichiers.append(fichier)

    def nombre(self):
        return len(self.fichiers)

    def taille_totale(self):
        return sum(f.taille_mo for f in self.fichiers)

    # étape 3 : le pattern « champion », sur des objets
    def plus_gros(self):
        champion = self.fichiers[0]
        for f in self.fichiers:
            if f.taille_mo > champion.taille_mo:
                champion = f
        return champion                         # on renvoie l'OBJET, pas juste son nom

    # étape 4 : une compréhension de liste avec un filtre
    def par_extension(self, extension):
        return [f.nom for f in self.fichiers if f.extension() == extension]

    # étape 5 : un générateur (yield) : les fichiers sont livrés un par un
    def gros_fichiers(self, seuil):
        for f in self.fichiers:
            if f.taille_mo > seuil:
                yield f

    # étape 6 : le compteur par dictionnaire, en additionnant des tailles
    def bilan_par_type(self):
        bilan = {}
        for f in self.fichiers:
            ext = f.extension()
            bilan[ext] = bilan.get(ext, 0) + f.taille_mo
        return bilan


# étape 2 : on remplit l'inventaire à partir des données
inventaire = Inventaire()
for nom, taille in DONNEES:                     # chaque couple est déballé en deux variables
    inventaire.ajouter(Fichier(nom, taille))
print(f"{inventaire.nombre()} fichiers, {inventaire.taille_totale()} Mo")

# étape 3
print(inventaire.plus_gros().nom)

# étape 4
print(inventaire.par_extension(".jpg"))

# étape 5
for f in inventaire.gros_fichiers(100):
    print(f"{f.nom} ({f.taille_mo} Mo)")

# étape 6
print(inventaire.bilan_par_type())

# Ce qu'il faut remarquer : l'Inventaire ne manipule jamais des couples
# (nom, taille) « nus ». Il range des objets Fichier, et il leur DEMANDE ce
# dont il a besoin (f.extension(), f.taille_mo). Si demain on change la façon
# de calculer l'extension, on ne touche qu'à la classe Fichier.
