"""Render data/contributions.json as an animated, terminal-styled heatmap SVG.

STATIC=1 renders without animation (handy for previewing).
"""
import json
import os
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "contributions.json"
OUT = ROOT / "contrib-heatmap.svg"
STATIC = os.environ.get("STATIC") == "1"

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
CELL, GAP = 13, 3
PAD_X, TOP = 46, 64
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def level(count, peak):
    if count == 0:
        return 0
    ratio = count / peak
    if ratio >= 0.9:
        return 5
    if ratio >= 0.6:
        return 4
    if ratio >= 0.35:
        return 3
    if ratio >= 0.15:
        return 2
    return 1


def main():
    data = json.loads(DATA.read_text())
    days = data["days"]
    peak = max(1, max(d["count"] for d in days))
    first = date.fromisoformat(days[0]["date"])
    lead = (first.weekday() + 1) % 7  # GitHub weeks start on Sunday

    cells, month_starts, seen = [], [], None
    for i, d in enumerate(days):
        week, dow = divmod(i + lead, 7)
        x, y = PAD_X + week * (CELL + GAP), TOP + dow * (CELL + GAP)
        dt = date.fromisoformat(d["date"])
        if dt.month != seen:
            month_starts.append((x, MONTHS[dt.month - 1]))
            seen = dt.month
        anim = "" if STATIC else f' style="animation-delay:{(week + dow) * 0.022:.3f}s"'
        tip = f'{d["count"]} contribution{"" if d["count"] == 1 else "s"} on {d["date"]}'
        cells.append(
            f'<rect class="c" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2.5" '
            f'fill="{PALETTE[level(d["count"], peak)]}"{anim}><title>{tip}</title></rect>'
        )

    weeks = (len(days) + lead + 6) // 7
    width = PAD_X + weeks * (CELL + GAP) + 24
    grid_bottom = TOP + 7 * (CELL + GAP)
    height = grid_bottom + 64

    labels, last_x = [], -100
    for x, m in month_starts:
        if x - last_x >= 30:  # skip labels that would overlap
            labels.append(f'<text x="{x}" y="{TOP - 10}" class="m">{m}</text>')
            last_x = x

    dows = "".join(
        f'<text x="{PAD_X - 8}" y="{TOP + r * (CELL + GAP) + 10}" class="m" text-anchor="end">{n}</text>'
        for r, n in ((1, "Mon"), (3, "Wed"), (5, "Fri"))
    )

    lx = width - 24 - len(PALETTE) * (CELL + 3) - 34
    legend = (
        f'<text x="{lx - 8}" y="{grid_bottom + 24}" class="m" text-anchor="end">less</text>'
        + "".join(
            f'<rect x="{lx + i * (CELL + 3)}" y="{grid_bottom + 14}" width="{CELL}" height="{CELL}" rx="2.5" fill="{c}"/>'
            for i, c in enumerate(PALETTE)
        )
        + f'<text x="{lx + len(PALETTE) * (CELL + 3) + 5}" y="{grid_bottom + 24}" class="m">more</text>'
    )

    sep = '  <tspan class="dim">|</tspan>  '
    stats = (
        f'<tspan class="hi">{data["total"]:,}</tspan> contributions in the last year'
        f'{sep}streak <tspan class="hi">{data["current_streak"]}d</tspan>'
        f'{sep}longest <tspan class="hi">{data["longest_streak"]}d</tspan>'
        f'{sep}best day <tspan class="hi">{data["best_day"]["count"]}</tspan>'
    )

    css = f"""
    text {{ font-family: {FONT}; white-space: pre; }}
    .m {{ fill: #7d8590; font-size: 11px; }}
    .s {{ fill: #c9d1d9; font-size: 13px; }}
    .hi {{ fill: #39d353; font-weight: 700; }}
    .dim {{ fill: #484f58; }}
    """
    if not STATIC:
        css += """
    .c { opacity: 0; transform-box: fill-box; transform-origin: center;
         animation: drop .45s cubic-bezier(.2,.8,.3,1.3) forwards; }
    @keyframes drop { from { opacity: 0; transform: translateY(-10px) scale(.4); }
                      to   { opacity: 1; transform: none; } }
    .f { opacity: 0; animation: fade .6s ease 1.6s forwards; }
    @keyframes fade { to { opacity: 1; } }
    """

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="Contribution heatmap for {data["username"]}">
<style>{css}</style>
<rect x=".5" y=".5" width="{width - 1}" height="{height - 1}" rx="10" fill="#0d1117" stroke="#30363d"/>
<circle cx="20" cy="18" r="5.5" fill="#ff5f56"/><circle cx="38" cy="18" r="5.5" fill="#ffbd2e"/><circle cx="56" cy="18" r="5.5" fill="#27c93f"/>
<text x="{width / 2}" y="22" class="m" text-anchor="middle">~/contributions — {data["username"]}</text>
{"".join(labels)}{dows}
{"".join(cells)}
<g{"" if STATIC else ' class="f"'}>{legend}
<text x="{PAD_X}" y="{grid_bottom + 24}" class="s">{stats}</text>
<text x="{PAD_X}" y="{grid_bottom + 46}" class="m">updated {data["generated"]} · refreshed daily by GitHub Actions</text></g>
</svg>'''
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT.name} ({width}x{height})")


if __name__ == "__main__":
    main()
