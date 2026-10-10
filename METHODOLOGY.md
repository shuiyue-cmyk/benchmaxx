# BenchMaxx Evaluation Protocol

**Protocol version 1.0** · Status: Stable

This document is the normative specification of the BenchMaxx benchmark. The reference
implementation in [`benchmaxx/`](benchmaxx/) and the conformance tests in [`tests/`](tests/)
follow it. Where the two disagree, this document wins and the disagreement is a bug.

The key words MUST, MUST NOT, SHOULD and MAY are used as described in RFC 2119.

---

## 1. Scope and Motivation

Mainstream LLM benchmarks measure what a model *does*. This is expensive, easy to contaminate
and hard to reproduce. BenchMaxx measures what a model *is called*. That property is cheap to
observe, needs no inference and cannot be gamed by training on the test set. It can be gamed by
marketing, and §8.2 discusses that.

BenchMaxx has two primary tracks:

| Track | Metric | Symbol | Direction |
| :-- | :-- | :-- | :-: |
| A | Generation Index | GI | higher is better |
| B | Nomenclature Length | NL | higher is better |

One auxiliary metric is derived from them: **Nomenclatural Efficiency** (NE = GI / NL).

## 2. Population

### 2.1 Data source

The population MUST be drawn from the public OpenRouter model catalogue
(`GET https://openrouter.ai/api/v1/models`). No API key is required. Each evaluation run MUST
archive the raw API response as a snapshot under `data/snapshots/YYYY-MM-DD.json` (UTC date of
retrieval), so that any published result can be recomputed exactly.

### 2.2 Exclusion criteria

A catalogue entry is excluded if any of these holds, checked in order:

| # | Criterion | Rationale |
| :-: | :-- | :-- |
| E1 | Slug begins with `~` | A moving alias (e.g. `~openai/gpt-latest`), not a model |
| E2 | Author segment is `openrouter` | A platform router (Auto Router, Fusion, …) |
| E3 | `pricing.prompt == "-1"` | Variable pricing, which marks a third-party meta-router |
| E4 | `architecture.output_modalities ≠ ["text"]` | Not a text model (image, audio or mixed output) |

### 2.3 Variant collapsing

OpenRouter exposes routing variants of one model under suffixed slugs (`:free`, `:batch`, …).
All slugs that share a base slug (the part before `:`) MUST be collapsed into one *model*.
Metadata comes from the base slug when it is listed, and otherwise from the first listed variant.

### 2.4 Callability verification

A model is *callable* if at least one of its slugs has at least one provider endpoint at
`GET /api/v1/models/{slug}/endpoints` at retrieval time. Models that fail this check MUST be
reported in the census and MUST NOT be scored. Implementations MAY skip the check
(`--skip-endpoint-check`). Results produced that way MUST be marked
`callability_verified: false`.

## 3. Canonical Name

Both metrics are computed on a model's **canonical name**, derived from the catalogue
`name` field as follows:

1. **Vendor prefix removal.** If the name contains `": "`, everything up to and including the
   first occurrence is removed. (`"OpenAI: GPT-5.5"` → `"GPT-5.5"`)
2. **Variant tag removal.** If the slug has a variant suffix `:tag`, a trailing `"(tag)"`
   (case-insensitive) is removed. (`"Gemma 4 31B (free)"` → `"Gemma 4 31B"`)
3. **Whitespace normalisation.** Runs of whitespace collapse to one space, and leading and
   trailing whitespace is stripped.

Any other parenthetical content is part of the name. For example, `"Weaver (alpha)"` and
`"GPT-4o (2024-11-20)"` keep their parentheses.

## 4. Track A: Generation Index (GI)

### 4.1 Definition

The Generation Index is the numeric value of the **first generation-bearing number** in the
canonical name. Informally, it is the "version number" that the vendor put in the name.

### 4.2 Extraction procedure

Given a canonical name *N*:

1. **Strip parentheticals.** Remove every `(...)` group.
2. **Strip calendar dates.** Remove standalone tokens of the form `YYYY-MM-DD`, `MM-DD` or
   `MM-YYYY`.
3. **Strip MoE shorthand.** Remove tokens of the form `<int>x<int>[letter]` (e.g. `8x22B`).
4. **Scan numeric tokens** left to right. A numeric token is a maximal run `\d+(\.\d+)*`, along
   with any letters directly before it (*prefix*) and directly after it (*suffix*). Discard the
   token if:
   - **(Magnitude rule)** its suffix is exactly one of `B`, `M`, `T`, `K` (case-insensitive).
     These are parameter counts (`27B`, `A3B`, `2.4T`) or context sizes (`16k`), or
   - **(Snapshot rule)** it has no decimal point and four or more digits. These are build
     stamps such as `2507`, `0905` or `2512`.
