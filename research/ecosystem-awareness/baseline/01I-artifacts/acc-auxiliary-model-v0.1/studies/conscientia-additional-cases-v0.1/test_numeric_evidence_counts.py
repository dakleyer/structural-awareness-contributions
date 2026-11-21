"""Count-input regressions for the existing mission and finite-support rules."""
from copy import deepcopy
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import unittest

import campaign as source

CASES = json.loads(Path(__file__).with_name("CASES.json").read_text(encoding="utf-8"))["cases"]
BAD_COUNTS = (float("nan"), float("inf"), float("-inf"), True, False,
              "UNKNOWN", "3", {}, [])


def mission():
    return deepcopy(next(c for c in CASES if c["kind"] == "mission"
                         and c["authorized_change"] is True))


class NumericEvidenceCountTests(unittest.TestCase):
    def test_consumed_mission_count_must_be_finite_numeric_evidence(self):
        for value in BAD_COUNTS:
            case = mission()
            case["actual_independent"] = value
            with self.subTest(value=repr(value)):
                with self.assertRaisesRegex(ValueError, "actual_independent"):
                    source.result(case)
                self.assertIs(case["actual_independent"], value)

    def test_unconsumed_count_does_not_erase_known_control_outcome(self):
        for key in ("authorized_change", "source_basis_valid"):
            for value in BAD_COUNTS:
                case = mission()
                case[key] = False
                case["actual_independent"] = value
                with self.subTest(key=key, value=repr(value)):
                    result = source.result(case)
                    self.assertEqual(result["status"], "UNSUPPORTED_MISSION_CHANGE")
                    self.assertIs(result["mission_change"], False)
                    self.assertIs(result["source_independent"], value)

    def test_explicit_unknown_count_and_existing_threshold_are_preserved(self):
        case = mission()
        case["actual_independent"] = None
        result = source.result(case)
        self.assertEqual(result["status"], "MISSION_BASIS_NOT_ESTABLISHED")
        self.assertIsNone(result["mission_change"])
        for value, expected in ((2 - 2**-51, False), (2, True), (2 + 2**-51, True)):
            case = mission()
            case["actual_independent"] = value
            self.assertIs(source.result(case)["mission_change"], expected)

    def test_boolean_values_are_not_integer_support_cardinalities(self):
        base = deepcopy(next(c for c in CASES if c["kind"] == "kl"))
        for key in ("m", "n"):
            for value in (True, False, None, 1.0, "1", float("nan"), float("inf")):
                case = deepcopy(base)
                case.update(m=2, n=1)
                case[key] = value
                with self.subTest(key=key, value=repr(value)):
                    with self.assertRaisesRegex(ValueError, "kl finite support"):
                        source.result(case)
        case = deepcopy(base)
        case.update(m=True, n=True)
        with self.assertRaisesRegex(ValueError, "kl finite support"):
            source.result(case)

    def test_existing_finite_mission_and_integer_support_results_are_unchanged(self):
        reports = []
        for case in CASES:
            if case["kind"] == "mission":
                for flags in product((False, True), repeat=2):
                    for count in (-1, 0, .5, 1, 1.5, 2, 2.5, 3, 1000):
                        item = deepcopy(case)
                        item["authorized_change"], item["source_basis_valid"] = flags
                        item["actual_independent"] = count
                        reports.append({"id": item["id"], "flags": flags, "count": count,
                                        "result": source.result(item)})
            elif case["kind"] == "kl":
                for m in range(1, 10):
                    for n in range(1, m + 1):
                        item = deepcopy(case)
                        item.update(m=m, n=n)
                        reports.append({"id": item["id"], "m": m, "n": n,
                                        "result": source.result(item)})
        self.assertEqual(len(reports), 198)
        digest = sha256(json.dumps(reports, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        # Complete result dictionaries from captured parent #104 c0043e6.
        self.assertEqual(digest, "d671dd570e451254edefa29283a89120fe1ba0a23f41e10c12f87e75af84791a")


if __name__ == "__main__":
    unittest.main()
