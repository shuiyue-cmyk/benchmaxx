# BenchMaxx Leaderboard

> Snapshot **2026-10-10** · protocol v1.0 · BenchMaxx v1.0.0 · source: OpenRouter public API

## 0. Census

| Quantity | Value |
| :-- | --: |
| Catalogue entries (all slugs) | 458 |
| Excluded (alias / router / non-text output) | 40 |
| Eligible models (after collapsing `:free`, `:batch`, … variants) | 332 |
| Failed callability check (0 live endpoints) | 0 |
| **Evaluated models** | **332** |
| GI-qualified | 292 |
| Did Not Qualify for GI (no generation number in name) | 40 |

| Statistic | Value |
| :-- | --: |
| Mean GI | 3.537 |
| Median GI | 3.4 |
| Mean NL | 14.54 |
| Median NL | 14 |
| Industry Generational Velocity (OLS, GI per year) | +0.451 |

## 1. Track A: Generation Index (GI) ↑

All 292 GI-qualified models, ranked by the generation number in their name. Ties share a rank.
Bar chart of every model: [`figures/full_gi.svg`](figures/full_gi.svg).

| Rank | Model | Vendor | GI | NL | Listed | Slug |
| --: | :-- | :-- | --: | --: | :-- | :-- |
| 🥇 1 | Pareto 26.10 Preview | unbiased | `26.10` | 20 | 2026-10-01 | `unbiased/pareto-26.10-preview` |
| 🥈 2 | GPT-6.1 Sol | OpenAI | `6.1` | 11 | 2026-09-29 | `openai/gpt-6.1-sol` |
| 🥈 2 | GPT-6.1 Sol Pro | OpenAI | `6.1` | 15 | 2026-09-29 | `openai/gpt-6.1-sol-pro` |
| 4 | GPT-6 Astra | OpenAI | `6` | 11 | 2026-09-04 | `openai/gpt-6-astra` |
| 4 | GPT-6 Astra Pro | OpenAI | `6` | 15 | 2026-09-04 | `openai/gpt-6-astra-pro` |
| 4 | GPT-6 Luna | OpenAI | `6` | 10 | 2026-09-22 | `openai/gpt-6-luna` |
| 4 | GPT-6 Luna Pro | OpenAI | `6` | 14 | 2026-09-22 | `openai/gpt-6-luna-pro` |
| 4 | GPT-6 Sol | OpenAI | `6` | 9 | 2026-09-22 | `openai/gpt-6-sol` |
| 4 | GPT-6 Sol Pro | OpenAI | `6` | 13 | 2026-09-22 | `openai/gpt-6-sol-pro` |
| 10 | GPT-5.6 Luna | OpenAI | `5.6` | 12 | 2026-07-09 | `openai/gpt-5.6-luna` |
| 10 | GPT-5.6 Luna Pro | OpenAI | `5.6` | 16 | 2026-07-09 | `openai/gpt-5.6-luna-pro` |
| 10 | GPT-5.6 Sol | OpenAI | `5.6` | 11 | 2026-07-09 | `openai/gpt-5.6-sol` |
| 10 | GPT-5.6 Sol Pro | OpenAI | `5.6` | 15 | 2026-07-09 | `openai/gpt-5.6-sol-pro` |
| 10 | GPT-5.6 Terra | OpenAI | `5.6` | 13 | 2026-07-09 | `openai/gpt-5.6-terra` |
| 10 | GPT-5.6 Terra Pro | OpenAI | `5.6` | 17 | 2026-07-09 | `openai/gpt-5.6-terra-pro` |
| 16 | Claude Haiku 5.5 | Anthropic | `5.5` | 16 | 2026-10-07 | `anthropic/claude-haiku-5.5` |
| 16 | Claude Opus 5.5 | Anthropic | `5.5` | 15 | 2026-09-22 | `anthropic/claude-opus-5.5` |
| 16 | Claude Sonnet 5.5 | Anthropic | `5.5` | 17 | 2026-09-28 | `anthropic/claude-sonnet-5.5` |
| 16 | GPT-5.5 | OpenAI | `5.5` | 7 | 2026-04-24 | `openai/gpt-5.5` |
| 16 | GPT-5.5 Pro | OpenAI | `5.5` | 11 | 2026-04-24 | `openai/gpt-5.5-pro` |
| 21 | GPT-5.4 | OpenAI | `5.4` | 7 | 2026-03-05 | `openai/gpt-5.4` |
| 21 | GPT-5.4 Mini | OpenAI | `5.4` | 12 | 2026-03-17 | `openai/gpt-5.4-mini` |
| 21 | GPT-5.4 Nano | OpenAI | `5.4` | 12 | 2026-03-17 | `openai/gpt-5.4-nano` |
| 21 | GPT-5.4 Pro | OpenAI | `5.4` | 11 | 2026-03-05 | `openai/gpt-5.4-pro` |
| 25 | GLM 5.3 | Z.ai | `5.3` | 7 | 2026-08-18 | `z-ai/glm-5.3` |
| 25 | GLM 5.3 Flash | Z.ai | `5.3` | 13 | 2026-08-26 | `z-ai/glm-5.3-flash` |
| 25 | GLM 5.3 FlashX | Z.ai | `5.3` | 14 | 2026-09-18 | `z-ai/glm-5.3-flashx` |
| 25 | GLM 5.3 Prime | Z.ai | `5.3` | 13 | 2026-09-23 | `z-ai/glm-5.3-prime` |
| 25 | GPT-5.3-Codex | OpenAI | `5.3` | 13 | 2026-02-24 | `openai/gpt-5.3-codex` |
| 30 | GLM 5.2 | Z.ai | `5.2` | 7 | 2026-06-16 | `z-ai/glm-5.2` |
| 30 | GPT-5.2 | OpenAI | `5.2` | 7 | 2025-12-10 | `openai/gpt-5.2` |
| 30 | GPT-5.2 Chat | OpenAI | `5.2` | 12 | 2025-12-10 | `openai/gpt-5.2-chat` |
| 30 | GPT-5.2 Pro | OpenAI | `5.2` | 11 | 2025-12-10 | `openai/gpt-5.2-pro` |
| 30 | GPT-5.2-Codex | OpenAI | `5.2` | 13 | 2026-01-14 | `openai/gpt-5.2-codex` |
| 35 | Claude Fable 5.1 | Anthropic | `5.1` | 16 | 2026-09-01 | `anthropic/claude-fable-5.1` |
| 35 | GLM 5.1 | Z.ai | `5.1` | 7 | 2026-04-07 | `z-ai/glm-5.1` |
| 35 | GPT-5.1 | OpenAI | `5.1` | 7 | 2025-11-13 | `openai/gpt-5.1` |
| 35 | GPT-5.1-Codex | OpenAI | `5.1` | 13 | 2025-11-13 | `openai/gpt-5.1-codex` |
| 35 | GPT-5.1-Codex-Max | OpenAI | `5.1` | 17 | 2025-12-04 | `openai/gpt-5.1-codex-max` |
| 35 | GPT-5.1-Codex-Mini | OpenAI | `5.1` | 18 | 2025-11-13 | `openai/gpt-5.1-codex-mini` |
| 41 | Claude Fable 5 | Anthropic | `5` | 14 | 2026-06-09 | `anthropic/claude-fable-5` |
| 41 | Claude Opus 5 | Anthropic | `5` | 13 | 2026-07-24 | `anthropic/claude-opus-5` |
| 41 | Claude Sonnet 5 | Anthropic | `5` | 15 | 2026-06-30 | `anthropic/claude-sonnet-5` |
| 41 | GLM 5 | Z.ai | `5` | 5 | 2026-02-11 | `z-ai/glm-5` |
| 41 | GLM 5 Turbo | Z.ai | `5` | 11 | 2026-03-15 | `z-ai/glm-5-turbo` |
| 41 | GLM 5V Turbo | Z.ai | `5` | 12 | 2026-04-01 | `z-ai/glm-5v-turbo` |
| 41 | GPT-5 | OpenAI | `5` | 5 | 2025-08-07 | `openai/gpt-5` |
| 41 | GPT-5 Mini | OpenAI | `5` | 10 | 2025-08-07 | `openai/gpt-5-mini` |
| 41 | GPT-5 Nano | OpenAI | `5` | 10 | 2025-08-07 | `openai/gpt-5-nano` |
| 41 | GPT-5 Pro | OpenAI | `5` | 9 | 2025-10-06 | `openai/gpt-5-pro` |
| 41 | Palmyra X5 | Writer | `5` | 10 | 2026-01-21 | `writer/palmyra-x5` |
| 41 | Step 5 Preview | StepFun | `5` | 14 | 2026-10-08 | `stepfun/step-5-preview` |
| 53 | Claude Opus 4.8 | Anthropic | `4.8` | 15 | 2026-05-27 | `anthropic/claude-opus-4.8` |
| 54 | Claude Opus 4.7 | Anthropic | `4.7` | 15 | 2026-04-16 | `anthropic/claude-opus-4.7` |
| 54 | GLM 4.7 | Z.ai | `4.7` | 7 | 2025-12-22 | `z-ai/glm-4.7` |
| 54 | GLM 4.7 Flash | Z.ai | `4.7` | 13 | 2026-01-19 | `z-ai/glm-4.7-flash` |
| 54 | Grok 4.7 | SpaceXAI | `4.7` | 8 | 2026-09-21 | `x-ai/grok-4.7` |
| 58 | Claude Opus 4.6 | Anthropic | `4.6` | 15 | 2026-02-04 | `anthropic/claude-opus-4.6` |
| 58 | Claude Sonnet 4.6 | Anthropic | `4.6` | 17 | 2026-02-17 | `anthropic/claude-sonnet-4.6` |
| 58 | GLM 4.6 | Z.ai | `4.6` | 7 | 2025-09-30 | `z-ai/glm-4.6` |
| 58 | GLM 4.6V | Z.ai | `4.6` | 8 | 2025-12-08 | `z-ai/glm-4.6v` |
| 58 | Grok 4.6 | SpaceXAI | `4.6` | 8 | 2026-08-12 | `x-ai/grok-4.6` |
| 63 | Claude Haiku 4.5 | Anthropic | `4.5` | 16 | 2025-10-15 | `anthropic/claude-haiku-4.5` |
| 63 | Claude Opus 4.5 | Anthropic | `4.5` | 15 | 2025-11-24 | `anthropic/claude-opus-4.5` |
| 63 | Claude Sonnet 4.5 | Anthropic | `4.5` | 17 | 2025-09-29 | `anthropic/claude-sonnet-4.5` |
| 63 | GLM 4.5 | Z.ai | `4.5` | 7 | 2025-07-25 | `z-ai/glm-4.5` |
| 63 | GLM 4.5 Air | Z.ai | `4.5` | 11 | 2025-07-25 | `z-ai/glm-4.5-air` |
| 63 | GLM 4.5V | Z.ai | `4.5` | 8 | 2025-08-11 | `z-ai/glm-4.5v` |
| 63 | Grok 4.5 | SpaceXAI | `4.5` | 8 | 2026-07-08 | `x-ai/grok-4.5` |
| 70 | Grok 4.3 | SpaceXAI | `4.3` | 8 | 2026-04-30 | `x-ai/grok-4.3` |
| 71 | Granite 4.2 8B | IBM | `4.2` | 14 | 2026-08-31 | `ibm-granite/granite-4.2-8b` |
| 71 | Grok 4.20 | SpaceXAI | `4.20` | 9 | 2026-03-31 | `x-ai/grok-4.20` |
| 71 | Grok 4.20 Multi-Agent | SpaceXAI | `4.20` | 21 | 2026-03-31 | `x-ai/grok-4.20-multi-agent` |
| 74 | Claude Opus 4.1 | Anthropic | `4.1` | 15 | 2025-08-05 | `anthropic/claude-opus-4.1` |
| 74 | Cydonia 24B V4.1 | TheDrummer | `4.1` | 16 | 2025-09-27 | `thedrummer/cydonia-24b-v4.1` |
| 74 | DeepSeek V4.1 Flash | DeepSeek | `4.1` | 19 | 2026-09-10 | `deepseek/deepseek-v4.1-flash` |
| 74 | GPT-4.1 | OpenAI | `4.1` | 7 | 2025-04-14 | `openai/gpt-4.1` |
| 74 | GPT-4.1 Mini | OpenAI | `4.1` | 12 | 2025-04-14 | `openai/gpt-4.1-mini` |
| 74 | GPT-4.1 Nano | OpenAI | `4.1` | 12 | 2025-04-14 | `openai/gpt-4.1-nano` |
| 80 | Claude Sonnet 4 | Anthropic | `4` | 15 | 2025-05-22 | `anthropic/claude-sonnet-4` |
| 80 | DeepSeek V4 Flash 0423 | DeepSeek | `4` | 22 | 2026-04-24 | `deepseek/deepseek-v4-flash` |
| 80 | DeepSeek V4 Flash 0731 | DeepSeek | `4` | 22 | 2026-07-31 | `deepseek/deepseek-v4-flash-0731` |
| 80 | DeepSeek V4 Flash Vision Exp | DeepSeek | `4` | 28 | 2026-08-21 | `deepseek/deepseek-v4-flash-vision-exp` |
| 80 | DeepSeek V4 Pro 0423 | DeepSeek | `4` | 20 | 2026-04-24 | `deepseek/deepseek-v4-pro` |
| 80 | DeepSeek V4 Pro 0813 | DeepSeek | `4` | 20 | 2026-08-12 | `deepseek/deepseek-v4-pro-0813` |
| 80 | Gemma 4 26B A4B | Google | `4` | 15 | 2026-04-03 | `google/gemma-4-26b-a4b-it` |
| 80 | Gemma 4 31B | Google | `4` | 11 | 2026-04-02 | `google/gemma-4-31b-it` |
| 80 | GPT-4 | OpenAI | `4` | 5 | 2023-05-28 | `openai/gpt-4` |
| 80 | GPT-4 Turbo | OpenAI | `4` | 11 | 2024-04-09 | `openai/gpt-4-turbo` |
| 80 | GPT-4o | OpenAI | `4` | 6 | 2024-05-13 | `openai/gpt-4o` |
| 80 | GPT-4o (2024-05-13) | OpenAI | `4` | 19 | 2024-05-13 | `openai/gpt-4o-2024-05-13` |
| 80 | GPT-4o (2024-08-06) | OpenAI | `4` | 19 | 2024-08-06 | `openai/gpt-4o-2024-08-06` |
| 80 | GPT-4o (2024-11-20) | OpenAI | `4` | 19 | 2024-11-20 | `openai/gpt-4o-2024-11-20` |
| 80 | GPT-4o-mini | OpenAI | `4` | 11 | 2024-07-18 | `openai/gpt-4o-mini` |
| 80 | GPT-4o-mini (2024-07-18) | OpenAI | `4` | 24 | 2024-07-18 | `openai/gpt-4o-mini-2024-07-18` |
| 80 | Granite 4.0 Micro | IBM | `4.0` | 17 | 2025-10-20 | `ibm-granite/granite-4.0-h-micro` |
| 80 | Hermes 4 405B | Nous | `4` | 13 | 2025-08-26 | `nousresearch/hermes-4-405b` |
| 80 | Hy4 preview | Tencent | `4` | 11 | 2026-08-28 | `tencent/hy4-preview` |
| 80 | Llama 4 Maverick | Meta | `4` | 16 | 2025-04-05 | `meta-llama/llama-4-maverick` |
| 80 | Llama 4 Scout | Meta | `4` | 13 | 2025-04-05 | `meta-llama/llama-4-scout` |
| 80 | Llama Guard 4 12B | Meta | `4` | 17 | 2025-04-30 | `meta-llama/llama-guard-4-12b` |
| 80 | Magnum v4 72B | anthracite-org | `4` | 13 | 2024-10-22 | `anthracite-org/magnum-v4-72b` |
| 80 | Mistral Large 4 | Mistral | `4` | 15 | 2026-10-06 | `mistralai/mistral-large-4-0` |
| 80 | Mistral Small 4 | Mistral | `4` | 15 | 2026-03-16 | `mistralai/mistral-small-2603` |
| 80 | o4 Mini | OpenAI | `4` | 7 | 2025-04-16 | `openai/o4-mini` |
| 80 | o4 Mini High | OpenAI | `4` | 12 | 2025-04-16 | `openai/o4-mini-high` |
| 80 | Phi 4 | Microsoft | `4` | 5 | 2025-01-10 | `microsoft/phi-4` |
| 80 | Solar Mini 4 | Upstage | `4` | 12 | 2026-09-23 | `upstage/solar-mini4` |
| 80 | Solar Pro 4 | Upstage | `4` | 11 | 2026-08-10 | `upstage/solar-pro4` |
| 110 | Gemini 3.8 Flash | Google | `3.8` | 16 | 2026-09-02 | `google/gemini-3.8-flash` |
| 110 | Qwen3.8 2.4T A95B | Qwen | `3.8` | 17 | 2026-08-12 | `qwen/qwen3.8-2.4t-a95b` |
| 110 | Qwen3.8 27B | Qwen | `3.8` | 11 | 2026-08-14 | `qwen/qwen3.8-27b` |
| 110 | Qwen3.8 Flash | Qwen | `3.8` | 13 | 2026-08-26 | `qwen/qwen3.8-flash` |
| 110 | Qwen3.8 Max (0902) | Qwen | `3.8` | 18 | 2026-09-03 | `qwen/qwen3.8-max-0902` |
| 110 | Qwen3.8 Max Prime | Qwen | `3.8` | 17 | 2026-09-23 | `qwen/qwen3.8-max-prime` |
| 110 | Qwen3.8 Omni Flash | Qwen | `3.8` | 18 | 2026-09-21 | `qwen/qwen3.8-omni-flash` |
| 117 | Gemini 3.7 Flash | Google | `3.7` | 16 | 2026-08-13 | `google/gemini-3.7-flash` |
| 117 | Qwen3.7 Flash | Qwen | `3.7` | 13 | 2026-07-27 | `qwen/qwen3.7-flash` |
| 117 | Qwen3.7 Max | Qwen | `3.7` | 11 | 2026-05-21 | `qwen/qwen3.7-max` |
| 117 | Qwen3.7 Plus | Qwen | `3.7` | 12 | 2026-06-03 | `qwen/qwen3.7-plus` |
| 117 | Step 3.7 Flash | StepFun | `3.7` | 14 | 2026-05-28 | `stepfun/step-3.7-flash` |
| 122 | Gemini 3.6 Flash | Google | `3.6` | 16 | 2026-07-21 | `google/gemini-3.6-flash` |
| 122 | Qwen3.6 27B | Qwen | `3.6` | 11 | 2026-04-27 | `qwen/qwen3.6-27b` |
| 122 | Qwen3.6 35B A3B | Qwen | `3.6` | 15 | 2026-04-27 | `qwen/qwen3.6-35b-a3b` |
| 122 | Qwen3.6 Flash | Qwen | `3.6` | 13 | 2026-04-27 | `qwen/qwen3.6-flash` |
| 122 | Qwen3.6 Plus | Qwen | `3.6` | 12 | 2026-04-02 | `qwen/qwen3.6-plus` |
| 127 | Aion 3.5 | AionLabs | `3.5` | 8 | 2026-09-23 | `aion-labs/aion-3.5` |
| 127 | Aion 3.5 Mini | AionLabs | `3.5` | 13 | 2026-09-23 | `aion-labs/aion-3.5-mini` |
| 127 | Gemini 3.5 Flash | Google | `3.5` | 16 | 2026-05-19 | `google/gemini-3.5-flash` |
| 127 | Gemini 3.5 Flash Lite | Google | `3.5` | 21 | 2026-07-21 | `google/gemini-3.5-flash-lite` |
| 127 | GPT-3.5 Turbo | OpenAI | `3.5` | 13 | 2023-05-28 | `openai/gpt-3.5-turbo` |
| 127 | GPT-3.5 Turbo (older v0613) | OpenAI | `3.5` | 27 | 2024-01-25 | `openai/gpt-3.5-turbo-0613` |
| 127 | GPT-3.5 Turbo 16k | OpenAI | `3.5` | 17 | 2023-08-28 | `openai/gpt-3.5-turbo-16k` |
| 127 | GPT-3.5 Turbo Instruct | OpenAI | `3.5` | 22 | 2023-09-28 | `openai/gpt-3.5-turbo-instruct` |
| 127 | Mistral Medium 3.5 | Mistral | `3.5` | 18 | 2026-04-30 | `mistralai/mistral-medium-3-5` |
| 127 | Nemotron 3.5 Content Safety | NVIDIA | `3.5` | 27 | 2026-06-04 | `nvidia/nemotron-3.5-content-safety` |
| 127 | Nemotron 3.5 Lightning | NVIDIA | `3.5` | 22 | 2026-08-11 | `nvidia/nemotron-3.5-lightning` |
| 127 | Qwen3.5 397B A17B | Qwen | `3.5` | 17 | 2026-02-16 | `qwen/qwen3.5-397b-a17b` |
| 127 | Qwen3.5 Plus 2026-02-15 | Qwen | `3.5` | 23 | 2026-02-16 | `qwen/qwen3.5-plus-02-15` |
| 127 | Qwen3.5 Plus 2026-04-20 | Qwen | `3.5` | 23 | 2026-04-27 | `qwen/qwen3.5-plus-20260420` |
| 127 | Qwen3.5-122B-A10B | Qwen | `3.5` | 17 | 2026-02-25 | `qwen/qwen3.5-122b-a10b` |
| 127 | Qwen3.5-27B | Qwen | `3.5` | 11 | 2026-02-25 | `qwen/qwen3.5-27b` |
| 127 | Qwen3.5-35B-A3B | Qwen | `3.5` | 15 | 2026-02-25 | `qwen/qwen3.5-35b-a3b` |
| 127 | Qwen3.5-9B | Qwen | `3.5` | 10 | 2026-03-10 | `qwen/qwen3.5-9b` |
| 127 | Qwen3.5-Flash | Qwen | `3.5` | 13 | 2026-02-25 | `qwen/qwen3.5-flash-02-23` |
| 127 | Step 3.5 Flash | StepFun | `3.5` | 14 | 2026-01-29 | `stepfun/step-3.5-flash` |
| 147 | Llama 3.3 70B Instruct | Meta | `3.3` | 22 | 2024-12-06 | `meta-llama/llama-3.3-70b-instruct` |
| 147 | Llama 3.3 Euryale 70B | Sao10K | `3.3` | 21 | 2024-12-18 | `sao10k/l3.3-euryale-70b` |
| 149 | DeepSeek V3.2 | DeepSeek | `3.2` | 13 | 2025-12-01 | `deepseek/deepseek-v3.2` |
| 149 | DeepSeek V3.2 Exp | DeepSeek | `3.2` | 17 | 2025-09-29 | `deepseek/deepseek-v3.2-exp` |
| 149 | Llama 3.2 1B Instruct | Meta | `3.2` | 21 | 2024-09-25 | `meta-llama/llama-3.2-1b-instruct` |
| 149 | Llama 3.2 3B Instruct | Meta | `3.2` | 21 | 2024-09-25 | `meta-llama/llama-3.2-3b-instruct` |
| 149 | Mistral Small 3.2 24B | Mistral | `3.2` | 21 | 2025-06-20 | `mistralai/mistral-small-3.2-24b-instruct` |
| 154 | DeepSeek V3.1 | DeepSeek | `3.1` | 13 | 2025-08-21 | `deepseek/deepseek-chat-v3.1` |
| 154 | DeepSeek V3.1 Terminus | DeepSeek | `3.1` | 22 | 2025-09-22 | `deepseek/deepseek-v3.1-terminus` |
| 154 | Gemini 3.1 Flash Lite | Google | `3.1` | 21 | 2026-05-07 | `google/gemini-3.1-flash-lite` |
| 154 | Gemini 3.1 Flash Lite Preview | Google | `3.1` | 29 | 2026-03-03 | `google/gemini-3.1-flash-lite-preview` |
| 154 | Gemini 3.1 Pro Preview | Google | `3.1` | 22 | 2026-02-19 | `google/gemini-3.1-pro-preview` |
| 154 | Gemini 3.1 Pro Preview Custom Tools | Google | `3.1` | 35 | 2026-02-25 | `google/gemini-3.1-pro-preview-customtools` |
| 154 | Ling 3.1 Flash | inclusionAI | `3.1` | 14 | 2026-10-02 | `inclusionai/ling-3.1-flash` |
| 154 | Llama 3.1 70B Instruct | Meta | `3.1` | 22 | 2024-07-23 | `meta-llama/llama-3.1-70b-instruct` |
| 154 | Llama 3.1 8B Instruct | Meta | `3.1` | 21 | 2024-07-23 | `meta-llama/llama-3.1-8b-instruct` |
| 154 | Llama 3.1 Euryale 70B v2.2 | Sao10K | `3.1` | 26 | 2024-08-28 | `sao10k/l3.1-euryale-70b` |
| 154 | Mistral Medium 3.1 | Mistral | `3.1` | 18 | 2025-08-13 | `mistralai/mistral-medium-3.1` |
| 154 | Mistral Small 3.1 24B | Mistral | `3.1` | 21 | 2025-03-17 | `mistralai/mistral-small-3.1-24b-instruct` |
| 166 | Aion-3.0 | AionLabs | `3.0` | 8 | 2026-07-07 | `aion-labs/aion-3.0` |
| 166 | Aion-3.0-Mini | AionLabs | `3.0` | 13 | 2026-07-07 | `aion-labs/aion-3.0-mini` |
| 166 | DeepSeek V3 | DeepSeek | `3` | 11 | 2024-12-26 | `deepseek/deepseek-chat` |
| 166 | DeepSeek V3 0324 | DeepSeek | `3` | 16 | 2025-03-24 | `deepseek/deepseek-chat-v3-0324` |
| 166 | Dots3-Note Preview | Dots Studio | `3` | 18 | 2026-08-14 | `dots-studio/dots-3-note-preview` |
| 166 | Gemini 3 Flash Preview | Google | `3` | 22 | 2025-12-17 | `google/gemini-3-flash-preview` |
| 166 | Gemma 3 12B | Google | `3` | 11 | 2025-03-13 | `google/gemma-3-12b-it` |
| 166 | Gemma 3 27B | Google | `3` | 11 | 2025-03-12 | `google/gemma-3-27b-it` |
| 166 | Gemma 3 4B | Google | `3` | 10 | 2025-03-13 | `google/gemma-3-4b-it` |
| 166 | Hermes 3 405B Instruct | Nous | `3` | 22 | 2024-08-16 | `nousresearch/hermes-3-llama-3.1-405b` |
| 166 | Hermes 3 70B Instruct | Nous | `3` | 21 | 2024-08-18 | `nousresearch/hermes-3-llama-3.1-70b` |
| 166 | Hy3 | Tencent | `3` | 3 | 2026-07-06 | `tencent/hy3` |
| 166 | Hy3 preview | Tencent | `3` | 11 | 2026-04-22 | `tencent/hy3-preview` |
| 166 | Kimi K3 | MoonshotAI | `3` | 7 | 2026-07-16 | `moonshotai/kimi-k3` |
| 166 | Ling 3.0 Flash | inclusionAI | `3.0` | 14 | 2026-07-23 | `inclusionai/ling-3.0-flash` |
| 166 | Ling 3.0 Flash Fin | inclusionAI | `3.0` | 18 | 2026-08-27 | `inclusionai/ling-3.0-flash-fin` |
| 166 | Ling 3.0 Flash Sante | inclusionAI | `3.0` | 20 | 2026-09-04 | `inclusionai/ling-3.0-flash-sante` |
| 166 | Ling 3.0 Flash VL | inclusionAI | `3.0` | 17 | 2026-09-10 | `inclusionai/ling-3.0-flash-vl` |
| 166 | Llama 3 8B Lunaris | Sao10K | `3` | 18 | 2024-08-13 | `sao10k/l3-lunaris-8b` |
| 166 | MiniMax M3 | MiniMax | `3` | 10 | 2026-05-31 | `minimax/minimax-m3` |
| 166 | Ministral 3 14B 2512 | Mistral | `3` | 20 | 2025-12-02 | `mistralai/ministral-14b-2512` |
| 166 | Ministral 3 3B 2512 | Mistral | `3` | 19 | 2025-12-02 | `mistralai/ministral-3b-2512` |
| 166 | Ministral 3 8B 2512 | Mistral | `3` | 19 | 2025-12-02 | `mistralai/ministral-8b-2512` |
| 166 | Mistral Large 3 2512 | Mistral | `3` | 20 | 2025-12-01 | `mistralai/mistral-large-2512` |
| 166 | Mistral Medium 3 | Mistral | `3` | 16 | 2025-05-07 | `mistralai/mistral-medium-3` |
| 166 | Mistral Small 3 | Mistral | `3` | 15 | 2025-01-30 | `mistralai/mistral-small-24b-instruct-2501` |
| 166 | Morph V3 Fast | Morph | `3` | 13 | 2025-07-07 | `morph/morph-v3-fast` |
| 166 | Morph V3 Large | Morph | `3` | 14 | 2025-07-07 | `morph/morph-v3-large` |
| 166 | Nemotron 3 Nano 30B A3B | NVIDIA | `3` | 23 | 2025-12-14 | `nvidia/nemotron-3-nano-30b-a3b` |
| 166 | Nemotron 3 Nano Omni | NVIDIA | `3` | 20 | 2026-04-28 | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` |
| 166 | Nemotron 3 Super | NVIDIA | `3` | 16 | 2026-03-11 | `nvidia/nemotron-3-super-120b-a12b` |
| 166 | Nemotron 3 Ultra | NVIDIA | `3` | 16 | 2026-06-04 | `nvidia/nemotron-3-ultra-550b-a55b` |
| 166 | o3 | OpenAI | `3` | 2 | 2025-04-16 | `openai/o3` |
| 166 | o3 Mini | OpenAI | `3` | 7 | 2025-01-31 | `openai/o3-mini` |
| 166 | o3 Mini High | OpenAI | `3` | 12 | 2025-02-12 | `openai/o3-mini-high` |
| 166 | o3 Pro | OpenAI | `3` | 6 | 2025-06-10 | `openai/o3-pro` |
| 166 | Qwen3 14B | Qwen | `3` | 9 | 2025-04-28 | `qwen/qwen3-14b` |
| 166 | Qwen3 235B A22B Instruct 2507 | Qwen | `3` | 29 | 2025-07-21 | `qwen/qwen3-235b-a22b-2507` |
| 166 | Qwen3 235B A22B Thinking 2507 | Qwen | `3` | 29 | 2025-07-25 | `qwen/qwen3-235b-a22b-thinking-2507` |
| 166 | Qwen3 30B A3B | Qwen | `3` | 13 | 2025-04-28 | `qwen/qwen3-30b-a3b` |
| 166 | Qwen3 30B A3B Instruct 2507 | Qwen | `3` | 27 | 2025-07-29 | `qwen/qwen3-30b-a3b-instruct-2507` |
| 166 | Qwen3 32B | Qwen | `3` | 9 | 2025-04-28 | `qwen/qwen3-32b` |
| 166 | Qwen3 Coder 30B A3B Instruct | Qwen | `3` | 28 | 2025-07-31 | `qwen/qwen3-coder-30b-a3b-instruct` |
| 166 | Qwen3 Coder 480B A35B | Qwen | `3` | 21 | 2025-07-23 | `qwen/qwen3-coder` |
| 166 | Qwen3 Coder Flash | Qwen | `3` | 17 | 2025-09-17 | `qwen/qwen3-coder-flash` |
| 166 | Qwen3 Coder Next | Qwen | `3` | 16 | 2026-02-04 | `qwen/qwen3-coder-next` |
| 166 | Qwen3 Next 80B A3B Instruct | Qwen | `3` | 27 | 2025-09-11 | `qwen/qwen3-next-80b-a3b-instruct` |
| 166 | Qwen3 Next 80B A3B Thinking | Qwen | `3` | 27 | 2025-09-11 | `qwen/qwen3-next-80b-a3b-thinking` |
| 166 | Qwen3 VL 235B A22B Instruct | Qwen | `3` | 27 | 2025-09-23 | `qwen/qwen3-vl-235b-a22b-instruct` |
| 166 | Qwen3 VL 30B A3B Instruct | Qwen | `3` | 25 | 2025-10-06 | `qwen/qwen3-vl-30b-a3b-instruct` |
| 166 | Qwen3 VL 30B A3B Thinking | Qwen | `3` | 25 | 2025-10-06 | `qwen/qwen3-vl-30b-a3b-thinking` |
| 166 | Qwen3 VL 8B Instruct | Qwen | `3` | 20 | 2025-10-14 | `qwen/qwen3-vl-8b-instruct` |
| 166 | Reka Flash 3 | rekaai | `3` | 12 | 2025-03-12 | `rekaai/reka-flash-3` |
| 166 | Relace Apply 3 | Relace | `3` | 14 | 2025-09-26 | `relace/relace-apply-3` |
| 166 | Solar Pro 3 | Upstage | `3` | 11 | 2026-01-27 | `upstage/solar-pro-3` |
| 221 | Kimi K2.7 Code | MoonshotAI | `2.7` | 14 | 2026-06-12 | `moonshotai/kimi-k2.7-code` |
| 221 | MiniMax M2.7 | MiniMax | `2.7` | 12 | 2026-03-18 | `minimax/minimax-m2.7` |
| 223 | Kimi K2.6 | MoonshotAI | `2.6` | 9 | 2026-04-20 | `moonshotai/kimi-k2.6` |
| 223 | MiMo-V2.6-Flash | Xiaomi | `2.6` | 15 | 2026-09-21 | `xiaomi/mimo-v2.6-flash` |
| 223 | MiMo-V2.6-Pro | Xiaomi | `2.6` | 13 | 2026-09-21 | `xiaomi/mimo-v2.6-pro` |
| 223 | MiMo-V2.6-Pro-UltraSpeed | Xiaomi | `2.6` | 24 | 2026-09-21 | `xiaomi/mimo-v2.6-pro-ultraspeed` |
| 227 | Gemini 2.5 Flash | Google | `2.5` | 16 | 2025-06-17 | `google/gemini-2.5-flash` |
| 227 | Gemini 2.5 Flash Lite | Google | `2.5` | 21 | 2025-07-22 | `google/gemini-2.5-flash-lite` |
| 227 | Gemini 2.5 Pro | Google | `2.5` | 14 | 2025-06-17 | `google/gemini-2.5-pro` |
| 227 | Gemini 2.5 Pro Preview 06-05 | Google | `2.5` | 28 | 2025-06-05 | `google/gemini-2.5-pro-preview` |
| 227 | Kimi K2.5 | MoonshotAI | `2.5` | 9 | 2026-01-27 | `moonshotai/kimi-k2.5` |
| 227 | LFM2.5-2.6B | LiquidAI | `2.5` | 11 | 2026-08-11 | `liquid/lfm-2.5-2.6b` |
| 227 | Mercury 2.5 | Inception | `2.5` | 11 | 2026-09-08 | `inception/mercury-2.5` |
| 227 | MiMo-V2.5 | Xiaomi | `2.5` | 9 | 2026-04-22 | `xiaomi/mimo-v2.5` |
| 227 | MiMo-V2.5-Pro | Xiaomi | `2.5` | 13 | 2026-04-22 | `xiaomi/mimo-v2.5-pro` |
| 227 | MiniMax M2.5 | MiniMax | `2.5` | 12 | 2026-02-12 | `minimax/minimax-m2.5` |
| 227 | Nex-N2.5-Mini | Nex AGI | `2.5` | 13 | 2026-09-08 | `nex-agi/nex-n2.5-mini` |
| 227 | Nex-N2.5-Pro | Nex AGI | `2.5` | 12 | 2026-09-08 | `nex-agi/nex-n2.5-pro` |
| 227 | Qwen2.5 72B Instruct | Qwen | `2.5` | 20 | 2024-09-19 | `qwen/qwen-2.5-72b-instruct` |
| 227 | Qwen2.5 7B Instruct | Qwen | `2.5` | 19 | 2024-10-16 | `qwen/qwen-2.5-7b-instruct` |
| 227 | Qwen2.5 Coder 32B Instruct | Qwen | `2.5` | 26 | 2024-11-11 | `qwen/qwen-2.5-coder-32b-instruct` |
| 227 | Qwen2.5 VL 72B Instruct | Qwen | `2.5` | 23 | 2025-02-01 | `qwen/qwen2.5-vl-72b-instruct` |
| 243 | Laguna S 2.1 | Poolside | `2.1` | 12 | 2026-07-21 | `poolside/laguna-s-2.1` |
| 243 | Laguna XS 2.1 | Poolside | `2.1` | 13 | 2026-07-02 | `poolside/laguna-xs-2.1` |
| 243 | MiniMax M2.1 | MiniMax | `2.1` | 12 | 2025-12-23 | `minimax/minimax-m2.1` |
| 243 | Seed 2.1 Turbo | ByteDance Seed | `2.1` | 14 | 2026-08-12 | `bytedance-seed/seed-2-1-turbo` |
| 247 | Aion-2.0 | AionLabs | `2.0` | 8 | 2026-02-23 | `aion-labs/aion-2.0` |
| 247 | Devstral 2 2512 | Mistral | `2` | 15 | 2025-12-09 | `mistralai/devstral-2512` |
| 247 | Fugu Ultra v2 | Sakana | `2` | 13 | 2026-09-11 | `sakana/fugu-ultra-v2` |
| 247 | Gemma 2 27B | Google | `2` | 11 | 2024-07-13 | `google/gemma-2-27b-it` |
| 247 | Hy-MT2-1.8B | Tencent | `2` | 11 | 2026-08-20 | `tencent/hy-mt2-1.8b` |
| 247 | Hy-MT2-30B-A3B | Tencent | `2` | 14 | 2026-08-20 | `tencent/hy-mt2-30b-a3b` |
| 247 | Hy-MT2-7B | Tencent | `2` | 9 | 2026-08-19 | `tencent/hy-mt2-7b` |
| 247 | Kimi K2 0711 | MoonshotAI | `2` | 12 | 2025-07-11 | `moonshotai/kimi-k2` |
| 247 | Kimi K2 0905 | MoonshotAI | `2` | 12 | 2025-09-04 | `moonshotai/kimi-k2-0905` |
| 247 | Kimi K2 Thinking | MoonshotAI | `2` | 16 | 2025-11-06 | `moonshotai/kimi-k2-thinking` |
| 247 | LongCat 2.0 | Meituan | `2.0` | 11 | 2026-07-20 | `meituan/longcat-2.0` |
| 247 | Mercury 2 | Inception | `2` | 9 | 2026-03-04 | `inception/mercury-2` |
| 247 | MiniMax M2 | MiniMax | `2` | 10 | 2025-10-23 | `minimax/minimax-m2` |
| 247 | MiniMax M2-her | MiniMax | `2` | 14 | 2026-01-23 | `minimax/minimax-m2-her` |
| 247 | Nova 2 Lite | Amazon | `2` | 11 | 2025-12-02 | `amazon/nova-2-lite-v1` |
| 247 | Schematron V2 Small | Inference.net | `2` | 19 | 2026-09-12 | `inference-net/schematron-v2-small` |
| 247 | Schematron V2 Turbo | Inference.net | `2` | 19 | 2026-09-12 | `inference-net/schematron-v2-turbo` |
| 247 | Seed-2.0-Code | ByteDance Seed | `2.0` | 13 | 2026-08-12 | `bytedance-seed/seed-2.0-code` |
| 247 | Seed-2.0-Lite | ByteDance Seed | `2.0` | 13 | 2026-03-10 | `bytedance-seed/seed-2.0-lite` |
| 247 | Seed-2.0-Mini | ByteDance Seed | `2.0` | 13 | 2026-02-26 | `bytedance-seed/seed-2.0-mini` |
| 247 | Skyfall 36B V2 | TheDrummer | `2` | 14 | 2025-03-10 | `thedrummer/skyfall-36b-v2` |
| 247 | Ternary Bonsai 2 27B | PrismML | `2` | 20 | 2026-09-18 | `prism-ml/ternary-bonsai-2-27b` |
| 247 | WizardLM-2 8x22B | Microsoft | `2` | 16 | 2024-04-16 | `microsoft/wizardlm-2-8x22b` |
| 270 | Seed 1.6 | ByteDance Seed | `1.6` | 8 | 2025-12-23 | `bytedance-seed/seed-1.6` |
| 270 | Seed 1.6 Flash | ByteDance Seed | `1.6` | 14 | 2025-12-23 | `bytedance-seed/seed-1.6-flash` |
| 272 | Perceptron Mk1.5 | Perceptron | `1.5` | 16 | 2026-09-25 | `perceptron/perceptron-mk1.5` |
| 273 | Muse Spark 1.3 | Meta | `1.3` | 14 | 2026-09-02 | `meta/muse-spark-1.3` |
| 273 | Muse Spark 1.3 Contributor | Meta | `1.3` | 26 | 2026-09-02 | `meta/muse-spark-1.3-contributor` |
| 275 | Muse Spark 1.2 | Meta | `1.2` | 14 | 2026-08-05 | `meta/muse-spark-1.2` |
| 275 | Muse Spark 1.2 Contributor | Meta | `1.2` | 26 | 2026-08-21 | `meta/muse-spark-1.2-contributor` |
| 277 | Apodex 1.1 Mini | Apodex | `1.1` | 15 | 2026-10-01 | `apodex/apodex-1.1-mini` |
| 277 | Muse Spark 1.1 | Meta | `1.1` | 14 | 2026-07-16 | `meta/muse-spark-1.1` |
| 279 | Aion-RP 1.0 (8B) | AionLabs | `1.0` | 16 | 2025-02-04 | `aion-labs/aion-rp-llama-3.1-8b` |
| 279 | Ember-1 | Fireworks | `1` | 7 | 2026-09-24 | `fireworks/ember-1` |
| 279 | MiniMax M1 | MiniMax | `1` | 10 | 2025-06-17 | `minimax/minimax-m1` |
| 279 | MiniMax-01 | MiniMax | `01` | 10 | 2025-01-15 | `minimax/minimax-01` |
| 279 | Nova Lite 1.0 | Amazon | `1.0` | 13 | 2024-12-05 | `amazon/nova-lite-v1` |
| 279 | Nova Micro 1.0 | Amazon | `1.0` | 14 | 2024-12-05 | `amazon/nova-micro-v1` |
| 279 | Nova Premier 1.0 | Amazon | `1.0` | 16 | 2025-10-31 | `amazon/nova-premier-v1` |
| 279 | Nova Pro 1.0 | Amazon | `1.0` | 12 | 2024-12-05 | `amazon/nova-pro-v1` |
| 279 | o1 | OpenAI | `1` | 2 | 2024-12-17 | `openai/o1` |
| 279 | o1-pro | OpenAI | `1` | 6 | 2025-03-19 | `openai/o1-pro` |
| 279 | Perceptron Mk1 | Perceptron | `1` | 14 | 2026-05-12 | `perceptron/perceptron-mk1` |
| 279 | R1 | DeepSeek | `1` | 2 | 2025-01-20 | `deepseek/deepseek-r1` |
| 279 | R1 0528 | DeepSeek | `1` | 7 | 2025-05-28 | `deepseek/deepseek-r1-0528` |
| 292 | Grok Build 0.1 | SpaceXAI | `0.1` | 14 | 2026-05-20 | `x-ai/grok-build-0.1` |

### 1.1 Foundational Humility Award (lowest GI)

| Model | Vendor | GI | Listed |
| :-- | :-- | --: | :-- |
| Grok Build 0.1 | SpaceXAI | `0.1` | 2026-05-20 |
| Aion-RP 1.0 (8B) | AionLabs | `1.0` | 2025-02-04 |
| Ember-1 | Fireworks | `1` | 2026-09-24 |
| MiniMax M1 | MiniMax | `1` | 2025-06-17 |
| MiniMax-01 | MiniMax | `01` | 2025-01-15 |
| Nova Lite 1.0 | Amazon | `1.0` | 2024-12-05 |
| Nova Micro 1.0 | Amazon | `1.0` | 2024-12-05 |
| Nova Premier 1.0 | Amazon | `1.0` | 2025-10-31 |
| Nova Pro 1.0 | Amazon | `1.0` | 2024-12-05 |
| o1 | OpenAI | `1` | 2024-12-17 |

## 2. Track B: Nomenclature Length (NL) ↑

All 332 evaluated models, ranked by the character count of their canonical name. Ties share a rank.
Bar chart of every model: [`figures/full_nl.svg`](figures/full_nl.svg).

| Rank | Model | Vendor | NL | GI | Slug |
| --: | :-- | :-- | --: | --: | :-- |
| 🥇 1 | Gemini 3.1 Pro Preview Custom Tools | Google | 35 | `3.1` | `google/gemini-3.1-pro-preview-customtools` |
| 🥈 2 | Gemini 3.1 Flash Lite Preview | Google | 29 | `3.1` | `google/gemini-3.1-flash-lite-preview` |
| 🥈 2 | Qwen3 235B A22B Instruct 2507 | Qwen | 29 | `3` | `qwen/qwen3-235b-a22b-2507` |
| 🥈 2 | Qwen3 235B A22B Thinking 2507 | Qwen | 29 | `3` | `qwen/qwen3-235b-a22b-thinking-2507` |
| 5 | DeepSeek V4 Flash Vision Exp | DeepSeek | 28 | `4` | `deepseek/deepseek-v4-flash-vision-exp` |
| 5 | Gemini 2.5 Pro Preview 06-05 | Google | 28 | `2.5` | `google/gemini-2.5-pro-preview` |
| 5 | Qwen3 Coder 30B A3B Instruct | Qwen | 28 | `3` | `qwen/qwen3-coder-30b-a3b-instruct` |
| 8 | GPT-3.5 Turbo (older v0613) | OpenAI | 27 | `3.5` | `openai/gpt-3.5-turbo-0613` |
| 8 | Nemotron 3.5 Content Safety | NVIDIA | 27 | `3.5` | `nvidia/nemotron-3.5-content-safety` |
| 8 | Qwen3 30B A3B Instruct 2507 | Qwen | 27 | `3` | `qwen/qwen3-30b-a3b-instruct-2507` |
| 8 | Qwen3 Next 80B A3B Instruct | Qwen | 27 | `3` | `qwen/qwen3-next-80b-a3b-instruct` |
| 8 | Qwen3 Next 80B A3B Thinking | Qwen | 27 | `3` | `qwen/qwen3-next-80b-a3b-thinking` |
| 8 | Qwen3 VL 235B A22B Instruct | Qwen | 27 | `3` | `qwen/qwen3-vl-235b-a22b-instruct` |
| 14 | Llama 3.1 Euryale 70B v2.2 | Sao10K | 26 | `3.1` | `sao10k/l3.1-euryale-70b` |
| 14 | Muse Spark 1.2 Contributor | Meta | 26 | `1.2` | `meta/muse-spark-1.2-contributor` |
| 14 | Muse Spark 1.3 Contributor | Meta | 26 | `1.3` | `meta/muse-spark-1.3-contributor` |
| 14 | Qwen2.5 Coder 32B Instruct | Qwen | 26 | `2.5` | `qwen/qwen-2.5-coder-32b-instruct` |
| 18 | Qwen3 VL 30B A3B Instruct | Qwen | 25 | `3` | `qwen/qwen3-vl-30b-a3b-instruct` |
| 18 | Qwen3 VL 30B A3B Thinking | Qwen | 25 | `3` | `qwen/qwen3-vl-30b-a3b-thinking` |
| 20 | GPT-4o-mini (2024-07-18) | OpenAI | 24 | `4` | `openai/gpt-4o-mini-2024-07-18` |
| 20 | MiMo-V2.6-Pro-UltraSpeed | Xiaomi | 24 | `2.6` | `xiaomi/mimo-v2.6-pro-ultraspeed` |
| 22 | Nemotron 3 Nano 30B A3B | NVIDIA | 23 | `3` | `nvidia/nemotron-3-nano-30b-a3b` |
| 22 | Qwen2.5 VL 72B Instruct | Qwen | 23 | `2.5` | `qwen/qwen2.5-vl-72b-instruct` |
| 22 | Qwen3.5 Plus 2026-02-15 | Qwen | 23 | `3.5` | `qwen/qwen3.5-plus-02-15` |
| 22 | Qwen3.5 Plus 2026-04-20 | Qwen | 23 | `3.5` | `qwen/qwen3.5-plus-20260420` |
| 26 | DeepSeek V3.1 Terminus | DeepSeek | 22 | `3.1` | `deepseek/deepseek-v3.1-terminus` |
| 26 | DeepSeek V4 Flash 0423 | DeepSeek | 22 | `4` | `deepseek/deepseek-v4-flash` |
| 26 | DeepSeek V4 Flash 0731 | DeepSeek | 22 | `4` | `deepseek/deepseek-v4-flash-0731` |
| 26 | Gemini 3 Flash Preview | Google | 22 | `3` | `google/gemini-3-flash-preview` |
| 26 | Gemini 3.1 Pro Preview | Google | 22 | `3.1` | `google/gemini-3.1-pro-preview` |
| 26 | GPT-3.5 Turbo Instruct | OpenAI | 22 | `3.5` | `openai/gpt-3.5-turbo-instruct` |
| 26 | Hermes 3 405B Instruct | Nous | 22 | `3` | `nousresearch/hermes-3-llama-3.1-405b` |
| 26 | Llama 3.1 70B Instruct | Meta | 22 | `3.1` | `meta-llama/llama-3.1-70b-instruct` |
| 26 | Llama 3.3 70B Instruct | Meta | 22 | `3.3` | `meta-llama/llama-3.3-70b-instruct` |
| 26 | Mixtral 8x22B Instruct | Mistral | 22 | DNQ | `mistralai/mixtral-8x22b-instruct` |
| 26 | Nemotron 3.5 Lightning | NVIDIA | 22 | `3.5` | `nvidia/nemotron-3.5-lightning` |
| 26 | Trinity Large Thinking | Arcee AI | 22 | DNQ | `arcee-ai/trinity-large-thinking` |
| 26 | Voxtral Small 24B 2507 | Mistral | 22 | DNQ | `mistralai/voxtral-small-24b-2507` |
| 39 | Command R7B (12-2024) | Cohere | 21 | DNQ | `cohere/command-r7b-12-2024` |
| 39 | Gemini 2.5 Flash Lite | Google | 21 | `2.5` | `google/gemini-2.5-flash-lite` |
| 39 | Gemini 3.1 Flash Lite | Google | 21 | `3.1` | `google/gemini-3.1-flash-lite` |
| 39 | Gemini 3.5 Flash Lite | Google | 21 | `3.5` | `google/gemini-3.5-flash-lite` |
| 39 | gpt-oss-safeguard-20b | OpenAI | 21 | DNQ | `openai/gpt-oss-safeguard-20b` |
| 39 | Grok 4.20 Multi-Agent | SpaceXAI | 21 | `4.20` | `x-ai/grok-4.20-multi-agent` |
| 39 | Hermes 3 70B Instruct | Nous | 21 | `3` | `nousresearch/hermes-3-llama-3.1-70b` |
| 39 | Hunyuan A13B Instruct | Tencent | 21 | DNQ | `tencent/hunyuan-a13b-instruct` |
| 39 | Llama 3.1 8B Instruct | Meta | 21 | `3.1` | `meta-llama/llama-3.1-8b-instruct` |
| 39 | Llama 3.2 1B Instruct | Meta | 21 | `3.2` | `meta-llama/llama-3.2-1b-instruct` |
| 39 | Llama 3.2 3B Instruct | Meta | 21 | `3.2` | `meta-llama/llama-3.2-3b-instruct` |
| 39 | Llama 3.3 Euryale 70B | Sao10K | 21 | `3.3` | `sao10k/l3.3-euryale-70b` |
| 39 | Mistral Small 3.1 24B | Mistral | 21 | `3.1` | `mistralai/mistral-small-3.1-24b-instruct` |
| 39 | Mistral Small 3.2 24B | Mistral | 21 | `3.2` | `mistralai/mistral-small-3.2-24b-instruct` |
| 39 | Qwen3 Coder 480B A35B | Qwen | 21 | `3` | `qwen/qwen3-coder` |
| 54 | Command R+ (08-2024) | Cohere | 20 | DNQ | `cohere/command-r-plus-08-2024` |
| 54 | DeepSeek V4 Pro 0423 | DeepSeek | 20 | `4` | `deepseek/deepseek-v4-pro` |
| 54 | DeepSeek V4 Pro 0813 | DeepSeek | 20 | `4` | `deepseek/deepseek-v4-pro-0813` |
| 54 | Ling 3.0 Flash Sante | inclusionAI | 20 | `3.0` | `inclusionai/ling-3.0-flash-sante` |
| 54 | Ministral 3 14B 2512 | Mistral | 20 | `3` | `mistralai/ministral-14b-2512` |
| 54 | Mistral Large 3 2512 | Mistral | 20 | `3` | `mistralai/mistral-large-2512` |
| 54 | Nemotron 3 Nano Omni | NVIDIA | 20 | `3` | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` |
| 54 | Pareto 26.10 Preview | unbiased | 20 | `26.10` | `unbiased/pareto-26.10-preview` |
| 54 | Qwen2.5 72B Instruct | Qwen | 20 | `2.5` | `qwen/qwen-2.5-72b-instruct` |
| 54 | Qwen3 VL 8B Instruct | Qwen | 20 | `3` | `qwen/qwen3-vl-8b-instruct` |
| 54 | Ternary Bonsai 2 27B | PrismML | 20 | `2` | `prism-ml/ternary-bonsai-2-27b` |
| 65 | Command R (08-2024) | Cohere | 19 | DNQ | `cohere/command-r-08-2024` |
| 65 | DeepSeek V4.1 Flash | DeepSeek | 19 | `4.1` | `deepseek/deepseek-v4.1-flash` |
| 65 | GPT-4o (2024-05-13) | OpenAI | 19 | `4` | `openai/gpt-4o-2024-05-13` |
| 65 | GPT-4o (2024-08-06) | OpenAI | 19 | `4` | `openai/gpt-4o-2024-08-06` |
| 65 | GPT-4o (2024-11-20) | OpenAI | 19 | `4` | `openai/gpt-4o-2024-11-20` |
| 65 | Ministral 3 3B 2512 | Mistral | 19 | `3` | `mistralai/ministral-3b-2512` |
| 65 | Ministral 3 8B 2512 | Mistral | 19 | `3` | `mistralai/ministral-8b-2512` |
| 65 | Qwen2.5 7B Instruct | Qwen | 19 | `2.5` | `qwen/qwen-2.5-7b-instruct` |
| 65 | Schematron V2 Small | Inference.net | 19 | `2` | `inference-net/schematron-v2-small` |
| 65 | Schematron V2 Turbo | Inference.net | 19 | `2` | `inference-net/schematron-v2-turbo` |
| 65 | Sonar Deep Research | Perplexity | 19 | DNQ | `perplexity/sonar-deep-research` |
| 65 | Sonar Reasoning Pro | Perplexity | 19 | DNQ | `perplexity/sonar-reasoning-pro` |
| 77 | Dots3-Note Preview | Dots Studio | 18 | `3` | `dots-studio/dots-3-note-preview` |
| 77 | GPT-5.1-Codex-Mini | OpenAI | 18 | `5.1` | `openai/gpt-5.1-codex-mini` |
| 77 | Ling 3.0 Flash Fin | inclusionAI | 18 | `3.0` | `inclusionai/ling-3.0-flash-fin` |
| 77 | Llama 3 8B Lunaris | Sao10K | 18 | `3` | `sao10k/l3-lunaris-8b` |
| 77 | Mistral Large 2407 | Mistral | 18 | DNQ | `mistralai/mistral-large-2407` |
| 77 | Mistral Medium 3.1 | Mistral | 18 | `3.1` | `mistralai/mistral-medium-3.1` |
| 77 | Mistral Medium 3.5 | Mistral | 18 | `3.5` | `mistralai/mistral-medium-3-5` |
| 77 | Qwen3.8 Max (0902) | Qwen | 18 | `3.8` | `qwen/qwen3.8-max-0902` |
| 77 | Qwen3.8 Omni Flash | Qwen | 18 | `3.8` | `qwen/qwen3.8-omni-flash` |
| 86 | Claude Sonnet 4.5 | Anthropic | 17 | `4.5` | `anthropic/claude-sonnet-4.5` |
| 86 | Claude Sonnet 4.6 | Anthropic | 17 | `4.6` | `anthropic/claude-sonnet-4.6` |
| 86 | Claude Sonnet 5.5 | Anthropic | 17 | `5.5` | `anthropic/claude-sonnet-5.5` |
| 86 | DeepSeek V3.2 Exp | DeepSeek | 17 | `3.2` | `deepseek/deepseek-v3.2-exp` |
| 86 | GPT-3.5 Turbo 16k | OpenAI | 17 | `3.5` | `openai/gpt-3.5-turbo-16k` |
| 86 | GPT-5.1-Codex-Max | OpenAI | 17 | `5.1` | `openai/gpt-5.1-codex-max` |
| 86 | GPT-5.6 Terra Pro | OpenAI | 17 | `5.6` | `openai/gpt-5.6-terra-pro` |
| 86 | Granite 4.0 Micro | IBM | 17 | `4.0` | `ibm-granite/granite-4.0-h-micro` |
| 86 | Ling 3.0 Flash VL | inclusionAI | 17 | `3.0` | `inclusionai/ling-3.0-flash-vl` |
| 86 | Llama Guard 4 12B | Meta | 17 | `4` | `meta-llama/llama-guard-4-12b` |
| 86 | Qwen3 Coder Flash | Qwen | 17 | `3` | `qwen/qwen3-coder-flash` |
| 86 | Qwen3.5 397B A17B | Qwen | 17 | `3.5` | `qwen/qwen3.5-397b-a17b` |
| 86 | Qwen3.5-122B-A10B | Qwen | 17 | `3.5` | `qwen/qwen3.5-122b-a10b` |
| 86 | Qwen3.8 2.4T A95B | Qwen | 17 | `3.8` | `qwen/qwen3.8-2.4t-a95b` |
| 86 | Qwen3.8 Max Prime | Qwen | 17 | `3.8` | `qwen/qwen3.8-max-prime` |
| 101 | Aion-RP 1.0 (8B) | AionLabs | 16 | `1.0` | `aion-labs/aion-rp-llama-3.1-8b` |
| 101 | Claude Fable 5.1 | Anthropic | 16 | `5.1` | `anthropic/claude-fable-5.1` |
| 101 | Claude Haiku 4.5 | Anthropic | 16 | `4.5` | `anthropic/claude-haiku-4.5` |
| 101 | Claude Haiku 5.5 | Anthropic | 16 | `5.5` | `anthropic/claude-haiku-5.5` |
| 101 | Cydonia 24B V4.1 | TheDrummer | 16 | `4.1` | `thedrummer/cydonia-24b-v4.1` |
| 101 | DeepSeek V3 0324 | DeepSeek | 16 | `3` | `deepseek/deepseek-chat-v3-0324` |
| 101 | Gemini 2.5 Flash | Google | 16 | `2.5` | `google/gemini-2.5-flash` |
| 101 | Gemini 3.5 Flash | Google | 16 | `3.5` | `google/gemini-3.5-flash` |
| 101 | Gemini 3.6 Flash | Google | 16 | `3.6` | `google/gemini-3.6-flash` |
| 101 | Gemini 3.7 Flash | Google | 16 | `3.7` | `google/gemini-3.7-flash` |
| 101 | Gemini 3.8 Flash | Google | 16 | `3.8` | `google/gemini-3.8-flash` |
| 101 | GPT-5.6 Luna Pro | OpenAI | 16 | `5.6` | `openai/gpt-5.6-luna-pro` |
| 101 | Kimi K2 Thinking | MoonshotAI | 16 | `2` | `moonshotai/kimi-k2-thinking` |
| 101 | Llama 4 Maverick | Meta | 16 | `4` | `meta-llama/llama-4-maverick` |
| 101 | Mistral Medium 3 | Mistral | 16 | `3` | `mistralai/mistral-medium-3` |
| 101 | Muse Glimmer 30B | Meta | 16 | DNQ | `meta/muse-glimmer-30b` |
| 101 | Nemotron 3 Super | NVIDIA | 16 | `3` | `nvidia/nemotron-3-super-120b-a12b` |
| 101 | Nemotron 3 Ultra | NVIDIA | 16 | `3` | `nvidia/nemotron-3-ultra-550b-a55b` |
| 101 | Nova Premier 1.0 | Amazon | 16 | `1.0` | `amazon/nova-premier-v1` |
| 101 | Perceptron Mk1.5 | Perceptron | 16 | `1.5` | `perceptron/perceptron-mk1.5` |
| 101 | Qwen3 Coder Next | Qwen | 16 | `3` | `qwen/qwen3-coder-next` |
| 101 | Sonar Pro Search | Perplexity | 16 | DNQ | `perplexity/sonar-pro-search` |
| 101 | WizardLM-2 8x22B | Microsoft | 16 | `2` | `microsoft/wizardlm-2-8x22b` |
| 124 | Apodex 1.1 Mini | Apodex | 15 | `1.1` | `apodex/apodex-1.1-mini` |
| 124 | Claude Opus 4.1 | Anthropic | 15 | `4.1` | `anthropic/claude-opus-4.1` |
| 124 | Claude Opus 4.5 | Anthropic | 15 | `4.5` | `anthropic/claude-opus-4.5` |
| 124 | Claude Opus 4.6 | Anthropic | 15 | `4.6` | `anthropic/claude-opus-4.6` |
| 124 | Claude Opus 4.7 | Anthropic | 15 | `4.7` | `anthropic/claude-opus-4.7` |
| 124 | Claude Opus 4.8 | Anthropic | 15 | `4.8` | `anthropic/claude-opus-4.8` |
| 124 | Claude Opus 5.5 | Anthropic | 15 | `5.5` | `anthropic/claude-opus-5.5` |
| 124 | Claude Sonnet 4 | Anthropic | 15 | `4` | `anthropic/claude-sonnet-4` |
| 124 | Claude Sonnet 5 | Anthropic | 15 | `5` | `anthropic/claude-sonnet-5` |
| 124 | Devstral 2 2512 | Mistral | 15 | `2` | `mistralai/devstral-2512` |
| 124 | Gemma 4 26B A4B | Google | 15 | `4` | `google/gemma-4-26b-a4b-it` |
| 124 | GPT Chat Latest | OpenAI | 15 | DNQ | `openai/gpt-chat-latest` |
| 124 | GPT-5.6 Sol Pro | OpenAI | 15 | `5.6` | `openai/gpt-5.6-sol-pro` |
| 124 | GPT-6 Astra Pro | OpenAI | 15 | `6` | `openai/gpt-6-astra-pro` |
| 124 | GPT-6.1 Sol Pro | OpenAI | 15 | `6.1` | `openai/gpt-6.1-sol-pro` |
| 124 | MiMo-V2.6-Flash | Xiaomi | 15 | `2.6` | `xiaomi/mimo-v2.6-flash` |
| 124 | Mistral Large 4 | Mistral | 15 | `4` | `mistralai/mistral-large-4-0` |
| 124 | Mistral Small 3 | Mistral | 15 | `3` | `mistralai/mistral-small-24b-instruct-2501` |
| 124 | Mistral Small 4 | Mistral | 15 | `4` | `mistralai/mistral-small-2603` |
| 124 | North Mini Code | Cohere | 15 | DNQ | `cohere/north-mini-code` |
| 124 | Qwen3.5-35B-A3B | Qwen | 15 | `3.5` | `qwen/qwen3.5-35b-a3b` |
| 124 | Qwen3.6 35B A3B | Qwen | 15 | `3.6` | `qwen/qwen3.6-35b-a3b` |
| 146 | Claude Fable 5 | Anthropic | 14 | `5` | `anthropic/claude-fable-5` |
| 146 | Codestral 2508 | Mistral | 14 | DNQ | `mistralai/codestral-2508` |
| 146 | Gemini 2.5 Pro | Google | 14 | `2.5` | `google/gemini-2.5-pro` |
| 146 | GLM 5.3 FlashX | Z.ai | 14 | `5.3` | `z-ai/glm-5.3-flashx` |
| 146 | GPT-6 Luna Pro | OpenAI | 14 | `6` | `openai/gpt-6-luna-pro` |
| 146 | Granite 4.2 8B | IBM | 14 | `4.2` | `ibm-granite/granite-4.2-8b` |
| 146 | Grok Build 0.1 | SpaceXAI | 14 | `0.1` | `x-ai/grok-build-0.1` |
| 146 | Hy-MT2-30B-A3B | Tencent | 14 | `2` | `tencent/hy-mt2-30b-a3b` |
| 146 | Kimi K2.7 Code | MoonshotAI | 14 | `2.7` | `moonshotai/kimi-k2.7-code` |
| 146 | Ling 3.0 Flash | inclusionAI | 14 | `3.0` | `inclusionai/ling-3.0-flash` |
| 146 | Ling 3.1 Flash | inclusionAI | 14 | `3.1` | `inclusionai/ling-3.1-flash` |
| 146 | MiniMax M2-her | MiniMax | 14 | `2` | `minimax/minimax-m2-her` |
| 146 | Morph V3 Large | Morph | 14 | `3` | `morph/morph-v3-large` |
| 146 | Muse Spark 1.1 | Meta | 14 | `1.1` | `meta/muse-spark-1.1` |
| 146 | Muse Spark 1.2 | Meta | 14 | `1.2` | `meta/muse-spark-1.2` |
| 146 | Muse Spark 1.3 | Meta | 14 | `1.3` | `meta/muse-spark-1.3` |
| 146 | Nova Micro 1.0 | Amazon | 14 | `1.0` | `amazon/nova-micro-v1` |
| 146 | Perceptron Mk1 | Perceptron | 14 | `1` | `perceptron/perceptron-mk1` |
| 146 | Relace Apply 3 | Relace | 14 | `3` | `relace/relace-apply-3` |
| 146 | ReMM SLERP 13B | undi95 | 14 | DNQ | `undi95/remm-slerp-l2-13b` |
| 146 | Seed 1.6 Flash | ByteDance Seed | 14 | `1.6` | `bytedance-seed/seed-1.6-flash` |
| 146 | Seed 2.1 Turbo | ByteDance Seed | 14 | `2.1` | `bytedance-seed/seed-2-1-turbo` |
| 146 | Skyfall 36B V2 | TheDrummer | 14 | `2` | `thedrummer/skyfall-36b-v2` |
| 146 | Step 3.5 Flash | StepFun | 14 | `3.5` | `stepfun/step-3.5-flash` |
| 146 | Step 3.7 Flash | StepFun | 14 | `3.7` | `stepfun/step-3.7-flash` |
| 146 | Step 5 Preview | StepFun | 14 | `5` | `stepfun/step-5-preview` |
| 146 | UnslopNemo 12B | TheDrummer | 14 | DNQ | `thedrummer/unslopnemo-12b` |
| 146 | Weaver (alpha) | Mancer | 14 | DNQ | `mancer/weaver` |
| 174 | Aion 3.5 Mini | AionLabs | 13 | `3.5` | `aion-labs/aion-3.5-mini` |
| 174 | Aion-3.0-Mini | AionLabs | 13 | `3.0` | `aion-labs/aion-3.0-mini` |
| 174 | Claude Opus 5 | Anthropic | 13 | `5` | `anthropic/claude-opus-5` |
| 174 | DeepSeek V3.1 | DeepSeek | 13 | `3.1` | `deepseek/deepseek-chat-v3.1` |
| 174 | DeepSeek V3.2 | DeepSeek | 13 | `3.2` | `deepseek/deepseek-v3.2` |
| 174 | Fugu Ultra v2 | Sakana | 13 | `2` | `sakana/fugu-ultra-v2` |
| 174 | GLM 4.7 Flash | Z.ai | 13 | `4.7` | `z-ai/glm-4.7-flash` |
| 174 | GLM 5.3 Flash | Z.ai | 13 | `5.3` | `z-ai/glm-5.3-flash` |
| 174 | GLM 5.3 Prime | Z.ai | 13 | `5.3` | `z-ai/glm-5.3-prime` |
| 174 | GPT-3.5 Turbo | OpenAI | 13 | `3.5` | `openai/gpt-3.5-turbo` |
| 174 | GPT-5.1-Codex | OpenAI | 13 | `5.1` | `openai/gpt-5.1-codex` |
| 174 | GPT-5.2-Codex | OpenAI | 13 | `5.2` | `openai/gpt-5.2-codex` |
| 174 | GPT-5.3-Codex | OpenAI | 13 | `5.3` | `openai/gpt-5.3-codex` |
| 174 | GPT-5.6 Terra | OpenAI | 13 | `5.6` | `openai/gpt-5.6-terra` |
| 174 | GPT-6 Sol Pro | OpenAI | 13 | `6` | `openai/gpt-6-sol-pro` |
| 174 | Hermes 4 405B | Nous | 13 | `4` | `nousresearch/hermes-4-405b` |
| 174 | Inkling Small | Thinking Machines | 13 | DNQ | `thinkingmachines/inkling-small` |
| 174 | Laguna XS 2.1 | Poolside | 13 | `2.1` | `poolside/laguna-xs-2.1` |
| 174 | Llama 4 Scout | Meta | 13 | `4` | `meta-llama/llama-4-scout` |
| 174 | Magnum v4 72B | anthracite-org | 13 | `4` | `anthracite-org/magnum-v4-72b` |
| 174 | MiMo-V2.5-Pro | Xiaomi | 13 | `2.5` | `xiaomi/mimo-v2.5-pro` |
| 174 | MiMo-V2.6-Pro | Xiaomi | 13 | `2.6` | `xiaomi/mimo-v2.6-pro` |
| 174 | Mistral Large | Mistral | 13 | DNQ | `mistralai/mistral-large` |
| 174 | Morph V3 Fast | Morph | 13 | `3` | `morph/morph-v3-fast` |
| 174 | Nex-N2.5-Mini | Nex AGI | 13 | `2.5` | `nex-agi/nex-n2.5-mini` |
| 174 | Nova Lite 1.0 | Amazon | 13 | `1.0` | `amazon/nova-lite-v1` |
| 174 | Qwen3 30B A3B | Qwen | 13 | `3` | `qwen/qwen3-30b-a3b` |
| 174 | Qwen3.5-Flash | Qwen | 13 | `3.5` | `qwen/qwen3.5-flash-02-23` |
| 174 | Qwen3.6 Flash | Qwen | 13 | `3.6` | `qwen/qwen3.6-flash` |
| 174 | Qwen3.7 Flash | Qwen | 13 | `3.7` | `qwen/qwen3.7-flash` |
| 174 | Qwen3.8 Flash | Qwen | 13 | `3.8` | `qwen/qwen3.8-flash` |
| 174 | Relace Search | Relace | 13 | DNQ | `relace/relace-search` |
| 174 | Sakana Namazu | Sakana | 13 | DNQ | `sakana/sakana-namazu` |
| 174 | Seed-2.0-Code | ByteDance Seed | 13 | `2.0` | `bytedance-seed/seed-2.0-code` |
| 174 | Seed-2.0-Lite | ByteDance Seed | 13 | `2.0` | `bytedance-seed/seed-2.0-lite` |
| 174 | Seed-2.0-Mini | ByteDance Seed | 13 | `2.0` | `bytedance-seed/seed-2.0-mini` |
| 210 | GLM 5V Turbo | Z.ai | 12 | `5` | `z-ai/glm-5v-turbo` |
| 210 | GPT-4.1 Mini | OpenAI | 12 | `4.1` | `openai/gpt-4.1-mini` |
| 210 | GPT-4.1 Nano | OpenAI | 12 | `4.1` | `openai/gpt-4.1-nano` |
| 210 | GPT-5.2 Chat | OpenAI | 12 | `5.2` | `openai/gpt-5.2-chat` |
| 210 | GPT-5.4 Mini | OpenAI | 12 | `5.4` | `openai/gpt-5.4-mini` |
| 210 | GPT-5.4 Nano | OpenAI | 12 | `5.4` | `openai/gpt-5.4-nano` |
| 210 | GPT-5.6 Luna | OpenAI | 12 | `5.6` | `openai/gpt-5.6-luna` |
| 210 | gpt-oss-120b | OpenAI | 12 | DNQ | `openai/gpt-oss-120b` |
| 210 | Kimi K2 0711 | MoonshotAI | 12 | `2` | `moonshotai/kimi-k2` |
| 210 | Kimi K2 0905 | MoonshotAI | 12 | `2` | `moonshotai/kimi-k2-0905` |
| 210 | Laguna S 2.1 | Poolside | 12 | `2.1` | `poolside/laguna-s-2.1` |
| 210 | MiniMax M2.1 | MiniMax | 12 | `2.1` | `minimax/minimax-m2.1` |
| 210 | MiniMax M2.5 | MiniMax | 12 | `2.5` | `minimax/minimax-m2.5` |
| 210 | MiniMax M2.7 | MiniMax | 12 | `2.7` | `minimax/minimax-m2.7` |
| 210 | Mistral Nemo | Mistral | 12 | DNQ | `mistralai/mistral-nemo` |
| 210 | MythoMax 13B | gryphe | 12 | DNQ | `gryphe/mythomax-l2-13b` |
| 210 | Nex-N2.5-Pro | Nex AGI | 12 | `2.5` | `nex-agi/nex-n2.5-pro` |
| 210 | Nova Pro 1.0 | Amazon | 12 | `1.0` | `amazon/nova-pro-v1` |
| 210 | o3 Mini High | OpenAI | 12 | `3` | `openai/o3-mini-high` |
| 210 | o4 Mini High | OpenAI | 12 | `4` | `openai/o4-mini-high` |
| 210 | Qwen3.6 Plus | Qwen | 12 | `3.6` | `qwen/qwen3.6-plus` |
| 210 | Qwen3.7 Plus | Qwen | 12 | `3.7` | `qwen/qwen3.7-plus` |
| 210 | Reka Flash 3 | rekaai | 12 | `3` | `rekaai/reka-flash-3` |
| 210 | Solar Mini 4 | Upstage | 12 | `4` | `upstage/solar-mini4` |
| 234 | DeepSeek V3 | DeepSeek | 11 | `3` | `deepseek/deepseek-chat` |
| 234 | Gemma 2 27B | Google | 11 | `2` | `google/gemma-2-27b-it` |
| 234 | Gemma 3 12B | Google | 11 | `3` | `google/gemma-3-12b-it` |
| 234 | Gemma 3 27B | Google | 11 | `3` | `google/gemma-3-27b-it` |
| 234 | Gemma 4 31B | Google | 11 | `4` | `google/gemma-4-31b-it` |
| 234 | GLM 4.5 Air | Z.ai | 11 | `4.5` | `z-ai/glm-4.5-air` |
| 234 | GLM 5 Turbo | Z.ai | 11 | `5` | `z-ai/glm-5-turbo` |
| 234 | GPT-4 Turbo | OpenAI | 11 | `4` | `openai/gpt-4-turbo` |
| 234 | GPT-4o-mini | OpenAI | 11 | `4` | `openai/gpt-4o-mini` |
| 234 | GPT-5.2 Pro | OpenAI | 11 | `5.2` | `openai/gpt-5.2-pro` |
| 234 | GPT-5.4 Pro | OpenAI | 11 | `5.4` | `openai/gpt-5.4-pro` |
| 234 | GPT-5.5 Pro | OpenAI | 11 | `5.5` | `openai/gpt-5.5-pro` |
| 234 | GPT-5.6 Sol | OpenAI | 11 | `5.6` | `openai/gpt-5.6-sol` |
| 234 | GPT-6 Astra | OpenAI | 11 | `6` | `openai/gpt-6-astra` |
| 234 | GPT-6.1 Sol | OpenAI | 11 | `6.1` | `openai/gpt-6.1-sol` |
| 234 | gpt-oss-20b | OpenAI | 11 | DNQ | `openai/gpt-oss-20b` |
| 234 | Hy-MT2-1.8B | Tencent | 11 | `2` | `tencent/hy-mt2-1.8b` |
| 234 | Hy3 preview | Tencent | 11 | `3` | `tencent/hy3-preview` |
| 234 | Hy4 preview | Tencent | 11 | `4` | `tencent/hy4-preview` |
| 234 | LFM2.5-2.6B | LiquidAI | 11 | `2.5` | `liquid/lfm-2.5-2.6b` |
| 234 | LongCat 2.0 | Meituan | 11 | `2.0` | `meituan/longcat-2.0` |
| 234 | Mercury 2.5 | Inception | 11 | `2.5` | `inception/mercury-2.5` |
| 234 | Nova 2 Lite | Amazon | 11 | `2` | `amazon/nova-2-lite-v1` |
| 234 | Qwen3.5-27B | Qwen | 11 | `3.5` | `qwen/qwen3.5-27b` |
| 234 | Qwen3.6 27B | Qwen | 11 | `3.6` | `qwen/qwen3.6-27b` |
| 234 | Qwen3.7 Max | Qwen | 11 | `3.7` | `qwen/qwen3.7-max` |
| 234 | Qwen3.8 27B | Qwen | 11 | `3.8` | `qwen/qwen3.8-27b` |
| 234 | Solar Pro 3 | Upstage | 11 | `3` | `upstage/solar-pro-3` |
| 234 | Solar Pro 4 | Upstage | 11 | `4` | `upstage/solar-pro4` |
| 263 | Command A+ | Cohere | 10 | DNQ | `cohere/command-a-plus` |
| 263 | Fugu Ultra | Sakana | 10 | DNQ | `sakana/fugu-ultra` |
| 263 | Gemma 3 4B | Google | 10 | `3` | `google/gemma-3-4b-it` |
| 263 | GPT-5 Mini | OpenAI | 10 | `5` | `openai/gpt-5-mini` |
| 263 | GPT-5 Nano | OpenAI | 10 | `5` | `openai/gpt-5-nano` |
| 263 | GPT-6 Luna | OpenAI | 10 | `6` | `openai/gpt-6-luna` |
| 263 | MiniMax M1 | MiniMax | 10 | `1` | `minimax/minimax-m1` |
| 263 | MiniMax M2 | MiniMax | 10 | `2` | `minimax/minimax-m2` |
| 263 | MiniMax M3 | MiniMax | 10 | `3` | `minimax/minimax-m3` |
| 263 | MiniMax-01 | MiniMax | 10 | `01` | `minimax/minimax-01` |
| 263 | Palmyra X5 | Writer | 10 | `5` | `writer/palmyra-x5` |
| 263 | Qwen3.5-9B | Qwen | 10 | `3.5` | `qwen/qwen3.5-9b` |
| 263 | UI-TARS 7B | ByteDance | 10 | DNQ | `bytedance/ui-tars-1.5-7b` |
| 263 | Uncensored | Venice | 10 | DNQ | `cognitivecomputations/dolphin-mistral-24b-venice-edition` |
| 277 | Command A | Cohere | 9 | DNQ | `cohere/command-a` |
| 277 | GPT-5 Pro | OpenAI | 9 | `5` | `openai/gpt-5-pro` |
| 277 | GPT-6 Sol | OpenAI | 9 | `6` | `openai/gpt-6-sol` |
| 277 | Grok 4.20 | SpaceXAI | 9 | `4.20` | `x-ai/grok-4.20` |
| 277 | Hy-MT2-7B | Tencent | 9 | `2` | `tencent/hy-mt2-7b` |
| 277 | Kimi K2.5 | MoonshotAI | 9 | `2.5` | `moonshotai/kimi-k2.5` |
| 277 | Kimi K2.6 | MoonshotAI | 9 | `2.6` | `moonshotai/kimi-k2.6` |
| 277 | Mercury 2 | Inception | 9 | `2` | `inception/mercury-2` |
| 277 | MiMo-V2.5 | Xiaomi | 9 | `2.5` | `xiaomi/mimo-v2.5` |
| 277 | Qwen-Plus | Qwen | 9 | DNQ | `qwen/qwen-plus` |
| 277 | Qwen3 14B | Qwen | 9 | `3` | `qwen/qwen3-14b` |
| 277 | Qwen3 32B | Qwen | 9 | `3` | `qwen/qwen3-32b` |
| 277 | Reka Edge | rekaai | 9 | DNQ | `rekaai/reka-edge` |
| 277 | Sonar Pro | Perplexity | 9 | DNQ | `perplexity/sonar-pro` |
| 291 | Aion 3.5 | AionLabs | 8 | `3.5` | `aion-labs/aion-3.5` |
| 291 | Aion-2.0 | AionLabs | 8 | `2.0` | `aion-labs/aion-2.0` |
| 291 | Aion-3.0 | AionLabs | 8 | `3.0` | `aion-labs/aion-3.0` |
| 291 | Fugu Max | Sakana | 8 | DNQ | `sakana/fugu-max` |
| 291 | GLM 4.5V | Z.ai | 8 | `4.5` | `z-ai/glm-4.5v` |
| 291 | GLM 4.6V | Z.ai | 8 | `4.6` | `z-ai/glm-4.6v` |
| 291 | Grok 4.3 | SpaceXAI | 8 | `4.3` | `x-ai/grok-4.3` |
| 291 | Grok 4.5 | SpaceXAI | 8 | `4.5` | `x-ai/grok-4.5` |
| 291 | Grok 4.6 | SpaceXAI | 8 | `4.6` | `x-ai/grok-4.6` |
| 291 | Grok 4.7 | SpaceXAI | 8 | `4.7` | `x-ai/grok-4.7` |
| 291 | Seed 1.6 | ByteDance Seed | 8 | `1.6` | `bytedance-seed/seed-1.6` |
| 302 | Ember-1 | Fireworks | 7 | `1` | `fireworks/ember-1` |
| 302 | GLM 4.5 | Z.ai | 7 | `4.5` | `z-ai/glm-4.5` |
| 302 | GLM 4.6 | Z.ai | 7 | `4.6` | `z-ai/glm-4.6` |
| 302 | GLM 4.7 | Z.ai | 7 | `4.7` | `z-ai/glm-4.7` |
| 302 | GLM 5.1 | Z.ai | 7 | `5.1` | `z-ai/glm-5.1` |
| 302 | GLM 5.2 | Z.ai | 7 | `5.2` | `z-ai/glm-5.2` |
| 302 | GLM 5.3 | Z.ai | 7 | `5.3` | `z-ai/glm-5.3` |
| 302 | GPT-4.1 | OpenAI | 7 | `4.1` | `openai/gpt-4.1` |
| 302 | GPT-5.1 | OpenAI | 7 | `5.1` | `openai/gpt-5.1` |
| 302 | GPT-5.2 | OpenAI | 7 | `5.2` | `openai/gpt-5.2` |
| 302 | GPT-5.4 | OpenAI | 7 | `5.4` | `openai/gpt-5.4` |
| 302 | GPT-5.5 | OpenAI | 7 | `5.5` | `openai/gpt-5.5` |
| 302 | Inkling | Thinking Machines | 7 | DNQ | `thinkingmachines/inkling` |
| 302 | Kimi K3 | MoonshotAI | 7 | `3` | `moonshotai/kimi-k3` |
| 302 | o3 Mini | OpenAI | 7 | `3` | `openai/o3-mini` |
| 302 | o4 Mini | OpenAI | 7 | `4` | `openai/o4-mini` |
| 302 | R1 0528 | DeepSeek | 7 | `1` | `deepseek/deepseek-r1-0528` |
| 319 | GPT-4o | OpenAI | 6 | `4` | `openai/gpt-4o` |
| 319 | o1-pro | OpenAI | 6 | `1` | `openai/o1-pro` |
| 319 | o3 Pro | OpenAI | 6 | `3` | `openai/o3-pro` |
| 319 | Pareto | unbiased | 6 | DNQ | `unbiased/pareto` |
| 323 | GLM 5 | Z.ai | 5 | `5` | `z-ai/glm-5` |
| 323 | GPT-4 | OpenAI | 5 | `4` | `openai/gpt-4` |
| 323 | GPT-5 | OpenAI | 5 | `5` | `openai/gpt-5` |
| 323 | Phi 4 | Microsoft | 5 | `4` | `microsoft/phi-4` |
| 323 | Sonar | Perplexity | 5 | DNQ | `perplexity/sonar` |
| 328 | Saba | Mistral | 4 | DNQ | `mistralai/mistral-saba` |
| 329 | Hy3 | Tencent | 3 | `3` | `tencent/hy3` |
| 330 | o1 | OpenAI | 2 | `1` | `openai/o1` |
| 330 | o3 | OpenAI | 2 | `3` | `openai/o3` |
| 330 | R1 | DeepSeek | 2 | `1` | `deepseek/deepseek-r1` |

