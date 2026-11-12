#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 06 : itérateurs & générateurs   (série 2, après exercices.py)

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
#  👓 LIRE 1 — Une compréhension qui filtre ET transforme
# ══════════════════════════════════════════════════════════════════════
#  Quelle liste est affichée ? (Astuce : réécris-la en boucle for dans ta tête.)
#  ✏️ ma prédiction :

print("LIRE 1 →", [n * 2 for n in [1, 2, 3, 4] if n > 2])


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 2 — Dans quel ordre s'exécute un générateur ?
# ══════════════════════════════════════════════════════════════════════
#  Cinq lignes vont s'afficher. Dans quel ORDRE ? (Attention : créer un
#  générateur n'exécute pas son code.)
#  ✏️ ma prédiction :

def compte():
    print("LIRE 2 → début")
    yield 1
    print("LIRE 2 → milieu")
    yield 2

g = compte()
print("LIRE 2 → créé")
print("LIRE 2 →", next(g))
print("LIRE 2 →", next(g))


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — De la boucle à la compréhension
# ══════════════════════════════════════════════════════════════════════
#  Ce script construit la liste des prix supérieurs à 20 €, avec une
#  boucle. Réécris-le en UNE compréhension de liste — et profites-en pour
#  retirer 5 € à chaque prix gardé.
#
#  👀 Résultat attendu APRÈS ta modification :
#     [20, 35]

prix = [10, 25, 8, 40]
chers = []
for p in prix:
    if p > 20:
        chers.append(p)
print(chers)


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — La longueur de chaque nom de fichier
# ══════════════════════════════════════════════════════════════════════
#  Construis, en une ligne, un DICTIONNAIRE qui associe chaque nom de
#  fichier à son nombre de caractères, puis affiche-le.
#
#  👀 Résultat attendu :
#     {'cv.pdf': 6, 'photo.jpg': 9}

noms = ["cv.pdf", "photo.jpg"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — Compter les PDF sans construire de liste
# ══════════════════════════════════════════════════════════════════════
#  Affiche combien de fichiers de  documents  sont des ".pdf", en une
#  ligne, sans boucle for classique et sans liste intermédiaire.
#
#  👀 Résultat attendu :
#     2

documents = ["cv.pdf", "photo.jpg", "facture.pdf", "notes.txt"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 3 — Un compte à rebours
# ══════════════════════════════════════════════════════════════════════
#  Écris un générateur  compte_a_rebours(depart)  qui produit les nombres
#  de  depart  jusqu'à 1, un par un. Affiche tout ce qu'il produit pour
#  depart = 3, sous forme de liste.
#
#  👀 Résultat attendu :
#     [3, 2, 1]

# ✏️ ton code ici :

