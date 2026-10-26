# Deployment Differential Study (DDS) — Canonical Method Index v0.1

**Status:** canonical working method router for the Ecosystem Awareness research corpus; not an adopted standard, certification scheme, assurance opinion or claim of product superiority.  
**Date:** 7 October 2026.  
**Terminology revision:** 0.1.1 — Stage A/B/C; definitions and evidence unchanged.  
**Method identity:** one DDS method, three substantive development stages.  
**Stage A source:** [DDS Stage A — Specification Discovery / Challenge–Trajectory Profile v0.1](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md)  
**Stage B source:** [DDS Stage B — Architecture Verification v0.1](./DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md)  
**Stage C source:** [DDS Stage C — Implementation / Problem Validation v0.1](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md)  
**Research basis:** [DDS research basis, benchmarking and value proposition](./DDS_RESEARCH_BASIS_AND_BENCHMARKING_2026-10-06.md)

The stage names are **DDS Stage A**, **DDS Stage B** and **DDS Stage C**. Existing `DDS_GATE_B_...` and `DDS_GATE_C_...` filenames are retained as stable link targets; their current titles and content use Stage. Frozen records retain the terminology used at registration/execution.

## 1. One method, three stages

DDS is the single substantive testing/evaluation method used by this corpus. The stages are distinguished by the **object under test** and by the **authoritative reference used to adjudicate it**.

| DDS stage | Object under test | Authoritative reference | Primary output |
|---|---|---|---|
| **Stage A — Specification Discovery** | Candidate specification, mechanism, control profile or technology/configuration trajectory | Frozen Challenge, scenario/reduction, strong peers, falsifiers and acceptance rule | Versioned candidate specification package / bounded differential finding |
| **Stage B — Architecture Verification** | Candidate architecture or reference realization intended to implement the Stage A specification | Frozen Stage A specification package and its requirement/behavior contract | Versioned verified/partially verified/nonconformant architecture package |
| **Stage C — Implementation / Problem Validation** | Pinned executable implementation/configuration | Originating Challenge plus independently observed execution/effect/target state | Bounded empirical implementation/problem-validation finding |

The default maturation path is:

~~~text
Challenge
   ↓
DDS Stage A — discover / select the specification
   ↓
Stage A specification package
   ↓
DDS Stage B — verify architecture realization
   ↓
Stage B architecture package
   ↓
DDS Stage C — validate implementation against the problem
~~~

A pre-existing architecture or product does not need to have been designed by DDS. It may enter Stage B through an explicit mapping to a frozen Stage A package and may enter Stage C only after the applicable lineage, registration and evidence conditions are declared.

## 2. Evidence mode is orthogonal to stage identity

Documentary, analytical, mathematical, virtual, symbolic, deterministic-fixture, controlled-harness, native-execution, matched-campaign and independently replicated evidence are **evidence modes**, not DDS stages.

Examples:

- executable Python over an abstract specification can still be **Stage A**;
- a formal or deterministic reference model can be **Stage B** if the object under test is the architecture realization against the frozen specification;
- **Stage C** requires a claim about a pinned implementation/configuration against the Challenge and observed effects, even if the environment is still a bounded sandbox.

No evidence mode silently promotes a result from one stage to another.

## 3. Full and Simplified DDS stage profiles

A profile may deliberately exercise only a bounded subset of one stage.

Use:

- **DDS Stage A/B/C profile** when the declared stage question and required surfaces are covered for the stated scope;
- **Simplified DDS Stage A/B/C profile** when selected stage surfaces are intentionally collapsed, unscored or out of scope.

“Simplified” is a coverage statement, not a quality judgment. The profile must identify what is omitted and may not inherit claims from the omitted surfaces.

## 4. Support artefacts are not competing test methods

The following retain their source-native semantics and ownership but serve DDS rather than define parallel corpus-wide methods:

- **DBC — Decision Boundary Challenge:** reusable Challenge/adjudication vocabulary, boundary questions, dispositions and case families;
- **00D:** comparator/fairness and matched-resource contract;
- **R01 oracle / C02:** test-infrastructure qualification and reference/harness machinery;
- **C11:** result-producing campaign registration, resource, comparator and analysis freeze;
- **T03:** admitted real-technology adapter/execution route;
- **UC-4:** external testbed/interoperability envelope with its own Stage-0/Stage-1 vocabulary;
- **CTv1, tool broker, isolation and sidecar contracts:** reusable evidence/instrument infrastructure.

