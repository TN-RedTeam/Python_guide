#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 05 : la POO (les classes)

Le corrigé des exercices, avec le code complet et commenté.
Lance-le (python3 solutions.py) pour voir tous les résultats attendus.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""


# ── EXERCICE 1 — Ta première classe ──────────────────────────────────
class Animal:
    def __init__(self, nom, cri):
        self.nom = nom              # on RANGE les valeurs reçues dans l'objet
        self.cri = cri
    def parler(self):
        return f"{self.nom} fait {self.cri} !"   # on RELIT self.nom et self.cri

rex = Animal("Rex", "Wouf")         # c'est TOI qui donnes "Rex" et "Wouf"
print(rex.parler())                 # Rex fait Wouf !


# ── EXERCICE 2 — Une classe avec des calculs ─────────────────────────
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    def aire(self):
        return self.largeur * self.hauteur
    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)

r = Rectangle(3, 4)
print(r.aire())        # 12
print(r.perimetre())   # 14


# ── EXERCICE 3 — L'héritage ──────────────────────────────────────────
class Carre(Rectangle):             # Carre hérite de Rectangle
    def __init__(self, cote):
        super().__init__(cote, cote)   # même côté pour largeur ET hauteur
    # aire() et perimetre() viennent de Rectangle : rien à réécrire.

c = Carre(5)
print(c.aire())        # 25
print(c.perimetre())   # 20


# ── EXERCICE 4 — Un objet qui garde un état ──────────────────────────
class CompteBancaire:
    def __init__(self, solde=0):
        self.solde = solde
    def deposer(self, montant):
        self.solde += montant
    def retirer(self, montant):
        if montant > self.solde:    # garde : on refuse si le solde est insuffisant
            return                  # on quitte sans rien changer
        self.solde -= montant

compte = CompteBancaire(100)
compte.deposer(50)     # 150
compte.retirer(200)    # refusé (200 > 150) -> reste 150
compte.retirer(30)     # 120
print(compte.solde)    # 120
