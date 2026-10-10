"""Result serialisation: JSON, CSV, Markdown leaderboards and README summaries."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

from . import PROTOCOL_VERSION, __version__
from .evaluate import Entry

BEGIN, END = "<!-- BENCHMAXX:BEGIN -->", "<!-- BENCHMAXX:END -->"
MEDALS = {1: "🥇 1", 2: "🥈 2", 3: "🥉 3"}

CSV_FIELDS = ["rank_gi", "rank_nl", "rank_ne", "model_id", "canonical_name", "vendor", "released",
              "gi_raw", "gi", "nl", "ne", "endpoints", "slugs", "display_name"]


def _rank(rank: int | None) -> str:
    return MEDALS.get(rank, str(rank)) if rank else "—"


def _code(text: str) -> str:
    return f"`{text}`"


def _table(headers: list[str], rows: list[list[str]], align: str) -> str:
    sep = {"l": ":--", "r": "--:", "c": ":-:"}
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(sep[a] for a in align) + " |"]
    lines += ["| " + " | ".join(str(c).replace("|", "\\|") for c in row) + " |" for row in rows]
    return "\n".join(lines)


def _top(entries: list[Entry], key: str, n: int) -> list[Entry]:
    ranked = [e for e in entries if getattr(e, key) is not None and getattr(e, key) <= n]
    return sorted(ranked, key=lambda e: (getattr(e, key), e.canonical_name.lower()))


def _bottom_nl(entries: list[Entry], n: int) -> list[Entry]:
    return sorted(entries, key=lambda e: (e.nl, e.canonical_name.lower()))[:n]


# ---------------------------------------------------------------------------
# Machine-readable outputs


def write_json(path: Path, meta: dict, census: dict, stats: dict, vendors: list[dict], entries: list[Entry]) -> None:
    payload = {"meta": meta, "census": census, "statistics": stats, "vendors": vendors,
               "models": [e.as_dict() for e in entries]}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, entries: list[Entry]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for entry in entries:
            row = entry.as_dict()
            row["slugs"] = " ".join(row["slugs"])
            writer.writerow(row)


# ---------------------------------------------------------------------------
# Full leaderboard (English)


def leaderboard_markdown(meta: dict, census: dict, stats: dict, vendors: list[dict], entries: list[Entry]) -> str:
    gi_rows = [[_rank(e.rank_gi), e.canonical_name, e.vendor, _code(e.gi_raw), str(e.nl), e.released]
               for e in _top(entries, "rank_gi", 25)]
    nl_rows = [[_rank(e.rank_nl), e.canonical_name, e.vendor, str(e.nl), _code(e.gi_raw) if e.gi_raw else "DNQ"]
               for e in _top(entries, "rank_nl", 25)]
    brevity_rows = [[e.canonical_name, e.vendor, str(e.nl)] for e in _bottom_nl(entries, 10)]
    ne_rows = [[_rank(e.rank_ne), e.canonical_name, _code(e.gi_raw), str(e.nl), f"{e.ne:.4f}"]
               for e in _top(entries, "rank_ne", 15)]
    humble = sorted((e for e in entries if e.gi is not None), key=lambda e: (e.gi, e.canonical_name.lower()))[:10]
    humble_rows = [[e.canonical_name, e.vendor, _code(e.gi_raw), e.released] for e in humble]
    vendor_rows = [[v["vendor"], str(v["models"]), f'{v["gi_coverage"]:.0%}',
                    f'{v["gi_max"]:g}' if v["gi_max"] is not None else "—",
                    f'{v["gi_median"]:g}' if v["gi_median"] is not None else "—",
                    f'{v["nl_mean"]:.1f}',
                    f'{v["velocity"]:+.2f}' if v["velocity"] is not None else "—"] for v in vendors]
    dnq = sorted((e for e in entries if e.gi is None), key=lambda e: e.canonical_name.lower())

    return f"""# BenchMaxx Leaderboard

> Snapshot **{meta["snapshot_date"]}** · protocol v{PROTOCOL_VERSION} · BenchMaxx v{__version__} · source: OpenRouter public API

## 0. Census

| Quantity | Value |
| :-- | --: |
| Catalogue entries (all slugs) | {census["catalogue_size"]} |
| Excluded (alias / router / non-text output) | {sum(census["excluded"].values())} |
| Eligible models (after collapsing `:free`, `:batch`, … variants) | {census["eligible_models"]} |
| Failed callability check (0 live endpoints) | {len(census["uncallable"])} |
| **Evaluated models** | **{census["evaluated_models"]}** |
| GI-qualified | {census["gi_qualified"]} |
| Did Not Qualify for GI (no generation number in name) | {census["dnq"]} |

