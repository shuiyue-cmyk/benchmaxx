# BenchMaxx Leaderboard

> Snapshot **2026-10-17** · protocol v1.0 · BenchMaxx v1.0.0 · source: OpenRouter public API

## 0. Census

| Quantity | Value |
| :-- | --: |
| Catalogue entries (all slugs) | 470 |
| Excluded (alias / router / non-text output) | 41 |
| Eligible models (after collapsing `:free`, `:batch`, … variants) | 340 |
| Failed callability check (0 live endpoints) | 0 |
| **Evaluated models** | **340** |
| GI-qualified | 296 |
| Did Not Qualify for GI (no generation number in name) | 44 |

| Statistic | Value |
| :-- | --: |
| Mean GI | 3.54 |
| Median GI | 3.5 |
| Mean NL | 14.51 |
| Median NL | 14 |
| Industry Generational Velocity (OLS, GI per year) | +0.452 |

## 1. Track A: Generation Index (GI) ↑

All 296 GI-qualified models, ranked by the generation number in their name. Ties share a rank.
Bar chart of every model: [`figures/full_gi.svg`](figures/full_gi.svg).

| Rank | Model | Vendor | GI | NL | Listed | Slug |
| --: | :-- | :-- | --: | --: | :-- | :-- |
| 🥇 1 | Pareto 26.9 | unbiased | `26.9` | 11 | 2026-10-13 | `unbiased/pareto-26.9` |
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
| 74 | DeepSeek V4.1 Flash 1017 | DeepSeek | `4.1` | 24 | 2026-10-17 | `deepseek/deepseek-v4.1-flash-1017` |
| 74 | GPT-4.1 | OpenAI | `4.1` | 7 | 2025-04-14 | `openai/gpt-4.1` |
| 74 | GPT-4.1 Mini | OpenAI | `4.1` | 12 | 2025-04-14 | `openai/gpt-4.1-mini` |
| 74 | GPT-4.1 Nano | OpenAI | `4.1` | 12 | 2025-04-14 | `openai/gpt-4.1-nano` |
| 81 | DeepSeek V4 Flash 0423 | DeepSeek | `4` | 22 | 2026-04-24 | `deepseek/deepseek-v4-flash` |
| 81 | DeepSeek V4 Flash 0731 | DeepSeek | `4` | 22 | 2026-07-31 | `deepseek/deepseek-v4-flash-0731` |
| 81 | DeepSeek V4 Flash Vision Exp | DeepSeek | `4` | 28 | 2026-08-21 | `deepseek/deepseek-v4-flash-vision-exp` |
| 81 | DeepSeek V4 Pro 0423 | DeepSeek | `4` | 20 | 2026-04-24 | `deepseek/deepseek-v4-pro` |
| 81 | DeepSeek V4 Pro 0813 | DeepSeek | `4` | 20 | 2026-08-12 | `deepseek/deepseek-v4-pro-0813` |
| 81 | Gemini 4 Argon | Google | `4` | 14 | 2026-10-13 | `google/gemini-4-argon` |
| 81 | Gemma 4 26B A4B | Google | `4` | 15 | 2026-04-03 | `google/gemma-4-26b-a4b-it` |
| 81 | Gemma 4 31B | Google | `4` | 11 | 2026-04-02 | `google/gemma-4-31b-it` |
| 81 | GPT-4 | OpenAI | `4` | 5 | 2023-05-28 | `openai/gpt-4` |
| 81 | GPT-4 Turbo | OpenAI | `4` | 11 | 2024-04-09 | `openai/gpt-4-turbo` |
| 81 | GPT-4o | OpenAI | `4` | 6 | 2024-05-13 | `openai/gpt-4o` |
| 81 | GPT-4o (2024-05-13) | OpenAI | `4` | 19 | 2024-05-13 | `openai/gpt-4o-2024-05-13` |
| 81 | GPT-4o (2024-08-06) | OpenAI | `4` | 19 | 2024-08-06 | `openai/gpt-4o-2024-08-06` |
| 81 | GPT-4o (2024-11-20) | OpenAI | `4` | 19 | 2024-11-20 | `openai/gpt-4o-2024-11-20` |
| 81 | GPT-4o-mini | OpenAI | `4` | 11 | 2024-07-18 | `openai/gpt-4o-mini` |
| 81 | GPT-4o-mini (2024-07-18) | OpenAI | `4` | 24 | 2024-07-18 | `openai/gpt-4o-mini-2024-07-18` |
| 81 | Granite 4.0 Micro | IBM | `4.0` | 17 | 2025-10-20 | `ibm-granite/granite-4.0-h-micro` |
| 81 | Hermes 4 405B | Nous | `4` | 13 | 2025-08-26 | `nousresearch/hermes-4-405b` |
| 81 | Hy4 preview | Tencent | `4` | 11 | 2026-08-28 | `tencent/hy4-preview` |
| 81 | Llama 4 Maverick | Meta | `4` | 16 | 2025-04-05 | `meta-llama/llama-4-maverick` |
| 81 | Llama 4 Scout | Meta | `4` | 13 | 2025-04-05 | `meta-llama/llama-4-scout` |
| 81 | Llama Guard 4 12B | Meta | `4` | 17 | 2025-04-30 | `meta-llama/llama-guard-4-12b` |
| 81 | Magnum v4 72B | anthracite-org | `4` | 13 | 2024-10-22 | `anthracite-org/magnum-v4-72b` |
| 81 | Mistral Large 4 | Mistral | `4` | 15 | 2026-10-06 | `mistralai/mistral-large-4-0` |
| 81 | Mistral Small 4 | Mistral | `4` | 15 | 2026-03-16 | `mistralai/mistral-small-2603` |
| 81 | o4 Mini | OpenAI | `4` | 7 | 2025-04-16 | `openai/o4-mini` |
| 81 | o4 Mini High | OpenAI | `4` | 12 | 2025-04-16 | `openai/o4-mini-high` |
| 81 | Phi 4 | Microsoft | `4` | 5 | 2025-01-10 | `microsoft/phi-4` |
| 81 | Solar Mini 4 | Upstage | `4` | 12 | 2026-09-23 | `upstage/solar-mini4` |
| 81 | Solar Pro 4 | Upstage | `4` | 11 | 2026-08-10 | `upstage/solar-pro4` |
| 81 | Xing4.0 29B A4B | XingChen | `4.0` | 15 | 2026-10-16 | `xingchen-agi/xing4.0-29b-a4b` |
| 112 | Gemini 3.8 Flash | Google | `3.8` | 16 | 2026-09-02 | `google/gemini-3.8-flash` |
| 112 | Qwen3.8 2.4T A95B | Qwen | `3.8` | 17 | 2026-08-12 | `qwen/qwen3.8-2.4t-a95b` |
| 112 | Qwen3.8 27B | Qwen | `3.8` | 11 | 2026-08-14 | `qwen/qwen3.8-27b` |
| 112 | Qwen3.8 Flash | Qwen | `3.8` | 13 | 2026-08-26 | `qwen/qwen3.8-flash` |
| 112 | Qwen3.8 Max (0902) | Qwen | `3.8` | 18 | 2026-09-03 | `qwen/qwen3.8-max-0902` |
| 112 | Qwen3.8 Max Prime | Qwen | `3.8` | 17 | 2026-09-23 | `qwen/qwen3.8-max-prime` |
| 112 | Qwen3.8 Omni Flash | Qwen | `3.8` | 18 | 2026-09-21 | `qwen/qwen3.8-omni-flash` |
| 119 | Gemini 3.7 Flash | Google | `3.7` | 16 | 2026-08-13 | `google/gemini-3.7-flash` |
| 119 | Qwen3.7 Flash | Qwen | `3.7` | 13 | 2026-07-27 | `qwen/qwen3.7-flash` |
| 119 | Qwen3.7 Max | Qwen | `3.7` | 11 | 2026-05-21 | `qwen/qwen3.7-max` |
| 119 | Qwen3.7 Plus | Qwen | `3.7` | 12 | 2026-06-03 | `qwen/qwen3.7-plus` |
| 119 | Step 3.7 Flash | StepFun | `3.7` | 14 | 2026-05-28 | `stepfun/step-3.7-flash` |
| 124 | Gemini 3.6 Flash | Google | `3.6` | 16 | 2026-07-21 | `google/gemini-3.6-flash` |
| 124 | Qwen3.6 27B | Qwen | `3.6` | 11 | 2026-04-27 | `qwen/qwen3.6-27b` |
| 124 | Qwen3.6 35B A3B | Qwen | `3.6` | 15 | 2026-04-27 | `qwen/qwen3.6-35b-a3b` |
| 124 | Qwen3.6 Flash | Qwen | `3.6` | 13 | 2026-04-27 | `qwen/qwen3.6-flash` |
| 124 | Qwen3.6 Plus | Qwen | `3.6` | 12 | 2026-04-02 | `qwen/qwen3.6-plus` |
| 129 | Aion 3.5 | AionLabs | `3.5` | 8 | 2026-09-23 | `aion-labs/aion-3.5` |
| 129 | Aion 3.5 Mini | AionLabs | `3.5` | 13 | 2026-09-23 | `aion-labs/aion-3.5-mini` |
| 129 | Gemini 3.5 Flash | Google | `3.5` | 16 | 2026-05-19 | `google/gemini-3.5-flash` |
| 129 | Gemini 3.5 Flash Lite | Google | `3.5` | 21 | 2026-07-21 | `google/gemini-3.5-flash-lite` |
| 129 | GPT-3.5 Turbo | OpenAI | `3.5` | 13 | 2023-05-28 | `openai/gpt-3.5-turbo` |
| 129 | GPT-3.5 Turbo (older v0613) | OpenAI | `3.5` | 27 | 2024-01-25 | `openai/gpt-3.5-turbo-0613` |
| 129 | GPT-3.5 Turbo 16k | OpenAI | `3.5` | 17 | 2023-08-28 | `openai/gpt-3.5-turbo-16k` |
| 129 | GPT-3.5 Turbo Instruct | OpenAI | `3.5` | 22 | 2023-09-28 | `openai/gpt-3.5-turbo-instruct` |
| 129 | Mistral Medium 3.5 | Mistral | `3.5` | 18 | 2026-04-30 | `mistralai/mistral-medium-3-5` |
| 129 | Nemotron 3.5 Content Safety | NVIDIA | `3.5` | 27 | 2026-06-04 | `nvidia/nemotron-3.5-content-safety` |
| 129 | Nemotron 3.5 Lightning | NVIDIA | `3.5` | 22 | 2026-08-11 | `nvidia/nemotron-3.5-lightning` |
| 129 | Nemotron 3.5 Super VL | NVIDIA | `3.5` | 21 | 2026-10-15 | `nvidia/nemotron-3.5-super-vl` |
| 129 | Qwen3.5 397B A17B | Qwen | `3.5` | 17 | 2026-02-16 | `qwen/qwen3.5-397b-a17b` |
| 129 | Qwen3.5 Plus 2026-02-15 | Qwen | `3.5` | 23 | 2026-02-16 | `qwen/qwen3.5-plus-02-15` |
| 129 | Qwen3.5 Plus 2026-04-20 | Qwen | `3.5` | 23 | 2026-04-27 | `qwen/qwen3.5-plus-20260420` |
| 129 | Qwen3.5-122B-A10B | Qwen | `3.5` | 17 | 2026-02-25 | `qwen/qwen3.5-122b-a10b` |
| 129 | Qwen3.5-27B | Qwen | `3.5` | 11 | 2026-02-25 | `qwen/qwen3.5-27b` |
| 129 | Qwen3.5-35B-A3B | Qwen | `3.5` | 15 | 2026-02-25 | `qwen/qwen3.5-35b-a3b` |
| 129 | Qwen3.5-9B | Qwen | `3.5` | 10 | 2026-03-10 | `qwen/qwen3.5-9b` |
| 129 | Qwen3.5-Flash | Qwen | `3.5` | 13 | 2026-02-25 | `qwen/qwen3.5-flash-02-23` |
| 129 | Step 3.5 Flash | StepFun | `3.5` | 14 | 2026-01-29 | `stepfun/step-3.5-flash` |
| 150 | Llama 3.3 70B Instruct | Meta | `3.3` | 22 | 2024-12-06 | `meta-llama/llama-3.3-70b-instruct` |
| 150 | Llama 3.3 Euryale 70B | Sao10K | `3.3` | 21 | 2024-12-18 | `sao10k/l3.3-euryale-70b` |
| 152 | DeepSeek V3.2 | DeepSeek | `3.2` | 13 | 2025-12-01 | `deepseek/deepseek-v3.2` |
| 152 | DeepSeek V3.2 Exp | DeepSeek | `3.2` | 17 | 2025-09-29 | `deepseek/deepseek-v3.2-exp` |
| 152 | Llama 3.2 1B Instruct | Meta | `3.2` | 21 | 2024-09-25 | `meta-llama/llama-3.2-1b-instruct` |
| 152 | Llama 3.2 3B Instruct | Meta | `3.2` | 21 | 2024-09-25 | `meta-llama/llama-3.2-3b-instruct` |
| 152 | Mistral Small 3.2 24B | Mistral | `3.2` | 21 | 2025-06-20 | `mistralai/mistral-small-3.2-24b-instruct` |
| 157 | DeepSeek V3.1 | DeepSeek | `3.1` | 13 | 2025-08-21 | `deepseek/deepseek-chat-v3.1` |
| 157 | DeepSeek V3.1 Terminus | DeepSeek | `3.1` | 22 | 2025-09-22 | `deepseek/deepseek-v3.1-terminus` |
| 157 | Gemini 3.1 Flash Lite | Google | `3.1` | 21 | 2026-05-07 | `google/gemini-3.1-flash-lite` |
| 157 | Gemini 3.1 Flash Lite Preview | Google | `3.1` | 29 | 2026-03-03 | `google/gemini-3.1-flash-lite-preview` |
| 157 | Gemini 3.1 Pro Preview | Google | `3.1` | 22 | 2026-02-19 | `google/gemini-3.1-pro-preview` |
| 157 | Gemini 3.1 Pro Preview Custom Tools | Google | `3.1` | 35 | 2026-02-25 | `google/gemini-3.1-pro-preview-customtools` |
| 157 | Ling 3.1 Flash | inclusionAI | `3.1` | 14 | 2026-10-02 | `inclusionai/ling-3.1-flash` |
| 157 | Llama 3.1 70B Instruct | Meta | `3.1` | 22 | 2024-07-23 | `meta-llama/llama-3.1-70b-instruct` |
| 157 | Llama 3.1 8B Instruct | Meta | `3.1` | 21 | 2024-07-23 | `meta-llama/llama-3.1-8b-instruct` |
| 157 | Llama 3.1 Euryale 70B v2.2 | Sao10K | `3.1` | 26 | 2024-08-28 | `sao10k/l3.1-euryale-70b` |
| 157 | Mistral Medium 3.1 | Mistral | `3.1` | 18 | 2025-08-13 | `mistralai/mistral-medium-3.1` |
| 157 | Mistral Small 3.1 24B | Mistral | `3.1` | 21 | 2025-03-17 | `mistralai/mistral-small-3.1-24b-instruct` |
| 157 | Moondream 3.1 | Moondream | `3.1` | 13 | 2026-10-15 | `moondream/moondream3.1-9b-a2b` |
| 170 | Aion-3.0 | AionLabs | `3.0` | 8 | 2026-07-07 | `aion-labs/aion-3.0` |
| 170 | Aion-3.0-Mini | AionLabs | `3.0` | 13 | 2026-07-07 | `aion-labs/aion-3.0-mini` |
| 170 | DeepSeek V3 | DeepSeek | `3` | 11 | 2024-12-26 | `deepseek/deepseek-chat` |
| 170 | DeepSeek V3 0324 | DeepSeek | `3` | 16 | 2025-03-24 | `deepseek/deepseek-chat-v3-0324` |
| 170 | Dots3-Note Preview | Dots Studio | `3` | 18 | 2026-08-14 | `dots-studio/dots-3-note-preview` |
| 170 | Gemini 3 Flash Preview | Google | `3` | 22 | 2025-12-17 | `google/gemini-3-flash-preview` |
| 170 | Gemma 3 12B | Google | `3` | 11 | 2025-03-13 | `google/gemma-3-12b-it` |
| 170 | Gemma 3 27B | Google | `3` | 11 | 2025-03-12 | `google/gemma-3-27b-it` |
| 170 | Gemma 3 4B | Google | `3` | 10 | 2025-03-13 | `google/gemma-3-4b-it` |
| 170 | Hermes 3 405B Instruct | Nous | `3` | 22 | 2024-08-16 | `nousresearch/hermes-3-llama-3.1-405b` |
| 170 | Hermes 3 70B Instruct | Nous | `3` | 21 | 2024-08-18 | `nousresearch/hermes-3-llama-3.1-70b` |
| 170 | Hy3 | Tencent | `3` | 3 | 2026-07-06 | `tencent/hy3` |
| 170 | Hy3 preview | Tencent | `3` | 11 | 2026-04-22 | `tencent/hy3-preview` |
| 170 | Kimi K3 | MoonshotAI | `3` | 7 | 2026-07-16 | `moonshotai/kimi-k3` |
| 170 | Ling 3.0 Flash | inclusionAI | `3.0` | 14 | 2026-07-23 | `inclusionai/ling-3.0-flash` |
| 170 | Ling 3.0 Flash VL | inclusionAI | `3.0` | 17 | 2026-09-10 | `inclusionai/ling-3.0-flash-vl` |
| 170 | Llama 3 8B Lunaris | Sao10K | `3` | 18 | 2024-08-13 | `sao10k/l3-lunaris-8b` |
| 170 | MiniMax M3 | MiniMax | `3` | 10 | 2026-05-31 | `minimax/minimax-m3` |
| 170 | Ministral 3 14B 2512 | Mistral | `3` | 20 | 2025-12-02 | `mistralai/ministral-14b-2512` |
| 170 | Ministral 3 3B 2512 | Mistral | `3` | 19 | 2025-12-02 | `mistralai/ministral-3b-2512` |
| 170 | Ministral 3 8B 2512 | Mistral | `3` | 19 | 2025-12-02 | `mistralai/ministral-8b-2512` |
| 170 | Mistral Large 3 2512 | Mistral | `3` | 20 | 2025-12-01 | `mistralai/mistral-large-2512` |
| 170 | Mistral Medium 3 | Mistral | `3` | 16 | 2025-05-07 | `mistralai/mistral-medium-3` |
| 170 | Mistral Small 3 | Mistral | `3` | 15 | 2025-01-30 | `mistralai/mistral-small-24b-instruct-2501` |
| 170 | Moondream 3 Preview | Moondream | `3` | 19 | 2026-10-15 | `moondream/moondream3-preview` |
| 170 | Morph V3 Fast | Morph | `3` | 13 | 2025-07-07 | `morph/morph-v3-fast` |
| 170 | Morph V3 Large | Morph | `3` | 14 | 2025-07-07 | `morph/morph-v3-large` |
| 170 | Nemotron 3 Nano 30B A3B | NVIDIA | `3` | 23 | 2025-12-14 | `nvidia/nemotron-3-nano-30b-a3b` |
| 170 | Nemotron 3 Nano Omni | NVIDIA | `3` | 20 | 2026-04-28 | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` |
| 170 | Nemotron 3 Super | NVIDIA | `3` | 16 | 2026-03-11 | `nvidia/nemotron-3-super-120b-a12b` |
| 170 | Nemotron 3 Ultra | NVIDIA | `3` | 16 | 2026-06-04 | `nvidia/nemotron-3-ultra-550b-a55b` |
| 170 | o3 | OpenAI | `3` | 2 | 2025-04-16 | `openai/o3` |
| 170 | o3 Mini | OpenAI | `3` | 7 | 2025-01-31 | `openai/o3-mini` |
| 170 | o3 Mini High | OpenAI | `3` | 12 | 2025-02-12 | `openai/o3-mini-high` |
| 170 | o3 Pro | OpenAI | `3` | 6 | 2025-06-10 | `openai/o3-pro` |
| 170 | Qwen3 14B | Qwen | `3` | 9 | 2025-04-28 | `qwen/qwen3-14b` |
| 170 | Qwen3 235B A22B Instruct 2507 | Qwen | `3` | 29 | 2025-07-21 | `qwen/qwen3-235b-a22b-2507` |
| 170 | Qwen3 235B A22B Thinking 2507 | Qwen | `3` | 29 | 2025-07-25 | `qwen/qwen3-235b-a22b-thinking-2507` |
| 170 | Qwen3 30B A3B | Qwen | `3` | 13 | 2025-04-28 | `qwen/qwen3-30b-a3b` |
| 170 | Qwen3 30B A3B Instruct 2507 | Qwen | `3` | 27 | 2025-07-29 | `qwen/qwen3-30b-a3b-instruct-2507` |
| 170 | Qwen3 32B | Qwen | `3` | 9 | 2025-04-28 | `qwen/qwen3-32b` |
| 170 | Qwen3 Coder 30B A3B Instruct | Qwen | `3` | 28 | 2025-07-31 | `qwen/qwen3-coder-30b-a3b-instruct` |
| 170 | Qwen3 Coder 480B A35B | Qwen | `3` | 21 | 2025-07-23 | `qwen/qwen3-coder` |
| 170 | Qwen3 Coder Flash | Qwen | `3` | 17 | 2025-09-17 | `qwen/qwen3-coder-flash` |
| 170 | Qwen3 Coder Next | Qwen | `3` | 16 | 2026-02-04 | `qwen/qwen3-coder-next` |
| 170 | Qwen3 Next 80B A3B Instruct | Qwen | `3` | 27 | 2025-09-11 | `qwen/qwen3-next-80b-a3b-instruct` |
| 170 | Qwen3 Next 80B A3B Thinking | Qwen | `3` | 27 | 2025-09-11 | `qwen/qwen3-next-80b-a3b-thinking` |
| 170 | Qwen3 VL 235B A22B Instruct | Qwen | `3` | 27 | 2025-09-23 | `qwen/qwen3-vl-235b-a22b-instruct` |
| 170 | Qwen3 VL 30B A3B Instruct | Qwen | `3` | 25 | 2025-10-06 | `qwen/qwen3-vl-30b-a3b-instruct` |
| 170 | Qwen3 VL 30B A3B Thinking | Qwen | `3` | 25 | 2025-10-06 | `qwen/qwen3-vl-30b-a3b-thinking` |
| 170 | Qwen3 VL 8B Instruct | Qwen | `3` | 20 | 2025-10-14 | `qwen/qwen3-vl-8b-instruct` |
| 170 | Reka Flash 3 | rekaai | `3` | 12 | 2025-03-12 | `rekaai/reka-flash-3` |
| 170 | Relace Apply 3 | Relace | `3` | 14 | 2025-09-26 | `relace/relace-apply-3` |
| 170 | Solar Pro 3 | Upstage | `3` | 11 | 2026-01-27 | `upstage/solar-pro-3` |
| 224 | Kimi K2.7 Code | MoonshotAI | `2.7` | 14 | 2026-06-12 | `moonshotai/kimi-k2.7-code` |
| 224 | MiniMax M2.7 | MiniMax | `2.7` | 12 | 2026-03-18 | `minimax/minimax-m2.7` |
| 226 | Kimi K2.6 | MoonshotAI | `2.6` | 9 | 2026-04-20 | `moonshotai/kimi-k2.6` |
| 226 | MiMo-V2.6-Flash | Xiaomi | `2.6` | 15 | 2026-09-21 | `xiaomi/mimo-v2.6-flash` |
| 226 | MiMo-V2.6-Pro | Xiaomi | `2.6` | 13 | 2026-09-21 | `xiaomi/mimo-v2.6-pro` |
| 226 | MiMo-V2.6-Pro-UltraSpeed | Xiaomi | `2.6` | 24 | 2026-09-21 | `xiaomi/mimo-v2.6-pro-ultraspeed` |
| 230 | Gemini 2.5 Flash | Google | `2.5` | 16 | 2025-06-17 | `google/gemini-2.5-flash` |
| 230 | Gemini 2.5 Flash Lite | Google | `2.5` | 21 | 2025-07-22 | `google/gemini-2.5-flash-lite` |
| 230 | Gemini 2.5 Pro | Google | `2.5` | 14 | 2025-06-17 | `google/gemini-2.5-pro` |
| 230 | Gemini 2.5 Pro Preview 06-05 | Google | `2.5` | 28 | 2025-06-05 | `google/gemini-2.5-pro-preview` |
| 230 | Kimi K2.5 | MoonshotAI | `2.5` | 9 | 2026-01-27 | `moonshotai/kimi-k2.5` |
| 230 | LFM2.5-2.6B | LiquidAI | `2.5` | 11 | 2026-08-11 | `liquid/lfm-2.5-2.6b` |
| 230 | LFM2.5-24B-A2B | LiquidAI | `2.5` | 14 | 2026-10-13 | `liquid/lfm-2.5-24b-a2b` |
| 230 | Mercury 2.5 | Inception | `2.5` | 11 | 2026-09-08 | `inception/mercury-2.5` |
| 230 | MiMo-V2.5 | Xiaomi | `2.5` | 9 | 2026-04-22 | `xiaomi/mimo-v2.5` |
| 230 | MiMo-V2.5-Pro | Xiaomi | `2.5` | 13 | 2026-04-22 | `xiaomi/mimo-v2.5-pro` |
| 230 | MiniMax M2.5 | MiniMax | `2.5` | 12 | 2026-02-12 | `minimax/minimax-m2.5` |
| 230 | Nex-N2.5-Mini | Nex AGI | `2.5` | 13 | 2026-09-08 | `nex-agi/nex-n2.5-mini` |
| 230 | Nex-N2.5-Pro | Nex AGI | `2.5` | 12 | 2026-09-08 | `nex-agi/nex-n2.5-pro` |
| 230 | Qwen2.5 72B Instruct | Qwen | `2.5` | 20 | 2024-09-19 | `qwen/qwen-2.5-72b-instruct` |
| 230 | Qwen2.5 7B Instruct | Qwen | `2.5` | 19 | 2024-10-16 | `qwen/qwen-2.5-7b-instruct` |
| 230 | Qwen2.5 Coder 32B Instruct | Qwen | `2.5` | 26 | 2024-11-11 | `qwen/qwen-2.5-coder-32b-instruct` |
| 230 | Qwen2.5 VL 72B Instruct | Qwen | `2.5` | 23 | 2025-02-01 | `qwen/qwen2.5-vl-72b-instruct` |
| 247 | Laguna S 2.1 | Poolside | `2.1` | 12 | 2026-07-21 | `poolside/laguna-s-2.1` |
| 247 | Laguna XS 2.1 | Poolside | `2.1` | 13 | 2026-07-02 | `poolside/laguna-xs-2.1` |
| 247 | MiniMax M2.1 | MiniMax | `2.1` | 12 | 2025-12-23 | `minimax/minimax-m2.1` |
| 247 | Seed 2.1 Turbo | ByteDance Seed | `2.1` | 14 | 2026-08-12 | `bytedance-seed/seed-2-1-turbo` |
| 251 | Aion-2.0 | AionLabs | `2.0` | 8 | 2026-02-23 | `aion-labs/aion-2.0` |
| 251 | Devstral 2 2512 | Mistral | `2` | 15 | 2025-12-09 | `mistralai/devstral-2512` |
| 251 | Fugu Ultra v2 | Sakana | `2` | 13 | 2026-09-11 | `sakana/fugu-ultra-v2` |
| 251 | Gemma 2 27B | Google | `2` | 11 | 2024-07-13 | `google/gemma-2-27b-it` |
| 251 | Hy-MT2-1.8B | Tencent | `2` | 11 | 2026-08-20 | `tencent/hy-mt2-1.8b` |
| 251 | Hy-MT2-30B-A3B | Tencent | `2` | 14 | 2026-08-20 | `tencent/hy-mt2-30b-a3b` |
| 251 | Hy-MT2-7B | Tencent | `2` | 9 | 2026-08-19 | `tencent/hy-mt2-7b` |
| 251 | Kimi K2 0711 | MoonshotAI | `2` | 12 | 2025-07-11 | `moonshotai/kimi-k2` |
| 251 | Kimi K2 0905 | MoonshotAI | `2` | 12 | 2025-09-04 | `moonshotai/kimi-k2-0905` |
| 251 | Kimi K2 Thinking | MoonshotAI | `2` | 16 | 2025-11-06 | `moonshotai/kimi-k2-thinking` |
| 251 | LongCat 2.0 | Meituan | `2.0` | 11 | 2026-07-20 | `meituan/longcat-2.0` |
| 251 | Mercury 2 | Inception | `2` | 9 | 2026-03-04 | `inception/mercury-2` |
| 251 | MiniMax M2 | MiniMax | `2` | 10 | 2025-10-23 | `minimax/minimax-m2` |
| 251 | MiniMax M2-her | MiniMax | `2` | 14 | 2026-01-23 | `minimax/minimax-m2-her` |
| 251 | Nova 2 Lite | Amazon | `2` | 11 | 2025-12-02 | `amazon/nova-2-lite-v1` |
| 251 | Schematron V2 Small | Inference.net | `2` | 19 | 2026-09-12 | `inference-net/schematron-v2-small` |
| 251 | Schematron V2 Turbo | Inference.net | `2` | 19 | 2026-09-12 | `inference-net/schematron-v2-turbo` |
| 251 | Seed-2.0-Code | ByteDance Seed | `2.0` | 13 | 2026-08-12 | `bytedance-seed/seed-2.0-code` |
| 251 | Seed-2.0-Lite | ByteDance Seed | `2.0` | 13 | 2026-03-10 | `bytedance-seed/seed-2.0-lite` |
| 251 | Seed-2.0-Mini | ByteDance Seed | `2.0` | 13 | 2026-02-26 | `bytedance-seed/seed-2.0-mini` |
| 251 | Skyfall 36B V2 | TheDrummer | `2` | 14 | 2025-03-10 | `thedrummer/skyfall-36b-v2` |
| 251 | Ternary Bonsai 2 27B | PrismML | `2` | 20 | 2026-09-18 | `prism-ml/ternary-bonsai-2-27b` |
| 251 | WizardLM-2 8x22B | Microsoft | `2` | 16 | 2024-04-16 | `microsoft/wizardlm-2-8x22b` |
| 274 | Seed 1.6 | ByteDance Seed | `1.6` | 8 | 2025-12-23 | `bytedance-seed/seed-1.6` |
| 274 | Seed 1.6 Flash | ByteDance Seed | `1.6` | 14 | 2025-12-23 | `bytedance-seed/seed-1.6-flash` |
| 276 | Perceptron Mk1.5 | Perceptron | `1.5` | 16 | 2026-09-25 | `perceptron/perceptron-mk1.5` |
| 277 | Muse Spark 1.3 | Meta | `1.3` | 14 | 2026-09-02 | `meta/muse-spark-1.3` |
| 277 | Muse Spark 1.3 Contributor | Meta | `1.3` | 26 | 2026-09-02 | `meta/muse-spark-1.3-contributor` |
| 279 | Muse Spark 1.2 | Meta | `1.2` | 14 | 2026-08-05 | `meta/muse-spark-1.2` |
| 279 | Muse Spark 1.2 Contributor | Meta | `1.2` | 26 | 2026-08-21 | `meta/muse-spark-1.2-contributor` |
| 281 | Muse Spark 1.1 | Meta | `1.1` | 14 | 2026-07-16 | `meta/muse-spark-1.1` |
| 282 | Aion-RP 1.0 (8B) | AionLabs | `1.0` | 16 | 2025-02-04 | `aion-labs/aion-rp-llama-3.1-8b` |
| 282 | Beam 1.0 501B A23B | Reflection | `1.0` | 18 | 2026-10-16 | `reflection/beam-1.0-501b-a23b` |
| 282 | Ember-1 | Fireworks | `1` | 7 | 2026-09-24 | `fireworks/ember-1` |
| 282 | MiniMax M1 | MiniMax | `1` | 10 | 2025-06-17 | `minimax/minimax-m1` |
| 282 | MiniMax-01 | MiniMax | `01` | 10 | 2025-01-15 | `minimax/minimax-01` |
| 282 | Nova Lite 1.0 | Amazon | `1.0` | 13 | 2024-12-05 | `amazon/nova-lite-v1` |
| 282 | Nova Micro 1.0 | Amazon | `1.0` | 14 | 2024-12-05 | `amazon/nova-micro-v1` |
| 282 | Nova Premier 1.0 | Amazon | `1.0` | 16 | 2025-10-31 | `amazon/nova-premier-v1` |
| 282 | Nova Pro 1.0 | Amazon | `1.0` | 12 | 2024-12-05 | `amazon/nova-pro-v1` |
| 282 | o1 | OpenAI | `1` | 2 | 2024-12-17 | `openai/o1` |
| 282 | o1-pro | OpenAI | `1` | 6 | 2025-03-19 | `openai/o1-pro` |
| 282 | Perceptron Mk1 | Perceptron | `1` | 14 | 2026-05-12 | `perceptron/perceptron-mk1` |
| 282 | R1 | DeepSeek | `1` | 2 | 2025-01-20 | `deepseek/deepseek-r1` |
| 282 | R1 0528 | DeepSeek | `1` | 7 | 2025-05-28 | `deepseek/deepseek-r1-0528` |
| 296 | Grok Build 0.1 | SpaceXAI | `0.1` | 14 | 2026-05-20 | `x-ai/grok-build-0.1` |

### 1.1 Foundational Humility Award (lowest GI)

| Model | Vendor | GI | Listed |
| :-- | :-- | --: | :-- |
| Grok Build 0.1 | SpaceXAI | `0.1` | 2026-05-20 |
| Aion-RP 1.0 (8B) | AionLabs | `1.0` | 2025-02-04 |
| Beam 1.0 501B A23B | Reflection | `1.0` | 2026-10-16 |
| Ember-1 | Fireworks | `1` | 2026-09-24 |
| MiniMax M1 | MiniMax | `1` | 2025-06-17 |
| MiniMax-01 | MiniMax | `01` | 2025-01-15 |
| Nova Lite 1.0 | Amazon | `1.0` | 2024-12-05 |
| Nova Micro 1.0 | Amazon | `1.0` | 2024-12-05 |
| Nova Premier 1.0 | Amazon | `1.0` | 2025-10-31 |
| Nova Pro 1.0 | Amazon | `1.0` | 2024-12-05 |

## 2. Track B: Nomenclature Length (NL) ↑

All 340 evaluated models, ranked by the character count of their canonical name. Ties share a rank.
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
| 20 | DeepSeek V4.1 Flash 1017 | DeepSeek | 24 | `4.1` | `deepseek/deepseek-v4.1-flash-1017` |
| 20 | GPT-4o-mini (2024-07-18) | OpenAI | 24 | `4` | `openai/gpt-4o-mini-2024-07-18` |
| 20 | MiMo-V2.6-Pro-UltraSpeed | Xiaomi | 24 | `2.6` | `xiaomi/mimo-v2.6-pro-ultraspeed` |
| 23 | Nemotron 3 Nano 30B A3B | NVIDIA | 23 | `3` | `nvidia/nemotron-3-nano-30b-a3b` |
| 23 | Qwen2.5 VL 72B Instruct | Qwen | 23 | `2.5` | `qwen/qwen2.5-vl-72b-instruct` |
| 23 | Qwen3.5 Plus 2026-02-15 | Qwen | 23 | `3.5` | `qwen/qwen3.5-plus-02-15` |
| 23 | Qwen3.5 Plus 2026-04-20 | Qwen | 23 | `3.5` | `qwen/qwen3.5-plus-20260420` |
| 27 | DeepSeek V3.1 Terminus | DeepSeek | 22 | `3.1` | `deepseek/deepseek-v3.1-terminus` |
| 27 | DeepSeek V4 Flash 0423 | DeepSeek | 22 | `4` | `deepseek/deepseek-v4-flash` |
| 27 | DeepSeek V4 Flash 0731 | DeepSeek | 22 | `4` | `deepseek/deepseek-v4-flash-0731` |
| 27 | Gemini 3 Flash Preview | Google | 22 | `3` | `google/gemini-3-flash-preview` |
| 27 | Gemini 3.1 Pro Preview | Google | 22 | `3.1` | `google/gemini-3.1-pro-preview` |
| 27 | GPT-3.5 Turbo Instruct | OpenAI | 22 | `3.5` | `openai/gpt-3.5-turbo-instruct` |
| 27 | Hermes 3 405B Instruct | Nous | 22 | `3` | `nousresearch/hermes-3-llama-3.1-405b` |
| 27 | Llama 3.1 70B Instruct | Meta | 22 | `3.1` | `meta-llama/llama-3.1-70b-instruct` |
| 27 | Llama 3.3 70B Instruct | Meta | 22 | `3.3` | `meta-llama/llama-3.3-70b-instruct` |
| 27 | Mixtral 8x22B Instruct | Mistral | 22 | DNQ | `mistralai/mixtral-8x22b-instruct` |
| 27 | Nemotron 3.5 Lightning | NVIDIA | 22 | `3.5` | `nvidia/nemotron-3.5-lightning` |
| 27 | Trinity Large Thinking | Arcee AI | 22 | DNQ | `arcee-ai/trinity-large-thinking` |
| 27 | Voxtral Small 24B 2507 | Mistral | 22 | DNQ | `mistralai/voxtral-small-24b-2507` |
| 40 | Command R7B (12-2024) | Cohere | 21 | DNQ | `cohere/command-r7b-12-2024` |
| 40 | Gemini 2.5 Flash Lite | Google | 21 | `2.5` | `google/gemini-2.5-flash-lite` |
| 40 | Gemini 3.1 Flash Lite | Google | 21 | `3.1` | `google/gemini-3.1-flash-lite` |
| 40 | Gemini 3.5 Flash Lite | Google | 21 | `3.5` | `google/gemini-3.5-flash-lite` |
| 40 | gpt-oss-safeguard-20b | OpenAI | 21 | DNQ | `openai/gpt-oss-safeguard-20b` |
| 40 | Grok 4.20 Multi-Agent | SpaceXAI | 21 | `4.20` | `x-ai/grok-4.20-multi-agent` |
| 40 | Hermes 3 70B Instruct | Nous | 21 | `3` | `nousresearch/hermes-3-llama-3.1-70b` |
| 40 | Hunyuan A13B Instruct | Tencent | 21 | DNQ | `tencent/hunyuan-a13b-instruct` |
| 40 | Llama 3.1 8B Instruct | Meta | 21 | `3.1` | `meta-llama/llama-3.1-8b-instruct` |
| 40 | Llama 3.2 1B Instruct | Meta | 21 | `3.2` | `meta-llama/llama-3.2-1b-instruct` |
| 40 | Llama 3.2 3B Instruct | Meta | 21 | `3.2` | `meta-llama/llama-3.2-3b-instruct` |
| 40 | Llama 3.3 Euryale 70B | Sao10K | 21 | `3.3` | `sao10k/l3.3-euryale-70b` |
| 40 | Mistral Small 3.1 24B | Mistral | 21 | `3.1` | `mistralai/mistral-small-3.1-24b-instruct` |
| 40 | Mistral Small 3.2 24B | Mistral | 21 | `3.2` | `mistralai/mistral-small-3.2-24b-instruct` |
| 40 | Nemotron 3.5 Super VL | NVIDIA | 21 | `3.5` | `nvidia/nemotron-3.5-super-vl` |
| 40 | Qwen3 Coder 480B A35B | Qwen | 21 | `3` | `qwen/qwen3-coder` |
| 56 | Command R+ (08-2024) | Cohere | 20 | DNQ | `cohere/command-r-plus-08-2024` |
| 56 | DeepSeek V4 Pro 0423 | DeepSeek | 20 | `4` | `deepseek/deepseek-v4-pro` |
| 56 | DeepSeek V4 Pro 0813 | DeepSeek | 20 | `4` | `deepseek/deepseek-v4-pro-0813` |
| 56 | Ministral 3 14B 2512 | Mistral | 20 | `3` | `mistralai/ministral-14b-2512` |
| 56 | Mistral Large 3 2512 | Mistral | 20 | `3` | `mistralai/mistral-large-2512` |
| 56 | Nemotron 3 Nano Omni | NVIDIA | 20 | `3` | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` |
| 56 | Qwen2.5 72B Instruct | Qwen | 20 | `2.5` | `qwen/qwen-2.5-72b-instruct` |
| 56 | Qwen3 VL 8B Instruct | Qwen | 20 | `3` | `qwen/qwen3-vl-8b-instruct` |
| 56 | Ternary Bonsai 2 27B | PrismML | 20 | `2` | `prism-ml/ternary-bonsai-2-27b` |
| 65 | Command R (08-2024) | Cohere | 19 | DNQ | `cohere/command-r-08-2024` |
| 65 | DeepSeek V4.1 Flash | DeepSeek | 19 | `4.1` | `deepseek/deepseek-v4.1-flash` |
| 65 | GPT-4o (2024-05-13) | OpenAI | 19 | `4` | `openai/gpt-4o-2024-05-13` |
| 65 | GPT-4o (2024-08-06) | OpenAI | 19 | `4` | `openai/gpt-4o-2024-08-06` |
| 65 | GPT-4o (2024-11-20) | OpenAI | 19 | `4` | `openai/gpt-4o-2024-11-20` |
| 65 | Ministral 3 3B 2512 | Mistral | 19 | `3` | `mistralai/ministral-3b-2512` |
| 65 | Ministral 3 8B 2512 | Mistral | 19 | `3` | `mistralai/ministral-8b-2512` |
| 65 | Moondream 3 Preview | Moondream | 19 | `3` | `moondream/moondream3-preview` |
| 65 | Qwen2.5 7B Instruct | Qwen | 19 | `2.5` | `qwen/qwen-2.5-7b-instruct` |
| 65 | Schematron V2 Small | Inference.net | 19 | `2` | `inference-net/schematron-v2-small` |
| 65 | Schematron V2 Turbo | Inference.net | 19 | `2` | `inference-net/schematron-v2-turbo` |
| 65 | Sonar Deep Research | Perplexity | 19 | DNQ | `perplexity/sonar-deep-research` |
| 65 | Sonar Reasoning Pro | Perplexity | 19 | DNQ | `perplexity/sonar-reasoning-pro` |
| 78 | Beam 1.0 501B A23B | Reflection | 18 | `1.0` | `reflection/beam-1.0-501b-a23b` |
| 78 | Dots3-Note Preview | Dots Studio | 18 | `3` | `dots-studio/dots-3-note-preview` |
| 78 | GPT-5.1-Codex-Mini | OpenAI | 18 | `5.1` | `openai/gpt-5.1-codex-mini` |
| 78 | Llama 3 8B Lunaris | Sao10K | 18 | `3` | `sao10k/l3-lunaris-8b` |
| 78 | Mistral Large 2407 | Mistral | 18 | DNQ | `mistralai/mistral-large-2407` |
| 78 | Mistral Medium 3.1 | Mistral | 18 | `3.1` | `mistralai/mistral-medium-3.1` |
| 78 | Mistral Medium 3.5 | Mistral | 18 | `3.5` | `mistralai/mistral-medium-3-5` |
| 78 | Qwen3.8 Max (0902) | Qwen | 18 | `3.8` | `qwen/qwen3.8-max-0902` |
| 78 | Qwen3.8 Omni Flash | Qwen | 18 | `3.8` | `qwen/qwen3.8-omni-flash` |
| 87 | Claude Sonnet 4.5 | Anthropic | 17 | `4.5` | `anthropic/claude-sonnet-4.5` |
| 87 | Claude Sonnet 4.6 | Anthropic | 17 | `4.6` | `anthropic/claude-sonnet-4.6` |
| 87 | Claude Sonnet 5.5 | Anthropic | 17 | `5.5` | `anthropic/claude-sonnet-5.5` |
| 87 | DeepSeek V3.2 Exp | DeepSeek | 17 | `3.2` | `deepseek/deepseek-v3.2-exp` |
| 87 | GPT-3.5 Turbo 16k | OpenAI | 17 | `3.5` | `openai/gpt-3.5-turbo-16k` |
| 87 | GPT-5.1-Codex-Max | OpenAI | 17 | `5.1` | `openai/gpt-5.1-codex-max` |
| 87 | GPT-5.6 Terra Pro | OpenAI | 17 | `5.6` | `openai/gpt-5.6-terra-pro` |
| 87 | Granite 4.0 Micro | IBM | 17 | `4.0` | `ibm-granite/granite-4.0-h-micro` |
| 87 | Ling 3.0 Flash VL | inclusionAI | 17 | `3.0` | `inclusionai/ling-3.0-flash-vl` |
| 87 | Llama Guard 4 12B | Meta | 17 | `4` | `meta-llama/llama-guard-4-12b` |
| 87 | Qwen3 Coder Flash | Qwen | 17 | `3` | `qwen/qwen3-coder-flash` |
| 87 | Qwen3.5 397B A17B | Qwen | 17 | `3.5` | `qwen/qwen3.5-397b-a17b` |
| 87 | Qwen3.5-122B-A10B | Qwen | 17 | `3.5` | `qwen/qwen3.5-122b-a10b` |
| 87 | Qwen3.8 2.4T A95B | Qwen | 17 | `3.8` | `qwen/qwen3.8-2.4t-a95b` |
| 87 | Qwen3.8 Max Prime | Qwen | 17 | `3.8` | `qwen/qwen3.8-max-prime` |
| 102 | Aion-RP 1.0 (8B) | AionLabs | 16 | `1.0` | `aion-labs/aion-rp-llama-3.1-8b` |
| 102 | Claude Fable 5.1 | Anthropic | 16 | `5.1` | `anthropic/claude-fable-5.1` |
| 102 | Claude Haiku 4.5 | Anthropic | 16 | `4.5` | `anthropic/claude-haiku-4.5` |
| 102 | Claude Haiku 5.5 | Anthropic | 16 | `5.5` | `anthropic/claude-haiku-5.5` |
| 102 | Cydonia 24B V4.1 | TheDrummer | 16 | `4.1` | `thedrummer/cydonia-24b-v4.1` |
| 102 | DeepSeek V3 0324 | DeepSeek | 16 | `3` | `deepseek/deepseek-chat-v3-0324` |
| 102 | Gemini 2.5 Flash | Google | 16 | `2.5` | `google/gemini-2.5-flash` |
| 102 | Gemini 3.5 Flash | Google | 16 | `3.5` | `google/gemini-3.5-flash` |
| 102 | Gemini 3.6 Flash | Google | 16 | `3.6` | `google/gemini-3.6-flash` |
| 102 | Gemini 3.7 Flash | Google | 16 | `3.7` | `google/gemini-3.7-flash` |
| 102 | Gemini 3.8 Flash | Google | 16 | `3.8` | `google/gemini-3.8-flash` |
| 102 | GPT-5.6 Luna Pro | OpenAI | 16 | `5.6` | `openai/gpt-5.6-luna-pro` |
| 102 | Kimi K2 Thinking | MoonshotAI | 16 | `2` | `moonshotai/kimi-k2-thinking` |
| 102 | Llama 4 Maverick | Meta | 16 | `4` | `meta-llama/llama-4-maverick` |
| 102 | Mistral Medium 3 | Mistral | 16 | `3` | `mistralai/mistral-medium-3` |
| 102 | Muse Glimmer 30B | Meta | 16 | DNQ | `meta/muse-glimmer-30b` |
| 102 | Nemotron 3 Super | NVIDIA | 16 | `3` | `nvidia/nemotron-3-super-120b-a12b` |
| 102 | Nemotron 3 Ultra | NVIDIA | 16 | `3` | `nvidia/nemotron-3-ultra-550b-a55b` |
| 102 | Nova Premier 1.0 | Amazon | 16 | `1.0` | `amazon/nova-premier-v1` |
| 102 | Perceptron Mk1.5 | Perceptron | 16 | `1.5` | `perceptron/perceptron-mk1.5` |
| 102 | Qwen3 Coder Next | Qwen | 16 | `3` | `qwen/qwen3-coder-next` |
| 102 | Sonar Pro Search | Perplexity | 16 | DNQ | `perplexity/sonar-pro-search` |
| 102 | WizardLM-2 8x22B | Microsoft | 16 | `2` | `microsoft/wizardlm-2-8x22b` |
| 125 | Claude Opus 4.1 | Anthropic | 15 | `4.1` | `anthropic/claude-opus-4.1` |
| 125 | Claude Opus 4.5 | Anthropic | 15 | `4.5` | `anthropic/claude-opus-4.5` |
| 125 | Claude Opus 4.6 | Anthropic | 15 | `4.6` | `anthropic/claude-opus-4.6` |
| 125 | Claude Opus 4.7 | Anthropic | 15 | `4.7` | `anthropic/claude-opus-4.7` |
| 125 | Claude Opus 4.8 | Anthropic | 15 | `4.8` | `anthropic/claude-opus-4.8` |
| 125 | Claude Opus 5.5 | Anthropic | 15 | `5.5` | `anthropic/claude-opus-5.5` |
| 125 | Claude Sonnet 5 | Anthropic | 15 | `5` | `anthropic/claude-sonnet-5` |
| 125 | Devstral 2 2512 | Mistral | 15 | `2` | `mistralai/devstral-2512` |
| 125 | Gemma 4 26B A4B | Google | 15 | `4` | `google/gemma-4-26b-a4b-it` |
| 125 | GPT Chat Latest | OpenAI | 15 | DNQ | `openai/gpt-chat-latest` |
| 125 | GPT-5.6 Sol Pro | OpenAI | 15 | `5.6` | `openai/gpt-5.6-sol-pro` |
| 125 | GPT-6 Astra Pro | OpenAI | 15 | `6` | `openai/gpt-6-astra-pro` |
| 125 | GPT-6.1 Sol Pro | OpenAI | 15 | `6.1` | `openai/gpt-6.1-sol-pro` |
| 125 | MiMo-V2.6-Flash | Xiaomi | 15 | `2.6` | `xiaomi/mimo-v2.6-flash` |
| 125 | Mistral Large 4 | Mistral | 15 | `4` | `mistralai/mistral-large-4-0` |
| 125 | Mistral Small 3 | Mistral | 15 | `3` | `mistralai/mistral-small-24b-instruct-2501` |
| 125 | Mistral Small 4 | Mistral | 15 | `4` | `mistralai/mistral-small-2603` |
| 125 | Muse Spark Open | Meta | 15 | DNQ | `meta/muse-spark-open` |
| 125 | North Mini Code | Cohere | 15 | DNQ | `cohere/north-mini-code` |
| 125 | Qwen3.5-35B-A3B | Qwen | 15 | `3.5` | `qwen/qwen3.5-35b-a3b` |
| 125 | Qwen3.6 35B A3B | Qwen | 15 | `3.6` | `qwen/qwen3.6-35b-a3b` |
| 125 | Xing4.0 29B A4B | XingChen | 15 | `4.0` | `xingchen-agi/xing4.0-29b-a4b` |
| 147 | Claude Fable 5 | Anthropic | 14 | `5` | `anthropic/claude-fable-5` |
| 147 | Codestral 2508 | Mistral | 14 | DNQ | `mistralai/codestral-2508` |
| 147 | Gemini 2.5 Pro | Google | 14 | `2.5` | `google/gemini-2.5-pro` |
| 147 | Gemini 4 Argon | Google | 14 | `4` | `google/gemini-4-argon` |
| 147 | GLM 5.3 FlashX | Z.ai | 14 | `5.3` | `z-ai/glm-5.3-flashx` |
| 147 | GPT-6 Luna Pro | OpenAI | 14 | `6` | `openai/gpt-6-luna-pro` |
| 147 | Granite 4.2 8B | IBM | 14 | `4.2` | `ibm-granite/granite-4.2-8b` |
| 147 | Grok Build 0.1 | SpaceXAI | 14 | `0.1` | `x-ai/grok-build-0.1` |
| 147 | Hy-MT2-30B-A3B | Tencent | 14 | `2` | `tencent/hy-mt2-30b-a3b` |
| 147 | Kimi K2.7 Code | MoonshotAI | 14 | `2.7` | `moonshotai/kimi-k2.7-code` |
| 147 | LFM2.5-24B-A2B | LiquidAI | 14 | `2.5` | `liquid/lfm-2.5-24b-a2b` |
| 147 | Ling 3.0 Flash | inclusionAI | 14 | `3.0` | `inclusionai/ling-3.0-flash` |
| 147 | Ling 3.1 Flash | inclusionAI | 14 | `3.1` | `inclusionai/ling-3.1-flash` |
| 147 | MiniMax M2-her | MiniMax | 14 | `2` | `minimax/minimax-m2-her` |
| 147 | Morph V3 Large | Morph | 14 | `3` | `morph/morph-v3-large` |
| 147 | Muse Spark 1.1 | Meta | 14 | `1.1` | `meta/muse-spark-1.1` |
| 147 | Muse Spark 1.2 | Meta | 14 | `1.2` | `meta/muse-spark-1.2` |
| 147 | Muse Spark 1.3 | Meta | 14 | `1.3` | `meta/muse-spark-1.3` |
| 147 | Nova Micro 1.0 | Amazon | 14 | `1.0` | `amazon/nova-micro-v1` |
| 147 | Perceptron Mk1 | Perceptron | 14 | `1` | `perceptron/perceptron-mk1` |
| 147 | Relace Apply 3 | Relace | 14 | `3` | `relace/relace-apply-3` |
| 147 | ReMM SLERP 13B | undi95 | 14 | DNQ | `undi95/remm-slerp-l2-13b` |
| 147 | Seed 1.6 Flash | ByteDance Seed | 14 | `1.6` | `bytedance-seed/seed-1.6-flash` |
| 147 | Seed 2.1 Turbo | ByteDance Seed | 14 | `2.1` | `bytedance-seed/seed-2-1-turbo` |
| 147 | Skyfall 36B V2 | TheDrummer | 14 | `2` | `thedrummer/skyfall-36b-v2` |
| 147 | Step 3.5 Flash | StepFun | 14 | `3.5` | `stepfun/step-3.5-flash` |
| 147 | Step 3.7 Flash | StepFun | 14 | `3.7` | `stepfun/step-3.7-flash` |
| 147 | Step 5 Preview | StepFun | 14 | `5` | `stepfun/step-5-preview` |
| 147 | UnslopNemo 12B | TheDrummer | 14 | DNQ | `thedrummer/unslopnemo-12b` |
| 147 | Weaver (alpha) | Mancer | 14 | DNQ | `mancer/weaver` |
| 177 | Aion 3.5 Mini | AionLabs | 13 | `3.5` | `aion-labs/aion-3.5-mini` |
| 177 | Aion-3.0-Mini | AionLabs | 13 | `3.0` | `aion-labs/aion-3.0-mini` |
| 177 | Claude Opus 5 | Anthropic | 13 | `5` | `anthropic/claude-opus-5` |
| 177 | DeepSeek V3.1 | DeepSeek | 13 | `3.1` | `deepseek/deepseek-chat-v3.1` |
| 177 | DeepSeek V3.2 | DeepSeek | 13 | `3.2` | `deepseek/deepseek-v3.2` |
| 177 | Fugu Ultra v2 | Sakana | 13 | `2` | `sakana/fugu-ultra-v2` |
| 177 | GLM 4.7 Flash | Z.ai | 13 | `4.7` | `z-ai/glm-4.7-flash` |
| 177 | GLM 5.3 Flash | Z.ai | 13 | `5.3` | `z-ai/glm-5.3-flash` |
| 177 | GLM 5.3 Prime | Z.ai | 13 | `5.3` | `z-ai/glm-5.3-prime` |
| 177 | GPT-3.5 Turbo | OpenAI | 13 | `3.5` | `openai/gpt-3.5-turbo` |
| 177 | GPT-5.1-Codex | OpenAI | 13 | `5.1` | `openai/gpt-5.1-codex` |
| 177 | GPT-5.2-Codex | OpenAI | 13 | `5.2` | `openai/gpt-5.2-codex` |
| 177 | GPT-5.3-Codex | OpenAI | 13 | `5.3` | `openai/gpt-5.3-codex` |
| 177 | GPT-5.6 Terra | OpenAI | 13 | `5.6` | `openai/gpt-5.6-terra` |
| 177 | GPT-6 Sol Pro | OpenAI | 13 | `6` | `openai/gpt-6-sol-pro` |
| 177 | Hermes 4 405B | Nous | 13 | `4` | `nousresearch/hermes-4-405b` |
| 177 | Inkling Small | Thinking Machines | 13 | DNQ | `thinkingmachines/inkling-small` |
| 177 | Laguna XS 2.1 | Poolside | 13 | `2.1` | `poolside/laguna-xs-2.1` |
| 177 | Llama 4 Scout | Meta | 13 | `4` | `meta-llama/llama-4-scout` |
| 177 | Magnum v4 72B | anthracite-org | 13 | `4` | `anthracite-org/magnum-v4-72b` |
| 177 | MiMo-V2.5-Pro | Xiaomi | 13 | `2.5` | `xiaomi/mimo-v2.5-pro` |
| 177 | MiMo-V2.6-Pro | Xiaomi | 13 | `2.6` | `xiaomi/mimo-v2.6-pro` |
| 177 | Mistral Large | Mistral | 13 | DNQ | `mistralai/mistral-large` |
| 177 | Moondream 3.1 | Moondream | 13 | `3.1` | `moondream/moondream3.1-9b-a2b` |
| 177 | Morph V3 Fast | Morph | 13 | `3` | `morph/morph-v3-fast` |
| 177 | Nex-N2.5-Mini | Nex AGI | 13 | `2.5` | `nex-agi/nex-n2.5-mini` |
| 177 | Nova Lite 1.0 | Amazon | 13 | `1.0` | `amazon/nova-lite-v1` |
| 177 | Qwen3 30B A3B | Qwen | 13 | `3` | `qwen/qwen3-30b-a3b` |
| 177 | Qwen3.5-Flash | Qwen | 13 | `3.5` | `qwen/qwen3.5-flash-02-23` |
| 177 | Qwen3.6 Flash | Qwen | 13 | `3.6` | `qwen/qwen3.6-flash` |
| 177 | Qwen3.7 Flash | Qwen | 13 | `3.7` | `qwen/qwen3.7-flash` |
| 177 | Qwen3.8 Flash | Qwen | 13 | `3.8` | `qwen/qwen3.8-flash` |
| 177 | Relace Search | Relace | 13 | DNQ | `relace/relace-search` |
| 177 | Sakana Namazu | Sakana | 13 | DNQ | `sakana/sakana-namazu` |
| 177 | Seed-2.0-Code | ByteDance Seed | 13 | `2.0` | `bytedance-seed/seed-2.0-code` |
| 177 | Seed-2.0-Lite | ByteDance Seed | 13 | `2.0` | `bytedance-seed/seed-2.0-lite` |
| 177 | Seed-2.0-Mini | ByteDance Seed | 13 | `2.0` | `bytedance-seed/seed-2.0-mini` |
| 214 | GLM 5V Turbo | Z.ai | 12 | `5` | `z-ai/glm-5v-turbo` |
| 214 | GPT-4.1 Mini | OpenAI | 12 | `4.1` | `openai/gpt-4.1-mini` |
| 214 | GPT-4.1 Nano | OpenAI | 12 | `4.1` | `openai/gpt-4.1-nano` |
| 214 | GPT-5.2 Chat | OpenAI | 12 | `5.2` | `openai/gpt-5.2-chat` |
| 214 | GPT-5.4 Mini | OpenAI | 12 | `5.4` | `openai/gpt-5.4-mini` |
| 214 | GPT-5.4 Nano | OpenAI | 12 | `5.4` | `openai/gpt-5.4-nano` |
| 214 | GPT-5.6 Luna | OpenAI | 12 | `5.6` | `openai/gpt-5.6-luna` |
| 214 | gpt-oss-120b | OpenAI | 12 | DNQ | `openai/gpt-oss-120b` |
| 214 | Kimi K2 0711 | MoonshotAI | 12 | `2` | `moonshotai/kimi-k2` |
| 214 | Kimi K2 0905 | MoonshotAI | 12 | `2` | `moonshotai/kimi-k2-0905` |
| 214 | Laguna S 2.1 | Poolside | 12 | `2.1` | `poolside/laguna-s-2.1` |
| 214 | MiniMax M2.1 | MiniMax | 12 | `2.1` | `minimax/minimax-m2.1` |
| 214 | MiniMax M2.5 | MiniMax | 12 | `2.5` | `minimax/minimax-m2.5` |
| 214 | MiniMax M2.7 | MiniMax | 12 | `2.7` | `minimax/minimax-m2.7` |
| 214 | Mistral Nemo | Mistral | 12 | DNQ | `mistralai/mistral-nemo` |
| 214 | MythoMax 13B | gryphe | 12 | DNQ | `gryphe/mythomax-l2-13b` |
| 214 | Nex-N2.5-Pro | Nex AGI | 12 | `2.5` | `nex-agi/nex-n2.5-pro` |
| 214 | Nova Pro 1.0 | Amazon | 12 | `1.0` | `amazon/nova-pro-v1` |
| 214 | o3 Mini High | OpenAI | 12 | `3` | `openai/o3-mini-high` |
| 214 | o4 Mini High | OpenAI | 12 | `4` | `openai/o4-mini-high` |
| 214 | Qwen3.6 Plus | Qwen | 12 | `3.6` | `qwen/qwen3.6-plus` |
| 214 | Qwen3.7 Plus | Qwen | 12 | `3.7` | `qwen/qwen3.7-plus` |
| 214 | Reka Flash 3 | rekaai | 12 | `3` | `rekaai/reka-flash-3` |
| 214 | Solar Mini 4 | Upstage | 12 | `4` | `upstage/solar-mini4` |
| 238 | DeepSeek V3 | DeepSeek | 11 | `3` | `deepseek/deepseek-chat` |
| 238 | Gemma 2 27B | Google | 11 | `2` | `google/gemma-2-27b-it` |
| 238 | Gemma 3 12B | Google | 11 | `3` | `google/gemma-3-12b-it` |
| 238 | Gemma 3 27B | Google | 11 | `3` | `google/gemma-3-27b-it` |
| 238 | Gemma 4 31B | Google | 11 | `4` | `google/gemma-4-31b-it` |
| 238 | GLM 4.5 Air | Z.ai | 11 | `4.5` | `z-ai/glm-4.5-air` |
| 238 | GLM 5 Turbo | Z.ai | 11 | `5` | `z-ai/glm-5-turbo` |
| 238 | GPT-4 Turbo | OpenAI | 11 | `4` | `openai/gpt-4-turbo` |
| 238 | GPT-4o-mini | OpenAI | 11 | `4` | `openai/gpt-4o-mini` |
| 238 | GPT-5.2 Pro | OpenAI | 11 | `5.2` | `openai/gpt-5.2-pro` |
| 238 | GPT-5.4 Pro | OpenAI | 11 | `5.4` | `openai/gpt-5.4-pro` |
| 238 | GPT-5.5 Pro | OpenAI | 11 | `5.5` | `openai/gpt-5.5-pro` |
| 238 | GPT-5.6 Sol | OpenAI | 11 | `5.6` | `openai/gpt-5.6-sol` |
| 238 | GPT-6 Astra | OpenAI | 11 | `6` | `openai/gpt-6-astra` |
| 238 | GPT-6.1 Sol | OpenAI | 11 | `6.1` | `openai/gpt-6.1-sol` |
| 238 | gpt-oss-20b | OpenAI | 11 | DNQ | `openai/gpt-oss-20b` |
| 238 | Hy-MT2-1.8B | Tencent | 11 | `2` | `tencent/hy-mt2-1.8b` |
| 238 | Hy3 preview | Tencent | 11 | `3` | `tencent/hy3-preview` |
| 238 | Hy4 preview | Tencent | 11 | `4` | `tencent/hy4-preview` |
| 238 | LFM2.5-2.6B | LiquidAI | 11 | `2.5` | `liquid/lfm-2.5-2.6b` |
| 238 | LongCat 2.0 | Meituan | 11 | `2.0` | `meituan/longcat-2.0` |
| 238 | Mercury 2.5 | Inception | 11 | `2.5` | `inception/mercury-2.5` |
| 238 | Muse Wonder | Meta | 11 | DNQ | `meta/muse-wonder` |
| 238 | Nova 2 Lite | Amazon | 11 | `2` | `amazon/nova-2-lite-v1` |
| 238 | Pareto 26.9 | unbiased | 11 | `26.9` | `unbiased/pareto-26.9` |
| 238 | Qwen3.5-27B | Qwen | 11 | `3.5` | `qwen/qwen3.5-27b` |
| 238 | Qwen3.6 27B | Qwen | 11 | `3.6` | `qwen/qwen3.6-27b` |
| 238 | Qwen3.7 Max | Qwen | 11 | `3.7` | `qwen/qwen3.7-max` |
| 238 | Qwen3.8 27B | Qwen | 11 | `3.8` | `qwen/qwen3.8-27b` |
| 238 | Solar Pro 3 | Upstage | 11 | `3` | `upstage/solar-pro-3` |
| 238 | Solar Pro 4 | Upstage | 11 | `4` | `upstage/solar-pro4` |
| 269 | Command A+ | Cohere | 10 | DNQ | `cohere/command-a-plus` |
| 269 | Fugu Ultra | Sakana | 10 | DNQ | `sakana/fugu-ultra` |
| 269 | Gemma 3 4B | Google | 10 | `3` | `google/gemma-3-4b-it` |
| 269 | GPT-5 Mini | OpenAI | 10 | `5` | `openai/gpt-5-mini` |
| 269 | GPT-5 Nano | OpenAI | 10 | `5` | `openai/gpt-5-nano` |
| 269 | GPT-6 Luna | OpenAI | 10 | `6` | `openai/gpt-6-luna` |
| 269 | MiniMax M1 | MiniMax | 10 | `1` | `minimax/minimax-m1` |
| 269 | MiniMax M2 | MiniMax | 10 | `2` | `minimax/minimax-m2` |
| 269 | MiniMax M3 | MiniMax | 10 | `3` | `minimax/minimax-m3` |
| 269 | MiniMax-01 | MiniMax | 10 | `01` | `minimax/minimax-01` |
| 269 | Palmyra X5 | Writer | 10 | `5` | `writer/palmyra-x5` |
| 269 | Qwen3.5-9B | Qwen | 10 | `3.5` | `qwen/qwen3.5-9b` |
| 269 | UI-TARS 7B | ByteDance | 10 | DNQ | `bytedance/ui-tars-1.5-7b` |
| 269 | Uncensored | Venice | 10 | DNQ | `cognitivecomputations/dolphin-mistral-24b-venice-edition` |
| 283 | Command A | Cohere | 9 | DNQ | `cohere/command-a` |
| 283 | GPT-5 Pro | OpenAI | 9 | `5` | `openai/gpt-5-pro` |
| 283 | GPT-6 Sol | OpenAI | 9 | `6` | `openai/gpt-6-sol` |
| 283 | Grok 4.20 | SpaceXAI | 9 | `4.20` | `x-ai/grok-4.20` |
| 283 | Hy-MT2-7B | Tencent | 9 | `2` | `tencent/hy-mt2-7b` |
| 283 | Kimi K2.5 | MoonshotAI | 9 | `2.5` | `moonshotai/kimi-k2.5` |
| 283 | Kimi K2.6 | MoonshotAI | 9 | `2.6` | `moonshotai/kimi-k2.6` |
| 283 | Mercury 2 | Inception | 9 | `2` | `inception/mercury-2` |
| 283 | MiMo-V2.5 | Xiaomi | 9 | `2.5` | `xiaomi/mimo-v2.5` |
| 283 | Qwen-Plus | Qwen | 9 | DNQ | `qwen/qwen-plus` |
| 283 | Qwen3 14B | Qwen | 9 | `3` | `qwen/qwen3-14b` |
| 283 | Qwen3 32B | Qwen | 9 | `3` | `qwen/qwen3-32b` |
| 283 | Reka Edge | rekaai | 9 | DNQ | `rekaai/reka-edge` |
| 283 | Sonar Pro | Perplexity | 9 | DNQ | `perplexity/sonar-pro` |
| 283 | Summarize | ScaleDown | 9 | DNQ | `scaledown/summarize` |
| 298 | Aion 3.5 | AionLabs | 8 | `3.5` | `aion-labs/aion-3.5` |
| 298 | Aion-2.0 | AionLabs | 8 | `2.0` | `aion-labs/aion-2.0` |
| 298 | Aion-3.0 | AionLabs | 8 | `3.0` | `aion-labs/aion-3.0` |
| 298 | Fugu Max | Sakana | 8 | DNQ | `sakana/fugu-max` |
| 298 | GLM 4.5V | Z.ai | 8 | `4.5` | `z-ai/glm-4.5v` |
| 298 | GLM 4.6V | Z.ai | 8 | `4.6` | `z-ai/glm-4.6v` |
| 298 | Grok 4.3 | SpaceXAI | 8 | `4.3` | `x-ai/grok-4.3` |
| 298 | Grok 4.5 | SpaceXAI | 8 | `4.5` | `x-ai/grok-4.5` |
| 298 | Grok 4.6 | SpaceXAI | 8 | `4.6` | `x-ai/grok-4.6` |
| 298 | Grok 4.7 | SpaceXAI | 8 | `4.7` | `x-ai/grok-4.7` |
| 298 | Seed 1.6 | ByteDance Seed | 8 | `1.6` | `bytedance-seed/seed-1.6` |
| 309 | Ember-1 | Fireworks | 7 | `1` | `fireworks/ember-1` |
| 309 | Extract | ScaleDown | 7 | DNQ | `scaledown/extract` |
| 309 | Glimpse | Elorian | 7 | DNQ | `elorian/glimpse` |
| 309 | GLM 4.5 | Z.ai | 7 | `4.5` | `z-ai/glm-4.5` |
| 309 | GLM 4.6 | Z.ai | 7 | `4.6` | `z-ai/glm-4.6` |
| 309 | GLM 4.7 | Z.ai | 7 | `4.7` | `z-ai/glm-4.7` |
| 309 | GLM 5.1 | Z.ai | 7 | `5.1` | `z-ai/glm-5.1` |
| 309 | GLM 5.2 | Z.ai | 7 | `5.2` | `z-ai/glm-5.2` |
| 309 | GLM 5.3 | Z.ai | 7 | `5.3` | `z-ai/glm-5.3` |
| 309 | GPT-4.1 | OpenAI | 7 | `4.1` | `openai/gpt-4.1` |
| 309 | GPT-5.1 | OpenAI | 7 | `5.1` | `openai/gpt-5.1` |
| 309 | GPT-5.2 | OpenAI | 7 | `5.2` | `openai/gpt-5.2` |
| 309 | GPT-5.4 | OpenAI | 7 | `5.4` | `openai/gpt-5.4` |
| 309 | GPT-5.5 | OpenAI | 7 | `5.5` | `openai/gpt-5.5` |
| 309 | Inkling | Thinking Machines | 7 | DNQ | `thinkingmachines/inkling` |
| 309 | Kimi K3 | MoonshotAI | 7 | `3` | `moonshotai/kimi-k3` |
| 309 | o3 Mini | OpenAI | 7 | `3` | `openai/o3-mini` |
| 309 | o4 Mini | OpenAI | 7 | `4` | `openai/o4-mini` |
| 309 | R1 0528 | DeepSeek | 7 | `1` | `deepseek/deepseek-r1-0528` |
| 328 | GPT-4o | OpenAI | 6 | `4` | `openai/gpt-4o` |
| 328 | o1-pro | OpenAI | 6 | `1` | `openai/o1-pro` |
| 328 | o3 Pro | OpenAI | 6 | `3` | `openai/o3-pro` |
| 331 | GLM 5 | Z.ai | 5 | `5` | `z-ai/glm-5` |
| 331 | GPT-4 | OpenAI | 5 | `4` | `openai/gpt-4` |
| 331 | GPT-5 | OpenAI | 5 | `5` | `openai/gpt-5` |
| 331 | Phi 4 | Microsoft | 5 | `4` | `microsoft/phi-4` |
| 331 | Sonar | Perplexity | 5 | DNQ | `perplexity/sonar` |
| 336 | Saba | Mistral | 4 | DNQ | `mistralai/mistral-saba` |
| 337 | Hy3 | Tencent | 3 | `3` | `tencent/hy3` |
| 338 | o1 | OpenAI | 2 | `1` | `openai/o1` |
| 338 | o3 | OpenAI | 2 | `3` | `openai/o3` |
| 338 | R1 | DeepSeek | 2 | `1` | `deepseek/deepseek-r1` |

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

