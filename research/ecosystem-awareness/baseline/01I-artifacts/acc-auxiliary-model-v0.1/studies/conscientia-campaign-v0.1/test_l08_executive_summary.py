"""L08 portable summary integrity and source-driven 7x7 threshold map."""
from __future__ import annotations

from copy import deepcopy
import builtins
from fractions import Fraction
from hashlib import sha256
import unittest
from unittest.mock import patch

from l08_robustness import run
from l08_executive_summary import summarize, as_markdown
import l08_executive_summary as presentation
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
MANIFEST=json.loads((HERE/"L08_PROTOCOL.json").read_text(encoding="utf-8"))


class PortableExperimentalReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw=run(MANIFEST)
        cls.s=summarize(cls.raw)
        cls.byid={row["panel"]:row for row in cls.s["panels"]}

    def test_published_default_summary_is_unchanged(self):
        digest = sha256(json.dumps(self.s, sort_keys=True,
                                  separators=(",", ":")).encode()).hexdigest()
        self.assertEqual(digest,
                         "4d3da83ce13e0081ddf1d7442404b244b9f30bec7a6cd014f3007dbbcf3707dd")

    def test_source_owned_original_accuracy_surfaces_not_hand_entered(self):
        self.assertEqual(self.s["total_grid_cells"],98)
        self.assertEqual(self.s["paired_evaluations"],18816)
        self.assertEqual(len(self.s["price_contracts"]),4)
        self.assertEqual(self.s["source_manifest_sha256"],self.raw["manifest_sha256"])
        self.assertEqual(len(self.raw["source_engine_sha256"]),3)
        self.assertTrue(all(len(v)==64 for v in
                            self.raw["source_engine_sha256"].values()))
        self.assertEqual(len(self.byid),2)
        self.assertEqual(self.s["independent_real_world_source_accuracy_evidence"],
                         "NOT_AVAILABLE")

    def test_original_access_asymmetry_survives_fair_provenance_check(self):
        x=self.byid["HISTORICAL_ACCESS_AND_QUALIFICATION"]
        counts=x["two_axis_verdict_counts"]
        self.assertEqual(counts,{
            "BOUNDARY_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES":15,
            "DOMAIN_FACTS_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES":22,
            "INCOMPARABLE_ERROR_VS_MISSED_OPPORTUNITY_TRADEOFF":12,
        })
        self.assertEqual(sum(counts.values()),49)
        self.assertEqual(x["critical_endpoints"]["1|1"]["two_axis_result"],"D")

    def test_matched_availability_yields_conditional_reversals_and_tie(self):
        x=self.byid["EQUAL_PUBLIC_SOURCE_AND_DOMAIN_AVAILABILITY"]
        counts=x["two_axis_verdict_counts"]
        self.assertEqual(counts,{
            "BOUNDARY_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES":13,
            "DOMAIN_FACTS_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES":9,
            "INCOMPARABLE_ERROR_VS_MISSED_OPPORTUNITY_TRADEOFF":26,
            "TIE_ON_ERRORS_AND_MISSED_CANDIDATES":1,
        })
        self.assertEqual(x["critical_endpoints"]["1|1/2"]["two_axis_result"],"B")
        self.assertEqual(x["critical_endpoints"]["1/2|1"]["two_axis_result"],"D")
        self.assertEqual(x["critical_endpoints"]["1|1"]["two_axis_result"],"T")
        self.assertEqual(len(x["classification_matrix"]),7)
        self.assertTrue(all(len(row["values"])==7 for row in x["classification_matrix"]))

    def test_memberships_can_change_only_through_price_without_changing_physics(self):
        x=self.byid["EQUAL_PUBLIC_SOURCE_AND_DOMAIN_AVAILABILITY"]
        memberships=x["three_axis_membership_by_price_contract"]
        self.assertEqual(set(memberships),set(self.s["price_contracts"]))
        # The same physically perfect source B can be on a cost frontier under
        # one synthetic schedule, not another.
        cheap=memberships["SOURCE_CHEAP_ORIGINAL"]["SOURCE_BOUNDARY_ONLY"]
        expensive=memberships["SOURCE_EXPENSIVE_DIRECT_CHEAP"]["SOURCE_BOUNDARY_ONLY"]
        self.assertGreater(cheap,expensive)
        self.assertEqual(x["without_price_pareto_membership"]["SOURCE_BOUNDARY_ONLY"],19)
        self.assertEqual(cheap,49)
        self.assertEqual(expensive,18)
        self.assertEqual(sum(x["two_axis_verdict_counts"].values()),49)

    def test_report_is_non_private_and_readable_without_synthetic_generalisation(self):
        md=as_markdown(self.s)
        self.assertIn("18816",md)
        self.assertIn("EQUAL_PUBLIC_SOURCE_AND_DOMAIN_AVAILABILITY",md)
        self.assertIn("INCOMPARABLE_ERROR_VS_MISSED_OPPORTUNITY_TRADEOFF",md)
        self.assertIn("SOURCE_BOUNDARY_ONLY",md)
        self.assertNotIn("truth_PRIVATE_FOR_REFEREE_ONLY",json.dumps(self.s))
        self.assertIn("ni demuestra prioridad causal",md)

    def test_incomplete_grid_is_rejected_not_filled_by_default(self):
        s=deepcopy(self.raw)
        s["panels"][0]["cells"].pop()
        with self.assertRaisesRegex(ValueError,"missing grid records"):
            summarize(s)
        s=deepcopy(self.raw)
        s["panels"][0]["cells"][1]["assumed_per_domain_observation_accuracy"]=(
            s["panels"][0]["cells"][0]["assumed_per_domain_observation_accuracy"])
        with self.assertRaisesRegex(ValueError,"duplicate source/domain grid"):
            summarize(s)




