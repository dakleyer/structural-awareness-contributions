"""Round 39: PR #85's explicit-boolean evidence flags against parent PR #83.

Usage: python3 -B explicit_flags_check.py <study dir on #83 ddd29db2> <study dir on #85>
       (study dir = studies/mathematical-lineage-social-agentic-v0.1)

1. All 16 combinations of the four boolean gates (received, value link,
   authority, budget) give identical candidate_status before and after.
2. For each gate and for every observation's `captured`, non-boolean
   stand-ins ("UNKNOWN", "yes", 1, 2, {"x": 1}, [1]) with all other gates
   open: count how many reach the positive status before and after.
Exit code 1 if a boolean case changes or a stand-in is positive after. Writes nothing.
"""
import copy
import importlib
import itertools
import sys
from fractions import Fraction

POS = "SCOPED_PROPOSAL_FOR_EXTERNAL_ACTION_CHECK"
GATES = ("received_after_exchange", "source_to_value_link_qualified", "action_authorized", "decision_budget_ok")
STANDINS = ("UNKNOWN", "yes", 1, 2, {"x": 1}, [1])


def load(path):
    for m in [k for k in sys.modules if k.startswith(("test_theme18", "qualified_gain"))]:
        del sys.modules[m]
    sys.path.insert(0, path)
    try:
        return importlib.import_module("test_theme18_candidate_admission")
    finally:
        sys.path.pop(0)


def run(mod, rows=None, **gates):
    return mod.assess_candidate(rows if rows is not None else mod.reports(),
                                source_value_lower_bound=Fraction(9, 10), **gates)["candidate_status"]


def survey(mod):
    boolean = [run(mod, **dict(zip(GATES, combo))) for combo in itertools.product((False, True), repeat=4)]
    positive = {}
    for g in GATES:
        positive[g] = sum(run(mod, **{**dict.fromkeys(GATES, True), g: v}) == POS for v in STANDINS)
    rows = mod.reports()
    hits = 0
    for i in range(len(rows)):
        for v in STANDINS:
            changed = copy.deepcopy(rows)
            changed[i]["captured"] = v
            hits += run(mod, changed, **dict.fromkeys(GATES, True)) == POS
    positive["captured (any observation)"] = hits
    return boolean, positive


b_old, p_old = survey(load(sys.argv[1]))
b_new, p_new = survey(load(sys.argv[2]))
print("16 boolean combinations identical before/after:", b_old == b_new, "| positive:", b_new.count(POS))
print("non-boolean stand-ins reaching the positive status (before -> after):")
for k in p_old:
    print(f"   {k:32s} {p_old[k]} -> {p_new[k]}")
ok = b_old == b_new and not any(p_new.values())
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
