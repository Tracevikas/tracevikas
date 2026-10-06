"""Neofetch-style info card (info-card.svg). Edit INFO below, then re-run.

STATIC=1 renders without animation.
"""
import os
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "info-card.svg"
STATIC = os.environ.get("STATIC") == "1"

USER, HOST = "vikas", "github"
INFO = [
    ("Name", "Vikas Kushwaha"),
    ("Role", "Software Engineer"),
    ("Now", "Building web apps @ Square Yards"),
    ("Learning", "Next.js internals, server components"),
    None,
    ("Languages", "JavaScript · TypeScript"),
    ("Frontend", "React · Next.js · Tailwind CSS"),
    ("Backend", "Node.js · MongoDB · MySQL"),
    ("Basics", "HTML5 · CSS3"),
    None,
    ("Portfolio", "github.com/Tracevikas/portfoliov2"),
    ("GitHub", "github.com/Tracevikas"),
    ("LinkedIn", "in/vikas-kushwaha-098844297"),
    ("Uptime", "on GitHub since 2020"),
    ("Hobby", "learning new things in my free time"),
]
COLORS = ["#ff5f56", "#ffbd2e", "#27c93f", "#58a6ff", "#bc8cff", "#39c5cf", "#c9d1d9"]

WIDTH, MIN_HEIGHT = 500, 424
PAD, HEAD, LINE_H = 22, 52, 22
KEY_W = 92
STEP = 0.12
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"


def main():
    rows, i, y = [], 0, HEAD + 14

    def line(content, extra_y=0):
        nonlocal i
        delay = "" if STATIC else f' style="animation-delay:{0.3 + i * STEP:.2f}s"'
        rows.append(f'<g class="l"{delay}>{content}</g>')
        i += 1

    title = f"{USER}@{HOST}"
    line(f'<text x="{PAD}" y="{y}"><tspan class="u">{USER}</tspan><tspan class="v">@</tspan>'
         f'<tspan class="u">{HOST}</tspan></text>')
    y += LINE_H
    line(f'<text x="{PAD}" y="{y - 6}" class="d">{"-" * len(title)}</text>')
    y += LINE_H - 6

    for item in INFO:
        if item is None:
            y += LINE_H // 2
            continue
        key, val = item
        line(f'<text x="{PAD}" y="{y}" class="k">{escape(key)}</text>'
             f'<text x="{PAD + KEY_W}" y="{y}" class="v">{escape(val)}</text>')
        y += LINE_H

    y += 6
    swatches = "".join(
        f'<rect x="{PAD + n * 26}" y="{y}" width="22" height="14" rx="2" fill="{c}"/>' for n, c in enumerate(COLORS)
    )
    line(swatches)

    HEIGHT = max(MIN_HEIGHT, y + 14 + PAD)

    css = f"""
    text {{ font-family: {FONT}; font-size: 13px; white-space: pre; }}
    .u {{ fill: #39d353; font-weight: 700; }}
    .k {{ fill: #58a6ff; font-weight: 700; }}
    .v {{ fill: #c9d1d9; }}
    .d {{ fill: #484f58; }}
    .t {{ fill: #7d8590; font-size: 11px; }}
    """
    if not STATIC:
        css += """
    .l { opacity: 0; animation: in .5s ease-out forwards; }
    @keyframes in { from { opacity: 0; transform: translateX(-12px); } to { opacity: 1; transform: none; } }
    """

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-label="About {USER}">
<style>{css}</style>
<rect x=".5" y=".5" width="{WIDTH - 1}" height="{HEIGHT - 1}" rx="10" fill="#0d1117" stroke="#30363d"/>
<circle cx="20" cy="18" r="5.5" fill="#ff5f56"/><circle cx="38" cy="18" r="5.5" fill="#ffbd2e"/><circle cx="56" cy="18" r="5.5" fill="#27c93f"/>
<text x="{WIDTH / 2:.0f}" y="22" class="t" text-anchor="middle">{USER}@{HOST}: ~/neofetch</text>
{"".join(rows)}
</svg>'''
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT.name} ({WIDTH}x{HEIGHT})")


if __name__ == "__main__":
    main()
