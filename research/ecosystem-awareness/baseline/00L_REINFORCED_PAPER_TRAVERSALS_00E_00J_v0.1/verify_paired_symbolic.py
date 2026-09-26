"""Small standard-library replay of matched 00K microfixtures and Step-0 guards.

Run from any directory: python verify_paired_symbolic.py
This does not execute the full 00K pytest suites or any commercial product.
"""

from __future__ import annotations

import argparse
import importlib
import json
from datetime import timedelta
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
FIXTURES = HERE.parent / "fixtures"


FIELD_TYPES = {
    'affected_accounts': int,
    'ambulance_slot': int,
    'authority_current': bool,
    'base_root': str,
    'bus_slot': int,
    'campaign_ref': str,
    'corridor': str,
    'exposure_usd': int,
    'finding_reconstructable': bool,
    'fire_slot': int,
    'freeze_active': bool,
    'fresh': bool,
    'generation': int,
    'grant_current': bool,
    'hard_capacity': int,
    'incident_open': bool,
    'last_root': str,
    'leaf_grants_current': bool,
    'local_grants_current': bool,
    'max_steps': int,
    'message_count': int,
    'min_independent_roots': int,
    'proposition_supported': str,
    'record_class': str,
    'record_id': str,
    'resolves_at_step_3': bool,
    'root_current': bool,
    'signed': bool,
    'source': str,
    'source_available': bool,
    'source_version': str,
    'useful_horizon': int,
}


class IncompleteObservation(ValueError):
    pass


def module(fixture: str, name: str):
    folder = str(FIXTURES / fixture)
    sys.path.insert(0, folder)
    try:
        return importlib.import_module(name)
    finally:
        sys.path.pop(0)


def preflight(observation: dict, required: set[str]) -> None:
    """Test-harness guard: deliberately independent from each 00K model."""
    if set(observation) != required or any(observation[k] is None for k in required):
        raise IncompleteObservation("missing, null or unexpected observable field")
    for key, value in observation.items():
        expected_type = FIELD_TYPES.get(key)
        if expected_type is None or type(value) is not expected_type:
            raise IncompleteObservation(f"invalid type for {key}")
        if isinstance(value, str) and not value.strip():
            raise IncompleteObservation(f"empty identifier for {key}")
        if type(value) is int and value < 0:
            raise IncompleteObservation(f"negative numeric field {key}")
        if key in {"message_count", "min_independent_roots"} and value < 1:
            raise IncompleteObservation(f"nonpositive count {key}")


def evaluate(case_id: str, observation: dict) -> tuple[str, str, str]:
    """Only the observed fields enter the 00K implementation; oracle stays outside."""
    preflight(observation, set(observation))
    if case_id == "00E":
        m = module("00K-A2-P2-00E", "ablation_A2")
        stream = (m.EvidenceStep(False, False), m.EvidenceStep(True, False),
                  m.EvidenceStep(True, observation["resolves_at_step_3"]))
        fx = m.SearchFixture(stream, observation["hard_capacity"], observation["useful_horizon"])
        budget = observation["max_steps"]
        return (m.route_q_bounded_search(fx, budget).value,
                m.strong_peer_budgeted_search(fx, budget).value,
                m.ablated_search_until_capacity(fx).value)

    if case_id == "00F":
        m = module("00K-A6b-P6-00F", "ablation_A6b_00F")
        corridor = observation["corridor"]
        granted = observation["local_grants_current"]
        fx = m.MobilityFixture((
            m.LocalPosture("ambulance", corridor, observation["ambulance_slot"], "E", authorized=granted),
            m.LocalPosture("fire", corridor, observation["fire_slot"], "W", authorized=granted),
            m.LocalPosture("bus", corridor, observation["bus_slot"], "E", authorized=granted),
        ))
        return (m.route_q_p6(fx).value, m.strong_compatibility_peer(fx).value,
                m.ablated_local_only(fx).value)

    if case_id == "00G":
        m = module("00K-A6-P6-00G", "ablation_A6")
        claims = [m.Claim(f"agent-{i}", m.CANDIDATE_FRAME,
                          observation["last_root"] if i == observation["message_count"] - 1
                          else observation["base_root"], True, True, 0.95)
                  for i in range(observation["message_count"])]
        authority = m.TransitionAuthority("Mission-Owner", m.CANDIDATE_FRAME,
                                          observation["authority_current"],
                                          observation["min_independent_roots"])
        return (m.route_q(claims, authority).value,
                m.strong_peer_source_independence(claims, authority).value,
                m.ablated_identity_quorum(claims, 2).value)

    if case_id == "00H":
        m = module("00K-A4-P4-00H", "ablation_A4")
        peer = module("00K-A4-P4-00H", "a2l_strong_peer")
        finding = m.Finding(observation["affected_accounts"], observation["exposure_usd"],
                            observation["finding_reconstructable"])
        campaign = observation["campaign_ref"]
        expiry = m.NOW + timedelta(days=30) if observation["leaf_grants_current"] else m.NOW
        # Three representative leaves, with the population size held in the finding.
        actions = [m.LeafAction(f"ACCT-{i}", 40.0,
                                m.LeafGrant(f"CASE-{i}", 50.0, campaign, expiry),
                                m.NOW + timedelta(seconds=i)) for i in range(3)]
        registry = {campaign: m.RootCampaignAuthority(campaign, "Finance-Ops", True,
                                                       m.NOW + timedelta(days=30))} if observation["root_current"] else {}
        return (m.route_q_decision(finding, actions, registry).value,
                peer.a2l_strong_peer_decision(finding, actions, registry).value,
                m.ablated_no_rescue(finding, actions).value)

    if case_id == "00I":
        m = module("00K-A5-P5-00I", "ablation_A5")
        peer = module("00K-A5-P5-00I", "p5_strong_peer")
        basis = m.DecisionBasis("db-node-7", 217, True, False, "cfg-217")
        action = m.QueuedAction("PATCH-A", "db-node-7", 217,
                                m.TechnicalGrant("G-5521", observation["grant_current"]), basis)
        current = m.CurrentState(observation["generation"], observation["incident_open"],
                                 observation["freeze_active"], observation["source_version"],
                                 observation["source_available"])
        return (m.route_q(action, current).value,
                peer.full_basis_compare_before_act(action, current).value,
                m.native_generation_compare(action, current).value)

    if case_id == "00J":
        m = module("00K-A1-P1-00J", "ablation_A1")
        peer = module("00K-A1-P1-00J", "p1_strong_repairs")
        evidence = [m.Evidence(observation["record_id"], observation["record_class"],
                               observation["proposition_supported"], observation["signed"],
                               observation["fresh"], observation["source"])]
        return (m.route_q(evidence).value, peer.semantic_policy_matrix(evidence).value,
                peer.trusted_issuer_only(evidence).value)

    raise ValueError(f"unknown case {case_id}")


