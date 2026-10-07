# DDS — Typed output validation and semantic receiving controls

Documentation 0.2 · 7 October 2026 · complete within the declared local Stage-A question.

## Finding and decision

A receiver can reject malformed structure and constrain selected integration fields while preserving a separate decision about applicability and correctness. Schema-valid content can be wrong, unauthorized or inapplicable. The cases do not measure model schema-adherence probabilities, language quality or real API latency.

The test supports local compositional feasibility and explicit failure limits. It does not establish superiority, a product-wide conclusion or deployment ROI. The [extension](./EXTENSION.md) supplies the two review steps and mechanism/producer/interaction map. The [candidate specification](./CANDIDATE_SPECIFICATION_PACKAGE.json) identifies what a future realization would need to satisfy.

## Registered scope and evidence

**Object/base:** STRUCTURED-OUTPUT-BOUNDED-RECEIVER-0.1. **Runtime/evidence:** actual Pydantic2.13.5 strict selected BaseModel plus JSON duplicate-member pre-parser and SQLite receiving state; no LLM/API generation or full JSON-Schema conformance test. Inputs and environment law are registered before execution in the [Card](./CURRENT_RUN_CARD.json), with the [actual-byte Freeze](./CURRENT_FREEZE.json). The [current run](./runs/2026-10-07-03/RESULTS.json) passes 10 named-world expectations and 2 separate deliberate Type1/Type2 sensitivity controls. Expected negative and P outcomes are retained.

| Case | Human/process scenario | Observed | Prior M in G | C selected units | Qualified excess / signed gap to G |
|---|---|---|---|---:|---:|
| S01 | A purchasing receiver validates a typed record and applies its admitted tenant-a amount. | I | True | 6 | 0 |
| S02 | The generator/input fixture returns amount as text; strict selected typing must reject coercion. | Ø | False | 2 | unavailable |
| S03 | An unrequested command field appears in an otherwise typed output. | Ø | False | 2 | unavailable |
| S04 | The required currency is absent. | Ø | False | 2 | unavailable |
| S05 | Two amount members occur in the JSON wire; preparse duplicate-member rejection is required. | Ø | False | 1 | unavailable |
| S06 | The output is schema-valid for tenant-b but the receiving operation belongs to tenant-a. | Ø | False | 4 | unavailable |
| S07 | An admitted but false policy source supplies limit9999, and schema-valid output repeats it; factual correctness is not established by typing. | P | False | 6 | unavailable |
| S08 | The upstream fixture reports a refusal; the owner admits a recorded manual-review deferment. | M | True | 3 | 0 |
| S09 | The wire is incomplete; the owner admits a recorded deferment rather than fabricated completion. | M | True | 3 | 0 |
| S10 | The typed record is valid but current operation authority is revoked. | Ø | False | 4 | unavailable |

Instrument assertion PASS does not mean all scenarios were delivered. Outcomes here are {"I": 1, "Ø": 6, "P": 1, "M": 2}. The scenarios are authored examples, not a representative population.

## Cost, diagnostics and acceptance

Cost is the sum of the frozen selected actual SQLite API and policy-entry units (weight1), including commit/rollback. Candidate, setup and evaluator entries are separated. Current total candidate units **33**, with every component/trace in the run. Money, tokens, real staffing/network/service times and lifecycle remain unscored, not zero. These heterogeneous units are not a cross-technology ranking.

Private minimum_G is exact only within the two frozen qualifying/reference procedures. The raw run field `excess` is a signed arithmetic gap; [current cost interpretation](./COST_INTERPRETATION.json) credits excess work only for legitimate I/M closures. A negative gap from an incomplete/incorrect trace is not efficiency. The actual witness is meaningful and uses the same actor information/interfaces. The global accessible-information lower bound is not established. Missing legitimate closure witnesses yield unavailable minima; cheap P/Ø traces are not credited as efficiency.

The [M-admission map](./runs/2026-10-07-03/M_ADMISSION_BEFORE_CANDIDATES.json) is sealed before candidate evaluation. Type1 is **0/3** eligible named traces; Type2 is **1/10** registered named traces under the declared causal rule. No P enters the Type1 numerator. Excess alone is not Type1. Raw P is not automatically Type2. Two deliberate fault controls are separately reported, never pooled as product performance. No population estimate or statistical confidence interval is claimed.

Acceptance is the registered scoped expectation/falsifier contract, not native/global deployment acceptance. Positive continuity, malformed/scope/currentness boundaries, expected material violations and control sensitivity all retain their specified results.

## Baseline, residual risk and conditional business value

Native mechanisms are credited according to their documented scope. The same-information conventional qualified/reference procedures can close legitimate cases; no superiority over them is established. The example value is **A receiver can reject malformed structure and constrain selected integration fields while preserving a separate decision about applicability and correctness.**

Residual limits: Schema-valid content can be wrong, unauthorized or inapplicable. The cases do not measure model schema-adherence probabilities, language quality or real API latency. Source/authority authenticity, real availability, independent review, native integration, monetary burden, wider action spaces and distributional transfer remain conditional. A material change to source/permission/timing/effect contract needs explicit requalification and, when result-producing, a prospective successor.

## Current coverage, closure and delivery

Challenge/configuration, scenario explanations, Step 1 correspondence/transfer limits, Step 2 producers/burden/interactions, selected route/effect/cost/type controls, acceptance, bibliography, reproducibility, business interpretation and residual limits are present. This is a declared **Simplified Stage A** record. B requires a separate architecture-to-frozen-spec verification package; C requires admitted pinned-implementation/effect validation. Neither is inferred from this execution.

The selected technical question is closed with an evidence-bounded answer. The technical record is this report and its reproducible dossier; fees, Sponsor/seal, DOI, international submission and commissioned long reports retain their separate existing states. No SOW output or fee is added or waived.

Reproduce with the registered runtime: `python -B current_study.py --output <fresh directory>`. [Current status](./CURRENT_STUDY_RECORD.json) is the live reading record; old Cards/results retain their registered identity and dates.

