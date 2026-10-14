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
