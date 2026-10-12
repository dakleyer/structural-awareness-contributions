# Deployment Differential Study (DDS) — Canonical Method Index v0.1

> **Research-candidate register — 12 October 2026:** [DDS potential contributions and source register](./DDS_POTENTIAL_CONTRIBUTIONS_REGISTER_v0.1.md) collects proposed additions from the mathematical and other article-review initiatives, with strong comparators, development obligations and source links. It is a supporting research backlog, not a new method authority or an admitted Stage result.

**Status:** canonical working method router for the Ecosystem Awareness research corpus; not an adopted standard, certification scheme, assurance opinion or claim of product superiority.  
**Date:** 7 October 2026.  
**Terminology revision:** 0.1.3 — Stage A/B/C; definitions and evidence unchanged.  
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
- **Cross-corpus examples:** UC-21 `R0/R1/R2` are comparison routes; `T08/S5` identifies the AWS Step Functions/RDS profile for the delayed repair, while `T09/S6` identifies the Panodyssey/TEMS rights profile. AWS `AWS-I0/I1/I2`, Steven Zhao's local `I0/I1/I2`, R01 `M/I/P` and DDS `I/M/P/Ø` retain distinct source-specific meanings. For the full translation discipline, consult [Stage A §10A — namespace safety](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#10a-namespace-safety-for-cross-corpus-review).

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
| 00E–00J positive/negative technology trajectories and current product profiles | **Stage A — Simplified** | Challenge + technology/configuration mapping + trajectory/quality gates + positive/negative routes | generally unscored | primary / branch-specific | generally collapsed into legitimate continuity / expected outcome | binary / trajectory-gate based | not part of frozen route | documentary / symbolic / fixture-specific as individually stated; no Stage B/C promotion |
| [00I AWS Step Functions/RDS](./baseline/00I_A01_AWS_STEP_FUNCTIONS_RDS_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) ordinary → defended → same frozen defended-under-drift | **Stage A — Simplified** | strong continuity and drift controls over the 00I Challenge | unscored as Stage A Cost unless separately declared | stale/prohibited action is primary | I/M not separately priced/scored | trajectory-gate based | not part of frozen route | source-reviewed design + inspectable skeleton/fixture evidence; unexecuted as AWS product; Stage B/C not established |
| [R01 core](./baseline/reductions/00G-R01/README.md) | **Stage A — rich probabilistic reference instantiation** | richest current C/R/E specification-discovery reference | explicit | explicit | explicit I/M/P and sufficient-delivery `s` | quantitative `A_{b,δ,p}` | optional downstream projection | mathematical / virtual / harness stages separately stated |
| [R01 technology-extension protocol](./baseline/reductions/00G-R01/extensions/TECHNOLOGY_EXTENSION_PROTOCOL.md) | **Stage A internal extension discipline** | Stage1 preserved correspondence/isomorphism + Stage2 non-isomorphic mechanisms/composition | explicit where profile declares it | explicit where profile declares it | explicit where profile declares it | quantitative/profile-specific | not intrinsic | protocol / proof / traversal stages; not a standalone Stage result |
| [Human Escalation / Whispering](./baseline/reductions/00G-R01/extensions/HUMAN_ESCALATION_WHISPERING.md) | **Stage A — rich** | kernel mapping + additional mechanisms + stochastic C/R/E + R1/R2/R3 | explicit virtual and finite local model ledgers | explicit `r` | explicit `s`, X/Y/M and incompletion | quantitative | deployment BV not calibrated | virtual/analytical core + published finite SQLite companion; no native/human Stage C campaign |
| [01K-A01 Human Capacity / HID component](./baseline/01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1.md) | **Stage A support / reusable component** | process-relative A/B/C/D + EHD profile + runtime human-capacity scheduling + HID architecture burden | explicit human runtime/readiness/ACW/component ledger; `C(τ)=Σ_g c_g(τ)` retained | inherited from frozen Challenge / route; HC-HID adds no private Risk definition | inherited from frozen Challenge I/M/P/Ø; matched-route comparison only | component states + Challenge acceptance remain separate | deployment-specific only | specification + JSON schema + deterministic semantic controls; no real human calibration |
| [RAG / OAuth-OIDC / MCP / SQL-idempotency / durable-workflow / cache-TTL / queues / typed-output / observability current studies](./baseline/reductions/00G-R01/extensions/README.md) | **Stage A — Simplified** | bounded local mechanism/configuration studies with declared Stage1/Stage2 scope | profile-specific actual/local counters; incomplete lifecycle cost | profile-specific | profile-specific I/M/P/Ø | binary/profile-specific | conditional/unscored as stated | executed local SQLite/crypto/parser/model evidence; no native product Stage C |
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
7. [Limited claim source/consumer register](./DDS_CLAIM_SOURCE_CONSUMER_REGISTER_v0.1.md) — ten externally reused statements, their owning sources, evidence ceilings and maintenance triggers; an editorial aid, not a new DDS authority.
8. [Stage A VNext review ledger](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md) — proposals, applied successors and remaining audit tests; frozen Stage A remains the source contract.

