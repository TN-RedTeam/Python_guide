#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère les icônes PWA (PNG) en pur stdlib — aucune dépendance (pas de PIL).

Usage :  python3 webapp/make_icons.py
Produit : webapp/icons/icon-192.png, icon-512.png, icon-maskable-512.png

Design : fond dégradé indigo→violet à coins arrondis, serpent stylisé (courbe
en S faite de disques qui s'affinent vers la queue) + œil.
"""

import math
import struct
import zlib
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent / "icons"


def ecrire_png(chemin: Path, pixels: list[list[tuple]]) -> None:
    """Écrit une image RGBA (liste de lignes de tuples) au format PNG."""
    hauteur, largeur = len(pixels), len(pixels[0])

    def bloc(genre: bytes, donnees: bytes) -> bytes:
        return (struct.pack(">I", len(donnees)) + genre + donnees
                + struct.pack(">I", zlib.crc32(genre + donnees)))

    brut = b"".join(
        b"\x00" + b"".join(bytes(px) for px in ligne) for ligne in pixels
    )
    entete = struct.pack(">IIBBBBB", largeur, hauteur, 8, 6, 0, 0, 0)
    chemin.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + bloc(b"IHDR", entete)
        + bloc(b"IDAT", zlib.compress(brut, 9))
        + bloc(b"IEND", b"")
    )


def melanger(dessous: tuple, dessus: tuple, alpha: float) -> tuple:
    """Pose `dessus` sur `dessous` avec une opacité 0..1 (anti-crénelage)."""
    a = max(0.0, min(1.0, alpha))
    return (
        round(dessous[0] * (1 - a) + dessus[0] * a),
        round(dessous[1] * (1 - a) + dessus[1] * a),
        round(dessous[2] * (1 - a) + dessus[2] * a),
        max(dessous[3], round(255 * a)) if dessous[3] < 255 else 255,
    )


def dessiner_icone(taille: int, pleine: bool) -> list[list[tuple]]:
    """`pleine=True` : fond bord à bord (icône « maskable » Android)."""
    s = taille / 512.0                       # facteur d'échelle
    rayon_coin = 0 if pleine else 96 * s
    haut = (93, 110, 255)                    # indigo (accent de l'app)
    bas = (147, 51, 234)                     # violet

    pixels = []
    for y in range(taille):
        t = y / (taille - 1)
        fond = tuple(round(haut[i] * (1 - t) + bas[i] * t) for i in range(3))
        ligne = []
        for x in range(taille):
            # coins arrondis : distance au rectangle intérieur
            dx = max(rayon_coin - x, x - (taille - 1 - rayon_coin), 0)
            dy = max(rayon_coin - y, y - (taille - 1 - rayon_coin), 0)
            dehors = math.hypot(dx, dy) - rayon_coin
            if dehors > 0.5:
                ligne.append((0, 0, 0, 0))
            elif dehors > -0.5:               # bord adouci
                a = 0.5 - dehors
                ligne.append((fond[0], fond[1], fond[2], round(255 * a)))
            else:
                ligne.append((fond[0], fond[1], fond[2], 255))
        pixels.append(ligne)

    def disque(cx: float, cy: float, r: float, couleur: tuple) -> None:
        x0, x1 = max(0, int(cx - r - 1)), min(taille - 1, int(cx + r + 1))
        y0, y1 = max(0, int(cy - r - 1)), min(taille - 1, int(cy + r + 1))
        for yy in range(y0, y1 + 1):
            for xx in range(x0, x1 + 1):
                d = math.hypot(xx - cx, yy - cy)
                if d <= r + 0.5 and pixels[yy][xx][3] > 0:
                    pixels[yy][xx] = melanger(pixels[yy][xx], couleur, r + 0.5 - d)

    # ── le serpent : courbe en S, épaisse à la tête, fine à la queue ──
    vert = (74, 222, 128)
    vert_sombre = (22, 163, 74)
    marge = 150 * s if not pleine else 170 * s
    for i in range(120):
        t = i / 119.0                                        # 0 = queue, 1 = tête
        cx = taille / 2 + math.sin(t * math.pi * 2.1 + 0.4) * (taille / 2 - marge)
        cy = (taille - 2 * marge) * (1 - t) + marge
        r = (10 + 30 * t) * s
        disque(cx, cy, r * 1.18, vert_sombre)               # liseré sombre
        disque(cx, cy, r, vert)

    # tête un peu plus large + œil
    tete_x = taille / 2 + math.sin(1 * math.pi * 2.1 + 0.4) * (taille / 2 - marge)
    tete_y = marge
    disque(tete_x, tete_y, 46 * s, vert_sombre)
    disque(tete_x, tete_y, 40 * s, vert)
    disque(tete_x + 14 * s, tete_y - 8 * s, 9 * s, (15, 18, 32))
    disque(tete_x + 16 * s, tete_y - 10 * s, 3 * s, (255, 255, 255))

    return pixels


def main() -> None:
    DOSSIER.mkdir(exist_ok=True)
    ecrire_png(DOSSIER / "icon-512.png", dessiner_icone(512, pleine=False))
    ecrire_png(DOSSIER / "icon-192.png", dessiner_icone(192, pleine=False))
    ecrire_png(DOSSIER / "icon-maskable-512.png", dessiner_icone(512, pleine=True))
    for f in sorted(DOSSIER.glob("*.png")):
        print(f"✅ {f.name} ({f.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    main()
