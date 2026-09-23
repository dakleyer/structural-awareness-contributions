# Deep Corpus Audit — Structural / Ecosystem Awareness — 23 September 2026

**Repository:** `dakleyer/structural-awareness-contributions`  
**Audit head:** `a6dbafa9a5102f8ae530158b6f8076ba31870f2b`  
**Purpose:** verify that the September restructuring, coherence work and presentation passes did not reduce the Ecosystem Awareness corpus to a small reader layer or discard prior architecture, requirements, scenarios, cases, validation, FG-TIDA mappings, test design or implementation material.

> **Audit conclusion:** the substantive public corpus is still present and extensive. The current tree contains the original controlled/frozen material, integrated working successors, reference scenarios and quality plans, the canonical requirements/KPI system, current and historical benchmarks, four general validation profiles, FG-TIDA-specific cases/tests, ideal/current interface mappings, specification/charter preparation, test-design annexes, a pre-registration family, harness/trace code and lineage/conservation records. Where working documents evolved, exact earlier public blobs have now been materialized under `governance/preserved-public-snapshots/` rather than left only in Git history.

## 1. What was checked

The audit used:

- current recursive tree and directory inventories;
- comparison from pre-corpus / freeze checkpoints to current `main`;
- file history for the critical requirements/scenario/benchmark documents;
- exact blob comparison where the historical file is intended to remain unchanged;
- paragraph-level conservation checks for continuous validation files assembled from split parts;
- current Canonical Corpus Manifest and freeze/maintenance records.

Checkpoints included:

- `17a694dd` — 1 September pre-freeze FG-TIDA package checkpoint;
- `081ff3b9` — 11 September controlled-public-mirror checkpoint;
- `239ec5f5` — 17 September first integrated requirements / benchmark / scenario suite;
- `55fb4da3` — 19 September substantive EA citation anchor;
- current `main`.

From the 1 September checkpoint to current `main`, Git reports **no removed files**. From the 11 September checkpoint, the only removed paths reported are two aborted `.corpus-import` transfer chunks and the former `validation/UC-EA-01_v0.3_FROZEN.md` path; the UC-EA-01 content is present in the consolidated baseline route and its earlier exact public freeze is also preserved.

## 2. Canonical requirements system — PRESENT

Current source:

`research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md`

Current size is roughly 43 KB. Its current section structure is intact:

- Challenges **S1–S14**;
- sufficiently-good conditions **T1–T4**;
- foundational hypotheses **H1–H6**;
- KPI and falsification protocol;
- response-safety measures;
- Type-1 / Type-2 trajectory measures;
- end-to-end `S# → T# → H# → KPI` traceability;
- S14 aggregate reading;
- complete-test procedure and worked route.

The earlier working inputs also remain:

- `00A_SUFFICIENTLY_GOOD_SOLUTION_REQUIREMENTS.md`;
- `00C_FALSIFIABLE_CANDIDATE_SOLUTION_HYPOTHESES_AND_KPIS.md`.

They are preserved as provenance/non-canonical inputs, not deleted.

The first integrated 17 September requirements file has additionally been materialized byte-for-byte at:

`governance/preserved-public-snapshots/EA_REQUIREMENTS_INITIAL_INTEGRATED_2026-09-17.md`

This ensures later requirement refinements cannot erase the original integrated wording.

## 3. 00E — 100 Million Tokens scenario and quality plan — PRESENT

Current source:

`baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md`

Current size is roughly 60 KB.

The document still contains:

- the **exact five-stage source story**;
- wide exploration / Type-2 collapse;
- human escalation and bounded-capacity failure;
- alternative-generation / speculative certainty;
- structural-residual aversion;
- multiple epistemic collapse through composition;
- executive case sheet;
- four-quadrant map;
- many-to-one funnel / information-loss mechanism;
- failure reconstruction FM-I2 / FM-I1 / FM-O2 / FM-O1;
- complete cascade and arbitration;
- **Integrated Quality Plan**;
- Q0–Q5 gates;
- frozen conditions;
- deterministic gate logic;
- `scope → S# → T# → H# → KPI → disposition`;
- Route N — requirements not satisfied;
- Route Q — requirements satisfied;
- gate acceptance and recording form;
- explicit claim boundary.

Its product/implementation annexes remain:

- `00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.1.md`;
- `00E_A02_LANGGRAPH_LANGSMITH_IMPLEMENTATION_PROFILE_v0.1.md`.

