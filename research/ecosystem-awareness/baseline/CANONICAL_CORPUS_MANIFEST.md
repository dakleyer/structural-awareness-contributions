# Ecosystem Awareness — Canonical Corpus Manifest

**Public mirror status:** single-folder location consolidated 15 September 2026; intended continuous-source filenames and controlled revision/SHA-256 verification still pending  
**Controlled architecture/validation freeze:** 2026-09-10  
**Repository:** `dakleyer/structural-awareness-contributions`  
**Parent path:** `research/ecosystem-awareness/`  
**General canonical corpus folder:** `research/ecosystem-awareness/baseline/`  
**FG-TIDA application package:** `research/ecosystem-awareness/fg-tida/`

This manifest maps the general public reading corpus to the exact controlled Google Drive corpus. On 21 September 2026, FG-TIDA-specific application material was separated into `research/ecosystem-awareness/fg-tida/` so Theme-number mappings, charter/specification preparation, FG-TIDA-specific cases/tests and provenance cannot be mistaken for the programme-independent EA architecture. **Location consolidation on 15 September 2026** relocated the previously separate validation, lineage, governance and provenance Markdown into `baseline/`; the former blob paths remain recoverable in Git history at commit `bbd3ed275309e4087cbe06b654472e31c3cd186f`. Relative Markdown links were mechanically rebased for navigation. Thus relocated blobs are **not byte-identical** to the former public blobs, even where research prose is unchanged; controlled Drive-revision/SHA parity remains unverified. Until every file listed below exists at the stated public path and passes the corresponding SHA-256 check, the public repository must be treated as an **incomplete mirror** of the controlled corpus.

## A. Canonical / release baseline — publication status

The [`baseline/README.md`](./README.md) supplies the ordered reader index for the general EA architecture and validation corpus. The separate [`fg-tida/README.md`](../fg-tida/README.md) supplies the FG-TIDA application route. The original controlled v0.4 release baseline historically contained six documents, including the FG-TIDA-oriented document 05; current reader navigation now treats 05 as an FG-TIDA application source rather than part of the general canonical interface layer.

The controlled baseline is complete in Google Drive. All six are now publicly present as ordered split parts; the six intended single-file canonical paths and checksum inventory remain pending. A word-level comparison on 15 September 2026 found parity across the six after repair of a benchmark split artifact; this is not byte-level or revision-anchored verification.

| # | Intended public file | Controlled Drive source | Public status |
|---|---|---|---|
| 1 | `baseline/01_FOUNDATIONAL_THEORY_v0.4.md` | `1LxqqoNOO6R9_7kcp6KqaVQ2crIKRzucKWejtivKB8uk` | All ordered split parts present; canonical single-file path / SHA check pending |
| 2 | `baseline/02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.md` | `1IZKJJZr3_CDyPng789faWfpawWRgzwzMZvg_EkLdkbs` | All ordered split parts present; canonical single-file path / SHA check pending |
| 3 | `baseline/03_FUNCTIONAL_ARCHITECTURE_v0.4.md` | `1lfF9p1acEYzGNGLr5KJxv3tH7XJu9X2J5lPJApK8Jmc` | All ordered split parts present; canonical single-file path / SHA check pending |
| 4 | `baseline/04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.md` | `1yqMqaurnlGgN2x-JDJ6AgXtRGus1MMXcVKTPg7cR5_I` | Controlled v0.4 split source preserved; current general reader successor is `baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md`; SHA check of controlled source remains pending |
| 5 | `baseline/05_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.md` | `1kSMeygAUe8JaM5MHTnT6DMvhiwVM8sWV1-Bc6A1H7-E` | Controlled historical source preserved; current FG-TIDA application route is `../fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md` (+ parts 2–3); SHA check of controlled source remains pending |
| 6 | `baseline/06_ARCHITECTURE_BENCHMARK_v0.4.md` | `1ZYVI6Co5kMoH-0rhVVChYvrACJaGjARl4qX1TD3iAf8` | All three ordered split parts present and transfer residue repaired 15 September 2026; canonical single-file path / SHA check pending; separate historical public-freeze copy is preserved in the consolidated folder |