Generations delivered per character of name. All 296 GI-qualified models.

| Rank | Model | Vendor | GI | NL | NE |
| --: | :-- | :-- | --: | --: | --: |
| 🥇 1 | Pareto 26.9 | unbiased | `26.9` | 11 | 2.4455 |
| 🥈 2 | o3 | OpenAI | `3` | 2 | 1.5000 |
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
| 108 | Gemini 4 Argon | Google | `4` | 14 | 0.2857 |
| 109 | Qwen3.7 Flash | Qwen | `3.7` | 13 | 0.2846 |
| 110 | GPT-5.1-Codex-Mini | OpenAI | `5.1` | 18 | 0.2833 |
| 111 | Claude Haiku 4.5 | Anthropic | `4.5` | 16 | 0.2812 |
| 112 | Kimi K2.5 | MoonshotAI | `2.5` | 9 | 0.2778 |
| 112 | MiMo-V2.5 | Xiaomi | `2.5` | 9 | 0.2778 |
| 114 | Qwen3.6 Flash | Qwen | `3.6` | 13 | 0.2769 |
| 115 | Claude Opus 4.1 | Anthropic | `4.1` | 15 | 0.2733 |
| 116 | DeepSeek V3 | DeepSeek | `3` | 11 | 0.2727 |
| 116 | Gemma 3 12B | Google | `3` | 11 | 0.2727 |
| 116 | Gemma 3 27B | Google | `3` | 11 | 0.2727 |
| 116 | Hy3 preview | Tencent | `3` | 11 | 0.2727 |
| 116 | Solar Pro 3 | Upstage | `3` | 11 | 0.2727 |
| 121 | Claude Sonnet 4.6 | Anthropic | `4.6` | 17 | 0.2706 |
| 122 | Aion 3.5 Mini | AionLabs | `3.5` | 13 | 0.2692 |
| 122 | GPT-3.5 Turbo | OpenAI | `3.5` | 13 | 0.2692 |
| 122 | Qwen3.5-Flash | Qwen | `3.5` | 13 | 0.2692 |
| 125 | Gemma 4 26B A4B | Google | `4` | 15 | 0.2667 |
| 125 | Mistral Large 4 | Mistral | `4` | 15 | 0.2667 |
| 125 | Mistral Small 4 | Mistral | `4` | 15 | 0.2667 |
| 125 | Xing4.0 29B A4B | XingChen | `4.0` | 15 | 0.2667 |
| 129 | Claude Sonnet 4.5 | Anthropic | `4.5` | 17 | 0.2647 |
| 130 | Step 3.7 Flash | StepFun | `3.7` | 14 | 0.2643 |
| 131 | Cydonia 24B V4.1 | TheDrummer | `4.1` | 16 | 0.2562 |
| 132 | Aion-2.0 | AionLabs | `2.0` | 8 | 0.2500 |
| 132 | Llama 4 Maverick | Meta | `4` | 16 | 0.2500 |
| 132 | o3 Mini High | OpenAI | `3` | 12 | 0.2500 |
| 132 | Reka Flash 3 | rekaai | `3` | 12 | 0.2500 |
| 132 | Step 3.5 Flash | StepFun | `3.5` | 14 | 0.2500 |
| 137 | DeepSeek V3.2 | DeepSeek | `3.2` | 13 | 0.2462 |
| 138 | Qwen3.6 35B A3B | Qwen | `3.6` | 15 | 0.2400 |
| 139 | DeepSeek V3.1 | DeepSeek | `3.1` | 13 | 0.2385 |
| 139 | Moondream 3.1 | Moondream | `3.1` | 13 | 0.2385 |
| 141 | Gemini 3.8 Flash | Google | `3.8` | 16 | 0.2375 |
| 142 | Granite 4.0 Micro | IBM | `4.0` | 17 | 0.2353 |
| 142 | Llama Guard 4 12B | Meta | `4` | 17 | 0.2353 |
| 144 | Qwen3.5-35B-A3B | Qwen | `3.5` | 15 | 0.2333 |
| 145 | Gemini 3.7 Flash | Google | `3.7` | 16 | 0.2313 |
| 146 | Aion-3.0-Mini | AionLabs | `3.0` | 13 | 0.2308 |
| 146 | Morph V3 Fast | Morph | `3` | 13 | 0.2308 |
| 146 | Qwen3 30B A3B | Qwen | `3` | 13 | 0.2308 |
| 149 | LFM2.5-2.6B | LiquidAI | `2.5` | 11 | 0.2273 |
| 149 | Mercury 2.5 | Inception | `2.5` | 11 | 0.2273 |
| 151 | Gemini 3.6 Flash | Google | `3.6` | 16 | 0.2250 |
| 151 | MiniMax M2.7 | MiniMax | `2.7` | 12 | 0.2250 |
| 153 | Qwen3.8 2.4T A95B | Qwen | `3.8` | 17 | 0.2235 |
| 153 | Qwen3.8 Max Prime | Qwen | `3.8` | 17 | 0.2235 |
| 155 | Hy-MT2-7B | Tencent | `2` | 9 | 0.2222 |
| 155 | Mercury 2 | Inception | `2` | 9 | 0.2222 |
| 157 | Ling 3.1 Flash | inclusionAI | `3.1` | 14 | 0.2214 |
| 158 | Gemini 3.5 Flash | Google | `3.5` | 16 | 0.2188 |
| 159 | DeepSeek V4.1 Flash | DeepSeek | `4.1` | 19 | 0.2158 |
| 160 | Ling 3.0 Flash | inclusionAI | `3.0` | 14 | 0.2143 |
| 160 | Morph V3 Large | Morph | `3` | 14 | 0.2143 |
| 160 | Relace Apply 3 | Relace | `3` | 14 | 0.2143 |
| 163 | Qwen3.8 Max (0902) | Qwen | `3.8` | 18 | 0.2111 |
| 163 | Qwen3.8 Omni Flash | Qwen | `3.8` | 18 | 0.2111 |
| 165 | GPT-4o (2024-05-13) | OpenAI | `4` | 19 | 0.2105 |
| 165 | GPT-4o (2024-08-06) | OpenAI | `4` | 19 | 0.2105 |
| 165 | GPT-4o (2024-11-20) | OpenAI | `4` | 19 | 0.2105 |
| 168 | MiniMax M2.5 | MiniMax | `2.5` | 12 | 0.2083 |
| 168 | Nex-N2.5-Pro | Nex AGI | `2.5` | 12 | 0.2083 |
| 170 | GPT-3.5 Turbo 16k | OpenAI | `3.5` | 17 | 0.2059 |
| 170 | Qwen3.5 397B A17B | Qwen | `3.5` | 17 | 0.2059 |
| 170 | Qwen3.5-122B-A10B | Qwen | `3.5` | 17 | 0.2059 |
| 173 | DeepSeek V4 Pro 0423 | DeepSeek | `4` | 20 | 0.2000 |
| 173 | DeepSeek V4 Pro 0813 | DeepSeek | `4` | 20 | 0.2000 |
| 173 | Grok 4.20 Multi-Agent | SpaceXAI | `4.20` | 21 | 0.2000 |
| 173 | MiMo-V2.6-Pro | Xiaomi | `2.6` | 13 | 0.2000 |
| 173 | MiniMax M2 | MiniMax | `2` | 10 | 0.2000 |
| 173 | Mistral Small 3 | Mistral | `3` | 15 | 0.2000 |
| 173 | Seed 1.6 | ByteDance Seed | `1.6` | 8 | 0.2000 |
| 180 | Mistral Medium 3.5 | Mistral | `3.5` | 18 | 0.1944 |
| 181 | Kimi K2.7 Code | MoonshotAI | `2.7` | 14 | 0.1929 |
| 182 | MiMo-V2.5-Pro | Xiaomi | `2.5` | 13 | 0.1923 |
| 182 | Nex-N2.5-Mini | Nex AGI | `2.5` | 13 | 0.1923 |
| 184 | DeepSeek V3.2 Exp | DeepSeek | `3.2` | 17 | 0.1882 |
| 185 | DeepSeek V3 0324 | DeepSeek | `3` | 16 | 0.1875 |
| 185 | Mistral Medium 3 | Mistral | `3` | 16 | 0.1875 |
| 185 | Nemotron 3 Super | NVIDIA | `3` | 16 | 0.1875 |
| 185 | Nemotron 3 Ultra | NVIDIA | `3` | 16 | 0.1875 |
| 185 | Qwen3 Coder Next | Qwen | `3` | 16 | 0.1875 |
| 190 | DeepSeek V4 Flash 0423 | DeepSeek | `4` | 22 | 0.1818 |
| 190 | DeepSeek V4 Flash 0731 | DeepSeek | `4` | 22 | 0.1818 |
| 190 | Gemma 2 27B | Google | `2` | 11 | 0.1818 |
| 190 | Hy-MT2-1.8B | Tencent | `2` | 11 | 0.1818 |
| 190 | LongCat 2.0 | Meituan | `2.0` | 11 | 0.1818 |
| 190 | Nova 2 Lite | Amazon | `2` | 11 | 0.1818 |
| 196 | Gemini 2.5 Pro | Google | `2.5` | 14 | 0.1786 |
| 196 | LFM2.5-24B-A2B | LiquidAI | `2.5` | 14 | 0.1786 |
| 198 | Ling 3.0 Flash VL | inclusionAI | `3.0` | 17 | 0.1765 |
| 198 | Qwen3 Coder Flash | Qwen | `3` | 17 | 0.1765 |
| 200 | Laguna S 2.1 | Poolside | `2.1` | 12 | 0.1750 |
| 200 | MiniMax M2.1 | MiniMax | `2.1` | 12 | 0.1750 |
| 202 | MiMo-V2.6-Flash | Xiaomi | `2.6` | 15 | 0.1733 |
| 203 | Mistral Medium 3.1 | Mistral | `3.1` | 18 | 0.1722 |
| 204 | DeepSeek V4.1 Flash 1017 | DeepSeek | `4.1` | 24 | 0.1708 |
| 205 | Dots3-Note Preview | Dots Studio | `3` | 18 | 0.1667 |
| 205 | Gemini 3.5 Flash Lite | Google | `3.5` | 21 | 0.1667 |
| 205 | GPT-4o-mini (2024-07-18) | OpenAI | `4` | 24 | 0.1667 |
| 205 | Kimi K2 0711 | MoonshotAI | `2` | 12 | 0.1667 |
| 205 | Kimi K2 0905 | MoonshotAI | `2` | 12 | 0.1667 |
| 205 | Llama 3 8B Lunaris | Sao10K | `3` | 18 | 0.1667 |
| 205 | Nemotron 3.5 Super VL | NVIDIA | `3.5` | 21 | 0.1667 |
| 205 | o1-pro | OpenAI | `1` | 6 | 0.1667 |
| 213 | Laguna XS 2.1 | Poolside | `2.1` | 13 | 0.1615 |
| 214 | GPT-3.5 Turbo Instruct | OpenAI | `3.5` | 22 | 0.1591 |
| 214 | Nemotron 3.5 Lightning | NVIDIA | `3.5` | 22 | 0.1591 |
| 216 | Ministral 3 3B 2512 | Mistral | `3` | 19 | 0.1579 |
| 216 | Ministral 3 8B 2512 | Mistral | `3` | 19 | 0.1579 |
| 216 | Moondream 3 Preview | Moondream | `3` | 19 | 0.1579 |
| 219 | Llama 3.3 Euryale 70B | Sao10K | `3.3` | 21 | 0.1571 |
| 220 | Gemini 2.5 Flash | Google | `2.5` | 16 | 0.1562 |
| 221 | Fugu Ultra v2 | Sakana | `2` | 13 | 0.1538 |
| 221 | Seed-2.0-Code | ByteDance Seed | `2.0` | 13 | 0.1538 |
| 221 | Seed-2.0-Lite | ByteDance Seed | `2.0` | 13 | 0.1538 |
| 221 | Seed-2.0-Mini | ByteDance Seed | `2.0` | 13 | 0.1538 |
| 225 | Llama 3.2 1B Instruct | Meta | `3.2` | 21 | 0.1524 |
| 225 | Llama 3.2 3B Instruct | Meta | `3.2` | 21 | 0.1524 |
| 225 | Mistral Small 3.2 24B | Mistral | `3.2` | 21 | 0.1524 |
| 228 | Qwen3.5 Plus 2026-02-15 | Qwen | `3.5` | 23 | 0.1522 |
| 228 | Qwen3.5 Plus 2026-04-20 | Qwen | `3.5` | 23 | 0.1522 |
| 230 | Llama 3.3 70B Instruct | Meta | `3.3` | 22 | 0.1500 |
| 230 | Ministral 3 14B 2512 | Mistral | `3` | 20 | 0.1500 |
| 230 | Mistral Large 3 2512 | Mistral | `3` | 20 | 0.1500 |
| 230 | Nemotron 3 Nano Omni | NVIDIA | `3` | 20 | 0.1500 |
| 230 | Qwen3 VL 8B Instruct | Qwen | `3` | 20 | 0.1500 |
| 230 | Seed 2.1 Turbo | ByteDance Seed | `2.1` | 14 | 0.1500 |
| 236 | Gemini 3.1 Flash Lite | Google | `3.1` | 21 | 0.1476 |
| 236 | Llama 3.1 8B Instruct | Meta | `3.1` | 21 | 0.1476 |
| 236 | Mistral Small 3.1 24B | Mistral | `3.1` | 21 | 0.1476 |
| 239 | DeepSeek V4 Flash Vision Exp | DeepSeek | `4` | 28 | 0.1429 |
| 239 | Ember-1 | Fireworks | `1` | 7 | 0.1429 |
| 239 | Hermes 3 70B Instruct | Nous | `3` | 21 | 0.1429 |
| 239 | Hy-MT2-30B-A3B | Tencent | `2` | 14 | 0.1429 |
| 239 | MiniMax M2-her | MiniMax | `2` | 14 | 0.1429 |
| 239 | Qwen3 Coder 480B A35B | Qwen | `3` | 21 | 0.1429 |
| 239 | R1 0528 | DeepSeek | `1` | 7 | 0.1429 |
| 239 | Skyfall 36B V2 | TheDrummer | `2` | 14 | 0.1429 |
| 247 | DeepSeek V3.1 Terminus | DeepSeek | `3.1` | 22 | 0.1409 |
| 247 | Gemini 3.1 Pro Preview | Google | `3.1` | 22 | 0.1409 |
| 247 | Llama 3.1 70B Instruct | Meta | `3.1` | 22 | 0.1409 |
| 250 | Gemini 3 Flash Preview | Google | `3` | 22 | 0.1364 |
| 250 | Hermes 3 405B Instruct | Nous | `3` | 22 | 0.1364 |
| 252 | Devstral 2 2512 | Mistral | `2` | 15 | 0.1333 |
| 253 | Qwen2.5 7B Instruct | Qwen | `2.5` | 19 | 0.1316 |
| 254 | Nemotron 3 Nano 30B A3B | NVIDIA | `3` | 23 | 0.1304 |
| 255 | GPT-3.5 Turbo (older v0613) | OpenAI | `3.5` | 27 | 0.1296 |
| 255 | Nemotron 3.5 Content Safety | NVIDIA | `3.5` | 27 | 0.1296 |
| 257 | Kimi K2 Thinking | MoonshotAI | `2` | 16 | 0.1250 |
| 257 | Qwen2.5 72B Instruct | Qwen | `2.5` | 20 | 0.1250 |
| 257 | WizardLM-2 8x22B | Microsoft | `2` | 16 | 0.1250 |
| 260 | Qwen3 VL 30B A3B Instruct | Qwen | `3` | 25 | 0.1200 |
| 260 | Qwen3 VL 30B A3B Thinking | Qwen | `3` | 25 | 0.1200 |
| 262 | Llama 3.1 Euryale 70B v2.2 | Sao10K | `3.1` | 26 | 0.1192 |
| 263 | Gemini 2.5 Flash Lite | Google | `2.5` | 21 | 0.1190 |
| 264 | Seed 1.6 Flash | ByteDance Seed | `1.6` | 14 | 0.1143 |
| 265 | Qwen3 30B A3B Instruct 2507 | Qwen | `3` | 27 | 0.1111 |
| 265 | Qwen3 Next 80B A3B Instruct | Qwen | `3` | 27 | 0.1111 |
| 265 | Qwen3 Next 80B A3B Thinking | Qwen | `3` | 27 | 0.1111 |
| 265 | Qwen3 VL 235B A22B Instruct | Qwen | `3` | 27 | 0.1111 |
| 269 | Qwen2.5 VL 72B Instruct | Qwen | `2.5` | 23 | 0.1087 |
| 270 | MiMo-V2.6-Pro-UltraSpeed | Xiaomi | `2.6` | 24 | 0.1083 |
| 271 | Qwen3 Coder 30B A3B Instruct | Qwen | `3` | 28 | 0.1071 |
| 272 | Gemini 3.1 Flash Lite Preview | Google | `3.1` | 29 | 0.1069 |
| 273 | Schematron V2 Small | Inference.net | `2` | 19 | 0.1053 |
| 273 | Schematron V2 Turbo | Inference.net | `2` | 19 | 0.1053 |
| 275 | Qwen3 235B A22B Instruct 2507 | Qwen | `3` | 29 | 0.1034 |
| 275 | Qwen3 235B A22B Thinking 2507 | Qwen | `3` | 29 | 0.1034 |
| 277 | MiniMax M1 | MiniMax | `1` | 10 | 0.1000 |
| 277 | MiniMax-01 | MiniMax | `01` | 10 | 0.1000 |
| 277 | Ternary Bonsai 2 27B | PrismML | `2` | 20 | 0.1000 |
| 280 | Qwen2.5 Coder 32B Instruct | Qwen | `2.5` | 26 | 0.0962 |
| 281 | Perceptron Mk1.5 | Perceptron | `1.5` | 16 | 0.0938 |
| 282 | Muse Spark 1.3 | Meta | `1.3` | 14 | 0.0929 |
| 283 | Gemini 2.5 Pro Preview 06-05 | Google | `2.5` | 28 | 0.0893 |
| 284 | Gemini 3.1 Pro Preview Custom Tools | Google | `3.1` | 35 | 0.0886 |
| 285 | Muse Spark 1.2 | Meta | `1.2` | 14 | 0.0857 |
| 286 | Nova Pro 1.0 | Amazon | `1.0` | 12 | 0.0833 |
| 287 | Muse Spark 1.1 | Meta | `1.1` | 14 | 0.0786 |
| 288 | Nova Lite 1.0 | Amazon | `1.0` | 13 | 0.0769 |
| 289 | Nova Micro 1.0 | Amazon | `1.0` | 14 | 0.0714 |
| 289 | Perceptron Mk1 | Perceptron | `1` | 14 | 0.0714 |
| 291 | Aion-RP 1.0 (8B) | AionLabs | `1.0` | 16 | 0.0625 |
| 291 | Nova Premier 1.0 | Amazon | `1.0` | 16 | 0.0625 |
| 293 | Beam 1.0 501B A23B | Reflection | `1.0` | 18 | 0.0556 |
| 294 | Muse Spark 1.3 Contributor | Meta | `1.3` | 26 | 0.0500 |
| 295 | Muse Spark 1.2 Contributor | Meta | `1.2` | 26 | 0.0462 |
| 296 | Grok Build 0.1 | SpaceXAI | `0.1` | 14 | 0.0071 |

