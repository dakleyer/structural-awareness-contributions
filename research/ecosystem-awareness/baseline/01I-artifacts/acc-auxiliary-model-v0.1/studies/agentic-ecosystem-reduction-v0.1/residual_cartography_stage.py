"""Stage I/II/III qualified-residual cartography OVERLAY on PR57's frozen ACC engine.

Research fixture only. The PR57 source has TWO physical providers.
This overlay adds FOUR cartographic observers and a NEW opportunity-arrival gate.
It does not revise the AG01-AG30 original policy outputs or original reference JSON.
All simulation source provenance is synthetic, not cryptographically authenticated.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
import math
from pathlib import Path
from typing import Any

from agentic_reduction import declared_public, plan_public, score_after_plan

HERE = Path(__file__).resolve().parent
THRESHOLD = 0.6
N_OBSERVERS = 4
CROSS_SOURCE_SCOPE = "vendor-ecosystem-v1"
META_EXCHANGE_TIME = 3
REFERENCE_AG01 = "AG01-QUALIFIED-NEAR-OPTIMUM"


@dataclass(frozen=True)
class Observation:
    event_id: str
    time: int
    source_scope: str
    features: tuple[float, ...]
    captured_before_admission: bool = True
    first_capture_observer_id: str | None = None


def fixture_case(case_id: str = REFERENCE_AG01) -> dict:
    data = json.loads((HERE / "CASES.json").read_text(encoding="utf-8"))
    matches = [row for row in data["cases"] if row["id"] == case_id]
    if len(matches) != 1:
        raise ValueError("Case not found or duplicated: " + case_id)
    return matches[0]


def local_claim(event: Observation, dimension: int) -> dict:
    """One observer sees only one numeric coordinate, not the four-coordinate event."""
    if dimension not in range(N_OBSERVERS):
        raise ValueError("unsupported observer index")
    raw = event.features[dimension] if dimension < len(event.features) else None
    is_valid = (type(raw) in (int, float)
                and math.isfinite(float(raw))
                and 0.0 <= float(raw) <= 1.0
                and bool(event.event_id)
                and event.captured_before_admission)
    if not is_valid:
        return {"event_id": event.event_id,
                "source_scope": event.source_scope,
                "observer_id": "observer-" + str(dimension),
                "finding": "UNKNOWN_BAD_OR_UNCAPTURED_INPUT"}
    return {"event_id": event.event_id,
            "source_scope": event.source_scope,
            "observer_id": "observer-" + str(dimension),
            "finding": ("CERTIFIED_OUTSIDE_LOCAL_A" if raw > THRESHOLD
                        else "IN_LOCAL_A")}


def common_cartographic_label(claims: list[dict], *, source_scope: str) -> dict:
    """Signed negative local predicates only; UNKNOWN is never logical NOT A_i."""
    if len(claims) != N_OBSERVERS or not claims:
        return {"joint_region": False, "reason": "INCOMPLETE_VIEWS"}
    event_ids = {c["event_id"] for c in claims}
    origins = {c["observer_id"] for c in claims}
    scopes = {c["source_scope"] for c in claims}
    required_origins = {"observer-" + str(i) for i in range(N_OBSERVERS)}
    if len(event_ids) != 1 or origins != required_origins or scopes != {source_scope}:
        return {"joint_region": False, "reason": "SOURCE_OR_EVENT_MISMATCH"}
    if all(c["finding"] == "CERTIFIED_OUTSIDE_LOCAL_A" for c in claims):
        return {"joint_region": True, "reason": "DEMORGAN_QUALIFIED_CONJUNCTION",
                "meta_label": "COMMON_RESIDUAL_CANDIDATE",
                "source_observers": sorted(origins)}
    return {"joint_region": False, "reason": "NOT_ALL_NEGATIVE_PROVED"}


def qualified_event(event: Observation, *, required_scope: str) -> dict:
    if (event.first_capture_observer_id is not None
            and event.first_capture_observer_id not in
            {"observer-" + str(i) for i in range(N_OBSERVERS)}):
        return {"joint_region": False, "reason": "INVALID_FIRST_CAPTURE_SOURCE"}
    claims = [local_claim(event, i) for i in range(N_OBSERVERS)]
    return common_cartographic_label(claims, source_scope=required_scope)


def geometric_referee_value(features: tuple[float, ...]) -> float:
    """Separate four-dimensional analytic illustration, NOT the ACC Y(k) score."""
    if len(features) != N_OBSERVERS or any(
            type(v) not in (int, float) or not 0 <= float(v) <= 1
            for v in features):
        raise ValueError("invalid scalar features for analytic geometry")
    return 1.0 - sum((1.0 - v) ** 2 for v in features) / N_OBSERVERS


def region_utility_lower_infimum() -> float:
    """Under the declared synthetic utility formula and all four z_i > 0.6."""
    return 1.0 - (1.0 - THRESHOLD) ** 2


def object_policy(scenario: dict, arm: str) -> dict:
    public = declared_public(scenario)
    plan = plan_public(public, scenario.get("Q"), arm=arm,
                       directed=scenario["directed"], full=scenario["full_A"])
    return score_after_plan(scenario, plan)


def three_stages(*, case_id: str = REFERENCE_AG01,
                 events: tuple[Observation, ...] = (),
                 assumed_class_to_q_source_valid: bool = True) -> dict:
    """Do not transfer until event is actually received after meta exchange.

    Unlike the original AG01 Q_META_PROTOCOL this introduces an explicit,
    NEW candidate-arrival gate and class-to-Q link assumption.
    """
    scenario = fixture_case(case_id)
    a_only = object_policy(scenario, "A_ONLY")
    q_review = object_policy(scenario, "Q_REVIEW_ONLY")
    candidate = None
    meta = {"joint_region": False, "reason": "NO_CANDIDATE_RECEIVED"}
    for event in sorted(events, key=lambda item: item.time):
        if event.time <= META_EXCHANGE_TIME:
            continue
        verdict = qualified_event(event, required_scope=scenario["public"]["scope"])
        if verdict["joint_region"]:
            candidate, meta = event, verdict
            break

    linked = bool(candidate is not None and assumed_class_to_q_source_valid
                  and scenario.get("Q") is not None)
    if linked:
        final = object_policy(scenario, "Q_META_PROTOCOL")
        matched = object_policy(scenario, "CONVENTIONAL_EQUIVALENT_Q")
    else:
        final = q_review
        matched = a_only
    source_scope = scenario["public"]["scope"]
    # We examine the actually supplied prefix independently of the new
    # post-exchange opportunity gate. A prior hit would falsify any report
    # that NO qualifying observation had been received before exchange.
    prior_qualified_hits = [
        e.event_id for e in events
        if e.time <= META_EXCHANGE_TIME
        and qualified_event(e, required_scope=source_scope)["joint_region"]
    ]
    stage_two_map = {
        "prior_qualified_hit_ids": prior_qualified_hits,
        "earlier_retained_hits_are_not_replayed_by_this_new_gate": True,
        "formal_region": "AND(observer-i CERTIFIED_OUTSIDE_LOCAL_A, i=0..3)",
        "feature_domain": "[0,1]^4",
        "typed_threshold": THRESHOLD,
        "source_scope": source_scope,
        "independently_sourced_AG01_near_gain_lower_bound":
            q_review["second_order_claimed_but_blocked_lower_bound"],
        "no_matched_event_as_of_meta_exchange": len(prior_qualified_hits) == 0,
        "unknown_future_encounter_time_and_agent": True,
    }
    # This is a serialized rule proposal, not real network publication or
    # authorization for other actors to use a candidate.
    schema_notice = None
    if candidate is not None:
        schema_notice = {
            "schema": "SA-META-CARTOGRAPHY-QUALIFICATION-v0.1",
            "event_id": candidate.event_id,
            "first_capture_observer_id": candidate.first_capture_observer_id,
            "source_scope": source_scope,
            "rule_version": 1,
            "meta_label": "COMMON_RESIDUAL_CANDIDATE",
            "source_observers": meta["source_observers"],
            "class_to_Q_source_is_synthetically_qualified":
                assumed_class_to_q_source_valid,
            "accepted_ordinary_action":
                ("EXISTING_AUTHORIZED_TRANSFER" if final["plan"]["transfer"] > 0
                 else "NO_ACTION_ALLOWED"),
            "transfer_amount_if_authorized": final["plan"]["transfer"],
            "receiver_must_revalidate": [
                "scope", "source_version_and_truth", "target_question",
                "operational_capability", "consent_and_authority", "cost"
            ],
            "broadcast_performed": False,
            "full_external_population_identified": False,
        }
    return {
        "case_id": case_id,
        "stage_2_source_cartography": stage_two_map,
        "stage_3_meta_syntax_message": schema_notice,
        "same_original_two_physical_providers": True,
        "new_cartographic_observers": N_OBSERVERS,
        "new_event_availability_gate": True,
        "new_source_class_to_q_link_is_synthetic_assumption":
            assumed_class_to_q_source_valid,
        "stage_1": a_only,
        "stage_2": q_review,
        "stage_3": final,
        "matched_conventional_with_same_q": matched,
        "candidate_event_id": candidate.event_id if candidate else None,
        "first_capture_observer_id":
            candidate.first_capture_observer_id if candidate else None,
        "meta_label": meta,
        "candidate_quality_scored_by_separate_geometry_only":
            (geometric_referee_value(candidate.features) if candidate else None),
        "objective_utility_geometry_is_not_ACC_mission_output": True,
        "no_real_world_probability_or_source_authentication": True,
    }


def example_events() -> tuple[Observation, ...]:
    return (
        Observation("routine-1", 1, CROSS_SOURCE_SCOPE,
                    (0.40, 0.35, 0.45, 0.50)),
        Observation("routine-4", 4, CROSS_SOURCE_SCOPE,
                    (0.20, 0.40, 0.30, 0.50)),
        Observation("previously-unclassifiable-7", 7, CROSS_SOURCE_SCOPE,
                    (0.90, 0.85, 0.80, 0.95),
                    first_capture_observer_id="observer-2"),
    )


def main() -> dict:
    x = three_stages(events=example_events())
    return {
        "study": "NEW_SYNTHETIC_CARTOGRAPHIC_OVERLAY_OF_ORIGINAL_PR57_AG01",
        "stage_outputs": [
            x[key]["observed_by_referee_only"]["output"]
            for key in ("stage_1", "stage_2", "stage_3")
        ],
        "technical_optimum_reference_only":
            x["stage_3"]["technical_optimum_referee_only"],
        "stage_gaps": [
            x[key]["mission_output_gap_to_same_budget_technical_optimum"]
            for key in ("stage_1", "stage_2", "stage_3")
        ],
        "stage_2_claimed_near_gain":
            x["stage_2"]["second_order_claimed_but_blocked_lower_bound"],
        "stage_3_captured": x["candidate_event_id"],
        "stage_3_first_capture_observer":
            x["first_capture_observer_id"],
        "stage_3_label": x["meta_label"]["meta_label"],
        "stage_2_cartography": x["stage_2_source_cartography"],
        "stage_3_rule_message": x["stage_3_meta_syntax_message"],
        "finite_geometric_objective": x["candidate_quality_scored_by_separate_geometry_only"],
        "same_info_conventional_output":
            x["matched_conventional_with_same_q"]["observed_by_referee_only"]["output"],
        "limitations": [
            "Four cartographic observers are a new overlay, not source PR57 physical providers",
            "Source link validity is stipulated, not actually authenticated",
            "Original AG01 does not require candidate arrival; new gate is explicit",
            "Arrival time 7 is constructed, not a convergence theorem",
            "No subjective AI suffering or real deployment"
        ]
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True, ensure_ascii=False))
