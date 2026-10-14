#!/usr/bin/env python3
"""DDS China Unicom CU-HIB-01 author-side integrity and synthetic-case checks.

This validates DOCUMENTS/LOCAL CALIBRATION ONLY. It does not test a PDP,
constitute a blind preregistration, prove an EA differential, or assert
approval by China Unicom, FG-TIDA or ITU.
"""

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

PKG = Path(__file__).resolve().parent.parent
CAMPAIGNS = PKG.parent
REQUIRED = (
    "CAMPAIGN.md",
    "CAMPAIGN.json",
    "SCIENTIFIC_DESIGN.md",
    "INTERFACE_CONTRACT.md",
    "PRIMARY_TRIAL_PROTOCOL_DRAFT_v0.1.md",
    "SOURCES_AND_CUSTODY.md",
    "RUN_CARD_PREPARATION.md",
    "CONTINUATION.md",
    "CHALLENGE_CONTRACT_v0.2.md",
    "REQUIREMENTS_TRACEABILITY_v0.2.md",
    "APPROVAL_AND_PREREGISTRATION_v0.2.md",
    "AUDIT_REPORT_2026-10-14.md",
    "fixtures/PUBLIC_CALIBRATION_VECTORS_v0.2.json",
    "THIRD_PARTY_CHALLENGE_DOSSIER_R123_v0.3.md",
    "THIRD_PARTY_CRITICAL_REVIEW_R123_v0.3.md",
    "R123_STAGE_REGISTER_v0.3.json",
)
checks = []
errors = []


def check(label, ok, detail=None):
    checks.append({"check": label, "status": "PASS" if ok else "FAIL"})
    if not ok:
        errors.append({"check": label, "detail": str(detail or "")})


def load_json(rel):
    return json.loads((PKG / rel).read_text(encoding="utf-8"))


check("required_files_exist", all((PKG / p).is_file() for p in REQUIRED))
if not (PKG / "CAMPAIGN.json").exists():
    print(json.dumps({"errors": errors, "checks": checks}))
    sys.exit(1)

campaign = load_json("CAMPAIGN.json")
book = load_json("fixtures/PUBLIC_CALIBRATION_VECTORS_v0.2.json")
registry = json.loads((CAMPAIGNS / "REGISTRY.json").read_text(encoding="utf-8"))
index = (CAMPAIGNS / "INDEX.md").read_text(encoding="utf-8")
cs = book.get("cases", [])
by = {x.get("id"): x for x in cs}
check("unique_case_ids", len(by) == len(cs))
check("twelve_public_calibration_cases", len(cs) == 12)
check("campaign_identity_matches", book.get("campaign_handle") == campaign.get("campaign_handle") == "DDS-A-CU-PLM-EA-01")
check("registry_has_two_distinct_campaigns", len({x.get("working_id") for x in registry.get("campaigns", [])}) == len(registry.get("campaigns", [])) and {"DDS-A-FLORES-POP-EA-01", "DDS-A-CU-PLM-EA-01"}.issubset({x.get("working_id") for x in registry.get("campaigns", [])}))
check("both_campaigns_indexed", all(x in index for x in ("DDS-A-FLORES-POP-EA-01", "DDS-A-CU-PLM-EA-01")))
check("no_execution_in_fixture", book.get("scored_execution") is False and book.get("blind_trial") is False and all(x.get("observed_run") is None for x in cs))
check("no_source_owner_approval_claim", book.get("source_policy_owner_approved") is False and campaign.get("collaboration_approval") == "NOT_ESTABLISHED")
status = campaign.get("status", {})
check("nonpromoted_dds_status", status.get("formal_admission") is False and status.get("specification_frozen") is False and status.get("run_executed") is False and status.get("stage_b_started") is False and status.get("stage_c_started") is False)
check("service_criticality_constant", all(x["reference_world"]["T0"]["critical_service_S"] is True and x["reference_world"]["T2"]["critical_service_S"] is True for x in cs))
if "CU-C2" in by:
    t0, t2 = (by["CU-C2"]["reference_world"][k] for k in ("T0", "T2"))
    differences = [k for k in set(t0) | set(t2) if t0.get(k) != t2.get(k)]
    check("primary_changes_exactly_one_dependency_edge", differences == ["edge_S_R"] and t0["edge_S_R"] is False and t2["edge_S_R"] is True)
