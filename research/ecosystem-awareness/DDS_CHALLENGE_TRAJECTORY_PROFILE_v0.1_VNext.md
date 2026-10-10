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
8. **No-zombie check:** once a proposed change is incorporated, remove it from this VNext; Git history is the archive.

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
