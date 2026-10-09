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