## 4. Vendor Analysis

Vendors with at least 3 evaluated models. *Velocity* is the OLS slope of GI against listing date (generations per year).

| Vendor | Models | GI coverage | Max GI | Median GI | Mean NL | Velocity |
| :-- | --: | --: | --: | --: | --: | --: |
| OpenAI | 60 | 93% | 6.1 | 5.1 | 12.1 | +0.92 |
| Anthropic | 15 | 100% | 5.5 | 4.8 | 15.4 | +1.01 |
| Z.ai | 16 | 100% | 5.3 | 5 | 9.4 | +0.77 |
| StepFun | 3 | 100% | 5 | 3.7 | 14.0 | +2.20 |
| SpaceXAI | 7 | 100% | 4.7 | 4.3 | 10.9 | +2.16 |
| DeepSeek | 15 | 100% | 4.1 | 3.2 | 17.1 | +1.28 |
| TheDrummer | 3 | 67% | 4.1 | 3.05 | 14.7 | — |
| Google | 21 | 100% | 4 | 3.1 | 17.9 | +0.76 |
| Mistral | 20 | 65% | 4 | 3 | 16.9 | +0.49 |
| Meta | 16 | 81% | 4 | 3.1 | 18.1 | -1.13 |
| Tencent | 7 | 86% | 4 | 2.5 | 11.4 | -1.29 |
| Nous | 3 | 100% | 4 | 3 | 18.7 | +0.98 |
| Upstage | 3 | 100% | 4 | 4 | 11.3 | +1.63 |
| Qwen | 42 | 98% | 3.8 | 3.5 | 18.0 | +0.72 |
| NVIDIA | 7 | 100% | 3.5 | 3 | 20.7 | +0.74 |
| AionLabs | 6 | 100% | 3.5 | 3 | 11.0 | +1.53 |
| Sao10K | 3 | 100% | 3.3 | 3.1 | 21.7 | +0.79 |
| inclusionAI | 3 | 100% | 3.1 | 3 | 15.0 | +0.43 |
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

