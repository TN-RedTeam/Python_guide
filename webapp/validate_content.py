#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Valide la cohérence du contenu du cours et de webapp/content.json.

Lancé en CI (et en local : `python3 webapp/validate_content.py`). Sort en
erreur (code 1) au premier problème, en listant TOUT ce qui ne va pas.

Contrôles :
  1. Structure de content.json : chaque module a id / titre / emoji / readme ;
     un module avec `exercices` a des `solutions` (et inversement).
  2. Parité exercices ↔ solutions : toute fonction/classe définie DANS un
     exercice (ex. les fonctions buggées du module 07) existe dans le corrigé.
  3. Liens internes des cours (.md) : les chemins relatifs pointent sur des
     fichiers/dossiers qui existent vraiment (pas de lien mort).
"""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CONTENT = Path(__file__).resolve().parent / "content.json"

erreurs: list[str] = []


def erreur(msg: str) -> None:
    erreurs.append(msg)


# ─────────────────────── 1. Structure de content.json ───────────────────────


def valider_structure() -> None:
    if not CONTENT.exists():
        erreur("content.json absent — lance d'abord `python3 webapp/build_content.py`.")
        return
    data = json.loads(CONTENT.read_text(encoding="utf-8"))

    for cle in ("modules", "guides", "projets", "pentest"):
        if cle not in data:
            erreur(f"content.json : clé « {cle} » manquante.")

    for m in data.get("modules", []):
        ident = m.get("id", "??")
        for champ in ("id", "num", "emoji", "title", "readme"):
            if champ not in m:
                erreur(f"module {ident} : champ « {champ} » manquant.")
        if not (m.get("readme") or "").strip():
            erreur(f"module {ident} : README vide.")
        # exercices <-> solutions vont par paire
        if ("exercices" in m) != ("solutions" in m):
            erreur(f"module {ident} : exercices et solutions doivent aller ensemble.")

    pentest = data.get("pentest", {})
    for g in pentest.get("groupes", []):
        if not g.get("files"):
            erreur(f"pentest/{g.get('id')} : aucun script.")


# ──────────────── 2 & 3. Parité et contrat des exercices/solutions ───────────


def _parse(fichier: Path) -> ast.Module:
    return ast.parse(fichier.read_text(encoding="utf-8"))


def unites_pedagogiques(fichier: Path) -> set[str]:
    """Fonctions ET classes définies au premier niveau — les « unités » que
    l'apprenant implémente. On exclut les harnais d'auto-correction, dont les
    noms varient selon la convention du module (verifie / _check / _verifier…)."""
    HARNAIS = {
        "verifie",
        "_check",
        "_verifier",
        "afficher",
        "_lancer_les_essais",
        "_verifier_async",
    }
    unites = set()
    for n in _parse(fichier).body:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if n.name not in HARNAIS and not n.name.startswith("scenario"):
                unites.add(n.name)
    return unites


def valider_exercices() -> None:
    exercices = sorted(RACINE.glob("*/exercices.py")) + sorted(RACINE.glob("*/*/exercices.py"))
    for exo in exercices:
        sol = exo.with_name("solutions.py")
        module = exo.parent.name
        if not sol.exists():
            erreur(f"{module} : exercices.py sans solutions.py.")
            continue
        # Parité : toute unité (fonction/classe) définie DANS l'exercice (ex. les
        # fonctions buggées du module 07) doit exister aussi dans les solutions.
        # Le nouveau format d'exercices n'impose plus de fonctions (l'apprenant
        # écrit son code à partir de valeurs visibles), donc beaucoup d'exercices
        # ne définissent rien au premier niveau : la parité est alors triviale.
        manquantes = unites_pedagogiques(exo) - unites_pedagogiques(sol)
        if manquantes:
            erreur(
                f"{module} : corrigé incomplet — {sorted(manquantes)} "
                f"présent(es) dans exercices.py mais pas dans solutions.py."
            )


# ─────────────────────────── 4. Liens internes .md ──────────────────────────

LIEN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def valider_liens() -> None:
    fichiers = (
        list(RACINE.glob("*/README.md"))
        + list(RACINE.glob("*.md"))
        + list(RACINE.glob("projets/**/README.md"))
        + list(RACINE.glob("pentest/**/README.md"))
    )
    for md in fichiers:
        for cible in LIEN.findall(md.read_text(encoding="utf-8")):
            cible = cible.strip()
            # On ignore les liens externes, ancres, mails, et images data:
            if re.match(r"^(https?:|mailto:|#|data:|tel:)", cible):
                continue
            chemin = cible.split("#")[0].split("?")[0]
            if not chemin:
                continue
            cible_path = (md.parent / chemin).resolve()
            if not cible_path.exists():
                erreur(f"{md.relative_to(RACINE)} : lien mort → « {cible} »")


def valider_fraicheur() -> None:
    """content.json doit refléter les sources (sinon on a oublié de rebuild)."""
    try:
        import build_content
    except Exception as e:  # pragma: no cover
        erreur(f"impossible d'importer build_content : {e}")
        return
    if not CONTENT.exists():
        return  # déjà signalé par valider_structure
    attendu = build_content.construire_contenu()
    actuel = json.loads(CONTENT.read_text(encoding="utf-8"))
    sans_date = lambda d: {k: v for k, v in d.items() if k != "generated"}
    if sans_date(attendu) != sans_date(actuel):
        erreur(
            "content.json est périmé — relance `python3 webapp/build_content.py` et committe-le."
        )


def main() -> int:
    valider_structure()
    valider_fraicheur()
    valider_exercices()
    valider_liens()

    if erreurs:
        print(f"❌ {len(erreurs)} problème(s) détecté(s) :\n")
        for e in erreurs:
            print("  •", e)
        return 1
    print("✅ Contenu valide : structure, exercices/solutions et liens internes OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
