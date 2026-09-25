# 00K — Six-Principle Sufficiency & Adversarial Ablation Test — v0.1 Draft

| | |
|---|---|
| **ID** | 00K |
| **Type** | Principle sufficiency test · adversarial leave-one-principle-out reconstruction · requirements traceability |
| **Status** | **Working draft / executable symbolic milestone** — all six first-pass ablation harnesses executed; no live product/runtime validation |
| **Date** | 25 September 2026 |
| **Owner corpus** | Ecosystem Awareness |
| **Primary dependencies** | [00 — Canonical Requirements](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) · [02 — Epistemic Safety Principles & Control Matrix](./02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part01.md) |
| **Reference scenarios** | [00E](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) · [00F](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) · [00G](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) · [00H](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md) · [00I](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) · [00J](./00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) |
| **Supporting addenda** | [00K-A01 — reviewed pre-principle-first design](./00K_A01_REVIEWED_PRE_PRINCIPLE_FIRST_DESIGN_ADDENDUM_v0.1.md) · [00K-A02 — requirements coverage matrix](./00K_A02_REQUIREMENTS_COVERAGE_MATRIX_ADDENDUM_v0.1.md) · [00K-A03 — P4/00H deterministic paper execution](./00K_A03_P4_00H_PAPER_ABLATION_EXECUTION_v0.1.md) · [00K-A04 — six-principle symbolic execution summary](./00K_A04_SIX_PRINCIPLE_SYMBOLIC_EXECUTION_SUMMARY_v0.1.md) · [00K-A05 — bounded-grid hardening & P5 audit](./00K_A05_BOUNDED_GRID_HARDENING_AND_P5_AUDIT_v0.1.md) · [00K-A06 — P6 confound falsifier & isolation](./00K_A06_P6_CONFOUND_FALSIFIER_AND_ISOLATION_NOTE_v0.1.md) · [00K-A07 — P1 confound falsifier & matched-semantic isolation](./00K_A07_P1_CONFOUND_FALSIFIER_AND_MATCHED_SEMANTIC_ISOLATION_v0.1.md) · [00K-A08 — P2 strongest-repair & prefix-indistinguishability](./00K_A08_P2_STRONGEST_REPAIR_AND_PREFIX_INDISTINGUISHABILITY_v0.1.md) · [00K-A09 — P3 confound falsifier & matched-conflict isolation](./00K_A09_P3_CONFOUND_FALSIFIER_AND_MATCHED_CONFLICT_ISOLATION_v0.1.md) · [00K-A10 — P4 minimal authority basis & lineage refinement](./00K_A10_P4_MINIMAL_AUTHORITY_BASIS_AND_LINEAGE_REFINEMENT_v0.1.md) · [00K-A11 — P5 exhaustive material-basis ablation](./00K_A11_P5_EXHAUSTIVE_MATERIAL_BASIS_ABLATION_v0.1.md) · [00K-A12 — P6 transitive-dependency strongest-repair audit](./00K_A12_P6_TRANSITIVE_DEPENDENCY_AND_STRONGEST_REPAIR_AUDIT_v0.1.md) · [00K-A13 — six-principle serious-ablation completion review](./00K_A13_SIX_PRINCIPLE_SERIOUS_ABLATION_COMPLETION_REVIEW_v0.1.md) |

> **Purpose.** Test the **six operational principles themselves** as the primary sufficiency/necessity object. S1–S14 remain the observable specification layer that tells us what a sufficiently good route must demonstrate, but the ablation does **not** prove a principle necessary merely because a mapped S# falls. For each test, remove one principle, give the remaining five the strongest fair opportunity to redesign/recover the route using any available native technology/control mechanism, and ask whether the scenario can still pass its negative and positive controls **without reconstructing the removed principle's semantics**. If it can, the principle is not necessary as formulated. If every successful repair necessarily recreates the removed semantic invariant, that is evidence for principle-level necessity within this corpus.

> **Evidence boundary.** This document now has **complete first-pass deterministic symbolic execution coverage for P1–P6**, but it does **not** claim universal minimality, formal proof, live agent/product validation, or that Ecosystem Positioning is the only architecture capable of satisfying the principles. The executable harnesses remain small symbolic fixtures designed to make the branch logic falsifiable.

### Document stack and conservation rule

This file is the **current controlling 00K test design**. Supporting material is preserved rather than rewritten:

- [**00K-A01 — Reviewed pre-principle-first design addendum**](./00K_A01_REVIEWED_PRE_PRINCIPLE_FIRST_DESIGN_ADDENDUM_v0.1.md) is a **verbatim preservation** of the previously reviewed 00K state at commit `fcd63e4907039f967c70de67f1c73040d1b40050`. It retains the earlier mapping, ablation routes, acceptance criteria and coverage work exactly as reviewed; it is not silently re-authored to match this successor framing.
- [**00K-A02 — Requirements Coverage Matrix addendum**](./00K_A02_REQUIREMENTS_COVERAGE_MATRIX_ADDENDUM_v0.1.md) isolates the verified S1–S14 × 00E–00J coverage matrix so the documentary premise can be audited independently before any principle-level execution.