The exact first integrated 17 September 00E document and both implementation profiles are additionally preserved under `governance/preserved-public-snapshots/`.

## 4. 00F — Smart-City Mobility / Mobility Chaos scenario and quality plan — PRESENT

Current source:

`baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md`

Current size is roughly 25 KB.

It still contains:

- executive case card;
- actor/local-window table;
- shared corridor decision scope;
- six-stage failure development;
- Emergency Plan A / Emergency Plan B / NORMAL / HOLD divergence;
- failure mechanism;
- **Quality-Plan Fixture**;
- gate register `challenge → sufficiency → hypothesis → KPI → disposition`;
- Q0–Q5 deterministic gate logic;
- Route N and Route Q;
- falsification conditions;
- product-annex boundary.

Its implementation profiles remain:

- `00F_A01_FIWARE_NGSI_LD_IMPLEMENTATION_PROFILE_v0.1.md`;
- `00F_A02_AWS_IOT_TWINMAKER_CORE_IMPLEMENTATION_PROFILE_v0.1.md`.

The exact first integrated 17 September 00F and both implementation profiles are also preserved as historical snapshots.

## 5. 00G — Collective False-Context / Bar-to-Napoleon scenario — PRESENT

Current source:

`baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.1.md`

This is the additional synthetic scenario for:

- correlated narrative reinforcement;
- collective false-context convergence;
- mission displacement;
- authority/admissibility confusion;
- signalling and repositioning stress.

It remains explicitly candidate / non-executed material and has not replaced 00E or 00F.

## 6. Benchmark family — PRESENT, not collapsed

The benchmark is not one small replacement file. The current tree retains the full family:

### Current canonical working benchmark

`00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md` — roughly 40 KB.

It contains:

- evidence grades E1–E4;
- comparator arms B0–B3 and fairness contract;
- industry capability baseline;
- EA-H1–EA-H4 differential hypotheses;
- canonical requirements mapping;
- required benchmark branches;
- existing-agent-benchmark analysis;
- separate 00E and 00F plausibility/evidence records;
- pre-registration;
- common outcome vector;
- result classes;
- empirical next actions;
- primary sources and provenance.

### Preserved earlier benchmark material

Also still present:

- `06_ARCHITECTURE_BENCHMARK_v0.4.part01.md`;
- `06_ARCHITECTURE_BENCHMARK_v0.4.part02.md`;
- `06_ARCHITECTURE_BENCHMARK_v0.4.part03.md`;
- `ARCHITECTURE_BENCHMARK_v0.4_PUBLIC_FREEZE.md`;
- `ARCHITECTURE_BENCHMARK_v0.5_REVIEWED_WORKING.md`;
- `07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md`;
- `00D_MARKET_AND_INDUSTRY_BENCHMARK_RESEARCH_v0.1.md`.

The 15 September benchmark split repair changed the tail wording of part 1 from “potentially differentiated” to “potentially distinctive” and removed a duplicated fragment at the start of part 2. Part 3 is byte-identical to its first publication. The historical public-freeze benchmark remains separately preserved.

The first integrated 00D v0.2 from 17 September is now also preserved exactly as:

`governance/preserved-public-snapshots/EA_BENCHMARK_00D_INITIAL_INTEGRATED_2026-09-17.md`.

## 7. Validation and case family — PRESENT and complete

The four general EA Architecture-Validation Profiles are still present:

1. `UC-EA-01_v0.3_FROZEN.md` — action-time operating-frame requalification;
2. `UC-EA-02_v0.6_MAINTENANCE_FREEZE.md` — bounded determination under incomplete evidence;
3. `UC-EA-03_v0.4_MAINTENANCE_FREEZE.md` — human oversight under bounded effective capacity;
4. `UC-EA-04_v0.5_MAINTENANCE_FREEZE.md` — scope-indexed composition of local determinations.

Also present:

- `VALIDATION_PROFILE_FAMILY_v0.5_FROZEN.md`;
- its original ordered split parts;
- every UC profile's original ordered split parts;
- `VALIDATION_PROFILE_READING_NOTE.md`;
- `USE_CASE_PORTFOLIO_REQUIREMENTS_COVERAGE_MAP_v0.1.md`.

A paragraph-level conservation check was run against all split parts for the Validation Profile Family and UC-EA-01…04. **No substantive paragraph from the split sources was missing from the continuous files.**

