# DDS Stage A — VNext

<!-- DDS terminology revision 3 (2026-10-07): Stage A/B/C only; source scientific version and evidence unchanged. -->

**Owning source:** [DDS Stage A — Specification Discovery / Challenge–Trajectory Profile v0.1](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md)  
**DDS method router:** [DDS Canonical Method Index v0.1](./DDS_CANONICAL_METHOD_INDEX_v0.1.md)  
**Current review date:** 8 October 2026.  
**Status:** current Stage A review ledger only. Historical incorporated proposals have been removed from this VNext because Git history already preserves them.

## 1. Current Stage A state

Stage A is now explicitly separated from the complete DDS method.

The live Stage A source currently provides:

- canonical identity as **DDS Stage A — Specification Discovery**;
- explicit A/B/C stage taxonomy for a reader entering this file;
- distinction between **DDS Stages** and local **trajectory gates**;
- full versus **Simplified DDS Stage A** coverage semantics;
- Challenge and bounded reduction;
- blind evaluator/private-map discipline;
- technology/configuration mapping;
- Stage 1 technology–problem extension/isomorphism profiling;
- Stage 2 non-isomorphic mechanism study;
- I/M/P/Ø route/outcome semantics;
- Type-0/1/2 and M-admission diagnostics where admitted;
- Cost/Risk/Effectiveness accounting;
- acceptance and optional Business Value projection;
- proportionality and material-assumption checks;
- reduced coverage / delivery separation;
- current R01, extension and HEW research relationships;
- evidence/claim boundary;
- minimum Stage A citation block;
- explicit Stage A entry, exit and handoff contract to Stage B.

The latest reader-orientation/handoff incorporation is commit `27938fa70a82c2fa07f79c60eed34ab4c2d9f267`.

### Conservation check for that incorporation

The Stage A clarification commit added **125 lines and deleted 0 lines**. No prior Stage A scientific text, mathematics, result, threshold, evidence record or source relationship was removed by that change.

## 2. Incorporated — no longer pending

The following items are incorporated in the live Stage A source and are intentionally **not repeated as before/after proposals in this VNext**:

- canonical-boundary / meaning-of-canonical clarification;
- reduced-coverage and delivery clarification 0.1.2;
- Stage 1 extension/isomorphism + Stage 2 non-isomorphic-mechanism clarification 0.1.3;
- HEW / executed-companion evidence parity;
- proportionality clarification 0.1.4;
- material-assumption check;
- bibliography / research-basis route;
- scoped-study completion route;
- Type-0/1/2, M-admission and blind-reference refinements already present in Stage A;
- split from one monolithic DDS file into Index + Stage A + Stage B + Stage C;
- Stage A reader taxonomy and scope boundary;
- Stage A entry/exit package and Stage B handoff contract.

Their detailed historical text remains available in Git history. They are not active work items.

## 3. Pending Stage A changes

**No rewrite of the canonical v0.1 source is pending. One additive successor proposal is active: the gate-diagnostic subprofile described below.**

The existing Stage A science, reader taxonomy, entry/exit boundary, Simplified coverage semantics, Stage B handoff contract and profile mapping are incorporated in the live source. The gate-diagnostic proposal adds a result/diagnostic layer without changing those frozen semantics.

The former `GA-P01` is complete:

