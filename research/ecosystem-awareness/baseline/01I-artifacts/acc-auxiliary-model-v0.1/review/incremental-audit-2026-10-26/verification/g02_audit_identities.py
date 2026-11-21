"""G-02 and L-09 (round 31): identities and leakage checks for PR #73.

Usage: python3 -B g02_audit_identities.py <checkout of PR #73>

1. Runs PR #73's manifest and checks identities that must hold by
   construction if the audit channel is real and not a relabelled flag:
   - legacy flagged arm keeps its 4 wrong of 12 false Q (history preserved);
   - a blind audit (detects nothing) gives exactly the unaudited-Q outcome;
   - an unavailable or unqualified audit makes the audited arm abstain on all
     48 x replicates adjudicable observations and miss every justified ALLOW;
   - a perfect audit gives 0 wrong decisions.
2. Checks that no new public field carries the variant, the truth or the
   legacy flag, and measures how many FALSE_Q cases are still identifiable
   from the public view alone (L-09): a view that never occurs with a true
   claim in the frozen 60 cases.
Exit code 1 if an identity fails. Writes nothing.
"""
import collections
import json
import os
import sys

CAMP = ("research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/"
        "conscientia-campaign-v0.1")
here = os.path.join(sys.argv[1], CAMP)
sys.path.insert(0, here)
os.chdir(here)
import g02_evidence_audit as g  # noqa: E402

out = g.run(json.load(open("G02_AUDIT_PROTOCOL.json")))
reps = out["replicates_per_case"]
reg = {r["regime"]: r["new_policy_outcomes"] for r in out["regimes"]}
fails = []


def check(label, ok):
    print(("OK   " if ok else "FAIL ") + label)
    if not ok:
        fails.append(label)


base = out["historical_flag_baseline_UNCHANGED"]
check(f"legacy flagged arm still 4 wrong of 12 false Q ({base['legacy_flag_arm_wrong']}/{base['ordinary_Q_wrong']})",
      base["legacy_flag_arm_wrong"] == 4 and base["false_Q_with_declared_boolean"] == 4)
key = ("wrong", "unresolved", "missed_justified_allows")
pick = lambda r, a: tuple(reg[r][a][k] for k in key)  # noqa: E731
check("blind audit == unaudited Q",
      pick("BLIND_AUDIT_FALSE_ASSURANCE", "Q_WITH_AUDIT_OBSERVATION") == pick("BLIND_AUDIT_FALSE_ASSURANCE", "Q_UNAUDITED_SOURCE"))
for r in ("AUDIT_UNAVAILABLE_DIRECT_AVAILABLE", "AUDIT_UNQUALIFIED_WRONG_SCOPE"):
    check(f"{r}: audited arm abstains everywhere {pick(r, 'Q_WITH_AUDIT_OBSERVATION')}",
          pick(r, "Q_WITH_AUDIT_OBSERVATION") == (0, 48 * reps, 12 * reps))
check("perfect audit: 0 wrong", reg["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["Q_WITH_AUDIT_OBSERVATION"]["wrong"] == 0)
print("published figures: weak audit", pick("WEAK_AUDIT_STRONG_CONVENTIONAL", "Q_WITH_AUDIT_OBSERVATION"),
      "| strong conventional", pick("WEAK_AUDIT_STRONG_CONVENTIONAL", "CONVENTIONAL_INDEPENDENT_MEASURED"),
      "| perfect conventional", pick("PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL", "CONVENTIONAL_INDEPENDENT_MEASURED"))

cases = json.load(open("CASE_REGISTRY.json"))["cases"]
leak = [c["case_id"] for c in cases
        if {"variant", "truth_private_for_scoring", "independent_audit"} & set(g.public_Q(c)) or
        {"variant", "truth_private_for_scoring"} & set(c["public"])]
check("no variant, truth or legacy flag in the public Q or public A", not leak)
views = collections.defaultdict(list)
for c in cases:
    q = g.public_Q(c)
    if g.q_can_be_used(c["public"], q):
        views[json.dumps({**q, **c["public"]}, sort_keys=True)].append(
            (c["variant"], c["truth_private_for_scoring"] == q["claimed_action"]))
alone = sum(1 for items in views.values() for v, _ in items
            if v == "FALSE_Q" and not any(t for _, t in items))
print(f"L-09: FALSE_Q cases identifiable from the public view alone: {alone} of 12 "
      "(baseline_action REVIEW with an ALLOW claim, in families whose true claim has baseline ALLOW)")
print("RESULT:", "PASS" if not fails else f"FAIL {fails}")
sys.exit(1 if fails else 0)