## 10. Migration and preservation status

The pre-existing Stage A file path is intentionally preserved because it is widely referenced throughout the corpus. It is now the canonical **Stage A** source, not the complete DDS method router.

As of 7 October 2026, the active canonical routers, R01/extension entry points, legacy Oracle/harness/testbed indexes, current technology studies/profiles, DBC/00D support routes, WORKPLAN/VISUAL_GUIDE and Ecosystem Positioning review route have been cross-referenced to this Index and the applicable DDS Stage.

Existing historical results, Run Cards, FREEZE files, traces, manifests, hashes and source-native terminology are **not rewritten by the migration**. Where a frozen record contains the former identity/path “single canonical DDS technical profile” / `DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md`, that field remains evidence of the method identity used when the run was registered/executed; current entry points explain that the old path is Stage A and this Index is now the complete method router.

Any later stale-link correction is corpus maintenance, not a scientific regrading or a new DDS method version.

### Current extension-study completion records — 7 October2026

The [study completeness review](./baseline/reductions/00G-R01/extensions/COMPLETENESS_REVIEW_2026-10-07.md) and [current catalogue](./baseline/reductions/00G-R01/extensions/CURRENT_STUDY_CATALOGUE.json) route thirteen scoped executed Stage A studies. Four new local studies add prospective cost/M-admission/Type 1/2 records. They do not establish Stage B/C or native product validation. Dated frozen crosswalks remain historical evidence; current per-study records provide navigation rather than a second canonical method. The newly linked Hugging Face deterministic Stage A card remains design-only until its own prospective execution/admission is complete.


## 11. Reader route from cases to studies and results

The reader route is **UC-21 → objectives → Challenges → DDS → campaigns → results**. Within DDS, the technology/version/configuration is mapped to a Challenge through a specified evaluation scenario/profile. The source method records the bounded base scenario and technology mapping separately; its original meaning, frozen facts and labels remain intact.

**Navigation addition — 12 October 2026.** DDS serves research questions from UC-21 and other cases. Begin with the originating case and objective, identify the exercise and its contract, follow the applicable method and instruments, inspect recorded runs, and return the finding to the question it addresses.

