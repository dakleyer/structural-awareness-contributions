# Deployment Differential Study (DDS) — Canonical Challenge–Trajectory Profile v0.1

**Status:** canonical working DDS technical profile inside the Ecosystem Awareness research corpus; additive public methodology, not an adopted standard, certification scheme, assurance method or claim of product superiority.  
**Date:** 6 October 2026.  
**Scope:** technical/research definition of a DDS exercise and its profiles. Commercial packaging, fees, contracting, sponsor recognition and private commissioning records are governed separately and do not redefine this technical method.

> **Conservation rule.** This profile does not amend, strengthen or reinterpret frozen scenario traversals, R01 proofs, DBC results, 00D benchmark results or historical execution records. It supplies a common DDS vocabulary and coverage map so those artefacts can be described as fuller or simplified DDS implementation profiles without changing their original evidence.

## 1. What a DDS is

A **Deployment Differential Study (DDS)** is a bounded challenge–trajectory evaluation of a technology, technology combination, configuration or deployment.

A DDS asks:

> Given a declared Challenge, a frozen scenario and a specific technology/configuration, which admissible, prohibited or incomplete routes remain reachable; what evidence, cost and uncertainty are accumulated while traversing them; and does the resulting configuration fall inside the preregistered acceptance region?

Where a concrete deployment decision exists, the technical result may then be projected into bounded **Business Value–Risk–Cost (BV–R–C)**.

DDS is the method envelope. R01, the current technology trajectories, DBC and 00D keep their own semantics:

- **R01** is the richest current probabilistic DDS reference instantiation and retains its own mathematics.
- **DBC** is an applied evidence/adjudication route and evidence-maturity framework; it does not redefine DDS route semantics.
- **00D** is a fair-comparison/benchmark contract; it does not define DDS trace accounting.
- The frozen positive/negative technology traversals associated with the current UC21 challenge family are **simplified DDS implementation profiles**. They remain valid in their original form.

## 2. Canonical DDS chain

The canonical chain is:

~~~text
CHALLENGE
   ↓
BOUNDED SCENARIO / REDUCTION
   ↓
TECHNOLOGY / CONFIGURATION MAPPING
   ├─ preserved correspondence / kernel
   ├─ declared parameter changes
   └─ additional mechanisms / information
   ↓
ROUTE + GATE MODEL
   ├─ I_k  high-value admissible routes
   ├─ M_j  market/reference admissible routes
   ├─ P_l  prohibited/material-violation routes
   └─ Ø    incomplete / no-sufficient-route
   ↓
VIRTUAL TRAVERSALS / EXECUTED TRACES
   ↓
TRACE ACCOUNTING
   ├─ Cost
   ├─ Risk
   └─ Effectiveness
   ↓
ACCEPTANCE POLICY
   ↓
ACCEPTED / OUTSIDE ACCEPTANCE / NOT ESTABLISHED
   ↓
OPTIONAL DEPLOYMENT PROJECTION
   └─ Business Value – Risk – Cost
   ↓
DIFFERENTIAL CONTRIBUTION FINDING
~~~

Every DDS implementation profile must state which parts of this chain it actually instantiates and which are intentionally unscored, collapsed, documentary or out of scope.

## 3. Challenge first

The **Challenge** is a technology-independent problem or failure family worth evaluating.

A Challenge must be meaningful before a technology is mapped to it. It may originate from a public use case, a reference failure family, a deployment-owner problem, a reduced mathematical case or another bounded source.

The Challenge definition should state, at minimum:

- task / mission;
- receiving decision or commitment;
- decision owner;
- material world facts and assumptions;
- authority/admissibility boundary;
- observable and hidden facts;
- action library and null/fallback action;
- sufficient-quality criterion;
- material-violation definition;
- useful response/evaluation horizon;
- acceptance policy or the information needed to construct it.

The Challenge is then instantiated as a **bounded scenario, fixture or reduction**. A reduction may simplify the narrative or state space only if it preserves the relation needed for the stated claim.

## 4. Technology mapping

Before traversal, map the exact technology/version/configuration to the Challenge.

The mapping separates three things that must not be conflated.

### 4.1 Preserved correspondence / kernel

Record which Challenge objects, relations, events, observations, authority conditions, charges, latency and outcomes are preserved.

Calling the relation an **isomorphism** requires the applicable preservation obligations to be established. Otherwise state the actual relation, for example:

- parameterized correspondence;
- one-way simulation;
- homomorphic / projected relation where proved;
- analogy with pending obligations;
- new reduction with no inherited kernel.

Narrative similarity is not isomorphism.

### 4.2 Parameter changes

Record changes that preserve the basic mechanism but alter effective conditions, such as:

- cost / price;
- latency;
- search radius;
- network topology;
- initial information;
- source availability;
- capacity;
- human availability;
- physical or token budget;
- deadline / freshness window.