5. The first token that is not discarded is the generation. Prefixes and other suffixes do
   not disqualify a token, so `Qwen3.8`, `K2.6`, `V2.6`, `o3`, `Mk1.5`, `4o` and `5V` all count.
6. If no token survives, the model **Did Not Qualify (DNQ)** for Track A. It is still scored on
   Track B.

### 4.3 Decimal Interpretation Principle (DIP)

The raw token is read as a **decimal number**, using only its first two dot-separated
components: `"4.20"` → 4.2, `"26.10"` → 26.1, `"01"` → 1.0.

The DIP was chosen over semantic-version ordering on purpose. The task is to measure the
*magnitude of the number in the name*, not the vendor's intended release order. As a result,
`Grok 4.20` (GI 4.2) ranks below `Grok 4.3` (GI 4.3). The raw string is always reported next to
the value.

### 4.4 Worked examples

| Canonical name | Discarded tokens | GI (raw) | GI |
| :-- | :-- | :-: | :-: |
| `Qwen3.8 2.4T A95B` | `2.4T`, `A95B` (magnitude) | `3.8` | 3.8 |
| `Kimi K2 0905` | `0905` (snapshot) | `2` | 2.0 |
| `Cydonia 24B V4.1` | `24B` (magnitude) | `4.1` | 4.1 |
| `GPT-4o (2024-11-20)` | parenthetical | `4` | 4.0 |
| `WizardLM-2 8x22B` | `8x22B` (MoE) | `2` | 2.0 |
| `Grok 4.20 Multi-Agent` | none | `4.20` | 4.2 |
| `gpt-oss-120b` | `120b` (magnitude) | none | DNQ |
| `Mistral Large 2407` | `2407` (snapshot) | none | DNQ |

## 5. Track B: Nomenclature Length (NL)

**NL** is the number of Unicode code points in the canonical name (§3). Spaces, hyphens,
dots and parentheses all count. No unit conversion is applied.

## 6. Auxiliary Metrics

| Metric | Definition | Interpretation |
| :-- | :-- | :-- |
| **Nomenclatural Efficiency (NE)** | GI / NL, to 4 decimal places | Generations delivered per character of name |
| **Generational Velocity** | OLS slope of GI against listing date (fractional years). Computed industry-wide and per vendor (≥ 3 models, needs date variance) | How fast a vendor's version numbers inflate, in generations per year |
| **GI Coverage** | Share of a vendor's models that are GI-qualified | How committed a vendor is to numbering |

The listing date is the catalogue `created` timestamp, converted to a UTC date. It records
when the model first appeared on OpenRouter, which can differ from its actual release.

## 7. Ranking

All tracks use **standard competition ranking** ("1224"): entries with equal scores share a
rank, and the next rank skips accordingly. Models without a score for a track are unranked on
that track. For display only, ties are ordered alphabetically by canonical name.

## 8. Threats to Validity

### 8.1 Construct validity

GI measures the number a vendor wrote down, not any capability. Vendors number things on
different scales. `GPT-6`, `Kimi K3` and `Pareto 26.10` are not on a common scale, and
BenchMaxx deliberately makes no attempt to align them.

### 8.2 Goodhart's Law

A vendor can raise its GI by renaming a model. Calendar versioning (`YY.MM`) currently gives a
large advantage. BenchMaxx treats this as a *finding*, not a flaw.

### 8.3 Display-name drift

OpenRouter display names are curated and can change between snapshots, which changes NL. All
published results are tied to an archived snapshot for this reason.

### 8.4 Parser coverage

The extraction rules are heuristic. They are validated against every name in the reference
snapshot and pinned by conformance tests. New naming conventions may need a protocol revision.

## 9. Versioning

Any change to §2–§7 that can change a published score MUST increment the protocol version.
Results from different protocol versions MUST NOT be compared on the same leaderboard.

## 10. Reproducibility Checklist

- [x] Public data source, no credentials required
- [x] Raw snapshot archived per run
- [x] Deterministic scoring (no sampling, no inference, no LLM-as-judge)
- [x] Zero third-party dependencies (Python ≥ 3.10 standard library only)
- [x] Conformance test suite
- [x] Continuous integration: conformance tests plus re-scoring of the latest archived snapshot