The portfolio coverage map further preserves the current coverage/gap model across S1–S14 and explicitly identifies unimplemented or unexecuted evidence.

## 8. FG-TIDA-specific cases and parent case — PRESENT

The general UC-EA profiles remain separate from FG-TIDA ownership.

The FG-TIDA package contains:

- `fg-tida/cases/EA_DAOS_MODEL_CASE_INTERFACE_v0.1.md`;
- `fg-tida/cases/DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md`;
- `fg-tida/tests/EA-ITP-01_v0.1_FROZEN.md`.

The parent DAOS submission remains separately preserved under:

`submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/`

including:

- Case Design / Pre-Freeze Working Structure;
- Annex I Minimal Operational Case;
- Annex II Case Extensibility;
- Annex III Challenges Exposed by the Case;
- Annex IV FG-TIDA ToR Mapping and Traceability;
- Annex V Adjacent Standards and Research Relevance;
- package README.

This means the case family is broader than “four cases”: it includes four general validation profiles, a separate interoperability test, the DAOS parent case and its annexes, two FG-TIDA-specific EA case documents, plus the 00E/00F/00G reference scenarios.

## 9. General architecture 01–04 — PRESENT

The controlled/public architecture remains:

- 01 Foundational Theory v0.4 — five parts;
- 02 Epistemic Safety Principles & Control Matrix v0.4 — three parts;
- 03 Functional Architecture v0.4 — three parts;
- 04 Functional Interfaces & Agentic Security v0.4 — three parts.

Current working successors/additions remain:

- `01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md` — about 127 KB;
- `04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md` — about 87 KB;
- topology;
- 01A through 01J interface/integration/positioning annexes.

### 01 conservation

All five v0.4 split parts remain in the repository. The v0.5 integrated reader contains the v0.4 substance; audit spot-checking found the source paragraphs preserved, with some later expanded formulations. The v0.4 sources themselves remain accessible, so expanded current text does not erase the earlier wording.

### 02 and 03 conservation

02 part 1 and 03 part 1 were explicitly repaired from the frozen Drive export on 11 September. Their current blobs equal those repaired exact public blobs. The remaining 02/03 parts checked are unchanged from their repaired/published source state.

### 04 conservation — important boundary

04 v0.4 was later amended in Git with namespace clarifications, Composition-Critical EHD material and Appendix-A interface quality/conformance work. Therefore the current v0.4 files should **not** be treated as proof of byte-identical frozen-source parity.

To guarantee conservation, the three exact later-11-September commits explicitly described as repaired frozen exports have now been materialized under:

- `FUNCTIONAL_INTERFACES_v0.4_part01_FROZEN_REPAIRED_2026-09-11.md`;
- `FUNCTIONAL_INTERFACES_v0.4_part02_FROZEN_REPAIRED_2026-09-11.md`;
- `FUNCTIONAL_INTERFACES_v0.4_part03_FROZEN_REPAIRED_2026-09-11.md`.

The current v0.5 integrated interface reader carries the programme-independent current interface architecture and the Appendix-A conformance route.

## 10. Ideal FG-TIDA architecture 05 and current-state bridge 05A — PRESENT

This structure remains explicit:

**04 General EA interface → 05 ideal FG-TIDA mapping → 05A current FG-TIDA mapping**

### 05 ideal

Present under both historical baseline and current FG-TIDA route:

- `05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md`;
- part 2;
- part 3.

The three historical baseline 05 parts were compared against the 11 September checkpoint and are **byte-identical** there. Nothing from the ideal 05 contract was deleted.

### 05A current state

Present as:

`fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md`

The baseline and FG-TIDA copies have the same substantive bridge; blob differences come from rebased links and routing to the current general-interface successor.

The FG-TIDA interface README still states the rule explicitly:

**general EA interface → ideal FG-TIDA mapping → current FG-TIDA mapping**.

## 11. Specification / charter preparation — PRESENT

The FG-TIDA application package still includes the extensive specification-preparation line:

`fg-tida/specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.2_DRAFT.md` — roughly 47 KB.

It contains:

