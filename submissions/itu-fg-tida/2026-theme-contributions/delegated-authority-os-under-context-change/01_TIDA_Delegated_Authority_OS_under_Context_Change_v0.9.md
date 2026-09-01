# Candidate Shared Frozen Case — Working Structure

- **Version:** 0.9
- **Status:** Pre-freeze discussion note — not an adopted FG-TIDA deliverable

## Purpose

The objective is to build a small, concrete and reusable agentic case that existing FG-TIDA themes can test against once its facts are frozen. It is not a proposal for a universal model, a new monolithic architecture or a separate workstream. The case should be deliberately minimal, but broad enough to expose meaningful interfaces between authority, delegation, context, human oversight, evidence and action-time decisions.

## Ideal pre-freeze design conditions — 3 + 1

The current working view uses **three ideal design conditions plus one authority-validity condition**. These are proposed qualities for maturing this candidate case for possible shared/cross-theme use; they are **not agreed FG-TIDA requirements or exclusion criteria for other cases**. A narrow or highly specific case may still be especially useful even when broad reuse or extensibility is not its objective.

### D1 — Intelligibility and concreteness

The case should describe one understandable real-life or realistic future situation, not an abstract architecture. Citizens, policy makers, architects and implementers should all be able to understand the same case at an appropriate level and identify who is acting, under what authority, what changed and what determination is required.

For this package, the concrete case is separated into [Annex I — Minimal Operational Case Outline](02_ANNEX_I_Minimal_Operational_Case_Outline_v0.3.md), so the case-design condition and the case facts remain distinct.

### D2 — Minimality with bounded extensibility

The case should use the smallest practical core while, where shared reuse is intended, remaining extensible to a reasonably broad family of agentic situations. Extensibility should be tested deliberately: where the same principals, roles, agents, grants, commitments and context logic still work, and where the model stops being representative and a different case is needed. **Universality is not the objective**, and a deliberately narrow sector-specific case can remain valuable even when this condition is not a design priority.

The bounded extension tests are kept separately in [Annex II — Why the Minimal Case Is Extensible](03_ANNEX_II_Case_Extensibility_Upward_Downward_Horizontal_v1.2.md).

### D3 — FG-TIDA ToR alignment

The case and the later technical challenges should map clearly to the FG-TIDA Terms of Reference. Rich service context is allowed only to make the situation concrete; the case should not drift into city optimization, policy design or unrelated system architecture. In-scope and out-of-scope elements should remain explicit.

The detailed mapping is kept separately in [Annex IV — FG-TIDA ToR Mapping and Traceability](05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability_v1.0.md).

### +1 — Declared governing regime for authority determinations

Following the current Theme #16 authority-interface discussion, especially [Pam Dixon’s clarification](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5481112607), where a case asks whether a mandate is valid, remains in standing, may be revoked, or continues to bind at action time, the **governing legal regime should be declared as a case fact**.

This does not make multijurisdictionality a requirement. A single-regime case can be fully useful. Where materially different regimes are tested, the same structural core may become a controlled family of regime-specific variants rather than one supposed universal legal answer.

## Provenance note

The case grows from the xSeil passenger-transport/logistics deployment in the Riviera Maya (2016–2017) and the broader Car Evolution formalization (2023), later connected to Tegrity.AI work on Minimal Agentic Control Architecture / Minimum Sufficient Control. This lineage is provenance only: it does not need to be understood in order to use the case, and it does not imply FG-TIDA adoption or endorsement.

## Pre-freeze → freeze → testing

This proposal is intentionally not frozen. The initial design can be refined while the case remains pre-freeze; once it is useful and stable enough, a numbered version can be frozen deliberately and its facts should no longer move to accommodate a preferred solution.

The purpose of the pre-freeze work is therefore to make the case sufficiently clear, appropriately bounded, traceable to the ToR and—where authority validity is tested—legally determinate under a declared governing regime. This does not require one universal case or prevent alternative or complementary cases from being developed.

## After freeze: challenges to test

The frozen case should expose a set of technical or solution challenges. Different themes or workstreams can use the same stable facts to show how their requirements or architectures handle the challenge relevant to them; no single theme must solve the entire case. Passing one challenge does not mean satisfying the whole ToR, proving universal coverage or solving all agentic systems.

The challenge surface is kept separately in [Annex III — Challenges Exposed by the Case](04_ANNEX_III_PostFreeze_Solution_Challenges_v1.3.md). The point of the main note is not to reproduce the S1–S14 list, but to explain why a stable case should expose testable questions once frozen.

## Package structure

The package remains modular:

1. **This main note** — purpose, pre-freeze design conditions, provenance and freeze logic.
2. [**Annex I — Minimal Operational Case Outline**](02_ANNEX_I_Minimal_Operational_Case_Outline_v0.3.md) — the concrete case to be understood and eventually frozen.
3. [**Annex II — Why the Minimal Case Is Extensible**](03_ANNEX_II_Case_Extensibility_Upward_Downward_Horizontal_v1.2.md) — bounded upward, downward and horizontal extensibility.
4. [**Annex III — Challenges Exposed by the Case**](04_ANNEX_III_PostFreeze_Solution_Challenges_v1.3.md) — the technical/solution challenge surface.
5. [**Annex IV — FG-TIDA ToR Mapping and Traceability**](05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability_v1.0.md) — evidence that the case remains within mandate.
6. [**Annex V — Adjacent Standards and Research Relevance**](06_ANNEX_V_Adjacent_Standards_and_Research_Relevance_v1.1.md) — controlled interfaces with adjacent groups, standards and research.

## What follows

The next document, Annex I, presents the concrete case itself. The remaining annexes test extensibility, challenges, ToR traceability and adjacent interfaces without expanding this main note into the case, the challenge catalogue or the standards map.

### Version note — 0.9

v0.9 restores the previously reviewed modular main-document structure. Relative to that structure, the substantive changes are limited to: moving the pre-freeze design conditions to the front, adding the Pam Dixon governing-regime `+1`, qualifying D1/D2 as ideal rather than exclusionary conditions, and compressing provenance to a short note. **Annex I–V are unchanged.**
