#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 03 : fonctions & modules

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  fonctions.py  (puis usage_module.py)
  Les exercices ne demandent RIEN de plus que ce qui y est expliqué.

▶ COMMENT COMPLÉTER UNE FONCTION :
    • Chaque fonction contient une ligne « ... » (trois points) : c'est le
      TROU à remplir. Efface ce « ... » et écris ton code à la place, juste
      sous le commentaire « # TODO ».
    • Garde les 4 espaces en début de ligne : en Python, ce décalage
      (l'indentation) signifie « ce code est À L'INTÉRIEUR de la fonction ».
    • Pense au « return » : une fonction doit RENVOYER son résultat. Sans
      « return », elle ne renvoie « rien » (None) et le test échoue.

  Exemple — au départ, la fonction a un trou :

      def double(n):
          ...

  À toi de remplacer le « ... » par la vraie réponse :

      def double(n):
          return n * 2

  Chaque fonction t'explique tout ce qu'il faut : son OBJECTIF, un EXEMPLE, et
  les ÉTAPES pour y arriver. Tu n'as PAS besoin de lire le bas du fichier.

▶ 💾 ASTUCE « git pull » (pour ne jamais perdre ton travail) :
  Ne code pas directement dans ce fichier (il est suivi par git). Copie-le et
  travaille dans la copie — elle est ignorée par git, donc une mise à jour du
  guide (« git pull ») ne touchera jamais ton travail :
      cp exercices.py exercices_perso.py      # puis :  python3 exercices_perso.py

▶ LANCER LES TESTS :   python3 exercices.py
  Pour chaque ❌, le test affiche ce qu'il ATTENDAIT et ce que TA fonction
  a renvoyé : compare les deux, ton erreur est dans l'écart.

▶ BLOQUÉ ? Réessaie en relisant l'indice écrit dans la fonction. En tout
  dernier recours, ouvre solutions.py (le corrigé commenté).
"""


def salutation(nom, politesse="Bonjour"):
    """OBJECTIF : renvoyer une salutation. Le paramètre `politesse` a une valeur
    PAR DÉFAUT ("Bonjour") : si on ne le précise pas, c'est celle-là qui sert.

    Exemples : salutation("Ada")           ->  "Bonjour Ada !"
               salutation("Ada", "Salut")  ->  "Salut Ada !"

    Comment t'y prendre :
      - construis le texte avec une f-string : f"{politesse} {nom} !" ;
      - renvoie-la.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def moyenne(*notes):
    """OBJECTIF : accepter un nombre VARIABLE de notes et renvoyer leur moyenne.
    Renvoyer 0 s'il n'y a aucune note (sinon division par zéro = plantage).

    Exemples : moyenne(10, 20)  ->  15.0        moyenne()  ->  0

    Comment t'y prendre :
      - grâce à l'étoile, `notes` est un tuple de toutes les valeurs reçues ;
      - si ce tuple est vide (if not notes:), renvoie 0 ;
      - sinon, renvoie sum(notes) / len(notes)  (la somme divisée par le nombre).
    """
    ...   # ⬅️ remplace cette ligne par ton code


def applique(fonction, liste):
    """OBJECTIF : appliquer `fonction` à CHAQUE élément de `liste` et renvoyer
    la liste des résultats. (Oui : une fonction peut recevoir une AUTRE fonction
    en argument — voir le cours, section 6.)

    Exemple : applique(lambda x: x * 2, [1, 2, 3])  ->  [2, 4, 6]

    Comment t'y prendre :
      1. crée une liste vide : resultat = [] ;
      2. parcours `liste` avec une boucle for ;
      3. pour chaque x, appelle fonction(x) et ajoute le retour : resultat.append(fonction(x)) ;
      4. renvoie resultat.
      (Au module 06, tu apprendras à écrire tout ça en une seule ligne.)
    """
    ...   # ⬅️ remplace cette ligne par ton code


def compter_mots(phrase):
    """OBJECTIF : renvoyer le nombre de mots d'une phrase (mots séparés par des espaces).

    Exemple : compter_mots("le chat dort")  ->  3

    Comment t'y prendre :
      - phrase.split() découpe la phrase en une LISTE de mots ;
      - len(...) compte combien il y en a ;
      - renvoie len(phrase.split()).
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ════════════════════════════════════════════════════════════════════
#  ▶ ON TESTE TON CODE — lance le fichier pour voir tes ✅ / ❌
#
#  C'est ICI qu'on APPELLE tes fonctions, avec des exemples concrets.
#  → C'est d'ici que vient une valeur comme "Ada" : c'est juste un
#    ARGUMENT qu'on passe à l'appel. Rien de magique, rien de caché.
#  C'est normal et voulu : en HAUT on DÉFINIT les fonctions, et plus bas
#  on les UTILISE (définir une fonction ≠ l'appeler — cf. ce module).
#
#  Comment lire une ligne d'essai :
#      verifie(salutation, "Ada", attendu="Bonjour Ada !")
#   ↑  appelle  salutation("Ada")  et compare le résultat à "Bonjour Ada !".
# ════════════════════════════════════════════════════════════════════
def verifie(fonction, *arguments, attendu):
    """Appelle fonction(*arguments) et compare au résultat attendu. (Mécanique du test.)"""
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

    def fois_deux(x):                 # une petite fonction qu'on passe à `applique`
        return x * 2

    resultats = [
        verifie(salutation, "Ada",              attendu="Bonjour Ada !"),
        verifie(salutation, "Ada", "Salut",     attendu="Salut Ada !"),
        verifie(moyenne, 10, 20,                attendu=15.0),
        verifie(moyenne,                        attendu=0),
        verifie(applique, fois_deux, [1, 2, 3], attendu=[2, 4, 6]),
        verifie(compter_mots, "le chat dort",   attendu=3),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