### 2.1 Brevity Prize (shortest names)

| Model | Vendor | NL |
| :-- | :-- | --: |
| o1 | OpenAI | 2 |
| o3 | OpenAI | 2 |
| R1 | DeepSeek | 2 |
| Hy3 | Tencent | 3 |
| Saba | Mistral | 4 |
| GLM 5 | Z.ai | 5 |
| GPT-4 | OpenAI | 5 |
| GPT-5 | OpenAI | 5 |
| Phi 4 | Microsoft | 5 |
| Sonar | Perplexity | 5 |

## 3. Auxiliary Track: Nomenclatural Efficiency (NE = GI / NL) ↑

Generations delivered per character of name. All 292 GI-qualified models.

| Rank | Model | Vendor | GI | NL | NE |
| --: | :-- | :-- | --: | --: | --: |
| 🥇 1 | o3 | OpenAI | `3` | 2 | 1.5000 |
| 🥈 2 | Pareto 26.10 Preview | unbiased | `26.10` | 20 | 1.3050 |
| 🥉 3 | GLM 5 | Z.ai | `5` | 5 | 1.0000 |
| 🥉 3 | GPT-5 | OpenAI | `5` | 5 | 1.0000 |
| 🥉 3 | Hy3 | Tencent | `3` | 3 | 1.0000 |
| 6 | GPT-4 | OpenAI | `4` | 5 | 0.8000 |
| 6 | Phi 4 | Microsoft | `4` | 5 | 0.8000 |
| 8 | GPT-5.5 | OpenAI | `5.5` | 7 | 0.7857 |
| 9 | GPT-5.4 | OpenAI | `5.4` | 7 | 0.7714 |
| 10 | GLM 5.3 | Z.ai | `5.3` | 7 | 0.7571 |
| 11 | GLM 5.2 | Z.ai | `5.2` | 7 | 0.7429 |
| 11 | GPT-5.2 | OpenAI | `5.2` | 7 | 0.7429 |
| 13 | GLM 5.1 | Z.ai | `5.1` | 7 | 0.7286 |
| 13 | GPT-5.1 | OpenAI | `5.1` | 7 | 0.7286 |
| 15 | GLM 4.7 | Z.ai | `4.7` | 7 | 0.6714 |
| 16 | GPT-4o | OpenAI | `4` | 6 | 0.6667 |
| 16 | GPT-6 Sol | OpenAI | `6` | 9 | 0.6667 |
| 18 | GLM 4.6 | Z.ai | `4.6` | 7 | 0.6571 |
| 19 | GLM 4.5 | Z.ai | `4.5` | 7 | 0.6429 |
| 20 | GPT-6 Luna | OpenAI | `6` | 10 | 0.6000 |
| 21 | Grok 4.7 | SpaceXAI | `4.7` | 8 | 0.5875 |
| 22 | GPT-4.1 | OpenAI | `4.1` | 7 | 0.5857 |
| 23 | GLM 4.6V | Z.ai | `4.6` | 8 | 0.5750 |
| 23 | Grok 4.6 | SpaceXAI | `4.6` | 8 | 0.5750 |
| 25 | o4 Mini | OpenAI | `4` | 7 | 0.5714 |
| 26 | GLM 4.5V | Z.ai | `4.5` | 8 | 0.5625 |
| 26 | Grok 4.5 | SpaceXAI | `4.5` | 8 | 0.5625 |
| 28 | GPT-5 Pro | OpenAI | `5` | 9 | 0.5556 |
| 29 | GPT-6.1 Sol | OpenAI | `6.1` | 11 | 0.5545 |
| 30 | GPT-6 Astra | OpenAI | `6` | 11 | 0.5455 |
| 31 | Grok 4.3 | SpaceXAI | `4.3` | 8 | 0.5375 |
| 32 | GPT-5.6 Sol | OpenAI | `5.6` | 11 | 0.5091 |
| 33 | GPT-5 Mini | OpenAI | `5` | 10 | 0.5000 |
| 33 | GPT-5 Nano | OpenAI | `5` | 10 | 0.5000 |
| 33 | GPT-5.5 Pro | OpenAI | `5.5` | 11 | 0.5000 |
| 33 | o1 | OpenAI | `1` | 2 | 0.5000 |
| 33 | o3 Pro | OpenAI | `3` | 6 | 0.5000 |
| 33 | Palmyra X5 | Writer | `5` | 10 | 0.5000 |
| 33 | R1 | DeepSeek | `1` | 2 | 0.5000 |
| 40 | GPT-5.4 Pro | OpenAI | `5.4` | 11 | 0.4909 |
| 41 | GPT-5.2 Pro | OpenAI | `5.2` | 11 | 0.4727 |
| 42 | GPT-5.6 Luna | OpenAI | `5.6` | 12 | 0.4667 |
| 42 | Grok 4.20 | SpaceXAI | `4.20` | 9 | 0.4667 |
| 44 | GPT-6 Sol Pro | OpenAI | `6` | 13 | 0.4615 |
| 45 | GLM 5 Turbo | Z.ai | `5` | 11 | 0.4545 |
| 46 | GPT-5.4 Mini | OpenAI | `5.4` | 12 | 0.4500 |
| 46 | GPT-5.4 Nano | OpenAI | `5.4` | 12 | 0.4500 |
| 48 | Aion 3.5 | AionLabs | `3.5` | 8 | 0.4375 |
| 49 | GPT-5.2 Chat | OpenAI | `5.2` | 12 | 0.4333 |
| 50 | GPT-5.6 Terra | OpenAI | `5.6` | 13 | 0.4308 |
| 51 | GPT-6 Luna Pro | OpenAI | `6` | 14 | 0.4286 |
| 51 | Kimi K3 | MoonshotAI | `3` | 7 | 0.4286 |
| 51 | o3 Mini | OpenAI | `3` | 7 | 0.4286 |
| 54 | GLM 5V Turbo | Z.ai | `5` | 12 | 0.4167 |
| 55 | GLM 4.5 Air | Z.ai | `4.5` | 11 | 0.4091 |
| 56 | GLM 5.3 Flash | Z.ai | `5.3` | 13 | 0.4077 |
| 56 | GLM 5.3 Prime | Z.ai | `5.3` | 13 | 0.4077 |
| 56 | GPT-5.3-Codex | OpenAI | `5.3` | 13 | 0.4077 |
| 59 | GPT-6.1 Sol Pro | OpenAI | `6.1` | 15 | 0.4067 |
| 60 | GPT-5.2-Codex | OpenAI | `5.2` | 13 | 0.4000 |
| 60 | GPT-6 Astra Pro | OpenAI | `6` | 15 | 0.4000 |
| 62 | GPT-5.1-Codex | OpenAI | `5.1` | 13 | 0.3923 |
| 63 | Claude Opus 5 | Anthropic | `5` | 13 | 0.3846 |
| 64 | GLM 5.3 FlashX | Z.ai | `5.3` | 14 | 0.3786 |
| 65 | Aion-3.0 | AionLabs | `3.0` | 8 | 0.3750 |
| 66 | GPT-5.6 Sol Pro | OpenAI | `5.6` | 15 | 0.3733 |
| 67 | Claude Opus 5.5 | Anthropic | `5.5` | 15 | 0.3667 |
| 68 | Gemma 4 31B | Google | `4` | 11 | 0.3636 |
| 68 | GPT-4 Turbo | OpenAI | `4` | 11 | 0.3636 |
| 68 | GPT-4o-mini | OpenAI | `4` | 11 | 0.3636 |
| 68 | Hy4 preview | Tencent | `4` | 11 | 0.3636 |
| 68 | Solar Pro 4 | Upstage | `4` | 11 | 0.3636 |
| 73 | GLM 4.7 Flash | Z.ai | `4.7` | 13 | 0.3615 |
| 74 | Claude Fable 5 | Anthropic | `5` | 14 | 0.3571 |
| 74 | Step 5 Preview | StepFun | `5` | 14 | 0.3571 |
| 76 | GPT-5.6 Luna Pro | OpenAI | `5.6` | 16 | 0.3500 |
| 76 | Qwen3.5-9B | Qwen | `3.5` | 10 | 0.3500 |
| 78 | Qwen3.8 27B | Qwen | `3.8` | 11 | 0.3455 |
| 79 | Claude Haiku 5.5 | Anthropic | `5.5` | 16 | 0.3438 |
| 80 | GPT-4.1 Mini | OpenAI | `4.1` | 12 | 0.3417 |
| 80 | GPT-4.1 Nano | OpenAI | `4.1` | 12 | 0.3417 |
| 82 | Qwen3.7 Max | Qwen | `3.7` | 11 | 0.3364 |
| 83 | Claude Sonnet 5 | Anthropic | `5` | 15 | 0.3333 |
| 83 | o4 Mini High | OpenAI | `4` | 12 | 0.3333 |
| 83 | Qwen3 14B | Qwen | `3` | 9 | 0.3333 |
| 83 | Qwen3 32B | Qwen | `3` | 9 | 0.3333 |
| 83 | Solar Mini 4 | Upstage | `4` | 12 | 0.3333 |
| 88 | GPT-5.6 Terra Pro | OpenAI | `5.6` | 17 | 0.3294 |
| 89 | Qwen3.6 27B | Qwen | `3.6` | 11 | 0.3273 |
| 90 | Claude Sonnet 5.5 | Anthropic | `5.5` | 17 | 0.3235 |
| 91 | Claude Opus 4.8 | Anthropic | `4.8` | 15 | 0.3200 |
| 92 | Claude Fable 5.1 | Anthropic | `5.1` | 16 | 0.3187 |
| 93 | Qwen3.5-27B | Qwen | `3.5` | 11 | 0.3182 |
| 94 | Claude Opus 4.7 | Anthropic | `4.7` | 15 | 0.3133 |
| 95 | Qwen3.7 Plus | Qwen | `3.7` | 12 | 0.3083 |
| 96 | Hermes 4 405B | Nous | `4` | 13 | 0.3077 |
| 96 | Llama 4 Scout | Meta | `4` | 13 | 0.3077 |
| 96 | Magnum v4 72B | anthracite-org | `4` | 13 | 0.3077 |
| 99 | Claude Opus 4.6 | Anthropic | `4.6` | 15 | 0.3067 |
| 100 | Claude Opus 4.5 | Anthropic | `4.5` | 15 | 0.3000 |
| 100 | Gemma 3 4B | Google | `3` | 10 | 0.3000 |
| 100 | GPT-5.1-Codex-Max | OpenAI | `5.1` | 17 | 0.3000 |
| 100 | Granite 4.2 8B | IBM | `4.2` | 14 | 0.3000 |
| 100 | MiniMax M3 | MiniMax | `3` | 10 | 0.3000 |
| 100 | Qwen3.6 Plus | Qwen | `3.6` | 12 | 0.3000 |
| 106 | Qwen3.8 Flash | Qwen | `3.8` | 13 | 0.2923 |
| 107 | Kimi K2.6 | MoonshotAI | `2.6` | 9 | 0.2889 |
| 108 | Qwen3.7 Flash | Qwen | `3.7` | 13 | 0.2846 |
| 109 | GPT-5.1-Codex-Mini | OpenAI | `5.1` | 18 | 0.2833 |
| 110 | Claude Haiku 4.5 | Anthropic | `4.5` | 16 | 0.2812 |
| 111 | Kimi K2.5 | MoonshotAI | `2.5` | 9 | 0.2778 |
| 111 | MiMo-V2.5 | Xiaomi | `2.5` | 9 | 0.2778 |
| 113 | Qwen3.6 Flash | Qwen | `3.6` | 13 | 0.2769 |
| 114 | Claude Opus 4.1 | Anthropic | `4.1` | 15 | 0.2733 |
| 115 | DeepSeek V3 | DeepSeek | `3` | 11 | 0.2727 |
| 115 | Gemma 3 12B | Google | `3` | 11 | 0.2727 |
| 115 | Gemma 3 27B | Google | `3` | 11 | 0.2727 |
| 115 | Hy3 preview | Tencent | `3` | 11 | 0.2727 |
| 115 | Solar Pro 3 | Upstage | `3` | 11 | 0.2727 |
| 120 | Claude Sonnet 4.6 | Anthropic | `4.6` | 17 | 0.2706 |
| 121 | Aion 3.5 Mini | AionLabs | `3.5` | 13 | 0.2692 |
| 121 | GPT-3.5 Turbo | OpenAI | `3.5` | 13 | 0.2692 |
| 121 | Qwen3.5-Flash | Qwen | `3.5` | 13 | 0.2692 |
| 124 | Claude Sonnet 4 | Anthropic | `4` | 15 | 0.2667 |
| 124 | Gemma 4 26B A4B | Google | `4` | 15 | 0.2667 |
| 124 | Mistral Large 4 | Mistral | `4` | 15 | 0.2667 |
| 124 | Mistral Small 4 | Mistral | `4` | 15 | 0.2667 |
| 128 | Claude Sonnet 4.5 | Anthropic | `4.5` | 17 | 0.2647 |
| 129 | Step 3.7 Flash | StepFun | `3.7` | 14 | 0.2643 |
| 130 | Cydonia 24B V4.1 | TheDrummer | `4.1` | 16 | 0.2562 |
| 131 | Aion-2.0 | AionLabs | `2.0` | 8 | 0.2500 |
| 131 | Llama 4 Maverick | Meta | `4` | 16 | 0.2500 |
| 131 | o3 Mini High | OpenAI | `3` | 12 | 0.2500 |
| 131 | Reka Flash 3 | rekaai | `3` | 12 | 0.2500 |
| 131 | Step 3.5 Flash | StepFun | `3.5` | 14 | 0.2500 |
| 136 | DeepSeek V3.2 | DeepSeek | `3.2` | 13 | 0.2462 |
| 137 | Qwen3.6 35B A3B | Qwen | `3.6` | 15 | 0.2400 |
| 138 | DeepSeek V3.1 | DeepSeek | `3.1` | 13 | 0.2385 |
| 139 | Gemini 3.8 Flash | Google | `3.8` | 16 | 0.2375 |
| 140 | Granite 4.0 Micro | IBM | `4.0` | 17 | 0.2353 |
| 140 | Llama Guard 4 12B | Meta | `4` | 17 | 0.2353 |
| 142 | Qwen3.5-35B-A3B | Qwen | `3.5` | 15 | 0.2333 |
| 143 | Gemini 3.7 Flash | Google | `3.7` | 16 | 0.2313 |
| 144 | Aion-3.0-Mini | AionLabs | `3.0` | 13 | 0.2308 |
| 144 | Morph V3 Fast | Morph | `3` | 13 | 0.2308 |
| 144 | Qwen3 30B A3B | Qwen | `3` | 13 | 0.2308 |
| 147 | LFM2.5-2.6B | LiquidAI | `2.5` | 11 | 0.2273 |
| 147 | Mercury 2.5 | Inception | `2.5` | 11 | 0.2273 |
| 149 | Gemini 3.6 Flash | Google | `3.6` | 16 | 0.2250 |
| 149 | MiniMax M2.7 | MiniMax | `2.7` | 12 | 0.2250 |
| 151 | Qwen3.8 2.4T A95B | Qwen | `3.8` | 17 | 0.2235 |
| 151 | Qwen3.8 Max Prime | Qwen | `3.8` | 17 | 0.2235 |
| 153 | Hy-MT2-7B | Tencent | `2` | 9 | 0.2222 |
| 153 | Mercury 2 | Inception | `2` | 9 | 0.2222 |
| 155 | Ling 3.1 Flash | inclusionAI | `3.1` | 14 | 0.2214 |
| 156 | Gemini 3.5 Flash | Google | `3.5` | 16 | 0.2188 |
| 157 | DeepSeek V4.1 Flash | DeepSeek | `4.1` | 19 | 0.2158 |
| 158 | Ling 3.0 Flash | inclusionAI | `3.0` | 14 | 0.2143 |
| 158 | Morph V3 Large | Morph | `3` | 14 | 0.2143 |
| 158 | Relace Apply 3 | Relace | `3` | 14 | 0.2143 |
| 161 | Qwen3.8 Max (0902) | Qwen | `3.8` | 18 | 0.2111 |
| 161 | Qwen3.8 Omni Flash | Qwen | `3.8` | 18 | 0.2111 |
| 163 | GPT-4o (2024-05-13) | OpenAI | `4` | 19 | 0.2105 |
| 163 | GPT-4o (2024-08-06) | OpenAI | `4` | 19 | 0.2105 |
| 163 | GPT-4o (2024-11-20) | OpenAI | `4` | 19 | 0.2105 |
| 166 | MiniMax M2.5 | MiniMax | `2.5` | 12 | 0.2083 |
| 166 | Nex-N2.5-Pro | Nex AGI | `2.5` | 12 | 0.2083 |
| 168 | GPT-3.5 Turbo 16k | OpenAI | `3.5` | 17 | 0.2059 |
| 168 | Qwen3.5 397B A17B | Qwen | `3.5` | 17 | 0.2059 |
| 168 | Qwen3.5-122B-A10B | Qwen | `3.5` | 17 | 0.2059 |
| 171 | DeepSeek V4 Pro 0423 | DeepSeek | `4` | 20 | 0.2000 |
| 171 | DeepSeek V4 Pro 0813 | DeepSeek | `4` | 20 | 0.2000 |
| 171 | Grok 4.20 Multi-Agent | SpaceXAI | `4.20` | 21 | 0.2000 |
| 171 | MiMo-V2.6-Pro | Xiaomi | `2.6` | 13 | 0.2000 |
| 171 | MiniMax M2 | MiniMax | `2` | 10 | 0.2000 |
| 171 | Mistral Small 3 | Mistral | `3` | 15 | 0.2000 |
| 171 | Seed 1.6 | ByteDance Seed | `1.6` | 8 | 0.2000 |
| 178 | Mistral Medium 3.5 | Mistral | `3.5` | 18 | 0.1944 |
| 179 | Kimi K2.7 Code | MoonshotAI | `2.7` | 14 | 0.1929 |
| 180 | MiMo-V2.5-Pro | Xiaomi | `2.5` | 13 | 0.1923 |
| 180 | Nex-N2.5-Mini | Nex AGI | `2.5` | 13 | 0.1923 |
| 182 | DeepSeek V3.2 Exp | DeepSeek | `3.2` | 17 | 0.1882 |
| 183 | DeepSeek V3 0324 | DeepSeek | `3` | 16 | 0.1875 |
| 183 | Mistral Medium 3 | Mistral | `3` | 16 | 0.1875 |
| 183 | Nemotron 3 Super | NVIDIA | `3` | 16 | 0.1875 |
| 183 | Nemotron 3 Ultra | NVIDIA | `3` | 16 | 0.1875 |
| 183 | Qwen3 Coder Next | Qwen | `3` | 16 | 0.1875 |
| 188 | DeepSeek V4 Flash 0423 | DeepSeek | `4` | 22 | 0.1818 |
| 188 | DeepSeek V4 Flash 0731 | DeepSeek | `4` | 22 | 0.1818 |
| 188 | Gemma 2 27B | Google | `2` | 11 | 0.1818 |
| 188 | Hy-MT2-1.8B | Tencent | `2` | 11 | 0.1818 |
| 188 | LongCat 2.0 | Meituan | `2.0` | 11 | 0.1818 |
| 188 | Nova 2 Lite | Amazon | `2` | 11 | 0.1818 |
| 194 | Gemini 2.5 Pro | Google | `2.5` | 14 | 0.1786 |
| 195 | Ling 3.0 Flash VL | inclusionAI | `3.0` | 17 | 0.1765 |
| 195 | Qwen3 Coder Flash | Qwen | `3` | 17 | 0.1765 |
| 197 | Laguna S 2.1 | Poolside | `2.1` | 12 | 0.1750 |
| 197 | MiniMax M2.1 | MiniMax | `2.1` | 12 | 0.1750 |
| 199 | MiMo-V2.6-Flash | Xiaomi | `2.6` | 15 | 0.1733 |
| 200 | Mistral Medium 3.1 | Mistral | `3.1` | 18 | 0.1722 |
| 201 | Dots3-Note Preview | Dots Studio | `3` | 18 | 0.1667 |
| 201 | Gemini 3.5 Flash Lite | Google | `3.5` | 21 | 0.1667 |
| 201 | GPT-4o-mini (2024-07-18) | OpenAI | `4` | 24 | 0.1667 |
| 201 | Kimi K2 0711 | MoonshotAI | `2` | 12 | 0.1667 |
| 201 | Kimi K2 0905 | MoonshotAI | `2` | 12 | 0.1667 |
| 201 | Ling 3.0 Flash Fin | inclusionAI | `3.0` | 18 | 0.1667 |
| 201 | Llama 3 8B Lunaris | Sao10K | `3` | 18 | 0.1667 |
| 201 | o1-pro | OpenAI | `1` | 6 | 0.1667 |
| 209 | Laguna XS 2.1 | Poolside | `2.1` | 13 | 0.1615 |
| 210 | GPT-3.5 Turbo Instruct | OpenAI | `3.5` | 22 | 0.1591 |
| 210 | Nemotron 3.5 Lightning | NVIDIA | `3.5` | 22 | 0.1591 |
| 212 | Ministral 3 3B 2512 | Mistral | `3` | 19 | 0.1579 |
| 212 | Ministral 3 8B 2512 | Mistral | `3` | 19 | 0.1579 |
| 214 | Llama 3.3 Euryale 70B | Sao10K | `3.3` | 21 | 0.1571 |
| 215 | Gemini 2.5 Flash | Google | `2.5` | 16 | 0.1562 |
| 216 | Fugu Ultra v2 | Sakana | `2` | 13 | 0.1538 |
| 216 | Seed-2.0-Code | ByteDance Seed | `2.0` | 13 | 0.1538 |
| 216 | Seed-2.0-Lite | ByteDance Seed | `2.0` | 13 | 0.1538 |
| 216 | Seed-2.0-Mini | ByteDance Seed | `2.0` | 13 | 0.1538 |
| 220 | Llama 3.2 1B Instruct | Meta | `3.2` | 21 | 0.1524 |
| 220 | Llama 3.2 3B Instruct | Meta | `3.2` | 21 | 0.1524 |
| 220 | Mistral Small 3.2 24B | Mistral | `3.2` | 21 | 0.1524 |
| 223 | Qwen3.5 Plus 2026-02-15 | Qwen | `3.5` | 23 | 0.1522 |
| 223 | Qwen3.5 Plus 2026-04-20 | Qwen | `3.5` | 23 | 0.1522 |
| 225 | Ling 3.0 Flash Sante | inclusionAI | `3.0` | 20 | 0.1500 |
| 225 | Llama 3.3 70B Instruct | Meta | `3.3` | 22 | 0.1500 |
| 225 | Ministral 3 14B 2512 | Mistral | `3` | 20 | 0.1500 |
| 225 | Mistral Large 3 2512 | Mistral | `3` | 20 | 0.1500 |
| 225 | Nemotron 3 Nano Omni | NVIDIA | `3` | 20 | 0.1500 |
| 225 | Qwen3 VL 8B Instruct | Qwen | `3` | 20 | 0.1500 |
| 225 | Seed 2.1 Turbo | ByteDance Seed | `2.1` | 14 | 0.1500 |
| 232 | Gemini 3.1 Flash Lite | Google | `3.1` | 21 | 0.1476 |
| 232 | Llama 3.1 8B Instruct | Meta | `3.1` | 21 | 0.1476 |
| 232 | Mistral Small 3.1 24B | Mistral | `3.1` | 21 | 0.1476 |
| 235 | DeepSeek V4 Flash Vision Exp | DeepSeek | `4` | 28 | 0.1429 |
| 235 | Ember-1 | Fireworks | `1` | 7 | 0.1429 |
| 235 | Hermes 3 70B Instruct | Nous | `3` | 21 | 0.1429 |
| 235 | Hy-MT2-30B-A3B | Tencent | `2` | 14 | 0.1429 |
| 235 | MiniMax M2-her | MiniMax | `2` | 14 | 0.1429 |
| 235 | Qwen3 Coder 480B A35B | Qwen | `3` | 21 | 0.1429 |
| 235 | R1 0528 | DeepSeek | `1` | 7 | 0.1429 |
| 235 | Skyfall 36B V2 | TheDrummer | `2` | 14 | 0.1429 |
| 243 | DeepSeek V3.1 Terminus | DeepSeek | `3.1` | 22 | 0.1409 |
| 243 | Gemini 3.1 Pro Preview | Google | `3.1` | 22 | 0.1409 |
| 243 | Llama 3.1 70B Instruct | Meta | `3.1` | 22 | 0.1409 |
| 246 | Gemini 3 Flash Preview | Google | `3` | 22 | 0.1364 |
| 246 | Hermes 3 405B Instruct | Nous | `3` | 22 | 0.1364 |
| 248 | Devstral 2 2512 | Mistral | `2` | 15 | 0.1333 |
| 249 | Qwen2.5 7B Instruct | Qwen | `2.5` | 19 | 0.1316 |
| 250 | Nemotron 3 Nano 30B A3B | NVIDIA | `3` | 23 | 0.1304 |
| 251 | GPT-3.5 Turbo (older v0613) | OpenAI | `3.5` | 27 | 0.1296 |
| 251 | Nemotron 3.5 Content Safety | NVIDIA | `3.5` | 27 | 0.1296 |
| 253 | Kimi K2 Thinking | MoonshotAI | `2` | 16 | 0.1250 |
| 253 | Qwen2.5 72B Instruct | Qwen | `2.5` | 20 | 0.1250 |
| 253 | WizardLM-2 8x22B | Microsoft | `2` | 16 | 0.1250 |
| 256 | Qwen3 VL 30B A3B Instruct | Qwen | `3` | 25 | 0.1200 |
| 256 | Qwen3 VL 30B A3B Thinking | Qwen | `3` | 25 | 0.1200 |
| 258 | Llama 3.1 Euryale 70B v2.2 | Sao10K | `3.1` | 26 | 0.1192 |
| 259 | Gemini 2.5 Flash Lite | Google | `2.5` | 21 | 0.1190 |
| 260 | Seed 1.6 Flash | ByteDance Seed | `1.6` | 14 | 0.1143 |
| 261 | Qwen3 30B A3B Instruct 2507 | Qwen | `3` | 27 | 0.1111 |
| 261 | Qwen3 Next 80B A3B Instruct | Qwen | `3` | 27 | 0.1111 |
| 261 | Qwen3 Next 80B A3B Thinking | Qwen | `3` | 27 | 0.1111 |
| 261 | Qwen3 VL 235B A22B Instruct | Qwen | `3` | 27 | 0.1111 |
| 265 | Qwen2.5 VL 72B Instruct | Qwen | `2.5` | 23 | 0.1087 |
| 266 | MiMo-V2.6-Pro-UltraSpeed | Xiaomi | `2.6` | 24 | 0.1083 |
| 267 | Qwen3 Coder 30B A3B Instruct | Qwen | `3` | 28 | 0.1071 |
| 268 | Gemini 3.1 Flash Lite Preview | Google | `3.1` | 29 | 0.1069 |
| 269 | Schematron V2 Small | Inference.net | `2` | 19 | 0.1053 |
| 269 | Schematron V2 Turbo | Inference.net | `2` | 19 | 0.1053 |
| 271 | Qwen3 235B A22B Instruct 2507 | Qwen | `3` | 29 | 0.1034 |
| 271 | Qwen3 235B A22B Thinking 2507 | Qwen | `3` | 29 | 0.1034 |
| 273 | MiniMax M1 | MiniMax | `1` | 10 | 0.1000 |
| 273 | MiniMax-01 | MiniMax | `01` | 10 | 0.1000 |
| 273 | Ternary Bonsai 2 27B | PrismML | `2` | 20 | 0.1000 |
| 276 | Qwen2.5 Coder 32B Instruct | Qwen | `2.5` | 26 | 0.0962 |
| 277 | Perceptron Mk1.5 | Perceptron | `1.5` | 16 | 0.0938 |
| 278 | Muse Spark 1.3 | Meta | `1.3` | 14 | 0.0929 |
| 279 | Gemini 2.5 Pro Preview 06-05 | Google | `2.5` | 28 | 0.0893 |
| 280 | Gemini 3.1 Pro Preview Custom Tools | Google | `3.1` | 35 | 0.0886 |
| 281 | Muse Spark 1.2 | Meta | `1.2` | 14 | 0.0857 |
| 282 | Nova Pro 1.0 | Amazon | `1.0` | 12 | 0.0833 |
| 283 | Muse Spark 1.1 | Meta | `1.1` | 14 | 0.0786 |
| 284 | Nova Lite 1.0 | Amazon | `1.0` | 13 | 0.0769 |
| 285 | Apodex 1.1 Mini | Apodex | `1.1` | 15 | 0.0733 |
| 286 | Nova Micro 1.0 | Amazon | `1.0` | 14 | 0.0714 |
| 286 | Perceptron Mk1 | Perceptron | `1` | 14 | 0.0714 |
| 288 | Aion-RP 1.0 (8B) | AionLabs | `1.0` | 16 | 0.0625 |
| 288 | Nova Premier 1.0 | Amazon | `1.0` | 16 | 0.0625 |
| 290 | Muse Spark 1.3 Contributor | Meta | `1.3` | 26 | 0.0500 |
| 291 | Muse Spark 1.2 Contributor | Meta | `1.2` | 26 | 0.0462 |
| 292 | Grok Build 0.1 | SpaceXAI | `0.1` | 14 | 0.0071 |

