"""Dependency-free SVG figures. Colours adapt to light/dark mode on GitHub."""

from __future__ import annotations

import math
from html import escape

from .evaluate import Entry, _year_fraction

WIDTH, HEIGHT = 760, 440
MARGIN = {"left": 64, "right": 24, "top": 52, "bottom": 56}

STYLE = """
  .bg { fill: #ffffff; }
  .title { font: 600 15px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: #1f2328; }
  .subtitle, .tick, .axis-label { font: 11px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: #59636e; }
  .axis-label { font-size: 12px; }
  .grid { stroke: #d1d9e0; stroke-width: 1; }
  .axis { stroke: #818b98; stroke-width: 1; }
  .pt { fill: #0969da; fill-opacity: 0.55; stroke: #0969da; stroke-width: 0.8; }
  .pt-hi { fill: #cf222e; fill-opacity: 0.9; stroke: #cf222e; }
  .trend { stroke: #bf8700; stroke-width: 1.5; stroke-dasharray: 5 4; fill: none; }
  .label { font: 500 10.5px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: #1f2328; paint-order: stroke; stroke: #ffffff; stroke-width: 3px; stroke-linejoin: round; }
  @media (prefers-color-scheme: dark) {
    .bg { fill: #0d1117; }
    .title, .label { fill: #e6edf3; }
    .label { stroke: #0d1117; }
    .subtitle, .tick, .axis-label { fill: #9198a1; }
    .grid { stroke: #2f3742; }
    .axis { stroke: #656c76; }
    .pt { fill: #4493f8; stroke: #4493f8; }
    .pt-hi { fill: #ff7b72; stroke: #ff7b72; }
    .trend { stroke: #d29922; }
  }
"""


def _nice_ticks(lo: float, hi: float, target: int = 6) -> list[float]:
    span = hi - lo or 1.0
    raw = span / target
    magnitude = 10 ** math.floor(math.log10(raw))
    step = next(m * magnitude for m in (1, 2, 2.5, 5, 10) if m * magnitude >= raw)
    start = math.floor(lo / step) * step
    ticks = [round(start, 10)]
    while ticks[-1] < hi - step * 1e-9:  # last tick must cover hi
        ticks.append(round(ticks[-1] + step, 10))
    return ticks


def _y_ceiling(values: list[float]) -> float:
    """Axis ceiling that keeps extreme outliers (> 2x the runner-up) from flattening the plot."""
    distinct = sorted(set(values), reverse=True)
    if len(distinct) > 1 and distinct[0] > 2 * distinct[1]:
        return distinct[1] * 1.15
    return distinct[0]


def _scatter(*, title: str, subtitle: str, x_label: str, y_label: str,
             points: list[tuple[float, float, str, bool]],
             x_ticks: list[tuple[float, str]], y_ticks: list[float],
             trend: tuple[float, float] | None = None) -> str:
    x0, x1 = x_ticks[0][0], x_ticks[-1][0]
    y0, y1 = y_ticks[0], y_ticks[-1]
    pw = WIDTH - MARGIN["left"] - MARGIN["right"]
    ph = HEIGHT - MARGIN["top"] - MARGIN["bottom"]

    def sx(x: float) -> float:
        return MARGIN["left"] + (x - x0) / (x1 - x0) * pw

    def sy(y: float) -> float:
        return MARGIN["top"] + ph - (y - y0) / (y1 - y0) * ph

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}" role="img" aria-label="{escape(title)}">',
           f"<style>{STYLE}</style>",
           f'<rect class="bg" width="{WIDTH}" height="{HEIGHT}" rx="6"/>',
           f'<text class="title" x="{MARGIN["left"]}" y="24">{escape(title)}</text>',
           f'<text class="subtitle" x="{MARGIN["left"]}" y="40">{escape(subtitle)}</text>']
    for y in y_ticks:
        out.append(f'<line class="grid" x1="{MARGIN["left"]}" x2="{WIDTH - MARGIN["right"]}" y1="{sy(y):.1f}" y2="{sy(y):.1f}"/>')
        out.append(f'<text class="tick" x="{MARGIN["left"] - 8}" y="{sy(y) + 4:.1f}" text-anchor="end">{y:g}</text>')
    for x, text in x_ticks:
        out.append(f'<line class="axis" x1="{sx(x):.1f}" x2="{sx(x):.1f}" y1="{MARGIN["top"] + ph}" y2="{MARGIN["top"] + ph + 4}"/>')
        out.append(f'<text class="tick" x="{sx(x):.1f}" y="{MARGIN["top"] + ph + 18}" text-anchor="middle">{escape(text)}</text>')
    out.append(f'<line class="axis" x1="{MARGIN["left"]}" x2="{WIDTH - MARGIN["right"]}" y1="{MARGIN["top"] + ph}" y2="{MARGIN["top"] + ph}"/>')
    out.append(f'<text class="axis-label" x="{MARGIN["left"] + pw / 2}" y="{HEIGHT - 12}" text-anchor="middle">{escape(x_label)}</text>')
    out.append(f'<text class="axis-label" transform="translate(16 {MARGIN["top"] + ph / 2}) rotate(-90)" text-anchor="middle">{escape(y_label)}</text>')
    if trend:
        slope, intercept = trend
        out.append(f'<line class="trend" x1="{sx(x0):.1f}" y1="{sy(slope * x0 + intercept):.1f}" x2="{sx(x1):.1f}" y2="{sy(slope * x1 + intercept):.1f}"/>')
    for x, y, label, highlight in sorted(points, key=lambda p: p[3]):
        if y > y1:  # off-scale outlier: pin to the top edge and say so
            px, py = sx(x), MARGIN["top"] + 6
            out.append(f'<path class="pt pt-hi" d="M{px:.1f} {py - 6:.1f} L{px + 5:.1f} {py + 3:.1f} L{px - 5:.1f} {py + 3:.1f} Z"><title>{escape(label)}</title></path>')
            anchor = "end" if px > WIDTH - 220 else "start"
            dx = -9 if anchor == "end" else 9
            out.append(f'<text class="label" x="{px + dx:.1f}" y="{py + 3:.1f}" text-anchor="{anchor}">{escape(label)}, off scale</text>')
            continue
        css = "pt pt-hi" if highlight else "pt"
        out.append(f'<circle class="{css}" cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="{4 if highlight else 3.2}"><title>{escape(label)}</title></circle>')
        if highlight:
            anchor = "end" if sx(x) > WIDTH - 160 else "start"
            dx = -7 if anchor == "end" else 7
            out.append(f'<text class="label" x="{sx(x) + dx:.1f}" y="{sy(y) + 3.5:.1f}" text-anchor="{anchor}">{escape(label)}</text>')
    out.append("</svg>")
    return "\n".join(out)