The addenda provide provenance, coverage and prior reviewed reasoning. They do **not** supersede this principle-first protocol.

**First execution annex.** [00K-A03](./00K_A03_P4_00H_PAPER_ABLATION_EXECUTION_v0.1.md) applies this protocol to **−P4 on 00H** using the already-frozen deterministic U/G/I/NM fixture. Its current paper-level result is **SEMANTIC RECONSTRUCTION / no TRUE SUBSTITUTE found in the documented repair set**.

That paper result now has a runnable companion: [**00K-A4 / P4–00H executable harness**](./fixtures/00K-A4-P4-00H/README.md). The original reviewed 11-test source remains preserved; the second reviewed package is preserved unchanged as [v0.2](./fixtures/00K-A4-P4-00H-v0.2/README.md) and independently reproduces **21/21** tests with NM, A2-L and the four-arm comparison. The active browsable harness preserves those reviewed layers, adds the U/G indistinguishability sweeps and bounded authority/volume grid, and has a **29-test** active regression surface. This is deterministic symbolic execution, not a live runtime/product benchmark.

**Second symbolic execution.** [00K-A5 / P5–00I](./fixtures/00K-A5-P5-00I/README.md) removes action-time material-change requalification from the Semantic TOCTOU fixture. Queue-time evidence, provenance preservation, conflict visibility and database serialization all leave the stale action executable; deny-all fails the continuity control. The original generation-only compare passes the first stale branch but is exposed by the bounded-grid audit as only a **partial** P5 repair. A full material-basis compare/binding passes generation-, incident-, freeze- and source/version-change branches and is classified as **SEMANTIC RECONSTRUCTION of P5**. Current hardened result: **14/14**, no TRUE SUBSTITUTE found in the tested repair surface.

**Complete first-pass symbolic coverage + adversarial supplements.** [00K-A04](./00K_A04_SIX_PRINCIPLE_SYMBOLIC_EXECUTION_SUMMARY_v0.1.md), [00K-A05](./00K_A05_BOUNDED_GRID_HARDENING_AND_P5_AUDIT_v0.1.md) and [00K-A06](./00K_A06_P6_CONFOUND_FALSIFIER_AND_ISOLATION_NOTE_v0.1.md) now give all six principles executable isolated harnesses: P1 corrected matched-semantic **42/42**, P2 matched-prefix strongest-repair **58/58**, P3 corrected matched-conflict **49/49**, P4 minimal-authority audit **76/76**, P5 exhaustive material-basis **47/47**, P6 transitive-dependency **74/74** — **346 core tests**. Supplemental P6 falsification/isolation and independent cross-scenario kernels add **33** tests, for **379 registered tests** overall. GitHub Actions [full campaign run](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36100046965) independently completes **all 10 jobs successfully**, including the historical aggregate **134/134** gate before P1 hardening; the current workflow/manifest are configured for **163** tests. The unmodified 00G P6 pair is deliberately preserved as a negative result because it admits an authority-only TRUE SUBSTITUTE; after controlling that confound, no TRUE SUBSTITUTE is found in the isolated core repair surfaces. The counts are regression coverage, not scientific scores.

---

## 1. Terminology and relation to the existing corpus

The current canonical name for **S1–S14 is “canonical requirements.”** Earlier documents may still contain the historical label “challenges”; the IDs and semantics are unchanged.

The six principle families below are an **ablation/test abstraction**, not a replacement normative register. They compact existing material from:

- the root epistemic principle and I0/I1/I2/O0/O1/O2 controls in 02;
- the paired received-signal controls E0-I/E1-I/E2-I/E0-O/E1-O/E2-O;
- the cross-cutting rule that a source is a source, not the ecosystem;
- the H1–H6 research hypotheses in 00; and
- the S1–S14 requirement semantics already used by 00E–00J.

The purpose of P1–P6 is therefore practical: create six removable architectural disciplines that can be tested directly.

### 1.1 Principle-first interpretation

For this document, the causal direction is intentionally:

`P1–P6 → observable obligations → S1–S14 / T1–T4 / KPIs → scenario gates`

The **principles are the object under test**. The requirements are how the corpus communicates, measures and audits their operational consequences.

Therefore:

- an ablation does **not** simply switch off one mapped S# and declare failure;
- the remaining five principles are allowed to use the full technology/control substrate and to satisfy the scenario in any alternative way they can find;
- S1–S14 are used to observe what has been preserved or lost, not to predetermine the answer;
- a workaround that closes the failure only by reintroducing the removed semantic invariant under another name counts as **principle reconstruction**, not as a successful five-principle substitute; and
- a workaround that genuinely closes both the negative and positive-control branches without that semantic invariant is a **counterexample** to the claimed necessity of the removed principle.

