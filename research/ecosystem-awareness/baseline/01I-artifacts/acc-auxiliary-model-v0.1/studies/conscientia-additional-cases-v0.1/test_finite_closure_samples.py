"""Finite numeric evidence for the existing local-closure calculation."""
from copy import deepcopy
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import unittest

import campaign as source

CASES = json.loads(Path(__file__).with_name("CASES.json").read_text(encoding="utf-8"))["cases"]
BAD_NUMBERS = (float("nan"), float("inf"), float("-inf"), True, False,
               None, "UNKNOWN", "1", {}, [])


def sample():
    return deepcopy(next(c for c in CASES if c["kind"] == "closure" and c["L"] is not None))


class FiniteClosureSampleTests(unittest.TestCase):
    def test_each_sample_field_is_finite_regardless_of_sample_order(self):
        base = sample()
        labels = ("sample_position", "sample_lower", "sample_upper")
        for index in range(len(base["samples"])):
            for field, label in enumerate(labels):
                for value in BAD_NUMBERS:
                    case = deepcopy(base)
                    case["samples"][index][field] = value
                    with self.subTest(index=index, field=field, value=repr(value)):
                        with self.assertRaisesRegex(ValueError, label):
                            source.result(case)
                        self.assertIs(case["samples"][index][field], value)

    def test_finite_samples_cannot_emit_overflowed_projected_bounds(self):
        for bounds, label in (((-1e308, 0), "projected_lower"),
                              ((0, 1e308), "projected_upper")):
            case = sample()
            case.update(L=1e308, x=1, samples=[[0, *bounds]])
            with self.subTest(label=label):
                with self.assertRaisesRegex(ValueError, label):
                    source.result(case)
        case = sample()
        case.update(L=1, x=1e308, samples=[[-1e308, 0, 1]])
        with self.assertRaisesRegex(ValueError, "projected_lower"):
            source.result(case)

    def test_unestablished_regularity_retains_existing_unknown_path(self):
        base = sample()
        base["L"] = None
        supported = source.result(base)
        self.assertEqual(supported["status"], "REGULARITY_NOT_ESTABLISHED")
        self.assertIsNone(supported["bounds"])
        for value in BAD_NUMBERS:
            case = deepcopy(base)
            case["samples"] = [[value, value, value]]
            with self.subTest(value=repr(value)):
                self.assertEqual(source.result(case), supported)

    def test_original_finite_controls_keep_complete_results(self):
        reports = []
        for case in CASES:
            if case["kind"] != "closure":
                continue
            for L, x, threshold, shift in product((None, 0, .5, 1, 2),
                                                  (-1, 0, 1, 2, 3),
                                                  (0, 7, 9, 12), (-20, 0, 20)):
                item = deepcopy(case)
                item.update(L=L, x=x, threshold=threshold)
                item["samples"] = [[p, l + shift, u + shift] for p, l, u in item["samples"]]
                reports.append({"id": item["id"], "parameters": [L, x, threshold, shift],
                                "result": source.result(item)})
        self.assertEqual(len(reports), 900)
        digest = sha256(json.dumps(reports, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        # Complete result dictionaries from captured parent #103 215dbd1.
        self.assertEqual(digest, "d88fe4d0e6de8cec9a497abf9850c4575484fb187568e7bd93b05a02153715a6")


if __name__ == "__main__":
    unittest.main()
