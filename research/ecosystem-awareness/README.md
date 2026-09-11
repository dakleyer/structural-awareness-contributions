# Ecosystem Awareness — Canonical Public Corpus

> **Public mirror of the controlled Ecosystem Awareness corpus.** This repository preserves the complete current canonical/release baseline and the current validation freeze defined in Google Drive. It is contributor-level research and pre-standardization material: it is **not** an ITU-T deliverable, Recommendation, adoption statement, certification, or institutional endorsement.

**Public corpus freeze:** 11 September 2026  
**Controlled baseline freeze:** 10 September 2026  
**Maintainer:** Iván Abril Palma / Tegrity.AI / The Integral Management Society  
**Institutional context:** The Integral Management Society is a Swiss non-profit association.

## Start here

Agents and reviewers should read in this order:

1. [`CANONICAL_CORPUS_MANIFEST.md`](./CANONICAL_CORPUS_MANIFEST.md) — exact scope, source Drive IDs/revisions, SHA-256 checksums and current/superseded rules.
2. [`baseline/`](./baseline/) — the six complete canonical architecture documents.
3. [`validation/`](./validation/) — the current validation family, four current profiles and the interoperability test.
4. [`governance/`](./governance/) — original freeze and maintenance-freeze controls.
5. [`provenance/`](./provenance/) — public FG-TIDA provenance and status boundaries.
6. [`lineage/`](./lineage/) — preserved derivation/conservation material. Read this for history and rationale, not as a substitute for the current baseline.

## Canonical architecture baseline

The controlling Drive freeze manifest defines six baseline documents:

1. Foundational Theory of Bounded Uncertainty — v0.4
2. Epistemic Safety Principles & Control Matrix — v0.4
3. Functional Architecture — v0.4
4. Functional Interfaces & Agentic Security Integration — v0.4
5. Provisional Cross-Theme Interface Contracts — v0.4
6. Architecture Benchmark & Novelty Audit — v0.4

Together they preserve the problem definition, epistemic principles, Type 0/1/2 taxonomy, four-position epistemic state, F1–F9 architecture, O1–O6 and IF-S1–IF-S13 interfaces, EHD/handoff semantics, cross-theme boundaries, prior-art benchmark and falsification boundary. No one file should be treated as the whole architecture by itself.

## Current validation set

The 10 September maintenance freeze leaves the architecture baseline unchanged and supersedes only UC-EA-02/03/04. The current set is:

- UC-EA-01 v0.3 — Frozen (unchanged)
- UC-EA-02 v0.6 — Maintenance Freeze
- UC-EA-03 v0.4 — Maintenance Freeze
- UC-EA-04 v0.5 — Maintenance Freeze
- Validation Profile Family & Traceability v0.5 — Frozen (unchanged)
- EA-ITP-01 v0.1 — Frozen (unchanged)

The earlier frozen UC-EA-02 v0.5, UC-EA-03 v0.3 and UC-EA-04 v0.4 remain historical evidence in Drive; the maintenance successors above are the current validation versions.

## Frozen architectural invariants

- F1–F9 are the complete top-level Ecosystem Awareness function set; no F10.
- O1–O6 and IF-S1–IF-S13 are the external interface taxonomy; no O7 or Interface S14.
- No Type 3 and no UC-EA-05.
- F2.APQ is a sub-capability of F2, not a new top-level function.
- EHD is the general interoperable epistemic handoff contract; the Theme #13 four-field determinacy envelope is a specialized profile.
- Source-native producer semantics remain authoritative; discussion mappings are not normative translation tables.
- Theme #13 operational blast radius and EA/F5 epistemic dependency / inherited-indeterminacy assessment remain separate responsibilities.
- Theme #16 retains ownership of the implementation-neutral human-oversight/intervention lifecycle.
- Ecosystem Awareness does not create authority, execute containment, or globally rank/certify acquisition or signalling mechanisms.
- Interoperability is tested externally before architecture reopening.

## Public FG-TIDA anchors

- Theme #13 working thread: https://github.com/FG-TIDA/themes/issues/13
- Current public Ecosystem Awareness conceptual / functional milestone: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5585387513
- Placement / foundational-interface acknowledgement by Ward Duchamps: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256
- FG-TIDA Use Case #4, external federated-interoperability fixture: https://github.com/FG-TIDA/use-cases/issues/4

These are public provenance anchors. They do not imply ITU-T adoption of this corpus.

## Source-of-truth rule

The Markdown files here are complete exports of the identified Google Drive documents at the controlled corpus revision. For exact freeze provenance, **Drive file ID + revisionId in the freeze manifest remains the controlling content anchor**. This GitHub directory is the canonical **public mirror** and public entry point.

Do not silently edit a frozen document in place. A substantive successor must have a new version/freeze record and must preserve the previous public state.
