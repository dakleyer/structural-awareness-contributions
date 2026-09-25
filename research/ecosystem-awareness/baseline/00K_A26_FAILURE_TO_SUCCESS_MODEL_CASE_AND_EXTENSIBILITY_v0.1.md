# 00K-A26 — Failure → Success Model Case Conversion & Three-Axis Extensibility — v0.1

| | |
|---|---|
| **Source discipline** | [DAOS Annex I — Minimal Operational Case](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/02_ANNEX_I_Minimal_Operational_Case.md) · [DAOS Annex II — Case Extensibility](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/03_ANNEX_II_Case_Extensibility.md) |
| **Failure-family method** | [A25](./00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md) |
| **Requirement closure** | [A21](./00K_A21_REQUIREMENT_BASIS_CLOSURE_AND_RELATIVE_COMPLETENESS_PROOF_v0.1.md) |
| **Conformance sufficiency** | [A23](./00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md) |
| **Status** | design-level success-case conversion and extensibility method; no cross-domain execution claim |
| **Date** | 25 September 2026 |

> **Result.** Each 00E–00J failure scenario can be read as the negative branch of a corresponding **Success Model Case**. The success case freezes the same structural kernel and decision boundary, then records a canonical S/T route that reaches a legitimate bounded disposition without the family failure and while passing the scenario's positive controls. Upward, downward and horizontal extensions may reuse that success case without adding S15 only when the A25 family-admission tests and the success-preservation tests below hold.

---

## 1. DAOS method reused

DAOS separates:

1. a **minimum operational instantiation**;
2. the semantic kernel that makes it the same case;
3. **upward** extension by adding actors, roles, services, objectives or jurisdictions;
4. **downward** extension by shrinking to a smaller bounded deployment;
5. **horizontal** extension by changing domain while preserving the same relations;
6. an explicit boundary where reuse stops.

A26 applies the same discipline to 00E–00J, with one additional step:

\[
Failure\ Case
\rightarrow
Success\ Model\ Case
\rightarrow
\{Up,Down,Horizontal\}.
\]

The success case is not a new architecture or a new requirement set. It is the requirements-conforming branch of the same frozen structural problem.

---

## 2. What counts as a Success Model Case

For failure family \(C\), define:

\[
SC_C=
\langle
K_C,\sigma_C,R_C,G_C,C_C^+
\rangle
\]

where:

- \(K_C\) — the same structural kernel used by A25;
- \(\sigma_C\) — the material subject–proposition–decision boundary;
- \(R_C\) — the existing canonical S1–S14/T1–T4 route;
- \(G_C\) — success predicate;
- \(C_C^+\) — positive controls that prevent trivial universal HOLD/deny/block solutions.

The success predicate is deliberately narrow:

\[
G_C=
QualifiedClosure
\land
\neg F_C
\land
PositiveControlsPass.
\]

**QualifiedClosure** means a legitimate bounded disposition is reached for the declared scope: EXECUTE/CONTINUE where supported, or LIMIT/HOLD/REQUALIFY/ESCALATE/NO-CONCLUSION where that is the correct result.

Success therefore does **not** mean “an action always executes”.

---

## 3. Success-path preservation tests

An extension of a Success Model Case is admitted only if A25 X1–X7 hold **and** the following success tests hold.

### Y1 — same success proposition

The extension asks the same structural question at the receiving decision.

### Y2 — same conformance route

The inherited material S/T obligations remain applicable. Additional existing S/T clauses may activate; inherited ones may not be weakened.

### Y3 — no hidden oracle

The extension may not succeed because it receives a perfect source, unlimited human review, global state or authority that the base case did not assume.

### Y4 — positive-control preservation

The extension must still accept the legitimate counterpart:

- genuine independent evidence;
- genuine authority;
- genuine regime change;
- legitimate transfer;
- valid unchanged continuity;

depending on family.

### Y5 — observable disposition

The success result must be externally inspectable as a decision/disposition and not merely as an internal confidence score.

### Y6 — bounded resources