else:
    check("primary_case_exists", False)
if all(k in by for k in ("CU-C3+", "CU-C3-")):
    a, b = by["CU-C3+"], by["CU-C3-"]
    check("two_worlds_identical_participant_packet", a["participant_packet"] == b["participant_packet"])
    check("two_worlds_have_different_hidden_graph_truth", a["reference_world"]["T2"]["edge_S_R"] != b["reference_world"]["T2"]["edge_S_R"])
else:
    check("both_unobservable_worlds_exist", False)
check("positive_cases_retain_full_restoration", all(by.get(k, {}).get("provisional_oracle", {}).get("full_restore_eligible") is True and "RESTORE_FULL" in by[k]["provisional_oracle"]["allowable_dispositions"] for k in ("CU-C0", "CU-C6")))
check("nonpositive_cases_cannot_full_restore", all(x["provisional_oracle"]["full_restore_eligible"] is False and "RESTORE_FULL" not in x["provisional_oracle"]["allowable_dispositions"] for x in cs if x["id"] not in ("CU-C0", "CU-C6")))
if all(k in by for k in ("CU-C7", "CU-C8")):
    check("restricted_permission_has_own_grant", by["CU-C7"]["reference_world"]["T2"]["restricted_observation_grant"] == "VALID" and "RESTORE_RESTRICTED_OBSERVE_ONLY" in by["CU-C7"]["provisional_oracle"]["allowable_dispositions"])
    check("no_restricted_permission_without_grant", by["CU-C8"]["reference_world"]["T2"]["restricted_observation_grant"] == "ABSENT" and "RESTORE_RESTRICTED_OBSERVE_ONLY" not in by["CU-C8"]["provisional_oracle"]["allowable_dispositions"])
check("same_root_not_independent", all(z.get("root") == "X" for z in by.get("CU-C9", {}).get("participant_packet", {}).get("signals", [])) and len(by.get("CU-C9", {}).get("participant_packet", {}).get("signals", [])) == 3)

check("primary_packet_is_native_edge_evidence_not_precomputed_policy",
      by["CU-C2"]["participant_packet"]["dependency_S_R"] == "EDGE_ADDED"
      and by["CU-C2"]["participant_packet"]["service_S_criticality"] == "CRITICAL")
check("observation_grant_preexisted_edge_change",
      by["CU-C7"]["reference_world"]["T0"]["restricted_observation_grant"] == "VALID"
      and by["CU-C7"]["reference_world"]["T2"]["restricted_observation_grant"] == "VALID")
check("human_ack_is_separate_postactivation_event",
      by["CU-C10"]["reference_world"]["T0"]["human_resume_ack"] is False
      and by["CU-C10"]["reference_world"]["T2"]["human_resume_ack"] is False
      and by["CU-C10"]["post_activation_input_event"]["time"] == "T3")


# v0.3 context-first challenge and source reconciliation; documentary checks only.
r123 = load_json("R123_STAGE_REGISTER_v0.3.json")
third_party = (PKG / "THIRD_PARTY_CHALLENGE_DOSSIER_R123_v0.3.md").read_text(encoding="utf-8")
third_party_review = (PKG / "THIRD_PARTY_CRITICAL_REVIEW_R123_v0.3.md").read_text(encoding="utf-8")
stages = r123.get("stages", [])
r123_cases = r123.get("cases", [])
check("v03_campaign_version", campaign.get("version") == "0.3")
check("v03_source_author_agreement_recorded", campaign.get("source_cutoff", {}).get("source_authors_agree_restoration_anchor") is True)
check("v03_six_original_source_comment_links",
      all("issuecomment-" + comment_id in third_party for comment_id in
          ("5700157082","5707764621","5915019756","6072991126","6164646309","6165603429")))