Codestral 2508 (`mistralai/codestral-2508`), Command A (`cohere/command-a`), Command A+ (`cohere/command-a-plus`), Command R (08-2024) (`cohere/command-r-08-2024`), Command R+ (08-2024) (`cohere/command-r-plus-08-2024`), Command R7B (12-2024) (`cohere/command-r7b-12-2024`), Extract (`scaledown/extract`), Fugu Max (`sakana/fugu-max`), Fugu Ultra (`sakana/fugu-ultra`), Glimpse (`elorian/glimpse`), GPT Chat Latest (`openai/gpt-chat-latest`), gpt-oss-120b (`openai/gpt-oss-120b`), gpt-oss-20b (`openai/gpt-oss-20b`), gpt-oss-safeguard-20b (`openai/gpt-oss-safeguard-20b`), Hunyuan A13B Instruct (`tencent/hunyuan-a13b-instruct`), Inkling (`thinkingmachines/inkling`), Inkling Small (`thinkingmachines/inkling-small`), Mistral Large (`mistralai/mistral-large`), Mistral Large 2407 (`mistralai/mistral-large-2407`), Mistral Nemo (`mistralai/mistral-nemo`), Mixtral 8x22B Instruct (`mistralai/mixtral-8x22b-instruct`), Muse Glimmer 30B (`meta/muse-glimmer-30b`), Muse Spark Open (`meta/muse-spark-open`), Muse Wonder (`meta/muse-wonder`), MythoMax 13B (`gryphe/mythomax-l2-13b`), North Mini Code (`cohere/north-mini-code`), Qwen-Plus (`qwen/qwen-plus`), Reka Edge (`rekaai/reka-edge`), Relace Search (`relace/relace-search`), ReMM SLERP 13B (`undi95/remm-slerp-l2-13b`), Saba (`mistralai/mistral-saba`), Sakana Namazu (`sakana/sakana-namazu`), Sonar (`perplexity/sonar`), Sonar Deep Research (`perplexity/sonar-deep-research`), Sonar Pro (`perplexity/sonar-pro`), Sonar Pro Search (`perplexity/sonar-pro-search`), Sonar Reasoning Pro (`perplexity/sonar-reasoning-pro`), Summarize (`scaledown/summarize`), Trinity Large Thinking (`arcee-ai/trinity-large-thinking`), UI-TARS 7B (`bytedance/ui-tars-1.5-7b`), Uncensored (`cognitivecomputations/dolphin-mistral-24b-venice-edition`), UnslopNemo 12B (`thedrummer/unslopnemo-12b`), Voxtral Small 24B 2507 (`mistralai/voxtral-small-24b-2507`), Weaver (alpha) (`mancer/weaver`)

## 6. Figures

![Vendor champions](figures/vendor_champions.svg)

Complete per-model bar charts: [Track A (GI)](figures/full_gi.svg) · [Track B (NL)](figures/full_nl.svg)

![Figure 1](figures/gi_over_time.svg)

![Figure 2](figures/gi_vs_nl.svg)

---

Full per-model data: [`latest.csv`](latest.csv) · [`latest.json`](latest.json)