## A.0 Current integrated working foundation successor (outside the controlled release baseline)

- [`baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md`](./01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) — published 15 September 2026 as the current single-file **working successor of document 01**. It reorganizes and retains the full prose of v0.4 §§1–18, once each, under the two related foundational origins and their integration; includes the new 01A §§1.1–1.3, reader dictionary and provenance register. The five v0.4 split parts and 01A source note remain intact and independently accessible. This successor is **not** a controlled Google Drive freeze/revision anchor, an extra seventh frozen baseline document, completed validation or proof of exact parity with the pinned v0.4 revision. It does not close the incomplete-mirror/SHA verification issue.

## A.0a Current integrated general-interface successor

- [`baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md`](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) — current programme-independent interface reader. It preserves the general O/S/EHD semantics of the controlled v0.4 source while removing FG-TIDA Theme-number mappings from the canonical interface layer. Those mappings are maintained separately in the [FG-TIDA interface package](../fg-tida/interfaces/README.md). The controlled v0.4 split files remain preserved as historical source/provenance and are not silently rewritten.

## A.1 Newly authored working foundation companion (outside the controlled release baseline)

- `baseline/01A_FOUNDATIONAL_DUAL_ORIGIN_NOTE_v0.1.md` — present as a public, additive working note. It separates residual indeterminacy, ecosystem change and their integration, with conservation links to the unchanged v0.4 parts and the already published Theme #13 comment. Its substantive development is now incorporated into the current working 01 v0.5 successor; this separate 01A file remains preserved as source history. It is **not** one of the six controlled/frozen baseline documents, does not have a Google Drive freeze ID/revision anchor, and does not make the incomplete public mirror complete.

## A.2 Newly authored EA/MSCA working interface annex (outside the controlled release baseline)

- `baseline/01B_EA_MSCA_INTERFACE_ANNEX_v0.2.md` — current public additive EA↔MSCA interface successor. It preserves the v0.1 source-profile mapping while adding the current S/E/C/P/M representation/assessment boundary, sparse/UNASSESSED state, ACC/signalling/authority separation, compatibility-qualified inputs, extensibility boundary and pending Control Positioning limit. It is **not** a seventh/eighth frozen baseline document, implemented interprogramme API, completed validation, canonical MSCA Architecture/Operation, or controlled Google Drive freeze/revision anchor. `01B_EA_MSCA_INTERFACE_ANNEX_v0.1.md` remains preserved provenance.

## A.3 Newly authored EA/Regime Awareness working interface annex (outside the controlled release baseline)

- `baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md` — current additive EA↔Regime Awareness interface successor. It preserves the public minimal-detector boundary and v0.1 source contracts while adding the broader qualified A/B/C/D regime-position and directional-confidence delta projection used by EA/MSCA positioning. It is **not** an extra frozen baseline document, implemented common API, independent empirical validation or claim that the broader gradient semantics are published results of the minimal-detector paper. `01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.1.md` remains preserved provenance.

## A.4 Independently reviewed joint EA/MSCA/RA operation profile (outside the controlled release baseline)

- `baseline/01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md` — additive candidate composition profile, published 15 September 2026 after independent architecture review. It binds operation, S/Q, RA Ψ/context/posture/action-safety, MSCA S/E/C/P/M, authority/permit and useful cost/response horizon; distinguishes required RA-triggered action from optional advisory RA evidence; and proposes falsification tests. It is **not** a seventh frozen baseline document, an implemented joint gate, a safety proof, a completed pilot or an adopted standard. The controlled v0.4 baseline remains unchanged.

## A.4b Additive distributed-positioning and governance annexes (outside the controlled release baseline)

