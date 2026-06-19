#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 04 : exceptions & fichiers

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  fichiers.py
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


def division_sure(a, b):
    """Renvoie a / b, ou None si b vaut 0 (au lieu de planter).
    Ex : division_sure(10, 2) -> 5.0
         division_sure(10, 0) -> None
    """
    # TODO : utilise try / except ZeroDivisionError
    ...


def convertir_entier(texte):
    """Convertit `texte` en entier, ou renvoie None si ce n'est pas un nombre.
    Ex : convertir_entier("42")  -> 42
         convertir_entier("abc") -> None
    """
    # TODO : try / except ValueError autour de int(...)
    ...


def ecrire_puis_lire(chemin, contenu):
    """Écrit `contenu` dans le fichier `chemin`, puis relit et renvoie ce qu'il contient.
    Ex : ecrire_puis_lire("/tmp/x.txt", "salut") -> "salut"
    Utilise `with open(...)` en mode "w" puis "r", avec encoding="utf-8".
    """
    # TODO : deux blocs with open(...)
    ...


def compter_lignes(chemin):
    """Renvoie le nombre de lignes du fichier `chemin`.
    Si le fichier n'existe pas, renvoie 0 (sans planter).
    """
    # TODO : try / except FileNotFoundError ; lis les lignes et compte-les
    ...


# ════════════════════════════════════════════════════════════════════
#  Auto-vérification — NE PAS MODIFIER
# ════════════════════════════════════════════════════════════════════
import tempfile
import os


def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Vérification — module 04 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("division_sure(10, 2)", lambda: division_sure(10, 2), 5.0)
    essai("division_sure(10, 0)", lambda: division_sure(10, 0), None)
    essai("convertir_entier('42')", lambda: convertir_entier("42"), 42)
    essai("convertir_entier('abc')", lambda: convertir_entier("abc"), None)

    # Exercices fichiers : on travaille dans un dossier temporaire
    dossier = tempfile.mkdtemp()
    chemin = os.path.join(dossier, "test.txt")
    essai("ecrire_puis_lire(...)", lambda: ecrire_puis_lire(chemin, "salut"), "salut")

    chemin3 = os.path.join(dossier, "trois.txt")
    with open(chemin3, "w", encoding="utf-8") as f:
        f.write("a\nb\nc\n")
    essai("compter_lignes(3 lignes)", lambda: compter_lignes(chemin3), 3)
    essai("compter_lignes(inexistant)", lambda: compter_lignes(os.path.join(dossier, "nope.txt")), 0)

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
