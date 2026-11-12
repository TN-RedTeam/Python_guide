#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 01 : les bases

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire, ligne par ligne.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit tes prédictions et essayé.
"""


# ── 👓 LIRE 1 — Une variable qui change ──────────────────────────────
stock = 10              # stock vaut 10
stock = stock - 3       # à droite : 10 - 3 = 7 ; stock vaut maintenant 7
stock = stock * 2       # à droite : 7 * 2 = 14 ; stock vaut maintenant 14
print("LIRE 1 →", stock)
# Réponse : 14. Python calcule TOUJOURS le côté droit du = en premier, avec
# l'ancienne valeur, puis range le résultat dans la variable.


# ── 👓 LIRE 2 — Une boucle avec une condition ────────────────────────
total = 0
for i in range(1, 6):       # i vaut 1, 2, 3, 4, 5 (6 est exclu)
    if i % 2 == 0:          # vrai seulement pour 2 et 4
        total = total + i   # tour i=2 : total = 2 ; tour i=4 : total = 6
print("LIRE 2 →", total)
# Réponse : 6. Les tours i=1, 3 et 5 ne changent rien : le if est faux.


# ── 🔧 MODIFIER 1 — L'ascenseur ──────────────────────────────────────
for etage in range(2, 7, 2):    # de 2 à 6 inclus (7 exclu), de 2 en 2
    print(f"Étage {etage}")
# Autre solution valable : garder range(1, 7) et ajouter  if etage % 2 == 0:


# ── ✍️ ÉCRIRE 1 — Le prix soldé ──────────────────────────────────────
prix = 80
reduction = 25
prix_solde = prix - prix * reduction / 100     # 80 - 20.0 = 60.0
print(f"Prix soldé : {prix_solde} €")


# ── ✍️ ÉCRIRE 2 — La mention ─────────────────────────────────────────
moyenne = 13.5
if moyenne >= 16:
    print("Très bien")
elif moyenne >= 14:
    print("Bien")
elif moyenne >= 12:
    print("Assez bien")
elif moyenne >= 10:
    print("Passable")
else:
    print("Recalé")
# On part du seuil le plus haut : dès qu'un test est vrai, les suivants sont ignorés.


# ── ✍️ ÉCRIRE 3 — Combien de semaines pour économiser ? ──────────────
economies = 20
par_semaine = 15
objectif = 100
semaines = 0
while economies < objectif:      # on ne sait pas d'avance combien de tours -> while
    economies = economies + par_semaine
    semaines = semaines + 1
print(semaines)
# 20 -> 35 -> 50 -> 65 -> 80 -> 95 -> 110 : il a fallu 6 semaines.
