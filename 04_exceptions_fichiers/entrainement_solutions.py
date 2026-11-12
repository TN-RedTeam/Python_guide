#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 04 : exceptions & fichiers

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire, ligne par ligne.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit tes prédictions et essayé.
"""


# ── 👓 LIRE 1 — Le chemin suivi dans un try / except ─────────────────
try:
    print("LIRE 1 → A")         # s'exécute normalement
    nombre = int("12a")         # ERREUR ici (ValueError) -> on SAUTE au except
    print("LIRE 1 → B")         # jamais exécutée
except ValueError:
    print("LIRE 1 → C")         # exécutée parce que l'erreur est une ValueError
print("LIRE 1 → D")             # hors du try : exécutée dans tous les cas
# Réponse : A, C, D. Dès qu'une ligne du try échoue, le reste du try est abandonné.


# ── 👓 LIRE 2 — Les modes d'ouverture "w" et "a" ─────────────────────
with open("essai.txt", "w", encoding="utf-8") as f:
    f.write("un ")              # "w" : crée le fichier -> « un »
with open("essai.txt", "a", encoding="utf-8") as f:
    f.write("deux ")            # "a" : ajoute à la fin -> « un deux »
with open("essai.txt", "w", encoding="utf-8") as f:
    f.write("trois")            # "w" : VIDE le fichier puis écrit -> « trois »
with open("essai.txt", "r", encoding="utf-8") as f:
    print("LIRE 2 →", f.read())
# Réponse : trois. Le dernier "w" a effacé tout ce qu'il y avait avant.


# ── 🔧 MODIFIER 1 — Compléter le journal sans l'effacer ──────────────
with open("journal.txt", "w", encoding="utf-8") as f:
    f.write("Lundi : sport\n")

with open("journal.txt", "a", encoding="utf-8") as f:     # "a" = ajout à la fin
    f.write("Mardi : courses\n")

with open("journal.txt", "r", encoding="utf-8") as f:
    print(f.read().strip())


# ── ✍️ ÉCRIRE 1 — Additionner des saisies en ignorant les erreurs ────
saisies = ["12", "abc", "7", "", "3"]
total = 0
for saisie in saisies:
    try:
        total = total + int(saisie)     # int("abc") et int("") lèvent une ValueError
    except ValueError:
        pass                            # pass = « ne rien faire » : on ignore cette saisie
print(total)
# Le try est DANS la boucle : une saisie invalide n'arrête pas les suivantes.


# ── ✍️ ÉCRIRE 2 — Enregistrer une liste de courses ───────────────────
courses = ["pain", "lait", "oeufs"]
with open("essai.txt", "w", encoding="utf-8") as f:
    for article in courses:
        f.write(article + "\n")         # \n = retour à la ligne après chaque article
with open("essai.txt", "r", encoding="utf-8") as f:
    print(len(f.readlines()))


# ── ✍️ ÉCRIRE 3 — Un produit qui n'est pas en stock ──────────────────
stock = {"pommes": 5, "poires": 2}
produit = "kiwis"
try:
    print(stock[produit])               # une clé absente lève une KeyError
except KeyError:
    print("Produit inconnu")
