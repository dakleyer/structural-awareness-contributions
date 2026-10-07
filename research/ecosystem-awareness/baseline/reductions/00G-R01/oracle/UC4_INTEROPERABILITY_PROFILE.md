# R01 ↔ Nelson UC-4 interoperability profile

Working bridge v0.1 · 4 October 2026 · source-contributor review requested before calling it UC-4-compatible.

## 1. Design intent

Nelson's UC #4 is the **primary testbed contract** for R01 integration with Theme #13. R01 should enter that testbed as a bounded imported profile, not require UC #4 to adopt an R01-native experiment format.

UC #4 Requirements 22–24 are therefore treated as the governing interoperability constraints:

- versioned adapters for imported contracts;
- frozen positive, boundary and rejection cases with machine-readable expected outcomes;
- mutually agreed, version-pinned scope with source-contributor validation and no silent maintenance obligation.

Source: https://github.com/FG-TIDA/use-cases/issues/4

Nelson's package description also separates common experiment data from adapter-specific mappings. It records question/hypothesis, controlled change, actors/trust boundaries, source versions, expected observations, resources, reproducibility and sharing. Schema 1.1.0 additionally records assessment time, determination consumed, provenance, required execution capabilities and separate technical/preparer/contributor review states.

Sources:
- https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5847245589
- https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5871266911
- revised #13 mapping package v0.4.1-r1: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5900725441
- Stage-0 calibration result: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5949120841

## 2. What R01 reuses unchanged in meaning

| UC-4 concept | R01 use |
|---|---|
| Experiment question / hypothesis | Identifies the bounded R01 claim or technology question; never inferred from results. |
| Controlled change | Defines exactly what differs between comparator/technology conditions. |
| Source versions | Pins R01 scenario, technology profile, imported Theme outputs and adapter versions. |
| Adapter | Preserves source-specific semantics and translates only at the declared boundary. |
| Expected outcome | Stored outside the candidate-visible view and applied only after candidate execution. |
| Assessment time | Required because R01 evidence, mandate, dependency and state applicability are time-bound. |
| Consumed determination reference | Identifies an upstream determination without allowing R01/EA to recreate that semantic authority. |
| Required capabilities | Declares what the execution environment must actually provide before a case is runnable. |
| Review states | Technical validity, preparer review and source-contributor semantic review remain distinct. |
| Positive / boundary / rejection vectors | Used directly as the minimum Stage-0 control structure. |

## 2.1 Nelson Stage-0 controls reused

Nelson reports 64 passing reference assertions in the UC-6 / Theme #13 calibration, plus deliberate applicability corruption, malformed-record isolation, deterministic replay, missing agent-ID sensitivity and case-order reversal. R01 reuses those **testbed patterns**, not the UC-6 authority semantics. The detailed source-to-R01 mapping is in [NELSON_BASELINE_IMPORT.md](./NELSON_BASELINE_IMPORT.md).

R01 additionally adds an identifier-permutation control because §2.17 explicitly requires auditing accidental hints, and a no-reference vector that must remain `INCONCLUSIVE`.

## 3. R01-only sidecar

R01 needs private information that **must not become a shared Theme #13 interface**. It is therefore kept in a sidecar referenced by the experiment/test-vector identity.

The sidecar adds only:

- private frozen-world reference and hash;
- participant-view projection and forbidden-private-field policy;
- finite operation/cost/deadline contract from R01 §§2.6, 2.11–2.12;
- exact bounded reference method(s);
- R01 task-state and candidate-state evaluation from §§2.16–2.17;
- acceptance parameters from §1.4: epsilon, economic cost target b, physical budget R and deadline T;
- separate evaluator/oracle resource ledger;
- sealed candidate-trace hash before reference evaluation.

These are evaluator/testbed concerns. They are **not Theme #13 signal fields** and are not proposed as FG-TIDA-wide vocabulary.

## 4. Semantic ownership

R01 must not turn imported determinations into locally authored truth.

```text
source owner determination
        |
        v
UC-4 versioned adapter
        |
        v
Theme #13 / EA consumer view
        |
        +--> R01 participant-visible observation
        |
        +--> private testbed record of the source/version/expected relation
```

