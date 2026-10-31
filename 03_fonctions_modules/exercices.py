#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 03 : fonctions & modules

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une serie de fonctions A TROUS que tu completes toi-meme. Tu lances le
 fichier, et il TESTE tes reponses : ✅ = reussi, ❌ = encore a corriger.
══════════════════════════════════════════════════════════════════════

▶ DIFFICULTE PROGRESSIVE (4 niveaux) :
  Les exercices sont ranges du plus simple au plus difficile :
    NIVEAU 1 — REPRODUCTION  : tu recopies quasi mot pour mot ce que le cours montre.
    NIVEAU 2 — ADAPTATION    : meme mecanique, mais dans un contexte un peu different.
    NIVEAU 3 — COMBINAISON   : tu assembles deux idees vues dans le cours.
    NIVEAU 4 — DEFI          : tu dois reflechir un peu plus, mais tout est dans le cours.
  Commence par le niveau 1. Ne passe au suivant que quand tout est ✅.

▶ RAPPEL DU COURS :
  Chaque exercice te RAPPELLE le bout de cours dont tu as besoin, avec le
  code exact vu en classe. Tu n'as PAS a deviner ni a chercher ailleurs.

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commente   →  fonctions.py  (puis usage_module.py)
  Les exercices ne demandent RIEN de plus que ce qui y est explique.

