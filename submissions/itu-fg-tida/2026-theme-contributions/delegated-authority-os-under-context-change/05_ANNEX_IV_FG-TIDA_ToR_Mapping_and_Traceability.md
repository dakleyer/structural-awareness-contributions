# Annex IV — FG-TIDA Terms of Reference Mapping and Traceability

- **Version:** 1.0
- **Parent case:** [Annex I — Minimal Operational Case](02_ANNEX_I_Minimal_Operational_Case.md)
- **Status:** Public pre-freeze working annex; not an adopted FG-TIDA deliverable.

## Case-level anchor

The case as a whole directly supports **ToR 3.3 (use cases)** and **4.1 (use cases and requirements analysis)**: it is a concrete multi-actor agentic situation used to expose technical trust and identity requirements. The mapping below shows how individual solution challenges exercise selected parts of the mandate; passing the case is evidence against those selected requirements, not proof of full ToR coverage.

## Coverage boundary

The strongest coverage is around delegation, dynamic trust lifecycle, human oversight, runtime trust control, technical-policy, interoperability, accountability and assessment. The case deliberately does not attempt to cover every FG-TIDA deliverable, national digital-ID content, AI governance, or agentic-AI protocols. Its role is to provide one sufficiently rich shared test case through which selected ToR requirements can be made concrete and compared across themes.

**Source:** [ITU-T FG-TIDA Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx), clauses 2, 3.3–3.4, 4.1–4.5 and Annex A.1/A.2; current text reviewed 31 August 2026.

## Challenge-to-ToR mapping

| Challenge | Primary ToR anchors | Supporting anchors | What the case tests |
|---|---|---|---|
| **S1 — Authority provenance & current applicability** | 4.3; A.1.2; A.2.2 | A.2.7 | Delegation origin, scope, standing, expiry/revocation and whether authority still binds at action time. |
| **S8 — Bounded subdelegation & non-amplification** | A.1.2; 4.3 | A.2.2; A.2.7 | Whether delegation remains bounded through agent chains and whether scope, duration, limits and revocation survive composition. |
| **S2 — Preference fidelity & reviewable decision basis** | 3.4; 4.1; A.2.1 | A.2.4 | Preferences/limits only insofar as they are needed to determine whether delegated action remains trustworthy, attributable and reviewable; this is not a general AI-alignment task. |
| **S9 — Multi-principal composition, non-substitution & conflict** | 2; 4.2; A.2.1; A.2.5; A.2.7 | — | Multi-actor ecosystems, heterogeneous trust, multiple authority sources and consistent runtime trust state without assuming one universal hierarchy. |
| **S3 — Regime & context qualification** | 4.3; A.2.2; A.2.4; A.2.8 | — | Dynamic trust, context-sensitive evaluation, changed conditions, intervention triggers and evidence that the prior control/authority frame remains valid. |
| **S10 — Commitment state & material change** | 4.3; A.2.2 | A.2.7 | Trust across lifecycle moments—recommendation, commitment and action—and whether material change triggers re-evaluation, revocation or a new decision. |
| **S4 — Human oversight authority & capacity** | 3.4; 4.3; 4.5; A.2.4 | — | Meaningful human oversight, escalation criteria, accountability and whether oversight remains operationally viable at scale. |
| **S11 — Policy integrity across domains & jurisdictions** | 4.4; A.1.5; A.2.5 | 4.2 | Technical-policy expression, interoperability and preservation of policy origin/scope across sectors or jurisdictions; the case does not decide substantive law or policy. |
| **S5 — Operational indeterminacy & containment** | 3.4; 4.3 | A.2.2; A.2.7 | Resilience and safe handling when trust/authority evidence is incomplete or conflicting; containment is a trust-control consequence, not general system-safety design. |
| **S12 — Accountability, challenge & repair** | 3.4; 4.5; A.2.4 | A.2.2 | Traceability and reconstruction of who acted under which authority and evidence. “Repair” is limited to correcting future trust state without rewriting history. |
| **S6 — Interoperable, privacy-preserving trust determination** | 3.4; 4.2; 4.4; A.2.5 | — | Interoperability, privacy, machine-readable trust information and cross-system determination without unnecessary disclosure. |
| **S13 — Authority history vs intervention history** | 4.3; A.1.2; A.2.4; A.2.7 | — | The cross-theme seam: provenance and intervention records remain distinct, while operative authority for a current action stays unambiguous. |
| **S7 — Identity & representation link** | 2; 4.2; A.1.1; A.1.2 | — | The human/agent/organization relationship, identity layers, authorization/delegation and which principal an acting agent actually represents. |
| **S14 — Evidence-to-decision assessment** | 3.4; 4.5; A.2.2; A.2.4 | — | Criteria, evidence sufficiency, assessment status and the decision supported by that evidence; the assessment method need not become the runtime architecture. |

## Traceability rule

This mapping is intentionally many-to-many. It gives existing themes a shared test surface; it does **not** require every theme to solve the whole case or create a standalone workstream. The mapping should be rechecked against the live ToR before any frozen release or formal external use.