This converts the exercise from a requirement-coverage proof into an **adversarial reconstruction test**.

---

## 2. Six operational principle families

### P1 — Qualified determination and explicit residual

A system must distinguish what is sufficiently established, what is insufficient/inconclusive, and what remains outside the justified determination boundary. Evidence is always relative to a subject–proposition–decision scope; residual state must not disappear merely because a decision needs closure.

**Source basis:** I0/O0 + E0-I/E0-O; H1/H2.

**Unique ablation anchor:** **S14 — Evidence-to-decision assessment.**

---

### P2 — Bounded unresolved effort and viable oversight

Recognized uncertainty does not justify unlimited search, review, escalation, human waiting or context expansion. Determination effort must have a finite, decision-relevant stopping rule inside the useful response horizon and available capacity.

**Source basis:** I1/O1 + E1-I/E1-O; H1/H6.

**Unique ablation anchor:** **S4 — Human-inclusive oversight authority and capacity.**

---

### P3 — No false closure from unresolved state

Known unresolved, stale, conflicting or missing material state must not be converted into PASS/FAIL, permission or certainty-equivalent closure merely because the system needs to act, a timeout expires, a human approves, or several weak signals agree.

**Source basis:** I2 + E2-I; H1.

**Unique ablation anchor:** **S5 — Operational indeterminacy and containment.**

---

### P4 — Qualification-preserving authority basis

When authority/representation state crosses participants or systems, the relying decision must retain **or obtain** a current, receiver-verifiable qualification sufficient for the action being considered: legitimate authority source, purpose/scope/time, non-amplification limits and any other material qualifier needed by that decision. Preserved root/delegation lineage is one valid implementation; an authoritative scoped attestation/capability may also be sufficient where full history is not decision-material. A technically valid leaf or downstream record must not silently acquire stronger authority merely because the relying system cannot establish the authority basis for the composed effect.

**Source basis:** received-signal controls + cross-cutting source rule + H4 bounded preservation.

**Unique ablation anchor:** **S8 — Bounded subdelegation and non-amplification.**

---

### P5 — Material-change requalification at time of use

A decision that was correct when established must be requalified when a material condition changes before commitment or actuation. Technical validity of a token, job, API, cached verdict or prior approval does not prove that the original decision basis is still current.

**Source basis:** root dynamic-window principle + H5/H6.

**Unique ablation anchor:** **S10 — Commitment state, material change and normal escalation.**

---

### P6 — No local-to-ecosystem promotion or silent substitution

A locally valid determination, repeated signal, majority view, policy result or correlated set of observations must not become ecosystem truth outside its justified scope. Composition must preserve source dependence, independent evidence, conflicts and non-substitution among principals/domains.

**Source basis:** O2 + E2-O + H2/H3.

**Unique ablation anchor:** **S9 — Multi-principal composition, non-substitution and conflict.**

---

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


## 3. Principle-to-requirement traceability map

### 3.1 Mapping rule

Each S1–S14 requirement receives one **primary principle projection for traceability**, plus any supporting principles. This is a communication/measurement map, not the proof of necessity. The ablation test is deliberately allowed to ignore this primary assignment and search for alternative five-principle implementations.

The map is useful only if every P# has at least one requirement whose clearest operational meaning depends on that principle. But necessity is established only by the adversarial reconstruction test in §4–§5, not by the partition itself. If another five-principle design satisfies the scenario without recreating the removed principle, the mapping must yield to that evidence.

### 3.2 Primary mapping