def gi_over_time(entries: list[Entry], velocity: float | None) -> str:
    scored = [e for e in entries if e.gi is not None]
    xs = [_year_fraction(e.released) for e in scored]
    first, last = math.floor(min(xs) * 2) / 2, math.ceil(max(xs) * 2) / 2
    x_ticks = []
    t = first
    while t <= last + 1e-9:
        year, half = int(t), t % 1
        x_ticks.append((t, f"{year}" if half == 0 else f"{year} H2"))
        t += 0.5
    ceiling = _y_ceiling([e.gi for e in scored])
    in_range = sorted((e for e in scored if e.gi <= ceiling), key=lambda e: (-e.gi, e.nl))
    top = {in_range[0].model_id, in_range[-1].model_id}
    points = [(x, e.gi, f"{e.canonical_name} ({e.gi_raw})", e.model_id in top) for x, e in zip(xs, scored)]
    trend = None
    if velocity is not None:
        mx = sum(xs) / len(xs)
        my = sum(e.gi for e in scored) / len(scored)
        trend = (velocity, my - velocity * mx)
    subtitle = f"n = {len(scored)} models. Dashed line: OLS fit"
    if velocity is not None:
        subtitle += f", Generational Velocity = {velocity:+.2f} generations/year"
    return _scatter(title="Figure 1. Generation Index by release date",
                    subtitle=subtitle, x_label="Date first listed on OpenRouter",
                    y_label="Generation Index (GI)", points=points, x_ticks=x_ticks,
                    y_ticks=_nice_ticks(0, ceiling), trend=trend)


def gi_vs_nl(entries: list[Entry]) -> str:
    scored = [e for e in entries if e.gi is not None]
    ceiling = _y_ceiling([e.gi for e in scored])
    top = ({sorted(scored, key=lambda e: (-e.nl, e.model_id))[0].model_id}
           | {sorted(scored, key=lambda e: (-(e.ne or 0), e.model_id))[0].model_id})
    points = [(e.nl, e.gi, f"{e.canonical_name} (NE {e.ne:.3f})", e.model_id in top) for e in scored]
    x_ticks = [(t, f"{t:g}") for t in _nice_ticks(0, max(e.nl for e in scored))]
    return _scatter(title="Figure 2. Generation Index vs. Nomenclature Length",
                    subtitle=f"n = {len(scored)} models. Highlighted: longest name and highest Nomenclatural Efficiency",
                    x_label="Nomenclature Length (NL, characters)", y_label="Generation Index (GI)",
                    points=points, x_ticks=x_ticks, y_ticks=_nice_ticks(0, ceiling))


