# Candidate Shared Frozen Case — Working Structure

- **Version:** 1.1

**Pre-freeze discussion note — not an adopted FG-TIDA deliverable**

## Purpose

The objective is to build a small, concrete and reusable agentic case that existing FG-TIDA themes can test against once its facts are frozen. It is not a proposal for a universal model, a new monolithic architecture or a separate workstream. The case should be deliberately minimal, but broad enough to expose meaningful interfaces between authority, delegation, context, human oversight, evidence and action-time decisions.

## Ideal pre-freeze design conditions — 3 + 1

The following are proposed ideal design conditions for a case intended for possible shared or cross-theme use. They are not agreed FG-TIDA requirements or exclusion criteria for other cases. A deliberately narrow or highly specific case may still be especially useful when it exposes a particular boundary or problem in depth.

### D1 — Intelligibility and concreteness

The case must describe one understandable future real-life situation, not an abstract architecture. Citizens, policy makers, architects and implementers should all be able to understand the same case at an appropriate level and identify who is acting, under what authority, what changed and what determination is required.

The concrete case is described separately in:

[Annex I — Minimal Operational Case Outline](02_ANNEX_I_Minimal_Operational_Case.md)

### D2 — Minimality with bounded extensibility

The case should use the smallest practical core while remaining extensible to a reasonably broad family of agentic situations. Extensibility must be tested deliberately: where the same principals, roles, agents, grants, commitments and context logic still work, and where the model stops being representative and a different case is needed. Universality is not the objective.

For a shared or reusable case, this is an ideal condition rather than an exclusion criterion. A deliberately narrow case may still be more useful when the objective is to test a specific sector, failure mode or boundary.

The bounded extensibility analysis is kept separately in:

[Annex II — Why the Minimal Case Is Extensible](03_ANNEX_II_Case_Extensibility.md)

### D3 — FG-TIDA ToR alignment

The case and the later technical challenges must map clearly to the FG-TIDA Terms of Reference. Rich service context is allowed only to make the situation concrete; the case should not drift into city optimization, policy design or unrelated system architecture. In-scope and out-of-scope elements should remain explicit.

The detailed ToR mapping is kept separately in:

[Annex IV — FG-TIDA ToR Mapping and Traceability](05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability.md)

### +1 — Declared governing regime for authority determinations

Following the current Theme #16 authority-interface discussion, especially Pam Dixon’s clarification, where a case asks whether a mandate is valid, remains in standing, may be revoked, or continues to bind at action time, the governing legal regime should be declared as a case fact.

This does not make multijurisdictionality a requirement. A single-regime case can be fully useful. Where materially different regimes are tested, the same structural core may become a controlled family of regime-specific variants rather than one supposed universal legal answer.

Pam Dixon’s clarification:

https://github.com/FG-TIDA/themes/issues/16#issuecomment-5481112607

## Pre-freeze → freeze → testing

This proposal is intentionally not frozen. The case should first be worked collaboratively: an initial design can be proposed, then refined by other contributors until the relevant pre-freeze conditions are sufficiently met. That design phase should be short; once the case is useful and stable enough, a numbered version should be frozen deliberately and its facts should no longer move to accommodate a preferred solution.

## After freeze

The frozen case will expose a set of technical or solution challenges. Different themes or workstreams can use the same stable case to show how their requirements or architectures handle the challenge relevant to them; no single theme must solve the entire case. Passing one challenge does not mean satisfying the whole ToR, proving universal coverage or solving all agentic systems. The value is a shared, sufficiently broad toy/reference case that makes interfaces, gaps and incompatibilities visible under the same facts.

The technical challenge surface is kept separately in:

[Annex III — Challenges Exposed by the Case](04_ANNEX_III_Challenges_Exposed_by_the_Case.md)

Relevant interfaces with adjacent standards, groups and research are kept separately in:

[Annex V — Adjacent Standards and Research Relevance](06_ANNEX_V_Adjacent_Standards_and_Research_Relevance.md)

## What follows

The next document presents a first outline of such a case for discussion. It is a starting design to be challenged, extended and bounded before any version is frozen.
