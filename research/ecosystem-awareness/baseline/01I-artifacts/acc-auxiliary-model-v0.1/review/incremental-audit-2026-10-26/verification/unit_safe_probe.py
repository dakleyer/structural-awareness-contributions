"""Round 36: independent perturbation checks of the unit-safe reports in PR #81 and PR #82.

Usage: python3 -B unit_safe_probe.py <checkout of PR #82>   (PR #82 is stacked on #81)

PR #81 (unit_safe_envelope on the #66 runner):
  * randomise every legacy net, leader and extra field -> projection identical;
  * change one arm's output -> its physical gain changes;
  * NaN, inf, bool, text, float cost -> rejected; None -> UNKNOWN_MEASUREMENTS;
  * cost components that disagree with the total -> rejected;
  * K-01 prices at n16/n128/n256 and, per source-original agentic case, which
    arm realises the maximum physical output.
PR #82 (unit_safe_evidence on #57):
  * source file hashes equal to #57 a9894049 (passed in by git);
  * same physical resource budget in every arm of the 30 cases and 160 sweep cells;
  * AG01 Q_REVIEW_ONLY keeps its conditional signal with baseline output.
Writes nothing.
"""
import collections
import copy
import json
import os
import random
import sys
from fractions import Fraction as F
from pathlib import Path

root = Path(sys.argv[1]).resolve()
ST = root / "research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies"
sys.path.insert(0, str(ST / "intrinsic-abcd-economics-v0.1"))
sys.path.insert(0, str(ST / "agentic-ecosystem-reduction-v0.1"))
os.chdir(root)
import unit_safe_envelope as u  # noqa: E402
from economic_envelope_runner import execute  # noqa: E402
import unit_safe_evidence as ue  # noqa: E402

legacy = execute(json.loads((ST / "intrinsic-abcd-economics-v0.1/ECONOMIC_SWEEP_MANIFEST.json").read_text()),
                 root, model="both", details=True)
base = u.project_report(legacy)
print("PR #81 cases:", len(base["cases"]), base["groups"])

rng = random.Random(81)
noisy = copy.deepcopy(legacy)
for c in noisy["cases"]:
    for k in list(c):
        if k not in ("frame", "arms", "baseline_arm"):
            c[k] = "GARBAGE"
    for a in c["arms"]:
        a["net"] = str(rng.randint(-999, 999))
print("legacy net/leaders/extra fields randomised -> identical projection:",
      u.project_report(noisy)["cases"] == base["cases"])

moved = copy.deepcopy(legacy)
arm = moved["cases"][0]["arms"][1]
arm["gross"] = str(F(arm["gross"]) + 1)
print("one output +1 -> physical gain changes:",
      u.project_report(moved)["cases"][0]["physical_output_gain_vs_baseline"]
      != base["cases"][0]["physical_output_gain_vs_baseline"])
for bad in ("NaN", "inf", True, "abc", 1.5, None):
    probe = copy.deepcopy(legacy)
    probe["cases"][0]["arms"][1]["cost"] = bad
    try:
        out = u.project_report(probe)["cases"][0]["status"]
    except (ValueError, TypeError) as exc:
        out = "REJECTED " + type(exc).__name__
    print(f"  cost={bad!r:8} -> {out}")
probe = copy.deepcopy(legacy)
a = probe["cases"][0]["arms"][1]
key = next(iter(a["components"]))
a["components"][key] = str(F(a["components"][key]) + 1)
try:
    u.project_report(probe)
    print("components disagreeing with total: ACCEPTED (unexpected)")
except ValueError:
    print("components disagreeing with total: rejected")

for c in base["cases"]:
    cid = c["frame"]["case_id"]
    if cid.split("/")[0] in ("n16", "n128", "n256") and cid.endswith("/free/full/original"):
        o = {r["arm"]: (r["output"], r["information_cost"]) for r in c["observations"]}
        print(f"  K-01 {cid}: B {o['B_QUALIFIED']} | targeted {o['TARGETED_EXPLORATION_OF_A']}")
top = collections.Counter()
for c in base["cases"]:
    if c["frame"]["model"].startswith("ACC_AGENTIC") and c["frame"]["case_id"].endswith("source-original"):
        obs = {r["arm"]: F(r["output"]) for r in c["observations"]}
        best = max(obs.values())
        winners = sorted(k for k, v in obs.items() if v == best)
        top["CONVENTIONAL_DIRECTED alone" if winners == ["CONVENTIONAL_DIRECTED"] else
            "Q_META among the maximum" if "Q_META_PROTOCOL" in winners else "other"] += 1
        if c["frame"]["case_id"].startswith("AG01"):
            print("  AG01 (output, price):", {r["arm"]: (r["output"], r["information_cost"]) for r in c["observations"]})
print("agentic source-original, maximum physical output:", dict(top))

r = ue.report()
print("PR #82 cases/sweep:", r["case_count"], r["sweep_count"], "| hashes:", r["source_sha256"])
print("same physical resource budget in every arm:",
      all(v["total_resources_same"] for c in r["cases"] + r["sweep"] for v in c["physical_resource_accounting"].values()))
ag = next(c for c in r["cases"] if c["frame"]["case_id"].startswith("AG01"))
print("AG01 Q_REVIEW_ONLY output", next(o["output"] for o in ag["observations"] if o["arm"] == "Q_REVIEW_ONLY"),
      "with conditional signal", ag["source_awareness_signals"]["Q_REVIEW_ONLY"]["conditional_near_gain"])