| Reader question | Existing owning route |
|---|---|
| What is UC-21 trying to establish? | [UC-21 public entry](https://github.com/FG-TIDA/use-cases/issues/21) and [current objectives and reader guide](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/README.md#research-objectives) |
| Which scenario, reduction or extension supplies the problem? | [UC-21 scenarios](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/annexes/README.md), [R01 reference scenario](./baseline/reductions/00G-R01/Escenario-creatividad-validacion.md), [technology extension protocol](./baseline/reductions/00G-R01/extensions/TECHNOLOGY_EXTENSION_PROTOCOL.md) and [kernel/proof obligations](./baseline/reductions/00G-R01/extensions/family/KERNEL_AND_PROOF.md) |
| Which DDS stage applies? | [Stage A](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md), [Stage B](./DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md) and [Stage C](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md), selected by object and authoritative reference |
| How are observations and expected outcomes evaluated? | [R01 oracle/harness](./baseline/reductions/00G-R01/oracle/README.md), [preserved v0.9 instrument freeze](./baseline/reductions/00G-R01/oracle/STAGE0_FREEZE_v0.9.json) and [UC-4 interoperability profile](./baseline/reductions/00G-R01/oracle/UC4_INTEROPERABILITY_PROFILE.md) |
| Where are actual study reports and records? | The existing local study records below, [extension index](./baseline/reductions/00G-R01/extensions/README.md) and [catalogue](./baseline/reductions/00G-R01/extensions/CURRENT_STUDY_CATALOGUE.json) |
| Which work is prepared rather than executed? | [HF v0.3 preregistered package](./baseline/reductions/00G-R01/extensions/hugging-face/DDS_STAGE_A_V0_3_PACKAGE_MANIFEST.json) and [its version lineage](./baseline/reductions/00G-R01/extensions/hugging-face/STAGE_A_FREEZE_AND_VERSION_LINEAGE.md) identify the pending blind/mutation result separately from executed HF synthetic explorations |

For terminology, use [Stage A §3](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#3-challenge-first): the Challenge is the problem or failure family, and a bounded scenario, fixture or reduction instantiates it. [Stage A §6](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#6-segments-trajectory-gates-traversals-and-traces) distinguishes profile, traversal, trace and DDS battery/campaign. [UC-21 conventions](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/annexes/CONVENTIONS.md) retain the scenario and route labels. A research campaign, an S4 business campaign and R01's operational campaign are different source contexts and accounting units. Reduction/extension transfer follows its owning proof or family-admission contract; navigation does not merge them.

The oracle/harness evaluates a recorded candidate decision or execution against the declared frozen world, permitted outcomes, quality, resources and deadline. It keeps the evaluator's reference information distinct from candidate observations. Its self-tests qualify the instrument; a substantive study supplies its own registered object, comparators and evidence.

### Existing extension-study report routes

The thirteen extension-study records below declare Simplified Stage A completion within their own local question. Their reports, registrations, freezes and recorded evidence remain at the original paths. A later audit record remains distinct from the original run. Their individual scopes govern the interpretation of each result.

| Study | Question, report and bounded conclusion | Registration and evidence |
|---|---|---|
| Human escalation / whispering | [Study record](./baseline/reductions/00G-R01/extensions/dds-hew-v0.1/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/dds-study-completion-v0.1/HEW_COMPLETION_REPORT.md) | [Registration](./baseline/reductions/00G-R01/extensions/dds-hew-v0.1/RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/dds-hew-v0.1/FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/metrics/hew.json) |
| STAMP/STPA | [Study record](./baseline/reductions/00G-R01/extensions/independent-dds-exercises-v0.1/stamp-stpa/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/dds-study-completion-v0.1/STPA_COMPLETION_REPORT.md) | [Registration](./baseline/reductions/00G-R01/extensions/independent-dds-exercises-v0.1/stamp-stpa/RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/independent-dds-exercises-v0.1/stamp-stpa/FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/metrics/stamp-stpa.json) |
| SPIFFE selected JWT-SVID | [Study record](./baseline/reductions/00G-R01/extensions/independent-dds-exercises-v0.1/spiffe-jwt/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/dds-study-completion-v0.1/SPIFFE_COMPLETION_REPORT.md) | [Registration](./baseline/reductions/00G-R01/extensions/independent-dds-exercises-v0.1/spiffe-jwt/RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/independent-dds-exercises-v0.1/spiffe-jwt/FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/metrics/spiffe-jwt.json) |
| RATS local JWS | [Study record](./baseline/reductions/00G-R01/extensions/independent-dds-exercises-v0.1/rats-jws/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/dds-study-completion-v0.1/RATS_COMPLETION_REPORT.md) | [Registration](./baseline/reductions/00G-R01/extensions/independent-dds-exercises-v0.1/rats-jws/RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/independent-dds-exercises-v0.1/rats-jws/FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/metrics/rats-jws.json) |
| RAG | [Study record](./baseline/reductions/00G-R01/extensions/rag/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/rag/DDS_STUDY.md) | [Registration](./baseline/reductions/00G-R01/extensions/rag/RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/rag/FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/metrics/rag.json) |
| OAuth/OIDC | [Study record](./baseline/reductions/00G-R01/extensions/oauth-oidc/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/oauth-oidc/DDS_STUDY.md) | [Registration](./baseline/reductions/00G-R01/extensions/oauth-oidc/RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/oauth-oidc/FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/metrics/oauth-oidc.json) |
| MCP tool calling | [Study record](./baseline/reductions/00G-R01/extensions/mcp-tool-calling/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/mcp-tool-calling/DDS_STUDY.md) | [Registration](./baseline/reductions/00G-R01/extensions/mcp-tool-calling/RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/mcp-tool-calling/FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/metrics/mcp-tool-calling.json) |
| SQL transactions / idempotency | [Study record](./baseline/reductions/00G-R01/extensions/sql-transactions-idempotency/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/sql-transactions-idempotency/DDS_STUDY.md) | [Registration](./baseline/reductions/00G-R01/extensions/sql-transactions-idempotency/RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/sql-transactions-idempotency/FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/metrics/sql-transactions-idempotency.json) |
| Durable workflows / retries | [Study record](./baseline/reductions/00G-R01/extensions/durable-workflows-retries/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/durable-workflows-retries/DDS_STUDY.md) | [Registration](./baseline/reductions/00G-R01/extensions/durable-workflows-retries/RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/durable-workflows-retries/FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/metrics/durable-workflows-retries.json) |
| Cache / TTL | [Study record](./baseline/reductions/00G-R01/extensions/cache-ttl/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/cache-ttl/DDS_STUDY.md) | [Registration](./baseline/reductions/00G-R01/extensions/cache-ttl/CURRENT_RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/cache-ttl/CURRENT_FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/cache-ttl/RESULTS.json) |
| Queues / acknowledgement / redelivery | [Study record](./baseline/reductions/00G-R01/extensions/queues-ack-redelivery/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/queues-ack-redelivery/DDS_STUDY.md) | [Registration](./baseline/reductions/00G-R01/extensions/queues-ack-redelivery/CURRENT_RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/queues-ack-redelivery/CURRENT_FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/queues-ack-redelivery/RESULTS.json) |
| Structured output | [Study record](./baseline/reductions/00G-R01/extensions/structured-output/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/structured-output/DDS_STUDY.md) | [Registration](./baseline/reductions/00G-R01/extensions/structured-output/CURRENT_RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/structured-output/CURRENT_FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/structured-output/RESULTS.json) |
| Observability / response | [Study record](./baseline/reductions/00G-R01/extensions/observability-response/CURRENT_STUDY_RECORD.json) · [Report](./baseline/reductions/00G-R01/extensions/observability-response/DDS_STUDY.md) | [Registration](./baseline/reductions/00G-R01/extensions/observability-response/CURRENT_RUN_CARD.json) · [Freeze](./baseline/reductions/00G-R01/extensions/observability-response/CURRENT_FREEZE.json) · [Recorded evidence](./baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/observability-response/RESULTS.json) |

For a UC-21-specific comparison, consult the [existing external S5 exercise](https://github.com/zhaoxinghua09-cell/silent-failure-catalog/blob/a9eca743df5a5c1fbef5dc6f792ea08f8add29e0/examples/S5-Qregister/README.md), [research-side audit packet](https://github.com/dakleyer/structural-awareness-contributions/blob/2c7f545e2610e154b2e7d11fe827722bbf3c5658/research/ecosystem-awareness/review-packets/2026-10-11-steven-s5/README.md) and [separate 00I-STATEFUL companion](./baseline/fixtures/00I-STATEFUL/README.md). The [S4/CDA follow-up](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6111953753) retains its proposed state. These links do not combine their outcomes into one campaign.

For campaign reporting, use an existing owning report wherever it already identifies the question, contract/version, inputs, runs, findings and limitations. Add a campaign-level reader document only where a real registered campaign lacks that explanation. Several runs, versions, reductions or annexes can remain linked to one owning record; original paths and frozen results are retained.

Earlier symbolic campaigns, fixtures and reduction records remain reachable through the [EA baseline index](./baseline/README.md), [R01 index](./baseline/reductions/00G-R01/README.md), [00K symbolic campaign summary](./baseline/00K_A04_SIX_PRINCIPLE_SYMBOLIC_EXECUTION_CAMPAIGN_SUMMARY_v0.1.md) and [00L traversal records](./baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README.md). Each record retains its original version, unit of assessment and evidence limits. The thirteen-study table is an entry to the extension catalogue, not an inventory of every campaign in the repository.


## 12. Versions and supporting reading

Choose the method stage first, then the study record and the exact inputs used by its run. The [extension-package reading map](./baseline/reductions/00G-R01/extensions/README.md#complete-package-reading-map--12-october-2026) provides the study guides, cost explanations, shared repair evidence and retained source versions behind the thirteen reports above.

| Question | Reading route | Version and purpose |
|---|---|---|
| How was the diagnostic instrument first checked across different families? | [Validation plan v0.1](./DDS_STAGE_A_GATE_DIAGNOSTIC_VALIDATION_PLAN_v0.1.md) | The original three-family portability plan; its findings retain their registered version. |
| What should an instrument reviewer examine? | [External-audit checklist v0.2](./DDS_STAGE_A_GATE_DIAGNOSTIC_EXTERNAL_AUDIT_CHECKLIST_v0.2.md) and [frozen instrument manifest](./DDS_STAGE_A_GATE_DIAGNOSTIC_AUDIT_MANIFEST_v0.2.json) | Review of the v0.2 instrument package, separate from a candidate-technology verdict. |
| How is the cross-theme decision-boundary profile prepared? | [FG-TIDA evaluation profile v0.2 draft](./fg-tida/tests/FG_TIDA_DECISION_BOUNDARY_EVALUATION_PROFILE_v0.2_DRAFT.md) | This draft deliberately consumes the v0.1 diagnostic design. Its links identify that dependency; a newer instrument does not silently replace it. |

The submitted UC-21 snapshot, the maintained case branch, a registered study freeze and an instrument successor answer different version questions. Follow the cited snapshot for a recorded result and the maintained index for current reading. The [existing DDS review](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md) records the inventory and any unresolved version decisions.


## 13. Select an exercise and keep its comparison dimensions explicit

A case supplies the question and acceptance conditions. DDS supplies the study method. Read the [UC-21 Challenge guide](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/README.md#choose-a-challenge-and-its-evaluation-scenario), then select the bounded scenario, technology/configuration and evidence contract.

| Selection | Owning source | What the record preserves |
|---|---|---|
| Objective and scientific claim | [UC-21 claim selection](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/annexes/HYPOTHESES.md#13-claim-selection) | Case acceptance, HC, HR, HS or the selected H1–H6 contrast. |
| Challenge and admitted variant | [Family admission X1–X7](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/annexes/EXTENSIONALITY.md#4-admission-test-for-an-extension) and [DDS technology mapping](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#4-technology-mapping) | Kernel, receiving boundary, failure predicate, inherited acceptance, positive control, resources and declared additions. |
| Implementation comparison | [UC-21 R0/R1/R2](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/USE_CASE.md#5-select-prepare-and-run-one-experiment) | The tested configuration and, for recurrence, the demonstrated R1 correction retained in R2. |
| Method stage and recorded execution | [DDS stage definitions](#1-one-method-three-stages) and the study's owning record | Stage A/B/C, frozen version, run, actual effect, timing and burden. |

Keep labels qualified in cross-study comparisons. UC-21 R0/R1/R2, AWS-I0/I1/I2, the external S5 simulator's I0/I1/I2, causal conditions A–D, and DDS Stages A/B/C describe different dimensions. The [existing namespace rule](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#10a-namespace-safety-for-cross-corpus-review) preserves those meanings. In particular, the external S5 `I2-complete` selects a supplied-model correction; AWS-I2/R2 tests the retained corrected implementation under admitted drift.

For S4, a research campaign remains distinct from the refund campaign whose business authority is being assessed. Record unauthorized aggregate action and loss of the material finding separately. For an existing exercise, follow its original registration and evidence; a prospective successor declares its own question and changed scope before a new run.


## 14. Select the method profile and its instruments

Select the study's object and authoritative reference first. Then use the instruments admitted for that question.

| Question | Profile or instrument | Reference and use |
|---|---|---|
| Which specification distinctions survive the Challenge? | [Stage A](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) and [gate diagnostic v0.2 audit candidate](./DDS_STAGE_A_GATE_DIAGNOSTIC_PROFILE_v0.2_AUDIT_CANDIDATE.md) | The frozen Challenge and candidate specification; the diagnostic keeps gate verdict, level and dependency separate. Use the [v0.2 instrument freeze](./DDS_STAGE_A_GATE_DIAGNOSTIC_AUDIT_MANIFEST_v0.2.json) for that audit candidate. |
| Does an architecture realize the selected specification? | [Stage B](./DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md) | The frozen specification package and requirement-to-architecture evidence. |
| Does the implementation satisfy the problem under the registered conditions? | [Stage C](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md) | The Challenge, observed target/effect, acceptance policy and matched comparator contract. |
| How are candidate execution, private evaluation and resources recorded? | [R01 C02 reading sequence](./baseline/reductions/00G-R01/oracle/README.md#reading-sequence-from-registration-to-result) | Adapter, broker, frozen policy and sealed traces within the selected R01 profile. |
| How is the HF authority/evidence fixture evaluated? | [HF oracle C3](./baseline/fixtures/00G-HF-ORACLE-v0.4/README.md) | Its own frozen family predicates and controls; select its profile rather than substituting C02 labels. |

For a comparative study, freeze the task, facts, information access, authority, tools, resources, human capacity, timing and intended differences between arms. Read [Stage C comparator conditions](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md#8-comparators-and-fairness) with the selected stage's own contract. The campaign retains both successful conventional controls and adverse or inconclusive findings.


## 15. Recorded work and its owning reports

Read the report that owns the question before its run data. The routes below collect existing work without making a new campaign out of a folder, replay or file count.

| Recorded work | Owning report / evidence route | Unit and reading purpose |
|---|---|---|
| Thirteen local technology studies | [Study and successor lineage](./baseline/reductions/00G-R01/extensions/README.md#follow-the-evidence-from-original-study-to-successor) | Bounded questions, original cases, cost/type and repair successors. |
| Six-principle symbolic work | [00K campaign summary](./baseline/00K_A04_SIX_PRINCIPLE_SYMBOLIC_EXECUTION_CAMPAIGN_SUMMARY_v0.1.md#current-regression-count--12-october-2026) and [execution router](./baseline/fixtures/00K-SUITE/README.md) | Regression assertions over declared fixtures and their retained falsifiers. |
| Six-family paper/symbolic traversals | [00L reports](./baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README.md) | Conditional paper traces, symbolic records and correction/reproduction history. |
| S5 state/effect and recovery | [00I-STATEFUL report](./baseline/fixtures/00I-STATEFUL/README.md) | Local synthetic stateful execution and its SQLite/process-recovery companion. |
| HF receiver comparisons | [HF report-selection guide](./baseline/reductions/00G-R01/extensions/hugging-face/README.md#recorded-comparisons-and-their-results) | Paired programmed receiver paths, cached-lineage and configured Casbin-polling findings. |
| HF probabilistic/social/dynamic work | [R123](./baseline/traversals/00G-HF-PROBABILISTIC-R123-v0.1/RESULTS.md), [social propagation](./baseline/traversals/00G-HF-CONTINUOUS-SOCIAL-v0.1/RESULTS.md), [dynamic review](./baseline/traversals/00G-HF-DYNAMIC-REVIEW-v0.1/results/RESULTS.md) | Networks and receiver/checkpoint records in different constructed campaigns; these lots contain no EA arm. |
| Instrument calibration | [R01 calibration v0.9](./baseline/reductions/00G-R01/oracle/SELFTEST_RECORD_v0.9.md) | Controls of the evaluator infrastructure, kept separate from technology-study outcomes. |

[UC-21's maintained package on main](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/README.md) connects objectives and Challenges to these routes. A case conclusion cites the particular report/version and evidence it uses. Existing registrations retain the names, units and stopping rules under which their work was recorded.
