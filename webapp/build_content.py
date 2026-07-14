#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère webapp/content.json à partir des modules du dépôt (hors pentest).

Usage :  python3 webapp/build_content.py

Le fichier produit alimente la plateforme e-learning (webapp/index.html) :
pour chaque module on embarque le cours (README.md), les fichiers de démo,
les exercices et les solutions. On embarque aussi les guides transverses
(AIDE_MEMOIRE, LES_SYMBOLES…) et les mini-projets.
"""

import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent   # racine du dépôt
SORTIE = Path(__file__).resolve().parent / "content.json"

# Dossiers exclus de la plateforme (le pentest reste uniquement sur GitHub).
EXCLUS = {"pentest", "webapp", ".git", ".github"}

# Notes affichées dans l'IDE pour les modules dont certaines démos ne peuvent
# pas tourner dans un navigateur (pas de vrai disque, pas de réseau, pas de pip).
NOTES_NAVIGATEUR = {
    "00_demarrer": "Ce module parle d'installation : lis le cours, puis teste le "
                   "code dans le bac à sable — Python tourne déjà ici, dans ton navigateur !",
    "07_debugger": "breakpoint() / pdb sont interactifs : dans le navigateur, préfère "
                   "les print() pour suivre l'exécution. Les exercices, eux, fonctionnent.",
    "08_asyncio": "asyncio fonctionne dans le navigateur, mais certains affichages "
                  "peuvent arriver avec un léger décalage. Sur ta machine, tout est identique au cours.",
    "11_web_apis": "Les appels réseau (requests) ne sortent pas du navigateur : "
                   "lance les démos sur ta machine. Les exercices (JSON), eux, fonctionnent ici.",
    "12_taches_scripts": "La planification (cron / Planificateur Windows) se fait sur une "
                         "vraie machine. Les exercices fonctionnent ici.",
    "13_donnees_rapports": "Bonne nouvelle : pandas se télécharge automatiquement à la "
                           "première exécution (~15 Mo, sois patient·e). L'écriture de "
                           "fichiers Excel reste à tester sur ta machine.",
    "14_bibliotheques": "Ici, « pip install » est automatique : importe un paquet et il "
                        "est téléchargé (paquets en pur Python + ceux portés par Pyodide). "
                        "Sur ta machine, la vraie commande reste pip install.",
}

# Guides transverses embarqués (ordre d'affichage).
GUIDES = [
    ("LES_SYMBOLES.md", "Les symboles ( ) [ ] { } . = %", "🔣"),
    ("COMPRENDRE_LE_CODE.md", "Comprendre le code", "🧠"),
    ("ECRIRE_UN_SCRIPT.md", "Écrire un script (la méthode)", "✍️"),
    ("ANATOMIE_D_UN_SCRIPT.md", "Anatomie d'un script", "🦴"),
    ("AIDE_MEMOIRE.md", "Aide-mémoire", "📝"),
    ("GLOSSAIRE.md", "Glossaire", "📖"),
    ("PYTHON_VS_AUTRES_LANGAGES.md", "Python vs autres langages", "🆚"),
]

# ── Section « Pentest & sécurité » ──────────────────────────────────────
# Sous-dossiers du curriculum pentest, dans l'ordre d'affichage (titre lisible).
PENTEST_GROUPES = [
    ("01_basics", "01 · Bases Python"),
    ("02_network", "02 · Réseau"),
    ("03_web", "03 · Web"),
    ("04_recon", "04 · Reconnaissance"),
    ("05_automation", "05 · Automatisation"),
    ("06_crypto", "06 · Crypto & encodage"),
    ("offensif", "🎯 Démos offensives"),
]

# Scripts qui ne tournent PAS dans le navigateur (réseau ou système). Le reste
# (crypto, encodage, sqlite, hachage…) s'exécute très bien via Pyodide.
# Clé = chemin relatif depuis pentest/ ; valeur = "reseau" ou "systeme".
PENTEST_HORS_NAVIGATEUR = {
    "02_network/arp_detector.py": "systeme",
    "02_network/port_scanner.py": "reseau",
    "03_web/http_recon.py": "reseau",
    "04_recon/dns_recon.py": "reseau",
    "05_automation/cli_tool.py": "reseau",
    "offensif/deserialisation.py": "systeme",
    "offensif/injection_commande.py": "systeme",
    "offensif/ssrf.py": "reseau",
}
NOTE_RESEAU = ("🌐 Ce script ouvre des connexions réseau (sockets / HTTP / DNS) : le "
               "navigateur ne peut pas les établir. Lis le code et lance-le sur ta "
               "machine. Le terminal ci-dessous reste dispo pour tester du Python.")
NOTE_SYSTEME = ("🖥️ Ce script lance des commandes système (subprocess) : ça ne tourne "
                "pas dans le navigateur. Lance-le sur ta machine. Le terminal "
                "ci-dessous reste dispo pour tester du Python.")
NOTE_LAB = ("⚠️ Démonstration éducative — à exécuter uniquement sur tes propres "
            "systèmes ou un lab autorisé (CTF, DVWA…).")


def lire(chemin: Path) -> str:
    return chemin.read_text(encoding="utf-8")


def extraire_titre(markdown: str, defaut: str) -> tuple[str, str]:
    """Renvoie (emoji, titre) depuis le premier '# ...' du markdown."""
    for ligne in markdown.splitlines():
        if ligne.startswith("# "):
            brut = ligne[2:].strip()
            # Sépare un éventuel emoji de tête ("🚀 Module 00 : Démarrer…")
            m = re.match(r"^([^\w\s]+)\s+(.*)$", brut)
            emoji, titre = (m.group(1), m.group(2)) if m else ("", brut)
            # Retire le préfixe "Module NN :" / "Module NN —"
            titre = re.sub(r"^Module\s+\d+\s*[:—-]\s*", "", titre).strip()
            titre = titre.replace("`", "")
            titre = titre[0].upper() + titre[1:] if titre else titre
            return emoji, titre or defaut
    return "", defaut


def est_emoji(texte: str) -> bool:
    return any(unicodedata.category(c) == "So" for c in texte)


def fichiers_demo(dossier: Path) -> list[dict]:
    """Fichiers .py de démonstration (tout sauf exercices/solutions/tests)."""
    demos = []
    for f in sorted(dossier.glob("*.py")):
        if f.name in ("exercices.py", "solutions.py") or f.name.startswith("__"):
            continue
        demos.append({"name": f.name, "code": lire(f)})
    return demos


def construire_module(dossier: Path) -> dict:
    readme = lire(dossier / "README.md")
    emoji, titre = extraire_titre(readme, dossier.name)
    module = {
        "id": dossier.name,
        "num": dossier.name.split("_")[0],
        "emoji": emoji if est_emoji(emoji) else "📘",
        "title": titre,
        "readme": readme,
        "demos": fichiers_demo(dossier),
    }
    exercices = dossier / "exercices.py"
    solutions = dossier / "solutions.py"
    if exercices.exists():
        module["exercices"] = lire(exercices)
    if solutions.exists():
        module["solutions"] = lire(solutions)
    note = NOTES_NAVIGATEUR.get(dossier.name)
    if note:
        module["note"] = note
    return module


def construire_projets() -> dict:
    dossier = RACINE / "projets"
    projets = {
        "readme": lire(dossier / "README.md"),
        "files": fichiers_demo(dossier),
        "fil_rouge": {
            "readme": lire(dossier / "fil_rouge" / "README.md"),
            "files": fichiers_demo(dossier / "fil_rouge"),
        },
    }
    return projets


def note_pentest(rel_path: str, dans_offensif: bool) -> str | None:
    """Note affichée dans l'IDE pour un script pentest (None si rien à signaler)."""
    categorie = PENTEST_HORS_NAVIGATEUR.get(rel_path)
    if categorie == "reseau":
        return NOTE_RESEAU
    if categorie == "systeme":
        return NOTE_SYSTEME
    if dans_offensif:
        return NOTE_LAB
    return None