## 4. Vendor Analysis

Vendors with at least 3 evaluated models. *Velocity* is the OLS slope of GI against listing date (generations per year).

| Vendor | Models | GI coverage | Max GI | Median GI | Mean NL | Velocity |
| :-- | --: | --: | --: | --: | --: | --: |
| OpenAI | 60 | 93% | 6.1 | 5.1 | 12.1 | +0.92 |
| Anthropic | 16 | 100% | 5.5 | 4.75 | 15.4 | +0.99 |
| Z.ai | 16 | 100% | 5.3 | 5 | 9.4 | +0.77 |
| StepFun | 3 | 100% | 5 | 3.7 | 14.0 | +2.20 |
| SpaceXAI | 7 | 100% | 4.7 | 4.3 | 10.9 | +2.16 |
| DeepSeek | 14 | 100% | 4.1 | 3.2 | 16.6 | +1.32 |
| TheDrummer | 3 | 67% | 4.1 | 3.05 | 14.7 | — |
| Google | 20 | 100% | 4 | 3.1 | 18.1 | +0.74 |
| Mistral | 20 | 65% | 4 | 3 | 16.9 | +0.49 |
| Meta | 14 | 93% | 4 | 3.1 | 18.8 | -1.13 |
| Tencent | 7 | 86% | 4 | 2.5 | 11.4 | -1.29 |
| Nous | 3 | 100% | 4 | 3 | 18.7 | +0.98 |
| Upstage | 3 | 100% | 4 | 4 | 11.3 | +1.63 |
| Qwen | 42 | 98% | 3.8 | 3.5 | 18.0 | +0.72 |
| NVIDIA | 6 | 100% | 3.5 | 3 | 20.7 | +0.76 |
| AionLabs | 6 | 100% | 3.5 | 3 | 11.0 | +1.53 |
| Sao10K | 3 | 100% | 3.3 | 3.1 | 21.7 | +0.79 |
| inclusionAI | 5 | 100% | 3.1 | 3 | 16.6 | +0.43 |
| MiniMax | 8 | 100% | 3 | 2.05 | 11.2 | +1.56 |
| MoonshotAI | 7 | 100% | 3 | 2.5 | 11.3 | +0.99 |
| Xiaomi | 5 | 100% | 2.6 | 2.6 | 14.8 | +0.24 |
| ByteDance Seed | 6 | 100% | 2.1 | 2 | 12.5 | +0.61 |
| Amazon | 5 | 100% | 2 | 1 | 13.2 | +0.57 |
| Sakana | 4 | 25% | 2 | 2 | 11.0 | — |
| Cohere | 6 | 0% | — | — | 15.7 | — |
| Perplexity | 5 | 0% | — | — | 13.6 | — |