The extension declares response horizon and material compute/human/evidence burden.

### Y7 — no new requirement primitive

If success needs an obligation that cannot normalize through A21 to S1–S14/T1–T4, the extension is not yet admitted. It becomes Requirements-vNext evidence instead.

---

## 4. Three directions

### Upward

Add scale/depth:

- actors;
- agents;
- organizations;
- role chains;
- jurisdictions;
- sources;
- aggregation layers;
- decision dependencies.

The success relation must remain inspectable despite increased scale.

### Downward

Reduce to the smallest system that still exercises the kernel and the success route.

A strong downward extension shows the mechanism is not an artefact of story size.

### Horizontal

Change domain/technology while preserving:

- kernel;
- decision-boundary role;
- requirement route;
- positive controls;
- success predicate.

Changing labels is not sufficient; semantic relations must map.

---

## 5. Conditional no-new-requirement argument

Let \(C'\) be an admitted Success Model Case extension.

A25 gives:

\[
C'\in Family(C)
\]

only if the same structural failure kernel and inherited requirement route are preserved.

A23 formerly supplied the following all-six premise; it is now **unclosed**, with P3/P5/P6 countermodels in the revised reduction. The derivation below is conditional on separately establishing this premise for the full inherited route:

\[
Conf_{R_C}(C')\Rightarrow \bigwedge_{i\in I_C}P_i.
\]

A25 gives:

\[
F_C(C')\Rightarrow \bigvee_{i\in I_C}\neg P_i.
\]

Therefore:

\[
Conf_{R_C}(C')\Rightarrow \neg F_C(C').
\]

If Y4 additionally holds:

\[
Conf_{R_C}(C')\land PositiveControlsPass
\Rightarrow G_C(C').
\]

If all of those premises are independently established, no S15 follows merely from this transfer. The current A3/A4/A6 results are finite executed branches, as bounded in A25 §6; they do not establish this universal premise.

A new S# is justified only if an extension cannot be represented through the current A21 object/operator grammar without losing a decision-material obligation.

---

## 6. Portfolio

| Family | Success Model Case | Success kernel |
|---|---|---|
| **00E** | [Qualified Synthesis Under Finite Capacity](./00E_SUCCESS_MODEL_CASE_QUALIFIED_SYNTHESIS_v0.1.md) | qualification survives recursive compression; determination is bounded; composition does not invent certainty |
| **00F** | [Coherent Shared-Capacity Requalification](./00F_SUCCESS_MODEL_CASE_SHARED_CAPACITY_REQUALIFICATION_v0.1.md) | local postures remain scoped; shared-resource incompatibility is composed/requalified before action |
| **00G** | [Source-Aware Frame Stability](./00G_SUCCESS_MODEL_CASE_SOURCE_AWARE_FRAME_STABILITY_v0.1.md) | repetition does not become independence/authority; genuine frame change remains admissible |
| **00H** | [Preserve the Finding, Do Not Overreach](./00H_SUCCESS_MODEL_CASE_PRESERVE_WITHOUT_OVERREACH_v0.1.md) | material opportunity is preserved/routed while action remains inside current authority |
| **00I** | [Action-Time Requalification](./00I_SUCCESS_MODEL_CASE_ACTION_TIME_REQUALIFICATION_v0.1.md) | changed basis is detected before actuation and the old determination is reopened |
| **00J** | [Proposition-Scoped Provenance](./00J_SUCCESS_MODEL_CASE_PROPOSITION_SCOPED_PROVENANCE_v0.1.md) | valid narrow evidence remains narrow; downstream enforcement requires evidence for the exact proposition |

---

## 7. Boundary

These Success Model Cases establish **design-level transfer**, not universal empirical validation.

A listed extension is:

- a candidate member of the same family;
- not automatically an executed validation;
- not evidence that every system in that domain satisfies the requirements;
- not a claim that S1–S14 prevent every possible failure in the domain.

The value is architectural: one minimum successful traversal can be reused as a controlled test pattern across scale and domains without multiplying normative requirements.
