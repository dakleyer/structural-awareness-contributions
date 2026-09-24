# FG-TIDA interface projection

> **Navigation:** [Iván Abril Palma](https://github.com/dakleyer/dakleyer) → [Structural Awareness](https://github.com/dakleyer/structural-awareness-contributions) → [Ecosystem Awareness](../../README.md) → [FG-TIDA application package](../README.md) → **Interface projection**

This folder contains the **FG-TIDA application of the general EA interface architecture**. It does not define the generic EA interfaces; those live in 04.

## Three-layer reading rule

### 04 — programme-independent EA interfaces

Start with:

- [**04 — General Functional Interfaces & Agentic Security v0.5 Integrated**](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md)
- [**04 vNext Review & Delta**](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md)

04 defines the generic producer/consumer, Operational Agent Plane, Trust & Security Plane, EHD and conformance semantics. **No FG-TIDA Theme owns or changes 04.** If an FG-TIDA case exposes a genuinely generic gap, it returns upstream to the 04 delta.

### 05 — ideal FG-TIDA projection

Then read:

1. [**05 — FG-TIDA Ideal Cross-Theme Interface Contracts v0.4**](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) ([part 2](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part02.md), [part 3](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part03.md)) — frozen ideal mapping baseline.
2. [**05 Ideal Interfaces vNext Review & Delta v0.1 Draft**](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) — cumulative **maximum ideal FG-TIDA projection**, assuming the relevant Themes, semantic owners, implementations, reviewers and test capacity are available.

05 answers:

> **If FG-TIDA could fully realize the 04 architecture with mature Theme-owned semantics, what would the best coherent cross-Theme interface architecture look like?**

It may therefore be richer than what FG-TIDA can support today.

### 05A — realistic/current FG-TIDA projection

Finally read:

3. [**05A — FG-TIDA Current-State Interface and Conformance Bridge v0.1**](./05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md) — dated 19 September current-state snapshot.
4. [**05A Current-State vNext Review & Delta v0.1 Draft**](./05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) — updates the current-state mask as public FG-TIDA evidence changes.

05A is **not a separate architecture**. It starts from 05 Ideal and asks:

> **Which parts of that ideal architecture are actually defensible from the public FG-TIDA state now?**

It therefore classifies ideal relations as:

- **Current source state**
- **Candidate cross-Theme field**
- **Test-only evidence**
- **Not established**

A 05A limitation does not weaken 04 or invalidate 05. It identifies the current **maturity/adoption gap** between the ideal FG-TIDA architecture and the public state of the Focus Group.

## Control order

**00 Requirements → 00 Delta → 04 General Interfaces → 04 Delta → 05 Ideal → 05 Ideal Delta → 05A Current-State → 05A Current-State Delta**

The three layers must not be collapsed:

- **04** = generic EA interface architecture;
- **05** = ideal FG-TIDA application of 04;
- **05A** = realistic/current FG-TIDA subset of 05.

Theme numbers and Theme-specific ownership belong only in 05/05A, never in the technical semantics of 04.