| Statistic | Value |
| :-- | --: |
| Mean GI | {stats["gi_mean"]} |
| Median GI | {stats["gi_median"]:g} |
| Mean NL | {stats["nl_mean"]} |
| Median NL | {stats["nl_median"]:g} |
| Industry Generational Velocity (OLS, GI per year) | {stats["velocity"]:+.3f} |

## 1. Track A: Generation Index (GI) ↑

The largest generation number currently being served. Ties share a rank.

{_table(["Rank", "Model", "Vendor", "GI", "NL", "Listed"], gi_rows, "rllrrl")}

### 1.1 Foundational Humility Award (lowest GI)

{_table(["Model", "Vendor", "GI", "Listed"], humble_rows, "llrl")}

## 2. Track B: Nomenclature Length (NL) ↑

Character count of the canonical model name.

{_table(["Rank", "Model", "Vendor", "NL", "GI"], nl_rows, "rllrr")}

### 2.1 Brevity Prize (shortest names)

{_table(["Model", "Vendor", "NL"], brevity_rows, "llr")}

## 3. Auxiliary Track: Nomenclatural Efficiency (NE = GI / NL) ↑

Generations delivered per character of name.

{_table(["Rank", "Model", "GI", "NL", "NE"], ne_rows, "rlrrr")}

## 4. Vendor Analysis

Vendors with at least 3 evaluated models. *Velocity* is the OLS slope of GI against listing date (generations per year).

{_table(["Vendor", "Models", "GI coverage", "Max GI", "Median GI", "Mean NL", "Velocity"], vendor_rows, "lrrrrrr")}

## 5. Did Not Qualify (DNQ) for Track A

These models are served on OpenRouter but carry no generation number in their name. They are still scored on Track B.

{", ".join(f"{e.canonical_name} (`{e.model_id}`)" for e in dnq)}

## 6. Figures

![Figure 1](figures/gi_over_time.svg)

![Figure 2](figures/gi_vs_nl.svg)

---

Full per-model data: [`latest.csv`](latest.csv) · [`latest.json`](latest.json)
"""


# ---------------------------------------------------------------------------
# README summaries


def _summary(entries: list[Entry], meta: dict, census: dict, stats: dict, lang: str) -> str:
    gi = _top(entries, "rank_gi", 10)
    nl = _top(entries, "rank_nl", 10)
    if lang == "zh":
        head = (f"**快照日期：{meta['snapshot_date']}**　·　共评测 **{census['evaluated_models']}** 个可调用文本模型"
                f"（{census['gi_qualified']} 个具备代际数字）　·　行业代际膨胀速度 **{stats['velocity']:+.2f} 代/年**")
        gi_h = ["名次", "模型", "厂商", "代际指数 GI", "名称长度 NL"]
        nl_h = ["名次", "模型", "厂商", "名称长度 NL", "代际指数 GI"]
        t_gi, t_nl, more = "#### 赛道 A：代际指数（GI）Top 10", "#### 赛道 B：名称长度（NL）Top 10", "完整榜单见"
    else:
        head = (f"**Snapshot: {meta['snapshot_date']}** · **{census['evaluated_models']}** callable text models evaluated "
                f"({census['gi_qualified']} GI-qualified) · Industry Generational Velocity **{stats['velocity']:+.2f} generations/year**")
        gi_h = ["Rank", "Model", "Vendor", "GI", "NL"]
        nl_h = ["Rank", "Model", "Vendor", "NL", "GI"]
        t_gi, t_nl, more = "#### Track A: Generation Index (GI), Top 10", "#### Track B: Nomenclature Length (NL), Top 10", "Full results:"
    gi_rows = [[_rank(e.rank_gi), e.canonical_name, e.vendor, _code(e.gi_raw), str(e.nl)] for e in gi]
    nl_rows = [[_rank(e.rank_nl), e.canonical_name, e.vendor, str(e.nl), _code(e.gi_raw) if e.gi_raw else "DNQ"] for e in nl]
    return "\n\n".join([
        head, t_gi, _table(gi_h, gi_rows, "rllrr"), t_nl, _table(nl_h, nl_rows, "rllrr"),
        f"{more} [`results/LEADERBOARD.md`](results/LEADERBOARD.md)",
    ])


def update_readme(path: Path, entries: list[Entry], meta: dict, census: dict, stats: dict, lang: str) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    block = f"{BEGIN}\n{_summary(entries, meta, census, stats, lang)}\n{END}"
    new = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    path.write_text(new, encoding="utf-8")
    return new != text