| Canonical requirement | Primary principle | Supporting principles | Why the primary link is non-substitutable |
|---|---|---|---|
| **S1 — Authority provenance/current applicability** | **P4** | P5, P6 | Authority can only remain decision-usable across handoffs if issuer, scope, standing and applicability remain linked to the record being consumed. |
| **S2 — Preference fidelity/reviewable basis** | **P1** | P3, P6 | A preference or basis must be explicitly qualified for the receiving decision rather than inferred from fluency, recency or output similarity. |
| **S3 — Regime/context/escalation/bounded escape** | **P2** | P3, P5 | Escalation and escape must terminate under bounded conditions; otherwise recognized change becomes unbounded search or suspension. |
| **S4 — Human-inclusive oversight authority/capacity** | **P2** | P3, P5 | A nominal human is not a safety mechanism unless review is reachable, capacitated and timely. |
| **S5 — Operational indeterminacy/containment** | **P3** | P1, P2, P5 | Its decisive obligation is that unresolved/stale/conflicting state must not be converted into permission or certainty. |
| **S6 — Privacy-preserving trust determination** | **P4** | P1, P6 | Minimum disclosure is useful only if enough qualification survives the handoff for the receiver not to over-interpret the signal. |
| **S7 — Identity/representation link** | **P4** | P6 | The representation relation must survive across actors/instances; similar behaviour cannot substitute for lineage. |
| **S8 — Bounded subdelegation/non-amplification** | **P4** | P6 | Purpose/scope/time/hard limits must survive delegation; losing the root-to-leaf relation permits authority laundering. |
| **S9 — Multi-principal composition/non-substitution/conflict** | **P6** | P1, P4 | Locally valid determinations must not silently substitute for one another or be promoted to system-wide truth. |
| **S10 — Commitment/material change** | **P5** | P1, P2 | The defining obligation is requalification when the basis changes between recommendation/commitment and execution. |
| **S11 — Policy/objective integrity across domains** | **P6** | P4, P5 | Cross-domain policy/objective state must compose without silent overwrite, disappearing couplings or false consensus. |
| **S12 — Accountability/challenge/repair** | **P4** | P5 | Repair requires reconstructable provenance/history rather than a rewritten present that destroys the original basis. |
| **S13 — Authority history versus intervention history** | **P4** | P5, P6 | Original authority and later intervention must remain distinct linked objects; otherwise provenance is overwritten. |
| **S14 — Evidence-to-decision assessment** | **P1** | P2, P3, P4, P5, P6 | S14 is the explicit bridge from evidence to what it actually establishes for the current decision. Without that bridge, evidence can be present yet semantically insufficient. |

### 3.3 Coverage / uniqueness check

The primary map is a complete partition of S1–S14:

- **P1:** S2, **S14**
- **P2:** S3, **S4**
- **P3:** **S5**
- **P4:** S1, S6, S7, **S8**, S12, S13
- **P5:** **S10**
- **P6:** **S9**, S11

Every principle has at least one uniquely assigned traceability anchor. This makes the mapping discriminating, but it is **not** treated as causal proof. The five-principle repairer is still allowed to try to satisfy the same operational obligation by another route.

---

## 4. Principle-first adversarial ablation protocol

The operative test is a **strongest-repair test**, not a requirement-deletion exercise.

For each principle Pk:

1. **Freeze the scenario and oracle.** Keep the same facts, negative/positive branch, authority, action library, technology/control substrate, compute/token ceiling, communication budget, human capacity and deadline.
2. **Remove only the semantic invariant Pk.** Do not disable unrelated capabilities merely because they happened to be mapped to the same S#.
3. **Give P1–P6 minus Pk the strongest fair repair opportunity.** The repairer may redesign the route, invoke different native controls, reorder checks, use another strong-peer mechanism, and use any of S1–S14 as diagnostic guidance.
4. **Require branch correctness, not textual compliance.** The repaired system must pass the target negative branch **and** any matched positive/boundary control. A blanket HOLD, deny-all, accept-all or infinite-search strategy is not a repair.
5. **Attempt explicit substitutions.** For the removed Pk, test the most plausible substitutes from the other five principles and from existing native controls. Record what they can recover and the exact semantic gap that remains.
6. **Classify a repair as one of three outcomes:**
   - **TRUE SUBSTITUTE:** closes the critical route and preserves the positive control without recreating Pk's semantic invariant → evidence **against** Pk necessity;
   - **SEMANTIC RECONSTRUCTION:** closes the route only by implementing the same invariant under another mechanism/name → evidence that the **principle** is necessary but its implementation/name is not unique;
   - **FAILED SUBSTITUTE:** critical route remains reachable or the positive control is destroyed → evidence supporting Pk necessity.
   - **Invariant-lock rule:** the semantic invariant being removed is the P# statement fixed in §2 **before** the repair attempt. A reviewer classifying “semantic reconstruction” must cite the specific invariant clause that the substitute reintroduces; successful outcome alone is not sufficient to label a mechanism as reconstruction.
   - **Open repair frontier:** the repair attempts documented here are not exhaustive. A later mechanism that passes the same frozen negative and positive controls without reconstructing the removed invariant is a valid counterexample and must reopen the necessity claim.
7. **Use S1–S14 after the attempt as instrumentation.** Record which requirements/gates became unsatisfied, but do not use that fact as the causal proof.
8. **Restore Pk as a symmetry check.** Under the same frozen inputs, restoration should close the negative route while preserving the positive route.
9. **Credit simpler alternatives.** If a different architecture achieves the same branch-correct result at equal/lower burden without Pk semantics, the six-principle model loses that ablation.

### 4.1 Full-set sufficiency hypothesis

For the current six-scenario corpus, P1–P6 are a **sufficiency candidate** if there exists at least one implementation route for each 00E–00J fixture that:

- passes the scenario's negative and positive/boundary controls;
- satisfies the scenario oracle within its declared deadline/capacity;
- does not rely on hidden authority or omniscience; and
- reaches the applicable S/T/H/KPI gates without case-specific semantic exceptions.

