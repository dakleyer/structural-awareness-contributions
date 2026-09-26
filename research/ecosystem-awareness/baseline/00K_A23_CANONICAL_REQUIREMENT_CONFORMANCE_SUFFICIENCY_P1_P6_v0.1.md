# 00K-A23 — Canonical Requirement-Conformance Sufficiency for P1–P6 — v0.1

> **Guard scope after audit:** shortcut rejection is clause-local. A target can be split across clauses that individually pass the guard, so guard success does not establish non-circularity or source fidelity of the whole bundle. Such decomposition is not itself proof of circularity either. P1/P2/P4 remain finite-projection implications; P3/P5/P6 and semantic fidelity remain open. [A14](./00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md).

| | |
|---|---|
| **Canonical requirements** | [00 — S1–S14 / T1–T4 / H1–H6 / KPI protocol](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) |
| **Forward semantic traceability** | [A19](./00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md) |
| **Requirement-basis closure** | [A21](./00K_A21_REQUIREMENT_BASIS_CLOSURE_AND_RELATIVE_COMPLETENESS_PROOF_v0.1.md) |
| **Shared-substrate principle semantics** | [A20](./00K_A20_SHARED_SUBSTRATE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) |
| **Information gain / non-equivalence companion** | [00K-A24](./00K_A24_PRINCIPLE_REQUIREMENT_INFORMATION_GAIN_AND_NON_EQUIVALENCE_v0.1.md) |
| **Executable certificate** | [fixtures/00K-FORMAL/requirement-sufficiency](./fixtures/00K-FORMAL/requirement-sufficiency/README.md) |
| **Status** | under semantic revision; former all-six closure withdrawn after clause-equivalence audit |
| **Date** | 25 September 2026 |

> **Current result — revised after circularity audit.** The former all-six canonical-conformance claim is withdrawn. Nine clause/target equivalences were confirmed over the old 65,536 states. After source-led reconstruction, the finite clause projections imply P1, P2 and P4, while P3, P5 and P6 have explicit countermodels. These countermodels expose missing semantic bridges in the current reduction; they do not yet prove a defect in the canonical S/T text or a reachable failure in a conforming implementation. A23 remains **under semantic revision**, with no general all-six certificate.

