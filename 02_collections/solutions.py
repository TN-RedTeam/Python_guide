#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 02 : les collections

Corrige commente. Lance :   python3 solutions.py   (doit etre tout vert).
⚠️ A consulter APRES avoir essaye exercices.py par toi-meme.
"""


# ── NIVEAU 1 — REPRODUCTION ─────────────────────────────────────────

def deuxieme_element(liste):
    """Deuxieme element : index 1 (le premier est a l'index 0)."""
    return liste[1]


def total_panier(panier):
    """Somme des prix (les valeurs du dict)."""
    return sum(panier.values())       # .values() donne toutes les valeurs


# ── NIVEAU 2 — ADAPTATION ───────────────────────────────────────────

def compter_occurrences(liste, valeur):
    """Compte les apparitions de `valeur` — pattern COMPTEUR."""
    total = 0
    for element in liste:
        if element == valeur:
            total += 1
    return total
    # Variante : return liste.count(valeur)


def produits_en_rupture(stock):
    """Liste des produits dont la quantite vaut 0 — pattern .items() + filtre."""
    resultat = []
    for produit, quantite in stock.items():
        if quantite == 0:
            resultat.append(produit)
    return resultat
    # Variante : return [p for p, q in stock.items() if q == 0]


# ── NIVEAU 3 — COMBINAISON ──────────────────────────────────────────

def sans_doublons_tries(liste):
    """Valeurs distinctes, triees — combine set() + sorted()."""
    return sorted(set(liste))     # set() retire les doublons, sorted() trie et renvoie une liste


def inverser_dictionnaire(d):
    """Echange cles et valeurs — combine .items() + construction d'un dict."""
    inverse = {}
    for cle, valeur in d.items():     # .items() donne (cle, valeur)
        inverse[valeur] = cle         # la valeur devient la cle, et inversement
    return inverse
    # Variante : return {v: k for k, v in d.items()}


# ── NIVEAU 4 — DEFI ─────────────────────────────────────────────────

def compter_mots_liste(mots):
    """Compte combien de fois chaque mot apparait — pattern compteur sur dict."""
    compteur = {}
    for mot in mots:
        compteur[mot] = compteur.get(mot, 0) + 1
    return compteur


# ════════════════════════════════════════════════════════════════════
#  Auto-verification
# ════════════════════════════════════════════════════════════════════
def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Verification — module 02 (solutions) ---")
    res = [
        _check("deuxieme_element", deuxieme_element(["a", "b", "c"]), "b"),
        _check("total_panier", total_panier({"pain": 1.2, "lait": 0.8}), 2.0),
        _check("compter_occurrences", compter_occurrences([1, 2, 2, 3, 2], 2), 3),
        _check("produits_en_rupture",
               produits_en_rupture({"pommes": 5, "poires": 0, "kiwis": 0}),
               ["poires", "kiwis"]),
        _check("sans_doublons_tries", sans_doublons_tries([3, 1, 2, 3, 1]), [1, 2, 3]),
        _check("inverser_dictionnaire", inverser_dictionnaire({"a": 1, "b": 2}), {1: "a", 2: "b"}),
        _check("compter_mots_liste", compter_mots_liste(["a", "b", "a"]), {"a": 2, "b": 1}),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
