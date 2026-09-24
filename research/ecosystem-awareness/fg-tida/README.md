# Ecosystem Awareness — FG-TIDA application package

> **Navigation:** [Iván Abril Palma](https://github.com/dakleyer/dakleyer) → [Structural Awareness](https://github.com/dakleyer/structural-awareness-contributions) → [Ecosystem Awareness](../README.md) → **FG-TIDA application package**


> **FG-TIDA-specific application package.** This folder is deliberately separate from the general Ecosystem Awareness canonical architecture. It records how EA is being projected into the current FG-TIDA process, what an ideal FG-TIDA mapping would look like, what the public source state currently supports, and which FG-TIDA-specific cases/tests are available. Nothing in this package changes the general EA architecture by itself.

## Read in this order

1. [**Working Group / Phase 2 Charter preparation**](./charter/THEME_13_WORKING_GROUP_CHARTER_PREPARATION_DRAFT_v0.1.md) — candidate Theme #13 charter/WG structure for review; not submitted and not an established WG.
2. [**Specification preparation**](./specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md) — current source-to-specification map, normative maturity, Decision Boundary / cross-Theme conformance route, readiness gates and candidate document structure.
3. [**FG-TIDA interfaces**](./interfaces/README.md) — applies the general 04 interface architecture in two deliberately separate layers: **05 ideal FG-TIDA target** and **05A realistic/current FG-TIDA filter**, each with its own vNext delta.
4. [**FG-TIDA-specific cases**](./cases/README.md) — DAOS-derived case material used to exercise the FG-TIDA mapping.
5. [**FG-TIDA-specific tests**](./tests/README.md) — EHD / Theme #13 interoperability material plus the Decision Boundary cross-Theme evaluation profile.
6. [**FG-TIDA provenance**](./provenance/README.md) — public footprint and provenance records.

## General EA architecture versus FG-TIDA application

The canonical, programme-independent EA interfaces are maintained in [04 — General Functional Interfaces & Agentic Security v0.5 Integrated](../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md).

This package begins **after** that general interface layer:

```text
EA canonical architecture
    ↓
04 General interfaces — programme-independent
    └─ 04 delta/review — generic interface changes only
    ↓
FG-TIDA application package
    ├─ 05 ideal FG-TIDA cross-Theme mapping
    │   └─ 05 ideal delta — maximum coherent target
    ├─ 05A current-state FG-TIDA mapping
    │   └─ 05A delta — current public-evidence mask over 05
    ├─ Charter / WG preparation
    ├─ Specification preparation
    ├─ FG-TIDA-specific cases
    └─ FG-TIDA-specific tests/provenance
```

Theme numbers, FG-TIDA-specific ownership assumptions and current public discussion state belong here, not in the canonical general interface definition.

## Ideal versus current FG-TIDA interface rule

- [**05 — ideal FG-TIDA projection**](./interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) + [**05 Ideal Delta**](./interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md): the target architecture if the relevant Theme semantics, semantic owners, implementations and review/test capacity were available. It is the **maximum coherent application of 04 to FG-TIDA**, not a claim about present adoption.
- [**05A — current FG-TIDA bridge**](./interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md) + [**05A Current-State Delta**](./interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md): a **current-state filter over 05**, retaining only what the public FG-TIDA record presently supports and downgrading the rest to candidate, test-only or not established.

05 and 05A intentionally overlap heavily because they describe the **same target architecture at different maturity levels**. 05A is not an alternative design. The difference between them is the current evidence/adoption gap.

A current-source limitation in 05A does not weaken 04 or invalidate 05; conversely, an ideal 05 field does not become an FG-TIDA requirement merely because EA can express it.

## Case boundary

The four **UC-EA-01…04 architecture-validation profiles remain in the general EA corpus** because they test EA responsibilities independent of whether FG-TIDA adopts the architecture.

This package contains only case/test material whose meaning is specifically tied to FG-TIDA, such as:

- the DAOS model-case mapping and FG-TIDA ToR/use-case context;
- Theme #13 / UC #4 interoperability tests; and
- FG-TIDA public provenance.

The parent DAOS contribution remains separately preserved under the repository's [FG-TIDA submissions library](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/README.md).

## Status

Preparation and contributor-level research only. This package is not an FG-TIDA Working Group, charter, deliverable, specification, adopted interface or ITU-T position.

## Cumulative application-state note — 24 September 2026

This FG-TIDA package is an **application snapshot over the broader evolving EA/Positioning corpus**, not a promise that every later general-architecture development is already represented in FG-TIDA terms.

- **05 ideal + 05 ideal delta** preserve the maximum coherent cross-Theme target architecture.
- **05A current-state bridge + 05A delta** record the dated/current public-evidence mask over that same target architecture.
- **Specification preparation v0.3** is the current draft mapping of the source corpus into a possible future specification structure; it adds the Decision Boundary / evidence-strength conformance route and the current UC-6 → UC-4 executable-profile convergence. v0.2 remains preserved as the predecessor snapshot.
- Later general work on participant-local positioning, ACC, signalling/choreography, the objective-conditioned gradient, 00G and Canonical MSCA Operation/Repositioning does not become an FG-TIDA requirement or adopted Theme contract merely because it exists in the same repository.

Future interface updates should first distinguish whether they change the **ideal target (05 delta)** or only the **current evidence/maturity mask (05A delta)**. Specification/charter material should consume those layers rather than collapsing them, while earlier snapshots remain preserved for comparison. Test/conformance development should remain in `tests/` until the relevant WG/external-owner process promotes any property into normative specification text.
