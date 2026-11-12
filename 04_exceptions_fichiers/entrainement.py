#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRAÎNEMENT — Module 04 : exceptions & fichiers   (série 2, après exercices.py)

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

 Ce fichier crée deux petits fichiers (essai.txt, journal.txt) dans le
 dossier courant. Tu peux les supprimer après.

 Lancer :   python3 entrainement.py
 Corrigé expliqué :  entrainement_solutions.py
"""


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 1 — Le chemin suivi dans un try / except
# ══════════════════════════════════════════════════════════════════════
#  Parmi les lettres A, B, C et D, lesquelles s'affichent, et dans quel ordre ?
#  ✏️ ma prédiction :

try:
    print("LIRE 1 → A")
    nombre = int("12a")
    print("LIRE 1 → B")
except ValueError:
    print("LIRE 1 → C")
print("LIRE 1 → D")


# ══════════════════════════════════════════════════════════════════════
#  👓 LIRE 2 — Les modes d'ouverture "w" et "a"
# ══════════════════════════════════════════════════════════════════════
#  Trois écritures à la suite dans le même fichier. Que contient-il à la fin ?
#  ✏️ ma prédiction :

with open("essai.txt", "w", encoding="utf-8") as f:
    f.write("un ")
with open("essai.txt", "a", encoding="utf-8") as f:
    f.write("deux ")
with open("essai.txt", "w", encoding="utf-8") as f:
    f.write("trois")
with open("essai.txt", "r", encoding="utf-8") as f:
    print("LIRE 2 →", f.read())


# ══════════════════════════════════════════════════════════════════════
#  🔧 MODIFIER 1 — Compléter le journal sans l'effacer
# ══════════════════════════════════════════════════════════════════════
#  Ce script écrit une ligne dans journal.txt puis affiche le fichier.
#  Ajoute une étape, entre l'écriture et la lecture, qui AJOUTE la ligne
#  "Mardi : courses" à la fin du fichier, sans effacer la première.
#
#  👀 Résultat attendu APRÈS ta modification :
#     Lundi : sport
#     Mardi : courses

with open("journal.txt", "w", encoding="utf-8") as f:
    f.write("Lundi : sport\n")

with open("journal.txt", "r", encoding="utf-8") as f:
    print(f.read().strip())


# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 1 — Additionner des saisies en ignorant les erreurs
# ══════════════════════════════════════════════════════════════════════
#  saisies  contient ce que des utilisateurs ont tapé. Additionne tout ce
#  qui est un nombre entier valide, ignore le reste, et affiche le total.
#
#  👀 Résultat attendu :
#     22

saisies = ["12", "abc", "7", "", "3"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 2 — Enregistrer une liste de courses
# ══════════════════════════════════════════════════════════════════════
#  Écris chaque élément de  courses  dans le fichier essai.txt, un par
#  ligne. Puis relis le fichier et affiche son nombre de lignes.
#
#  👀 Résultat attendu :
#     3

courses = ["pain", "lait", "oeufs"]

# ✏️ ton code ici :



# ══════════════════════════════════════════════════════════════════════
#  ✍️ ÉCRIRE 3 — Un produit qui n'est pas en stock
# ══════════════════════════════════════════════════════════════════════
#  Affiche la quantité en stock de  produit. S'il n'existe pas dans le
#  dictionnaire, affiche "Produit inconnu" au lieu de planter.
#  (Fais-le avec try / except : quelle exception lève une clé absente ?)
#
#  👀 Résultat attendu :
#     Produit inconnu

stock = {"pommes": 5, "poires": 2}
produit = "kiwis"

# ✏️ ton code ici :

