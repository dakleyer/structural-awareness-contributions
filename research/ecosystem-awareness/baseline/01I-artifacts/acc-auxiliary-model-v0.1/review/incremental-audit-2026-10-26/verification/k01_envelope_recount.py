"""K-01, L-04 and L-05 (round 24): recount the PR #66 economic envelope.

Usage: python3 -B k01_envelope_recount.py <checkout of PR #66>

Runs PR #66's own runner (--model both --details) and recounts its 286 cases:
  * social #44: strict winners with and without SOURCE_PUBLIC_RECEIVER, an
    arm that copies the ledger of the policy the receiver selects (L-04);
  * agentic #57: strict leaders per price regime (L-05, evidence for F-04).
Expected on edb35e45: 168 + 118 cases; K-01 crossing at L = 9; social strict
wins with the receiver arm 0 for B, without it 10 for B (all under the
original prices); agentic source-original 14 strict wins for
CONVENTIONAL_DIRECTED and none for Q_META_PROTOCOL. Writes nothing.
"""
import collections
import json
import subprocess
import sys
from fractions import Fraction

root = sys.argv[1]
runner = ("research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/"
          "intrinsic-abcd-economics-v0.1/economic_envelope_runner.py")
out = subprocess.run([sys.executable, "-B", runner, "--corpus-root", ".", "--model", "both", "--details"],
                     cwd=root, capture_output=True, text=True, check=True).stdout
data = json.loads(out)
cases = data["cases"]
print("cases:", len(cases), "| K-01 crossing path nodes:", data["social_break_even"]["path_nodes"])
print("runner strict wins:", {g: v["strict_wins"] for g, v in data["summary"]["groups"].items()})


def leaders(case, exclude=()):
    arms = [a for a in case["arms"] if a["arm"] not in exclude and a["net"] not in (None, "UNKNOWN")]
    best = max(Fraction(a["net"]) for a in arms)
    return [a["arm"] for a in arms if Fraction(a["net"]) == best]


social = [c for c in cases if c["frame"]["model"] == "ACC_SOCIAL_INTRINSIC_44"]
agentic = [c for c in cases if c["frame"]["model"] != "ACC_SOCIAL_INTRINSIC_44"]
for label, exclude in (("social, all arms", ()), ("social, receiver arm excluded", ("SOURCE_PUBLIC_RECEIVER",))):
    by = collections.defaultdict(collections.Counter)
    for c in social:
        lead = leaders(c, exclude)
        by[c["frame"]["case_id"].split("/")[-1]]["strict:" + lead[0] if len(lead) == 1 else "tie"] += 1
    print(label)
    for regime, counts in by.items():
        print(f"   {regime:28s} {dict(counts)}")
dup = sum(1 for c in social if any(a["arm"] == "SOURCE_PUBLIC_RECEIVER" for a in c["arms"]) and any(
    a["arm"] != "SOURCE_PUBLIC_RECEIVER" and a["components"] == next(
        b for b in c["arms"] if b["arm"] == "SOURCE_PUBLIC_RECEIVER")["components"] and a["net"] == next(
        b for b in c["arms"] if b["arm"] == "SOURCE_PUBLIC_RECEIVER")["net"] for a in c["arms"]))
print(f"social cases where the receiver arm repeats another arm's ledger: {dup} of {len(social)}")
by = collections.defaultdict(collections.Counter)
for c in agentic:
    lead = leaders(c)
    by[c["frame"]["case_id"].split("/")[-1]]["strict:" + lead[0] if len(lead) == 1 else "tie"] += 1
print("agentic, strict leaders by price regime")
for regime, counts in by.items():
    print(f"   {regime:28s} {dict(counts)}")
