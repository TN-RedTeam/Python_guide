#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 01 : les bases

Corrigé commenté des exercices de exercices.py.
Lance-le pour vérifier que tout passe au vert :   python3 solutions.py
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé par toi-même.
"""


# ── NIVEAU 1 — REPRODUCTION ─────────────────────────────────────────

def presenter(nom, age):
    """Renvoie un texte de présentation avec une f-string."""
    return f"Je m'appelle {nom} et j'ai {age} ans."
    # Le f devant les guillemets dit à Python : remplace {nom} et {age}
    # par les valeurs réelles des variables.


def categorie_age(age):
    """Renvoie la catégorie d'âge en texte."""
    if age >= 18:
        return "Majeur"
    elif age >= 13:
        return "Adolescent"
    else:
        return "Enfant"
    # C'est l'exemple du cours (if/elif/else), avec return au lieu de print.
    # L'ordre compte : on teste le cas le plus grand d'abord (>= 18),
    # sinon le elif >= 13 attraperait aussi les majeurs.


# ── NIVEAU 2 — ADAPTATION ───────────────────────────────────────────

def est_pair(n):
    """True si n est pair."""
    return n % 2 == 0
    # n % 2 donne le reste de la division par 2.
    # Si le reste vaut 0, c'est pair → l'expression vaut True.
    # Sinon → False. Pas besoin de if : le test EST déjà True/False.


def convertir_temperature(celsius):
    """Convertit Celsius en Fahrenheit."""
    return celsius * 9 / 5 + 32
    # On applique la formule mathématique telle quelle.
    # Python respecte les priorités : * et / avant +, donc
    # celsius * 9 / 5 est calculé en premier, puis + 32.


# ── NIVEAU 3 — COMBINAISON ──────────────────────────────────────────

def somme_jusqua(n):
    """Somme des entiers de 1 à n inclus."""
    total = 0                         # on part de 0
    for i in range(1, n + 1):         # range(1, n+1) → 1, 2, ..., n
        total += i                    # total = total + i
    return total
    # Variante experte (une seule ligne) : return sum(range(1, n + 1))


def compter_pairs(limite):
    """Compte les nombres pairs de 1 à limite inclus."""
    compteur = 0                      # on part de 0
    for i in range(1, limite + 1):    # parcourt 1, 2, ..., limite
        if i % 2 == 0:               # si i est pair
            compteur += 1             # on en a trouvé un de plus
    return compteur
    # On combine : boucle for (répéter) + condition if (décider) + compteur.
    # Variante experte : return len([i for i in range(1, limite + 1) if i % 2 == 0])


# ── NIVEAU 4 — DÉFI ─────────────────────────────────────────────────

def fizzbuzz(n):
    """Renvoie Fizz / Buzz / FizzBuzz / le nombre, pour un n donné."""
    if n % 3 == 0 and n % 5 == 0:     # cas le PLUS précis testé en premier
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)                 # str() convertit le nombre en texte
    # PIÈGE classique : si on teste « par 3 » avant « par 3 ET par 5 »,
    # le nombre 15 (divisible par les deux) tombe dans « Fizz » et on
    # n'arrive jamais à « FizzBuzz ». D'où l'ordre : le plus précis d'abord.


# ════════════════════════════════════════════════════════════════════
#  Auto-vérification (identique à exercices.py)
# ════════════════════════════════════════════════════════════════════
def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Vérification — module 01 (solutions) ---\n")

    print("NIVEAU 1 — REPRODUCTION")
    res = [
        _check("presenter('Ada', 25)", presenter("Ada", 25), "Je m'appelle Ada et j'ai 25 ans."),
        _check("presenter('Bob', 17)", presenter("Bob", 17), "Je m'appelle Bob et j'ai 17 ans."),
        _check("categorie_age(10)", categorie_age(10), "Enfant"),
        _check("categorie_age(15)", categorie_age(15), "Adolescent"),
        _check("categorie_age(20)", categorie_age(20), "Majeur"),
    ]

    print("\nNIVEAU 2 — ADAPTATION")
    res += [
        _check("est_pair(4)", est_pair(4), True),
        _check("est_pair(7)", est_pair(7), False),
        _check("convertir_temperature(0)", convertir_temperature(0), 32.0),
        _check("convertir_temperature(100)", convertir_temperature(100), 212.0),
    ]

    print("\nNIVEAU 3 — COMBINAISON")
    res += [
        _check("somme_jusqua(5)", somme_jusqua(5), 15),
        _check("somme_jusqua(1)", somme_jusqua(1), 1),
        _check("compter_pairs(10)", compter_pairs(10), 5),
        _check("compter_pairs(7)", compter_pairs(7), 3),
    ]

    print("\nNIVEAU 4 — DÉFI")
    res += [
        _check("fizzbuzz(15)", fizzbuzz(15), "FizzBuzz"),
        _check("fizzbuzz(9)", fizzbuzz(9), "Fizz"),
        _check("fizzbuzz(10)", fizzbuzz(10), "Buzz"),
        _check("fizzbuzz(7)", fizzbuzz(7), "7"),
    ]

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