check("v03_correct_activation_order",
      r123.get("latest_source_agreement", "").endswith("6165603429") and
      [x.get("id") for x in stages] == ["R1", "R2", "R3"] and
      stages[1].get("required_order", [])[:3] ==
      ["AT_SUSPENSION_DECLARE_AND_PIN_RESTORE_CONDITION",
       "ON_ACTIVATION_VALIDATE_PINNED_CONDITION",
       "THEN_DERIVE_INTENT_AGAINST_CURRENT_CONTEXT"])
check("v03_source_policy_and_runs_not_approved",
      r123.get("source_owner_policy_approved") is False and
      r123.get("independent_oracle_assigned") is False and
      r123.get("stage_B") == "NOT_STARTED" and
      r123.get("stage_C") == "NOT_STARTED" and
      campaign.get("status", {}).get("local_design_approved") is False)
check("v03_all_controls_unexecuted",
      r123.get("status") == "NOT_APPROVED_NOT_PREREGISTERED_NOT_FROZEN_NOT_EXECUTED" and
      stages[1].get("frozen_completely") is False and
      all(x.get("completion") == "NOT_EXECUTED" for x in stages))
check("v03_R3_primary_one_variable_control",
      stages[2].get("world", {}).get("service_S_critical_at_t0") is True and
      stages[2].get("world", {}).get("service_S_critical_at_t2") is True and
      stages[2].get("world", {}).get("dependency_S_R_at_t0") is False and
      stages[2].get("world", {}).get("dependency_S_R_at_t2") is True)
check("v03_R3_unknown_worlds_do_not_leak_evaluator_truth",
      all(x.get("visible_packet_insufficient_for_full_action") is True
          for x in r123_cases if x.get("id") in ("R3-C+", "R3-C−")) and
      all(x.get("positive") is False for x in r123_cases
          if x.get("id") in ("R3-C+", "R3-C−")))
check("v03_review_not_independent",
      "not independent" in third_party_review.lower() and
      "NOT_ESTABLISHED" in third_party_review)
check("v03_primary_goal_not_EA_winner",
      r123.get("research_object") == "CONTINUING_APPLICABILITY_UNDER_CONTEXT_CHANGE" and
      r123.get("scientific_object_not") == "EA_PRODUCT_SUPERIORITY")

missing_links = []
relative_links_checked = 0
for rel in REQUIRED:
    path = PKG / rel
    if not path.exists() or not rel.endswith(".md"):
        continue
    text = path.read_text(encoding="utf-8")
    for url in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        if url.startswith(("https://", "http://", "mailto:", "#")):
            continue
        target = unquote(url.split("#", 1)[0])
        if not target:
            continue
        relative_links_checked += 1
        if not (path.parent / target).is_file():
            missing_links.append({"source": rel, "target": url})
check("relative_document_links_resolve", not missing_links, missing_links)
check("source_preserving_attribution", "#23" in (PKG / "SOURCES_AND_CUSTODY.md").read_text(encoding="utf-8") and "China Unicom" in (PKG / "CAMPAIGN.md").read_text(encoding="utf-8"))

hashes = {
    rel: hashlib.sha256((PKG / rel).read_bytes()).hexdigest()
    for rel in REQUIRED if (PKG / rel).exists()
}
result = {
    "audit_kind": "AUTHOR_SIDE_DOCUMENTARY_AND_SYNTHETIC_INTEGRITY",
    "scientific_stage_result": "NOT_ESTABLISHED",
    "source_owner_approval": "NOT_ESTABLISHED",
    "executed_external_pdp": False,
    "checked_relative_links": relative_links_checked,
    "case_count": len(cs),
    "checks": checks,
    "failed_checks": len(errors),
    "errors": errors,
    "document_sha256": hashes,
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(1 if errors else 0)