A support artefact may be used by more than one DDS stage.

## 5. Namespace rule

To prevent collision with existing scenario terminology:

- **DDS Stage A / B / C** means only the three development stages in this index.
- **trajectory gate** means a local decision/validation boundary inside a Challenge, including Q0–Q6 or equivalent local gates.
- **gate policy** means a profile-specific acceptance/verification policy; it is not a DDS Stage.
- **Stage-0 / Stage-1** retain the meaning assigned by the source testbed that owns them.
- **C02 / C11 / T03** retain their R01 lifecycle/delivery meaning.

## 6. Claim propagation rule

No stage result automatically proves a later stage.

- Stage A does not establish that an architecture realizes the selected specification.
- Stage B does not establish that the realized architecture solves the Challenge in execution.
- Stage C does not establish universal product safety, unrestricted transfer, certification or standards adoption.

A failure may diagnose a problem at the current stage or justify opening a successor of an earlier stage, but the failed record is preserved.

## 7. Historical and pre-DDS evidence incorporation

DDS was introduced after several bounded fixture, oracle, harness and benchmark artefacts already existed. Those artefacts are **not abandoned and are not parallel testing methods**. They are incorporated into DDS according to the object they tested and the evidence they actually produced.

This incorporation is classificatory and preservational:

- historical versions, commits, pre-registrations, freezes, traces and results remain authoritative for their own recorded runs;
- an artefact version such as `v0.4`, `v0.5` or an oracle freeze such as `v0.9` is the version of **that artefact**, not a DDS method version and not a later/higher DDS Stage;
- incorporation into DDS does not retroactively strengthen a result, make a descriptive fixture comparative, or convert instrumentation evidence into product validation;
- the applicable DDS Stage is determined by the **object under test**, not by whether Python, a harness or an executable fixture was used.

Current legacy incorporation map:

| Historical / pre-split artefact family | Original role and evidence | Current DDS reading |
|---|---|---|
| **00D-A01 bounded oracle / test construction** | Test-design discipline for frozen facts, oracle and controls | DDS support infrastructure usable by Stage A/B/C as applicable; not a substantive Stage result by itself |
| **00D-A03 RS-00E-Q1a Stage-0 harness design** | One deterministic harness design for one fixture family | DDS test-infrastructure design supporting a bounded Simplified Stage A execution; not Stage B/C |
| **RS-00E-Q1a v0.5 / Stage-0 execution** | Descriptive deterministic fixture run; B1/B3 tie; no independent reviewer | Historical **Simplified DDS Stage A deterministic evidence** for its bounded specification/trajectory question; Stage-0 remains the source testbed maturity label |
| **00L paper/symbolic traversals and correction runs** | Analytical/symbolic paired controls and regression evidence | Simplified DDS Stage A analytical/symbolic evidence within each declared scope |
| **R01 C02 oracle/harness, freezes v0.3–v0.9** | Instrument qualification, blinding, replay, resource and reference controls | Shared DDS **test-infrastructure qualification**; not itself Stage A/B/C substantive evidence |
| **00D v0.2 / v0.3 benchmark work** | Strong-peer, matched-resource and comparison discipline | DDS comparator/fairness support, primarily for Stage A and Stage C; not a second method |
| **DBC** | Decision-boundary challenge/adjudication vocabulary | Cross-stage DDS support module; not a second method |

Where an older record says “Stage-0”, “benchmark”, “oracle”, “harness”, “testbed” or another historical local term, preserve that term for the source record and use this index to understand its current DDS role.

## 8. Current DDS profile and support registry

This is the authoritative **cross-stage classification registry** for current DDS-related artefacts. It is a reading/classification aid only: it does not modify a cited artefact, transfer evidence across versions or promote historical results.