If authority, delegation, identity, oversight capacity or another imported state changes, the adapter preserves that source meaning. R01 may evaluate whether reliance remains supported in its scenario, but actual re-determination remains with the semantic owner.


## 4.1 Working design note — one DDS, three validation gates

> **Review status only.** This section is a design proposal for discussion before any amendment to the canonical DDS. It does not change Nelson's UC-4 stages, the existing DDS extension-review Stage 1/Stage 2 terminology, any frozen R01 result, or the current oracle implementation.

The same DDS may mature through three different validation gates. They reuse one oracle/testbed framework, but **the object being adjudicated and the reference used by the oracle are different at each gate**. The gates are therefore not three names for stronger evidence of the same claim.

```text
Challenge / failure family
        |
        v
Gate A — Specification Discovery
        |     freezes the surviving specification package
        v
Gate B — Architecture Conformance
        |     freezes a conformant architecture/reference realization
        v
Gate C — Implementation / Problem Validation
              tests a pinned executable implementation against the Challenge
```

### Shared oracle substrate

The three gates may reuse the same infrastructure for version pins, hashes, private evaluator state, candidate-visible projections, source ownership, resource ledgers, trace sealing and post-run adjudication. A gate-specific oracle contract determines **which reference is authoritative for that gate** and which evidence is admissible.

A future machine-readable profile could therefore add a gate selector such as `A_SPEC_DISCOVERY | B_ARCH_CONFORMANCE | C_PROBLEM_VALIDATION` plus the hashes of the candidate artifact, reference contract and acceptance policy. This is only a design direction at this stage; no schema change is proposed here.

### Gate A — Specification Discovery

**Object under test:** candidate requirements/specification packages.

**Question:** given the frozen Challenge, which specification or combination of specifications removes or reduces the material failure route while preserving legitimate/high-value routes and respecting the declared Cost/Risk/Effectiveness and authority constraints?

**Oracle reference:** the frozen Challenge/world truth, evaluator-private I/M/P/Ø relation or equivalent acceptance facts, positive/continuity controls, falsifiers and the declared strong conventional/reference alternatives.

Gate A may use documentary mappings, analytical or mathematical checks, virtual traversals, deterministic fixtures, model checking or other evidence modes appropriate to the bounded question. It does **not** require that the candidate specification already exist as a production implementation.

The oracle should be able to distinguish at least:

- a candidate specification that leaves the target P/failure route reachable;
- a candidate that closes P only by destroying legitimate I/M continuity;
- competing specifications that are non-dominated under the frozen acceptance policy;
- a conventional/reference specification that closes the problem at equal or lower burden;
- insufficient evidence.

**Gate-A product:** a versioned **candidate specification package** with explicit surviving requirements, assumptions, exclusions, falsifiers and evidence status. Gate A is the most developed of the three gates in the current DDS work.

### Gate B — Architecture Conformance

**Working systems-engineering alias:** **verification of specification realization**. This is deliberately close to established verification terminology rather than a new DDS-specific meaning.

**Object under test:** a candidate architecture, reference model or executable conformance layer intended to realize the Gate-A specification package.

**Question:** does the architecture actually realize the frozen specification, including its interfaces, semantic ownership, negative requirements and boundary behavior?

**Oracle reference:** the **frozen Gate-A specification package**, its requirement-to-architecture mapping, conformance fixtures, negative controls and counterexamples. The Gate-B oracle must not silently substitute the desired Challenge outcome for specification conformance.

Typical Gate-B checks may include:

- every mandatory selected requirement has an identified realization or an explicit unsupported status;
- source/authority semantics are preserved across interfaces rather than locally reinvented;
- required state, provenance, timing and residual information survive the declared transformations;
- positive controls remain possible;
- negative controls, mutations and counterexamples are rejected for the right reason;
- no hidden oracle/private truth is required by the candidate architecture;
- architecture-level bypasses do not make a nominally present requirement ineffective.

A failure at Gate B normally triggers architecture revision. If the architecture exposes a contradiction, impossibility or missing requirement in the frozen specification, the process returns explicitly to **a new Gate-A specification version**; Gate B must not rewrite Gate A in place after seeing the result.

