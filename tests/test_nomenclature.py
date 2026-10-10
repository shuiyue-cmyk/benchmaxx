"""Conformance tests for the nomenclature rules in METHODOLOGY.md sections 3 and 4."""

import unittest

from benchmaxx.evaluate import Entry, _assign_ranks, exclusion_reason
from benchmaxx.nomenclature import extract_generation, nomenclature_length, split_display_name


class CanonicalNameTests(unittest.TestCase):
    def test_vendor_prefix_is_removed(self):
        self.assertEqual(split_display_name("OpenAI: GPT-5.5", "openai/gpt-5.5"), ("OpenAI", "GPT-5.5"))

    def test_name_without_prefix(self):
        self.assertEqual(split_display_name("Mistral Large 2407", "mistralai/mistral-large-2407"),
                         (None, "Mistral Large 2407"))

    def test_routing_variant_tag_is_removed(self):
        self.assertEqual(split_display_name("Google: Gemma 4 31B (free)", "google/gemma-4-31b-it:free")[1], "Gemma 4 31B")
        self.assertEqual(split_display_name("Anthropic: Claude Opus 5.5 (batch)", "anthropic/claude-opus-5.5:batch")[1],
                         "Claude Opus 5.5")

    def test_other_parentheticals_are_part_of_the_name(self):
        self.assertEqual(split_display_name("Mancer: Weaver (alpha)", "mancer/weaver")[1], "Weaver (alpha)")

    def test_whitespace_is_normalised(self):
        self.assertEqual(split_display_name("Google: Gemma 4 26B A4B ", "google/gemma-4-26b-a4b-it")[1], "Gemma 4 26B A4B")

    def test_length_counts_code_points(self):
        self.assertEqual(nomenclature_length("o3"), 2)
        self.assertEqual(nomenclature_length("通义千问 3"), 6)


class GenerationIndexTests(unittest.TestCase):
    CASES = {
        # plain and glued version numbers
        "GPT-5.5": "5.5", "Claude Opus 4.8": "4.8", "Qwen3.8 Max Prime": "3.8", "Kimi K2.6": "2.6",
        "MiMo-V2.6-Pro-UltraSpeed": "2.6", "o3": "3", "GPT-4o-mini": "4", "Perceptron Mk1.5": "1.5",
        "GLM 5V Turbo": "5", "Hy3": "3", "Dots3-Note Preview": "3", "MiniMax-01": "01",
        # decimal interpretation keeps the raw string
        "Grok 4.20 Multi-Agent": "4.20", "Pareto 26.10 Preview": "26.10",
        # parameter counts and context sizes are skipped
        "Qwen3.8 2.4T A95B": "3.8", "LFM2.5-2.6B": "2.5", "Hy-MT2-1.8B": "2", "Cydonia 24B V4.1": "4.1",
        "GPT-3.5 Turbo 16k": "3.5", "WizardLM-2 8x22B": "2",
        # snapshot stamps and dates are skipped
        "Kimi K2 0905": "2", "Ministral 3 14B 2512": "3", "Gemini 2.5 Pro Preview 06-05": "2.5",
        "Qwen3.5 Plus 2026-04-20": "3.5", "GPT-4o (2024-11-20)": "4",
        # parenthetical content is ignored
        "Aion-RP 1.0 (8B)": "1.0",
    }
    DNQ = ["gpt-oss-120b", "Command R7B (12-2024)", "Mixtral 8x22B Instruct", "Mistral Large 2407",
           "Codestral 2508", "UI-TARS 7B", "Sonar Pro", "Hunyuan A13B Instruct"]

    def test_generation_extraction(self):
        for name, expected in self.CASES.items():
            with self.subTest(name=name):
                generation = extract_generation(name)
                self.assertIsNotNone(generation)
                self.assertEqual(generation.raw, expected)

    def test_did_not_qualify(self):
        for name in self.DNQ:
            with self.subTest(name=name):
                self.assertIsNone(extract_generation(name))

    def test_decimal_interpretation_principle(self):
        self.assertEqual(extract_generation("Grok 4.20").value, 4.2)
        self.assertLess(extract_generation("Grok 4.20").value, extract_generation("Grok 4.7").value)
        self.assertEqual(extract_generation("MiniMax-01").value, 1.0)


class PopulationTests(unittest.TestCase):
    @staticmethod
    def model(model_id, prompt="0.000001", outputs=("text",)):
        return {"id": model_id, "pricing": {"prompt": prompt}, "architecture": {"output_modalities": list(outputs)}}

    def test_exclusions(self):
        self.assertEqual(exclusion_reason(self.model("~openai/gpt-latest")), "alias")
        self.assertEqual(exclusion_reason(self.model("openrouter/auto")), "platform router")
        self.assertEqual(exclusion_reason(self.model("nvidia/switchyard", prompt="-1")), "meta-router (variable pricing)")
        self.assertEqual(exclusion_reason(self.model("google/nano-banana", outputs=("image", "text"))), "non-text output")
        self.assertIsNone(exclusion_reason(self.model("openai/gpt-5.5")))

    def test_competition_ranking(self):
        entries = [Entry(model_id=str(i), display_name="", canonical_name="", vendor="", vendor_slug="",
                         released="2026-01-01", slugs=[], endpoints=1, gi_raw=None, gi=gi, nl=1, ne=None)
                   for i, gi in enumerate([6.1, 5.5, 6.1, None, 4.0])]
        _assign_ranks(entries, "gi", "rank_gi")
        self.assertEqual([e.rank_gi for e in entries], [1, 3, 1, None, 4])


if __name__ == "__main__":
    unittest.main()
