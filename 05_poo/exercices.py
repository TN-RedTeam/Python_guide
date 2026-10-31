#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 05 : la POO (les classes)

──────────────────────────────────────────────────────────────────────
 DANS CE MODULE : tu écris des CLASSES (un moule à objets).
 Comme pour les fonctions, le point clé est :
   → C'est TOI qui crées l'objet, avec les valeurs de TON choix :
        f = Fichier("video.mp4", 700)
     Là, "video.mp4" et 700 entrent dans l'objet. Rien de caché.
 Donc chaque exercice te demande : (1) écrire la classe, (2) créer un
 objet toi-même avec des valeurs visibles, (3) appeler ses méthodes et
 afficher le résultat.
──────────────────────────────────────────────────────────────────────

 Tu lances, tu compares au « 👀 Résultat attendu ». Pas de correction
 automatique. Cours : README.md • Corrigé : solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Ta première classe : un Fichier
# ══════════════════════════════════════════════════════════════════════
#  Écris une classe  Fichier  avec :
#    - __init__(self, nom, taille_mo) qui range self.nom et self.taille_mo ;
#    - description(self) qui renvoie  "<nom> (<taille_mo> Mo)".
#  Puis crée un fichier et affiche sa description :
#    f = Fichier("video.mp4", 700)
#    print(f.description())
#
#  👀 Résultat attendu :
#     video.mp4 (700 Mo)

# ✏️ ton code ici (la classe, puis les 2 lignes qui créent et affichent) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Une classe avec des calculs
# ══════════════════════════════════════════════════════════════════════
#  Écris une classe  Rectangle  avec :
#    - __init__(self, largeur, hauteur) ;
#    - aire(self) qui renvoie largeur × hauteur ;
#    - perimetre(self) qui renvoie 2 × (largeur + hauteur).
#  Crée  Rectangle(3, 4)  et affiche son aire PUIS son périmètre.
#
#  👀 Résultat attendu :
#     12
#     14

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — L'héritage (réutiliser une classe)
# ══════════════════════════════════════════════════════════════════════
#  Un carré EST un rectangle à côtés égaux. Écris  Carre  qui HÉRITE de
#  Rectangle (celui de l'exercice 2, juste au-dessus) :
#    class Carre(Rectangle):
#        def __init__(self, cote):
#            super().__init__(cote, cote)   # réutilise le constructeur parent
#  aire() et perimetre() sont hérités : rien à réécrire.
#  Crée  Carre(5)  et affiche son aire PUIS son périmètre.
#
#  👀 Résultat attendu :
#     25
#     20

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Un objet qui garde un état : un compte (le défi)
# ══════════════════════════════════════════════════════════════════════
#  Écris  CompteBancaire  avec :
#    - __init__(self, solde=0) ;
#    - deposer(self, montant) : ajoute au solde ;
#    - retirer(self, montant) : retire, SAUF si le montant dépasse le solde
#      (dans ce cas, ne fait rien).
#  Puis joue ce scénario et affiche le solde final :
#    c = CompteBancaire(100)
#    c.deposer(50)      # 150
#    c.retirer(200)     # refusé (200 > 150) -> reste 150
#    c.retirer(30)      # 120
#    print(c.solde)
#
#  👀 Résultat attendu :
#     120

# ✏️ ton code ici :