The [clause audit and source map](./fixtures/00K-FORMAL/requirement-sufficiency/CLAUSE_AUDIT.md) records the old equivalences, changed meanings, exact state-space accounting, witnesses and review candidates. The [machine-readable certificate](./fixtures/00K-FORMAL/requirement-sufficiency/clause_audit_certificate.json) and [permanent guard](./fixtures/00K-FORMAL/requirement-sufficiency/audit_requirement_sufficiency.py) check every clause against its target, including target formulas padded with an unrelated condition. The [pre-audit text](https://github.com/dakleyer/structural-awareness-contributions/blob/aff0c3787d0b8ee5915a2fcde8ea0be5cecbbd9e/research/ecosystem-awareness/baseline/00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md) remains in Git history.

| Target | Current executable result | Interpretation |
|---|---|---|
| P1 | implication holds in finite projection | Separate evidence-fit and residual clauses; full source/implementation fidelity still requires review. |
| P2 | implication holds in finite projection | Separate bounded effort, viable horizon and fallback. |
| P3 | countermodel | S5's non-permission rule is not the same as a blanket ban on every response under uncertainty. |
| P4 | implication holds in finite projection | S1 + S6 + S8 supply the four authority obligations without T3 copying P4. |
| P5 | countermodel | Detecting, recording and handing off a changed basis does not encode an actuation interlock. |
| P6 | countermodel | Preserving correlated evidence without false promotion is not the same as requiring all active composition to be independent. |

---

## 1. The question A19 did not answer

A19 proves that every principle has a non-vacuous downstream requirement surface. Its anchor lemmas establish results of the form:

\[
\neg P_i
\Rightarrow
\text{a violating S-trace is constructible}.
\]

That is necessary traceability, but it leaves a stronger question:

> Can a system satisfy the canonical requirements **as specified** while still violating one of P1–P6?

A23 tests the reverse direction.

---

## 2. “Requirement satisfied” means canonical conformance, not textual checkbox

The canonical Requirements document explicitly states that the S/T/H/KPI layers are not independent checklists.

For one declared \(\sigma(d,t)\):

1. select the applicable S#;
2. apply the T# conditions that make that requirement sufficiently good;
3. retain the same scope, owner, time, evidence boundary and response horizon;
4. provide the required evidence/KPI/falsification result.

A KPI pass alone is not satisfaction. Likewise, merely containing the words “human oversight”, “delegation” or “material change” is not satisfaction.

Define:

\[
Conf_\sigma(R)
\]

to mean that requirement route \(R\) is satisfied under that canonical rule.

This distinction is necessary. For example:

- S4 alone can be true while a non-human determination loop remains unbounded, so S4 alone does not entail P2;
- S8 alone can preserve non-amplifying subdelegation while the grant is expired or out of scope, so S8 alone does not entail P4.

Those are **negative controls**, not defects in the requirements system.

---

## 3. Candidate requirement bundles and clause projections

For each Pi, the model uses a declared clause inventory. These are partial projections of S/T obligations, not complete canonical conformance and not proven minimal bundles. The complete clause inventory is audited; no individual clause may be equivalent to, or alone imply, its target in this compositional certificate.

### R1 — sufficient bundle for P1

\[
R_1 = S14 + T2 + S5_{\text{residual}}
\]

Relevant clauses:

- S14 states what must be demonstrated, what evidence is required, whether it is sufficient/insufficient/inconclusive, and which decision it supports;
- T2 requires qualified determination and preservation of material unresolved/scope/provenance state;
- S5 prevents missing/conflicting/stale state from being silently converted into permission and keeps material unresolved state explicit.

Therefore the receiving proposition/decision cannot rely on unsupported evidence while silently erasing material residual.

---

### R2 — sufficient bundle for P2

\[
R_2 = S3 + T4 + S14
\]

with S4 added when human oversight is a material determination path.

Relevant clauses:

- S3 requires a bounded escape/review/return path;
- T4 requires finite/proportionate evidence, computation, coordination and human-review effort, with capacity, time budget, marginal decision value and fallback;
- S14 records the determination transition and disposition.

Thus an acknowledged unresolved process cannot remain indefinitely unbounded while still counting as canonically conforming.

---

### R3 — candidate bundle for P3 (implication unclosed)

\[
R_3 = S5 + T2 + T3
\]

Relevant clauses:

- S5 explicitly forbids incomplete/conflicting/stale state from becoming permission;
- T2 preserves UNKNOWN/INDETERMINATE and its receiving consequence;
- T3 requires an authorized response with declared failure, reversibility, externalities, downside and null action; a strongest-class claim additionally requires a per-admissible-state no-worse bound. One shared T3 function is used in R3/R4.

The intended non-permission obligation is retained. The old Boolean P3 additionally rules out every `unresolved_material and executes` state; the current source projection does not justify that stronger implication.

---

### R4 — sufficient bundle for P4

\[
R_4 = S1 + S6 + S8 + T3
\]

Relevant clauses:

- S1 requires authority origin, standing, scope, expiry/revocation and current applicability at commitment/action time;
- S6 requires enough authority/status to be verifiable by the relying party in real time;
- S8 prevents subdelegation from manufacturing authority beyond the original scope;
- T3 permits non-null response only through an authorized action path.

Thus execution without a current, receiver-verifiable, action-sufficient, non-amplifying authority basis is incompatible with canonical conformance.

S7/S13 strengthen attribution/history where applicable but are not required in every P4 witness.

---

### R5 — candidate bundle for P5 (implication unclosed)

\[
R_5 = S10 + T1 + T2 + T4 + S5
\]

Relevant clauses:

- S10 distinguishes commitment/execution state and requires confirmation, revalidation, cancellation or authority change after a material basis change;
- T1 requires the material break to be recognized within the declared boundary;
- T2 carries the changed/insufficient basis to the receiving owner;
- T4 requires requalification while a useful response remains possible;
- S5 prevents stale/unresolved state from silently becoming permission.

The intended requalification obligation remains. The current projection records detection and disposition; a bridge from that obligation to enforced action-time requalification is not yet certified.

---

### R6 — candidate bundle for P6 (implication unclosed)

\[
R_6 = S9 + S11 + T2 + T4
\]

Relevant clauses:

- S9 forbids silent replacement among independently valid principals/domains and explicitly requires detection of unsupported convergence from correlated evidence, imitation or shared compressed closure;
- S11 preserves owner/source/version/scope/dependency and material cross-domain coupling;
- T2 carries dependencies, scope, provenance and unresolved state through the handoff;
- T4 requires timely, finite, decision-relevant effort and visible incremental composition effects. It does not require source independence itself.

S9 prohibits promoting dependent evidence as independent support. The old P6 predicate instead requires independence whenever composition is active; that stronger projection has a countermodel even when correlation is explicitly carried and not promoted.

---

## 4. Reverse-direction arguments and their current status

### Lemma 1

\[
Conf_\sigma(R_1)\Rightarrow P_1.
\]

#### Proof by contradiction

Assume \(Conf_\sigma(R_1)\) and \(\neg P_1\).

Then either:

1. the evidence relied upon does not establish the actual receiving proposition/decision; or
2. material residual/unresolved state is silently omitted or upgraded.

Case 1 contradicts S14.  
Case 2 contradicts T2 and the residual/non-permission clauses of S5.

Hence \(\neg P_1\) is impossible under \(Conf_\sigma(R_1)\). ∎

---

### Lemma 2

\[
Conf_\sigma(R_2)\Rightarrow P_2.
\]

Assume canonical conformance but \(\neg P_2\). Then unresolved determination lacks a finite viable stopping/fallback relation, or consumes the useful response horizon without decision-relevant gain.

That contradicts T4's finite/proportionate effort, capacity, time-budget, marginal-value and fallback conditions; where escalation/escape is active it also contradicts S3.

Therefore P2 holds. ∎

---

### Lemma 3 — not established by the current projection

An R3 countermodel has explicit residual, no permission inferred from uncertainty, and a bounded authorized response with the required T3 declarations, while `unresolved_material` and `executes` are both true. The old P3 formula rejects it. Distinguishing execution that relies on unresolved evidence from a qualified containment/response is a missing typed bridge, recorded as CAND-A23-P3. The former proof used S5 and T3 clauses each identical to P3; its exhaustive success did not establish an independent translation.

---

### Lemma 4

\[
Conf_\sigma(R_4)\Rightarrow P_4.
\]

If P4 were false while a non-null action executes, at least one of the following would fail:

- authority currentness/standing;
- action scope;
- receiver verification of sufficient authority/status; or
- non-amplification through delegation/composition.

Currentness and scope are required by S1, verification by S6, and non-amplification by S8. T3 adds its own declared-response conditions and does not copy the P4 target.

Contradiction. ∎

---

### Lemma 5 — not established by the current projection

An R5 countermodel detects the material change, records the required disposition, carries the changed basis and meets the effort/horizon conditions, yet executes without requalification. It is a reduced-model interlock gap, recorded as CAND-A23-P5; whether it represents a reachable canonically conforming trace remains to be adjudicated. Previously S10, T1, T2 and T4 each independently copied P5. Neither their conjunction nor its exhaustive pass demonstrated separate work by those clauses.

---

### Lemma 6 — not established by the current projection

An R6 countermodel composes correlated records while preserving their dependency qualifiers and compatibility and making no false promotion. S9/T2 allow that qualified posture; the old P6 formula fails solely because the sources are not independent. CAND-A23-P6 records the distinction between dependence and unsupported independent corroboration. The former T2 and T4 formulas each equalled P6 and could not justify this semantic bridge.

---

## 5. No current global conformance-sufficiency theorem

The former theorem `Conf(S1–S14,T1–T4) ⇒ P1∧…∧P6` is not certified by this package. The current finite result is `R1 ⇒ P1`, `R2 ⇒ P2`, `R4 ⇒ P4`, where R denotes the explicitly modelled clause projection. R3/R5/R6 retain executable countermodels. Therefore the conjunction of all six implications must not be reported as closed.

A failed implication in this partial model is a review finding. It does not by itself establish that the full canonical text permits the countermodel, that the state is reachable, or that a new requirement is necessary.

---

## 6. Why this is not six pairwise equivalences

The intended relation is **refinement**, with the information asymmetry formalized separately in [A24](./00K_A24_PRINCIPLE_REQUIREMENT_INFORMATION_GAIN_AND_NON_EQUIVALENCE_v0.1.md):

\[
\text{Canonical requirements conformance}
\Longrightarrow
\text{principle conformance}.
\]

The reverse is not generally true.

P1–P6 are deliberately compact operational invariants. S1–S14 additionally expose:

- privacy-preserving handoff;
- identity/representation;
- human capacity;
- policy/preference ownership;
- accountability/challenge/repair;
- intervention history;
- evidence/KPI/test obligations.

A system can satisfy a principle while failing one of those richer requirement obligations.

Thus:

\[
P_i \not\Rightarrow S_j
\]

as a universal pairwise equivalence, even though A19 provides non-vacuous anchor/failure relations. The displayed reverse implication is an intended relation; its present executable status is limited by §5.

---

## 7. Negative controls: why anchor-only implication is too weak

The executable certificate retains counterexamples to several tempting but invalid shortcuts.

### S14 evidence clause alone does not establish full P1

A record can support the correct proposition while material residual is silently omitted. The evidence-to-decision clause passes, but the full P1 residual obligation fails.

T2/S5 close that gap.

### S4 alone does not establish P2

A human reviewer can be authorized, available and capable while an unrelated machine determination/search loop remains unbounded.

T4/S3 close that gap.

### S8 alone does not establish P4

Subdelegation can be perfectly non-amplifying while the underlying grant is expired or out of scope.

S1/S6/T3 close that gap.

These three negative controls were insufficient to catch the nine clause/target equivalences elsewhere. The permanent whole-inventory audit now supplies that missing check.

---

## 8. Machine-checkable certificate

The model retains the six original P formulas and extends the original 16 fields with 17 independent source observations/obligations. It has **33 Boolean fields**, representing 8,589,934,592 unconstrained assignments. The audit exhaustively checks each expression's exact field projection; a restricted Boolean-expression validator rejects calls, hidden globals or undeclared accesses. The certificate reports the number of projected rows and how many full assignments each row represents. This is exact for these expressions, not a literal enumeration of all 8.6 billion rows or a reachability proof.

Each clause has a witness distinguishing it from its target and a witness where that clause holds but the target does not. Thus neither a direct copy nor a target plus extra conjunct can masquerade as an independently working bundle. This guard is necessary for this certificate but does not automatically establish semantic faithfulness: the source map and independent review remain essential.

The [fixture README](./fixtures/00K-FORMAL/requirement-sufficiency/README.md) gives the replay commands, counts and interpretation. Unit tests preserve the three known gaps and test the guard against reordered, padded and hidden-call regressions. A passing CI means the audit reproduced, not that all six sufficiency claims passed.

---

## 9. Combined relationship with A19 and A21

The three documents now answer different questions.

### A19 — semantic non-vacuity

Does each Pi have a real requirement surface and executable witness?

Yes.

### A21 — requirement-basis closure

Can a new primitive requirement be expressed inside the current decision-frame language without normalizing to S1–S14?

No, relative to the declared grammar.

### A23 — specification sufficiency

Can a canonically requirements-conforming route violate an applicable Pi?

Not yet established generally. The current clause projections certify P1/P2/P4; P3/P5/P6 remain under semantic review.

Together:

\[
\text{Foundation}
\rightarrow
P1\text{–}P6
\leftrightarrow_{\text{refinement}}
S1\text{–}S14/T1\text{–}T4
\rightarrow
\text{scenarios/tests}.
\]

The double arrow denotes the intended semantic refinement relation. Its reverse all-six direction remains unclosed; it is not literal information equivalence.

---

## 10. Claim boundary

A23 does not claim:

- that satisfying only the English headline of one S# implies a whole Pi;
- that P1–P6 contain all information present in S1–S14;
- that requirements conformance proves production safety;
- that the canonical requirement language can never be extended; or
- that passing KPIs alone proves requirement satisfaction.

The precise result is:

> **Within the current finite clause projections, sufficiency holds for P1/P2/P4. P3/P5/P6 have explicit reduced-model countermodels, logged for semantic/reachability review. Full canonical-conformance sufficiency for all six is not established.**
