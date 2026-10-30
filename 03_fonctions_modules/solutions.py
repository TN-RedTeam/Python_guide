#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 03 : fonctions & modules

Corrige commente. Lance :   python3 solutions.py   (doit etre tout vert).
⚠️ N'ouvre ce fichier qu'APRES avoir vraiment essaye par toi-meme.
"""


# ── NIVEAU 1 — REPRODUCTION ────────────────────────────────────────


def salutation(nom, politesse="Bonjour"):
    """Salutation avec politesse par defaut."""
    return f"{politesse} {nom} !"
    # politesse="Bonjour" : si on ne passe pas le 2e argument, c'est "Bonjour".
    # La f-string assemble les morceaux : f"{politesse} {nom} !"


def compter_mots(phrase):
    """Nombre de mots (separes par des espaces)."""
    return len(phrase.split())
    # .split() decoupe "le chat dort" en ["le", "chat", "dort"]
    # len() compte : 3 elements → 3


# ── NIVEAU 2 — ADAPTATION ──────────────────────────────────────────


def aire_rectangle(largeur, hauteur=1):
    """Aire d'un rectangle, avec hauteur par defaut a 1."""
    return largeur * hauteur
    # Meme principe que salutation : hauteur a une valeur par defaut.
    # aire_rectangle(7) → 7 * 1 = 7
    # aire_rectangle(5, 3) → 5 * 3 = 15


def moyenne(*notes):
    """Moyenne d'un nombre variable de notes (0 si aucune)."""
    if not notes:                       # tuple vide → "si aucune note"
        return 0                        # on evite la division par zero
    return sum(notes) / len(notes)      # somme / nombre d'elements
    # *notes ramasse tout dans un tuple : moyenne(10, 20) → notes = (10, 20)
    # sum((10, 20)) = 30, len((10, 20)) = 2, 30 / 2 = 15.0


# ── NIVEAU 3 — COMBINAISON ─────────────────────────────────────────


def applique(fonction, liste):
    """Applique une fonction a chaque element."""
    resultats = []
    for x in liste:
        resultats.append(fonction(x))   # on APPELLE la fonction recue, sur chaque element
    return resultats
    # fonction est un parametre comme un autre, sauf que c'est une FONCTION.
    # On l'appelle avec () : fonction(x) renvoie le resultat pour cet element.
    # Variante courte (module 06) : return [fonction(x) for x in liste]


# ── NIVEAU 4 — DEFI ────────────────────────────────────────────────


def trier_par_longueur(mots):
    """Trie une liste de mots par longueur (du plus court au plus long)."""
    return sorted(mots, key=lambda mot: len(mot))
    # sorted() renvoie une NOUVELLE liste triee.
    # key=lambda mot: len(mot) dit : "pour comparer, regarde la longueur".
    # lambda mot: len(mot) est une mini-fonction : elle prend mot, renvoie len(mot).


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
    print("--- Verification — module 03 (solutions) ---\n")
    print("NIVEAU 1 — REPRODUCTION")
    res = [
        _check("salutation('Ada')", salutation("Ada"), "Bonjour Ada !"),
        _check("salutation('Ada','Salut')", salutation("Ada", "Salut"), "Salut Ada !"),
        _check("compter_mots('le chat dort')", compter_mots("le chat dort"), 3),
    ]
    print("\nNIVEAU 2 — ADAPTATION")
    res += [
        _check("aire_rectangle(5, 3)", aire_rectangle(5, 3), 15),
        _check("aire_rectangle(7)", aire_rectangle(7), 7),
        _check("moyenne(10, 20)", moyenne(10, 20), 15.0),
        _check("moyenne()", moyenne(), 0),
    ]
    print("\nNIVEAU 3 — COMBINAISON")
    res += [
        _check("applique(x2, [1,2,3])", applique(lambda x: x * 2, [1, 2, 3]), [2, 4, 6]),
    ]
    print("\nNIVEAU 4 — DEFI")
    res += [
        _check("trier_par_longueur(['python','go','rust'])",
               trier_par_longueur(["python", "go", "rust"]),
               ["go", "rust", "python"]),
        _check("trier_par_longueur(['a','bb','ccc','dd'])",
               trier_par_longueur(["a", "bb", "ccc", "dd"]),
               ["a", "bb", "dd", "ccc"]),
    ]
    print(f"\n{sum(res)}/{len(res)} reussis")


if __name__ == "__main__":
    _verifier()
