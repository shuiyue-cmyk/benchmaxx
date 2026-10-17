<div align="center">

# BenchMaxx

**A Nomenclature-Centric Evaluation of Large Language Models**

*Measuring what models are called, not what they can do.*

[English](README.md) · [简体中文](README.zh-CN.md)

[![Conformance tests](https://github.com/shuiyue-cmyk/benchmaxx/actions/workflows/tests.yml/badge.svg)](https://github.com/shuiyue-cmyk/benchmaxx/actions/workflows/tests.yml)
![Protocol](https://img.shields.io/badge/protocol-v1.0-blue)
![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)
![Contamination](https://img.shields.io/badge/data%20contamination-impossible-success)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

</div>

> [!NOTE]
> BenchMaxx is a recreational benchmark. Its results say nothing about model quality. Its
> methodology is nonetheless taken completely seriously.

## Abstract

Modern LLM evaluation is held back by data contamination, saturation, high inference cost and
poor reproducibility. We propose **BenchMaxx**, a benchmark that avoids all four by never
running the models it evaluates. Instead, BenchMaxx scores every callable text model on
[OpenRouter](https://openrouter.ai) along two orthogonal axes of *nomenclatural capability*:

- **Track A, Generation Index (GI):** the size of the generation number in the model's name
  (`GPT-6.1` → 6.1, `Qwen3.8` → 3.8, `Kimi K3` → 3).
- **Track B, Nomenclature Length (NL):** the number of characters in the model's name.

Scoring is deterministic, needs no API key, costs no tokens and finishes in under a minute. The
leaderboard below is regenerated on each evaluation run, and every run is archived as a snapshot.

## Leaderboard

<!-- BENCHMAXX:BEGIN -->
**Snapshot: 2026-10-17** · **340** callable text models evaluated (296 GI-qualified) · Industry Generational Velocity **+0.45 generations/year**

#### Track A: Generation Index (GI), Top 10

| Rank | Model | Vendor | GI | NL |
| --: | :-- | :-- | --: | --: |
| 🥇 1 | Pareto 26.9 | unbiased | `26.9` | 11 |
| 🥈 2 | GPT-6.1 Sol | OpenAI | `6.1` | 11 |
| 🥈 2 | GPT-6.1 Sol Pro | OpenAI | `6.1` | 15 |
| 4 | GPT-6 Astra | OpenAI | `6` | 11 |
| 4 | GPT-6 Astra Pro | OpenAI | `6` | 15 |
| 4 | GPT-6 Luna | OpenAI | `6` | 10 |
| 4 | GPT-6 Luna Pro | OpenAI | `6` | 14 |
| 4 | GPT-6 Sol | OpenAI | `6` | 9 |
| 4 | GPT-6 Sol Pro | OpenAI | `6` | 13 |
| 10 | GPT-5.6 Luna | OpenAI | `5.6` | 12 |
| 10 | GPT-5.6 Luna Pro | OpenAI | `5.6` | 16 |
| 10 | GPT-5.6 Sol | OpenAI | `5.6` | 11 |
| 10 | GPT-5.6 Sol Pro | OpenAI | `5.6` | 15 |
| 10 | GPT-5.6 Terra | OpenAI | `5.6` | 13 |
| 10 | GPT-5.6 Terra Pro | OpenAI | `5.6` | 17 |

#### Track B: Nomenclature Length (NL), Top 10

| Rank | Model | Vendor | NL | GI |
| --: | :-- | :-- | --: | --: |
| 🥇 1 | Gemini 3.1 Pro Preview Custom Tools | Google | 35 | `3.1` |
| 🥈 2 | Gemini 3.1 Flash Lite Preview | Google | 29 | `3.1` |
| 🥈 2 | Qwen3 235B A22B Instruct 2507 | Qwen | 29 | `3` |
| 🥈 2 | Qwen3 235B A22B Thinking 2507 | Qwen | 29 | `3` |
| 5 | DeepSeek V4 Flash Vision Exp | DeepSeek | 28 | `4` |
| 5 | Gemini 2.5 Pro Preview 06-05 | Google | 28 | `2.5` |
| 5 | Qwen3 Coder 30B A3B Instruct | Qwen | 28 | `3` |
| 8 | GPT-3.5 Turbo (older v0613) | OpenAI | 27 | `3.5` |
| 8 | Nemotron 3.5 Content Safety | NVIDIA | 27 | `3.5` |
| 8 | Qwen3 30B A3B Instruct 2507 | Qwen | 27 | `3` |
| 8 | Qwen3 Next 80B A3B Instruct | Qwen | 27 | `3` |
| 8 | Qwen3 Next 80B A3B Thinking | Qwen | 27 | `3` |
| 8 | Qwen3 VL 235B A22B Instruct | Qwen | 27 | `3` |

Complete rankings of all models: [`results/LEADERBOARD.md`](results/LEADERBOARD.md)
<!-- BENCHMAXX:END -->

<p align="center">
  <img src="results/figures/vendor_champions.svg" alt="Vendor champions on Track A and Track B" width="100%">
</p>

<p align="center">
  <img src="results/figures/gi_over_time.svg" alt="Figure 1: Generation Index by release date" width="49%">
  <img src="results/figures/gi_vs_nl.svg" alt="Figure 2: Generation Index vs. Nomenclature Length" width="49%">
</p>

## Key Findings (inaugural run, 2026-10-10)

1. **Calendar versioning wins.** *Pareto 26.10 Preview* takes Track A with a GI of 26.1, about
   **4.3×** the runner-up (*GPT-6.1 Sol*, GI 6.1). It gets there by naming itself after the year
   and month. We see this as a textbook case of Goodhart's Law
   ([METHODOLOGY §8.2](METHODOLOGY.md#82-goodharts-law)).
2. **Preview Custom Tools.** *Gemini 3.1 Pro Preview Custom Tools* wins Track B with **35
   characters**, ahead of a three-way tie at 29 characters.
3. **Two characters suffice.** *o3* has the highest Nomenclatural Efficiency of any model
   (NE = 1.50): three generations in two characters.
4. **Generational inflation is real.** Across the industry, version numbers rise by
   **+0.45 generations per year**. StepFun (+2.20/yr) and SpaceXAI (+2.16/yr) inflate fastest.
5. **Generational regression is also real.** Meta (−1.13/yr) and Tencent (−1.29/yr) have
   *negative* velocity. Meta moved from *Llama 4* to *Muse Spark 1.x*.
6. **The decimal trap.** Under the Decimal Interpretation Principle, *Grok 4.20* (GI 4.2) ranks
   below its predecessor *Grok 4.3*.
7. **Conscientious objectors.** 40 of 332 models (12%) carry no generation number. Cohere and
   Perplexity have 0% GI coverage.

## Update: 2026-10-17

1. **The decimal trap, reversed.** *Pareto 26.10 Preview* was delisted and replaced by
   *Pareto 26.9*. Under the Decimal Interpretation Principle, going from 26.10 to 26.9 is an
   *upgrade*: GI rises from 26.1 to 26.9 and the vendor keeps Track A. The new lead is
   **4.4×** the runner-up (*GPT-6.1 Sol*, GI 6.1).
2. **Brevity pays twice.** Dropping "Preview" cut the name from 20 to 11 characters. With it,
   *Pareto 26.9* takes the Nomenclatural Efficiency crown from *o3* (NE **2.45** vs. 1.50).
3. **Google reaches generation 4.** *Gemini 4 Argon* is Google's first model with a GI of 4.
4. **Meta stops numbering.** *Muse Spark Open* and *Muse Wonder* arrived with no generation
   number. Meta's GI coverage fell to 81%, and its velocity stays at −1.13 generations/year.
5. **Population:** 340 callable models (+14 new, −6 delisted, including *Claude Sonnet 4*).
   All 14 new names parsed under protocol v1.0 without any rule changes.

## Methodology at a Glance

```
OpenRouter /models ──► exclude aliases, routers,      ──► collapse :free / :batch ──► verify ≥1 live
   (458 slugs)          non-text output (−40)               variants (332 models)       endpoint
                                                                                            │
                     ┌──────────────────────────────────────────────────────────────────────┘
                     ▼
     canonical name  "OpenAI: GPT-5.6 Terra Pro (batch)"  ──►  "GPT-5.6 Terra Pro"
                     │
          ┌──────────┴───────────┐
          ▼                      ▼
   GI = 5.6 (first number,   NL = 17 (code points)
   skipping 27B / 2507 /
   dates / 8x22B)
```

The full normative specification, including exclusion criteria, extraction rules, worked
examples, ranking and threats to validity, is in **[METHODOLOGY.md](METHODOLOGY.md)**.

## Reproducing the Results

You need Python 3.10 or newer. There are no dependencies to install.

```bash
git clone https://github.com/shuiyue-cmyk/benchmaxx.git
```

```bash
python -m benchmaxx
```

This fetches a fresh snapshot, verifies callability, and writes:

| Path | Contents |
| :-- | :-- |
| `data/snapshots/YYYY-MM-DD.json` | Raw API snapshot plus endpoint counts (the reproducibility anchor) |
| `results/LEADERBOARD.md` | Full leaderboards for all tracks, vendor analysis and DNQ list |
| `results/latest.csv` / `latest.json` | Per-model scores and ranks |
| `results/figures/*.svg` | Figures (adapt to light/dark mode) |

To re-score an archived snapshot exactly:

```bash
python -m benchmaxx --snapshot data/snapshots/2026-10-10.json
```

To run the conformance tests:

```bash
python -m unittest discover -s tests -t .
```

## FAQ

**Is a higher GI better?**
By the definition of this benchmark, yes. By any other definition, no.

**My favourite model has no number in its name.**
It is listed as *Did Not Qualify* for Track A and still competes on Track B. We respect its choice.

**Why is `Grok 4.20` scored 4.2?**
See the Decimal Interpretation Principle, [METHODOLOGY §4.3](METHODOLOGY.md#43-decimal-interpretation-principle-dip).

**Can a vendor game this benchmark?**
Yes, by renaming. Unlike other benchmarks, we document this openly.

**Will you add Track C: Hyphen Density?**
Proposals are welcome as issues. Protocol changes increment the protocol version.

## Citation

```bibtex
@misc{benchmaxx2026,
  title        = {BenchMaxx: A Nomenclature-Centric Evaluation of Large Language Models},
  author       = {{BenchMaxx Contributors}},
  year         = {2026},
  howpublished = {\url{https://github.com/shuiyue-cmyk/benchmaxx}},
  note         = {Protocol v1.0}
}
```

## License

[MIT](LICENSE). Model names and metadata belong to their respective owners and are retrieved
from the public OpenRouter API. BenchMaxx is not affiliated with OpenRouter or any model vendor.
