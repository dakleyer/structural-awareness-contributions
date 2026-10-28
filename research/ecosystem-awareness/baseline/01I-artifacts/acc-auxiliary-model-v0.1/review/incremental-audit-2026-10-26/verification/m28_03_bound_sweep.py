"""M28-03 reconfirmation and L-01 (round 23): utility lower bound in assess_candidate.

Usage: python3 -B m28_03_bound_sweep.py <studies/mathematical-lineage-social-agentic-v0.1 on PR #60>

Feeds 32 values as source_value_lower_bound with every other gate open
(received, link qualified, action authorized, budget ok). Expected on PR #60
8cd78d58: every non-finite or non-numeric value -> UTILITY_NOT_ESTABLISHED
(M28-03 repaired); 0.75 -> no strict gain; the next float above 0.75 -> gain.
L-01: finite bounds above 1 (1.5, 1e308, 10**21) still reach the positive
status although the geometry score G is confined to [0, 1]. Exit code 1 if a
non-finite or non-numeric value reaches the positive status. Writes nothing.
"""
import math
import sys
from decimal import Decimal
from fractions import Fraction

sys.path.insert(0, sys.argv[1])
import test_theme18_candidate_admission as t  # noqa: E402

OPEN = dict(received_after_exchange=True, source_to_value_link_qualified=True,
            action_authorized=True, decision_budget_ok=True)
POSITIVE = "SCOPED_PROPOSAL_FOR_EXTERNAL_ACTION_CHECK"
INVALID = [float("nan"), float("inf"), float("-inf"), True, False, "0.9", b"0.9", None,
           [0.9], (0.9,), {}, 1 + 0j, Decimal("NaN"), Decimal("sNaN"), Decimal("Infinity"),
           Decimal("-Infinity")]
VALID = [-0.0, Decimal("0.9"), Decimal("0.75"), Fraction(9, 10), Fraction(3, 4), 0.75,
         math.nextafter(0.75, 1), 0.9, 1.0, 1.5, 10 ** 21, -1, 0, 1, 1e308, 5e-324]


def status(value):
    try:
        return t.assess_candidate(t.reports(), source_value_lower_bound=value, **OPEN)["candidate_status"]
    except Exception as exc:  # a crash is reported, never counted as positive
        return f"RAISES {type(exc).__name__}"


bad = 0
for v in INVALID:
    s = status(v)
    bad += s == POSITIVE
    print(f"invalid  {repr(v)[:22]:24s} {s}")
for v in VALID:
    s = status(v)
    flag = "   <- L-01: above the [0, 1] range of G" if s == POSITIVE and v > 1 else ""
    print(f"numeric  {repr(v)[:22]:24s} {s}{flag}")
print(f"cases: {len(INVALID) + len(VALID)} | invalid values reaching the positive status: {bad}")
sys.exit(1 if bad else 0)