▶ COMMENT COMPLETER UNE FONCTION :
    - Chaque fonction contient une ligne « ... » (trois points) : c'est le
      TROU a remplir. Efface ce « ... » et ecris ton code a la place.
    - Garde les 4 espaces en debut de ligne (l'indentation).
    - Pense au « return » : une fonction doit RENVOYER son resultat.
      ❌ print(resultat)   → AFFICHE mais renvoie None (le test echoue)
      ✅ return resultat    → RENVOIE le resultat (le test reussit)
    - Les PARAMETRES (entre parentheses) sont DEJA remplis. N'ecris PAS
      nom = "Ada" ou liste = [...] dans la fonction !

  Exemple — au depart, la fonction a un trou :

      def double(n):
          ...

  A toi de remplacer le « ... » par la vraie reponse :

      def double(n):
          return n * 2

▶ 💾 ASTUCE « git pull » (pour ne jamais perdre ton travail) :
  Ne code pas directement dans ce fichier (il est suivi par git). Copie-le et
  travaille dans la copie — elle est ignoree par git :
      cp exercices.py exercices_perso.py      # puis :  python3 exercices_perso.py

▶ LANCER LES TESTS :   python3 exercices.py

▶ BLOQUE ? Relis le RAPPEL DU COURS dans l'exercice. En tout dernier
  recours, ouvre solutions.py (le corrige commente).
"""


# ╔════════════════════════════════════════════════════════════════════╗
# ║  NIVEAU 1 — REPRODUCTION                                         ║
# ║  Tu appliques directement ce que le cours montre.                 ║
# ╚════════════════════════════════════════════════════════════════════╝


def salutation(nom, politesse="Bonjour"):
    """OBJECTIF : renvoyer une salutation.

    Exemples : salutation("Ada")           ->  "Bonjour Ada !"
               salutation("Ada", "Salut")  ->  "Salut Ada !"

    ┌─ RAPPEL DU COURS (section 3 — valeurs par defaut) ─────────────┐
    │  def creer_message(nom, role="Guerrier"):                      │
    │      return f"Bienvenue {nom}, le {role} !"                    │
    │                                                                │
    │  creer_message("Baba")          → "Bienvenue Baba, le Guerrier !" │
    │  creer_message("Baba", "Mage")  → "Bienvenue Baba, le Mage !" │
    │                                                                │
    │  role="Guerrier" est la valeur PAR DEFAUT : si l'appelant ne   │
    │  fournit pas role, c'est "Guerrier" qui est utilise.           │
    └────────────────────────────────────────────────────────────────┘

    Comment t'y prendre :
      C'est exactement le meme schema que creer_message ci-dessus :
      - construis le texte avec une f-string : f"{politesse} {nom} !"
      - renvoie-la avec return.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def compter_mots(phrase):
    """OBJECTIF : renvoyer le nombre de mots d'une phrase.

    Exemple : compter_mots("le chat dort")  ->  3

    ┌─ RAPPEL DU COURS (section 2 — ce qu'une fonction peut utiliser) ┐
    │  En Python, les chaines de texte ont des METHODES pratiques :    │
    │                                                                  │
    │  "le chat dort".split()   →  ["le", "chat", "dort"]  (une LISTE)│
    │  len(["le", "chat", "dort"])  →  3   (le nombre d'elements)     │
    │                                                                  │
    │  .split() decoupe le texte en mots, len() les compte.           │
    └──────────────────────────────────────────────────────────────────┘

    Comment t'y prendre :
      1. phrase.split() te donne la liste des mots ;
      2. len(...) compte combien il y en a ;
      3. renvoie len(phrase.split()).
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ╔════════════════════════════════════════════════════════════════════╗
# ║  NIVEAU 2 — ADAPTATION                                           ║
# ║  Meme mecanique, contexte un peu different.                       ║
# ╚════════════════════════════════════════════════════════════════════╝


def aire_rectangle(largeur, hauteur=1):
    """OBJECTIF : renvoyer l'aire d'un rectangle (largeur x hauteur).
    Si la hauteur n'est pas donnee, elle vaut 1 par defaut (= un segment).

    Exemples : aire_rectangle(5, 3)  ->  15
               aire_rectangle(7)     ->  7    (hauteur vaut 1 par defaut)

    ┌─ RAPPEL DU COURS (section 3 — valeurs par defaut) ─────────────┐
    │  def creer_message(nom, role="Guerrier"):                      │
    │      return f"Bienvenue {nom}, le {role} !"                    │
    │                                                                │
    │  Ici c'est pareil : hauteur=1 est la valeur par defaut.        │
    │  Si on appelle aire_rectangle(7), hauteur vaut 1.              │
    │  Si on appelle aire_rectangle(5, 3), hauteur vaut 3.           │
    └────────────────────────────────────────────────────────────────┘

    Comment t'y prendre :
      - renvoie largeur * hauteur (c'est tout !).
    """
    ...   # ⬅️ remplace cette ligne par ton code


def moyenne(*notes):
    """OBJECTIF : accepter un nombre VARIABLE de notes et renvoyer leur moyenne.
    Renvoyer 0 s'il n'y a aucune note (sinon division par zero = plantage).

    Exemples : moyenne(10, 20)  ->  15.0        moyenne()  ->  0

    ┌─ RAPPEL DU COURS (section 5 — *args) ──────────────────────────┐
    │  def faire_somme(*nombres):                                    │
    │      total = 0                                                 │
    │      for n in nombres:                                         │
    │          total += n                                            │
    │      return total                                              │
    │                                                                │
    │  faire_somme(10, 20, 30)   → 60                                │
    │  faire_somme(1, 2, 3, 4)   → 10                                │
    │                                                                │
    │  L'etoile * "ramasse" tous les arguments dans un TUPLE.        │
    │  Ici, *notes fait pareil : notes = (10, 20) ou notes = ().     │
    │  sum(notes) fait la somme, len(notes) compte les elements.     │
    └────────────────────────────────────────────────────────────────┘

    Comment t'y prendre :
      1. si le tuple est vide (if not notes:), renvoie 0 ;
      2. sinon, renvoie sum(notes) / len(notes).
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ╔════════════════════════════════════════════════════════════════════╗
# ║  NIVEAU 3 — COMBINAISON                                          ║
# ║  Tu assembles deux idees du cours.                                ║
# ╚════════════════════════════════════════════════════════════════════╝


def applique(fonction, liste):
    """OBJECTIF : appliquer `fonction` a CHAQUE element de `liste` et renvoyer
    la liste des resultats.

    Exemple : applique(lambda x: x * 2, [1, 2, 3])  ->  [2, 4, 6]

    ┌─ RAPPEL DU COURS (section 6 — passer une fonction en argument) ┐
    │  def appliquer(fonction, valeur):                              │
    │      return fonction(valeur)                                   │
    │                                                                │
    │  print(appliquer(dire_bonjour, "Ada"))  → "Bonjour Ada"       │
    │                                                                │
    │  Une fonction est une valeur comme une autre : on peut la      │
    │  recevoir en parametre et l'APPELER avec ().                   │
    │  Ici, tu fais la meme chose, mais dans une BOUCLE : tu        │
    │  appelles fonction(x) pour chaque x de la liste.              │
    └────────────────────────────────────────────────────────────────┘

    Comment t'y prendre :
      1. cree une liste vide : resultat = []
      2. parcours `liste` avec une boucle for :
             for x in liste:
      3. a chaque tour, appelle fonction(x) et ajoute le retour :
             resultat.append(fonction(x))
      4. renvoie resultat.
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ╔════════════════════════════════════════════════════════════════════╗
# ║  NIVEAU 4 — DEFI                                                 ║
# ║  Tu dois reflechir un peu plus, mais tout est dans le cours.      ║
# ╚════════════════════════════════════════════════════════════════════╝


def trier_par_longueur(mots):
    """OBJECTIF : renvoyer la liste `mots` triee par LONGUEUR (du plus court
    au plus long).

    Exemple : trier_par_longueur(["python", "go", "rust"])  ->  ["go", "rust", "python"]

    ┌─ RAPPEL DU COURS (section 6 — lambda et tri) ──────────────────┐
    │  mots = ["python", "go", "rust"]                               │
    │  mots.sort(key=lambda mot: len(mot))                           │
    │  # → ["go", "rust", "python"]  (trie par longueur)             │
    │                                                                │
    │  key=... dit a Python : "pour comparer les elements, utilise   │
    │  CETTE fonction sur chacun". lambda mot: len(mot) = "la        │
    │  longueur du mot".                                             │
    │                                                                │
    │  sorted(liste, key=...) fait pareil mais RENVOIE une nouvelle  │
    │  liste (sans modifier l'originale).                            │
    └────────────────────────────────────────────────────────────────┘

    Comment t'y prendre :
      - renvoie sorted(mots, key=lambda mot: len(mot)).
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ════════════════════════════════════════════════════════════════════
#  ▶ ON TESTE TON CODE — lance le fichier pour voir tes ✅ / ❌
#
#  C'est ICI qu'on APPELLE tes fonctions, avec des exemples concrets.
#  → C'est d'ici que vient une valeur comme "Ada" : c'est juste un
#    ARGUMENT qu'on passe a l'appel. Rien de magique, rien de cache.
#  C'est normal et voulu : en HAUT on DEFINIT les fonctions, et plus bas
#  on les UTILISE (definir une fonction ≠ l'appeler — cf. ce module).
#
#  Comment lire une ligne d'essai :
#      verifie(salutation, "Ada", attendu="Bonjour Ada !")
#   ↑  appelle  salutation("Ada")  et compare le resultat a "Bonjour Ada !".
# ════════════════════════════════════════════════════════════════════
def verifie(fonction, *arguments, attendu):
    """Appelle fonction(*arguments) et compare au resultat attendu. (Mecanique du test.)"""
    try:
        obtenu = fonction(*arguments)
    except Exception as e:
        obtenu = f"ERREUR: {e}"
    ok = (obtenu == attendu)
    args_lisibles = ", ".join(a.__name__ if callable(a) else repr(a) for a in arguments)
    print(f"{'✅' if ok else '❌'} {fonction.__name__}({args_lisibles})  ->  {attendu!r}")
    if not ok:
        print(f"     ⚠️  ton code a renvoyé : {obtenu!r}")
    return ok


if __name__ == "__main__":
    print("--- Module 03 : fonctions & modules ---\n")

    def fois_deux(x):
        return x * 2

    print("NIVEAU 1 — REPRODUCTION")
    resultats = [
        verifie(salutation, "Ada",              attendu="Bonjour Ada !"),
        verifie(salutation, "Ada", "Salut",     attendu="Salut Ada !"),
        verifie(compter_mots, "le chat dort",   attendu=3),
    ]

    print("\nNIVEAU 2 — ADAPTATION")
    resultats += [
        verifie(aire_rectangle, 5, 3,           attendu=15),
        verifie(aire_rectangle, 7,              attendu=7),
        verifie(moyenne, 10, 20,                attendu=15.0),
        verifie(moyenne,                        attendu=0),
    ]

    print("\nNIVEAU 3 — COMBINAISON")
    resultats += [
        verifie(applique, fois_deux, [1, 2, 3], attendu=[2, 4, 6]),
    ]

    print("\nNIVEAU 4 — DEFI")
    resultats += [
        verifie(trier_par_longueur, ["python", "go", "rust"],
                attendu=["go", "rust", "python"]),
        verifie(trier_par_longueur, ["a", "bb", "ccc", "dd"],
                attendu=["a", "bb", "dd", "ccc"]),
    ]

    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
