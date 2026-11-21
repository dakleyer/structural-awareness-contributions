"""L-13: enforce the declared nonnegative Lipschitz-constant domain."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

import campaign as source

CASES = json.loads(Path(__file__).with_name("CASES.json").read_text(encoding="utf-8"))["cases"]


def sample():
    return deepcopy(next(c for c in CASES if c["id"] == "CLOSURE-02-CROSSES-THRESHOLD"))


class LipschitzDomainTests(unittest.TestCase):
    def test_negative_constants_cannot_certify_or_project(self):
        for value in (-.4, -1, -5e-324, -1e308):
            case = sample()
            case["L"] = value
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "nonnegative Lipschitz"):
                    source.result(case)
                self.assertEqual(case["L"], value)
        case = sample()
        case.update(L=-.4, samples=None)
        with self.assertRaisesRegex(ValueError, "nonnegative Lipschitz"):
            source.result(case)

    def test_zero_including_signed_zero_retains_constant_function_evidence(self):
        for value in (0, 0.0, -0.0):
            case = sample()
            case["L"] = value
            result = source.result(case)
            self.assertEqual(result["bounds"], [9.0, 10.0])
            self.assertEqual(result["status"], "PREDICATE_SUPPORTED_IN_FRAME")
            self.assertIs(result["global_D_open"], True)

    def test_positive_and_unestablished_regularity_keep_existing_results(self):
        for value, bounds in ((.4, [8.6, 10.4]), (1, [8.0, 11.0])):
            case = sample()
            case["L"] = value
            result = source.result(case)
            self.assertEqual(result["bounds"], bounds)
            self.assertEqual(result["status"], "PREDICATE_UNDETERMINED")
            self.assertIs(result["global_D_open"], True)
        case = sample()
        case.update(L=None, samples=None)
        result = source.result(case)
        self.assertEqual(result["status"], "REGULARITY_NOT_ESTABLISHED")
        self.assertIsNone(result["bounds"])


if __name__ == "__main__":
    unittest.main()
