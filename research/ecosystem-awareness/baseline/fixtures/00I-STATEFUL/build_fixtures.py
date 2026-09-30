"""Build declared synthetic inputs and a separate, manually specified oracle.

This is a fixture authoring tool, never imported by the candidate runtime.
Times are seconds since 14:00. The historical 47-test fixture is not changed.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def build():
    cases, expectations = [], {}

    def add(name, events=(), mode="guarded", outcome="DENY", applied=False,
            generation=217, **options):
        cases.append(dict(id=name, mode=mode, events=list(events), **options))
        expectations[name] = dict(disposition=outcome, applied=applied,
                                  final_generation=generation)

    def event(at, field, value, **options):
        return dict(at=at, field=field, value=value, **options)

    freeze = event(1200, "freeze", True)
    patch = event(900, "patch_b", 218)
    race = event(2521, "freeze", True)
    drift = event(1200, "manifest", "v18")
    stale = event(2519, "observation", "freeze", fault="stale")
    add("continuity", outcome="EXECUTE", applied=True, generation=216)
    add("freeze_before_use", [freeze])
    add("patch_b_supersedes", [patch], generation=218)
    add("canonical_s5", [patch, freeze], generation=218)
    add("diagnosis_changed", [event(1200, "diagnosis", "network_failure")])
    add("source_unavailable", [event(2519, "observation", "freeze", fault="unavailable")], outcome="ESCALATE")
    add("stale_source", [stale], outcome="ESCALATE")
    add("source_expires_before_act", [event(2519, "observation", "freeze", fault="near_expiry")])
    add("source_exact_expiry", [event(2519, "observation", "freeze", fault="boundary")], outcome="ESCALATE")
    add("wrong_owner", [event(2519, "observation", "freeze", fault="wrong_owner")], outcome="ESCALATE")
    add("future_timestamp", [event(2519, "observation", "freeze", fault="future")], outcome="ESCALATE")
    add("missing_source", [event(2519, "observation", "freeze", fault="missing")], outcome="ESCALATE")
    add("invalid_value_type", [event(2519, "observation", "freeze", fault="wrong_type")], outcome="ESCALATE")
    add("unavailable_manifest", [event(2519, "observation", "manifest", fault="unavailable")], outcome="ESCALATE")
    add("stale_manifest", [event(2519, "observation", "manifest", fault="stale")], outcome="ESCALATE")
    add("grant_expired", act_at=5400)
    add("freeze_after_check", [race])
    add("patch_after_check", [event(2521, "patch_b", 218)], generation=218)
    add("manifest_after_check", [event(2521, "manifest", "v18")])
    add("permit_expired", act_at=2530)
    add("intent_substitution", substitute_intent=True)
    add("duplicate_delivery", outcome="EXECUTE", applied=True, generation=216, duplicate=True)
    add("irrelevant_change", [event(1200, "metric", 999)], outcome="EXECUTE", applied=True, generation=216)
    add("d1_dynamic_manifest", [drift])
    add("d1_open_continuity", [event(1200, "freeze_b", False), drift], outcome="EXECUTE", applied=True, generation=216)
    freshness_change = event(1200, "freshness_budget", 5)
    six_seconds_old = event(2519, "observation", "freeze", fault="six_seconds_old")
    add("d4_freshness_policy_tightened", [freshness_change, six_seconds_old], outcome="ESCALATE")
    add("d4_freshness_valid_continuity", [freshness_change], outcome="EXECUTE", applied=True, generation=216)
    add("d4_static_freshness_control", [freshness_change, six_seconds_old], mode="static_manifest", outcome="ESCALATE")
    add("d1_then_d4_closed_dependency", [drift, event(1300, "freshness_budget", 5)])
    # Deliberate limitation: the contract itself omits a real prohibition.
    # Expected SAFETY outcome remains DENY, so the candidate must fail this row.
    add("shared_omission", [freeze], omit_reference_freeze=True)
    # Deliberate falsifiers: these rows are expected to fail scenario acceptance.
    add("cached_temporal_control", [freeze], mode="coverage_only")
    add("coverage_missing_detected", mode="coverage_only", omit_checked_freeze=True)
    add("coverage_continuity", mode="coverage_only", outcome="EXECUTE", applied=True, generation=216)
    add("unbound_race", [race], mode="unbound")
    add("static_manifest_drift", [drift], mode="static_manifest")
    add("deny_all_continuity", mode="deny_all", outcome="EXECUTE", applied=True, generation=216)
    # A writer bypasses the revision protocol: the assumption must remain visible.
    add("writer_bypass", [event(2521, "freeze", True, bypass=True)])
    unavailable = event(2519, "observation", "freeze", fault="unavailable")
    recovered = event(2521, "observation", "freeze", fault=None)
    add("recovery_unchanged_continuity", recovery=True, outcome="EXECUTE", applied=True, generation=216)
    add("recovery_returns_early", [unavailable, recovered], recovery=True, outcome="EXECUTE", applied=True, generation=216)
    add("recovery_returns_last_poll", [unavailable, event(2524, "observation", "freeze", fault=None)], recovery=True, outcome="EXECUTE", applied=True, generation=216)
    add("recovery_never_returns", [unavailable], recovery=True, outcome="ESCALATE")
    add("recovery_at_deadline", [unavailable, event(2525, "observation", "freeze", fault=None)], recovery=True, outcome="ESCALATE")
    add("recovery_freeze_during_wait", [unavailable, recovered, event(2521, "freeze", True)], recovery=True)
    add("recovery_patch_during_wait", [unavailable, recovered, event(2521, "patch_b", 218)], recovery=True, generation=218)
    add("recovery_new_dependency", [unavailable, recovered, event(2521, "manifest", "v18")], recovery=True)
    add("recovery_tighter_freshness", [unavailable, event(2521, "freshness_budget", 5), event(2521, "observation", "freeze", fault="six_seconds_old")], recovery=True, outcome="ESCALATE")
    add("recovery_flapping", [unavailable, recovered, event(2522, "observation", "freeze", fault="unavailable"), event(2523, "observation", "freeze", fault=None), event(2524, "observation", "freeze", fault="unavailable")], recovery=True, outcome="ESCALATE")
    add("recovery_race_after_recheck", [unavailable, recovered, event(2523, "freeze", True)], recovery=True, act_at=2524)
    add("recovery_duplicate", [unavailable, recovered], recovery=True, duplicate=True, outcome="EXECUTE", applied=True, generation=216)
    add("recovery_grant_expiry", [unavailable, recovered], recovery=True, grant_expires=2522)
    add("recovery_dispatch_deadline", [unavailable, recovered], recovery=True, act_at=2526, outcome="ESCALATE")
    add("recovery_no_recheck_control", [unavailable, recovered], outcome="EXECUTE", applied=True, generation=216)
    expected_failures = ["shared_omission", "cached_temporal_control", "unbound_race",
                         "static_manifest_drift", "deny_all_continuity", "writer_bypass", "d4_static_freshness_control", "recovery_no_recheck_control"]
    (HERE / "fixtures.json").write_text(json.dumps({"schema": "00I-stateful-input-v1", "cases": cases}, indent=2) + "\n")
    (HERE / "oracle.json").write_text(json.dumps({"schema": "00I-stateful-oracle-v1", "expectations": expectations,
                                                   "expected_failure_cases": expected_failures}, indent=2) + "\n")


if __name__ == "__main__":
    build()