These changes may alter the attainable region and must not be hidden inside “the same technology.”

### 4.3 Additional mechanisms

Record genuinely additional mechanisms or information sources separately.

For each additional mechanism, state:

1. operation and legitimate invoker;
2. information source, producer, scope, recipient, version and validity;
3. transition/effect change;
4. producer/use cost, latency, queue and maintenance;
5. interaction with other mechanisms;
6. authority implications;
7. what observation or route it can make newly reachable.

The traversal uses the **complete mapped configuration**: preserved correspondence plus declared parameter changes plus additional mechanisms.

## 5. Route and outcome space

DDS uses route/outcome classes rather than requiring one universal scalar.

### I — high-value admissible region

`I = {I_1, I_2, …}` contains routes that satisfy the high-value / sufficient-quality objective of the Challenge.

A provider-side DDS may deliberately select a Challenge relevant to a capability the studied technology plausibly contributes. However, **I is defined by the Challenge outcome, not by the identity of the mechanism that reaches it**. A peer reaching the same I route receives full credit.

### M — market/reference admissible region

`M = {M_1, M_2, …}` contains legitimate reference outcomes. M may represent a documented conventional route, one or more market-reference configurations, or another admissible lower-value result.

M is **not a default**. The evaluated system must still discover, select or complete it.

A DDS may use several M routes rather than a single strong peer. A strong peer may additionally be used as a comparison control under 00D/DBC rules.

### P — prohibited/material-violation region

`P = {P_1, P_2, …}` contains materially prohibited or incorrect outcomes.

Different P classes may represent different failure mechanisms or severities. Examples include false continuation, unauthorized execution, stale-basis action, dependency collapse or another Challenge-defined violation.

### Ø — incomplete / no-sufficient-route

Ø records failure to reach an admissible sufficient route because time, budget, evidence, capacity or search is exhausted.

Ø is not automatically Risk. It may reduce Effectiveness or completion. It enters Risk only if the Challenge explicitly defines that incompletion as a material violation.

## 6. Segments, gates, traversals and traces

These terms are distinct.

- **Segment** — a unit of search, observation, action or transition.
- **Gate** — a decision/validation boundary over a partial history.
- **Traversal** — an analytical, virtual or executed passage through the configured route/gate model.
- **Trace** — the recorded realized history of one traversal/execution.
- **DDS implementation profile** — one concrete mapping of the DDS method to a Challenge + technology/configuration.
- **DDS battery / campaign** — a preregistered set of profiles/traversals/executions used to estimate or compare results.

A gate need not correspond to one segment. A gate may cover one operation, a bundle of evidence, or thousands of candidate segments.

A gate also need not be binary. Depending on the Challenge it may:

- continue toward I;
- continue toward M;
- expose/block a P class;
- trigger renewed search;
- request evidence;
- requalify;
- escalate;
- pause;
- resume;
- terminate at Ø.

Probability, transition and observation laws may be defined per segment, group of segments or gate.

A trace should preserve, where material:

- observations and source/provenance;
- decisions;
- route/gate state;
- authority;
- cost/charges;
- timing;
- messages/handoffs;
- human involvement;
- irreversible effects;
- final I/M/P/Ø classification.

Private evaluator/oracle state must not be leaked to the participant merely because the evaluator uses it to adjudicate the trace.

## 7. DDS trace accounting

A DDS profile may use full or reduced accounting. An unscored dimension is **not zero**.

### 7.1 Cost

For trace `τ`:

[
C(τ)=sum_g c_g(τ)
]

where the declared ledger may include:

- search/exploration;
- validation;
- evidence production and consumption;
- compute/tokens;
- external calls;
- communication;
- latency;
- human review;
- coordination;
- implementation/maintenance where in scope;
- repeated/recovery work.

Aggregate Cost is defined before execution: expected cost, hard ceiling, percentile, total campaign cost or another explicit rule.

Commercial engagement fees are never the technical `C`.

### 7.2 Risk

The simplest DDS risk is:

[
R=P(τin P).
]

Where P classes have declared different material severity:

[
R=sum_j P(P_j)L_j
]

or another preregistered loss/risk function may be used.

A failed gate, HOLD or Ø outcome is not automatically Risk. Risk attaches to the material violation defined by the Challenge.

### 7.3 Effectiveness

The simplest DDS effectiveness is:

[
E=P(τin I).
]

Where several I routes carry different declared value:

[
E=sum_k P(I_k)v_k
]

may be used if the value weights are frozen before result inspection.

M remains admissible reference performance unless the Challenge states otherwise. Ø normally reduces completion/effectiveness.

## 8. Acceptance

For the common C–R–E profile:

[
mathcal A_{b,delta,p}
=
{(C,R,E): Cle b,;Rledelta,;Ege p}.
]

