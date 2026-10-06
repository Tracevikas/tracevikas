"""Turn source-prepped.png into a self-typing ASCII portrait SVG (vikas-ascii.svg).

Falls back to the GitHub avatar when no prepped photo exists.
STATIC=1 renders without animation.
"""
import io
import os
from pathlib import Path
from xml.sax.saxutils import escape

import numpy as np
import requests
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "source-prepped.png"
OUT = ROOT / "vikas-ascii.svg"
USERNAME = os.environ.get("GH_USER", "Tracevikas")
STATIC = os.environ.get("STATIC") == "1"

RAMP = " .`:-=+*cs#%@"  # bright -> dark
COLS = 72
CHAR_W, LINE_H, FONT_SIZE = 5.0, 9.0, 8.6
PAD, HEAD = 16, 40
ROW_DUR, ROW_STEP = 0.35, 0.045
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"


def load_image():
    if SRC.exists():
        return Image.open(SRC).convert("L")
    print("source-prepped.png not found - using GitHub avatar")
    raw = requests.get(f"https://github.com/{USERNAME}.png?size=460", timeout=30).content
    return ImageOps.autocontrast(Image.open(io.BytesIO(raw)).convert("L"), cutoff=1)


def to_ascii(img):
    w, h = img.size
    rows = round(COLS * (h / w) * (CHAR_W / LINE_H))
    px = np.asarray(img.resize((COLS, rows), Image.LANCZOS), dtype=np.float32) / 255.0
    idx = ((1.0 - px) * (len(RAMP) - 1)).round().astype(int)
    lines = ["".join(RAMP[i] for i in row).rstrip() for row in idx]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def main():
    lines = to_ascii(load_image())
    width = PAD * 2 + COLS * CHAR_W
    height = HEAD + len(lines) * LINE_H + PAD + 8

    defs, texts = [], []
    for r, line in enumerate(lines):
        if not line.strip():
            continue
        y = HEAD + (r + 1) * LINE_H
        attrs = f'x="{PAD}" y="{y:.1f}" textLength="{len(line) * CHAR_W:.1f}" lengthAdjust="spacingAndGlyphs"'
        if STATIC:
            texts.append(f'<text {attrs}>{escape(line)}</text>')
            continue
        # each row is revealed left-to-right by a growing clip rect, like it's being typed
        defs.append(
            f'<clipPath id="r{r}"><rect x="{PAD}" y="{y - LINE_H:.1f}" width="0" height="{LINE_H + 2}">'
            f'<animate attributeName="width" from="0" to="{COLS * CHAR_W}" begin="{r * ROW_STEP:.3f}s" '
            f'dur="{ROW_DUR}s" fill="freeze"/></rect></clipPath>'
        )
        texts.append(f'<text {attrs} clip-path="url(#r{r})">{escape(line)}</text>')

    end = len(lines) * ROW_STEP + ROW_DUR
    cursor = "" if STATIC else (
        f'<rect x="{PAD}" y="{height - PAD - 4}" width="7" height="2" fill="#39d353" opacity="0">'
        f'<animate attributeName="opacity" values="0;1;0" dur="1s" begin="{end:.2f}s" repeatCount="indefinite"/></rect>'
    )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" viewBox="0 0 {width:.0f} {height:.0f}" role="img" aria-label="ASCII portrait of {USERNAME}">
<style>text {{ font-family: {FONT}; font-size: {FONT_SIZE}px; fill: #8ddb8c; white-space: pre; }}
.t {{ fill: #7d8590; font-size: 11px; }}</style>
<defs>{"".join(defs)}</defs>
<rect x=".5" y=".5" width="{width - 1:.0f}" height="{height - 1:.0f}" rx="10" fill="#0d1117" stroke="#30363d"/>
<circle cx="20" cy="18" r="5.5" fill="#ff5f56"/><circle cx="38" cy="18" r="5.5" fill="#ffbd2e"/><circle cx="56" cy="18" r="5.5" fill="#27c93f"/>
<text x="{width / 2:.0f}" y="22" class="t" text-anchor="middle">~/portrait.txt</text>
{"".join(texts)}
{cursor}
</svg>'''
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT.name} ({len(lines)} rows)")


if __name__ == "__main__":
    main()