def verify(trace_jsonl: Path | None = None) -> None:
    document = json.loads((HERE / "00L_A10_PARES_CONTROLADOS.json").read_text(encoding="utf-8"))
    assert document["schema"] == "00L-paired-symbolic-v1"
    cases = document["cases"]
    assert [c["id"] for c in cases] == ["00E", "00F", "00G", "00H", "00I", "00J"]
    preflight_checks = 0
    branch_checks = 0
    trace_records = []
    failures = []
    for case in cases:
        factor = case["factor"]
        assert factor not in case["common"] and case["negative"] != case["positive"]
        assert set(case["expected"]) == {"negative", "positive"}
        required = set(case["common"]) | {factor}
        outputs = {}
        for branch in ("negative", "positive"):
            visible = dict(case["common"], **{factor: case[branch]})
            preflight(visible, required)
            # Step 0: deletion and explicit-null mutations must not reach the model.
            for field in sorted(required):
                for mutant in ({k: v for k, v in visible.items() if k != field},
                               dict(visible, **{field: None})):
                    try:
                        preflight(mutant, required)
                    except IncompleteObservation:
                        preflight_checks += 1
                    else:
                        raise AssertionError(f"Step-0 missed {case['id']}/{branch}/{field}")
            route, strong_peer, weak_peer = evaluate(case["id"], visible)
            expected = case["expected"][branch]
            statuses = {"route": route == expected, "strong_peer": strong_peer == expected,
                        "weak_peer": weak_peer == expected}
            for name in ("route", "strong_peer"):
                if not statuses[name]:
                    failures.append(f"{case['id']}/{branch}/{name}: expected {expected}")
            outputs[branch] = {"route": route, "strong_peer": strong_peer, "weak_peer": weak_peer}
            trace_records.append({
                "schema": "00L-symbolic-branch-v2",
                "case": case["id"],
                "branch": branch,
                "factor": factor,
                "observation": visible,
                "actual": outputs[branch],
                # The expected disposition is added to the trace only after evaluate().
                # It is never passed to any 00K implementation.
                "expected": expected,
                "matches_expected": statuses,
                "route_peer_agreement": route == strong_peer,
                "preflight_guard_mutations_rejected": 2 * len(required),
            })
            branch_checks += 1
        if outputs["negative"]["weak_peer"] == case["expected"]["negative"]:
            failures.append(f"{case['id']}: negative ablation did not discriminate")
        if outputs["negative"]["route"] == outputs["positive"]["route"]:
            failures.append(f"{case['id']}: route did not discriminate")
        print(json.dumps({"case": case["id"], "factor": factor, "branches": outputs}, ensure_ascii=False))

    # Separate regression for the canonical strict monetary threshold in 00H-MAT-1.
    h = module("00K-A4-P4-00H", "ablation_A4")
    assert not h.check_P1_evidence_sufficiency(h.Finding(100, 10_000.0, True))
    assert h.check_P1_evidence_sufficiency(h.Finding(100, 10_000.01, True))
    assert not h.check_P1_evidence_sufficiency(h.Finding(99, 240_000.0, True))
    if trace_jsonl is not None:
        trace_jsonl.write_text(
            "".join(json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n"
                    for record in trace_records), encoding="utf-8")
    if failures:
        raise AssertionError("evaluation failed; branch traces preserved: " + "; ".join(failures))
    print(f"OK: {branch_checks} symbolic branches; {preflight_checks} Step-0 drop/null mutations; "
          "00H strict boundary 3/3. Shared-contract peer passes every pair: no independent comparison or EA differential inferred.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trace-jsonl", type=Path,
                        help="Write 12 deterministic, post-evaluation branch records to this path")
    verify(parser.parse_args().trace_jsonl)
