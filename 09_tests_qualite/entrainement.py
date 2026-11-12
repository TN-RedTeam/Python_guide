#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 09 : tests & qualité   (série 2, après exercices.py)

──────────────────────────────────────────────────────────────────────
 Trois façons de travailler la même matière :
   👓 LIRE      : le code est donné. Écris ce qu'il va afficher AVANT
                 de lancer le fichier.
   🔧 MODIFIER  : un petit script qui marche déjà. Change-le pour
                 obtenir le nouveau résultat demandé.
   ✍️ ÉCRIRE    : comme dans exercices.py, mais sans indice ni liste
                 d'outils.
──────────────────────────────────────────────────────────────────────

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Le test qui révèle le bug
# ══════════════════════════════════════════════════════════════════════
#  Cette fonction dit si une personne est majeure. Deux tests la vérifient.
#  Quelles lignes s'affichent ? (Regarde bien le 2e test : 18 ans tout juste.)
#  ✏️ ma prédiction :

def est_majeur(age):
    return age > 18

try:
    assert est_majeur(20) == True
    print("LIRE 1 → test A passé")
    assert est_majeur(18) == True
    print("LIRE 1 → test B passé")
except AssertionError:
    print("LIRE 1 → un test a échoué")


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — Ajouter les tests qui manquent
# ══════════════════════════════════════════════════════════════════════
#  Cette fonction n'a qu'un seul test, sur un cas « normal ». Ajoute deux
#  tests de CAS LIMITES : une remise de 0 % (le prix ne change pas) et une
#  remise de 100 % (l'article devient gratuit). Puis mets le message à jour.
#
#  👀 Résultat attendu APRÈS ta modification :
#     remise OK (3 tests)

def prix_remise(prix, pourcentage):
    return prix - prix * pourcentage / 100

assert prix_remise(100, 20) == 80
print("remise OK (1 test)")


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — est_pair + ses tests
# ══════════════════════════════════════════════════════════════════════
#  1) Écris  est_pair(n)  qui renvoie True si n est pair, False sinon.
#  2) Teste-la avec au moins 3 assert : un nombre pair, un impair, et le
#     cas limite 0. Puis affiche "est_pair OK".
#
#  👀 Résultat attendu :
#     est_pair OK

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — compter_voyelles + ses tests
# ══════════════════════════════════════════════════════════════════════
#  1) Écris  compter_voyelles(mot)  qui renvoie le nombre de voyelles
#     (a, e, i, o, u) du mot.
#  2) Teste-la avec au moins 3 assert, dont un mot SANS voyelle et le
#     texte vide "". Puis affiche "voyelles OK".
#
#  👀 Résultat attendu :
#     voyelles OK

# ✏️ ton code ici :

