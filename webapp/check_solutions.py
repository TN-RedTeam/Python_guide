#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vérifie les corrigés montrés aux apprenants.

1. Chaque `solutions.py` doit s'exécuter sans erreur. S'il imprime encore un
   bilan « N/N réussis » (ancien format), on exige en plus qu'il soit plein.

2. Pour les séries d'entraînement (`entrainement.py`) et les défis
   (`projets/defis/defi_*.py`), on va plus loin : la sortie du corrigé doit être
   EXACTEMENT les « 👀 Résultat attendu » écrits dans l'énoncé. Un énoncé qui
   promet un résultat que le corrigé ne produit pas fait échouer la CI.
   Les lignes qui commencent par « LIRE » (exercices « prédis la sortie ») sont
   comparées à part : celles du corrigé doivent être celles que l'énoncé affiche
   réellement quand on le lance tel quel.
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
BILAN = re.compile(r"(\d+)\s*/\s*(\d+)\s+réussis")
PREFIXE_ATTENDU = "#     "  # une ligne de résultat attendu : « # » puis 5 espaces


def resultats_attendus(source: str) -> list[str]:
    """Les lignes des blocs « 👀 Résultat attendu » d'un énoncé, dans l'ordre."""
    lignes: list[str] = []
    dans_bloc = False
    for ligne in source.splitlines():
        if ligne.lstrip().startswith("#") and "👀" in ligne:
            dans_bloc = True
            continue
        if dans_bloc:
            if ligne.startswith(PREFIXE_ATTENDU) and ligne.strip() != "#":
                lignes.append(ligne[len(PREFIXE_ATTENDU) :].rstrip())
            else:
                dans_bloc = False
    return lignes


def lancer(script: Path, dossier: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True, cwd=dossier
    )


def separer(sortie: str) -> tuple[list[str], list[str]]:
    """(lignes « LIRE … », autres lignes) — sans les lignes vides."""
    lignes = [li.rstrip() for li in sortie.splitlines() if li.strip()]
    return [li for li in lignes if li.startswith("LIRE")], [
        li for li in lignes if not li.startswith("LIRE")
    ]


def premier_ecart(attendu: list[str], obtenu: list[str]) -> str:
    for i, (a, o) in enumerate(zip(attendu, obtenu)):
        if a != o:
            return f"ligne {i + 1} : attendu {a!r}, obtenu {o!r}"
    return f"{len(attendu)} ligne(s) attendue(s), {len(obtenu)} obtenue(s)"


def verifier_paire(enonce: Path, corrige: Path) -> list[str]:
    """Compare un énoncé (résultats attendus) à la sortie de son corrigé."""
    rel = enonce.relative_to(RACINE)
    if not corrige.exists():
        return [f"{rel} : corrigé {corrige.name} absent."]
    echecs: list[str] = []
    with tempfile.TemporaryDirectory() as dossier:
        res_enonce = lancer(enonce, dossier)
        res_corrige = lancer(corrige, dossier)
    if res_enonce.returncode != 0:
        echecs.append(
            f"{rel} : l'énoncé plante quand on le lance tel quel.\n{res_enonce.stderr.strip()}"
        )
    if res_corrige.returncode != 0:
        return echecs + [
            f"{corrige.relative_to(RACINE)} : le corrigé plante.\n{res_corrige.stderr.strip()}"
        ]

    lire_enonce, _ = separer(res_enonce.stdout)
    lire_corrige, reste_corrige = separer(res_corrige.stdout)
    attendus = resultats_attendus(enonce.read_text(encoding="utf-8"))
    if reste_corrige != attendus:
        echecs.append(
            f"{rel} : la sortie du corrigé ne correspond pas aux « 👀 Résultat attendu » "
            f"({premier_ecart(attendus, reste_corrige)})."
        )
    if res_enonce.returncode == 0 and lire_corrige != lire_enonce:
        echecs.append(
            f"{rel} : les réponses « LIRE » du corrigé ne sont pas celles que l'énoncé affiche "
            f"({premier_ecart(lire_enonce, lire_corrige)})."
        )
    return echecs


def paires_a_verifier() -> list[tuple[Path, Path]]:
    paires = [
        (e, e.with_name("entrainement_solutions.py"))
        for e in sorted(RACINE.glob("*/entrainement.py"))
    ]
    for enonce in sorted((RACINE / "projets" / "defis").glob("defi_*.py")):
        if not enonce.stem.endswith("_solution"):
            paires.append((enonce, enonce.with_name(enonce.stem + "_solution.py")))
    return paires


def main() -> int:
    echecs: list[str] = []

    solutions = sorted(RACINE.glob("*/solutions.py")) + sorted(RACINE.glob("*/*/solutions.py"))
    for sol in solutions:
        rel = sol.relative_to(RACINE)
        print(f"▶ {rel}")
        res = lancer(sol)
        sys.stdout.write(res.stdout)
        if res.returncode != 0:
            echecs.append(f"{rel} : le corrigé plante.\n{res.stderr.strip()}")
            continue
        scores = BILAN.findall(res.stdout)
        if scores:
            obtenu, total = scores[-1]
            if obtenu != total:
                echecs.append(f"{rel} : {obtenu}/{total} réussis (le corrigé n'est pas à 100 %).")

    paires = paires_a_verifier()
    for enonce, corrige in paires:
        print(f"▶ {enonce.relative_to(RACINE)}  ↔  {corrige.name}")
        echecs.extend(verifier_paire(enonce, corrige))

    if echecs:
        print(f"\n❌ {len(echecs)} problème(s) :")
        for e in echecs:
            print("  •", e)
        return 1
    print(
        f"\n✅ Les {len(solutions)} corrigés s'exécutent sans erreur ; "
        f"{len(paires)} énoncé(s) vérifié(s) contre la sortie de leur corrigé."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