**Gate-B product:** a versioned **conformant architecture/reference realization** or a bounded non-conformance/partial-conformance finding. Passing Gate B does not establish that the architecture solves the real Challenge in deployment.

#### Gate B — external lineage, reusable machinery and limits

Gate B should reuse established **verification** practice rather than invent a parallel discipline.

- **IEEE 1012-2024 — System, Software, and Hardware Verification and Validation.** IEEE frames verification and validation as distinct questions: development products are checked for conformance to the requirements of the activity, while validation asks whether the product satisfies intended use and user needs. Gate B aligns with the first question.  
  https://standards.ieee.org/ieee/1012/10784/
- **NASA Systems Engineering Handbook — Product Verification versus Product Validation.** NASA states the same distinction operationally: verification demonstrates compliance with requirements; validation demonstrates intended purpose in the intended environment. NASA also uses a Requirements Verification Matrix linking each shall-requirement to its verification evidence/method. Gate B can reuse this traceability shape.  
  https://www.nasa.gov/reference/2-4-distinctions-between-product-verification-and-product-validation/  
  https://www.nasa.gov/reference/system-engineering-handbook-appendix/
- **ISO/IEC/IEEE 29148:2018 — Requirements engineering.** Reuse requirements identification, lifecycle discipline and traceability where applicable. DDS does not claim clause-level conformance without licensed normative review.  
  https://www.iso.org/standard/72089.html
- **ISO/IEC/IEEE 42010:2022 — Architecture description.** Reuse architecture-description concepts, viewpoints, model kinds, correspondences and its explicit conformance treatment for architecture descriptions/frameworks/languages. Important boundary: 42010 conformance is not by itself proof that the entity architecture realizes the Gate-A functional requirements or solves the Challenge.  
  https://www.iso.org/standard/74393.html
- **TLA+ refinement / formal implementation.** Where Gate A and the candidate realization admit formal behavioural specifications, refinement mappings can be used to test/prove that a lower-level specification implements a higher-level one. This is a powerful optional Gate-B method, not a universal requirement and not evidence beyond the proved properties/direction.  
  https://lamport.azurewebsites.net/pubs/simple.pdf  
  https://lamport.azurewebsites.net/tla/book-02-02-27.pdf
- **ETSI TTCN-3.** Where the realization exposes an executable protocol/interface and the question is black-box conformance, TTCN-3 offers standardized test-case, verdict, timer and distributed-execution machinery and is used in standards conformance suites. It is an execution/conformance technology, not an oracle for whether the Gate-A specification itself is the right one.  
  https://ttcn-3.etsi.org/index.php/about/introduction

**What DDS adds at Gate B:** not a new definition of verification. DDS binds the verification target to the exact Gate-A package that survived the frozen Challenge, preserves the Challenge falsifiers/positive controls as regression pressure, keeps source semantic ownership explicit, and prevents a verified architecture from being relabelled as empirically validated.

A minimal future Gate-B machine-readable contract could contain:

```text
gate = B_ARCH_CONFORMANCE
reference_spec_hash
candidate_architecture_hash
requirements_trace_map
verification_method_by_requirement
positive_controls
negative_controls / counterexamples
source_semantic_owner_refs
verification_evidence_refs
result = VERIFIED | PARTIALLY_VERIFIED | NONCONFORMANT | NOT_ESTABLISHED
```

This is a design sketch only; it does not amend the current schema.

### Gate C — Implementation / Problem Validation

**Working systems-engineering alias:** **validation against intended problem/use**. This is deliberately close to established validation terminology.

**Object under test:** a pinned executable implementation/configuration of the architecture.

**Question:** when the implementation is exposed to the frozen Challenge or a justified representative/real instantiation of it, does it actually produce the required outcomes within the declared resource, timing, authority and continuity envelope?

**Oracle reference:** the Challenge and independently observed environment/target state. Gate-A specifications and Gate-B conformance records remain provenance and diagnostic evidence; they are **not themselves proof of Gate-C success**.

Gate C therefore requires evidence of actual effects appropriate to its evidence mode, for example:

