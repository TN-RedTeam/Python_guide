#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PAS À PAS — Module 01 : les bases  (style W3Schools / Codecademy)

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ? (lis ces 6 lignes, c'est important)
 Ici, le code est DÉJÀ écrit à 95 %. Il reste juste UN petit trou noté
 « ____ » à chaque étape. Tu remplaces ce « ____ » par le bon bout, tu
 relances le fichier, et tu vois ✅ ou ❌ tout de suite.
 → Tu ne pars JAMAIS d'une page blanche. Tu complètes, c'est tout.
 → Ça commence par remplir UN SEUL MOT. Ça monte tout doucement.
══════════════════════════════════════════════════════════════════════

▶ COMMENT FAIRE (le même geste à chaque étape) :
    1. Lis la CONSIGNE affichée quand tu lances le fichier.
    2. Trouve la fonction (etape_01, etape_02, …) ici dans le fichier.
    3. Remplace le « ____ » par ce que dit l'indice juste à côté.
    4. Relance :  python3 pas_a_pas.py   → tu vois ton ✅.
    5. Passe à l'étape suivante. Une étape = un petit trou = 10 secondes.

▶ EXEMPLE DU GESTE :
    Au départ :   return f"Bonjour {____}"
    L'indice dit : remplace ____ par  nom
    Tu écris :    return f"Bonjour {nom}"
    → ✅

▶ SI TU VOIS « tu n'as pas encore rempli le trou » : c'est NORMAL au
  début, ça veut juste dire que ce « ____ » attend encore ta réponse.

▶ 💾 Pour ne pas perdre ton travail lors d'un « git pull », tu peux copier
  le fichier :   cp pas_a_pas.py pas_a_pas_perso.py   (puis lance la copie)

▶ Quand tout est ✅ ici, tu seras PRÊT pour exercices.py (le niveau au-dessus).
"""


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 01 — écrire une variable dans un texte (f-string)
#  Remplace  ____  par :  nom
# ══════════════════════════════════════════════════════════════════════
def etape_01(nom):
    return f"Bonjour {____}"


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 02 — deux variables dans un texte
#  Remplace le 1er  ____  par :  nom      et le 2e  ____  par :  age
# ══════════════════════════════════════════════════════════════════════
def etape_02(nom, age):
    return f"{____} a {____} ans"


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 03 — utiliser un paramètre dans un calcul
#  La fonction reçoit un prix et doit renvoyer ce prix + 2.
#  Remplace  ____  par :  prix
# ══════════════════════════════════════════════════════════════════════
def etape_03(prix):
    return ____ + 2


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 04 — répondre True / False (une comparaison)
#  Renvoie True si l'âge est 18 ou plus.
#  Remplace  ____  par :  age
# ══════════════════════════════════════════════════════════════════════
def etape_04(age):
    return ____ >= 18


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 05 — tester si un nombre est pair (le modulo %)
#  « n % 2 » donne le reste. Si ce reste vaut 0, n est pair.
#  Remplace  ____  par :  0
# ══════════════════════════════════════════════════════════════════════
def etape_05(n):
    return n % 2 == ____


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 06 — choisir entre deux réponses (if / else)
#  La structure if/else est DÉJÀ écrite. Remplis juste les 2 réponses.
#  1er  ____  :  "Majeur"       2e  ____  :  "Mineur"
#  (n'oublie pas les guillemets : c'est du texte)
# ══════════════════════════════════════════════════════════════════════
def etape_06(age):
    if age >= 18:
        return ____
    else:
        return ____


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 07 — additionner de 1 à n (une boucle for)
#  La boucle est écrite. Il manque juste où elle s'arrête.
#  On veut aller jusqu'à n INCLUS, donc on s'arrête à n + 1.
#  Remplace  ____  par :  n + 1
# ══════════════════════════════════════════════════════════════════════
def etape_07(n):
    total = 0
    for i in range(1, ____):
        total = total + i
    return total


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 08 — compter les nombres pairs (boucle + compteur)
#  Tout est écrit. À chaque nombre pair, on ajoute 1 au compteur.
#  Remplace  ____  par :  1
# ══════════════════════════════════════════════════════════════════════
def etape_08(limite):
    compteur = 0
    for i in range(1, limite + 1):
        if i % 2 == 0:
            compteur = compteur + ____
    return compteur


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 09 — écrire la condition toi-même
#  On veut renvoyer "pair" ou "impair". Le if/else est écrit.
#  Il manque la condition : un nombre est pair si  n % 2  vaut 0.
#  Remplace  ____  par :  n % 2
# ══════════════════════════════════════════════════════════════════════
def etape_09(n):
    if ____ == 0:
        return "pair"
    else:
        return "impair"


# ══════════════════════════════════════════════════════════════════════
#  ÉTAPE 10 — la ligne complète (celle qui te bloquait au début !)
#  Plus d'aide dans le code : à toi d'écrire TOUTE la f-string.
#  Objectif :  etape_10("Ada", 25)  ->  "Je m'appelle Ada et j'ai 25 ans."
#  Remplace  ____  par :  f"Je m'appelle {nom} et j'ai {age} ans."
# ══════════════════════════════════════════════════════════════════════
def etape_10(nom, age):
    return ____


# ══════════════════════════════════════════════════════════════════════
#  ▶ LE CORRECTEUR — ne touche pas à ce qui suit, lance juste le fichier.
# ══════════════════════════════════════════════════════════════════════
ETAPES = [
    ("01", "Écrire une variable dans un texte", etape_01,
     [(("Ada",), "Bonjour Ada")], "remplace ____ par  nom"),
    ("02", "Deux variables dans un texte", etape_02,
     [(("Ada", 25), "Ada a 25 ans")], "remplace les ____ par  nom  et  age"),
    ("03", "Utiliser un paramètre dans un calcul", etape_03,
     [((10,), 12), ((0,), 2)], "remplace ____ par  prix"),
    ("04", "Répondre True / False", etape_04,
     [((20,), True), ((15,), False)], "remplace ____ par  age"),
    ("05", "Tester si un nombre est pair", etape_05,
     [((4,), True), ((7,), False)], "remplace ____ par  0"),
    ("06", "Choisir entre deux réponses (if/else)", etape_06,
     [((20,), "Majeur"), ((15,), "Mineur")], 'remplace les ____ par  "Majeur"  et  "Mineur"'),
    ("07", "Additionner de 1 à n (boucle for)", etape_07,
     [((5,), 15), ((1,), 1)], "remplace ____ par  n + 1"),
    ("08", "Compter les nombres pairs", etape_08,
     [((10,), 5), ((7,), 3)], "remplace ____ par  1"),
    ("09", "Écrire la condition toi-même", etape_09,
     [((4,), "pair"), ((7,), "impair")], "remplace ____ par  n % 2"),
    ("10", "La ligne complète (celle qui te bloquait !)", etape_10,
     [(("Ada", 25), "Je m'appelle Ada et j'ai 25 ans.")],
     'remplace ____ par  f"Je m\'appelle {nom} et j\'ai {age} ans."'),
]


def _tester_une_etape(fonction, cas):
    """Renvoie (tout_ok, details). Gère le trou ____ non rempli proprement."""
    details = []
    tout_ok = True
    for arguments, attendu in cas:
        try:
            obtenu = fonction(*arguments)
            if "____" in repr(obtenu):           # le ____ est resté dans le texte
                raise NameError("____")
            ok = (obtenu == attendu)
        except NameError as e:
            if "____" in str(e):
                details.append(("trou", arguments, attendu))
                tout_ok = False
                continue
            obtenu = f"ERREUR: {e}"
            ok = False
        except Exception as e:
            obtenu = f"ERREUR: {e}"
            ok = False
        if not ok:
            tout_ok = False
        details.append((ok, arguments, attendu, obtenu))
    return tout_ok, details


def _appel_lisible(nom_fonction, arguments):
    return f"{nom_fonction}(" + ", ".join(repr(a) for a in arguments) + ")"


if __name__ == "__main__":
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║   PAS À PAS — Module 01 : les bases                      ║")
    print("║   Remplace chaque  ____  dans le fichier, puis relance.  ║")
    print("╚══════════════════════════════════════════════════════════╝\n")

    faits = 0
    prochaine = None
    for num, titre, fonction, cas, indice in ETAPES:
        tout_ok, details = _tester_une_etape(fonction, cas)
        if tout_ok:
            print(f"✅ Étape {num} — {titre}")
            faits += 1
        else:
            # première étape pas encore réussie : on s'arrête d'y insister
            non_rempli = any(d[0] == "trou" for d in details)
            if non_rempli:
                print(f"⬜ Étape {num} — {titre}")
                print(f"     → à faire : {indice}")
            else:
                print(f"❌ Étape {num} — {titre}")
                print(f"     → {indice}")
                for d in details:
                    if d[0] is False:
                        _, arguments, attendu, obtenu = d
                        print(f"        {_appel_lisible(fonction.__name__, arguments)}"
                              f"  attendu : {attendu!r}   ton code a donné : {obtenu!r}")
            if prochaine is None:
                prochaine = (num, titre, indice)

    total = len(ETAPES)
    barre = "█" * faits + "░" * (total - faits)
    print(f"\n   Progression :  [{barre}]  {faits}/{total}")

    if faits == total:
        print("\n🎉 BRAVO — tu as tout rempli ! Tu viens d'écrire, étape par étape,")
        print("   exactement les fonctions qui te bloquaient avant.")
        print("   ➡️  Prochaine étape : ouvre  exercices.py  (le niveau au-dessus).")
    elif prochaine:
        num, titre, indice = prochaine
        print(f"\n👉 Ta prochaine étape : ÉTAPE {num} — {titre}")
        print(f"   Dans le fichier, trouve  def etape_{num}(...)  et {indice}")
        print("   Puis relance :  python3 pas_a_pas.py")
