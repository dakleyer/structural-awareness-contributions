# Ecosystem Awareness — FG-TIDA application package

> **Navigation:** [Iván Abril Palma](https://github.com/dakleyer/dakleyer) → [Structural Awareness](https://github.com/dakleyer/structural-awareness-contributions) → [Ecosystem Awareness](../README.md) → **FG-TIDA application package**


> **FG-TIDA-specific application package.** This folder is deliberately separate from the general Ecosystem Awareness canonical architecture. It records how EA is being projected into the current FG-TIDA process, what an ideal FG-TIDA mapping would look like, what the public source state currently supports, and which FG-TIDA-specific cases/tests are available. Nothing in this package changes the general EA architecture by itself.

## Read in this order

1. [**Working Group / Phase 2 Charter preparation**](./charter/THEME_13_WORKING_GROUP_CHARTER_PREPARATION_DRAFT_v0.1.md) — candidate Theme #13 charter/WG structure for review; not submitted and not an established WG.
2. [**Specification preparation**](./specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md) — current source-to-specification map, normative maturity, Decision Boundary / cross-Theme conformance route, readiness gates and candidate document structure.
3. [**FG-TIDA interfaces**](./interfaces/README.md) — separates the **ideal FG-TIDA cross-Theme projection** from the **currently defensible public-source bridge**.
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
    ↓
FG-TIDA application package
    ├─ Charter / WG preparation
    ├─ Specification preparation
    ├─ 05 ideal FG-TIDA cross-Theme mapping
    ├─ 05A current-source-constrained FG-TIDA mapping
    ├─ FG-TIDA-specific cases
    └─ FG-TIDA-specific tests/provenance
```

Theme numbers, FG-TIDA-specific ownership assumptions and current public discussion state belong here, not in the canonical general interface definition.

## Ideal versus current FG-TIDA interface rule

- **05 — ideal FG-TIDA projection:** what the bilateral cross-Theme contracts would look like if the participating Theme semantics were available and agreed.
- **05A — current FG-TIDA bridge:** the maximum mapping currently defensible from public FG-TIDA sources, with unsupported or unconfirmed fields kept candidate / not established.

05A may be narrower than 05. A current-source limitation does not weaken the general EA architecture; conversely, an ideal 05 field does not become an FG-TIDA requirement merely because EA can express it.

## Case boundary

The four **UC-EA-01…04 architecture-validation profiles remain in the general EA corpus** because they test EA responsibilities independent of whether FG-TIDA adopts the architecture.

This package contains only case/test material whose meaning is specifically tied to FG-TIDA, such as:

- the DAOS model-case mapping and FG-TIDA ToR/use-case context;
- Theme #13 / UC #4 interoperability tests; and
- FG-TIDA public provenance.

The parent DAOS contribution remains separately preserved under the repository's [FG-TIDA submissions library](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/README.md).

## Status

Preparation and contributor-level research only. This package is not an FG-TIDA Working Group, charter, deliverable, specification, adopted interface or ITU-T position.

## Cumulative application-state note — 23 September 2026

This FG-TIDA package is an **application snapshot over the broader evolving EA/Positioning corpus**, not a promise that every later general-architecture development is already represented in FG-TIDA terms.

- **05 ideal** preserves the candidate ideal cross-Theme projection.
- **05A current-state bridge** records what was defensible from the dated public FG-TIDA source state used by that bridge.
- **Specification preparation v0.3** is the current draft mapping of the source corpus into a possible future specification structure; it adds the Decision Boundary / evidence-strength conformance route and the current UC-6 → UC-4 executable-profile convergence. v0.2 remains preserved as the predecessor snapshot.
- Later general work on participant-local positioning, ACC, signalling/choreography, the objective-conditioned gradient, 00G and Canonical MSCA Operation/Repositioning does not become an FG-TIDA requirement or adopted Theme contract merely because it exists in the same repository.

Future FG-TIDA updates should therefore be made as explicit dated revisions to 05A/specification/charter material, while preserving the earlier application snapshot for comparison. Test/conformance development should remain in `tests/` until the relevant WG/external-owner process promotes any property into normative specification text.