- `baseline/01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md` — additive working annex published 21 September 2026. It reconciles existing individual-adaptation, signalling-without-required-cooperation, Semantic Window, EHD, APQ/F9 and EA↔MSCA mechanisms into an explicit participant-local distributed reading; distinguishes Decision-Scoped Epistemic Opportunity from mathematical-gradient claims; and preserves no-supercontroller, no-consensus and source-ownership boundaries. It is **not** a new frozen baseline document, implemented protocol, convergence result, standards adoption or proof of benefit.
- `baseline/01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md` — additive neighbouring governance/participation annex published 21 September 2026. It defines a candidate human-governed participation profile for membership, roles, permissions/obligations/prohibitions, hard constraints, versioning, revocation/exit and their interfaces with EA/authority/MSCA while explicitly preserving normative-MAS/electronic-institution prior art. It is **not** part of the EA core, a grant of legal personhood, a legal contract, an implemented governance protocol, an adopted standard or a replacement of external policy/authority owners.
- `baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_DISTRIBUTED_OPPORTUNITY_v0.1.md` — additive signalling annex published 23 September 2026. It formalizes selective participant-local disclosure, the EHD-carried projection of epistemic state/MSCA/ACC/authority references, local opportunity-gradient interpretation, ACC admissibility gating and authority verification under choreography rather than orchestration. It defines no mandatory wire protocol, common ecosystem ACC/MSCA, common trust root, consensus mechanism or global gradient service.
- `baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md` — additive working signalling annex published 23 September 2026. It defines selective participant-local signal projections across epistemic state, MSCA, ACC and authority/delegation; keeps signalling optional unless an applicable profile requires disclosure; couples received signals to participant-local opportunity ordering and choreography; and introduces a falsifiable false-context / mission-displacement reference scenario with matched S0–S3 comparison. It is **not** a mandatory signalling protocol, common ecosystem contract, common MSCA, global gradient, convergence result, completed experiment or standards adoption.

**Historic source-status boundary:** the original `baseline/05_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md` source is retained as historical controlled provenance. The current reader copy is [FG-TIDA 05 ideal](../fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md). Public availability does not imply FG-TIDA adoption or a new source-status determination.

## A.4a Current FG-TIDA interface and conformance bridge (outside the controlled release baseline)

- [`fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md`](../fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md) — additive public working companion to the 05 ideal FG-TIDA projection. It fixes a dated public-source snapshot and distinguishes current Theme-owned state, candidate cross-Theme fields and test-only conformance evidence; it applies the 04 Appendix A ICR discipline to bounded UC #4 adapter/fixture routes. It is not a modification of 05, an adopted FG-TIDA contract, a common wire schema, completed interoperability validation or a new control layer.

## A.5 Canonical universal test document and canonical working benchmark (outside the controlled release baseline)

- [`baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md`](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) — the sole canonical requirements document in the current reader route: complete S1–S14 challenge taxonomy, T1–T4 sufficiently-good conditions, foundational H1–H6 and their KPI/falsification protocol. It is not an EA differential or a market result.
- [`baseline/00A_SUFFICIENTLY_GOOD_SOLUTION_REQUIREMENTS.md`](./00A_SUFFICIENTLY_GOOD_SOLUTION_REQUIREMENTS.md) and [`baseline/00C_FALSIFIABLE_CANDIDATE_SOLUTION_HYPOTHESES_AND_KPIS.md`](./00C_FALSIFIABLE_CANDIDATE_SOLUTION_HYPOTHESES_AND_KPIS.md) — unchanged preserved working inputs, recorded as [non-canonical](./non-canonical/README.md). They remain available for provenance and existing cross-references but are not canonical reader-entry documents.
- [`baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md`](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) — the sole current benchmark in the canonical reader route. It integrates EA-H1…EA-H4, B0–B3 matched comparison, the industry/agent benchmark landscape and primary-source corroboration—with explicit limits—of the 00E/00F reference-scenario mechanisms. It is **not** an extra frozen baseline document, a completed comparison, proof of novelty, independent replication or standards adoption.
- [`baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md`](./00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md) — additive working annex to 00D. It provides the requirements-first scenario-fixture traceability matrix, fixture-record fields, bounded deterministic reference-oracle model, residual and regime-change dependency limits, falsification/negative-control rules and Stage 0–2 testbed progression. It makes a possible circularity inspectable; it is **not** a new canonical benchmark, a completed fixture/testbed, independent validation or claim of EA effectiveness.
- [`baseline/07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md`](./07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md) and [`baseline/00D_MARKET_AND_INDUSTRY_BENCHMARK_RESEARCH_v0.1.md`](./00D_MARKET_AND_INDUSTRY_BENCHMARK_RESEARCH_v0.1.md) — preserved non-canonical predecessors of the integrated benchmark. The earlier top-level `ARCHITECTURE_BENCHMARK_v0.5_REVIEWED_WORKING.md`, `ARCHITECTURE_BENCHMARK_v0.4_PUBLIC_FREEZE.md` and controlled `baseline/06_ARCHITECTURE_BENCHMARK_v0.4` source/split also remain preserved.

