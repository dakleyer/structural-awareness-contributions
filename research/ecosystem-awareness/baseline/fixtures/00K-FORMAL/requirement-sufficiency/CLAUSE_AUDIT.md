# A23 clause circularity audit and reconstruction

**Review:** begun 25 September 2026 Europe/Madrid; recorded after midnight, 26 September (25 September UTC). **Audited parent:** [`aff0c3787d0b8ee5915a2fcde8ea0be5cecbbd9e`](https://github.com/dakleyer/structural-awareness-contributions/commit/aff0c3787d0b8ee5915a2fcde8ea0be5cecbbd9e). **Source:** [canonical S1–S14 / T1–T4, §§2–3](../../../00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md). The canonical text and the six P functions are preserved; the requirement projections and the claims based on them are corrected.

## 1. Confirmed original defect

Direct evaluation over the original **65,536 states** confirmed nine logical equivalences, including reordered expressions:

| Target | Old clause names individually equivalent to the target |
|---|---|
| P3 | `s5_no_false_permission`, `t3_response_not_evidence` |
| P4 | `t3_authorized_response` |
| P5 | `s10_material_change_path`, `t1_material_break_visible`, `t2_changed_basis_carried`, `t4_requalification_timely` |
| P6 | `t2_composition_qualifiers_preserved`, `t4_nonmonotone_composition` |

The audit brief correctly identifies circular evidence but understates the duplicate set. A source clause may legitimately share an intended principle; equivalence alone is not a defect in the canonical requirement. The defect was presenting these particular translations as independent multi-clause evidence without establishing their fidelity. Existing anchor-only negative controls did not test this.

The brief also understates T4: its canonical text expressly includes non-monotone composition, contradiction treatment and incremental burden. Those obligations require visible effects; they do not assert `dependency_independent and compatibility_preserved`. P1/P2 had no equivalent individual clauses, but that fact alone does not prove full source fidelity.

## 2. Source-to-field map

All added fields are independent inputs. No field is calculated from `p1`–`p6`. They represent abstract observations or obligations, not externally verified real-world evidence. Functions are **partial clause projections**, not executable certification of every source sentence.

| Source / function | Meaning represented | Deliberate limit |
|---|---|---|
| S14 `s14_evidence_to_decision` | `evidence_fit`: evidence supports the receiving proposition. | Does not encode all transitions, arbitration, expiry or re-entry. |
| T2 `t2_qualified_residual` | `residual_explicit`: material unresolved state is carried. | Owner/privacy/expiry dimensions are not all represented. |
| S5 `s5_residual_nonpermission`, `s5_no_false_permission` | `permission_from_uncertainty` records the prohibited conversion of incomplete/conflicting/stale facts into permission; the residual clause additionally preserves explicitness. | This does not equate every action under uncertainty with false permission. Propagation containment and safe-state execution still need typed transitions. |
| S3 `s3_bounded_escape` | `fallback_defined`: a bounded escape/fallback exists. | Trigger, owner and oscillation semantics need richer states. |
| S4 `s4_human_capacity_surface` | `deadline_viable`: human path remains useful in time. | Retained only as the original insufficient anchor control. |
| **T3 `t3_bounded_authorized_response`** | For an executing non-neutral response: `response_authorized` and declared failure, reversibility, externalities, downside and null action. A `strong_response_claimed` additionally requires `no_worse_than_null`. | `no_worse_than_null` stands for a supplied certificate of the per-admissible-state comparison; this Boolean model does not calculate utilities or prove PNI. Non-executing/default/hold categories, deadline, re-entry and anti-oscillation need a typed trace model. One function is reused in R3/R4, never authority-field or P3 formula substitution. |
| S1/S6/S8 | Current+scoped authority; receiver verification; non-amplification, each conditional on execution. | Partial authority projection, with no claim of cryptographic verification. These three clauses jointly yield the retained P4 formula. |
| S10 `s10_material_change_path` | A material change must be detected (`material_break_detected`) and its required confirmation/revalidation/cancellation/authority-change disposition recorded (`change_disposition_recorded`). | Records the obligation; does not invent an enforced actuation interlock. |
| T1 `t1_material_break_visible` | Actual material change implies recognition. | Declared coverage, false positives and sensor distinguishability are not fully modelled. |
| T2 `t2_changed_basis_carried` | `changed_basis_carried`: the receiving owner gets the changed basis. | Does not replace this with successful requalification. |
| **T4 `t4_viable_requalification`** | Bounded effort, useful horizon, declared cost ledger and decision relevance of expansion. Active composition additionally requires `composition_effects_declared`. | Finite Boolean projection of timing/capacity/value, not measurement. Fallback is separately represented by S3 in R2. The same function is used in R2/R5/R6. |
| S9 `s9_non_substituting_composition` | Active composition does not promote dependent records as independent support (`dependent_support_promoted=False`). | Does not demand that all available records be independent. Principal hierarchy and every composition failure are not represented. |
| S11 `s11_cross_domain_coupling_preserved` | Required compatibility/coupling information is preserved. | Does not assert every pair of real-world demands is mutually satisfiable. |
| T2 `t2_composition_qualifiers_preserved` | Dependency qualification reaches the receiver (`dependency_qualifiers_carried`). | Preservation is distinct from independence itself. |

Adding an unrelated conjunct to a copied Pi could evade a mere non-equivalence test. The stronger guard also rejects **any individual clause that alone entails its target**, and requires each clause to be satisfiable and falsifiable. This guard is appropriate for the claimed compositional certificate; it is not a universal rule that legitimate requirements may never directly anchor a principle. T1 still overlaps S10, so the bundles are not claimed minimal or wholly irredundant.

## 3. Exact exhaustive result

The 16 original fields cannot express the distinct T3 response and T4 cost/effect obligations. The revised model has **33 independent Boolean fields** (8,589,934,592 unconstrained assignments). The restricted-expression audit proves each predicate uses only listed fields and exhaustively enumerates their union for each check. Every projected row covers all valuations of omitted fields. No reachability constraint is assumed, and no claim is made to have iterated 8.6 billion rows literally.

| Target | Projected rows checked | Rows satisfying R | R and not P | Result |
|---|---:|---:|---:|---|
| P1 | 8 | 1 | 0 | Implication in this projection |
| P2 | 256 | 3 | 0 | Implication in this projection |
| P3 | 4,096 | 518 | 3 | Not entailed |
| P4 | 8,192 | 4,099 | 0 | Implication in this projection |
| P5 | 8,192 | 108 | 3 | Not entailed |
| P6 | 1,024 | 34 | 1 | Not entailed |

The **22 clause-to-target comparisons** each have a distinguishing witness and a clause-true/target-false witness in the [certificate](./clause_audit_certificate.json). Three full-state counterexamples are replayable. Counts across different projections are not statistical rates or independent observations and must not be added as one full-state campaign.

## 4. Countermodels and adjudication

- **CAND-A23-P3:** explicit residual + no uncertainty-derived permission + declared authorized bounded response, but `unresolved_material=True` and `executes=True`. The unchanged P3 formula lacks the distinction between executing on an unresolved basis and executing a justified response to uncertainty. Determine the action/decision linkage before claiming a requirements gap.
- **CAND-A23-P5:** change detected, disposition recorded, changed basis carried and effort/horizon qualified, but the old action executes without requalification. Establish whether the canonical route's existing S10/S14 obligations already prohibit it and add a faithful transition/actuation mapping; do not define T1/T2/T4 as P5 again.
- **CAND-A23-P6:** correlated composition with dependency/coupling qualification preserved, no false independent corroboration and declared costs/effects. The unchanged P6 formula rejects any active correlated composition, which is stronger than the source S9 obligation. Determine the supported proposition and receiving disposition before changing requirements.

These candidates are registered in [Requirements-vNext](../../../00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md). They are **model-to-source/actuation bridge candidates**, not adopted requirements or proof of real canonical violations. No S15/T5/H7 is introduced. A23 remains under review; full closure requires semantic and reachability adjudication.

## 5. A25 and downstream scope

[A25 §6](../../../00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md#6-evidence-routes-and-conditional-transfer) now routes 00F/P3, 00H/P4 and 00G/P6 directly to their A3/A4/A6 implementations and positive/negative controls. Finite branch success does not transport to all admitted extensions without a separately proved base guarantee. X3/X4 express the required reflection/preservation assumptions; admission is not execution.

The brief's single-principle labels omit secondary principles: 00E and 00J profiles also depend on P3/P6 or P6; retaining P2/P1 alone does not preserve a full-family theorem. Transfer wording in all six extension profiles, A24/A26 and the index is therefore qualified at its dependency, while the six original scenarios, A1–A6 code, A19/A20/A22 and canonical requirements remain untouched.

## 6. Reproduction and editorial wording

~~~bash
PYTHONDONTWRITEBYTECODE=1 python audit_requirement_sufficiency.py --output replay.json
cmp clause_audit_certificate.json replay.json
PYTHONDONTWRITEBYTECODE=1 python -m unittest -v
~~~

Local result: certificate reproduced; **11 audit tests passed**. The passing status includes detecting the three expected gaps, not certifying all six implications. Local pytest is unavailable; fresh A3/A4/A6 regressions are left to the existing 00K CI campaign, with its exact run recorded in A12 after publication.

Suggested manuscript replacement (for the one sentence claiming all-six closure):

> A23's revised finite clause model supports P1, P2 and P4; P3, P5 and P6 remain under semantic review with explicit countermodels. For 00F, 00H and 00G, the extensibility evidence instead rests on the tested A3, A4 and A6 Route Q branches, without a guarantee over all admitted extensions.

## 7. Applied semantic follow-up

The [semantic bridge review](./SEMANTIC_BRIDGE_REVIEW.md) now checks the action-scope and corroboration distinctions and executes a candidate P5 transition interlock with positive controls and an interlock-removal mutation. It preserves this certificate and its three counterexamples. It is a bounded author review, not an independent review or all-six closure.
