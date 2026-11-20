"""L-01 (round 37): codomain guard in PR #83 against its parent PR #60 7fc88e2e.

Usage: python3 -B l01_codomain_check.py <study dir on PR #60 parent> <study dir on PR #83>
       (study dir = studies/mathematical-lineage-social-agentic-v0.1)

1. Codomain of the geometry score over [0,1]^4 from the unchanged adapter.
2. Values just above 1 (next float, 1001/1000, 1 + 10^-12, Decimal 1 + 10^-19)
   and far above (1.5, 1e21, 1e308) -> must be UTILITY_NOT_ESTABLISHED; 1 stays positive.
3. Every bound from -0.50 to 1.00 in hundredths classifies identically before and after.
Exit code 1 on any failure. Writes nothing.
"""
import importlib
import math
import sys
from decimal import Decimal
from fractions import Fraction as F

OPEN = dict(received_after_exchange=True, source_to_value_link_qualified=True,
            action_authorized=True, decision_budget_ok=True)
POS, NOT = "SCOPED_PROPOSAL_FOR_EXTERNAL_ACTION_CHECK", "UTILITY_NOT_ESTABLISHED"


def load(path):
    for m in [k for k in sys.modules if k.startswith(("test_theme18", "qualified_gain"))]:
        del sys.modules[m]
    sys.path.insert(0, path)
    try:
        return importlib.import_module("test_theme18_candidate_admission"), importlib.import_module("qualified_gain_adapters")
    finally:
        sys.path.pop(0)


def status(mod, v):
    return mod.assess_candidate(mod.reports(), source_value_lower_bound=v, **OPEN)["candidate_status"]


fails = []
old, _ = load(sys.argv[1])
grid = [F(i, 100) for i in range(-50, 101)]
before = [status(old, v) for v in grid]
new, adapters = load(sys.argv[2])
print("codomain over [0,1]^4:", [str(x) for x in adapters.geometry_score_bounds([(0, 1)] * 4)])
for v in (math.nextafter(1.0, 2), F(1001, 1000), F(10 ** 12 + 1, 10 ** 12), Decimal("1.0000000000000000001"),
          1.5, 10 ** 21, 1e308):
    got = status(new, v)
    print(f"  {repr(v)[:28]:30s} {got}")
    if got != NOT:
        fails.append(repr(v))
if status(new, 1) != POS:
    fails.append("1 lost its positive status")
after = [status(new, v) for v in grid]
same = before == after
print(f"hundredths -0.50..1.00 identical before/after: {same} | positive: {after.count(POS)}")
if not same:
    fails.append("valid bounds changed")
print("RESULT:", "PASS" if not fails else f"FAIL {fails}")
sys.exit(1 if fails else 0)