## A.6 FG-TIDA-specific EA/DAOS model-case interface annex (outside the controlled release baseline)

- [`fg-tida/cases/EA_DAOS_MODEL_CASE_INTERFACE_v0.1.md`](../fg-tida/cases/EA_DAOS_MODEL_CASE_INTERFACE_v0.1.md) — current public candidate interface between the intact TIDA — Delegated Authority OS under Context Change parent case and EA F1–F9. It states T0–T2 source-fact inputs, bounded EA outputs, CH-S1…14 ownership, four validation lenses, extension invariants and fair-test conditions. The detailed [`fg-tida/cases/DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md`](../fg-tida/cases/DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md) remains the FG-TIDA-specific reader/test guide, not an additional parent-case freeze. This annex does **not** rename or edit the parent submission, add an implemented API, certify interoperability, or turn UC-EA-01…04 into four FG-TIDA submissions.

## A.7 Reference failure scenarios and implementation profiles (outside the controlled release baseline)

- [`baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md`](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) — technology-neutral enterprise reference failure scenario and integrated quality plan. Its two current product profiles apply the frozen case to [Microsoft Agent 365](./00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.1.md) and [LangGraph/LangSmith](./00E_A02_LANGGRAPH_LANGSMITH_IMPLEMENTATION_PROFILE_v0.1.md).
- [`baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md`](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md) — technology-neutral smart-city mobility reference failure scenario in which residual uncertainty leads locally understandable Emergency Plan A, Emergency Plan B, NORMAL and HOLD postures to compete for one corridor; Q0–Q5 test whether their incompatibility is detected, bounded and requalified in time. Its two product profiles apply the frozen scenario to [FIWARE NGSI-LD / Orion-LD](./00F_A01_FIWARE_NGSI_LD_IMPLEMENTATION_PROFILE_v0.1.md) and [AWS IoT TwinMaker / IoT Core](./00F_A02_AWS_IOT_TWINMAKER_CORE_IMPLEMENTATION_PROFILE_v0.1.md), comparing standard, top and top-plus-EA implementations under gradual or initially unknown regime pivots.
- [`baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.1.md`](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.1.md) — synthetic technology-neutral reference scenario ("Bar-to-Napoleon" cascade) for collective false-context convergence, correlated narrative reinforcement, mission displacement, authority spoofing and admissibility confusion. It defines B0–B3 matched test arms and falsifiers for qualified signalling; it is a candidate test plan, not an executed result, real incident report or claim that EA prevents hallucination or catastrophic forgetting.

These are public working cases, not additional frozen baseline documents, real incident reports, product certifications, benchmark results or completed validations. Their product profiles do not rank the named technologies; they test implementation-dependent mitigation and the remaining regime-change boundary under fixed resources and deadlines.

## A.8 Use-case portfolio requirements-coverage map (outside the controlled release baseline)

- [`baseline/USE_CASE_PORTFOLIO_REQUIREMENTS_COVERAGE_MAP_v0.1.md`](./USE_CASE_PORTFOLIO_REQUIREMENTS_COVERAGE_MAP_v0.1.md) — additive public working annex that starts from the canonical S1–S14 / T1–T4 / H1–H6 / KPI route and maps coverage by UC-EA-01…04, the separately maintained FG-TIDA-specific EA-ITP-01 test, and 00E/00F. It distinguishes direct EA validation from external-owner boundary coverage and identifies the next requirements-first validation workbook. It does not modify the controlled requirements document, the frozen validation profiles, the Parent Case Study, 04, 05 or 05A; it is not a completed-validation claim.

## A.9 Stage-0 execution and coverage-alignment change record (outside the controlled release baseline)

