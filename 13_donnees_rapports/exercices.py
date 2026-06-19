#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 13 : données & rapports (le RAISONNEMENT, sans pandas)

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ CONTEXTE : les données sont une liste de ventes ; chaque vente est un
  dict, ex.  {"produit": "pomme", "montant": 10}.  pandas ferait ces calculs
  en une ligne, mais on reproduit la logique « à la main » pour comprendre.

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  rapport_ventes.py
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


def chiffre_affaires_total(ventes):
    """Renvoie la somme de tous les "montant".
    Ex : [{"montant": 10}, {"montant": 5}] -> 15
    """
    # TODO
    ...


def total_par_produit(ventes):
    """Renvoie un dict {produit: somme des montants de ce produit} (comme un groupby).
    Ex : [{"produit":"a","montant":10}, {"produit":"a","montant":5}, {"produit":"b","montant":3}]
         -> {"a": 15, "b": 3}
    """
    # TODO : parcours les ventes, accumule dans un dict avec .get(produit, 0)
    ...


def grosses_ventes(ventes, seuil):
    """Renvoie la liste des ventes dont le "montant" dépasse strictement `seuil`.
    Ex : grosses_ventes([{"montant":10},{"montant":3}], 5) -> [{"montant":10}]
    """
    # TODO : une compréhension de liste avec un filtre
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
    print("--- Vérification — module 13 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    ventes = [
        {"produit": "pomme", "montant": 10},
        {"produit": "pomme", "montant": 5},
        {"produit": "poire", "montant": 3},
    ]

    essai("chiffre_affaires_total", lambda: chiffre_affaires_total(ventes), 18)
    essai("total_par_produit", lambda: total_par_produit(ventes), {"pomme": 15, "poire": 3})
    essai("grosses_ventes(>4)", lambda: grosses_ventes(ventes, 4),
          [{"produit": "pomme", "montant": 10}, {"produit": "pomme", "montant": 5}])

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