- the authoritative cross-stage/current-corpus registry now lives in the [DDS Canonical Method Index](./DDS_CANONICAL_METHOD_INDEX_v0.1.md#8-current-dds-profile-and-support-registry);
- Stage A §11 now contains Stage A examples only and links to that registry;
- the previous detailed Cost/Risk/Effectiveness/Acceptance/BV/evidence information was moved into the Index registry rather than discarded;
- frozen historical results were not rewritten.

## 4. Cross-corpus work status — outside Stage A ownership

The following taxonomy/routing work has now been incorporated and is **not pending**:

- EA router and canonical-corpus README enter through the DDS Canonical Method Index;
- Canonical Corpus Manifest registers Index + Stages A/B/C as the DDS method set;
- DBC and 00D are classified as DDS support artefacts rather than parallel methods;
- R01 is routed as the richest current probabilistic Stage A reference instantiation;
- R01 C02 Oracle/harness is classified as shared DDS test-infrastructure qualification;
- RS-00E-Q1a Stage-0 is classified as bounded Simplified Stage A deterministic evidence while preserving historical version lineage;
- 00D-A01/A03 are classified as DDS test-design/support infrastructure;
- HEW, STAMP/STPA, SPIFFE, RATS and the current RAG/OAuth/MCP/SQL/durable-workflow studies are routed through Stage A with their evidence ceilings preserved;
- current 00E/00F/00G/00H/00I/00J technology/implementation trajectories are explicitly classified as Stage A or Stage A Challenge inputs as applicable;
- current human-readable study/completion/exercise reports point to the DDS Index while frozen Run Cards/FREEZE/RESULTS keep their execution-time identity;
- WORKPLAN and VISUAL_GUIDE state that W2/W3 and Stage-0/1/2 are workstream/evidence-maturity axes, not parallel DDS methods or DDS Stages;
- the public Ecosystem Positioning README points technical reviewers to the DDS Canonical Method Index;
- the authoritative global profile/support registry has moved from Stage A §11 to the DDS Index.

### Remaining work belongs elsewhere

| Remaining work | Owner |
|---|---|
| Stage B contract evolution and first 00I/S5 architecture-verification pilot | DDS Stage B |
| Stage C contract evolution and C11/T03 real-implementation validation route | DDS Stage C |
| Any further common cross-stage rule consolidation | DDS Canonical Method Index |
| Any future repository-wide stale-link cleanup discovered outside the current active routes | owning document / corpus maintenance |

None of these is a Stage A pending item.

## 5. Stage A review checks before any future incorporation

Any future Stage A change should pass all of these:

1. **Object check:** the object under test is still a candidate specification/mechanism/control profile, not architecture realization or product validation.
2. **Reference check:** the authoritative reference remains the frozen Challenge / Stage A acceptance and falsifier contract.
3. **Namespace check:** DDS Stage A/B/C is not confused with trajectory gates, gate policy, Stage-0/Stage-1 or C02/C11/T03.
4. **Evidence check:** evidence mode does not silently change Stage identity.
5. **Conservation check:** no frozen result, hash, theorem or historical evidence is strengthened or erased.
6. **Coverage check:** a Simplified Stage A profile declares selected and omitted surfaces.
7. **Handoff check:** any Stage B-ready result identifies a sufficiently frozen Stage A specification package.
8. **Closed-proposal check:** retain incorporated proposals, their before/after text, audit discussion and dissent as dated history in this VNext, with source version and decision; exclude them from the pending queue.

## 6. Current decision

**The canonical Stage A v0.1 source remains unchanged. The only active Stage A successor work is the additive gate-diagnostic subprofile below.**

The live Stage A source remains the canonical Specification-Discovery Stage. The gate-diagnostic work is deliberately isolated in versioned draft artefacts so no historical Stage A result, theorem or acceptance record is silently reinterpreted.

After the gate-diagnostic subprofile is independently reviewed and exercised with frozen result tables, a separate promotion decision can determine whether any part belongs in a future Stage A version. Stage B and Stage C work remain independently owned.


---

## Gate-diagnostic successor work — 8 October 2026

A new additive Stage A diagnostic subprofile has been drafted to address a limitation exposed by the current requirement-level audits: a single Stage A acceptance state does not show which properties pass, which are merely declared, which depend on unresolved prerequisites, or what minimum remediation would unlock downstream properties.

Current draft artefacts:

- [DDS Stage A Gate Diagnostic Profile v0.1 Draft](./DDS_STAGE_A_GATE_DIAGNOSTIC_PROFILE_v0.1_DRAFT.md)
- [DDS Stage A Gate Catalog v0.1 Draft](./DDS_STAGE_A_GATE_CATALOG_v0.1_DRAFT.json)
- [DDS Stage A Gate Diagnostic Validation Plan v0.1](./DDS_STAGE_A_GATE_DIAGNOSTIC_VALIDATION_PLAN_v0.1.md)
- [DDS Stage A Gate Diagnostic Validation Run v0.1](./DDS_STAGE_A_GATE_DIAGNOSTIC_VALIDATION_RUN_v0.1.md)
- [DDS Stage A Gate Diagnostic Result Template v0.1](./DDS_STAGE_A_GATE_DIAGNOSTIC_RESULT_TEMPLATE_v0.1.json)
- [Deterministic gate checker](./gate-diagnostic/check_gate_profile.py)
- [FG-TIDA Decision Boundary Evaluation Profile v0.2 Draft](./fg-tida/tests/FG_TIDA_DECISION_BOUNDARY_EVALUATION_PROFILE_v0.2_DRAFT.md)

The proposal is **not another DDS method and does not modify frozen Stage A results**. It adds a gate-by-gate output layer with separate own verdict, specification level, dependency/effective status, test role, root-blocker analysis, potential-unlock diagnosis and a Stage-B handoff queue. The core catalog is technology-neutral.

An initial maintainer-side structural portability run now covers the planned historical, mathematical/reduction and non-HF technology families. It found and repaired one false-blocking defect in the first dependency example. Promotion still requires independent review and actual frozen result tables; the catalog therefore remains draft.

A **v0.2 audit-candidate successor package is now frozen for external review**, while v0.1 remains preserved:
- [Profile v0.2 Audit Candidate](./DDS_STAGE_A_GATE_DIAGNOSTIC_PROFILE_v0.2_AUDIT_CANDIDATE.md)
- [Catalog v0.2 Audit Candidate](./DDS_STAGE_A_GATE_CATALOG_v0.2_AUDIT_CANDIDATE.json)
- [Result Template v0.2](./DDS_STAGE_A_GATE_DIAGNOSTIC_RESULT_TEMPLATE_v0.2.json)
- [Checker v0.2](./gate-diagnostic/check_gate_profile_v0.2.py)
- [Audit Manifest v0.2](./DDS_STAGE_A_GATE_DIAGNOSTIC_AUDIT_MANIFEST_v0.2.json)
- [External Audit Checklist v0.2](./DDS_STAGE_A_GATE_DIAGNOSTIC_EXTERNAL_AUDIT_CHECKLIST_v0.2.md)

This successor makes profile-required gates explicit, requires fail-capable preregistered cases for discriminating gates, machine-evaluates conditional named-claim dependencies, and defines PROFILE_PASS / PROFILE_PARTIAL / PROFILE_FAIL / PROFILE_COVERAGE_ONLY without introducing an aggregate score. It is frozen for **instrument audit**, not yet independently accepted and not a candidate-technology result.

No canonical v0.1 gate semantics are changed by this VNext entry.


---

## Audit implementation follow-up — G03.b / T06 (Plan 2.0, executed 10 October 2026)

**Source:** Reconciled audit v3.1 `G03.b / T06`, confirmed source defect. **Strategy:** v3.3 DS-12 source conservation, DS-02 one DDS method, B-minimal scoped changes. **Priority:** P1 for a Stage A instrument result, not an assertion of runtime product failure. **Decision:** programme owner requested immediate application of audit-derived corrections. **Actual status:** candidate successor and seven unit controls published; **T06 remains PARTIAL** pending end-to-end original-catalog replay, frozen preregistration evidence and external source-owner acceptance.

**Immutable predecessor:** [v0.2 checker](./gate-diagnostic/check_gate_profile_v0.2.py) blob `0aa51e7b050123c4a09967a5fae52bf290b6c8a5`, unchanged.

### TEXTO ANTES — existing v0.2 rule (complete affected validation passage)

```python
            raise ContractError(f"invalid_required_min_level:{gid}:{row.get('required_min_level')}")
        if not isinstance(row.get("required_for_profile"), bool):
            raise ContractError(f"required_for_profile_must_be_boolean:{gid}")
        if row.get("applicability") == "NOT_APPLICABLE" and row.get("own_verdict") != "NOT_APPLICABLE":
            raise ContractError(f"na_applicability_requires_na_verdict:{gid}")
        if row.get("applicability") == "APPLICABLE" and row.get("own_verdict") == "NOT_APPLICABLE":
            raise ContractError(f"applicable_gate_cannot_have_na_verdict:{gid}")
        if row.get("required_for_profile") and row.get("applicability") != "APPLICABLE":
            raise ContractError(f"required_gate_must_be_applicable:{gid}")
        if row.get("test_role") == "DISCRIMINATING":
            fail_cases = row.get("fail_capable_case_ids", [])
            if not isinstance(fail_cases, list) or not fail_cases:
                raise ContractError(f"discriminating_gate_requires_fail_capable_case:{gid}")
        rows[gid] = deepcopy(row)

    missing = sorted(set(gates) - set(rows))
    if missing:
        raise ContractError("missing_gate_rows:" + ",".join(missing))

    required_claims = result.get("profile", {}).get("required_named_claims", [])
    known_claims = set(catalog.get("named_claims", {}))
```

In this passage, N/A is checked for enum/verdict consistency but `applicability_rationale` is not checked.

### TEXTO DESPUÉS — successor candidate (complete new source)

The original v0.2 file has **not** been replaced. The proposed rule lives in a separately versioned, explicitly non-canonical successor.

```python
#!/usr/bin/env python3
"""Proposed DDS Stage A v0.3 checker successor for audit T06.

Preserves frozen v0.2 untouched. Adds a result-row completeness check:
NOT_APPLICABLE requires a nonempty, human-readable applicability rationale.
This checks existence of a reason, not that it was preregistered or true.
NOT a promoted or independently accepted DDS instrument.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

FROZEN_BASE = Path(__file__).with_name("check_gate_profile_v0.2.py")


class ApplicabilityContractError(ValueError):
    """New v0.3 result-admission condition failed."""


def require_na_rationale(result: dict[str, Any]) -> None:
    """Enforce per-row NA rationale presence before running frozen v0.2.

    Whether a reason predates the inspected outcomes remains a separate
    preregistration and reviewer obligation.
    """
    for position, row in enumerate(result.get("gates", [])):
        if not isinstance(row, dict):
            raise ApplicabilityContractError(f"non_object_gate_row:{position}")
        if (row.get("applicability") == "NOT_APPLICABLE"
                or row.get("own_verdict") == "NOT_APPLICABLE"):
            rationale = row.get("applicability_rationale")
            if not isinstance(rationale, str) or not rationale.strip():
                gid = row.get("gate_id", f"row-{position}")
                raise ApplicabilityContractError(
                    f"not_applicable_requires_rationale:{gid}"
                )


def load_frozen_checker():
    """Load the original source file without editing it."""
    spec = importlib.util.spec_from_file_location("dds_stage_a_checker_v02", FROZEN_BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError("frozen_v02_checker_unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compile_successor(catalog: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    require_na_rationale(result)
    base = load_frozen_checker()
    compiled = base.compile_result(catalog, result)
    compiled["diagnostic_checker_successor"] = {
        "revision": "v0.3-audit-candidate",
        "additional_control": "T06-not-applicable-rationale-present",
        "pre_registration_verified": False,
        "independent_review_status": "NOT_ESTABLISHED",
        "stage_b_or_c_validation": "NOT_ESTABLISHED",
    }
    return compiled


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog")
    parser.add_argument("result")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        catalog = json.loads(Path(args.catalog).read_text(encoding="utf-8"))
        result = json.loads(Path(args.result).read_text(encoding="utf-8"))
        payload = json.dumps(compile_successor(catalog, result), indent=2, ensure_ascii=False) + "\n"
        if args.output:
            Path(args.output).write_text(payload, encoding="utf-8")
        else:
            sys.stdout.write(payload)
        return 0
    except (ApplicabilityContractError, ValueError, OSError, ImportError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
```

**Source pin:** [proposed v0.3 checker](./gate-diagnostic/check_gate_profile_v0.3_audit_candidate.py), blob `97430b0cd933f080a31bc3118d6871f7256c61ed` and [commit](https://github.com/dakleyer/structural-awareness-contributions/commit/f76c732d8dafd72263df1fca4fd39a8fe6f1576f).

**Negative controls:** [seven tests](./gate-diagnostic/test_na_rationale_v03.py), blob `9b73180f5aef82b0e38fe790d0e6278cc619db5c`, [test commit](https://github.com/dakleyer/structural-awareness-contributions/commit/e1b7619e702775ed38ef7f7a1a159c93e75d0121). Author-side isolated pre-check tests returned `Ran 7 tests ... OK`; this is **not** a full v0.2 catalog replay or independently signed audit.

**Unchanged scientific/technical claims:** The v0.2 catalog, checker, audit manifest, Stage A v0.1 profile, all frozen fixtures and historical results retain their original bytes. `NOT_APPLICABLE` still needs a preregistered, materially justified out-of-scope decision: the successor verifies a nonblank text field only and **cannot** establish when the rationale was written. It does not close G03.a runtime-claim propagation, G03.c positive fixture/multihop work or G03.d L4 calibration.

**Next actual gate:** execute both v0.2 and v0.3 against the same fully registered catalog and input, with a PASS control, missing-rationale mutant, raw input/output hashes and named reviewer. Only then propose promotion; no freeze is overwritten.

---

## T05 — applied G03.a cross-stage claim output projection (Plan de Cambios 2.1, 10 October 2026)

**Source/audit**: [Reconciled audit G03.a/T05](https://github.com/dakleyer/structural-awareness-contributions/tree/main/research/ecosystem-awareness) · objective: prevent Stage A specification PASS from being read as Stage B runtime enforceability. **Strategy:** DS-02, DS-08 and DS-12: one DDS method, affirmative scoped result, add an auditable successor rather than revising frozen evidence.

**Authority:** User explicitly authorized the five-phase change process. **State:** `T05_IMPLEMENTED_AUTHOR_TESTED; INDEPENDENT_AGENT_REVIEW_NOT_PERFORMED`. This is not Stage B approval or independent external audit.

**Old checker blob:** `97430b0cd933f080a31bc3118d6871f7256c61ed` (v0.3 T06 predecessor). **New checker blob:** `69c3bafe024d99a534ba8896ef12e0ba277ab8f6`, [commit](https://github.com/dakleyer/structural-awareness-contributions/commit/9393375a5a459ca9c55fd4acb81fff2cd7676990).

### TEXTO ANTES — original module description

```python
"""Proposed DDS Stage A v0.3 checker successor for audit T06.

Preserves frozen v0.2 untouched. Adds a result-row completeness check:
NOT_APPLICABLE requires a nonempty, human-readable applicability rationale.
This checks existence of a reason, not that it was preregistered or true.
NOT a promoted or independently accepted DDS instrument.
"""
```

### TEXTO DESPUÉS — published module description

```python
"""Proposed DDS Stage A v0.3 checker successor for audit T05 and T06.

Preserves frozen v0.2 unchanged. T06 checks that every NOT_APPLICABLE
result provides a nonblank rationale (not its preregistration). T05 projects
Stage A declaration separately from Stage B realization/runtime assurance
for runtime-named claims. A Stage A pass is not runtime verification.
This remains an unadmitted audit candidate, not an independently accepted
instrument or a Stage B/C implementation result.
"""
```

### TEXTO ANTES — insertion location after `load_frozen_checker()`

**No cross-stage projection function existed** between `load_frozen_checker()` and `compile_successor()`.

### TEXTO DESPUÉS — full new cross-stage projection function

```python
def project_cross_stage_claims(compiled: dict[str, Any], catalog: dict[str, Any]) -> None:
    """Separate Stage A declaration from runtime assurance in named claims.

    Preserve v0.2's Stage A profile_outcome. Its authoritative reference is
    the frozen Challenge/specification, not a Stage B/C execution trace.
    Never trust participant-supplied Stage B status in a Stage A result.
    """
    catalog_claims = catalog.get("named_claims", {})
    runtime_named = (
        "CLAIM-RUNTIME-ENFORCEABILITY",
        "CLAIM-TRACEABLE-DISPOSITION-TO-ENFORCEMENT",
    )
    for name in runtime_named:
        if name in catalog_claims and not catalog_claims[name].get(
                "stage_b_required_for_runtime_claim"):
            raise RuntimeError(f"stage_b_requirement_missing_for:{name}")

    projected = []
    for claim in compiled.get("named_claims", []):
        name = claim.get("claim")
        source_claim = catalog_claims.get(name, {})
        if not source_claim.get("stage_b_required_for_runtime_claim", False):
            continue
        stage_a = claim["status"]
        claim["stage_a_declaration_status"] = stage_a
        claim["stage_b_realization_status"] = "NOT_ESTABLISHED"
        claim["runtime_assurance_status"] = "NOT_ESTABLISHED"
        claim["claim_scope"] = "STAGE_A_DECLARATION_ONLY"
        claim["runtime_assurance_note"] = (
            "Stage A evaluates the declared rule, not Stage B architecture "
            "realization or observed Stage C effects."
        )
        # A consumer inspecting only 'status' can no longer mistake a
        # Stage A declaration PASS for runtime enforcement verification.
        if stage_a == "PASS":
            claim["status"] = "CONDITIONAL_ON(STAGE_B_VERIFICATION)"
        elif stage_a.startswith("FAIL"):
            claim["status"] = stage_a
        else:
            claim["status"] = (
                "CONDITIONAL_ON(STAGE_A_DECLARATION,STAGE_B_VERIFICATION)"
            )
        projected.append(name)

    summary = compiled.setdefault("summary", {})
    summary["profile_outcome_scope"] = "DDS_STAGE_A_ONLY"
    summary["stage_b_realization_status"] = "NOT_ESTABLISHED"
    summary["runtime_assurance_status"] = "NOT_ESTABLISHED"
    summary["cross_stage_claims_projected"] = sorted(projected)
```

### TEXTO ANTES — complete previous `compile_successor`

```python
def compile_successor(catalog: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    require_na_rationale(result)
    base = load_frozen_checker()
    compiled = base.compile_result(catalog, result)
    compiled["diagnostic_checker_successor"] = {
        "revision": "v0.3-audit-candidate",
        "additional_control": "T06-not-applicable-rationale-present",
        "pre_registration_verified": False,
        "independent_review_status": "NOT_ESTABLISHED",
        "stage_b_or_c_validation": "NOT_ESTABLISHED",
    }
    return compiled
```

### TEXTO DESPUÉS — complete published `compile_successor`

```python
def compile_successor(catalog: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    require_na_rationale(result)
    base = load_frozen_checker()
    compiled = base.compile_result(catalog, result)
    project_cross_stage_claims(compiled, catalog)
    compiled["diagnostic_checker_successor"] = {
        "revision": "v0.3-audit-candidate",
        "additional_control": "T06-not-applicable-rationale-present",
        "additional_controls": [
            "T05-stage-a-declaration-versus-stage-b-runtime-claim-projection",
            "T06-not-applicable-rationale-present",
        ],
        "pre_registration_verified": False,
        "independent_review_status": "NOT_ESTABLISHED",
        "stage_b_or_c_validation": "NOT_ESTABLISHED",
    }
    return compiled
```

### Regression source and five-phase record

**Test file:** [T05 16-test module](./gate-diagnostic/test_t05_cross_stage_v03.py) at blob `2146b303e2a17719cd98ec95f8f1847a67ba40b8`, initially published in [commit 246b0311](https://github.com/dakleyer/structural-awareness-contributions/commit/246b03119ffc00a8e45568234b689bdbb6330a12) and corrected in [commit 2b0b7872](https://github.com/dakleyer/structural-awareness-contributions/commit/2b0b7872d8143a3ae84a2c7502c4d8590cf49c23) to use the **actual published checker filename**. The only change in the test correction was that import target.

1. **Exact plan:** unchanged old description and function documented above; additional helper and full replacement shown, unmodified frozen v0.2 and v0.2 catalog.
2. **Pre-application challenge:** local author tests 16/16 and six injected mutants detected 6/6, performed in separate subprocesses. This is an independent *execution process*, not an independent agent or external review.
3. **Application:** 3 GitHub commits changed only the v0.3 checker and the new T05 test file. Source-owner promotion has not occurred.
4. **Source integrity:** old/new file blobs re-read; frozen v0.2 checker `0aa51e7b050123c4a09967a5fae52bf290b6c8a5`, catalog `92e1c2b1f4316f77636f669c8b62a1d53091c372` and Stage A v0.1 remain unchanged.
5. **Readability/semantic review:** native Stage A result remains in `stage_a_declaration_status`; runtime-named claim `status` is conditional rather than plain PASS; profile-wide result carries `profile_outcome_scope=DDS_STAGE_A_ONLY`; T06 NA-rationale rule remains. A separate full 15-gate frozen catalog replay and named external review remain open.

**External reviewer/agent needed:** inspect original catalog and compare emitted Stage A data with Stage B handoff requirements, test consumer interpretation, sign the source pins and audit the new projection contract. `PROFILE_PASS` explicitly remains *a Stage A profile result only*.

---

## G02.b / T04 — Prospective review, freeze, amendment and dispute envelope (Change Plan 4.0; 10 October 2026)

**Status:** EDITORIAL_PROPOSAL_PUBLISHED; prospective template only; NOT_FROZEN; NOT_INDEPENDENTLY_REVIEWED; T04_NOT_CLOSED. This section is an append-only governance proposal in the *owning Stage A VNext*, not a change to Stage A v0.1, the frozen v0.2 diagnostic instrument, DDS Stage B/C, a scientific result, or an external source-owner contract.

**Why this is proposed:** The reconciled audit v3.1 classifies G02.b/T04 as a review/freeze/dispute minimum-envelope gap. G02.a/T03 separately concerns attributable reviewer independence. The documentary strategy v3.3 calls for source-owned, minimal, conserved revisions (DS-12), without retroactively rewriting frozen material. The controlling full audit and strategy must be read before asserting formal T04 closure.

### T04-E1. Minimum prospective review record (one version per frozen review)

For each future review, create a dated record using the following *field names and null semantics*. Empty values, `UNKNOWN`, `NOT_ESTABLISHED`, and merely author-reported claims cannot be promoted into evidence of independence, freeze, or acceptance.

```yaml
review_id: REQUIRED_UNIQUE_ID
review_version: 0.1
object_stage: STAGE_A | STAGE_B | STAGE_C | MIXED_UNCLASSIFIED
review_target: REPOSITORY_PATH_OR_STABLE_EXTERNAL_ID
target_git_commit: REQUIRED_PINNED_COMMIT_OR_NOT_ESTABLISHED
target_blob_sha: REQUIRED_PINNED_BLOB_OR_NOT_ESTABLISHED
review_question_and_claim_ceiling: REQUIRED_BEFORE_FREEZE
review_owner: REQUIRED_NAMED_RESPONSIBLE_PARTY
reviewer_identity: NOT_ESTABLISHED
reviewer_affiliation_and_role: NOT_ESTABLISHED
reviewer_relationship_to_authors: NOT_ESTABLISHED
conflict_of_interest_declaration: NOT_ESTABLISHED
independence_status: NOT_ESTABLISHED
criteria_and_acceptance_ref: NOT_ESTABLISHED
criteria_version_or_hash: NOT_ESTABLISHED
frozen_inputs_and_versions: []
freeze_time_utc: NOT_ESTABLISHED
freeze_actor: NOT_ESTABLISHED
blind_information_boundary: NOT_ESTABLISHED
adversarial_and_positive_controls: []
execution_or_document_review_record: NOT_RUN
raw_input_hashes: []
raw_output_hashes: []
findings_and_dispositions: []
reviewer_dissent_and_objections: []
dispute_resolution_authority: NOT_ESTABLISHED
amendment_history: []
reviewer_signoff: NOT_ESTABLISHED
owner_disposition: PENDING
external_acceptance: NOT_ESTABLISHED
```

The record is a proposed *minimum information envelope*, not an executable validation claim and not a declaration that a reviewer has been engaged. If `object_stage=MIXED_UNCLASSIFIED`, the review must separately identify the tested objects and governing references before any stage-specific acceptance.

### T04-E2. Freeze and change-control rules

1. **Before outcomes:** identify the review target, acceptance criteria, input versions, positive/adversarial controls, reviewer relationship, and information boundary; record the freeze timestamp, responsible actor and immutable source pins. If any necessary field is missing, classify the review `ENVELOPE_INCOMPLETE`, not accepted.
2. **During review:** distinguish the original raw observations from interpretations; preserve reviewer dissent even when the owner disagrees. A second script, separate prompt or repeated author pass does **not** establish a second independent reviewer.
3. **After freeze:** a changed target, criterion, fixture, input, reviewer identity, or material conflict opens an explicitly linked **successor review version**; do not alter the predecessor to make its earlier result look preregistered.
4. **Dispute:** log objected-to claim, evidence pins, disagreeing parties, proposed resolution, authorized decision maker and the final status. An unanswered objection stays `UNRESOLVED`, even if editorial text was published.
5. **Promotion:** publishing this template does not close G02.b/T04. A future claim of closure requires a named reviewer, dated pre-outcome freeze, independently held raw inputs and outputs as applicable, adjudication of dissent, owner disposition and an attributable signed acceptance record. No Stage B/C, UC-4 or product result follows from Stage A documentary review.

### T04-E3. Adversarial acceptance checks (future execution; NOT_RUN here)

- **A — retroactive freeze mutant:** change a criterion after the first observed outcome; expected result: `INVALID_PRE_REGISTRATION` and a new version required.
- **B — nominal reviewer mutant:** omit conflict/relationship or reuse author identity while asserting independence; expected result: `INDEPENDENCE_NOT_ESTABLISHED`.
- **C — disappearing dissent mutant:** omit a recorded objection from a later summary; expected result: `LOSS_OF_REVIEW_HISTORY`.
- **D — silent input replacement mutant:** change a source blob without changing its pin; expected result: `SOURCE_MISMATCH`.
- **E — false-stage promotion mutant:** interpret Stage A document PASS as realized runtime assurance; expected result: `STAGE_BOUNDARY_VIOLATION`.
- **F — controlled positive review:** freeze a complete, accurately attributable record, preserve controls and disagreement status, and report only the claim ceiling actually examined; expected result: `ELIGIBLE_FOR_REVIEWER_DECISION`, **not** automatic approval.

### T04-E4. Acceptance and ownership limits

**Present effect:** a review-envelope proposal is available in the existing owner-ledger, with no historical text replaced. **Still open:** a direct reading of the full v3.1 T04 audit card by a named independent reviewer; final selection of required/optional fields, actual freeze/adversarial runs, raw evidence custody, dispute resolution and source-owner acceptance. T03 reviewer-independence questions remain separately open. Future T04 implementers must compare the proposal with those primary sources, preserve this version, and record an exact BEFORE/AFTER successor before any normative incorporation.

**Result:** `T04_PROPOSAL_PUBLISHED_IN_VNEXT`; `T04_AUDIT_CLOSURE=NOT_ESTABLISHED`; `SCIENTIFIC_CORPUS_UNCHANGED_BY_THIS_EDITORIAL_INSERTION`.

---

## Auditorías anteriores frente al corpus vigente — 12 octubre 2026

**Codex, mismo asistente; `17b597bf91acb0f37daebc716e8f23f65daa23eb`.** Se cotejaron Index/Stages A-B-C, Stage A antes/después, UC4/oráculo y checkers v0.2/v0.3. Especificación, arquitectura y ejecución mantienen referencias distintas. T05/T06 tienen un sucesor publicado con su estado de autor; no se repiten como nuevos arreglos pendientes. No se ejecutó ningún instrumento.

La regla 8 de retirar propuestas contradice la conservación del viejo, discusión y desacuerdo. Git mantiene el ledger del 6 de octubre; no se reconstruye ni se reaplica su historia. Las nuevas reglas T04 sobre conservar dissent no devuelven automáticamente lo retirado.

El nuevo guard NA comprueba un motivo, pero no el tipo de `na_substitute_satisfied`. v0.2 usa truthiness y v0.3 hereda ese flujo. Una fila NA con motivo no vacío y el string `"false"` puede satisfacer la rama. Es razonamiento estático, no reproducción experimental o diagnóstico de todo el instrumento. [EP VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md#nueva-revisión-integral-de-cambios-y-consistencia--12-octubre-2026) registra el conjunto y los receptores.

### Cambio 74 — Rechazar sustitutos NA de tipo string antes de adjudicar

**Beneficio:** Evitar que un valor no booleano como "false" satisfaga por truthiness una dependencia NOT_APPLICABLE, produciendo calificación no sustentada.
**Fuente:** `research/ecosystem-awareness/gate-diagnostic/check_gate_profile_v0.3_audit_candidate.py`, blob `69c3bafe024d99a534ba8896ef12e0ba277ab8f6`, snapshot `17b597bf91acb0f37daebc716e8f23f65daa23eb`. Función completa require_na_rationale; propuesta para futuro sucesor, no edición delactual.
**Impacto Alto; riesgo Medio; esfuerzo Medio; prioridad Primera; 3 — Contratos y protocolo de evaluación.**
**Riesgo concreto:** Cambiaría la admisión de inputs del checker sucesor; hay que mantener T05/T06, consumidores y versiones congeladas. No modifica el checker v0.2 ni resultados.
**Coste:** Lectura estática, registrar casos válidos/invalidantes y revisar el contrato de entrada y consumidores. Confirmación prospectiva en un sucesor, sin regraduar corridas históricas.
**Dependencias y orden:** Propuesta de sucesor de v0.3; antes de decidir registrar/revisar booleanos true/false, ausencia y strings/listas/números, conserva T05/T06. No se ejecuta ni modifica código congelado por esta auditoría. Decisión concreta de Iván.

**Texto antes — viejo literal completo**

~~~~python
def require_na_rationale(result: dict[str, Any]) -> None:
    """Enforce per-row NA rationale presence before running frozen v0.2.

    Whether a reason predates the inspected outcomes remains a separate
    preregistration and reviewer obligation.
    """
    for position, row in enumerate(result.get("gates", [])):
        if not isinstance(row, dict):
            raise ApplicabilityContractError(f"non_object_gate_row:{position}")
        if (row.get("applicability") == "NOT_APPLICABLE"
                or row.get("own_verdict") == "NOT_APPLICABLE"):
            rationale = row.get("applicability_rationale")
            if not isinstance(rationale, str) or not rationale.strip():
                gid = row.get("gate_id", f"row-{position}")
                raise ApplicabilityContractError(
                    f"not_applicable_requires_rationale:{gid}"
                )
~~~~

**Texto después — propuesto completo**

~~~~python
def require_na_rationale(result: dict[str, Any]) -> None:
    """Enforce typed NA substitution and rationale before running frozen v0.2.

    Whether a reason predates the inspected outcomes remains a separate
    preregistration and reviewer obligation.
    """
    for position, row in enumerate(result.get("gates", [])):
        if not isinstance(row, dict):
            raise ApplicabilityContractError(f"non_object_gate_row:{position}")
        if ("na_substitute_satisfied" in row
                and not isinstance(row["na_substitute_satisfied"], bool)):
            gid = row.get("gate_id", f"row-{position}")
            raise ApplicabilityContractError(
                f"na_substitute_satisfied_must_be_boolean:{gid}"
            )
        if (row.get("applicability") == "NOT_APPLICABLE"
                or row.get("own_verdict") == "NOT_APPLICABLE"):
            rationale = row.get("applicability_rationale")
            if not isinstance(rationale, str) or not rationale.strip():
                gid = row.get("gate_id", f"row-{position}")
                raise ApplicabilityContractError(
                    f"not_applicable_requires_rationale:{gid}"
                )
~~~~

**Instrucciones de Iván:** una VNext por unidad, originals en lectura, conservar conversaciones y viejo completo. Auditoría publicable, incorporación pendiente de su decisión concreta. Contraejemplo por lectura de código; no ejecución/reproducción experimental. Par literal actual localizado.

### Cambio 75 — Mantener auditorías y viejos publicados al cerrar propuestas

**Beneficio:** Resolver la contradicción entre eliminar propuestas incorporadas y conservar audit conversation/antes-después visible que Iván pidió.
**Fuente:** `research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md`, blob `985845b1876652a60a0cadfff40201085f40be0d`, snapshot `17b597bf91acb0f37daebc716e8f23f65daa23eb`. Regla8 delledger; no se reabre el estado deincorporación.
**Impacto Alto; riesgo Medio; esfuerzo Medio; prioridad Primera; 1 — Claridad de evidencia y estado.**
**Riesgo concreto:** Confundir historia con cola vigente o reabrir cambios ya incorporados; restaurar debe usar textos auténticos y estados fechados, sin tocar canon.
**Coste:** Conciliar reglas, recuperar/citar las épocas auténticas y mantener su disposición actual. Redactar una línea no devuelve por sí solo las auditorías retiradas.
**Dependencias y orden:** Conservar estados de incorporación y decisiones actuales; no reaplicar incorporados ni reconstruir viejos de memoria. Decidir presentación histórica y restitución auténtica dentro de la única VNext.



**Instrucciones de Iván:** una VNext por unidad, originals en lectura, conservar conversaciones y viejo completo. Auditoría publicable, incorporación pendiente de su decisión concreta. Contradicción documental confirmada; regla propuesta, recuperación de épocas pendiente


---

## Consistencia de DDS y sus receptores — 12 octubre 2026

**Auditoría por Codex, mismo asistente de IA, para revisión humana.** Corte público `eb5d66d7e22dc18f093ee33fcd564e1fac6d2338`. No hay un commit público posterior al corte de la revisión integral anterior. Se releen completos Index y Stages A/B/C y se contrastan sus pasajes con EA/EP, R01, Oracle/UC-4, HF y HC-HID/MSCA. Se verificó la disponibilidad por blob de los 2.194 archivos del árbol; ese control de custodia y la búsqueda de referencias no equivalen a una nueva lectura científica de todos ellos. No se ejecutaron programas, modelos, productos o experimentos.

**Juicio:** la estructura principal sigue siendo consistente. Stage A compara especificaciones/mecanismos con el Challenge; B verifica una realización contra el paquete A congelado; C contrasta una implementación fijada con el Challenge y efectos observados. Simplified declara cobertura; el modo de evidencia es otro eje. Ninguno de estos nombres cambia los A/B/C/D epistemológicos de 00M, los Stage-0/1 de UC-4, las etiquetas locales de brazos o el significado de C02/C11/T03.

### Lecturas cruzadas y límites

- **Index ↔ Stage A:** Index §§1–6 y Stage A §§2.1/6/10/17 preservan objeto, referencia, paquete de salida y no promoción. La nota inicial de Stage A todavía dice “explicit DDS stages” para Stage1/Stage2; §13.1 conserva el vocabulario de extensión anterior. Index §5 reserva DDS Stage A/B/C para el desarrollo y su registro llama Stage1/Stage2 disciplina interna de A. Hay una ambigüedad de lectura al entrar, no evidencia de que hayan aparecido otras dos etapas ni cambiado las obligaciones. La propuesta 76 aclara sólo el primer párrafo; mantiene títulos, anchors e identificadores históricos.
- **Stage A ↔ B ↔ C:** B §§2/4/13 exige congelar el paquete antes de adjudicar, conserva fallos y abre un sucesor A cuando la especificación necesita revisión. C §§2/4/7/15 exige configuración, referencia y observación adecuadas; un producto previo puede entrar por correspondencia explícita. La ruta A→B→C no es una promoción automática, ni exige inventar diseño DDS previo para todo producto. Un modelo ejecutable no se convierte en C por ejecutarse.
- **C02/UC-4 ↔ DDS:** el Oracle README identifica instrumentación compartida; UC-4 §4.1 es una nota de diseño y conserva el alias anterior “Architecture Conformance”. Su contenido usa el paquete A como referencia y distingue efectos; no crea una autoridad rival a Stage B. Los instrumentos/calendarios locales no demuestran B/C ni admisión externa. No se necesita una corrección a un registro congelado para uniformar ese alias.
- **HF ↔ requisitos ↔ MSCA:** los dos textos del 12 de octubre distinguen recalificación local y arquitectura completa. S3/S10/T1 y F2/APQ pueden sostener una pregunta de detección/recalificación; S1/S14 no son sensores ni actuadores por su sola definición. CH-01…CH-08 son casos futuros, no añadidos al paquete ciego v0.3. MSCA §4.1 mantiene señal, capacidad y autoridad separadas; observar una novedad no impone migración de rol. Ver [comentario receptor en HF VNext](./baseline/reductions/00G-R01/extensions/hugging-face/README_VNext.md#consistencia-con-dds-y-msca--12-octubre-2026) y [Operation VNext](../../standards/minimum-sufficient-control/04_OPERATION_VNext.md#consistencia-con-dds-y-recalificación-local--12-octubre-2026).
- **Coste humano ↔ comparación DDS:** HC-HID §7A conserva vector cuando las magnitudes no son conmensurables y exige regla explícita para sumar/normalizar. Operation §4.1 exige mismo Challenge, calidad y autoridad; una ruta M más barata no acredita llegar al mismo I. Esa compatibilidad conceptual no mide capacidad humana, latencia real, ROI ni eficacia.

La frase del Index fechada el 7 de octubre sobre HF preparado no invalida las ejecuciones sintéticas posteriores: el lector HF distingue aquellas aproximaciones de la adjudicación histórica/prerregistrada pendiente. No se propone una etiqueta de “Stage A superado” para resolver una diferencia de fechas. [EA VNext](./README_VNext.md#consistencia-de-la-ruta-dds--12-octubre-2026) y [EP VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md#consistencia-del-corpus-en-torno-a-dds--12-octubre-2026) recogen las consecuencias para lectores.

### Auditorías anteriores que conservan vigencia

**74** sigue siendo una propuesta de admisión booleana del futuro checker: el código publicado no cambió desde el corte anterior, no se reprodujo aquí el contraejemplo y no se invalidan retrospectivamente resultados. **75** sigue identificando pérdida de historia visible frente a la instrucción de conservación; T04 exige preservar desacuerdos pero no devuelve por sí mismo lo retirado. T05/T06 mantienen autoría, independencia no establecida y replay completo pendiente. No se reabre su incorporación como si no hubiera sucedido, ni se declara cierre de T03/T04 o de las cinco/sexta científicas.

### Cambio 76 — precisión de la primera nota de Stage A

**Fuente vigente:** [Stage A](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md), blob `5b8517185308f75f57b8ce2096360e27d760438a`, línea 5 en el corte citado. Viejo literal completo: una coincidencia; propuesto: ninguna. **Impacto esperado Medio; riesgo Bajo; esfuerzo Bajo; prioridad Siguiente; tanda 1, claridad de evidencia y estado.** Beneficio: distinguir al primer vistazo las tres etapas DDS de las dos fases de extensión dentro de A. El índice y el cuerpo ya contienen la distinción correcta; no se demuestra un fallo técnico por la ambigüedad.



**Riesgo y coste concretos:** preservar Stage1/Stage2, §13.1 y sus anchors, contratos, versiones y resultados. El trabajo es una relectura/localización y custodia de un párrafo, con contraste Index §5/Stage A §6 y lector HC-HID; no requiere un nuevo test o expediente. **Dependencia/orden:** precisión documental separable de 74/75; no los resuelve. **Decisión de Iván:** pendiente sobre este pasaje exacto; candidato preparado para leer y decidir, no autorizado ni aplicado. Instrucción vigente: originales sólo en lectura y una VNext acumulativa. No se propone otro cambio canónico cuando el contexto actual ya mantiene la frontera.


---

## Registro de aportaciones y frontera del método — 12 octubre 2026

**Codex, mismo asistente; nuevo corte `f437c95cce3645a05ba45f52f521f6b9692e0aa7`.** Tras la publicación del cotejo anterior entró el [registro de veinte aportaciones potenciales](./DDS_POTENTIAL_CONTRIBUTIONS_REGISTER_v0.1.md), leído completo. El Index incorpora un banner de ruta hacia él; Index anterior recuperable por su snapshot y por retirada exacta del único banner. A/B/C, checker, catálogo, resultados y requisitos no cambiaron en ese merge.

**Consistencia mantenida:** todas las propuestas se vinculan a un propietario actual; un mecanismo o prueba no hereda automáticamente una aceptación. Las piezas de suficiencia, permiso receptor, mapas parciales, contradicción, computabilidad, cierre, cache/dependencias y cambio temporal mantienen sus distintos objetos y restricciones. Los tres ejemplos son construcciones ilustrativas con costes hipotéticos, no ahorros medidos o demostraciones de los artículos originales. Un peer fuerte puede empatar o ganar. [EA VNext](./README_VNext.md#nuevo-registro-de-aportaciones-dds--cotejo-del-merge-del-12-octubre-2026) registra el juicio específico de cada familia y sus fuentes pendientes.

**Dos condiciones a explicitar al concretar perfiles, sin cambiar el texto ahora:**

1. **DDS-PC-010, “C measured instrument if admitted”.** Si se califica el instrumento usado para medir otra tecnología, es infraestructura y no un resultado sustantivo C de esa tecnología. Si la tecnología objeto del Challenge es un instrumento real, su implementación puede ser objeto de C bajo el contrato de Stage C. La tabla común §2 mantiene esa frontera, pero la tarjeta deberá escoger y nombrar el objeto antes de SPECIFICATION_READY. Pregunta pendiente: ¿se prueba el evaluador o una implementación de medición como tecnología candidata? No se fabrica un par de reemplazo mientras no se haya elegido ese alcance.
2. **DDS-PC-011/012/020, humanos.** Un scheduler o ledger técnico puede evaluarse bajo un perfil declarado; disponibilidad, causalidad de carga y retención reales exigen validación de constructo, fuentes humanas y protocolo propios. Stage C de software no cierra ese estudio. Las tarjetas ya conservan esta separación; no añadir un requisito universal o un precio/hora sintético para suplir datos.

P1/P2/P3 son prioridad de desarrollo, no DDS Stage ni autorización de ejecución o cambios mínimos de bajo riesgo. Las veinte PROPOSED no son veinte modificaciones quirúrgicas listas y no subsanan T03/T04/T05/T06, ni 74/75/76. La propuesta 76 sigue contra el mismo blob de Stage A; el nuevo banner del Index no cambia su viejo. No se modifica el register adicional, se crea otro expediente o se activa campaña. Canon en lectura y pasadas científicas pendientes conservan su estado real.


---

## Acotar el cambio de conservación — 12 octubre 2026

**Codex, mismo asistente; corte `21c3946009af4a14433d7240eddce939e4ff9599`, este ledger blob `83bf1e5cb96805669c803a2bba3dc2cf7ce895c1`.** Iván pide planes al final de las VNext, alto impacto y bajo riesgo con muy poco texto. El cambio75 completo incluye recuperar/reconciliar historia auténtica y mantiene riesgo/esfuerzo Medio. El74 cambia admisión del checker y sigue riesgo Medio; no se presenta como arreglo textual de bajo riesgo. T04 y las auditorías anteriores permanecen.

La alternativa siguiente se limita a evitar retiradas futuras mediante una regla. No recupera las propuestas ya retiradas, no convierte un antecedente reconstruido en auténtico, no reabre lo incorporado y no cierra75/T04. Es una variante del75, no un nuevo hallazgo ni otro expediente. Su impacto Alto corresponde a preservar evidencia visible para revisiones y decisiones futuras; su riesgo Bajo corresponde exclusivamente a ese alcance documental.

## Plan de cambios al final — variante textual del 75

**Ubicación:** §5, regla8 del cuerpo anterior, fuera de las citas de propuestas. Viejo: una coincidencia en ese contexto; propuesto: ninguna. **Impacto esperado Alto; riesgo Bajo; esfuerzo Bajo; prioridad Primera.** Aplicado el 12 de octubre de 2026 en `908fdc6c9372b533d1a383d490227333ce4756be`; variante fuera de pendientes.



**Beneficio concreto:** impedir que cerrar una propuesta elimine el viejo/nuevo, la discusión o el desacuerdo de la única VNext. Fecha, versión y decisión separan historia de pendientes. No hace falta otro índice o una VNext por auditoría.

**Riesgo concreto:** la regla es prospectiva; no declara recuperadas las conversaciones antiguas ni altera el estado de una incorporación. Las notas fechadas sobre retiradas pasadas conservan su significado histórico. **Coste:** cotejo de una regla con conservación del procedimiento y T04, custodia y lectura de vuelta; restauración/adjudicación histórica sigue en el75 completo con riesgo/esfuerzo Medio.

**Compatibilidad y orden:** esta variante y el75 amplio reemplazan la misma regla: escoger una redacción, no aplicar dos reemplazos. Decidir esta variante no descarta el trabajo histórico pendiente. No modifica Stage A, Stage B/C, checkers, pruebas, hashes o resultados. **Instrucción de Iván:** conservar originales y conversaciones, una VNext por unidad y viejo completo visible. **Decisión:** Iván aprobó y se incorporó esta regla en `908fdc6c9372b533d1a383d490227333ce4756be`. La recuperación histórica del75 mantiene su trabajo separado por concretar.

**Fuera de esta tanda:** 74 necesita el sucesor/contrato y comprobaciones prospectivas; 75 histórico necesita custodia auténtica. Los tres SHA256/README requieren identificar épocas; no se corrigen hashes para simular conservación. Las siete réplicas conservan propietario/custodia y no se borran. Los resultados HF contrarios siguen válidos dentro de su scope. 76 es claridad de impacto Medio, riesgo Bajo; se conserva pero no se eleva artificialmente a Alto. [Primera tanda conjunta](../../architectural-contributions/ecosystem-positioning/README_VNext.md#primera-tanda-textual-de-alto-impacto-y-bajo-riesgo--12-octubre-2026).


---

<a id="ola2-cambio-06"></a>

## Ola 2 — cambio 6: DDS: tres etapas y dos fases internas de Stage A

**12 octubre 2026 · Codex.** Propuesta derivada de cambio 76; conserva los planes anteriores. Propuesta preparada; pendiente del go de Iván para esta ola.

**Fuente actual:** [research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md](https://github.com/dakleyer/structural-awareness-contributions/blob/908fdc6c9372b533d1a383d490227333ce4756be/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md), blob `5b8517185308f75f57b8ce2096360e27d760438a`. **Ubicación:** Nota Extension-stage clarification0.1.3 al principio.

**Justificación:** La primera nota llama etapas DDS a dos fases internas. La corrección la alinea con el índice y evita que el lector infiera cinco etapas.

**Impacto esperado Medio; riesgo Bajo; esfuerzo Bajo; prioridad Siguiente.**

**Riesgo concreto:** Mantener Stage1/Stage2, rutas y contenido técnico. Cambiar sólo la nota inicial no altera las etapas, obligaciones o resultados. **Coste:** Localización, sustitución y verificación del pasaje y sus referencias inmediatas.

**Dependencias y aceptación:** Index §5 y Stage A §§6/13.1; conservar nombres históricos Stage1/Stage2 e identificadores.

### Nota Extension-stage clarification0.1.3 al principio

Viejo verificado una vez fuera de citas de propuestas, línea 5 de la fuente fijada.



**Instrucción de Iván:** presentar los pares en la VNext antes de traerlos al chat y ejecutar sólo después del go de cada ola. **Decisión:** pendiente. Originales y fuentes congeladas conservados; estos pares preparan la redacción de revisión. Las variantes anteriores quedan como historia; esta selección no autoriza aplicarlas conjuntamente.


---

<a id="ola2-redaccion-06"></a>

## Ola 2 — redacción directa del cambio 6

**12 octubre 2026.** Iván solicita textos asertivos y concretos. Esta es la redacción propuesta vigente del cambio 76; la anterior queda como antecedente.

**Propósito:** La primera nota llama etapas DDS a dos fases internas. La corrección la alinea con el índice y evita que el lector infiera cinco etapas.

**Impacto Medio · Riesgo Bajo · Esfuerzo Bajo · Prioridad Siguiente.** Se mantienen las dependencias, aceptación y valoración del plan de Ola2.

**Fuente:** [research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md](https://github.com/dakleyer/structural-awareness-contributions/blob/ef0b8c1ef489226bbb6f81b0fb6028f2c32c50f8/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md), blob `5b8517185308f75f57b8ce2096360e27d760438a`.

### Nota Extension-stage clarification0.1.3 al principio



**Decisión de ola:** aprobada por Iván y aplicada el 12 de octubre de 2026 en `a27679dc451ce2db77432df2b206bb08339b24ef`. Cambio76 hecho y retirado de pendientes; se conserva el par completo.


## Aplicaciones confirmadas — 12 octubre 2026

- **Aplicado:** Ola1 variante limitada75.
- **Aplicado:** Ola2 cambio6 / propuesta76.

Publicación comprobada: [a27679dc451ce2db77432df2b206bb08339b24ef](https://github.com/dakleyer/structural-awareness-contributions/commit/a27679dc451ce2db77432df2b206bb08339b24ef). Estos cambios están hechos y quedan fuera de pendientes. Se conservan sus textos antes/después y las auditorías.

Continúan por separado el checker74 y la recuperación histórica75. La regla futura75 y la precisión DDS76 ya están aplicadas.


## Bloques aplicados retirados

Por instrucción de Iván, los pares literales ya incorporados se retiran de esta VNext. Se conservan las auditorías y los cambios pendientes. Los textos cerrados y sus decisiones se consultan en el [historial anterior a la retirada](https://github.com/dakleyer/structural-awareness-contributions/blob/590198efd529ffd302fba2d982a126ee51a07068/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md).


## Revisión del diseño de consolidación DDS por campañas — 12 octubre 2026

**Auditoría realizada por Codex, mismo asistente; revisión documental sobre el corte `07c83653babec79f387bdfd5fc4b93e4ac21b533`.** Iván solicita analizar el borrador autocontenido v0.2 de reorganización, no ejecutar la migración. Se leyó el plan completo y se contrastaron la navegación controlada, el método A/B/C, los contratos HF v0.3 y v0.3.1, sus ocho bindings de paquete, el catálogo de extensiones y los recorridos bot v0.6. El documento recibido permanece fuera del repositorio; aquí se publican las conclusiones de revisión.

El diseño coincide con DDS en distinguir objetos A/B/C y modos de evidencia, conserva los inputs y no convierte un resultado A en B/C. La regla organizativa «una campaña, una etapa» debe declararse como política prospectiva del registro, compatible con el método. No se exige dividir expedientes históricos ni alterar su identidad. Separar identidad de campaña, versiones materiales del contrato, runs y sucesores; registrar una campaña no equivale a aceptarla.

No recomiendo crear una segunda fuente metodológica mantenida en dds/canonical. El Index actual contiene enlaces ./baseline/..., y su copia literal a otra ubicación resolvería a destinos diferentes. Usar referencias inmutables al original; si posteriormente se requiere snapshot, identificarlo como copia y conservar su contexto. REGISTRY.json organiza campañas; el Index clasifica el método, el catálogo clasifica estudios, el registro de claims mantiene consumidores y el de aportaciones es backlog. Falta especificar sincronización/propietario de datos comunes.

La aceptación del plan dice rechazar «Stage retrospectivo», mientras otras secciones permiten clasificación histórica documentada. Hay que precisar: se admite clasificar retrospectivamente por objeto/evidencia; se rechaza atribuir un prerregistro, ejecución, aceptación o Stage más fuerte que lo demostrado. Esa distinción ya está en Index §7.

Preservación exige versiones exactas de inputs, no sólo estado actual. El expediente HF ilustra un mapa FG-TIDA fijado a blob38d64f61ef81a300a20d9d89cda65e5bb6ba5b22 distinto de main. La salida científica de una campaña se versiona por su contrato; el nombre de carpeta no le otorga aprobación. Una réplica archivística de una VNext no abre un expediente nuevo; toda conversación continúa en la única VNext propietaria.

[EP VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md) concentra el juicio estratégico y las condiciones; [EA VNext](./README_VNext.md) y [HF VNext](./baseline/reductions/00G-R01/extensions/hugging-face/README_VNext.md) registran las relaciones. Primera tanda sugerida de indexación: impacto Alto/riesgo Bajo/esfuerzo Medio. La copia y adopción operativa permanecen propuestas separadas; no se añade todavía canon, código, carpetas, pruebas o campañas.


## UC-21 y DDS: dos entradas enlazadas — 12 octubre 2026

**Revisión por Codex, mismo asistente.** Iván precisa que UC-21 es el caso con objetivos y campañas, y DDS el método de investigación. Se mantiene esta distinción y se ajusta el orden del diseño de consolidación: primero probar la navegación desde UC-21 usando sus ejercicios existentes; después comprobar su generalidad con HF y otra familia. No se crea una nueva campaña S5 ni se mueve el caso al corpus metodológico.

La entrada pública [UC-21](https://github.com/FG-TIDA/use-cases/issues/21) remite en su cuerpo al snapshot `aec08fb5b0fac2ee399372370e9ee2a82a2d5779`. Su cuerpo no nombra DDS; sus comentarios sí lo explican en [S5](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6109154445) y [S4/CDA](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6111953753). README y USE_CASE coinciden entre aquel snapshot y la rama de revisión `76ac39bae74d10f4586f5fb787f69deaf7f59add`, pero S6 de la rama es un adapter hacia 00J/00J-A01. Por eso publicar una propuesta en la rama no modifica lo que alcanza el lector del enlace congelado. Una futura actualización de la entrada debe añadir una ruta explícita al seguimiento y mantener el envío anterior. La Issue y sus comentarios no se modifican aquí.

El [autor de S5](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6115830369) propone cerrar en el alcance evidenciado. Se comprobó su README externo v0.1.3, blob`4b0d2a673c8ee945bd6c52248390a3c595b9285a`: declara `I2-complete` completo para las ramas seleccionadas dentro del modelo y separa predicates enforced/assumed upstream. Esto explica el estado de esa discusión; no constituye una nueva aceptación conjunta ni un rerun. La organización conserva el ejercicio y sus pins, sin reiniciarlo para llenar el registro.

**Relación propuesta:** entrada UC-21 → explicación del caso y objetivos → escenarios/hipótesis → ejercicios existentes → contrato DDS aplicable → runs/evidencia → conclusión para el objetivo UC-21 → posible selección posterior de especificaciones. Desde DDS se recorre la misma relación por método → campañas de distintos casos → fuente del Challenge → evidencia → resultado. El registro futuro debe apuntar a los expedientes reales y sus propietarios, con varias relaciones por campaña; no duplicarlos bajo ambas entradas.

**Asignación de funciones:** UC-21 mantiene su problema, objetivos, HC/HR/HS/H1–H6 y gates. DDS mantiene método y A/B/C. El expediente del estudio mantiene contrato, versión, comparadores, ejecución y conclusión. EA, RA, MSCA y otros componentes conservan fuentes y decisiones de incorporación. Objetivo, R0/R1/R2, Stage A/B/C, modo de evidencia y estado de ejecución son dimensiones separadas. Un resultado del caso no demuestra automáticamente necesidad de EA ni selección de una especificación.

**Preservación:** enlaces actuales, snapshot enviado, anexos, escenarios, figuras, pruebas, denominadores y autoría conservados. Toda relación estructural se revisa en las VNext de README correspondientes; tres niveles EP→Awareness→índices técnicos, con expedientes de campaña como documentos de trabajo. Mantener una sola VNext lógica aunque un registro enlace varias rutas. La copia física posterior sigue pendiente de matriz de versiones/dependencias; no es necesaria para implementar la lectura propuesta.

**Prioridad:** puente de lectura inicial de alto impacto esperado y riesgo Bajo; esfuerzo Medio por contraste entre repositorios y épocas. La precisión de trazabilidad de campañas en el caso tiene impacto Alto y riesgo Medio: debe concordar con la matriz de objetivos y plantilla RUN_RECORD antes de adoptarse como campo obligatorio. No se activan campañas, adopción canónica, cambios de Issue ni redistribución por publicar esta revisión.

**Prueba de compatibilidad:** los comentarios UC-21 ya usan Simplified Stage A para S5 y describen S4/CDA como posible mapping posterior, con DDS útil incluso cuando no se selecciona una especificación EA. Ese antecedente impide diseñar la consolidación como una teoría que absorba el caso o abra de nuevo S5. La campaña DDS clasifica el objeto y contrato del estudio, no los R0/R1/R2 del caso ni sus condiciones causales A–D.

La declaración de una campaña futura debe identificar: caso/versión/objetivo seleccionado, contrato y fuentes, Stage aplicable, comparadores, evidencia y retorno al resultado del caso. Un caso puede alimentar varias campañas; una campaña puede declarar varias fuentes del Challenge dentro de un scope explícito. El registro indexa, los expedientes originales gobiernan. La selección posterior de especificaciones es una decisión separada.

[UC-21 USE_CASE VNext](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/USE_CASE_VNext.md) contiene el antes/después de esta relación y [README VNext](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/README_VNext.md) el puente humano. [EP VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md) registra el orden común. Sin cambios metodológicos, nueva campaña, clasificación retrospectiva más fuerte o ejecución.
