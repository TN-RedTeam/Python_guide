#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Entraînement du module 09 : tests & qualité

Pour les exercices LIRE, le plus important n'est pas la réponse mais le
RAISONNEMENT : il est écrit en commentaire.
⚠️ N'ouvre ce fichier qu'APRÈS avoir écrit ta prédiction et essayé.
"""


# ── 👓 LIRE 1 — Le test qui révèle le bug ────────────────────────────
def est_majeur(age):
    return age > 18                 # BUG : à 18 ans pile, on EST majeur (il faudrait >=)

try:
    assert est_majeur(20) == True   # 20 > 18 -> True : le test passe
    print("LIRE 1 → test A passé")
    assert est_majeur(18) == True   # 18 > 18 -> False : AssertionError
    print("LIRE 1 → test B passé")  # jamais atteinte
except AssertionError:
    print("LIRE 1 → un test a échoué")
# Réponse : « test A passé », puis « un test a échoué ».
# Le test sur un cas « normal » (20 ans) ne voit pas le bug. C'est le test
# À LA FRONTIÈRE (18 ans) qui le révèle. D'où la règle : teste toujours les
# cas limites.


# ── 🔧 MODIFIER 1 — Ajouter les tests qui manquent ───────────────────
def prix_remise(prix, pourcentage):
    return prix - prix * pourcentage / 100

assert prix_remise(100, 20) == 80       # cas normal
assert prix_remise(100, 0) == 100       # cas limite : aucune remise
assert prix_remise(100, 100) == 0       # cas limite : tout est offert
print("remise OK (3 tests)")


# ── ✍️ ÉCRIRE 1 — est_pair + ses tests ───────────────────────────────
def est_pair(n):
    return n % 2 == 0

assert est_pair(4) == True
assert est_pair(7) == False
assert est_pair(0) == True              # cas limite : 0 est pair
print("est_pair OK")


# ── ✍️ ÉCRIRE 2 — compter_voyelles + ses tests ───────────────────────
def compter_voyelles(mot):
    total = 0
    for lettre in mot:
        if lettre in "aeiou":
            total += 1
    return total

assert compter_voyelles("bonjour") == 3
assert compter_voyelles("rythm") == 0   # aucun a, e, i, o, u
assert compter_voyelles("") == 0        # cas limite : texte vide
print("voyelles OK")
