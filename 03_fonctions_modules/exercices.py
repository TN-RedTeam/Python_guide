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

▶ LANCER LES TESTS :   python3 exercices.py
  Pour chaque ❌, le test affiche ce qu'il ATTENDAIT et ce que TA fonction
  a renvoyé : compare les deux, ton erreur est dans l'écart.

▶ BLOQUÉ ? Réessaie en relisant l'indice écrit dans la fonction. En tout
  dernier recours, ouvre solutions.py (le corrigé commenté).
"""


def salutation(nom, politesse="Bonjour"):
    """Renvoie une salutation. `politesse` a une valeur par défaut.
    Ex : salutation("Ada")               -> "Bonjour Ada !"
         salutation("Ada", "Salut")      -> "Salut Ada !"
    """
    # TODO : utilise une f-string
    ...


def moyenne(*notes):
    """Accepte un nombre VARIABLE de notes et renvoie leur moyenne.
    Renvoie 0 si aucune note (pour éviter la division par zéro).
    Ex : moyenne(10, 20)     -> 15.0
         moyenne()           -> 0
    """
    # TODO : *notes ramasse les arguments dans un tuple ; pense au cas vide
    ...


def applique(fonction, liste):
    """Applique `fonction` à chaque élément de `liste` et renvoie la liste des résultats.
    Ex : applique(lambda x: x * 2, [1, 2, 3]) -> [2, 4, 6]
    (Oui, une fonction peut recevoir une autre fonction en argument !)
    """
    # TODO : une compréhension de liste
    ...


def compter_mots(phrase):
    """Renvoie le nombre de mots d'une phrase (mots séparés par des espaces).
    Ex : compter_mots("le chat dort") -> 3
    Indice : la méthode .split() découpe une chaîne en liste de mots.
    """
    # TODO
    ...


# ════════════════════════════════════════════════════════════════════
#  Auto-vérification — NE PAS MODIFIER
# ════════════════════════════════════════════════════════════════════
def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Vérification — module 03 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("salutation('Ada')", lambda: salutation("Ada"), "Bonjour Ada !")
    essai("salutation('Ada','Salut')", lambda: salutation("Ada", "Salut"), "Salut Ada !")
    essai("moyenne(10, 20)", lambda: moyenne(10, 20), 15.0)
    essai("moyenne()", lambda: moyenne(), 0)
    essai("applique(x2, [1,2,3])", lambda: applique(lambda x: x * 2, [1, 2, 3]), [2, 4, 6])
    essai("compter_mots('le chat dort')", lambda: compter_mots("le chat dort"), 3)

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
