#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — 🧭 Penser comme un dev : les 5 patterns de raisonnement

══════════════════════════════════════════════════════════════════════
 BUT DU FICHIER
 Cinq fonctions à trous. Chacune est UN des patterns vus dans le cours
 (accumulateur, compteur, recherche, filtre, champion). Pour chacune :
   1. Lis le pseudo-code donné en commentaire.
   2. Traduis-le en Python, à la place des « ... ».
 Puis lance : ✅ = réussi, ❌ = à corriger. Ton code est sauvegardé ici.
══════════════════════════════════════════════════════════════════════

▶ La méthode, à chaque fois : pseudo-code d'abord (il est déjà écrit !),
  puis traduction ligne à ligne. Un jeu d'essai est donné en exemple.
"""


# ─────────────────────────────────────────────────────────────────────
# 1. ACCUMULATEUR — « faire un total »
#    Pseudo-code :
#        total ← 0
#        POUR chaque n DANS nombres : total ← total + n
#        RENVOYER total
#    Exemple : somme_liste([2, 5, 3]) → 10
# ─────────────────────────────────────────────────────────────────────
def somme_liste(nombres):
    total = 0
    for n in nombres:
        ...            # ajoute n au total
    return total


# ─────────────────────────────────────────────────────────────────────
# 2. COMPTEUR — « combien y en a-t-il qui… ? »
#    Compte combien de mots ont plus de 3 lettres.
#    Pseudo-code :
#        compte ← 0
#        POUR chaque mot DANS mots :
#            SI longueur(mot) > 3 : compte ← compte + 1
#        RENVOYER compte
#    Exemple : compter_mots_longs(["ok", "chien", "a", "table"]) → 2
# ─────────────────────────────────────────────────────────────────────
def compter_mots_longs(mots):
    compte = 0
    for mot in mots:
        ...            # si le mot fait plus de 3 lettres, incrémente compte
    return compte


# ─────────────────────────────────────────────────────────────────────
# 3. RECHERCHE + DRAPEAU — « est-ce que X existe ? » (renvoie True/False)
#    Pseudo-code :
#        trouve ← Faux
#        POUR chaque x DANS nombres :
#            SI x == cible : trouve ← Vrai
#        RENVOYER trouve
#    Exemple : contient([4, 8, 15], 8) → True ; contient([4, 8], 9) → False
# ─────────────────────────────────────────────────────────────────────
def contient(nombres, cible):
    trouve = False
    for x in nombres:
        ...            # si x est la cible, passe trouve à True
    return trouve


# ─────────────────────────────────────────────────────────────────────
# 4. FILTRE — « garder seulement ceux qui… »
#    Renvoie une NOUVELLE liste avec seulement les nombres pairs.
#    Pseudo-code :
#        gardes ← liste vide
#        POUR chaque n DANS nombres :
#            SI n est pair : ajouter n à gardes
#        RENVOYER gardes
#    Exemple : garder_pairs([1, 2, 3, 4]) → [2, 4]
#    (rappel : « n est pair » s'écrit  n % 2 == 0)
# ─────────────────────────────────────────────────────────────────────
def garder_pairs(nombres):
    gardes = []
    for n in nombres:
        ...            # si n est pair, ajoute-le à gardes (gardes.append(n))
    return gardes


# ─────────────────────────────────────────────────────────────────────
# 5. CHAMPION (max) — « le plus grand » + CAS LIMITE
#    Renvoie le plus grand nombre. Si la liste est VIDE, renvoie None.
#    Pseudo-code :
#        SI nombres est vide : RENVOYER None
#        meilleur ← premier élément
#        POUR chaque n DANS nombres :
#            SI n > meilleur : meilleur ← n
#        RENVOYER meilleur
#    Exemple : plus_grand([3, 9, 2]) → 9 ; plus_grand([]) → None
# ─────────────────────────────────────────────────────────────────────
def plus_grand(nombres):
    if not nombres:
        return None
    meilleur = nombres[0]
    for n in nombres:
        ...            # si n est plus grand que meilleur, mets meilleur à jour
    return meilleur


# ═══════════════════ AUTO-CORRECTION (ne pas modifier) ═══════════════════
def verifie(fonction, *arguments, attendu):
    try:
        obtenu = fonction(*arguments)
    except Exception as e:
        obtenu = f"ERREUR: {e}"
    ok = (obtenu == attendu)
    args_lisibles = ", ".join(repr(a) for a in arguments)
    print(f"{'✅' if ok else '❌'} {fonction.__name__}({args_lisibles})  ->  {attendu!r}")
    if not ok:
        print(f"     ⚠️  ton code a renvoyé : {obtenu!r}")
    return ok


if __name__ == "__main__":
    print("--- 🧭 Penser comme un dev : les 5 patterns ---\n")
    resultats = [
        verifie(somme_liste, [2, 5, 3],                 attendu=10),
        verifie(somme_liste, [],                         attendu=0),
        verifie(compter_mots_longs, ["ok", "chien", "a", "table"], attendu=2),
        verifie(contient, [4, 8, 15], 8,                 attendu=True),
        verifie(contient, [4, 8, 15], 9,                 attendu=False),
        verifie(garder_pairs, [1, 2, 3, 4],              attendu=[2, 4]),
        verifie(plus_grand, [3, 9, 2],                   attendu=9),
        verifie(plus_grand, [],                          attendu=None),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
