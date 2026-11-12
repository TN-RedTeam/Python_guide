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

 La ligne « 🧰 Outils » te dit QUOI utiliser, pas comment l'écrire.

 BLOQUÉ ?  1) relis le cours (README.md)
           2) lis l'indice de l'exercice, tout EN BAS de ce fichier
           3) en dernier recours : solutions.py

 Lancer :   python3 exercices.py
"""


# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 1 — Ta première classe : un Fichier
# ══════════════════════════════════════════════════════════════════════
#  Écris une classe  Fichier  qui retient un nom et une taille en Mo, avec
#  une méthode  description()  qui renvoie  "<nom> (<taille> Mo)".
#  Puis crée le fichier "video.mp4" de 700 Mo et affiche sa description.
#  🧰 Outils : class, __init__, self, une méthode, une f-string
#
#  👀 Résultat attendu :
#     video.mp4 (700 Mo)

# ✏️ ton code ici (la classe d'abord, puis la création de l'objet et le print) :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 2 — Une classe avec des calculs
# ══════════════════════════════════════════════════════════════════════
#  Écris une classe  Rectangle  (largeur, hauteur) avec deux méthodes :
#    - aire()       -> largeur × hauteur
#    - perimetre()  -> 2 × (largeur + hauteur)
#  Crée un rectangle de 3 sur 4 et affiche son aire PUIS son périmètre.
#  🧰 Outils : class, __init__, self, deux méthodes avec return
#
#  👀 Résultat attendu :
#     12
#     14

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 3 — L'héritage (réutiliser une classe)
# ══════════════════════════════════════════════════════════════════════
#  Un carré EST un rectangle dont les côtés sont égaux. Écris une classe
#  Carre  qui HÉRITE de Rectangle (celui de l'exercice 2) et qui se crée
#  avec UN seul nombre : le côté. N'y réécris ni aire() ni perimetre().
#  Crée un carré de côté 5 et affiche son aire PUIS son périmètre.
#  🧰 Outils : class Enfant(Parent), super().__init__
#
#  👀 Résultat attendu :
#     25
#     20

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  EXERCICE 4 — Un objet qui garde un état : un compte (le défi)
# ══════════════════════════════════════════════════════════════════════
#  Écris  CompteBancaire  avec :
#    - un solde de départ (0 si on n'en donne pas) ;
#    - deposer(montant) : ajoute au solde ;
#    - retirer(montant) : retire, SAUF si le montant dépasse le solde
#      (dans ce cas, le compte ne change pas).
#  Puis joue ce scénario et affiche le solde final :
#    ouvrir un compte avec 100  →  déposer 50  →  retirer 200 (refusé)
#    →  retirer 30  →  afficher le solde
#  🧰 Outils : une valeur par défaut dans __init__, self.solde, if
#
#  👀 Résultat attendu :
#     120

# ✏️ ton code ici :




# ══════════════════════════════════════════════════════════════════════
#  💡 INDICES — à ne lire QUE si tu bloques (cherche d'abord 10 minutes)
# ══════════════════════════════════════════════════════════════════════
#
#  Exercice 1 : __init__(self, nom, taille_mo) RANGE les valeurs dans
#               l'objet (self.nom = nom, …). description(self) les RELIT
#               avec self.nom et self.taille_mo. Pour créer l'objet :
#               f = Fichier("video.mp4", 700), puis print(f.description()).
#
#  Exercice 2 : même schéma que l'exercice 1. Chaque méthode fait un return
#               d'un calcul sur self.largeur et self.hauteur.
#
#  Exercice 3 : class Carre(Rectangle): et un seul __init__(self, cote) qui
#               appelle le constructeur du parent en lui donnant le côté
#               DEUX fois : super().__init__(cote, cote).
#
#  Exercice 4 : def __init__(self, solde=0). deposer fait self.solde += montant.
#               Dans retirer, teste d'abord si montant > self.solde : si oui,
#               return tout de suite (rien ne change) ; sinon soustrais.
#               Le scénario : c = CompteBancaire(100), c.deposer(50), etc.
