"""Build portable identity masters; view assets/PROVENANCE.md for sources."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".local" / "lib"))

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

COLORS = {
    "ground": "#191514", "field": "#352923", "ivory": "#F4ECE4",
    "sand": "#C7AE9C", "quiet": "#B59C8C",
}


class Lettering:
    def __init__(self, source: Path, weight: int):
        font = instantiateVariableFont(
            TTFont(source), {"wght": weight, "wdth": 100, "opsz": 72},
            inplace=False,
        )
        self.glyphs = font.getGlyphSet()
        self.cmap = font.getBestCmap()
        self.units = font["head"].unitsPerEm

    def draw(self, words, x, baseline, size, color, tracking=0):
        scale, cursor, paths = size / self.units, 0.0, []
        for char in words:
            name = self.cmap.get(ord(char))
            if name is None:
                raise ValueError(f"Font is missing {char!r}")
            glyph = self.glyphs[name]
            pen = SVGPathPen(self.glyphs)
            glyph.draw(pen)
            if command := pen.getCommands():
                paths.append(
                    f'<path transform="translate({cursor:.3f} 0)" d="{command}"/>'
                )
            cursor += glyph.width + tracking / scale
        return (
            f'<g fill="{color}" aria-label="{escape(words)}" '
            f'transform="translate({x} {baseline}) scale({scale:.6f} {-scale:.6f})">'
            + "".join(paths) + "</g>"
        )


def cat_portrait(x, y, width, height):
    """Place the exact existing avatar photo without repainting its pixels."""
    return (
        f'<image href="../../assets/cat-portrait.png" x="{x}" y="{y}" '
        f'width="{width}" height="{height}" preserveAspectRatio="xMidYMid meet"/>'
    )


def svg(width, height, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">
<title id="title">Pratham Sengar — Curious by default.</title>
<desc id="description">Pratham Sengar's dark charcoal and sepia identity featuring the exact cat photograph from his existing GitHub avatar.</desc>
<rect width="{width}" height="{height}" fill="{COLORS["ground"]}"/>
{body}
</svg>
'''


def build(font):
    bold, regular = Lettering(font, 700), Lettering(font, 450)
    desktop = f'<rect x="1045" width="555" height="580" fill="{COLORS["field"]}"/>'
    desktop += bold.draw("PRATHAM", 64, 225, 171, COLORS["ivory"], -2)
    desktop += bold.draw("SENGAR", 64, 390, 171, COLORS["sand"], -2)
    desktop += regular.draw("Curious by default.", 72, 485, 42, COLORS["ivory"])
    desktop += regular.draw("@Prathamji1505", 73, 535, 25, COLORS["quiet"])
    desktop += cat_portrait(1084, 28, 478, 400)
    desktop += regular.draw("Currently building.", 1100, 490, 32, COLORS["ivory"])

    mobile = bold.draw("PRATHAM", 42, 177, 143, COLORS["ivory"], -1.5)
    mobile += bold.draw("SENGAR", 42, 315, 143, COLORS["sand"], -1.5)
    mobile += f'<rect y="386" width="800" height="318" fill="{COLORS["field"]}"/>'
    mobile += cat_portrait(200, 395, 400, 300)
    mobile += regular.draw("Curious by default.", 48, 791, 44, COLORS["ivory"])
    mobile += regular.draw("@Prathamji1505", 50, 847, 27, COLORS["quiet"])

    outputs = {
        "profile-cat-desktop.svg": svg(1600, 580, desktop),
        "profile-cat-mobile.svg": svg(800, 900, mobile),
    }
    for filename, content in outputs.items():
        destination = ROOT / ".local" / "masters" / filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")
        print(f"Built {destination.relative_to(ROOT)}")

    record = {
        "font_sha256": hashlib.sha256(font.read_bytes()).hexdigest(),
        "font_axes": {"wght": [450, 700], "wdth": 100, "opsz": 72},
        "palette": COLORS,
        "masters": {
            name: hashlib.sha256(content.encode()).hexdigest()
            for name, content in outputs.items()
        },
        "origin": "Exact existing GitHub avatar photograph reused at the owner request, composed by tools/build_assets.py; avatar pixels unchanged.",
        "cat_portrait_sha256": hashlib.sha256((ROOT / "assets/cat-portrait.png").read_bytes()).hexdigest(),
    }
    (ROOT / "assets" / "manifest.json").write_text(
        json.dumps(record, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--font", type=Path,
        default=ROOT / ".local/fonts/BricolageGrotesque.ttf",
    )
    arguments = parser.parse_args()
    if not arguments.font.is_file():
        parser.error("Supply the Bricolage Grotesque font; see assets/PROVENANCE.md.")
    build(arguments.font)
