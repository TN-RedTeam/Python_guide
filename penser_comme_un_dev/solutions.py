#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — 🧭 Penser comme un dev : les 5 patterns

⚠️ Le corrigé n'aide que si tu as VRAIMENT essayé d'abord. Compare-le à TA
version : l'écart entre les deux, c'est ta leçon.
"""


# 1. ACCUMULATEUR
def somme_liste(nombres):
    total = 0
    for n in nombres:
        total = total + n
    return total


# 2. COMPTEUR
def compter_mots_longs(mots):
    compte = 0
    for mot in mots:
        if len(mot) > 3:
            compte = compte + 1
    return compte


# 3. RECHERCHE + DRAPEAU
def contient(nombres, cible):
    trouve = False
    for x in nombres:
        if x == cible:
            trouve = True
    return trouve


# 4. FILTRE
def garder_pairs(nombres):
    gardes = []
    for n in nombres:
        if n % 2 == 0:
            gardes.append(n)
    return gardes


# 5. CHAMPION (max) + cas limite
def plus_grand(nombres):
    if not nombres:
        return None
    meilleur = nombres[0]
    for n in nombres:
        if n > meilleur:
            meilleur = n
    return meilleur


def verifie(fonction, *arguments, attendu):
    try:
        obtenu = fonction(*arguments)
    except Exception as e:
        obtenu = f"ERREUR: {e}"
    ok = (obtenu == attendu)
    args_lisibles = ", ".join(repr(a) for a in arguments)
    print(f"{'✅' if ok else '❌'} {fonction.__name__}({args_lisibles})  ->  {attendu!r}")
    return ok


if __name__ == "__main__":
    resultats = [
        verifie(somme_liste, [2, 5, 3], attendu=10),
        verifie(somme_liste, [], attendu=0),
        verifie(compter_mots_longs, ["ok", "chien", "a", "table"], attendu=2),
        verifie(contient, [4, 8, 15], 8, attendu=True),
        verifie(contient, [4, 8, 15], 9, attendu=False),
        verifie(garder_pairs, [1, 2, 3, 4], attendu=[2, 4]),
        verifie(plus_grand, [3, 9, 2], attendu=9),
        verifie(plus_grand, [], attendu=None),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
