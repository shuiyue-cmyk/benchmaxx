"""Command-line entry point: ``python -m benchmaxx``."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import PROTOCOL_VERSION, __version__, figures, report
from .evaluate import build_population, candidate_slugs, summary_statistics, vendor_table
from .fetch import fetch_endpoint_counts, fetch_models

ROOT = Path(__file__).resolve().parent.parent


def _log(message: str) -> None:
    print(message, file=sys.stderr, flush=True)


def acquire(args: argparse.Namespace) -> dict:
    """Load a snapshot from disk, or fetch a fresh one and archive it."""
    if args.snapshot:
        _log(f"Loading snapshot {args.snapshot}")
        return json.loads(Path(args.snapshot).read_text(encoding="utf-8"))

    retrieved = datetime.now(timezone.utc)
    _log("Fetching model catalogue from OpenRouter ...")
    models = fetch_models()
    endpoint_counts = None
    if not args.skip_endpoint_check:
        slugs = candidate_slugs(models)
        _log(f"Verifying callability of {len(slugs)} slugs ...")
        endpoint_counts = fetch_endpoint_counts(slugs, workers=args.workers)
    snapshot = {
        "retrieved_at": retrieved.isoformat(timespec="seconds"),
        "source": "https://openrouter.ai/api/v1/models",
        "models": models,
        "endpoint_counts": endpoint_counts,
    }
    path = ROOT / "data" / "snapshots" / f"{retrieved.date().isoformat()}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(snapshot, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    _log(f"Snapshot archived to {path.relative_to(ROOT)}")
    return snapshot


def run(args: argparse.Namespace) -> int:
    snapshot = acquire(args)
    entries, census = build_population(snapshot["models"], snapshot.get("endpoint_counts"))
    stats = summary_statistics(entries)
    vendors = vendor_table(entries)
    meta = {
        "benchmaxx_version": __version__,
        "protocol_version": PROTOCOL_VERSION,
        "snapshot_date": snapshot["retrieved_at"][:10],
        "retrieved_at": snapshot["retrieved_at"],
        "callability_verified": snapshot.get("endpoint_counts") is not None,
    }

    out = Path(args.out)
    (out / "figures").mkdir(parents=True, exist_ok=True)
    report.write_json(out / "latest.json", meta, census, stats, vendors, entries)
    report.write_csv(out / "latest.csv", entries)
    (out / "LEADERBOARD.md").write_text(report.leaderboard_markdown(meta, census, stats, vendors, entries), encoding="utf-8")
    (out / "figures" / "gi_over_time.svg").write_text(figures.gi_over_time(entries, stats["velocity"]), encoding="utf-8")
    (out / "figures" / "gi_vs_nl.svg").write_text(figures.gi_vs_nl(entries), encoding="utf-8")
    (out / "figures" / "vendor_champions.svg").write_text(
        figures.vendor_champions(entries, meta["snapshot_date"]), encoding="utf-8")
    if not args.no_readme:
        report.update_readme(ROOT / "README.md", entries, meta, census, stats, "en")
        report.update_readme(ROOT / "README.zh-CN.md", entries, meta, census, stats, "zh")

    champion_gi = min((e for e in entries if e.rank_gi == 1), key=lambda e: e.model_id)
    champion_nl = min((e for e in entries if e.rank_nl == 1), key=lambda e: e.model_id)
    _log(f"Evaluated {census['evaluated_models']} models "
         f"({census['gi_qualified']} GI-qualified, {len(census['uncallable'])} uncallable).")
    _log(f"Track A champion: {champion_gi.canonical_name} (GI {champion_gi.gi_raw})")
    _log(f"Track B champion: {champion_nl.canonical_name} (NL {champion_nl.nl})")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="benchmaxx", description=__doc__)
    parser.add_argument("--version", action="version", version=f"BenchMaxx {__version__} (protocol {PROTOCOL_VERSION})")
    parser.add_argument("--snapshot", help="re-evaluate an archived snapshot instead of fetching live data")
    parser.add_argument("--skip-endpoint-check", action="store_true",
                        help="skip per-model callability verification (faster, less rigorous)")
    parser.add_argument("--workers", type=int, default=8, help="concurrent requests for callability check")
    parser.add_argument("--out", default=str(ROOT / "results"), help="output directory")
    parser.add_argument("--no-readme", action="store_true", help="do not update README leaderboard sections")
    return run(parser.parse_args(argv))
