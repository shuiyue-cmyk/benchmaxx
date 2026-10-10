"""Data acquisition from the public OpenRouter API (no API key required)."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

API_BASE = "https://openrouter.ai/api/v1"
USER_AGENT = "BenchMaxx/1.0"


def _get_json(url: str, retries: int = 4) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError) as exc:
            # 404 means the model has no endpoint page; retrying will not help.
            if isinstance(exc, urllib.error.HTTPError) and exc.code == 404:
                raise
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


def fetch_models() -> list[dict]:
    """Return the full public model catalogue."""
    return _get_json(f"{API_BASE}/models")["data"]


def fetch_endpoint_counts(model_ids: list[str], workers: int = 8) -> dict[str, int]:
    """Return, for each model slug, the number of provider endpoints currently serving it."""

    def count(model_id: str) -> tuple[str, int]:
        try:
            data = _get_json(f"{API_BASE}/models/{urllib.parse.quote(model_id, safe='/:')}/endpoints")
        except urllib.error.HTTPError:
            return model_id, 0
        return model_id, len((data.get("data") or {}).get("endpoints") or [])

    with ThreadPoolExecutor(max_workers=workers) as pool:
        return dict(pool.map(count, model_ids))