- [`baseline/00D_A02_STAGE_0_EXECUTION_AND_COVERAGE_ALIGNMENT_CHANGE_PLAN_v0.1.md`](./00D_A02_STAGE_0_EXECUTION_AND_COVERAGE_ALIGNMENT_CHANGE_PLAN_v0.1.md) — dated public record of the enacted changes to 00D-A01, the coverage map and the S14 reading. It preserves the frozen scenarios and architecture, does not report an executed fixture or EA result, and is limited to the public Contributions corpus.

## A.10 Open public maintenance items (outside the controlled release baseline)

| Item | Owner | Review date | Status boundary |
| --- | --- | --- | --- |
| Product-implementation profile source-basis review | EA corpus maintainer | 18 December 2026 | Record for each material product assertion whether it derives from dated public documentation, deployment configuration or inference. This is not a product benchmark, certification or execution result. |

## B. Current validation set — publication status

These validation artifacts are part of the canonical corpus. They are not unpublished comments and must not be omitted. On 15 September 2026 the five previously split validation documents were materialized as continuous public files at the intended paths; their ordered parts remain preserved. This resolves reader visibility and midword part boundaries, **not** the revision-anchored SHA-256 inventory.

| Intended public file | Status | Controlled Drive source | Public status |
|---|---|---|---|
| `baseline/VALIDATION_PROFILE_FAMILY_v0.5_FROZEN.md` | Frozen / unchanged | `1qjCLvOp02Lgh9hVlJae_GZTNImenMXboEJ3fJMsqmok` | Continuous file and ordered split parts present; controlled revision / SHA check pending |
| `baseline/UC-EA-01_v0.3_FROZEN.md` | Frozen / unchanged | `19k4fY-zu3IoRmsSuUyS0xgjqX7NhvvgoTAeZLN3ijI8` | Continuous validation-path file and ordered split parts now present; earlier public alias preserved in the consolidated folder; controlled revision / SHA check pending |
| `baseline/UC-EA-02_v0.6_MAINTENANCE_FREEZE.md` | Current maintenance successor | `1_a1edMjJx4ozTmMn9iT23j7zYjOcX7Fmln8Zn_Tf8Qw` | Continuous file and ordered split parts present; controlled revision / SHA check pending |
| `baseline/UC-EA-03_v0.4_MAINTENANCE_FREEZE.md` | Current maintenance successor | `1Mhv4mUIU-S5yifmH8G0UDRdf0ItXt1aEK4kn0kAG6uY` | Continuous file and ordered split parts present; controlled revision / SHA check pending |
| `baseline/UC-EA-04_v0.5_MAINTENANCE_FREEZE.md` | Current maintenance successor | `1y8wRR89mAYSgkYvsMS2ljr7V5jV1P2My1fIkonGkv1Y` | Continuous file and ordered split parts present; controlled revision / SHA check pending |
| `fg-tida/tests/EA-ITP-01_v0.1_FROZEN.md` | Frozen / unchanged | `1OnBzCX0TP6mtxdLjn9_OORq0UIOdl9I_3vkVsmRW1XA` | FG-TIDA-specific interoperability test; separated from the four general EA validation profiles; SHA check pending |

**Reader guide:** `baseline/VALIDATION_PROFILE_READING_NOTE.md` is the general validation reader. The FG-TIDA-specific [`fg-tida/cases/DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md`](../fg-tida/cases/DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md) traces the parent TIDA — Delegated Authority OS under Context Change case and its relationship to the four Architecture-Validation Profiles. The four UC-EA profiles remain general EA validation artifacts, not adopted FG-TIDA submissions.

## C. Governance controls — publication status

- `baseline/FREEZE_MANIFEST_2026-09-10.md` — present.
- `baseline/MAINTENANCE_FREEZE_MANIFEST_2026-09-10.md` — present.
- `baseline/MAINTENANCE_FREEZE_README_2026-09-10.md` — present.

## D. Preserved lineage / conservation — publication status

These materials preserve the path from problem definition and derivation into the current baseline. They do not override the current baseline.