A trace does not itself “pass the DDS.” Traces generate evidence. The evaluated technology/configuration/campaign is then classified against the frozen acceptance policy as:

- **inside acceptance**;
- **outside acceptance**;
- **not established / insufficient evidence**.

Other acceptance functions are allowed when the Challenge requires them, but they must be frozen and reproducible.

## 9. Business Value projection

Effectiveness is a technical/test-layer concept.

A deployment-facing DDS may map the meaning of reaching one or more I routes into bounded **Business Value**, such as:

- process completion;
- throughput;
- continuity;
- avoided downtime;
- decision quality;
- recoverability;
- reduced human review;
- time-to-value;
- another frozen operating objective.

The `E → Business Value` mapping and its assumptions must be explicit and traceable.

Business Value does not replace or retroactively rewrite the technical result.

The management-facing deployment view may therefore be reported as:

[
(BV,;R,;C).
]

This is not a claim about total company ROI or universal product value.

## 10. DDS profile coverage

There is one DDS method. Concrete implementations may instantiate all or only part of it.

A profile must declare coverage for:

| DDS surface | Required declaration |
|---|---|
| Challenge / frozen scenario | used / inherited / not used |
| Technology mapping | full / partial / documentary |
| Preserved correspondence | proved / parameterized / one-way / analogy / none |
| Additional mechanisms | enumerated / none / pending |
| I/M/P/Ø route model | full / reduced / collapsed |
| Segment/gate model | deterministic / probabilistic / documentary / other |
| Trace/oracle | defined / executed / pending |
| Cost | scored / descriptive / unscored |
| Risk | scored / descriptive / unscored |
| Effectiveness | scored / descriptive / collapsed / unscored |
| Acceptance policy | quantitative / binary / qualitative / pending |
| Business Value projection | defined / not applicable / pending |
| Evidence mode | documentary / analytical / virtual / sandbox / live / matched / replicated |
| Reproducibility | source pins / fixture / harness / traces / DOI as applicable |

A **simplified DDS profile** is therefore not another method. It is a DDS implementation profile that deliberately uses a reduced coverage set.

Evidence maturity and DDS coverage are orthogonal. A profile may cover many DDS surfaces only virtually, while a simpler profile may have stronger executed evidence.

## 11. Current profile mapping

The table below is a **classification aid**. It does not modify the cited artefacts or transfer evidence among them.

| Current artefact / family | DDS profile reading | Cost | Risk | Effectiveness / I-vs-M | Acceptance | BV projection | Evidence state |
|---|---|---:|---:|---:|---|---|---|
| 00E–00J positive/negative technology trajectories and their product profiles | Simplified DDS profiles: Challenge + technology mapping + quality gates + positive/negative routes | generally unscored | primary / branch-specific | generally collapsed into legitimate continuity / expected outcome | binary / gate-based | not part of frozen route | documentary / symbolic / fixture-specific as individually stated |
| 00I AWS ordinary → defended → same frozen defended-under-drift trajectory | Simplified DDS profile with strong continuity and drift controls | unscored as DDS C | stale/prohibited action is primary | I/M not separately priced/scored | gate-based | not part of frozen route | design / fixture evidence as stated by 00I |
| R01 core | Rich probabilistic DDS reference profile | explicit | explicit | explicit I/M/P and sufficient-delivery `s` | quantitative `A_{b,δ,p}` | optional downstream projection | mathematical / virtual / harness stages separately stated |
| R01 technology-extension protocol | DDS-compatible extension discipline | explicit | explicit | explicit | quantitative | not intrinsic | protocol / proof / traversal stages |
| Human escalation + whispering | Rich DDS implementation profile over R01: kernel mapping + additional mechanisms + stochastic C/R/E + R1/R2/R3 | explicit virtual ledger | explicit `r` | explicit `s`, X/Y/M and incompletion | quantitative | not yet defined | virtual/analytical; no real integration/campaign |
| DBC | Optional DDS evidence/adjudication companion | burden vector | branch-specific outcomes | value/continuity gates as preregistered | hard gates + comparative rule | may consume deployment value rule | evidence ladder DBC-EL# |
| 00D | Optional DDS comparator contract | matched burden | measured outcome | matched outcome | preregistered comparison | not intrinsic | benchmark design / execution as stated |

### 11.1 Frozen simplified profiles

Frozen positive/negative technology traversals are **not rewritten** merely to add richer DDS accounting.

If a later study wants to add, for example:

- explicit I and M routes;
- verification Cost;
- stochastic search segments;
- multiple P classes;
- a Business Value projection;

that work is a **new DDS successor/profile or extension** referencing the frozen traversal as its base. Historical results remain intact.

## 12. R01 as the rich reference instantiation

