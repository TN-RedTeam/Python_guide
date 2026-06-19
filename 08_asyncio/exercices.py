#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 08 : asyncio

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  demo_async.py
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

  ⚠️ Spécial asyncio : ici les fonctions sont « async ». On les complète
  pareil, mais un point d'attente s'écrit avec « await » (ex. « await
  asyncio.sleep(0) »). L'indice de chaque fonction te dit quoi « await ».

▶ LANCER LES TESTS :   python3 exercices.py
  Pour chaque ❌, le test affiche ce qu'il ATTENDAIT et ce que TA fonction
  a renvoyé : compare les deux, ton erreur est dans l'écart.

▶ BLOQUÉ ? Réessaie en relisant l'indice écrit dans la fonction. En tout
  dernier recours, ouvre solutions.py (le corrigé commenté).
"""

import asyncio


async def addition_async(a, b):
    """Fonction ASYNCHRONE qui renvoie a + b.
    Doit contenir un `await asyncio.sleep(0)` (simule un point d'attente),
    puis renvoyer la somme.
    """
    # TODO : await asyncio.sleep(0) puis return a + b
    ...


async def executer_tout(coroutines):
    """Reçoit une LISTE de coroutines, les lance toutes ENSEMBLE et renvoie
    la liste de leurs résultats (dans l'ordre).
    Indice : asyncio.gather(*coroutines) — n'oublie pas le `await` et l'étoile `*`.
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


async def _scenario():
    r1 = await addition_async(2, 3)
    r2 = await executer_tout([addition_async(1, 1), addition_async(10, 5)])
    return r1, r2


def _verifier():
    print("--- Vérification — module 08 ---")
    try:
        r1, r2 = asyncio.run(_scenario())
    except Exception as e:
        r1, r2 = f"ERREUR: {e}", f"ERREUR: {e}"
    res = [
        _check("addition_async(2, 3)", r1, 5),
        _check("executer_tout([...])", r2, [2, 15]),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