def construire_pentest() -> dict:
    """Section pentest : README global + chaque sous-dossier avec ses scripts."""
    base = RACINE / "pentest"
    groupes = []
    for nom, titre in PENTEST_GROUPES:
        dossier = base / nom
        if not dossier.is_dir():
            continue
        fichiers = []
        for f in sorted(dossier.glob("*.py")):
            if f.name.startswith("__"):
                continue
            entree = {"name": f.name, "code": lire(f)}
            note = note_pentest(f"{nom}/{f.name}", nom == "offensif")
            if note:
                entree["note"] = note
            fichiers.append(entree)
        groupe = {"id": nom, "titre": titre, "files": fichiers}
        readme = dossier / "README.md"
        if readme.exists():
            groupe["readme"] = lire(readme)
        groupes.append(groupe)
    return {"readme": lire(base / "README.md"), "groupes": groupes}


def main() -> None:
    modules = []
    for dossier in sorted(RACINE.iterdir()):
        if not dossier.is_dir() or dossier.name in EXCLUS:
            continue
        if not re.match(r"^\d{2}_", dossier.name):
            continue
        modules.append(construire_module(dossier))

    # Module de FONDATION « Penser comme un dev » : dossier sans préfixe
    # numérique (donc ignoré par le scan ci-dessus), inséré juste après
    # « Démarrer ». Il n'a pas de numéro : c'est le chapitre 0 du raisonnement.
    fondation = RACINE / "penser_comme_un_dev"
    if fondation.is_dir():
        mod = construire_module(fondation)
        mod["num"] = ""          # module de fondation, affiché sans numéro
        modules.insert(1, mod)

    guides = []
    for nom_fichier, titre, emoji in GUIDES:
        chemin = RACINE / nom_fichier
        if chemin.exists():
            guides.append({
                "id": chemin.stem,
                "title": titre,
                "emoji": emoji,
                "md": lire(chemin),
            })

    pentest = construire_pentest()

    contenu = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "modules": modules,
        "guides": guides,
        "projets": construire_projets(),
        "pentest": pentest,
        "modele_script": lire(RACINE / "modele_script.py"),
    }

    SORTIE.write_text(
        json.dumps(contenu, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    taille = SORTIE.stat().st_size / 1024
    nb_scripts = sum(len(g["files"]) for g in pentest["groupes"])
    print(f"✅ {SORTIE.name} généré : {len(modules)} modules, {len(guides)} guides, "
          f"pentest ({nb_scripts} scripts) — {taille:.0f} Ko")


if __name__ == "__main__":
    main()