R01 already contains the main machinery needed for a full DDS trajectory study:

1. fixed problem `x`;
2. task, mandate, world law, sufficient quality, horizon and violation definition;
3. technology manifest `θ_t`;
4. admitted strategy family;
5. I/M/P route semantics;
6. explicit costs and budgets;
7. risk and efficacy/effectiveness;
8. accepted region;
9. isomorphic-kernel review before additional mechanisms;
10. virtual R1/R2/R3 traversals;
11. oracle/harness/campaign separation.

DDS generalizes the **method shape**, not R01's theorem.

A DDS profile outside R01 does not inherit R01 mathematical results merely because it uses I/M/P, C/R/E or similar gates.

## 13. Technology extensions

A DDS technology extension should proceed in this order:

1. explain why the technology could matter for the Challenge;
2. identify preserved correspondence and its proof status;
3. isolate parameter changes;
4. inventory additional mechanisms and information;
5. define composition/interactions;
6. define I/M/P/Ø route space;
7. define segments, gates and probability/observation laws;
8. define trace ledger and C/R/E rules;
9. freeze acceptance policy and falsifiers;
10. traverse the complete mapped configuration;
11. only then execute harness/campaign stages when evidence access permits.

The current R01 technology-extension protocol remains the controlling source for R01-specific isomorphism, bounds and acceptance mathematics.

## 14. Human escalation / whispering profile status

The current Human Escalation / Whispering study is already substantially richer than the simplified technology traversals:

- it separates the isomorphic/preserved part from new information and pause/human mechanisms;
- it models the detect → escalate → pause → human resolution → resumption → delivery chain;
- it defines probability `q`, full cost `h/C_H`, risk `r`, efficacy `s`, deadlines and an accepted region;
- it includes positive controls and frozen R3 changes.

Its remaining DDS completion questions are primarily:

- normalize the current X/Y/M/V/incomplete outcomes to an explicit DDS I/M/P/Ø profile without changing the R01 source semantics;
- declare any market/reference M_j interpretation if used beyond the R01 M route;
- state the exact DDS trace schema generated by the future harness;
- define any deployment-specific `E → BV` projection only when a concrete deployment owner/problem exists;
- execute/calibrate a real technology implementation before making empirical claims.

## 15. Differential contribution

DDS does not require the studied technology to “win.”

A Differential Contribution Finding may establish that, under the frozen Challenge and profile:

- a technology makes one or more I routes newly reachable;
- it reaches the same I/M region at lower Cost;
- it reduces P-class Risk while preserving Effectiveness;
- it preserves value under a change that defeats the reference configuration;
- a market/reference M route already closes the problem at equal or lower burden;
- no material differential is established;
- evidence is insufficient.

A strong conventional or market-reference solution receives full credit.

## 16. Evidence and claim boundary

The following are different claims and must remain separate:

- mathematical proof;
- documentary technology mapping;
- virtual traversal;
- deterministic/symbolic execution;
- controlled harness execution;
- real API/product execution;
- matched comparative campaign;
- independent replication;
- deployment Business Value interpretation.

No later layer is implied by an earlier one.

This profile does not establish that:

- a named technology passes any Challenge;
- DDS is a certification or assurance scheme;
- the current simplified profiles become full C–R–E studies retroactively;
- R01 results transfer automatically to another Challenge;
- a Business Value projection is valid without a frozen deployment meaning for I;
- any standards body has adopted DDS.

## 17. Minimum citation rule

Future DDS implementation profiles should link this document and state, in one compact block:

~~~text
DDS profile:
Challenge / scenario:
Technology / version / configuration:
DDS surfaces used:
DDS surfaces unscored / collapsed:
Evidence mode:
Acceptance rule:
Base/frozen artefact:
Successor/extension status:
~~~

That block is sufficient to show which part of DDS is being used without inventing an ad hoc test vocabulary.

## 18. Source relationships

- [Ecosystem Awareness router](./README.md)
- [Canonical corpus manifest](./baseline/CANONICAL_CORPUS_MANIFEST.md)
- [Decision Boundary Challenge v0.2](./DECISION_BOUNDARY_CHALLENGE_v0.2.md)
- [00D canonical benchmark v0.2](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md)
- [R01 README](./baseline/reductions/00G-R01/README.md)
- [R01 technology extension protocol](./baseline/reductions/00G-R01/feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md)
- [Human escalation / whispering](./baseline/reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md)
- [00I Semantic TOCTOU](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_DRAFT.md)
- [00I AWS implementation profile](./baseline/00I_A01_AWS_STEP_FUNCTIONS_RDS_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md)

---

**Working status:** v0.1 defines the common DDS technical profile and classification vocabulary. It does not modify frozen source artefacts. Future profiles should cite it and declare their coverage rather than create parallel test taxonomies.
