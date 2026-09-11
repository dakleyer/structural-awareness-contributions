# Ecosystem Awareness — Canonical Public Corpus

> **Public mirror of the controlled Ecosystem Awareness corpus.** This repository preserves the complete current canonical/release baseline, the current validation freeze, the preserved research lineage and the public provenance material defined in Google Drive. It is contributor-level research and pre-standardization material: it is **not** an ITU-T deliverable, Recommendation, adoption statement, certification, or institutional endorsement.

**Public corpus freeze:** 11 September 2026  
**Controlled baseline freeze:** 10 September 2026  
**Maintainer:** Iván Abril Palma / Tegrity.AI / The Integral Management Society

## Start here

Agents and reviewers should read in this order:

1. [`CANONICAL_CORPUS_MANIFEST.md`](./CANONICAL_CORPUS_MANIFEST.md) — exact scope, Drive source IDs/revisions, current/superseded rules and corpus structure.
2. [`CORPUS_FILE_INVENTORY.sha256.md`](./CORPUS_FILE_INVENTORY.sha256.md) — SHA-256 inventory of every file in the exact complete public bundle.
3. [`baseline/`](./baseline/) — canonical architecture baseline.
4. [`validation/`](./validation/) — the Validation Profile Family, UC-EA-01…04 and EA-ITP-01.
5. [`governance/`](./governance/) — freeze and maintenance-freeze controls.
6. [`lineage/`](./lineage/) — preserved derivation, Articles 01–05, predecessor architecture and conservation records.
7. Public provenance material and the linked Parent Case Study.

The complete corpus is also preserved as one SHA-verifiable machine-readable archive:

[`ECOSYSTEM_AWARENESS_CANONICAL_PUBLIC_CORPUS_2026-09-11.tar.gz`](./ECOSYSTEM_AWARENESS_CANONICAL_PUBLIC_CORPUS_2026-09-11.tar.gz)

This archive contains the exact full Markdown files enumerated in `CORPUS_FILE_INVENTORY.sha256.md`, including all six current validation artifacts.

## Corpus boundary — what is included

The public corpus includes the complete controlled research object, not merely an executive extract:

- problem definition and foundational theory;
- epistemic principles, four-pole model and Type 0 / Type 1 / Type 2 control model;
- F1–F9 functional architecture;
- O1–O6 and IF-S1–IF-S13 functional interfaces and EHD semantics;
- provisional cross-theme interface contracts;
- benchmark, prior-art and falsification boundary;
- deep conceptual derivation and Articles 01–05;
- predecessor architecture and conservation/change-control records;
- Validation Profile Family & Traceability;
- UC-EA-01, UC-EA-02, UC-EA-03 and UC-EA-04 in their current frozen/maintenance-frozen versions;
- EA-ITP-01 interoperability test;
- freeze and maintenance-freeze manifests;
- public provenance register;
- the public Parent Case Study package, linked rather than duplicated.

### Deliberate exclusion

The only deliberate exclusion from the frozen corpus is **draft communication intended for future GitHub / FG-TIDA thread actions**: draft comments, ready-to-post replies and unpublished posting copy. Those are working communications, not canonical corpus artifacts. Once actually posted, they become public provenance and may be indexed in a later provenance/corpus release.

## Canonical architecture baseline

The controlling Drive freeze manifest defines six baseline documents:

1. Foundational Theory of Bounded Uncertainty — v0.4
2. Epistemic Safety Principles & Control Matrix — v0.4
3. Functional Architecture — v0.4
4. Functional Interfaces & Agentic Security Integration — v0.4
5. Provisional Cross-Theme Interface Contracts — v0.4
6. Architecture Benchmark & Novelty Audit — v0.4

No one file should be treated as the whole architecture by itself.

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

## Parent Case Study

The public Parent Case Study is part of the corpus evidence chain and remains at:

`submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/`

It is linked rather than duplicated here so that there is one public case source.

## Source-of-truth rule

Drive file ID + revisionId in the freeze manifests remains the controlling content anchor for the controlled release. This GitHub location is the canonical **public mirror / discovery point**.

Do not silently edit a frozen document in place. A substantive successor requires a new version/freeze record and preservation of the previous state.