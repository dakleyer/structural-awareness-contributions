# Deployment Differential Study (DDS) — Canonical Method Index v0.1

**Status:** canonical working method router for the Ecosystem Awareness research corpus; not an adopted standard, certification scheme, assurance opinion or claim of product superiority.  
**Date:** 7 October 2026.  
**Method identity:** one DDS method, three substantive development gates.  
**Gate A source:** [DDS Gate A — Specification Discovery / Challenge–Trajectory Profile v0.1](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md)  
**Gate B source:** [DDS Gate B — Architecture Verification v0.1](./DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md)  
**Gate C source:** [DDS Gate C — Implementation / Problem Validation v0.1](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md)  
**Research basis:** [DDS research basis, benchmarking and value proposition](./DDS_RESEARCH_BASIS_AND_BENCHMARKING_2026-10-06.md)

## 1. One method, three gates

DDS is the single substantive testing/evaluation method used by this corpus. The gates are distinguished by the **object under test** and by the **authoritative reference used to adjudicate it**.

| DDS gate | Object under test | Authoritative reference | Primary output |
|---|---|---|---|
| **Gate A — Specification Discovery** | Candidate specification, mechanism, control profile or technology/configuration trajectory | Frozen Challenge, scenario/reduction, strong peers, falsifiers and acceptance rule | Versioned candidate specification package / bounded differential finding |
| **Gate B — Architecture Verification** | Candidate architecture or reference realization intended to implement the Gate-A specification | Frozen Gate-A specification package and its requirement/behavior contract | Versioned verified/partially verified/nonconformant architecture package |
| **Gate C — Implementation / Problem Validation** | Pinned executable implementation/configuration | Originating Challenge plus independently observed execution/effect/target state | Bounded empirical implementation/problem-validation finding |

The default maturation path is:

~~~text
Challenge
   ↓
DDS Gate A — discover / select the specification
   ↓
Gate-A specification package
   ↓
DDS Gate B — verify architecture realization
   ↓
Gate-B architecture package
   ↓
DDS Gate C — validate implementation against the problem
~~~

A pre-existing architecture or product does not need to have been designed by DDS. It may enter Gate B through an explicit mapping to a frozen Gate-A package and may enter Gate C only after the applicable lineage, registration and evidence conditions are declared.

## 2. Evidence mode is orthogonal to gate identity

Documentary, analytical, mathematical, virtual, symbolic, deterministic-fixture, controlled-harness, native-execution, matched-campaign and independently replicated evidence are **evidence modes**, not DDS gates.

Examples:

- executable Python over an abstract specification can still be **Gate A**;
- a formal or deterministic reference model can be **Gate B** if the object under test is the architecture realization against the frozen specification;
- **Gate C** requires a claim about a pinned implementation/configuration against the Challenge and observed effects, even if the environment is still a bounded sandbox.

No evidence mode silently promotes a result from one gate to another.

## 3. Full and Simplified DDS gate profiles

A profile may deliberately exercise only a bounded subset of one gate.

Use:

- **DDS Gate A/B/C profile** when the declared gate question and required surfaces are covered for the stated scope;
- **Simplified DDS Gate A/B/C profile** when selected gate surfaces are intentionally collapsed, unscored or out of scope.

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

A support artefact may be used by more than one DDS gate.

## 5. Namespace rule

To prevent collision with existing scenario terminology:

- **DDS Gate A / B / C** means only the three development gates in this index.
- **trajectory gate** means a local decision/validation boundary inside a Challenge, including Q0–Q6 or equivalent local gates.
- **gate policy** means a profile-specific acceptance/verification policy; it is not a DDS Gate.
- **Stage-0 / Stage-1** retain the meaning assigned by the source testbed that owns them.
- **C02 / C11 / T03** retain their R01 lifecycle/delivery meaning.

## 6. Claim propagation rule

No gate result automatically proves a later gate.

- Gate A does not establish that an architecture realizes the selected specification.
- Gate B does not establish that the realized architecture solves the Challenge in execution.
- Gate C does not establish universal product safety, unrestricted transfer, certification or standards adoption.

A failure may diagnose a problem at the current gate or justify opening a successor of an earlier gate, but the failed record is preserved.

## 7. Historical and pre-DDS evidence incorporation

DDS was introduced after several bounded fixture, oracle, harness and benchmark artefacts already existed. Those artefacts are **not abandoned and are not parallel testing methods**. They are incorporated into DDS according to the object they tested and the evidence they actually produced.

This incorporation is classificatory and preservational:

- historical versions, commits, pre-registrations, freezes, traces and results remain authoritative for their own recorded runs;
- an artefact version such as `v0.4`, `v0.5` or an oracle freeze such as `v0.9` is the version of **that artefact**, not a DDS method version and not a later/higher DDS Gate;
- incorporation into DDS does not retroactively strengthen a result, make a descriptive fixture comparative, or convert instrumentation evidence into product validation;
- the applicable DDS Gate is determined by the **object under test**, not by whether Python, a harness or an executable fixture was used.

Current legacy incorporation map:

| Historical / pre-split artefact family | Original role and evidence | Current DDS reading |
|---|---|---|
| **00D-A01 bounded oracle / test construction** | Test-design discipline for frozen facts, oracle and controls | DDS support infrastructure usable by Gate A/B/C as applicable; not a substantive Gate result by itself |
| **00D-A03 RS-00E-Q1a Stage-0 harness design** | One deterministic harness design for one fixture family | DDS test-infrastructure design supporting a bounded Simplified Gate-A execution; not Gate B/C |
| **RS-00E-Q1a v0.5 / Stage-0 execution** | Descriptive deterministic fixture run; B1/B3 tie; no independent reviewer | Historical **Simplified DDS Gate-A deterministic evidence** for its bounded specification/trajectory question; Stage-0 remains the source testbed maturity label |
| **00L paper/symbolic traversals and correction runs** | Analytical/symbolic paired controls and regression evidence | Simplified DDS Gate-A analytical/symbolic evidence within each declared scope |
| **R01 C02 oracle/harness, freezes v0.3–v0.9** | Instrument qualification, blinding, replay, resource and reference controls | Shared DDS **test-infrastructure qualification**; not itself Gate A/B/C substantive evidence |
| **00D v0.2 / v0.3 benchmark work** | Strong-peer, matched-resource and comparison discipline | DDS comparator/fairness support, primarily for Gate A and Gate C; not a second method |
| **DBC** | Decision-boundary challenge/adjudication vocabulary | Cross-gate DDS support module; not a second method |

Where an older record says “Stage-0”, “benchmark”, “oracle”, “harness”, “testbed” or another historical local term, preserve that term for the source record and use this index to understand its current DDS role.

## 8. Canonical navigation

1. [Gate A — Specification Discovery](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md)
2. [Gate B — Architecture Verification](./DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md)
3. [Gate C — Implementation / Problem Validation](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md)
4. [Research basis and neighbouring approaches](./DDS_RESEARCH_BASIS_AND_BENCHMARKING_2026-10-06.md)
5. [DDS source register](./DDS_SOURCE_REGISTER_2026-10-06.json)
6. [DDS bibliography](./DDS_REFERENCES_2026-10-06.bib)

## 9. Migration note

The pre-existing Gate-A file path is intentionally preserved because it is widely referenced throughout the corpus. From this revision forward it is the canonical **Gate-A** source, not the complete DDS method router.

Existing historical results, freezes, hashes and source-native terminology are not rewritten by this split. Corpus-wide profile relabelling and router updates are a separate migration step.
