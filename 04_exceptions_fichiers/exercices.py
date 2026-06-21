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


def division_sure(a, b):
    """OBJECTIF : renvoyer a / b, mais renvoyer None si b vaut 0 (au lieu de
    laisser le programme planter).

    Exemples : division_sure(10, 2)  ->  5.0       division_sure(10, 0)  ->  None

    Comment t'y prendre :
      - mets le calcul a / b dans un bloc  try: ... ;
      - ajoute  except ZeroDivisionError:  qui renvoie None ;
      - dans le try (si tout va bien), renvoie a / b.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def convertir_entier(texte):
    """OBJECTIF : convertir `texte` en entier, ou renvoyer None si ce n'est pas
    un nombre valide (au lieu de planter).

    Exemples : convertir_entier("42")  ->  42        convertir_entier("abc")  ->  None

    Comment t'y prendre :
      - dans un  try:  renvoie int(texte) ;
      - int("abc") lève une ValueError : attrape-la avec  except ValueError:
        et renvoie None.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def ecrire_puis_lire(chemin, contenu):
    """OBJECTIF : écrire `contenu` dans le fichier `chemin`, puis le relire et
    renvoyer ce qu'il contient.

    Exemple : ecrire_puis_lire("/tmp/x.txt", "salut")  ->  "salut"

    Comment t'y prendre :
      1. ÉCRIRE : with open(chemin, "w", encoding="utf-8") as f:  puis  f.write(contenu) ;
      2. LIRE   : with open(chemin, "r", encoding="utf-8") as f:  puis  contenu_lu = f.read() ;
      3. renvoie contenu_lu.
      (Le « w » écrase/crée le fichier, le « r » le lit. `with` referme tout seul.)
    """
    ...   # ⬅️ remplace cette ligne par ton code


def compter_lignes(chemin):
    """OBJECTIF : renvoyer le nombre de lignes du fichier `chemin`.
    Si le fichier n'existe pas, renvoyer 0 (sans planter).

    Comment t'y prendre :
      - dans un  try: , ouvre le fichier : with open(chemin, "r", encoding="utf-8") as f: ;
      - f.readlines() renvoie la LISTE des lignes ; len(...) les compte ;
      - renvoie ce nombre ;
      - ajoute  except FileNotFoundError:  qui renvoie 0.
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ════════════════════════════════════════════════════════════════════
#  ▶ ON TESTE TON CODE — lance le fichier pour voir tes ✅ / ❌
#
#  C'est ICI qu'on APPELLE tes fonctions, avec des exemples concrets.
#  → Les valeurs d'exemple ci-dessous sont juste des ARGUMENTS qu'on passe
#    à l'appel. Rien de magique ni de caché.
#  C'est normal : en HAUT on DÉFINIT les fonctions, et plus bas on les
#  UTILISE (définir une fonction ≠ l'appeler).
#
#  Comment lire une ligne d'essai :
#      verifie(division_sure, 10, 2, attendu=5.0)
#   ↑  appelle  division_sure(10, 2)  et compare le résultat à 5.0.
# ════════════════════════════════════════════════════════════════════
import types as _types


def verifie(fonction, *arguments, attendu):
    """Appelle fonction(*arguments) et compare au résultat attendu. (Mécanique du test.)"""
    try:
        obtenu = fonction(*arguments)
        if isinstance(obtenu, _types.GeneratorType):   # un générateur → on le déroule en liste
            obtenu = list(obtenu)
    except Exception as e:
        obtenu = f"ERREUR: {e}"
    ok = (obtenu == attendu)
    args_lisibles = ", ".join(a.__name__ if callable(a) else repr(a) for a in arguments)
    print(f"{'✅' if ok else '❌'} {fonction.__name__}({args_lisibles})  ->  {attendu!r}")
    if not ok:
        print(f"     ⚠️  ton code a renvoyé : {obtenu!r}")
    return ok


if __name__ == "__main__":
    import tempfile, os
    print("--- Module 04 : exceptions & fichiers ---\n")

    # On prépare un dossier temporaire et un fichier de 3 lignes pour les tests
    # fichiers (rien n'est touché dans tes vrais dossiers).
    dossier = tempfile.mkdtemp()
    fichier = os.path.join(dossier, "test.txt")
    fichier3 = os.path.join(dossier, "trois.txt")
    with open(fichier3, "w", encoding="utf-8") as f:
        f.write("a\nb\nc\n")
    fichier_absent = os.path.join(dossier, "nexiste_pas.txt")

    resultats = [
        verifie(division_sure, 10, 2,            attendu=5.0),
        verifie(division_sure, 10, 0,            attendu=None),
        verifie(convertir_entier, "42",          attendu=42),
        verifie(convertir_entier, "abc",         attendu=None),
        verifie(ecrire_puis_lire, fichier, "salut", attendu="salut"),
        verifie(compter_lignes, fichier3,        attendu=3),
        verifie(compter_lignes, fichier_absent,  attendu=0),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