| Current artefact / family | Current DDS role / Stage | Coverage / reading | Cost | Risk | Effectiveness / I-vs-M | Acceptance | BV projection | Evidence state |
|---|---|---|---:|---:|---:|---|---|---|
| 00E–00J positive/negative technology trajectories and current product profiles | **Stage A — Simplified** | Challenge + technology/configuration mapping + trajectory/quality stages + positive/negative routes | generally unscored | primary / branch-specific | generally collapsed into legitimate continuity / expected outcome | binary / trajectory-stage based | not part of frozen route | documentary / symbolic / fixture-specific as individually stated; no Stage B/C promotion |
| [00I AWS Step Functions/RDS](./baseline/00I_A01_AWS_STEP_FUNCTIONS_RDS_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) ordinary → defended → same frozen defended-under-drift | **Stage A — Simplified** | strong continuity and drift controls over the 00I Challenge | unscored as Stage A Cost unless separately declared | stale/prohibited action is primary | I/M not separately priced/scored | stage-based | not part of frozen route | source-reviewed design + inspectable skeleton/fixture evidence; unexecuted as AWS product; Stage B/C not established |
| [R01 core](./baseline/reductions/00G-R01/README.md) | **Stage A — rich probabilistic reference instantiation** | richest current C/R/E specification-discovery reference | explicit | explicit | explicit I/M/P and sufficient-delivery `s` | quantitative `A_{b,δ,p}` | optional downstream projection | mathematical / virtual / harness stages separately stated |
| [R01 technology-extension protocol](./baseline/reductions/00G-R01/extensions/TECHNOLOGY_EXTENSION_PROTOCOL.md) | **Stage A internal extension discipline** | Stage1 preserved correspondence/isomorphism + Stage2 non-isomorphic mechanisms/composition | explicit where profile declares it | explicit where profile declares it | explicit where profile declares it | quantitative/profile-specific | not intrinsic | protocol / proof / traversal stages; not a standalone Stage result |
| [Human Escalation / Whispering](./baseline/reductions/00G-R01/extensions/HUMAN_ESCALATION_WHISPERING.md) | **Stage A — rich** | kernel mapping + additional mechanisms + stochastic C/R/E + R1/R2/R3 | explicit virtual and finite local model ledgers | explicit `r` | explicit `s`, X/Y/M and incompletion | quantitative | deployment BV not calibrated | virtual/analytical core + published finite SQLite companion; no native/human Stage C campaign |
| [01K-A01 Human Capacity / HID component](./baseline/01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1.md) | **Stage A support / reusable component** | process-relative A/B/C/D + EHD profile + runtime human-capacity scheduling + HID architecture burden | explicit human runtime/readiness/ACW/component ledger; `C(τ)=Σ_g c_g(τ)` retained | inherited from frozen Challenge / route; HC-HID adds no private Risk definition | inherited from frozen Challenge I/M/P/Ø; matched-route comparison only | component states + Challenge acceptance remain separate | deployment-specific only | specification + JSON schema + deterministic semantic controls; no real human calibration |
| [RAG / OAuth-OIDC / MCP / SQL-idempotency / durable-workflow current studies](./baseline/reductions/00G-R01/extensions/README.md) | **Stage A — Simplified** | bounded local mechanism/configuration studies with declared Stage1/Stage2 scope | profile-specific actual/local counters; incomplete lifecycle cost | profile-specific | profile-specific I/M/P/Ø | binary/profile-specific | conditional/unscored as stated | executed local SQLite/crypto/parser/model evidence; no native product Stage C |
| STAMP/STPA / SPIFFE selected JWT-SVID / RATS local JWS exercises | **Stage A — Simplified** | selected bounded technology/mechanism exercises | profile-specific | profile-specific | scenario-defined I/M/P/Ø | fixture/instrument acceptance | not deployment BV | finite model / actual local cryptographic or file/JWS operations; no full native/product validation |
| [RS-00E-Q1a v0.5 / Stage-0 execution](./baseline/fixtures/RS-00E-Q1a/README.md) | **Stage A — Simplified deterministic historical evidence** | one bounded Q1a specification/trajectory fixture family | modelled local burden only | bounded branch-specific | B1/B3 tie in descriptive fixture; no comparative differential | Stage-0 descriptive fixture acceptance | none | executed deterministic traces + corrected replay; no independent reviewer; not Stage B/C |
| [R01 C02 Oracle/harness](./baseline/reductions/00G-R01/oracle/README.md) | **DDS test-infrastructure qualification** | oracle/blinding/reference/replay/resource/admission controls shared by later Stages | evaluator/infrastructure separated | not a substantive Stage result | not a substantive Stage result | instrumentation self-test | none | instrument `0.7` under freeze `v0.9`; no real technology result |
| [DBC v0.2](./DECISION_BOUNDARY_CHALLENGE_v0.2.md) | **Cross-stage DDS support** | Challenge/adjudication vocabulary, dispositions and case families | burden vector | branch-specific outcomes | value/continuity gates as preregistered | hard gates + comparative rule when used | may consume deployment value rule | evidence ladder DBC-EL#; no independent method status |
| [00D v0.2 / v0.3](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | **DDS comparator/fairness support** — primarily A/C | matched B0–B3 / strong-peer/resource symmetry and comparison discipline | matched burden | measured outcome when executed | matched outcome | preregistered comparison | not intrinsic | benchmark design/execution as individually stated; comparative execution/independence still bounded by source status |
| [DDS Stage B](./DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md) / first 00I-S5 pilot | **Stage B — Architecture Verification** | frozen Stage A specification package → architecture/reference realization | verification burden optional/profile-specific | not Stage A Risk unless explicitly imported for regression | requirement-level verification, not deployment Effectiveness | VERIFIED / PARTIALLY_VERIFIED / NONCONFORMANT / NOT_ESTABLISHED | not intrinsic | canonical Stage B contract exists; first bounded pilot planned/not yet established as a completed architecture result |
| [DDS Stage C](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md) / C11→T03 real-technology route | **Stage C — Implementation / Problem Validation** | pinned executable implementation against originating Challenge and observed effects | actual registered operational/resource ledger | Challenge-defined material risk | actual bounded implementation effectiveness | VALIDATED_WITHIN_SCOPE / FAILED / trade-off / NOT_ESTABLISHED / infrastructure error | deployment-specific only | canonical Stage C contract and admission skeleton exist; no current native product completion claim |

### Registry reading rule

- A historical local version number (`v0.4`, `v0.5`, Oracle freeze `v0.9`, etc.) belongs to that artefact family, not to the DDS Stage taxonomy.
- **Simplified** describes declared coverage, not an automatic downgrade in evidence quality.
- Evidence mode (documentary, analytical, symbolic, executable fixture, native execution, independent replication) is orthogonal to Stage identity.
- Frozen records are never rewritten merely to make this registry look current. Entry points and current reports carry the crosswalk.
- If an artefact changes its object under test, a successor profile must declare the new Stage prospectively rather than relabel a historical result.

## 9. Canonical navigation

1. [Stage A — Specification Discovery](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md)
2. [Stage B — Architecture Verification](./DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md)
3. [Stage C — Implementation / Problem Validation](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md)
4. [Research basis and neighbouring approaches](./DDS_RESEARCH_BASIS_AND_BENCHMARKING_2026-10-06.md)
5. [DDS source register](./DDS_SOURCE_REGISTER_2026-10-06.json)
6. [DDS bibliography](./DDS_REFERENCES_2026-10-06.bib)

## 10. Migration and preservation status

The pre-existing Stage A file path is intentionally preserved because it is widely referenced throughout the corpus. It is now the canonical **Stage A** source, not the complete DDS method router.

As of 7 October 2026, the active canonical routers, R01/extension entry points, legacy Oracle/harness/testbed indexes, current technology studies/profiles, DBC/00D support routes, WORKPLAN/VISUAL_GUIDE and Ecosystem Positioning review route have been cross-referenced to this Index and the applicable DDS Stage.

Existing historical results, Run Cards, FREEZE files, traces, manifests, hashes and source-native terminology are **not rewritten by the migration**. Where a frozen record contains the former identity/path “single canonical DDS technical profile” / `DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md`, that field remains evidence of the method identity used when the run was registered/executed; current entry points explain that the old path is Stage A and this Index is now the complete method router.

Any later stale-link correction is corpus maintenance, not a scientific regrading or a new DDS method version.
