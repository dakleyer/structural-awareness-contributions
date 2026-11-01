"""L-08 (round 30): independent recount of PR #72's matched-evidence panels.

Usage: python3 -B l08_independent_panel.py <checkout of PR #72>

Uses only PR #70's world generator, original public planner and PR #68 referee
(create_world, plan_public, native_referee, _qualified). The qualified domain
policy is re-implemented here from its stated contract (consult the direct
observation; propose only if it is available, qualified and all three
measured bits are true). For both panels of L08_PROTOCOL.json and each cell
of the 7 x 7 accuracy grid, it counts errors and misses, classifies
boundary-only against qualified-domain on (errors, misses), and counts how
often SOURCE_BOUNDARY_ONLY is on the two-axis front among the four fair arms.
Writes nothing.
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
import g04_factorial as g  # noqa: E402

manifest = json.load(open("L08_PROTOCOL.json"))
seed, n, grid = manifest["seed"], manifest["worlds_per_grid_cell"], manifest["accuracy_grid"]


def qualified_domain(world):
    d = world["domain_observation"]
    ok = d.get("available") and g._qualified(d)
    return bool(ok and all(d[k] is True for k in ("measured_extra_stock", "measured_need", "measured_route_safe")))


def rights_ok(world):
    a = world["public_A"]
    return all(a[k] for k in ("role_change_declared_in_A", "owner_consent", "authorized_receiver",
                              "joint_protocol_available"))


def classify(b, d):
    if b == d:
        return "TIE"
    if b[0] <= d[0] and b[1] <= d[1]:
        return "BOUNDARY"
    if d[0] <= b[0] and d[1] <= b[1]:
        return "DOMAIN"
    return "INCOMPARABLE"


for panel in manifest["panels"]:
    classes = collections.Counter()
    on_front = 0
    extremes = {}
    for s in grid:
        for dacc in grid:
            p = dict(panel["base_parameters"], source_correct_if_qualified=s, domain_accuracy=dacc)
            tally = collections.defaultdict(lambda: [0, 0])
            for i in range(n):
                w = g.create_world(i, p, seed)
                eligible = g.native_referee(w["truth_PRIVATE_FOR_REFEREE_ONLY"])["eligible"]
                props = {arm: g.plan_public(w["public_A"], w["source_Q"], w["domain_observation"],
                                            w["targeted_observation"], arm)["propose"]
                         for arm in ("SOURCE_BOUNDARY_ONLY", "BOTH_SOURCE_AND_DOMAIN", "CONVENTIONAL_TARGETED")}
                props["QUALIFIED_DOMAIN"] = rights_ok(w) and qualified_domain(w)
                for arm, prop in props.items():
                    tally[arm][0] += prop and not eligible
                    tally[arm][1] += (not prop) and eligible
            b, d = tuple(tally["SOURCE_BOUNDARY_ONLY"]), tuple(tally["QUALIFIED_DOMAIN"])
            classes[classify(b, d)] += 1
            dominated = any(tuple(v) != b and v[0] <= b[0] and v[1] <= b[1] for v in tally.values())
            on_front += not dominated
            if (s, dacc) in (("1", "1"), ("1", "1/2"), ("1/2", "1")):
                extremes[f"Q {s} / facts {dacc}"] = {"boundary": b, "qualified_domain": d}
    print(panel["id"], "| classes:", dict(classes), f"| boundary on 2-axis front: {on_front}/{len(grid) ** 2}")
    for k, v in extremes.items():
        print("   ", k, v)
