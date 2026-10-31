#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 01 : les bases (variables, conditions, boucles)

══════════════════════════════════════════════════════════════════════
 C'EST QUOI CE FICHIER ?
 Une série de fonctions À TROUS que tu complètes toi-même. Tu lances le
 fichier, et il TESTE tes réponses : ✅ = réussi, ❌ = encore à corriger.
══════════════════════════════════════════════════════════════════════

▶ PROGRESSION PAR NIVEAUX (commence par le niveau 1 !) :
    NIVEAU 1 — REPRODUCTION  : tu refais exactement ce que le cours montre.
    NIVEAU 2 — ADAPTATION    : même logique, petit changement.
    NIVEAU 3 — COMBINAISON   : tu mélanges 2 concepts du cours.
    NIVEAU 4 — DÉFI          : exercice plus corsé (facultatif, pour aller plus loin).
  Fais-les DANS L'ORDRE. Si tu bloques au niveau 3, c'est normal : relis les
  niveaux 1-2 et le cours, puis réessaie. Le niveau 4 est un bonus.

▶ AVANT DE COMMENCER (dans cet ordre) :
    1. Lis le cours du module       →  README.md  (dans ce dossier)
    2. Observe l'exemple commenté   →  bases.py
  Les exercices ne demandent RIEN de plus que ce qui y est expliqué.

