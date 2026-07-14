#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lance chaque solutions.py et exige un score PLEIN (« N/N réussis »).

Un corrigé qui plante, ou qui n'atteint pas 100 %, fait échouer la CI :
c'est la garantie que la référence montrée aux apprenants est correcte.
"""

import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
BILAN = re.compile(r"(\d+)\s*/\s*(\d+)\s+réussis")


def main() -> int:
    solutions = sorted(RACINE.glob("*/solutions.py")) + sorted(RACINE.glob("*/*/solutions.py"))
    echecs: list[str] = []
    for sol in solutions:
        rel = sol.relative_to(RACINE)
        print(f"▶ {rel}")
        res = subprocess.run([sys.executable, str(sol)], capture_output=True, text=True)
        sys.stdout.write(res.stdout)
        if res.returncode != 0:
            echecs.append(f"{rel} : le corrigé plante.\n{res.stderr.strip()}")
            continue
        scores = BILAN.findall(res.stdout)
        if scores:
            obtenu, total = scores[-1]
            if obtenu != total:
                echecs.append(f"{rel} : {obtenu}/{total} réussis (le corrigé n'est pas à 100 %).")

    if echecs:
        print(f"\n❌ {len(echecs)} corrigé(s) en défaut :")
        for e in echecs:
            print("  •", e)
        return 1
    print(f"\n✅ Les {len(solutions)} corrigés passent (score plein).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