class ExactProbabilityPresentation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        manifest = deepcopy(MANIFEST)
        manifest["worlds_per_grid_cell"] = 16
        manifest["panels"] = manifest["panels"][:1]
        manifest["accuracy_grid"] = ["1/3", "0.3333333333333333333333333334"]
        cls.raw = run(manifest)
        cls.expected = list(manifest["accuracy_grid"])

    @staticmethod
    def reverse_set_iteration(values, *args, **kwargs):
        # A set has no promised iteration order. Exercise its adverse order
        # deterministically, without depending on a platform's hash seed.
        if isinstance(values, set) and kwargs.get("key") is not None:
            values = builtins.sorted(values, key=Fraction, reverse=True)
        return builtins.sorted(values, *args, **kwargs)

    def ordered_summary(self):
        with patch.object(presentation, "sorted", self.reverse_set_iteration, create=True):
            return summarize(self.raw)

    def test_distinct_source_probabilities_keep_their_exact_order(self):
        self.assertLess(Fraction(self.expected[0]), Fraction(self.expected[1]))
        self.assertEqual(float(Fraction(self.expected[0])),
                         float(Fraction(self.expected[1])))
        panel = self.ordered_summary()["panels"][0]
        self.assertEqual(panel["q_accuracy_rows"], self.expected)
        self.assertEqual([row["source_accuracy"] for row in panel["classification_matrix"]],
                         self.expected)

    def test_distinct_domain_probabilities_keep_their_exact_order(self):
        panel = self.ordered_summary()["panels"][0]
        self.assertEqual(panel["domain_accuracy_columns"], self.expected)

    def test_markdown_keeps_the_exact_axis_labels_and_row_order(self):
        text = as_markdown(self.ordered_summary())
        header = "| Q \\ dominio |" + "|".join(self.expected) + "|"
        self.assertIn(header, text)
        first = text.index("| " + self.expected[0] + " |")
        second = text.index("| " + self.expected[1] + " |")
        self.assertLess(first, second)


if __name__=="__main__":
    unittest.main()

