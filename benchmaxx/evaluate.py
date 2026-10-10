"""Population selection, scoring and aggregation (METHODOLOGY.md sections 2, 5 and 6)."""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from statistics import mean, median

from .nomenclature import extract_generation, nomenclature_length, split_display_name


@dataclass
class Entry:
    model_id: str
    display_name: str
    canonical_name: str
    vendor: str
    vendor_slug: str
    released: str            # ISO date of first listing on OpenRouter
    slugs: list[str]         # base slug plus routing variants (:free, :batch, ...)
    endpoints: int | None    # live provider endpoints across all slugs; None = not checked
    gi_raw: str | None
    gi: float | None
    nl: int
    ne: float | None         # Nomenclatural Efficiency = GI / NL
    rank_gi: int | None = None
    rank_nl: int | None = None
    rank_ne: int | None = None

    def as_dict(self) -> dict:
        return asdict(self)


def exclusion_reason(model: dict) -> str | None:
    """Return why a catalogue entry is outside the evaluated population, or None."""
    model_id = model["id"]
    if model_id.startswith("~"):
        return "alias"
    if model_id.split("/")[0] == "openrouter":
        return "platform router"
    if str(model.get("pricing", {}).get("prompt")) == "-1":
        return "meta-router (variable pricing)"
    if model.get("architecture", {}).get("output_modalities") != ["text"]:
        return "non-text output"
    return None


def candidate_slugs(models: list[dict]) -> list[str]:
    return [m["id"] for m in models if exclusion_reason(m) is None]


def build_population(models: list[dict], endpoint_counts: dict[str, int] | None) -> tuple[list[Entry], dict]:
    """Collapse routing variants, verify callability and score every model."""
    groups: dict[str, list[dict]] = {}
    excluded: dict[str, int] = {}
    for model in models:
        reason = exclusion_reason(model)
        if reason:
            excluded[reason] = excluded.get(reason, 0) + 1
            continue
        groups.setdefault(model["id"].partition(":")[0], []).append(model)

    entries: list[Entry] = []
    uncallable: list[str] = []
    for base_id, variants in groups.items():
        # Prefer the base slug's metadata; fall back to the first variant listed.
        primary = next((m for m in variants if m["id"] == base_id), variants[0])
        slugs = sorted(m["id"] for m in variants)
        endpoints = None
        if endpoint_counts is not None:
            endpoints = sum(endpoint_counts.get(s, 0) for s in slugs)
            if endpoints == 0:
                uncallable.append(base_id)
                continue
        vendor_label, canonical = split_display_name(primary["name"], primary["id"])
        vendor_slug = base_id.split("/")[0]
        generation = extract_generation(canonical)
        nl = nomenclature_length(canonical)
        entries.append(Entry(
            model_id=base_id,
            display_name=primary["name"],
            canonical_name=canonical,
            vendor=vendor_label or vendor_slug,
            vendor_slug=vendor_slug,
            released=datetime.fromtimestamp(primary["created"], timezone.utc).date().isoformat(),
            slugs=slugs,
            endpoints=endpoints,
            gi_raw=generation.raw if generation else None,
            gi=generation.value if generation else None,
            nl=nl,
            ne=round(generation.value / nl, 4) if generation else None,
        ))

    _normalise_vendor_labels(entries)
    _assign_ranks(entries, "gi", "rank_gi")
    _assign_ranks(entries, "nl", "rank_nl")
    _assign_ranks(entries, "ne", "rank_ne")
    entries.sort(key=lambda e: (e.rank_gi is None, e.rank_gi or 0, -e.nl, e.model_id))

    census = {
        "catalogue_size": len(models),
        "excluded": dict(sorted(excluded.items())),
        "eligible_models": len(groups),
        "uncallable": sorted(uncallable),
        "evaluated_models": len(entries),
        "gi_qualified": sum(e.gi is not None for e in entries),
        "dnq": sum(e.gi is None for e in entries),
    }
    return entries, census


def _normalise_vendor_labels(entries: list[Entry]) -> None:
    """Give every model of a vendor slug the label that vendor uses most often.

    Display names without a "Vendor: " prefix otherwise fall back to the raw slug.
    """
    votes: dict[str, Counter] = {}
    for entry in entries:
        if entry.vendor != entry.vendor_slug:
            votes.setdefault(entry.vendor_slug, Counter())[entry.vendor] += 1
    for entry in entries:
        if entry.vendor_slug in votes:
            entry.vendor = votes[entry.vendor_slug].most_common(1)[0][0]


def _assign_ranks(entries: list[Entry], metric: str, rank_field: str) -> None:
    """Standard competition ranking ("1224"), higher metric value ranks first."""
    scored = sorted((e for e in entries if getattr(e, metric) is not None),
                    key=lambda e: getattr(e, metric), reverse=True)
    previous, rank = None, 0
    for position, entry in enumerate(scored, start=1):
        value = getattr(entry, metric)
        if value != previous:
            rank, previous = position, value
        setattr(entry, rank_field, rank)


def _year_fraction(iso_date: str) -> float:
    d = datetime.fromisoformat(iso_date)
    start = datetime(d.year, 1, 1)
    return d.year + (d - start).days / (datetime(d.year + 1, 1, 1) - start).days


def _ols_slope(points: list[tuple[float, float]]) -> float | None:
    if len(points) < 3:
        return None
    mx = mean(p[0] for p in points)
    my = mean(p[1] for p in points)
    sxx = sum((x - mx) ** 2 for x, _ in points)
    if sxx == 0:
        return None
    return sum((x - mx) * (y - my) for x, y in points) / sxx


def generational_velocity(entries: list[Entry]) -> float | None:
    """OLS slope of GI against release date, in generations per year."""
    return _ols_slope([(_year_fraction(e.released), e.gi) for e in entries if e.gi is not None])


def vendor_table(entries: list[Entry], min_models: int = 3) -> list[dict]:
    by_vendor: dict[str, list[Entry]] = {}
    for entry in entries:
        by_vendor.setdefault(entry.vendor, []).append(entry)
    rows = []
    for vendor, items in by_vendor.items():
        if len(items) < min_models:
            continue
        gis = [e.gi for e in items if e.gi is not None]
        velocity = generational_velocity(items)
        rows.append({
            "vendor": vendor,
            "vendor_slugs": sorted({e.vendor_slug for e in items}),
            "models": len(items),
            "gi_coverage": round(len(gis) / len(items), 3),
            "gi_max": max(gis) if gis else None,
            "gi_median": median(gis) if gis else None,
            "nl_mean": round(mean(e.nl for e in items), 2),
            "velocity": round(velocity, 3) if velocity is not None else None,
        })
    rows.sort(key=lambda r: (r["gi_max"] is None, -(r["gi_max"] or 0), -r["models"]))
    return rows


def summary_statistics(entries: list[Entry]) -> dict:
    gis = [e.gi for e in entries if e.gi is not None]
    nls = [e.nl for e in entries]
    velocity = generational_velocity(entries)
    return {
        "gi_mean": round(mean(gis), 3),
        "gi_median": median(gis),
        "nl_mean": round(mean(nls), 2),
        "nl_median": median(nls),
        "velocity": round(velocity, 3) if velocity is not None else None,
    }