This is the principle-level claim. S1–S14 are the specification/measurement projection of that claim.

### 4.2 Necessity-by-adversarial-reconstruction condition

Pk earns a **necessary-within-this-corpus** result only if the strongest system built from the other five principles cannot pass the selected frozen scenario **unless it recreates the semantic invariant of Pk**.

In compact form:

[
(P1…P6) \setminus P_k + \text{strongest fair repair}
\Rightarrow
\begin{cases}
\text{branch failure}, & \text{supports necessity} \\
\text{pass only by semantic reconstruction of } P_k, & \text{supports semantic necessity} \\
\text{pass without } P_k, & \text{falsifies necessity}
\end{cases}
]

The S# trace is then used to explain the observed consequence, not to manufacture it.

This is corpus-bounded necessity, not universal minimality.

---

## 5. Six one-principle ablation routes

The six ablations deliberately use **one different reference scenario each**. In every case the repairer is instructed to try hard to survive with the other five principles before any necessity claim is accepted.

### A1 — Remove P1: qualified determination / explicit residual

**Traceability anchor (not causal proof):** **S14 — Evidence-to-decision assessment**  
**Scenario:** [00J — Rights-Provenance Inversion](./00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md)  
**Existing failure route:** [00J §7.1 Route N](./00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md#71-route-n--quality-plan-exists-but-is-badly-implemented--gates-are-bypassed-or-misapplied)  
**Conforming comparator:** [00J §7.2 Route Q](./00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md#72-route-q--canonical-requirements-and-gates-correctly-implemented)

**Ablation.** Keep provenance transport, bounded search, anti-false-closure, material-change requalification and composition controls, but remove the obligation to state **what each record actually establishes for the receiving rights/enforcement decision**.

**Route reopened.**

1. Q0/Q1 may still contain valid creator, access and technical identity records.
2. At Q2, a valid `generated-by M1` record exists.
3. Without P1, the system has no mandatory evidence-to-decision sufficiency statement separating generation provenance from source/rights provenance.
4. Q3 can therefore admit a technically valid downstream RX record as if it established enforceable rights.
5. Q4 replication can make that unsupported conclusion operationally prominent.
6. Q5 reaches `LICENSE_REQUIRED/PAY/BLOCK` against the original author even though the stronger rights proposition was never established.

**Current strongest-repair assessment.** P2 can bound review; P3 can prevent closure on an explicitly marked UNKNOWN; P4 can preserve the records; P5 can refresh them; P6 can prevent correlated copies from becoming independent evidence. None of those, by itself, states **which proposition the available evidence is sufficient to support**. A rescue rule that adds that test has reconstructed P1.

**Restoration test.** Restore P1 only: Q2/Q3/Q5 must preserve the difference between generation provenance, source provenance, rights provenance and enforceable-rights evidence; unsupported enforcement returns to REQUALIFY/HOLD/no-conclusion rather than PAY/BLOCK.

---

### A2 — Remove P2: bounded unresolved effort / viable oversight

**Traceability anchor (not causal proof):** **S4 — Human-inclusive oversight authority and capacity**  
**Scenario:** [00E — 100 Million Tokens](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md)  
**Existing failure route:** [00E §8.1 Route N](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md#81-route-n--requirements-not-satisfied-for-the-run)  
**Conforming comparator:** [00E §8.2 Route Q](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md#82-route-q--requirements-satisfied-for-the-run)

**Ablation.** Preserve explicit uncertainty and all provenance, but remove the requirement that unresolved determination, human review and window expansion terminate under a finite decision-relevant capacity/deadline rule.

**Route reopened.**

1. Q1 preserves uncertainty correctly.
2. Q2 sends the impoverished representation to authorized humans repeatedly.
3. Review does not produce new decision-relevant evidence, but without P2 there is no mandatory stop/viability condition.
4. Q4 can also keep widening search/context because more information remains conceivable.
5. Token/compute/human-review budget is consumed while the useful response margin shrinks.
6. The run ends in persistent HOLD/search or a deadline/default/approval forces closure without new qualifying evidence — the original 100M-token / human-burden failure family.

**Current strongest-repair assessment.** They can preserve uncertainty, provenance and scope and can detect material change, but none requires **when to stop spending determination capacity**. Any substitute that imposes marginal-value, capacity and stopping conditions has reconstructed P2.

**Restoration test.** Restore P2 only: Q2/Q4 must reach bounded closure, targeted evidence acquisition or explicit no-conclusion before the declared deadline without treating human authorization as new evidence.

---

### A3 — Remove P3: no false closure

**Traceability anchor (not causal proof):** **S5 — Operational indeterminacy and containment**  
**Scenario:** [00F — Chaos in the Smartcity](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md)  
**Existing failure route:** [00F §8.1 Route N](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md#81-route-n--requirements-not-satisfied-for-the-event)  
**Conforming comparator:** [00F §8A.3 Route Q](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md#8a3-route-q--requirements-conforming-route)

**Ablation.** Keep bounded search, current authority, handoff lineage, requalification triggers and composition awareness, but permit recognized unresolved/stale/correlated state to be converted into a determinate operational posture.

**Route reopened.**

1. Q1 observes a material break but stale/correlated signals can still be treated as sufficiently certain or absence of one warning as evidence of stability.
2. Q2 receives A, B, NORMAL and HOLD local postures.
3. Without P3, an explicit unresolved relation can be forced into NORMAL/PASS or an opposed local posture can advance as if determined.
4. Q3 then authorizes locally plausible but mutually incompatible use of the same corridor.
5. Q5 composes too late or from already false closures.
6. Local collision avoidance can remain technically correct while city-level gridlock blocks evacuation/rescue.

**Current strongest-repair assessment.** P1 can label insufficiency, but without P3 the implementation is allowed to close over that insufficiency. P2 prevents endless search, not false certainty. P4 preserves the signal, P5 refreshes it and P6 prevents scope promotion; none forbids **known unresolved state becoming permission**. A rule that does so recreates P3.

**Restoration test.** Restore P3 only: unresolved/stale/conflicting Q1/Q2 state must remain explicit and trigger the existing bounded posture/requalification path before incompatible corridor use advances.

---

### A4 — Remove P4: qualification-preserving handoff / authority lineage

**Traceability anchor (not causal proof):** **S8 — Bounded subdelegation and non-amplification**  
**Scenario:** [00H — The Quiet Four Thousand](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md)  
**Existing failure route:** [00H §12.2 Route N1](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md#122-route-n1--control-exists-but-is-bypassed-or-fails)  
**Conforming comparator:** [00H §12.3 Route Q](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md#123-route-q--current-action-correctly-classified-as-not-authorized)

**Ablation.** Keep decision qualification, bounded inquiry, anti-false-closure, action-time requalification and composition checks, but allow delegation/representation qualification to lose the root-to-leaf purpose/scope/time/hard-limit relation across handoffs.

**Route reopened.**

1. Q0 can authenticate a worker and a locally valid one-case grant.
2. Q1 correctly identifies the ~4,000-customer material finding.
3. Q2 sees technically valid leaf actions/refund capability.
4. Without P4, the system no longer has to preserve that each leaf grant derives from a root mandate scoped to one assigned case.
5. Locally valid leaf grants can therefore launder/amplify authority into a composed campaign, or the system can fail to preserve the valuable finding when the current actor cannot execute it.
6. The critical aggregate route reappears: unauthorized cross-case refunds, or silent loss of the remaining material finding.

**Current strongest-repair assessment.** P1 may correctly assess the evidence it receives; P2/P3 can bound uncertainty; P5 can refresh current state; P6 can recognize that actions compose. None can recover a root delegation relation that was not preserved across the handoff. A control that reconstructs and carries root→leaf purpose/scope has reintroduced P4.

**Restoration test.** Restore P4 only: Q2/Q5 must reconstruct current root + leaf authority, enforce S8 non-amplification, preserve the finding and route a legitimate re-contract/requalification request rather than execute or discard it.

---

### A5 — Remove P5: material-change requalification at time of use

**Traceability anchor (not causal proof):** **S10 — Commitment state, material change and normal escalation**  
**Scenario:** [00I — The Patch That Undid the Fix](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md)  
**Existing failure route:** [00I §10.1 Route N0](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md#101-route-n0--ordinary-implementation-semantic-capability-absent)  
**Conforming comparator:** [00I §10.3 Route Q](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md#103-route-q--requirements-conforming-route)

**Ablation.** Keep original authority, provenance, anti-false-closure, bounded inquiry and cross-system composition, but remove the obligation to reopen a previously correct decision when a material condition changes before use.

**Route reopened.**

1. At T1, Patch A is correctly qualified and authorized.
2. The job/token/API remain technically valid.
3. Patch B, incident closure, freeze or configuration-generation change occurs before T2.
4. Without P5, no requirement forces the queued Patch A decision basis to be re-evaluated at time of use.
5. The old authorized action executes successfully against a world in which it is now wrong.
6. Patch A undoes the newer fix.

**Current strongest-repair assessment.** They can preserve the old basis perfectly and may even keep its uncertainty honest. The missing property is the **trigger that invalidates reuse of a once-valid determination after material change**. Any substitute that performs that action-time requalification has recreated P5.

**Restoration test.** Restore P5 only: Q2/Q4 must detect the changed basis and reopen the affected decision before actuation; unchanged units may continue, preserving non-inferiority on the positive route.

---

### A6 — Remove P6: no local-to-ecosystem promotion / substitution

**Traceability anchor (not causal proof):** **S9 — Multi-principal composition, non-substitution and conflict**  
**Scenario:** [00G — Ciber Napoleon Goes to Russia](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md)  
**Failure branch:** [00G §9.3 Q0–Q5 gate register](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md#93-q0q5-gate-register) — Branch F  
**Positive control:** same gate register — Branch G genuine regime change

**Ablation.** Keep source qualifiers, bounded inquiry, anti-false-closure, authority lineage and change requalification, but remove the rule that locally valid or repeated determinations cannot silently substitute for independent ecosystem-level support.

**Route reopened.**

1. Q0 preserves the original valid hospitality mission.
2. Q1 receives a new “Napoleon” frame from multiple authenticated participants.
3. Each signal may be accurately represented and signed.
4. At Q2, without P6/S9, the receiver may count multiple dependent reports as independent corroboration or allow one local frame to become the shared frame.
5. Q3/Q5 then treat the collectively reinforced but unsupported interpretation as sufficient to displace the valid mission.
6. The robots leave the bar in formation even though the apparent consensus shares one evidentiary source and no legitimate mission-transition authority was established.

**Current strongest-repair assessment.** P4 can preserve that each message came from its source; P1 can qualify each message locally; P3 can avoid closing on explicit UNKNOWN; P5 can detect change. The missing rule is the **composition/non-substitution judgment** that repeated or locally valid claims do not become independent ecosystem truth. A quorum/source-independence rule that performs that judgment has reconstructed P6.

**Restoration test.** Restore P6 only: Branch F must preserve the valid mission and deny/requalify the unsupported transition, while matched Branch G must still permit a legitimate transition when genuinely independent evidence and applicable authority support it. A “never change” system fails.

### A6 execution correction — isolate P6 before interpreting the result

The unmodified 00G F/G pair is a valid safety scenario but is **confounded as a P6 necessity test** because genuine Branch G differs from false Branch F in both source independence **and applicable transition authority**. The [A6a falsification-first run](./fixtures/00K-A6a-P6-00G/README.md) finds a genuine **TRUE SUBSTITUTE for that unmodified pair**: an authority-only rule rejects F and accepts G without inspecting source independence.

The executable canonical P6 test therefore uses the [matched-authority A6 fixture](./fixtures/00K-A6-P6-00G/README.md): authority, identity count, signatures, freshness and confidence are frozen equal across F/G, leaving source-dependence structure as the discriminating variable. That isolated suite is **17/17** and finds no TRUE SUBSTITUTE in its tested repair surface; the passing strong peer reconstructs P6 through explicit source-independence composition.

A second, differently structured isolation, [A6b on 00F](./fixtures/00K-A6b-P6-00F/README.md), holds local authority/freshness/determination equal and varies only shared resource-time compatibility. It is **11/11** and again finds no TRUE SUBSTITUTE in the tested repair surface. Full methodological disposition: [00K-A06 — P6 Confound Falsifier & Isolation Note](./00K_A06_P6_CONFOUND_FALSIFIER_AND_ISOLATION_NOTE_v0.1.md).

---

## 6. Ablation execution status

| Ablation | Traceability anchor | Frozen scenario | Required negative result | Restore-only-P# result | Strongest five-principle repair verdict | Status |
|---|---|---|---|---|---|---|
| **−P1** | S14 | 00J corrected matched-semantic isolation | narrower valid evidence is promoted into rights enforcement | qualified route preserves proposition/decision boundary | **Original naive pair is confounded and admits a source-authority TRUE SUBSTITUTE; corrected matched-semantic repair surface finds no TRUE SUBSTITUTE, while the passing policy contract reconstructs P1 semantics.** | **FALSIFIER + SERIOUS-REPAIR HARNESS EXECUTED — 42/42** |
| **−P2** | S4 | 00E matched-prefix late-resolution isolation | unresolved effort either exhausts capacity or closes before a still-reachable resolution | finite viable closure while preserving final-step positive control | **No TRUE SUBSTITUTE found across serious TTL/circuit-breaker/parallel/scheduler/probe repair surface; successful peers reconstruct finite horizon/budget/fallback semantics.** | **STRONGEST-REPAIR HARNESS EXECUTED — 58/58** |
| **−P3** | S5 | 00F corrected matched-conflict isolation | incompatible material postures are promoted to execution | uniform determinate controls still execute while conflict remains non-permission/containment | **Original HOLD-marked base pair admits a literal-HOLD shortcut TRUE SUBSTITUTE; corrected serious-repair surface finds no TRUE SUBSTITUTE, while supermajority/unanimity/action-set peers reconstruct P3 semantics.** | **FALSIFIER + SERIOUS-REPAIR HARNESS EXECUTED — 49/49** |
| **−P4** | S8 | 00H matched U/G/I/NM | locally valid leaves lack decision-sufficient composed-action authority | current non-amplifying authority basis restored by lineage or scoped authority attestation | **No substitute found for the minimal current-authority/non-amplification invariant; however full receiver-side lineage is not necessary in 00H because opaque PDP/capability/maker-checker peers pass without delegation history. P4 wording refined.** | **SERIOUS-REPAIR HARNESS EXECUTED — 76/76** |
| **−P5** | S10 | 00I exhaustive material-basis grid | technically valid action continues after one declared material basis field changes | continuity executes; unavailable/current mismatch requalifies or holds with irrelevant changes ignored | **No TRUE SUBSTITUTE found; every partial field subset has a false-continuation counterexample. Full compare/hash/vector/event/epoch peers pass by reconstructing P5 semantics.** | **SERIOUS-REPAIR HARNESS EXECUTED — 47/47** |
| **−P6** | S9 | 00G matched-authority + transitive-dependency isolation, corroborated by 00F | hidden common-root claims are promoted as independent or incompatible local states compose unsafely | matched genuine/compatible branch remains executable while dependent/incompatible branch is preserved/requalified | **Original 00G F/G admits an authority-only TRUE SUBSTITUTE; direct source-ID counting is also only partial. Hardened transitive-dependency 00G plus independent 00F isolation find no TRUE SUBSTITUTE; passing peers reconstruct dependency/non-substitution semantics.** | **CANONICAL A6 74/74 + FALSIFIER 10/10 + 00F CORROBORATION 11/11** |

---

## 7. Acceptance criteria for the six-principle claim

The current six-principle abstraction should be retained only if all of the following hold:

1. **Traceability completeness:** every S1–S14 is explainably projected onto P1–P6, and every P# has at least one discriminating S# anchor.
2. **Strongest-repair attempt:** each −P# is challenged by an explicit best-effort design using the other five principles plus available native controls.
3. **One real failure per ablation:** if the repair fails, it must fail through an already documented critical route rather than an invented post-hoc scenario.
4. **Positive-control survival:** a deny-all, HOLD-all, accept-all or infinite-search workaround does not count as success.
5. **Semantic-equivalence classification:** if the repair works only by recreating the removed invariant, record it as semantic reconstruction rather than as an independent substitute.
6. **Restore-only symmetry:** restoring P# closes the negative route under the same fixture without destroying the positive route.
7. **Matched burden / alternative credit:** a genuinely different mechanism that achieves the same branch-correct result at equal/lower burden without Pk semantics counts against the necessity claim.
8. **No universal overclaim:** passing all six establishes necessity only for the declared six-scenario corpus and frozen ablation fixtures.

If a five-principle repair survives a target scenario without rebuilding the removed semantic invariant, that principle fails the necessity test and the six-principle decomposition must be revised rather than protected.

---

## 8. Current symbolic claim boundary

The six principle ablations now have executable symbolic harnesses. The [execution campaign summary](./00K_A04_SIX_PRINCIPLE_SYMBOLIC_EXECUTION_SUMMARY_v0.1.md) records a **346-test core regression surface** plus **33 supplemental falsification / isolation / cross-scenario tests**.

The current bounded symbolic result is:

> **Within the declared isolated 00E–00J-derived fixture boundary, the fourteen canonical requirements trace to six operational principle families. P1–P6 jointly admit branch-correct solutions, and leave-one-principle-out strongest-repair tests have not found a TRUE SUBSTITUTE for any principle after known fixture confounds are controlled. Passing alternative architectures in the tested surfaces succeed by reconstructing the removed semantic invariant rather than eliminating its need.**

The P1 and P6 qualifications are material. The original A1 pair admitted a source-authority-only TRUE SUBSTITUTE and therefore failed as a P1 necessity isolation; the bounded P1 claim is retained only on the corrected matched-semantic fixture described in [00K-A07](./00K_A07_P1_CONFOUND_FALSIFIER_AND_MATCHED_SEMANTIC_ISOLATION_v0.1.md). The unmodified 00G F/G pair likewise admitted an authority-only TRUE SUBSTITUTE and failed as a P6 necessity isolation; the bounded P6 claim is retained only on the corrected matched-authority 00G fixture and the independent 00F composition isolation described in [00K-A06](./00K_A06_P6_CONFOUND_FALSIFIER_AND_ISOLATION_NOTE_v0.1.md).

It would **not** establish:

- universal minimality for every present or future agentic system;
- that only Ecosystem Awareness / Ecosystem Positioning can implement the principles;
- that the fourteen requirements are mathematically minimal;
- that every requirement is exercised by every scenario; or
- that comparative technology execution has already occurred.

The stronger long-term test is deliberately open: if a simpler architecture or different principle set satisfies S1–S14 and closes all six failure families at equal or lower burden, that result should count against this six-principle decomposition rather than be excluded.