- pinned executable configuration and dependencies;
- candidate-visible versus evaluator-only information separation;
- matched comparator conditions where comparison is claimed;
- attempted action, actual effect and resulting target state observed separately;
- real/representative Cost, Risk and Effectiveness traces within the declared scope;
- continuity/positive controls so safety is not obtained only by blanket blocking;
- explicit treatment of infrastructure failure and unavailable evidence.

A Gate-C failure must not be repaired by changing the frozen Challenge, acceptance rule or implementation after inspecting the failing run. It opens a successor cycle. The diagnosis may point back to an implementation defect (repeat C), an architecture-realization defect (return to B), or an inadequate specification (return to A), but the failed evidence remains preserved.

**Gate-C product:** bounded empirical problem-validation evidence for the pinned implementation and evidence mode. It does not retroactively upgrade Gate A or Gate B, nor does a Gate-A/B success imply Gate C.

#### Gate C — external lineage, reusable machinery and limits

Gate C should reuse established **validation / TEVV / test execution** machinery.

- **IEEE 1012-2024 and NASA Systems Engineering.** These provide the closest conceptual boundary: validation asks whether the realized product satisfies intended use/user needs in the intended environment. NASA explicitly permits validation by test, analysis, inspection and demonstration and links validation planning to ConOps/stakeholder objectives. Gate C reuses that distinction rather than redefining validation.  
  https://standards.ieee.org/ieee/1012/10784/  
  https://www.nasa.gov/reference/2-4-distinctions-between-product-verification-and-product-validation/  
  https://www.nasa.gov/reference/system-engineering-handbook-appendix/
- **ISO/IEC/IEEE 15288:2023 — system life-cycle processes.** Reuse the system-lifecycle process frame and the distinction between development artefacts and the system of interest across its lifecycle. DDS does not claim full 15288 process alignment from this working note.  
  https://www.iso.org/standard/81702.html
- **ISO/IEC/IEEE 29119-2:2021 — software test processes.** Reuse generic governance/management/implementation structure for testing when appropriate. It does not supply the DDS Challenge, acceptance region or substantive oracle.  
  https://www.iso.org/standard/79428.html
- **NIST TEVV-Athlon (NIST AI 200-2 draft).** This is especially close to the Gate-C concern for AI: NIST frames TEVV-Athlon as a structured, extensible approach for assessing real-world impact/outcomes and explicitly includes agentic systems. DDS can reuse compatible evaluation planning/execution concepts while keeping its own bounded Challenge and differential claim.  
  https://www.nist.gov/artificial-intelligence/ai-research/tevv-athlon-framework-evaluating-ai-systems
- **NIST ARIA Evaluation Planning Manual (NIST AI 200-3, 2026).** ARIA combines model testing, red teaming and user testing for application-level trustworthiness evaluation. Those can become Gate-C evidence modules when material to the Challenge; DDS does not require all three for every profile.  
  https://www.nist.gov/publications/aria-evaluation-planning-manual-elements-aria-style-ai-evaluations
- **ETSI TTCN-3 / Inspect AI / other execution substrates.** These may host repeatable test execution, adapters, scoring and standardized protocol conformance. They do not decide whether the selected Challenge, acceptance rule or deployment interpretation is correct.  
  https://ttcn-3.etsi.org/  
  https://inspect.aisi.org.uk/

**What DDS adds at Gate C:** not a new definition of validation. DDS carries forward the exact Challenge/failure family that generated Gate A, the verified realization lineage from Gate B, matched comparator/fairness conditions, the I/M/P/Ø or equivalent outcome model, and explicit Cost/Risk/Effectiveness accounting. The purpose is to prevent a generic test pass from being promoted into evidence that the original problem was solved.

A minimal future Gate-C machine-readable contract could contain:

```text
gate = C_PROBLEM_VALIDATION
challenge_hash
gate_A_spec_hash
gate_B_architecture_hash
implementation/configuration_pin
environment_or_fixture_pin
candidate_visible_information_contract
comparator_contract
target/effect_observer_contract
C_R_E_ledger
acceptance_policy_hash
result = VALIDATED_WITHIN_SCOPE | FAILED | NONDOMINATED | NOT_ESTABLISHED | INFRASTRUCTURE_ERROR
```

Again this is a design sketch only.

### Gate A/B/C — reuse map and non-duplication boundary

