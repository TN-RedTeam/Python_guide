#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 06 : itérateurs & générateurs

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire, ligne par ligne.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit tes prédictions et essayé.
"""


# ── 👓 LIRE 1 — Une compréhension qui filtre ET transforme ───────────
print("LIRE 1 →", [n * 2 for n in [1, 2, 3, 4] if n > 2])
# Réponse : [6, 8]. En boucle, ça donnerait :
#     resultat = []
#     for n in [1, 2, 3, 4]:
#         if n > 2:                  # le filtre d'abord : on ne garde que 3 et 4
#             resultat.append(n * 2) # la transformation ensuite : 6 et 8


# ── 👓 LIRE 2 — Dans quel ordre s'exécute un générateur ? ────────────
def compte():
    print("LIRE 2 → début")
    yield 1
    print("LIRE 2 → milieu")
    yield 2

g = compte()                    # RIEN ne s'exécute : on a juste fabriqué le générateur
print("LIRE 2 → créé")
print("LIRE 2 →", next(g))      # 1er next : exécute jusqu'au 1er yield -> « début », puis 1
print("LIRE 2 →", next(g))      # 2e next : reprend après le yield -> « milieu », puis 2
# Ordre : créé, début, 1, milieu, 2.
# Un générateur est « paresseux » : son code n'avance que quand on lui demande
# la valeur suivante, et il se met en pause à chaque yield.


# ── 🔧 MODIFIER 1 — De la boucle à la compréhension ──────────────────
prix = [10, 25, 8, 40]
chers = [p - 5 for p in prix if p > 20]     # filtre (p > 20), puis transformation (p - 5)
print(chers)


# ── ✍️ ÉCRIRE 1 — La longueur de chaque nom de fichier ───────────────
noms = ["cv.pdf", "photo.jpg"]
print({nom: len(nom) for nom in noms})      # accolades + « clé: valeur » = dict en compréhension


# ── ✍️ ÉCRIRE 2 — Compter les PDF sans construire de liste ───────────
documents = ["cv.pdf", "photo.jpg", "facture.pdf", "notes.txt"]
print(sum(1 for d in documents if d.endswith(".pdf")))
# On additionne un 1 pour chaque fichier qui passe le filtre.


# ── ✍️ ÉCRIRE 3 — Un compte à rebours ────────────────────────────────
def compte_a_rebours(depart):
    n = depart
    while n >= 1:
        yield n             # livre n, puis se met en pause
        n -= 1

print(list(compte_a_rebours(3)))
# Variante : for n in range(depart, 0, -1): yield n
