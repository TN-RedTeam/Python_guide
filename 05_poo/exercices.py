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

  Chaque classe t'explique tout ce qu'il faut : son OBJECTIF, un EXEMPLE, et ce
  que doit faire chaque méthode. Tu n'as PAS besoin de lire le bas du fichier.

▶ 💾 ASTUCE « git pull » (pour ne jamais perdre ton travail) :
  Ne code pas directement dans ce fichier (il est suivi par git). Copie-le et
  travaille dans la copie — elle est ignorée par git, donc une mise à jour du
  guide (« git pull ») ne touchera jamais ton travail :
      cp exercices.py exercices_perso.py      # puis :  python3 exercices_perso.py

▶ LANCER LES TESTS :   python3 exercices.py
  Pour chaque ❌, le test affiche ce qu'il ATTENDAIT et ce que TON code a
  produit : compare les deux, ton erreur est dans l'écart.

▶ BLOQUÉ ? Réessaie en relisant l'indication de la classe. En tout dernier
  recours, ouvre solutions.py (le corrigé commenté).
"""


# ─────────────────────────────────────────────────────────────────────
# NIVEAU 1 — ta première classe : __init__ + une méthode
# ─────────────────────────────────────────────────────────────────────

class Animal:
    """OBJECTIF : un animal avec un nom et un cri.

    Exemple : Animal("Rex", "Wouf").parler()  ->  "Rex fait Wouf !"

    RAPPEL DU COURS (section 2 — définir une classe) :
        class Voiture:
            def __init__(self, marque, couleur):   # le constructeur
                self.marque = marque               # on RANGE dans l'objet
                self.couleur = couleur
            def klaxonner(self):                    # une méthode
                return f"La {self.marque} fait : POUT POUT !"

    C'est le MEME schéma ici :
      - __init__ reçoit nom et cri, et les RANGE dans self ;
      - parler() les RELIT avec self.nom et self.cri.

    Tu dois compléter 2 méthodes :
      - __init__(self, nom, cri) : range self.nom = nom  et  self.cri = cri ;
      - parler(self) : renvoie f"{self.nom} fait {self.cri} !"
    """

    def __init__(self, nom, cri):
        ...   # ⬅️ range nom et cri dans self (self.nom = nom, self.cri = cri)

    def parler(self):
        ...   # ⬅️ renvoie f"{self.nom} fait {self.cri} !"


# ─────────────────────────────────────────────────────────────────────
# NIVEAU 1 — une classe avec __init__ + deux méthodes de calcul
# ─────────────────────────────────────────────────────────────────────

class Rectangle:
    """OBJECTIF : un rectangle défini par sa largeur et sa hauteur.

    Exemple : Rectangle(3, 4).aire() -> 12   ;   Rectangle(3, 4).perimetre() -> 14

    RAPPEL DU COURS (section 2) : c'est exactement le schéma Voiture ci-dessus.
      - __init__ RANGE les données dans self ;
      - les méthodes les RELISENT avec self.xxx.

    Tu dois compléter 3 méthodes :
      - __init__(self, largeur, hauteur) : RANGE les deux valeurs dans l'objet
        (self.largeur = largeur, et pareil pour hauteur) ;
      - aire(self)      : renvoie largeur * hauteur (relis-les avec self.largeur...) ;
      - perimetre(self) : renvoie 2 * (largeur + hauteur).
    """

    def __init__(self, largeur, hauteur):
        ...   # ⬅️ range largeur et hauteur dans self (self.largeur = largeur, ...)

    def aire(self):
        ...   # ⬅️ renvoie self.largeur * self.hauteur

    def perimetre(self):
        ...   # ⬅️ renvoie 2 * (self.largeur + self.hauteur)


# ─────────────────────────────────────────────────────────────────────
# NIVEAU 2 — héritage : réutiliser une classe existante
# ─────────────────────────────────────────────────────────────────────

class Carre(Rectangle):
    """OBJECTIF : un carré EST un rectangle dont les deux côtés sont égaux.
    Il HÉRITE donc de Rectangle (il a déjà aire() et perimetre() gratuitement).

    Exemple : Carre(5).aire() -> 25   ;   Carre(5).perimetre() -> 20

    RAPPEL DU COURS (section 4 — héritage) :
        class Voiture(Vehicule):
            def __init__(self, nom, vitesse_max, nb_portes):
                super().__init__(nom, vitesse_max)   # appelle le parent
                self.nb_portes = nb_portes

    C'est le MEME schéma : super().__init__(...) appelle le constructeur de
    Rectangle. Comme un carré a TOUS les côtés égaux, on passe cote deux fois.

    À compléter : __init__(self, cote) doit appeler le constructeur du PARENT
    avec le même côté pour la largeur ET la hauteur :  super().__init__(cote, cote).
    """

    def __init__(self, cote):
        ...   # ⬅️ appelle super().__init__(cote, cote)


# ─────────────────────────────────────────────────────────────────────
# NIVEAU 3 — une classe avec logique : vérification avant action
# ─────────────────────────────────────────────────────────────────────

class CompteBancaire:
    """OBJECTIF : un compte qui mémorise un solde.

    Scénario : CompteBancaire(100), deposer(50) -> 150, retirer(200) refusé -> 150,
               retirer(30) -> 120.

    RAPPEL DU COURS (section 2 + section 3) :
      Dans __init__, on RANGE les données :
          self.solde = solde
      Dans une méthode, on MODIFIE les données de l'objet :
          self.solde += montant      (augmente)
          self.solde -= montant      (diminue)
      Et on peut ajouter un if pour PROTÉGER (comme le if du module 01) :
          if montant <= self.solde:
              self.solde -= montant

    Tu dois compléter 3 méthodes :
      - __init__(self, solde=0) : range le solde de départ dans self (self.solde = solde) ;
      - deposer(self, montant)  : augmente le solde (self.solde += montant) ;
      - retirer(self, montant)  : diminue le solde, MAIS ne fait RIEN si le montant
        dépasse le solde (vérifie avec un if avant de soustraire).
    """

    def __init__(self, solde=0):
        ...   # ⬅️ range le solde dans self

    def deposer(self, montant):
        ...   # ⬅️ ajoute montant au solde

    def retirer(self, montant):
        ...   # ⬅️ si montant <= self.solde, soustrais-le ; sinon ne fais rien


# ════════════════════════════════════════════════════════════════════
#  ▶ ON TESTE TON CODE — lance le fichier pour voir tes ✅ / ❌
#
#  C'est ICI qu'on UTILISE tes classes : on crée des objets (ex. Rectangle(3, 4))
#  et on appelle leurs méthodes (ex. .aire()). Les nombres comme 3 et 4 sont
#  juste les ARGUMENTS qu'on donne au moment de créer l'objet.
#  C'est normal : en HAUT on DÉFINIT les classes, et plus bas on s'en SERT.
#
#  ⚙️ Détail technique : ici chaque appel est écrit après « lambda: » pour
#     permettre au test de gérer proprement une erreur. Concentre-toi sur le
#     texte de gauche entre guillemets : c'est le vrai appel, en clair.
# ════════════════════════════════════════════════════════════════════
def verifie(appel, produire, attendu):
    """`appel` : le texte de l'appel (pour l'affichage).
    `produire` : une mini-fonction (lambda) qui FABRIQUE le résultat à tester."""
    try:
        obtenu = produire()
    except Exception as e:
        obtenu = f"ERREUR: {e}"
    ok = (obtenu == attendu)
    print(f"{'✅' if ok else '❌'} {appel}  ->  {attendu!r}")
    if not ok:
        print(f"     ⚠️  ton code a renvoyé : {obtenu!r}")
    return ok


def scenario_compte():
    """Crée un compte et enchaîne quelques opérations ; renvoie le solde final."""
    c = CompteBancaire(100)
    c.deposer(50)        # solde : 150
    c.retirer(200)       # refusé (200 > 150) → reste 150
    c.retirer(30)        # solde : 120
    return c.solde


if __name__ == "__main__":
    print("--- Module 05 : la POO (classes) ---\n")
    resultats = [
        verifie("Animal('Rex', 'Wouf').parler()", lambda: Animal("Rex", "Wouf").parler(), attendu="Rex fait Wouf !"),
        verifie("Animal('Mia', 'Miaou').parler()", lambda: Animal("Mia", "Miaou").parler(), attendu="Mia fait Miaou !"),
        verifie("Rectangle(3, 4).aire()",      lambda: Rectangle(3, 4).aire(),      attendu=12),
        verifie("Rectangle(3, 4).perimetre()", lambda: Rectangle(3, 4).perimetre(), attendu=14),
        verifie("Carre(5).aire()",             lambda: Carre(5).aire(),             attendu=25),
        verifie("Carre(5).perimetre()",        lambda: Carre(5).perimetre(),        attendu=20),
        verifie("CompteBancaire (scénario)",   scenario_compte,                     attendu=120),
    ]
    print(f"\n{sum(resultats)}/{len(resultats)} réussis ✅")
