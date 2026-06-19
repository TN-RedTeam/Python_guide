#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 06 : itérateurs & générateurs

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  generateurs.py
  Les exercices ne demandent RIEN de plus que ce qui y est expliqué.

▶ COMMENT COMPLÉTER UNE FONCTION :
    • Chaque fonction contient une ligne « ... » (trois points) : c'est le
      TROU à remplir. Efface ce « ... » et écris ton code à la place, juste
      sous le commentaire « # TODO ».
    • Garde les 4 espaces en début de ligne : en Python, ce décalage
      (l'indentation) signifie « ce code est À L'INTÉRIEUR de la fonction ».
    • Pense au « return » (ou au « yield » pour un générateur) : une fonction
      doit PRODUIRE son résultat, sinon le test échoue.

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


def filtrer_positifs(nombres):
    """Renvoie la liste des nombres strictement positifs (compréhension de liste).
    Ex : filtrer_positifs([3, -1, 0, 7, -2]) -> [3, 7]
    """
    # TODO : [ ... for ... in ... if ... ]
    ...


def noms_en_majuscules(noms):
    """Renvoie la liste des noms en MAJUSCULES (compréhension + méthode .upper()).
    Ex : noms_en_majuscules(["ada", "bob"]) -> ["ADA", "BOB"]
    """
    # TODO
    ...


def somme_carres(n):
    """Renvoie la somme des carrés de 0 à n-1.
    Ex : somme_carres(4) -> 0 + 1 + 4 + 9 = 14
    Indice : sum(... for ... in range(n))  (expression génératrice)
    """
    # TODO
    ...


def pairs_jusqua(limite):
    """GÉNÉRATEUR qui produit les nombres pairs de 0 (inclus) à `limite` (exclu).
    Ex : list(pairs_jusqua(10)) -> [0, 2, 4, 6, 8]
    Indice : utilise `yield` dans une boucle.
    """
    # TODO : un yield dans une boucle ; NE renvoie PAS une liste, utilise yield
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
    print("--- Vérification — module 06 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("filtrer_positifs([3,-1,0,7,-2])", lambda: filtrer_positifs([3, -1, 0, 7, -2]), [3, 7])
    essai("noms_en_majuscules(['ada','bob'])", lambda: noms_en_majuscules(["ada", "bob"]), ["ADA", "BOB"])
    essai("somme_carres(4)", lambda: somme_carres(4), 14)
    essai("list(pairs_jusqua(10))", lambda: list(pairs_jusqua(10)), [0, 2, 4, 6, 8])

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
