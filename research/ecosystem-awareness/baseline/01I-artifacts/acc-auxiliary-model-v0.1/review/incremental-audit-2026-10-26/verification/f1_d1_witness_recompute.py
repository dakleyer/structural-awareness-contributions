"""L-03 (round 23): recompute the F1/D1 residual witnesses cited for PR #60.

Usage: python3 -B f1_d1_witness_recompute.py <checkout of PR #60> <checkout of PR #57 at a9894049>

Social: both ProducerWorld variants hand off the same A (8, 8); joint capacity
is 10 versus 8. Agentic: PR57 declared_public(AG01) == declared_public(AG02),
and physical_response(transfer=2) gives 11.5 versus 8.875. Also checks that the
A hard-coded in PR #60's test equals PR57's declared_public(AG01). Exit code 1
on any mismatch. Writes nothing.
"""
import json
import os
import sys

ACC = "research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies"
pr60, pr57 = (os.path.abspath(p) for p in sys.argv[1:3])
sys.path.insert(0, os.path.join(pr60, ACC, "nested-composition-suffering-v0.1"))
sys.path.insert(0, os.path.join(pr60, ACC, "mathematical-lineage-social-agentic-v0.1"))
sys.path.insert(0, os.path.join(pr57, ACC, "agentic-ecosystem-reduction-v0.1"))
from nested_model import ProducerWorld, current_handoff, full_state_joint_capacity  # noqa: E402
import agentic_reduction as ar  # noqa: E402
import test_theme18_structural_adequacy as t  # noqa: E402

fails = []
social = {flag: (current_handoff(ProducerWorld(flag)), full_state_joint_capacity(ProducerWorld(flag))) for flag in (True, False)}
print("social (handoff A, joint capacity):", social)
if not (social[True][0] == social[False][0] and (social[True][1], social[False][1]) == (10, 8)):
    fails.append("social")
cases = json.load(open(os.path.join(pr57, ACC, "agentic-ecosystem-reduction-v0.1", "CASES.json")))["cases"]
ag01, ag02 = (next(c for c in cases if c["id"].startswith(k)) for k in ("AG01", "AG02"))
same_a = ar.declared_public(ag01) == ar.declared_public(ag02)
outs = (ar.physical_response(ag01, 2)["output"], ar.physical_response(ag02, 2)["output"])
print("agentic: same declared A:", same_a, "| output after transfer 2:", outs)
if not same_a or outs != (11.5, 8.875):
    fails.append("agentic")
pinned = t.AGENTIC_PUBLIC_A == ar.declared_public(ag01)
print("PR #60 test A equals PR57 declared_public(AG01):", pinned)
if not pinned:
    fails.append("pinned A")
print("RESULT:", "PASS" if not fails else f"FAIL {fails}")
sys.exit(1 if fails else 0)