BAR_STYLE = """
  .bg { fill: #ffffff; }
  .title { font: 700 26px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: #1f2328; }
  .subtitle { font: 14px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: #59636e; }
  .panel { font: 600 16px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: #1f2328; }
  .panel-note { font: 12px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: #59636e; }
  .name { font: 500 13px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: #1f2328; }
  .vendor { font: 11px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: #59636e; }
  .value { font: 600 13px ui-monospace, 'Cascadia Mono', Consolas, monospace; fill: #1f2328; }
  .footer { font: 12px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: #818b98; }
  .bar-a { fill: #0969da; }
  .bar-b { fill: #bc4c00; }
  .rule { stroke: #d1d9e0; stroke-width: 1; }
  @media (prefers-color-scheme: dark) {
    .bg { fill: #0d1117; }
    .title, .panel, .name, .value { fill: #e6edf3; }
    .subtitle, .panel-note, .vendor { fill: #9198a1; }
    .footer { fill: #656c76; }
    .bar-a { fill: #4493f8; }
    .bar-b { fill: #f0883e; }
    .rule { stroke: #2f3742; }
  }
"""


def _vendor_champions(entries: list[Entry], metric: str, n: int) -> list[Entry]:
    """Best model per vendor on a metric; ties go to the most recently listed model."""
    best: dict[str, Entry] = {}
    for e in entries:
        if getattr(e, metric) is None:
            continue
        current = best.get(e.vendor)
        if current is None or (getattr(e, metric), e.released) > (getattr(current, metric), current.released):
            best[e.vendor] = e
    return sorted(best.values(), key=lambda e: (-getattr(e, metric), e.canonical_name.lower()))[:n]


def _bar_panel(x: float, y: float, width: float, rows: list[tuple[str, str, float, str]], css: str) -> list[str]:
    label_w, value_w, row_h, bar_h = 250, 56, 44, 20
    bar_max = width - label_w - value_w
    top = max(v for _, _, v, _ in rows)
    out = []
    for i, (name, vendor, value, text) in enumerate(rows):
        cy = y + i * row_h + row_h / 2
        out.append(f'<text class="name" x="{x + label_w - 12}" y="{cy - 2:.1f}" text-anchor="end">{escape(name)}</text>')
        out.append(f'<text class="vendor" x="{x + label_w - 12}" y="{cy + 13:.1f}" text-anchor="end">{escape(vendor)}</text>')
        w = max(2.0, value / top * bar_max)
        opacity = 1 if i == 0 else 0.72
        out.append(f'<rect class="{css}" x="{x + label_w}" y="{cy - bar_h / 2:.1f}" width="{w:.1f}" height="{bar_h}" rx="3" fill-opacity="{opacity}"/>')
        out.append(f'<text class="value" x="{x + label_w + w + 8:.1f}" y="{cy + 4.5:.1f}">{escape(text)}</text>')
    return out


def vendor_champions(entries: list[Entry], snapshot_date: str, n: int = 10) -> str:
    """Two-panel horizontal bar chart: best model per vendor on Track A and Track B."""
    w, h = 1200, 675
    pad, gap = 48, 56
    panel_w = (w - 2 * pad - gap) / 2
    gi = _vendor_champions(entries, "gi", n)
    nl = _vendor_champions(entries, "nl", n)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="BenchMaxx vendor champions">',
           f"<style>{BAR_STYLE}</style>",
           f'<rect class="bg" width="{w}" height="{h}"/>',
           f'<text class="title" x="{pad}" y="56">BenchMaxx · Vendor Champions</text>',
           f'<text class="subtitle" x="{pad}" y="82">Best model per vendor among {len(entries)} callable OpenRouter text models · snapshot {escape(snapshot_date)} · protocol v1.0</text>',
           f'<line class="rule" x1="{pad}" x2="{w - pad}" y1="102" y2="102"/>']
    panels = [
        (pad, "Track A · Generation Index (GI) ↑", "The generation number in the name", gi, "bar-a",
         lambda e: (e.canonical_name, e.vendor, e.gi, e.gi_raw)),
        (pad + panel_w + gap, "Track B · Nomenclature Length (NL) ↑", "Characters in the name", nl, "bar-b",
         lambda e: (e.canonical_name, e.vendor, e.nl, str(e.nl))),
    ]
    for x, title, note, items, css, row in panels:
        out.append(f'<text class="panel" x="{x}" y="134">{escape(title)}</text>')
        out.append(f'<text class="panel-note" x="{x}" y="152">{escape(note)}</text>')
        out += _bar_panel(x, 166, panel_w, [row(e) for e in items], css)
    out.append(f'<text class="footer" x="{pad}" y="{h - 22}">Recreational benchmark. Says nothing about model quality.</text>')
    out.append(f'<text class="footer" x="{w - pad}" y="{h - 22}" text-anchor="end">github.com/shuiyue-cmyk/benchmaxx</text>')
    out.append("</svg>")
    return "\n".join(out)