- candidate specification identity;
- scope/non-goals;
- integrated/two-document/three-document options;
- source-to-specification map;
- normative maturity N1/N2/E/I/T/H;
- normative drafting and requirement-ID rules;
- S1–S14 projection;
- T1–T4 projection;
- EHD boundary;
- interface maturity register;
- versioning/compatibility/profile evolution;
- conformance architecture and ICR;
- use cases/examples;
- standards duplication review;
- security/privacy/governance;
- candidate outline;
- editorial governance;
- template readiness;
- draft lifecycle;
- open decisions;
- Gates A–F;
- backlog and audit disposition.

The earlier v0.1 and v0.2 baseline annex copies remain preserved. The Theme #13 Working Group / Phase-2 charter preparation draft also remains present.

## 12. Test design, testbed progression, harness and pre-registration — PRESENT

The implementation/test line is extensive and remains intact:

### 00D-A01 — test/oracle construction

`00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md` — roughly 35 KB.

Contains:

- fixture admission;
- bounded deterministic oracle;
- GEEW/EA/oracle role separation;
- determinism/stipulation/residual;
- controlled circularity;
- fixture record;
- traceability matrix;
- gate policy / falsification;
- deterministic fixture construction;
- Stage 0–2 testbed progression;
- implementation/preservation plan.

The historical detailed “Proof Sketch” version has not been discarded; it is preserved exactly in `governance/preserved-public-snapshots/EA_00D_A01_PROOF_SKETCH_2026-09-19.md`. The current old filename is only an alias to avoid overstating the evidence class.

### 00D-A02 — execution / alignment change record

Present and enacted, preserving the pre-execution plan and alignment decisions.

### 00D-A03 — deterministic harness design

`00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md` — roughly 17 KB.

Contains:

- bounded claim/source anchors;
- fixture family P1/P2/C0;
- deterministic oracle;
- minimal harness architecture;
- comparator/fairness contract;
- measures/gates/falsification;
- qualifier-loss instrumentation self-test;
- Canonical Trace v1 determinism self-test;
- execution sequence.

### Fixture family

`baseline/fixtures/RS-00E-Q1a/` currently contains:

- operative README;
- pre-registration v0.1;
- v0.2;
- v0.3;
- v0.4;
- **v0.5 operative pre-registration**;
- `canonical_trace_v1.py`;
- `test_canonical_trace_v1.py`.

The current status is correctly **pre-execution**: the harness/trace infrastructure and pre-registration exist, but no Stage-0 execution trace is claimed as completed.

## 13. Lineage and conservation — PRESENT

The baseline still contains the lineage set rather than collapsing it into current architecture:

- Architectural Principles;
- Three Dimensions of Indeterminacy (4 parts);
- Deep Conceptual Lineage / Derivation Map;
- Prompt-to-Canon Conservation Matrix (3 parts);
- APQ Corpus Change Record (2 parts);
- Articles 01–05 (including split parts where applicable).

The baseline inventory contains 19 lineage/conservation files under these families.

## 14. What actually remains incomplete

The corpus is **not missing its intellectual content**. The current open items are mainly publication/control verification:

1. intended single-file canonical paths for the six controlled v0.4 baseline documents;
2. controlled Drive revision ↔ public Git SHA-256 parity inventory;
3. explicit disposition of a small number of compatibility duplicates;
4. Stage-0 execution itself;
5. later Stage-1 / independent validation;
6. release/Zenodo DOI if/when external tooling is available.

Those are not the same as “the corpus was reduced.”

## 15. Strong conservation result

After this audit, the following historical wording is no longer dependent on Git-history navigation alone:

- 11 September root/router/manifest states;
- repaired frozen 04 source anchors;
- 17 September initial integrated requirements / benchmark / 00E / 00F / four implementation profiles;
- 19 September root/router/baseline/manifest/topology and detailed 00D-A01 Proof-Sketch state.

See:

`governance/preserved-public-snapshots/README.md`

## 16. Final determination

**No evidence was found that the September presentation/coherence passes reduced the EA corpus to a few summary documents.**

The major bodies remembered by the maintainer are all present:

- requirements;
- 100M Tokens;
- Mobility Chaos;
- their quality plans;
- benchmark;
- four validation profiles and related cases/tests;
- 01–04 architecture;
- 04 v0.5 integrated interface architecture;
- 05 ideal FG-TIDA interfaces;
- 05A current-state FG-TIDA bridge;
- specification and charter preparation;
- test design;
- coverage plan;
- deterministic harness design;
- pre-registration and canonical trace code;
- lineage and governance.

The honest remaining limitation is **verification of exact controlled Drive revisions**, not loss of the public corpus content.
