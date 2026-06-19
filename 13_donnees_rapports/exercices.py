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


def chiffre_affaires_total(ventes):
    """OBJECTIF : renvoyer la somme de tous les "montant" de la liste `ventes`.

    Exemple : chiffre_affaires_total([{"montant": 10}, {"montant": 5}])  ->  15

    Comment t'y prendre :
      - récupère le "montant" de chaque vente ;
      - additionne-les avec sum(...) ;
      - renvoie  sum(vente["montant"] for vente in ventes).
    """
    ...   # ⬅️ remplace cette ligne par ton code


def total_par_produit(ventes):
    """OBJECTIF : renvoyer un dict {produit: somme de ses montants} (un « groupby »).

    Exemple :
        total_par_produit([{"produit":"a","montant":10},
                           {"produit":"a","montant":5},
                           {"produit":"b","montant":3}])   ->   {"a": 15, "b": 3}

    Comment t'y prendre :
      1. crée un dict vide : total = {} ;
      2. parcours `ventes` ; pour chaque vente, lis p = vente["produit"] et m = vente["montant"] ;
      3. accumule : total[p] = total.get(p, 0) + m
         (.get(p, 0) renvoie 0 si le produit n'a pas encore été vu) ;
      4. renvoie total.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def grosses_ventes(ventes, seuil):
    """OBJECTIF : renvoyer la liste des ventes dont le "montant" dépasse
    STRICTEMENT `seuil`.

    Exemple : grosses_ventes([{"montant":10}, {"montant":3}], 5)  ->  [{"montant":10}]

    Comment t'y prendre (compréhension de liste avec filtre, vue au module 06) :
      - garde chaque vente dont vente["montant"] > seuil ;
      - renvoie  [v for v in ventes if v["montant"] > seuil].
    """
    ...   # ⬅️ remplace cette ligne par ton code


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
