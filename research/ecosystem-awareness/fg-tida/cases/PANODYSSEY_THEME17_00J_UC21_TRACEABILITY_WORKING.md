# Panodyssey Theme #17 → 00J → UC #21: Working Traceability Map

**Status:** Working crosswalk for discussion; not an adopted FG-TIDA deliverable, a Panodyssey product assessment, or a report of a production failure.  
**Prepared:** 3 October 2026  
**Purpose:** Bring together the Panodyssey challenge and ToR mapping work developed with Olena Pavlenko, Alexandre Leforestier’s public Theme #17 case, the specific 00J scenario and its relationship to FG-TIDA UC #21.

## 1. Scope and source case

[FG-TIDA Theme #17](https://github.com/FG-TIDA/themes/issues/17), proposed publicly by Alexandre Leforestier (Panodyssey), describes a production-side rights and identity chain for text. Its five stated layers cover domain AI access rules; machine-readable discovery per publication; per-work rights declarations distinguishing indexing, RAG and training; timestamped audit history; and certified author identity. Theme #17 identifies the agent-side identity and legal representation link as a remaining interoperability problem.

This is a bounded publishing-sector reference. The mapping below does not generalise from it to every publisher or creative-industry system.

## 2. How the case and use cases relate

The references form a traceable chain, with feedback between layers:

1. **Case study context — Theme #17:** the public Panodyssey production case and the system boundary it describes.
2. **Synthetic reference scenario — [00J, “The Author Pays for Their Own Work”](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md):** a fictional failure in which a valid generation/provenance record is promoted into a stronger downstream rights claim after source lineage is lost or flattened. It is not an incident report about Panodyssey or TEMS.
3. **Specific implementation trajectory — [00J-A01, Panodyssey Notice / TEMS](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md):** a source-reviewed, unexecuted analysis distinguishing the publicly documented source-side baseline (PANO-H0), a constructed defended peer (PANO-H1), and that same frozen peer under a synthetic resolver/identifier/lineage change (PANO-H2). It makes no Panodyssey/TEMS failure claim.
4. **Broader FG-TIDA use-case proposal — [UC #21](https://github.com/FG-TIDA/use-cases/issues/21), “When the controls work but the system fails”:** six cross-domain scenarios and three implementation walkthroughs. Its S6 concerns a rights-holder claim and has Q0–Q5 gates.

**The relationship is nested by level, not circular proof.** UC #21 is the broader proposal; 00J is a focused rights-provenance scenario that can instantiate and sharpen the rights branch (S6), while 00J-A01 supplies a specific, still-unexecuted implementation trajectory. Requirements and challenge mappings inform the test design; test evidence can then refine the mapping. The scenario itself is not evidence that the scenario’s conclusion is true. Evidence must come from a declared run or other independently reviewable source. UC #21 S6 and 00J are related, not identical or interchangeable.

## 3. Traceability chain

**Case Study → Challenge → ToR requirement → Use Case / test slice → evidence → determination**

The 16 September 2026 working reference called its industry challenges S1–S14. To avoid confusion with the Ecosystem Awareness canonical requirements S1–S14 and the separate FG-TIDA Annex III challenge set, this crosswalk labels those Panodyssey-map entries **PCH-01–PCH-14**. These are editorial aliases only; they do not create FG-TIDA identifiers. ToR anchors remain preliminary candidates from the working map and must be checked against the live ToR before any frozen or formal use.

| Panodyssey challenge | Challenge question | Preliminary ToR anchors |
|---|---|---|
| PCH-01 (working-map S1) — Authority provenance and current applicability | Can origin, scope, standing, expiry or revocation, and action-time applicability be established? | 4.3; A.1.2; A.2.2 · supporting: A.2.7 |
| PCH-02 (S2) — Preference fidelity and reviewable decision basis | Does delegated action respect applicable preferences and limits on a reviewable basis? | 3.4; 4.1; A.2.1 · supporting: A.2.4 |
| PCH-03 (S3) — Regime and context qualification | After a material change, does the prior authority/control frame still apply? | 4.3; A.2.2; A.2.4; A.2.8 |
| PCH-04 (S4) — Human oversight authority and capacity | Can an authorised human intervene meaningfully and in time? | 3.4; 4.3; 4.5; A.2.4 |
| PCH-05 (S5) — Operational indeterminacy and containment | Are incomplete or conflicting trust/authority facts contained without being treated as resolved? | 3.4; 4.3 · supporting: A.2.2; A.2.7 |
| PCH-06 (S6) — Interoperable, privacy-preserving trust determination | Can systems exchange enough machine-readable trust information without unnecessary disclosure? | 3.4; 4.2; 4.4; A.2.5 |
| PCH-07 (S7) — Identity and representation link | Can the actor, represented principal and authority be linked and kept attributable? | 2; 4.2; A.1.1; A.1.2 |
| PCH-08 (S8) — Bounded subdelegation and non-amplification | Does authority remain bounded through delegation, including scope, time, permissions and revocation? | A.1.2; 4.3 · supporting: A.2.2; A.2.7 |
| PCH-09 (S9) — Multi-principal composition, non-substitution and conflict | Can several principals and trust sources be composed without assuming a universal hierarchy? | 2; 4.2; A.2.1; A.2.5; A.2.7 |
| PCH-10 (S10) — Commitment state and material change | Are recommendation, commitment and action distinct, with reassessment after material change? | 4.3; A.2.2 · supporting: A.2.7 |
| PCH-11 (S11) — Policy integrity across domains and jurisdictions | Are policy origin, scope and meaning preserved across systems without standardising substantive law? | 4.4; A.1.5; A.2.5 · supporting: 4.2 |
| PCH-12 (S12) — Accountability, challenge and repair | Can the event be reconstructed, challenged and corrected for the future without rewriting history? | 3.4; 4.5; A.2.4 · supporting: A.2.2 |
| PCH-13 (S13) — Authority history versus intervention history | Do original authority and later intervention remain distinct while current authority is clear? | 4.3; A.1.2; A.2.4; A.2.7 |
| PCH-14 (S14) — Evidence-to-decision assessment | Are required evidence, its sufficiency/status, supported decision and residual uncertainty represented? | 3.4; 4.5; A.2.2; A.2.4 |

**Case-level ToR anchor:** the case supports ToR 3.3 (use cases) and 4.1 (use cases and requirements analysis) as candidate mapping. Other clauses above are selective challenge-level links, not a claim of complete ToR coverage. The live [FG-TIDA Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) is authoritative. The related [Annex IV mapping reference](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability.md) is itself marked a public pre-freeze working annex, not an adopted deliverable.

## 4. Olena’s three operational situations mapped to the case

The original working map recorded three proposed operational situations. The following links to 00J and UC #21 are a **working crosswalk**, not three separately submitted or accepted FG-TIDA use cases.

| Operational situation | Challenges from the working map | 00J / UC #21 relationship |
|---|---|---|
| Permission changes or is revoked after prior authorisation | PCH-01, PCH-10, PCH-13; PCH-05 only if evidence is incomplete or conflicting | 00J Q0/Q1 establish the rights and access frame; Q4 retains changed or replicated state; Q5 tests the final rights/enforcement proposition. Related UC #21 S6 gates include Q0, Q1, Q4 and Q5. |
| AI/crawler identity is uncertain or insufficiently verified | PCH-07, PCH-06, PCH-14 | 00J Q1 concerns the actor, represented principal and bounded access/use authority; Q5 prevents identity or a technical record alone from supporting enforcement. Related UC #21 S6 gates include Q0, Q1 and Q5. |
| Rights-holder intent is evidenced but AI compliance cannot be established | PCH-12, PCH-14, PCH-05; PCH-04 only when human decision is needed | 00J Q2–Q5 keep generation, source dependency, downstream claim, replication and enforcement distinct. Related UC #21 S6 gates include Q2, Q3, Q4 and Q5. |

The 00J core question is narrower than “is the platform compliant?” It asks whether the evidence available at the final decision supports the exact rights proposition being enforced against the exact subject, use and time. A generation record, a valid signature, or multiple copies of one downstream claim do not by themselves prove source independence or rights authority.

## 5. Evidence and status boundaries

- Theme #17 is the public source for the Panodyssey context and the problem statement as proposed by its author.
- 00J is a fictional reference scenario; its facts are synthetic or explicitly inferred, not claims about deployed products.
- 00J-A01 is source-reviewed design analysis, unexecuted and not a product benchmark.
- UC #21 is an open use-case proposal. Its scenarios and technology walkthroughs must retain their stated evidence status.
- The Panodyssey challenge-to-ToR links are preliminary working mappings. They do not mean that every challenge has been validated, that a technology is sufficient, or that FG-TIDA has adopted the mapping.

## 6. References

- [FG-TIDA Theme #17 — Digital Rights Infrastructure for Text](https://github.com/FG-TIDA/themes/issues/17)
- [FG-TIDA UC #21 — When the controls work but the system fails](https://github.com/FG-TIDA/use-cases/issues/21)
- [00J — Rights-Provenance Inversion / “The Author Pays for Their Own Work”](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md)
- [00J-A01 — Panodyssey Notice / TEMS Rights-Portability Implementation Trajectory](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md)
- [FG-TIDA Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx)
- [Annex IV — FG-TIDA ToR Mapping and Traceability (working reference)](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability.md)

**Preparation note:** This document consolidates the earlier “Panodyssey — Industry Challenge Map & FG-TIDA ToR Traceability — v0.1” working reference with the subsequent 00J/00J-A01 and UC #21 sources. It deliberately preserves the earlier mapping’s preliminary status and separates public evidence from synthetic scenario design.