- `baseline/ARCHITECTURAL_PRINCIPLES_v0.1.md` — present.
- `baseline/THREE_DIMENSIONS_OF_INDETERMINACY_WORKING_TECHNICAL_ARCHITECTURE.md` — present as single file or ordered split parts; canonical filename / SHA check pending.
- `baseline/DEEP_CONCEPTUAL_LINEAGE_DERIVATION_MAP_v0.1.md` — present as single file or ordered split parts; canonical filename / SHA check pending.
- `baseline/PROMPT_TO_CANON_CONSERVATION_MATRIX_v0.1.md` — present as single file or ordered split parts; canonical filename / SHA check pending.
- `baseline/CORPUS_CHANGE_RECORD_APQ_CONSERVATION_v0.1.md` — present as single file or ordered split parts; canonical filename / SHA check pending.
- `baseline/ARTICLE_01_NATURALISTIC_FOUNDATIONS_AND_AGENTIC_LIFECYCLE_INVERSION.md` — present as single file or ordered split parts; canonical filename / SHA check pending.
- `baseline/ARTICLE_02_MINIMUM_CONTROL_ARCHITECTURE_MULTI_OPTIMA.md` — present as single file or ordered split parts; canonical filename / SHA check pending.
- `baseline/ARTICLE_03_SEMANTIC_WINDOW_AND_GOOD_ENOUGH_EARLY_WARNING.md` — present as single file or ordered split parts; canonical filename / SHA check pending.
- `baseline/ARTICLE_04_ECOSYSTEM_SIGNALLING_WITHOUT_REQUIRED_COOPERATION.md` — present as single file or ordered split parts; canonical filename / SHA check pending.
- `baseline/ARTICLE_05_INTEGRATED_REFERENCE_MODEL_FOR_FG_TIDA.md` — present as single file or ordered split parts; canonical filename / SHA check pending.

## E. Parent case and public provenance

- Parent Case Study / DAOS fixture: publicly available elsewhere in this same repository under the ITU-T FG-TIDA submission tree and linked from the corpus README; it is not duplicated here unless a later preservation need requires it.
- FG-TIDA-specific provenance is now maintained under [`fg-tida/provenance/`](../fg-tida/provenance/README.md), including the public-footprint record and public-provenance record. Historical baseline copies remain recoverable for source conservation; controlled SHA parity remains pending.

## F. Publication boundary

The **general canonical corpus** is intended to include the complete programme-independent architecture, general interfaces, benchmark, lineage, Articles 01–05, validation family, UC-EA-01…04, freeze/maintenance controls and conservation material. The **FG-TIDA application package** separately contains charter/specification preparation, 05/05A Theme mappings, FG-TIDA-specific DAOS case material, EA-ITP-01 and FG-TIDA provenance. The linked Parent Case Study remains in the submissions tree.

The only deliberate exclusion is **unpublished GitHub/FG-TIDA comment, reply or posting-draft material** prepared for future public threads. Those drafts remain private until actually posted. Once posted, the public artifact may be cited as baseline/evidence, but the private drafting file does not become canon automatically.

## G. Verification route

The corpus must not be described as complete until all three conditions are true:

1. Every intended canonical public file exists at the path named in this manifest.
2. The generated SHA-256 inventory exists and verifies every canonical file.
3. No truncated split artifact, aborted transfer residue or historical alias inside the consolidated folder can be mistaken for the current canonical file.

The previously advertised verification bundle/inventory is not yet present and therefore must not be cited as completed verification.

**Revision-anchor exception:** the current Google Docs revisionId for controlled baseline document 02 (Epistemic Safety Principles & Control Matrix) differs from the revisionId fixed in `baseline/FREEZE_MANIFEST_2026-09-10.md`. A word-level comparison of the *current* Doc 02 against its GitHub split found no missing words, but does **not** certify that the public file matches the exact frozen revision. No substantive change has been established from the revision-token difference alone; the pinned revision still requires direct verification. Presence of ordered parts is not proof of equality. The 15 September 2026 text comparison used normalized word sequences, not frozen-revision SHA-256, and found link/format additions in some validation mirrors; these require explicit disposition before any completeness claim.

## Status boundary

This corpus is public research / pre-standardization material. It is not an ITU-T deliverable, adopted FG-TIDA architecture, NIST submission, product certification, or proof of novelty/superiority. Public FG-TIDA references document contributor-level provenance and third-party discussion only.
