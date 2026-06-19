#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 05 : la POO (classes)

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Des CLASSES À TROUS que tu complètes toi-même. Tu lances le fichier, et
 il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  poo.py
  Les exercices ne demandent RIEN de plus que ce qui y est expliqué.

▶ COMMENT COMPLÉTER UNE MÉTHODE :
    • Chaque méthode contient une ligne « ... » (trois points) : c'est le
      TROU à remplir. Efface ce « ... » et écris ton code à la place, juste
      sous le commentaire « # TODO ».
    • Garde l'indentation (les espaces en début de ligne) : c'est elle qui
      dit « ce code est À L'INTÉRIEUR de la méthode ».
    • « self » = l'objet en cours. Dans __init__, on RANGE les données dans
      self (self.xxx = ...). Les autres méthodes les RELISENT avec self.xxx.

  Exemple — au départ, la classe a des trous :

      class Chien:
          def __init__(self, nom):
              ...                       # le trou du constructeur
          def crier(self):
              ...                       # le trou de la méthode

  À toi de les remplacer par le vrai code :

      class Chien:
          def __init__(self, nom):
              self.nom = nom            # on RANGE le nom dans l'objet
          def crier(self):
              return f"{self.nom} : Wouf !"   # on RELIT self.nom

▶ LANCER LES TESTS :   python3 exercices.py
  Pour chaque ❌, le test affiche ce qu'il ATTENDAIT et ce que TON code a
  produit : compare les deux, ton erreur est dans l'écart.

▶ BLOQUÉ ? Réessaie en relisant l'indication de la classe. En tout dernier
  recours, ouvre solutions.py (le corrigé commenté).
"""


class Rectangle:
    """Un rectangle défini par sa largeur et sa hauteur.

    Doit fournir :
      - __init__(self, largeur, hauteur)  → range les deux dans l'objet
      - aire(self)        → largeur * hauteur
      - perimetre(self)   → 2 * (largeur + hauteur)
    """

    def __init__(self, largeur, hauteur):
        # TODO : range largeur et hauteur dans self
        ...

    def aire(self):
        # TODO
        ...

    def perimetre(self):
        # TODO
        ...


class Carre(Rectangle):
    """Un carré EST un rectangle dont les deux côtés sont égaux.

    __init__(self, cote) doit appeler le constructeur du parent (super())
    avec le même côté pour la largeur ET la hauteur.
    """

    def __init__(self, cote):
        # TODO : utilise super().__init__(...)
        ...


class CompteBancaire:
    """Un compte avec un solde.

      - __init__(self, solde=0)
      - deposer(self, montant)   → augmente le solde
      - retirer(self, montant)   → diminue le solde, MAIS refuse (ne fait rien)
                                    si le montant dépasse le solde
    """

    def __init__(self, solde=0):
        # TODO
        ...

    def deposer(self, montant):
        # TODO
        ...

    def retirer(self, montant):
        # TODO : vérifie d'abord que le solde est suffisant
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
    print("--- Vérification — module 05 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("Rectangle(3,4).aire()", lambda: Rectangle(3, 4).aire(), 12)
    essai("Rectangle(3,4).perimetre()", lambda: Rectangle(3, 4).perimetre(), 14)
    essai("Carre(5).aire()", lambda: Carre(5).aire(), 25)
    essai("Carre(5).perimetre()", lambda: Carre(5).perimetre(), 20)

    def scenario_compte():
        c = CompteBancaire(100)
        c.deposer(50)        # 150
        c.retirer(200)       # refusé → reste 150
        c.retirer(30)        # 120
        return c.solde

    essai("CompteBancaire scénario", scenario_compte, 120)

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