## 5. Did Not Qualify (DNQ) for Track A

These models are served on OpenRouter but carry no generation number in their name. They are still scored on Track B.

Codestral 2508 (`mistralai/codestral-2508`), Command A (`cohere/command-a`), Command A+ (`cohere/command-a-plus`), Command R (08-2024) (`cohere/command-r-08-2024`), Command R+ (08-2024) (`cohere/command-r-plus-08-2024`), Command R7B (12-2024) (`cohere/command-r7b-12-2024`), Fugu Max (`sakana/fugu-max`), Fugu Ultra (`sakana/fugu-ultra`), GPT Chat Latest (`openai/gpt-chat-latest`), gpt-oss-120b (`openai/gpt-oss-120b`), gpt-oss-20b (`openai/gpt-oss-20b`), gpt-oss-safeguard-20b (`openai/gpt-oss-safeguard-20b`), Hunyuan A13B Instruct (`tencent/hunyuan-a13b-instruct`), Inkling (`thinkingmachines/inkling`), Inkling Small (`thinkingmachines/inkling-small`), Mistral Large (`mistralai/mistral-large`), Mistral Large 2407 (`mistralai/mistral-large-2407`), Mistral Nemo (`mistralai/mistral-nemo`), Mixtral 8x22B Instruct (`mistralai/mixtral-8x22b-instruct`), Muse Glimmer 30B (`meta/muse-glimmer-30b`), MythoMax 13B (`gryphe/mythomax-l2-13b`), North Mini Code (`cohere/north-mini-code`), Pareto (`unbiased/pareto`), Qwen-Plus (`qwen/qwen-plus`), Reka Edge (`rekaai/reka-edge`), Relace Search (`relace/relace-search`), ReMM SLERP 13B (`undi95/remm-slerp-l2-13b`), Saba (`mistralai/mistral-saba`), Sakana Namazu (`sakana/sakana-namazu`), Sonar (`perplexity/sonar`), Sonar Deep Research (`perplexity/sonar-deep-research`), Sonar Pro (`perplexity/sonar-pro`), Sonar Pro Search (`perplexity/sonar-pro-search`), Sonar Reasoning Pro (`perplexity/sonar-reasoning-pro`), Trinity Large Thinking (`arcee-ai/trinity-large-thinking`), UI-TARS 7B (`bytedance/ui-tars-1.5-7b`), Uncensored (`cognitivecomputations/dolphin-mistral-24b-venice-edition`), UnslopNemo 12B (`thedrummer/unslopnemo-12b`), Voxtral Small 24B 2507 (`mistralai/voxtral-small-24b-2507`), Weaver (alpha) (`mancer/weaver`)

## 6. Figures

![Vendor champions](figures/vendor_champions.svg)

Complete per-model bar charts: [Track A (GI)](figures/full_gi.svg) · [Track B (NL)](figures/full_nl.svg)

![Figure 1](figures/gi_over_time.svg)

![Figure 2](figures/gi_vs_nl.svg)

---

Full per-model data: [`latest.csv`](latest.csv) · [`latest.json`](latest.json)
