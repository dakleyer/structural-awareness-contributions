# 00K-A02 — Requirements Coverage Matrix Addendum — v0.1

**Status:** supporting addendum to [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)  
**Purpose:** isolate the verified pre-ablation S1–S14 × 00E–00J coverage evidence for review and execution preparation.  
**Semantic authority:** this addendum does not redefine S1–S14, P1–P6 or any scenario gate. The section below is copied from the current 00K main document so the coverage evidence can be reviewed independently.

## 2A. Pre-ablation documentary coverage matrix

Before testing P1–P6, the corpus already provides a useful **requirements-necessity precursor**: the existing scenario quality plans state which S1–S14 requirements each gate depends on and what failure occurs when a gate is bypassed, absent or misapplied.

This matrix reorganizes that already-published material by requirement rather than by scenario. It is **documentary coverage, not execution evidence**.

### 2A.1 Method boundary

- **00E, 00F, 00H, 00I and 00J** expose requirement routes directly in their gate tables.
- **00G** declares the aggregate route **S1/S2/S3/S6/S9/S11/S14 → T1/T2/T3/T4 → H2/H3/H4/H5/H6**, while its Q0–Q5 register expresses the evidence/failure semantics gate by gate without repeating the S# route in every row. The matrix therefore marks 00G coverage from that aggregate declaration rather than pretending each individual row contains a separate S# annotation.
- **00J S2/S3/S4 are conditional extensions** when the fixture explicitly introduces preference fidelity, regime/exception or finite human dispute review. The base Q0–Q5 route already supplies the coverage listed below without relying on those optional branches.
- A checkmark means the current published scenario uses the requirement in its declared gate/route. It does not mean an executable test has been run.

### 2A.2 S1–S14 × reference-scenario matrix

| Requirement | 00E | 00F | 00G | 00H | 00I | 00J | Published failure pressure if the requirement is absent/misapplied |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **S1 — Authority provenance/current applicability** |  | ✓ | ✓ | ✓ | ✓ | ✓ | Identity, signature, transport or a locally valid grant can be treated as authority for a decision/scope it does not currently govern. |
| **S2 — Preference fidelity/reviewable decision basis** | ✓ |  | ✓ | ✓ |  | △ | A fluent/attractive/generated option or grouped finding can advance without demonstrating that it still represents the relevant principal/basis. |
| **S3 — Regime/context/escalation/bounded escape** | ✓ | ✓ | ✓ |  | ✓ | △ | A changed frame is missed, or uncertainty opens an unbounded escalation/escape path instead of bounded requalification. |
| **S4 — Human-inclusive oversight authority/capacity** | ✓ | ✓ |  |  |  | △ | Humans are repeatedly queried, unavailable or overloaded; nominal approval/capacity is mistaken for effective oversight. |
| **S5 — Operational indeterminacy/containment** | ✓ | ✓ |  |  | ✓ | ✓ | Known unresolved, stale or conflicting state can become permission/certainty, or containment becomes blanket/unbounded. |
| **S6 — Privacy-preserving trust handoff** | ✓ | ✓ | ✓ |  |  | △ | Scope/provenance/qualification can be lost across systems; access or transport validity can be promoted into a stronger trust/rights conclusion. |
| **S7 — Identity/representation link** |  |  |  | △ |  | ✓ | A technical actor, registry identity or leaf worker can be mistaken for the principal/rights holder it represents. |
| **S8 — Bounded subdelegation/non-amplification** |  |  |  | ✓ |  | △ | Valid leaf grants can manufacture authority absent at the root; purpose/scope/time limits amplify across delegation. |
| **S9 — Multi-principal composition/non-substitution/conflict** | ✓ | ✓ | ✓ | △ | △ | ✓ | Locally valid claims/postures can substitute for one another, dependent repetition can become corroboration, or one common-root campaign can be misclassified. |
| **S10 — Commitment/material change** | ✓ | ✓ |  |  | ✓ | △ | A previously correct commitment/decision can survive material change and execute from a stale basis. |
| **S11 — Policy/objective integrity across domains** | ✓ | ✓ | ✓ | ✓ | △ | ✓ | Source/version/scope/dependency or cross-domain policy relations can be flattened, overwritten or silently disappear. |
| **S12 — Accountability/challenge/repair** | ✓ | ✓ |  | △ | △ | ✓ | The system cannot reconstruct why a state/action occurred or repair future state without losing the historical basis. |
| **S13 — Authority history vs intervention history** |  |  |  | △ | △ | △ | A later approval/intervention can overwrite or launder the original authority/provenance history. |
| **S14 — Evidence-to-decision assessment** | ✓ | ✓ | ✓* | ✓ | ✓ | ✓ | Evidence may exist without an explicit statement of what it proves for the current decision; timeout, approval or repeated records can force unsupported closure. |

`✓` = base/current route coverage. `△` = variant/extended/conditional coverage. `✓*` for 00G denotes aggregate-route coverage as described above.

### 2A.3 Coverage findings

The union of the six current scenario routes covers **all fourteen requirements S1–S14**. No S# is absent from the six-scenario corpus.

Two requirements are especially cross-cutting:

- **S14** appears in all six scenario routes; in 00E/00F/00H/00I/00J it is explicitly repeated throughout the detailed gate routes, while 00G carries S14 in its aggregate canonical route and implements the evidence→decision distinction throughout Q0–Q5.
- **S9** is exercised across all six scenario families when base plus declared hardened/extended branches are considered; in 00H and 00I it is activated by the composition/history variants rather than being required by every base branch.

This is stronger than saying that the requirements were written after the scenarios. The quality plans already contain the two ingredients needed for an ablation pre-registration:

1. **requirement route** — which S#/T#/H# a gate needs; and
2. **failure-if-bypassed semantics** — what concrete bad outcome becomes reachable if that gate does not hold.

The six-principle ablation below therefore does not invent new failure mechanisms. It chooses one existing requirement anchor and one existing failure route for each removed principle.
