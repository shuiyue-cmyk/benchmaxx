"""Nomenclature analysis: canonical names and Generation Index extraction.

All rules here are specified normatively in METHODOLOGY.md (sections 3 and 4).
Any change to this module is a change to the benchmark and must bump the
protocol version in ``benchmaxx/__init__.py``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# Parenthetical qualifiers, e.g. "(2024-11-20)", "(8B)", "(Gemini 3.1 Flash Image)".
_PARENTHETICAL = re.compile(r"\s*\([^)]*\)")

# Calendar dates: 2026-04-20, 06-05, 12-2024.
_DATE = re.compile(r"(?<![\w.])(?:\d{4}-\d{2}-\d{2}|\d{2}-\d{2}(?:\d{2})?)(?![\w.])")

# Mixture-of-experts shorthand: 8x22B, 8x7b.
_MOE = re.compile(r"\d+x\d+[A-Za-z]?")

# A numeric token together with the letters glued to either side of it.
_TOKEN = re.compile(r"(?P<pre>[A-Za-z]*)(?P<num>\d+(?:\.\d+)*)(?P<post>[A-Za-z]*)")

# Single-letter magnitude suffixes: parameter counts (7B, 2.4T, 500M) and context sizes (16k).
_MAGNITUDE_SUFFIXES = {"b", "m", "t", "k"}


@dataclass(frozen=True)
class Generation:
    raw: str      # exactly as written in the name, e.g. "4.20"
    value: float  # Decimal Interpretation Principle: "4.20" -> 4.2


def split_display_name(display_name: str, model_id: str) -> tuple[str | None, str]:
    """Split an OpenRouter display name into (vendor label, canonical model name).

    The canonical name drops the ``"Vendor: "`` prefix and any trailing routing-variant
    tag that mirrors the slug suffix (``:free`` -> ``(free)``), then normalises whitespace.
    """
    vendor, sep, rest = display_name.partition(": ")
    if not sep:
        vendor, rest = None, display_name
    variant = model_id.partition(":")[2]
    if variant:
        rest = re.sub(rf"\s*\({re.escape(variant)}\)\s*$", "", rest, flags=re.IGNORECASE)
    return vendor, " ".join(rest.split())


def extract_generation(canonical_name: str) -> Generation | None:
    """Return the first generation-bearing number in a canonical name, or None (DNQ)."""
    text = _PARENTHETICAL.sub(" ", canonical_name)
    text = _DATE.sub(" ", text)
    text = _MOE.sub(" ", text)
    for match in _TOKEN.finditer(text):
        num, post = match["num"], match["post"]
        if post.lower() in _MAGNITUDE_SUFFIXES:
            continue  # parameter count or context window, not a generation
        if "." not in num and len(num) >= 4:
            continue  # snapshot stamp such as 2507 or 0905
        major, _, rest = num.partition(".")
        minor = rest.split(".")[0]
        return Generation(raw=num, value=float(f"{major}.{minor}" if minor else major))
    return None


def nomenclature_length(canonical_name: str) -> int:
    """Nomenclature Length: number of Unicode code points in the canonical name."""
    return len(canonical_name)
