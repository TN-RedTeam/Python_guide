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

import asyncio


async def addition_async(a, b):
    """OBJECTIF : une fonction ASYNCHRONE (async) qui renvoie a + b.

    Exemple : await addition_async(2, 3)  ->  5

    Comment t'y prendre :
      1. écris d'abord un point d'attente : await asyncio.sleep(0)
         (ça simule une pause ; obligatoire ici pour s'entraîner au `await`) ;
      2. ensuite, return a + b.
    """
    ...   # ⬅️ remplace cette ligne par ton code


async def executer_tout(coroutines):
    """OBJECTIF : recevoir une LISTE de coroutines, les lancer toutes ENSEMBLE,
    et renvoyer la liste de leurs résultats (dans l'ordre).

    Exemple : await executer_tout([addition_async(1, 1), addition_async(10, 5)])  ->  [2, 15]

    Comment t'y prendre :
      - asyncio.gather(*coroutines) lance toutes les coroutines en parallèle ;
        l'étoile `*` « déballe » la liste en arguments séparés ;
      - n'oublie pas le `await` devant (on attend que tout soit fini) ;
      - renvoie  await asyncio.gather(*coroutines).
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ════════════════════════════════════════════════════════════════════
#  ▶ ON TESTE TON CODE — lance le fichier pour voir tes ✅ / ❌
#
#  C'est ICI qu'on APPELLE tes fonctions async (voir _lancer_les_essais).
#  Les nombres (2, 3...) sont juste les ARGUMENTS passés à l'appel. Comme ce
#  sont des coroutines, on les appelle avec « await », le tout démarré par
#  asyncio.run(...). C'est normal : en HAUT on DÉFINIT, ici on UTILISE.
# ════════════════════════════════════════════════════════════════════
def afficher(appel, obtenu, attendu):
    """Affiche ✅/❌ pour un appel déjà exécuté. (Mécanique du test.)"""
    ok = (obtenu == attendu)
    print(f"{'✅' if ok else '❌'} {appel}  ->  {attendu!r}")
    if not ok:
        print(f"     ⚠️  ton code a renvoyé : {obtenu!r}")
    return ok


async def _lancer_les_essais():
    # C'est ICI qu'on APPELLE tes fonctions async (avec await) :
    r1 = await addition_async(2, 3)
    r2 = await executer_tout([addition_async(1, 1), addition_async(10, 5)])
    return r1, r2


if __name__ == "__main__":
    print("--- Module 08 : asyncio ---\n")
    try:
        r1, r2 = asyncio.run(_lancer_les_essais())
    except Exception as e:
        r1 = r2 = f"ERREUR: {e}"
    resultats = [
        afficher("addition_async(2, 3)", r1, 5),
        afficher("executer_tout([addition_async(1, 1), addition_async(10, 5)])", r2, [2, 15]),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