| DDS gate | Closest established discipline | Reuse directly | DDS-specific differential | Do **not** claim |
|---|---|---|---|---|
| **A — Specification Discovery** | Requirements/design exploration, hazard/failure analysis, formal modelling, experimental design | Existing DDS bibliography: STPA, NIST/ISO risk/quality, formal methods, benchmark/evaluation practice | Select competing specification packages against one frozen Challenge with strong-peer credit, positive/negative routes and C/R/E where in scope | That DDS invented requirements engineering, hazard analysis or design-space exploration |
| **B — Architecture Conformance** | Verification / refinement / requirements traceability | IEEE 1012, NASA verification matrices, ISO 29148, ISO 42010 architecture-description machinery, TLA+ refinement, TTCN-3 where appropriate | Verify the architecture/reference realization specifically against the Gate-A winner(s), retaining semantic ownership and Challenge-derived falsifiers | That 42010 AD conformance proves architecture functionality; that a formal proof transfers beyond proved properties; that B validates intended use |
| **C — Problem Validation** | System/product validation, TEVV, testing | IEEE 1012/NASA validation, ISO 15288/29119, NIST TEVV-Athlon/ARIA, TTCN-3/Inspect as execution substrates | Validate the pinned implementation against the originating Challenge with observed effects, matched comparators and DDS differential accounting | That a generic benchmark score, conformance suite or TEVV framework by itself proves the DDS problem solved |

This three-gate structure is therefore best understood as a **DDS orchestration of existing verification/validation disciplines around a Challenge-derived specification-discovery stage**, not a claim to have invented a new universal V&V architecture.

### Gate separation and progression

The default research-development path is **A → B → C**, but the gates are orthogonal to UC-4's current compatibility levels and to DDS evidence labels. A pre-existing product may enter B/C through an explicit mapping to a frozen specification and Challenge; it does not need to have been built by this programme. Conversely, an analytical Gate-A result does not become a product claim merely because a local harness exists.

The oracle should preserve a separate result record for each gate:

| Gate | Primary reference | Candidate object | What a pass establishes | What it does not establish |
|---|---|---|---|---|
| **A** | Frozen Challenge / acceptance truth | Specification package | The candidate specification survives the bounded architecture test under the declared evidence mode. | Architecture realization or product effectiveness. |
| **B** | Frozen Gate-A specification | Architecture / reference realization | The architecture conforms to the selected specification within the tested contract. | Real-world/representative Challenge effectiveness. |
| **C** | Frozen Challenge + observed effects | Executable implementation | The pinned implementation meets the bounded problem-validation acceptance rule. | Universal product safety, certification or unrestricted transfer. |

No gate result is silently promoted into another. A shared oracle implementation may host all three, but its **authoritative reference and admissible claim change with the selected gate**.

## 5. Compatibility levels

| Level | Meaning |
|---|---|
| R01-BRIDGE-DRAFT | R01 sidecar and adapter contract exist; no source-contributor review. Current status. |
| UC4-SOURCE-REVIEWED | Nelson confirms the mapping is compatible with his current experiment/testbed semantics. |
| UC4-SCHEMA-VALIDATED | The R01 profile has been packaged against a pinned UC-4 schema and passes its validator. |
| STAGE0-ADMITTED | Frozen case vectors, capabilities, reviews and expected outcomes are accepted for deterministic execution. |
| STAGE1-ADMITTED | A separately agreed federated/runtime integration exists. |

No higher level is inferred from a lower one.

## 6. Requested review points for Nelson

Before claiming UC4-SOURCE-REVIEWED, ask Nelson to correct at least these points:

1. whether R01's private evaluator fields should remain a sidecar or live under an extension object in his experiment package;
2. the preferred identity/reference mechanism linking a sidecar to a UC-4 experiment and test-vector ID;
3. whether the sealed pre-oracle candidate-trace hash should be part of the common experiment record, adapter result or external evidence manifest;
4. how he wants evaluator-only resource cost represented without contaminating the participant/comparator burden;
5. whether the current explicit statuses `PASS | FAIL | INCONCLUSIVE | INFRASTRUCTURE_ERROR` fit his expected-outcome semantics or require mapping.

Until that review, this profile deliberately avoids claiming exact UC-4 schema compatibility.