▶ COMMENT COMPLÉTER UNE FONCTION :
    • Chaque fonction contient une ligne « ... » (trois points) : c'est le
      TROU à remplir. Efface ce « ... » et écris ton code à la place.
    • Garde les 4 espaces en début de ligne : en Python, ce décalage
      (l'indentation) signifie « ce code est À L'INTÉRIEUR de la fonction ».

  Exemple — au départ, la fonction a un trou :

      def double(n):
          ...

  À toi de remplacer le « ... » par la vraie réponse :

      def double(n):
          return n * 2

  Chaque fonction t'explique tout ce qu'il faut : son OBJECTIF, un EXEMPLE,
  un RAPPEL DU COURS (le bout de code dont tu as besoin), et les ÉTAPES.
  Tu n'as PAS besoin de lire le bas du fichier.

▶ ⚠️ DEUX PIÈGES QUI FONT ÉCHOUER 90 % DES DÉBUTANTS :

  PIÈGE 1 — « return » et PAS « print »
  ──────────────────────────────────────
  Dans les exercices, ta fonction doit RENVOYER le résultat avec « return ».
  Si tu utilises « print », le texte s'AFFICHE à l'écran mais la fonction
  renvoie None (= rien), et le test échoue.

      ❌ FAUX :   print(f"Bonjour {nom}")     → affiche, mais renvoie None
      ✅ JUSTE :  return f"Bonjour {nom}"      → renvoie le texte au test

  print = AFFICHER à l'écran (pour toi).
  return = RENVOYER la réponse (pour le programme qui appelle ta fonction).

  PIÈGE 2 — les paramètres sont DÉJÀ remplis, ne les réécris pas
  ───────────────────────────────────────────────────────────────
  Quand tu écris  def presenter(nom, age):  les variables « nom » et « age »
  sont DÉJÀ remplies par celui qui appelle ta fonction. N'écris PAS
  nom = "Ada" ou age = 25 dans la fonction : ça ÉCRASE la vraie valeur.

      def presenter(nom, age):        # nom et age sont DÉJÀ là !
          ❌ nom = "Ada"              # ÉCRASE nom → toujours "Ada"
          ❌ age = 25                 # ÉCRASE age → toujours 25
          return f"... {nom} ... {age} ..."

      def presenter(nom, age):        # nom et age sont DÉJÀ là !
          ✅ return f"... {nom} ... {age} ..."    # UTILISE nom et age tels quels

  Imagine que les paramètres sont des BOÎTES déjà remplies par l'appelant.
  Toi, tu les OUVRES (tu les utilises), tu ne les REMPLIS PAS toi-même.

▶ 💾 ASTUCE « git pull » (pour ne jamais perdre ton travail) :
  Ne code pas directement dans ce fichier (il est suivi par git). Copie-le et
  travaille dans la copie — elle est ignorée par git, donc une mise à jour du
  guide (« git pull ») ne touchera jamais ton travail :
      cp exercices.py exercices_perso.py      # puis :  python3 exercices_perso.py

▶ LANCER LES TESTS :   python3 exercices.py
  Pour chaque ❌, le test affiche ce qu'il ATTENDAIT et ce que TA fonction
  a renvoyé : compare les deux, ton erreur est dans l'écart.

▶ BLOQUÉ ? Réessaie en relisant le RAPPEL DU COURS dans la fonction. En tout
  dernier recours, ouvre solutions.py (le corrigé commenté).
"""


# ┌──────────────────────────────────────────────────────────────────┐
# │  NIVEAU 1 — REPRODUCTION (je refais ce que le cours montre)     │
# └──────────────────────────────────────────────────────────────────┘

def presenter(nom, age):
    """OBJECTIF : renvoyer un texte de présentation.

    Exemple : presenter("Ada", 25)  ->  "Je m'appelle Ada et j'ai 25 ans."

    ⚠️ ATTENTION — lis bien avant de coder :
      - « nom » et « age » sont les PARAMÈTRES de la fonction : ils sont
        DÉJÀ remplis par celui qui appelle. N'écris PAS nom = "Ada" !
      - Utilise « return » (pas print) pour RENVOYER le texte.

    RAPPEL DU COURS (section « Les f-strings ») :
    ┌─────────────────────────────────────────────────────┐
    │  def message_joueur(nom, score):                    │
    │      return f"Joueur : {nom} | Score : {score}"     │
    │                                                     │
    │  message_joueur("Baba", 100)                        │
    │  # → "Joueur : Baba | Score : 100"                  │
    │                                                     │
    │  message_joueur("Toto", 50)                         │
    │  # → "Joueur : Toto | Score : 50"                   │
    │                                                     │
    │  Le f devant les guillemets dit à Python : remplace  │
    │  {nom} par la valeur de nom, {score} par celle de    │
    │  score. « return » renvoie le texte au programme.    │
    └─────────────────────────────────────────────────────┘
    C'est le MÊME schéma ici :
      - {nom} sera remplacé par "Ada" (ou "Bob", ou n'importe quel nom
        qu'on passe à l'appel) ;
      - {age} sera remplacé par 25 (ou 17, ou tout autre nombre).

    Comment t'y prendre (UNE SEULE LIGNE suffit) :
      return f"Je m'appelle {nom} et j'ai {age} ans."
    """
    ...   # ⬅️ remplace cette ligne par ton code (UNE seule ligne avec return)


def categorie_age(age):
    """OBJECTIF : renvoyer la catégorie d'âge sous forme de texte.
      - age < 13           →  "Enfant"
      - 13 <= age <= 17    →  "Adolescent"
      - age >= 18          →  "Majeur"

    Exemples : categorie_age(10) -> "Enfant"   categorie_age(15) -> "Adolescent"
               categorie_age(20) -> "Majeur"

    ⚠️ ATTENTION : « age » est le PARAMÈTRE — il est DÉJÀ rempli.
      N'écris PAS age = 20. Utilise « return » (pas print).

    RAPPEL DU COURS (section « if / elif / else ») :
    ┌─────────────────────────────────────────────────────┐
    │  def categorie(age):                                │
    │      if age >= 18:                                  │
    │          return "Majeur"                            │
    │      elif age >= 13:                                │
    │          return "Adolescent"                        │
    │      else:                                          │
    │          return "Enfant"                            │
    │                                                     │
    │  categorie(10)   # → "Enfant"                       │
    │  categorie(15)   # → "Adolescent"                   │
    │  categorie(20)   # → "Majeur"                       │
    └─────────────────────────────────────────────────────┘
    C'est EXACTEMENT ce code. Tu peux le recopier tel quel.

    Comment t'y prendre :
      if age >= 18:
          return "Majeur"
      elif age >= 13:
          return "Adolescent"
      else:
          return "Enfant"
    """
    ...   # ⬅️ remplace ces lignes par le if / elif / else avec return


# ┌──────────────────────────────────────────────────────────────────┐
# │  NIVEAU 2 — ADAPTATION (même logique, petit changement)        │
# └──────────────────────────────────────────────────────────────────┘

def est_pair(n):
    """OBJECTIF : renvoyer True si n est pair, False sinon.

    Exemples : est_pair(4)  ->  True       est_pair(7)  ->  False

    RAPPEL DU COURS (section « Opérations sur les nombres ») :
    ┌─────────────────────────────────────────────────────┐
    │  print(7 % 3)    # 1   MODULO : le reste            │
    │  # nombre % 2 == 0  teste si un nombre est pair     │
    └─────────────────────────────────────────────────────┘
    Le test  n % 2 == 0  vaut déjà True ou False. Il suffit de le renvoyer.

    Comment t'y prendre :
      - renvoie le résultat du test  n % 2 == 0.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def convertir_temperature(celsius):
    """OBJECTIF : convertir des degrés Celsius en degrés Fahrenheit.
    La formule est :  fahrenheit = celsius * 9 / 5 + 32

    Exemples : convertir_temperature(0)    ->  32.0
               convertir_temperature(100)  ->  212.0

    RAPPEL DU COURS (section « Opérations sur les nombres ») :
    ┌─────────────────────────────────────────────────────┐
    │  print(7 + 3)    # 10   addition                    │
    │  print(7 * 3)    # 21   multiplication               │
    │  print(7 / 3)    # 2.33  division (donne un float)   │
    └─────────────────────────────────────────────────────┘
    Tu connais +, *, / : applique la formule et renvoie le résultat.

    Comment t'y prendre :
      - calcule  celsius * 9 / 5 + 32 ;
      - renvoie le résultat avec return.
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ┌──────────────────────────────────────────────────────────────────┐
# │  NIVEAU 3 — COMBINAISON (je mélange 2 concepts du cours)       │
# └──────────────────────────────────────────────────────────────────┘

def somme_jusqua(n):
    """OBJECTIF : renvoyer la somme de tous les entiers de 1 à n inclus.

    Exemple : somme_jusqua(5)  ->  15   (car 1 + 2 + 3 + 4 + 5 = 15)

    RAPPEL DU COURS (section « La boucle for ») :
    ┌─────────────────────────────────────────────────────┐
    │  for i in range(5):         # i vaut 0, 1, 2, 3, 4 │
    │      print(f"Tour {i}")                             │
    │                                                     │
    │  # range(1, 6) → 1, 2, 3, 4, 5  (6 est exclu)     │
    └─────────────────────────────────────────────────────┘
    RAPPEL (section « Les raccourcis d'affectation ») :
    ┌─────────────────────────────────────────────────────┐
    │  total += 1   # total = total + 1                   │
    └─────────────────────────────────────────────────────┘
    Combine les deux : une boucle for qui AJOUTE i au total à chaque tour.

    Comment t'y prendre :
      1. crée un total à 0 :  total = 0
      2. parcours les nombres de 1 à n avec :  for i in range(1, n + 1):
         (range(1, n + 1) va de 1 jusqu'à n INCLUS car n+1 est exclu)
      3. à chaque tour, ajoute i :  total += i
      4. après la boucle, renvoie total.
    """
    ...   # ⬅️ remplace cette ligne par ton code


def compter_pairs(limite):
    """OBJECTIF : compter combien de nombres PAIRS il y a de 1 à `limite` inclus.

    Exemples : compter_pairs(10) -> 5    (2, 4, 6, 8, 10 = cinq nombres pairs)
               compter_pairs(7)  -> 3    (2, 4, 6 = trois nombres pairs)

    RAPPEL DU COURS — tu combines une boucle for ET une condition if :
    ┌─────────────────────────────────────────────────────┐
    │  for i in range(1, 11):   # i va de 1 à 10         │
    │      if i % 2 == 0:       # si i est pair           │
    │          print(i)                                   │
    └─────────────────────────────────────────────────────┘
    Au lieu de print, tu COMPTES : un compteur qui commence à 0 et qui
    augmente de 1 à chaque nombre pair trouvé.

    Comment t'y prendre :
      1. crée un compteur à 0 :  compteur = 0
      2. parcours de 1 à limite inclus :  for i in range(1, limite + 1):
      3. si i est pair (i % 2 == 0), ajoute 1 :  compteur += 1
      4. après la boucle, renvoie compteur.
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ┌──────────────────────────────────────────────────────────────────┐
# │  NIVEAU 4 — DÉFI (facultatif, pour aller plus loin)            │
# └──────────────────────────────────────────────────────────────────┘

def fizzbuzz(n):
    """OBJECTIF : pour UN nombre n, renvoyer (sous forme de TEXTE) :
      - "FizzBuzz" si n est divisible par 3 ET par 5 ;
      - "Fizz"     si divisible par 3 seulement ;
      - "Buzz"     si divisible par 5 seulement ;
      - sinon, le nombre lui-même converti en texte, ex. "7".

    Exemples : fizzbuzz(15) -> "FizzBuzz"   fizzbuzz(9) -> "Fizz"
               fizzbuzz(10) -> "Buzz"       fizzbuzz(7) -> "7"

    RAPPEL DU COURS — tu combines le modulo ET le if/elif/else :
    ┌─────────────────────────────────────────────────────┐
    │  n % 3 == 0     # True si n est divisible par 3     │
    │  n % 5 == 0     # True si n est divisible par 5     │
    │                                                     │
    │  if condition1 and condition2:  # les DEUX vraies    │
    │      ...                                            │
    │  elif condition1:                                   │
    │      ...                                            │
    │  elif condition2:                                   │
    │      ...                                            │
    │  else:                                              │
    │      ...                                            │
    └─────────────────────────────────────────────────────┘
    PIÈGE : teste le cas « divisible par 3 ET par 5 » EN PREMIER.
    Sinon, le cas « par 3 » l'attrape avant et tu n'arrives jamais au « ET ».

    Comment t'y prendre :
      - if n % 3 == 0 and n % 5 == 0: return "FizzBuzz"
      - elif n % 3 == 0: return "Fizz"
      - elif n % 5 == 0: return "Buzz"
      - else: return str(n)     (str() convertit le nombre en texte)
    """
    ...   # ⬅️ remplace cette ligne par ton code


# ════════════════════════════════════════════════════════════════════
#  ▶ ON TESTE TON CODE — lance le fichier pour voir tes ✅ / ❌
#
#  C'est ICI qu'on APPELLE tes fonctions, avec des exemples concrets.
#  → Les valeurs ci-dessous (comme "Ada", 25, "Bob", 17...) sont juste
#    des ARGUMENTS qu'on passe à l'appel. Rien de magique ni de caché.
#
#  POURQUOI PLUSIEURS TESTS PAR FONCTION ?
#  On teste presenter("Ada", 25) ET presenter("Bob", 17) pour vérifier
#  que ta fonction marche avec N'IMPORTE QUEL nom et N'IMPORTE QUEL age
#  — pas seulement avec "Ada". Si ton code dit toujours "Ada" même quand
#  on lui donne "Bob", c'est que tu as écrit nom = "Ada" dans la fonction
#  au lieu d'UTILISER le paramètre nom tel quel.
#
#  Comment lire une ligne de test :
#      verifie(presenter, "Ada", 25, attendu="Je m'appelle Ada et j'ai 25 ans.")
#   → appelle  presenter("Ada", 25)  et compare le résultat au texte attendu.
#      verifie(presenter, "Bob", 17, attendu="Je m'appelle Bob et j'ai 17 ans.")
#   → appelle  presenter("Bob", 17)  — ta fonction doit marcher aussi pour Bob !
# ════════════════════════════════════════════════════════════════════
import types as _types


def verifie(fonction, *arguments, attendu):
    """Appelle fonction(*arguments) et compare au résultat attendu. (Mécanique du test.)"""
    try:
        obtenu = fonction(*arguments)
        if isinstance(obtenu, _types.GeneratorType):
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
    print("--- Module 01 : les bases ---\n")

    print("NIVEAU 1 — REPRODUCTION")
    resultats = [
        verifie(presenter, "Ada", 25,   attendu="Je m'appelle Ada et j'ai 25 ans."),
        verifie(presenter, "Bob", 17,   attendu="Je m'appelle Bob et j'ai 17 ans."),
        verifie(categorie_age, 10,      attendu="Enfant"),
        verifie(categorie_age, 15,      attendu="Adolescent"),
        verifie(categorie_age, 20,      attendu="Majeur"),
    ]

    print("\nNIVEAU 2 — ADAPTATION")
    resultats += [
        verifie(est_pair, 4,            attendu=True),
        verifie(est_pair, 7,            attendu=False),
        verifie(convertir_temperature, 0,   attendu=32.0),
        verifie(convertir_temperature, 100, attendu=212.0),
    ]

    print("\nNIVEAU 3 — COMBINAISON")
    resultats += [
        verifie(somme_jusqua, 5,        attendu=15),
        verifie(somme_jusqua, 1,        attendu=1),
        verifie(compter_pairs, 10,      attendu=5),
        verifie(compter_pairs, 7,       attendu=3),
    ]

    print("\nNIVEAU 4 — DÉFI")
    resultats += [
        verifie(fizzbuzz, 15,           attendu="FizzBuzz"),
        verifie(fizzbuzz, 9,            attendu="Fizz"),
        verifie(fizzbuzz, 10,           attendu="Buzz"),
        verifie(fizzbuzz, 7,            attendu="7"),
    ]

    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
