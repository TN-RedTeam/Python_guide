#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORRIGÉ — Défi 1 : analyser un relevé de dépenses

Une solution possible, découpée en une fonction par étape. La tienne peut
être différente et tout aussi juste : ce qui compte, c'est le résultat
affiché ET que tu saches expliquer chaque ligne.
⚠️ N'ouvre ce fichier qu'APRÈS avoir vraiment essayé.
"""

CONTENU = """date,categorie,libelle,montant
2026-03-02,courses,Supermarché,54
2026-03-03,transport,Métro,22
2026-03-05,loisirs,Cinéma,12
2026-03-09,courses,Boulangerie,8
2026-03-12,logement,Loyer,700
2026-03-15,transport,Essence,45
2026-03-21,courses,Supermarché,62
2026-03-27,loisirs,Concert,35
"""
with open("releve.csv", "w", encoding="utf-8") as f:
    f.write(CONTENU)


# ── ÉTAPE 1 — Lire le fichier ────────────────────────────────────────
def lire_releve(chemin):
    """Renvoie la liste des dépenses (un dictionnaire par ligne du fichier)."""
    with open(chemin, "r", encoding="utf-8") as f:
        lignes = f.readlines()

    depenses = []
    for ligne in lignes[1:]:                    # [1:] = tout sauf la 1re ligne (l'en-tête)
        morceaux = ligne.strip().split(",")     # "2026-03-02,courses,Supermarché,54" -> 4 morceaux
        depenses.append({
            "categorie": morceaux[1],
            "libelle": morceaux[2],
            "montant": int(morceaux[3]),        # le texte "54" devient le nombre 54
        })
    return depenses


depenses = lire_releve("releve.csv")
print(f"{len(depenses)} dépenses")
print(depenses[0])


# ── ÉTAPE 2 — Le total du mois ───────────────────────────────────────
def total(depenses):
    somme = 0
    for depense in depenses:                    # pattern accumulateur
        somme = somme + depense["montant"]
    return somme


print(f"Total : {total(depenses)} €")


# ── ÉTAPE 3 — Le total par catégorie ─────────────────────────────────
def total_par_categorie(depenses):
    totaux = {}
    for depense in depenses:
        categorie = depense["categorie"]
        # .get(categorie, 0) : le total déjà accumulé pour cette catégorie, ou 0
        totaux[categorie] = totaux.get(categorie, 0) + depense["montant"]
    return totaux


totaux = total_par_categorie(depenses)
print(totaux)


# ── ÉTAPE 4 — Le classement des catégories ───────────────────────────
def classement(totaux):
    """Renvoie les couples (catégorie, total), du plus gros total au plus petit."""
    # totaux.items() donne des couples (catégorie, total) ; paire[1] est le total.
    return sorted(totaux.items(), key=lambda paire: paire[1], reverse=True)


for categorie, montant in classement(totaux):
    print(f"{categorie} : {montant} €")


# ── ÉTAPE 5 — Enregistrer le rapport ─────────────────────────────────
def ecrire_rapport(chemin, totaux, total_general):
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("RAPPORT DE MARS\n")
        for categorie, montant in classement(totaux):   # on RÉUTILISE la fonction de l'étape 4
            f.write(f"{categorie} : {montant} €\n")
        f.write(f"TOTAL : {total_general} €\n")


ecrire_rapport("rapport.txt", totaux, total(depenses))
with open("rapport.txt", "r", encoding="utf-8") as f:
    print(f.read().strip())

# Ce qu'il faut remarquer : chaque étape est une fonction qui REÇOIT ce dont
# elle a besoin et RENVOIE son résultat. Le rapport de l'étape 5 ne recalcule
# rien : il appelle les fonctions des étapes précédentes. C'est ça, « découper ».