FULL_STYLE = BAR_STYLE + """
  .rank { font: 600 11.5px ui-monospace, 'Cascadia Mono', Consolas, monospace; fill: #818b98; }
  .row-name { font: 500 12px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: #1f2328; }
  .row-vendor { font: 11px system-ui, -apple-system, 'Segoe UI', sans-serif; fill: #818b98; }
  .row-value { font: 600 11.5px ui-monospace, 'Cascadia Mono', Consolas, monospace; fill: #1f2328; }
  .zebra { fill: #f6f8fa; }
  .break { stroke: #ffffff; stroke-width: 3; }
  @media (prefers-color-scheme: dark) {
    .row-name, .row-value { fill: #e6edf3; }
    .zebra { fill: #151b23; }
    .break { stroke: #0d1117; }
  }
"""


def full_ranking(entries: list[Entry], metric: str, snapshot_date: str) -> str:
    """One horizontal bar per model, in rank order, for Track A ("gi") or Track B ("nl")."""
    is_gi = metric == "gi"
    rank_field = "rank_gi" if is_gi else "rank_nl"
    items = sorted((e for e in entries if getattr(e, metric) is not None),
                   key=lambda e: (getattr(e, rank_field), e.canonical_name.lower()))
    w, pad, head, row_h, bar_h = 1000, 40, 132, 20, 12
    rank_w, label_w, value_w = 44, 330, 60
    h = head + len(items) * row_h + 56
    bar_x = pad + rank_w + label_w
    bar_max = w - pad - value_w - bar_x
    values = [getattr(e, metric) for e in items]
    ceiling = _y_ceiling(values) if is_gi else max(values)
    css = "bar-a" if is_gi else "bar-b"
    title = ("Track A · Generation Index (GI): all models" if is_gi
             else "Track B · Nomenclature Length (NL): all models")
    note = (f"{len(items)} GI-qualified models · snapshot {snapshot_date} · protocol v1.0 · ties share a rank"
            if is_gi else f"{len(items)} evaluated models · snapshot {snapshot_date} · protocol v1.0 · ties share a rank")
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{escape(title)}">',
           f"<style>{FULL_STYLE}</style>",
           f'<rect class="bg" width="{w}" height="{h}"/>',
           f'<text class="title" x="{pad}" y="52">BenchMaxx · {escape(title)}</text>',
           f'<text class="subtitle" x="{pad}" y="80">{escape(note)}</text>',
           f'<line class="rule" x1="{pad}" x2="{w - pad}" y1="100" y2="100"/>']
    previous_rank = None
    for i, e in enumerate(items):
        y = head + i * row_h
        cy = y + row_h / 2
        if i % 2:
            out.append(f'<rect class="zebra" x="{pad}" y="{y}" width="{w - 2 * pad}" height="{row_h}"/>')
        rank = getattr(e, rank_field)
        if rank != previous_rank:  # show each rank once; tied rows below it stay blank
            out.append(f'<text class="rank" x="{pad + rank_w - 10}" y="{cy + 4}" text-anchor="end">{rank}</text>')
            previous_rank = rank
        out.append(f'<text x="{bar_x - 10}" y="{cy + 4}" text-anchor="end"><tspan class="row-name">{escape(e.canonical_name)}</tspan>'
                   f'<tspan class="row-vendor" dx="6">{escape(e.vendor)}</tspan></text>')
        value = getattr(e, metric)
        clipped = value > ceiling
        bw = bar_max if clipped else max(1.5, value / ceiling * bar_max * 0.92)
        out.append(f'<rect class="{css}" x="{bar_x}" y="{cy - bar_h / 2}" width="{bw:.1f}" height="{bar_h}" rx="2" fill-opacity="{1 if i == 0 else 0.75}"/>')
        if clipped:  # axis break: this bar is not to scale
            bx = bar_x + bar_max * 0.8
            for dx in (0, 6):
                out.append(f'<line class="break" x1="{bx + dx - 3:.1f}" y1="{cy + bar_h / 2 + 1}" x2="{bx + dx + 3:.1f}" y2="{cy - bar_h / 2 - 1}"/>')
        text = e.gi_raw if is_gi else str(e.nl)
        out.append(f'<text class="row-value" x="{bar_x + bw + 6:.1f}" y="{cy + 4}">{escape(text)}</text>')
    if is_gi and any(v > ceiling for v in values):
        foot = "Bars marked // are truncated and not drawn to scale."
    else:
        foot = "Recreational benchmark. Says nothing about model quality."
    out.append(f'<text class="footer" x="{pad}" y="{h - 22}">{escape(foot)}</text>')
    out.append(f'<text class="footer" x="{w - pad}" y="{h - 22}" text-anchor="end">github.com/shuiyue-cmyk/benchmaxx</text>')
    out.append("</svg>")
    return "\n".join(out)
