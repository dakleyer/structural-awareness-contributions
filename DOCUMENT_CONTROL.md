# Corpus Document Control — DC-GH-01

**Edition:** v1.0 · **Effective:** 25 October 2026 (owner-authorized GitHub publication)  
**Owner:** Iván Abril Palma · **Scope:** dakleyer/structural-awareness-contributions  
**Status:** Current repository document-control policy. **Implementation is progressive; publication is not a claim of corpus-wide conformity.**

**Latest conformity audit:** [25 October 2026 audit](./governance/DOCUMENT_CONTROL_CONFORMANCE_AUDIT_2026-10-25.md) · [VNext-link baseline inventory](./governance/review/DOCUMENT_CONTROL_VNEXT_LINK_INVENTORY_2026-10-25.json).

**Preserved predecessor:** [DOCUMENT_CONTROL v1.1, complete pre-consolidation text](./governance/preserved-public-snapshots/2026-10-25_DOCUMENT_CONTROL_v1.1_PRE_CONSOLIDATION.md). The [24 October v0.1 conventions](./governance/CORPUS_DOCUMENT_CONTROL_CONVENTIONS_v0.1.md) are a historical predecessor, not an independently operative second policy.

This document consolidates the repository's documentary identity, classification, navigation, VNext, preservation and maintenance rules. It replaces the operative document-control instructions scattered across the prior two controls, **without replacing domain-specific scientific, freeze, review or institutional requirements**.

## 1. Authority, scope and precedence

This file is the single current repository-wide rule for document identity, role, lifecycle, canonical/VNext relationships, document navigation, controlled changes and technical document-control verification.

The [Corpus Review Procedure](./governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) remains authoritative for the **method of substantive document reviews**, including human-readable review passes and specific before/after proposals. [Claim and Attribution Boundaries](./governance/CLAIM_BOUNDARIES.md) govern the proper qualification of scientific, institutional and external claims. The [EA Canonical Corpus Manifest](./research/ecosystem-awareness/baseline/CANONICAL_CORPUS_MANIFEST.md) and applicable source-specific freeze, release, provenance and custody records govern **their own identified sources and editions**, not all repository documents.

Preserve signed, frozen, submitted and preregistered source obligations within their exact scope. An owner-authorized file-specific restriction may be stricter than this general policy; it must be visible in the source or register. No generic cleanup instruction silently overrides such restrictions.

## 2. GitHub is the technical change record

Use GitHub commits, diffs, file revisions, pull requests, issue links, reviews and workflow results for technical provenance. Do **not** duplicate their timestamps, changed-path lists or revision SHAs in every Markdown header or in a continuously appended administrative log.

Explicit dates and edition labels are appropriate when they carry **semantic** meaning: a formal decision, scientific cutoff, research freeze, edition applicability, external submission or institutional effective date. A commit timestamp is not an approval, experimental observation or date of institutional effect.

GitHub publication, merge, issue label and a passing check do not themselves establish scientific validity, owner approval, operational readiness, external endorsement or institutional adoption. Cite a pinned commit when historical interpretation or exact public content matters.

## 3. Keep identity, role, lifecycle and claim status separate

1. **Logical identity:** which subject/document is owned, independently of its filename or location.
2. **Document role:** canonical, VNext, optional/contextual, router/control, evidence/execution, historical source or external submission.
3. **Lifecycle/edition:** active working, under review, frozen, historical, superseded or released within a declared scope.
4. **Claim maturity:** definition, hypothesis, proposal, analytical/model result, executed observation, independently reviewed result or unresolved question, as supported by the source.

**Canonical** means the current primary reading source for a defined logical subject and scope. It does **not** mean scientifically demonstrated, legally binding, independently validated, institutionally received or adopted by FG-TIDA/ITU or another external body. A canonically recorded hypothesis remains a hypothesis. Roles and lifecycle states may overlap: a canonical document may be frozen for one exact edition; a README may be a canonical router.

## 4. Minimal logical-document register

The repository shall progressively maintain a machine-readable DOCUMENT_REGISTRY.yml (to be created in Wave 1; not yet present) as the single operational mapping for identities and role-dependent checks. **Its nonexistence or incomplete coverage is an audit finding, not grounds to invent document roles.**

For registered sources, use only the fields needed to disambiguate: stable logical ID, repository path, role, lifecycle, accountable owner where required, canonical companion/owner relation for VNext, protection mode and approved blob for specially protected files, and relevant decision/exception reference when material. A current logical canonical may have **at most one active VNext**. Historical versions and historical VNext records may remain preserved under their exact editions but must not be counted as additional active companions.

A logical ID must not silently denote two competing current canons. A relocation retains the logical ID; a genuine split or new subject requires a justified identity/lineage decision. Filenames and path suffixes are useful hints, never sufficient proof of canonicality. Ambiguous or unregistered roles shall be reported as **unclassified**, not assumed to be compliant or noncompliant.

Do not rename all existing files, duplicate Git technical timestamps/SHA in document headers, or backfill every contextual record. Register first the protected sources, controlled routers, active canonical/VNext pairs and other documents needed to evaluate actual link findings.

## 5. Canonical and VNext link contract

A VNext is the cumulative review/development shadow **of a specific logical canonical document**. Repeated review passes remain in that one active shadow. A VNext of a VNext is not permitted.

| Source | Direct link to own VNext | Direct link to foreign VNext | Links to canonical, contextual or evidence sources |
| --- | --- | --- | --- |
| Canonical (including canonical router) | Allowed; normally once, when safely editable | **Not allowed** | Allowed |
| VNext | No VNext-of-VNext | **Allowed** | Allowed |
| Optional/contextual | Allowed | **Allowed** | Allowed |
| Historical/frozen | Preserve original edition; do not retrofit | Preserve historical citations | Preserve original references |

A canonical document may therefore reference other canonical, optional, contextual, scientific, evidential and historical materials; **among VNext documents, it may directly reference only its own companion VNext**. Cross-VNext review links and optional/contextual-to-VNext references are legitimate and useful for development of the next corpus. Label proposals clearly when the reader could mistake them for adopted content.

If a canonical source is frozen or externally signed, use its authorized reader index or review card to expose the current review route instead of altering frozen bytes. A hyperlink neither promotes the linked proposal nor transfers document ownership or approval.

## 6. Navigation ownership and preservation

Keep the public programme navigation distinct from internal technical reading routes:

- **Public route:** Iván Abril Palma profile → Structural Awareness Programme → four human programme areas (Mathematical Contributions; Field Notes/Research Series; Field Practice/Engineering; Architectural Contributions/pre-standardization) → Ecosystem Positioning.
- **Technical architecture:** Ecosystem Positioning routes to Ecosystem Awareness, Regime Awareness and Minimum Sufficient Control, with their own canonical technical indexes, work packages, evidence and applications.

Each controlled navigation family has one owner. Cross-links do not transfer ownership. The existing nine controlled navigation owner paths are the transitional baseline: root README; Ecosystem Positioning README; EA entry README; EA baseline README; EA FG-TIDA README; RS-00E-Q1a fixture README; Regime Awareness README; MSCA README; submissions README. The register shall identify these explicitly. Other package READMEs may describe executable packages without becoming extra programme-level navigation owners.

Do not delete or merge a README merely to reduce its numerical count. Moves, renames, splits, consolidation and hierarchy changes require scoped authorization, preserved source content, inbound-link/anchor assessment, reader continuity and exact before/after verification. Current README and link counts should be **generated**, not manually restated as invariant numbers.

## 7. Review, incorporation and promotion

Use a bounded GitHub issue or pull request to identify the proposed source, reason, material before/after difference, affected consumer meanings and relevant decision authority when substantive or structural change is intended. GitHub already records the technical authoring and file diff. A reviewer must distinguish AI-assisted analysis, human decision and independent external review.

The responsible owner expressly accepts, rejects or defers material proposals before their promotion. Incorporation edits only the approved living canonical target and any authorized consumers, preserving historical editions, external statuses, claims, results and link anchors. Promotion of a **canonical hypothesis** never upgrades it automatically into an experimentally established result.

Routine editorial fixes should have proportionate checks; do not create institutional approval steps for every spelling or link correction. External communications, standards submissions and institutional adoption remain subject to their distinct authority gates.

## 8. Protected, append-only, frozen and historical sources

A registered protection rule may specify owner-gated changes, append-only content, byte-frozen evidence, or historical preservation. The EA entry README and Ecosystem Positioning README have existing owner restrictions; the Ecosystem Positioning Development Strategy additionally carries an append-only instruction in the preserved control history. These protections remain effective pending precise register reconciliation.

For a **specially SHA-protected file**, maintain one current *approved* blob SHA in the register after a verified owner decision; older editions remain in Git history or relevant custody records. A different observed SHA is a finding to investigate, **not** an instruction to overwrite the expected SHA or restore the predecessor. Acceptance of a successor, corrective replacement or deferred review must be explicitly recorded.

Where exact binary/data/frozen bytes matter, preserve their applicable study-specific hashes, pinned sources and custody manifests. Git revision history alone is not a substitute for institutionally authentic records, cryptographic signatures or externally controlled originals.

## 9. Technical checks and enforcement

Extend the **existing** documentation-integrity workflow and script instead of creating a competing control mechanism. Build staged checks for:

1. Logical ID and path uniqueness; missing or conflicting current canonical/VNext relationships.
2. VNext-of-VNext and mutable canonical → foreign VNext direct links.
3. Existing Markdown path integrity and protected router/navigation checks.
4. Special protected SHA and append-only constraints where executable.
5. Bounded reports of link occurrences, distinct edges, source files, declared classes, exceptions and unclassified sources.

Keep the broad documentation link checker on pull requests/manual runs unless its false positives and notifications are separately resolved. A lightweight protected-file check may also run on pushes, but **post-push detection alone does not prevent a change**. Genuine merge-time enforcement requires applicable GitHub branch/ruleset controls and required checks/reviews to be configured and verified.

A green CI result certifies only the checks actually run. Missing classifications, frozen exceptions and semantic claims require separate human assessment; do not claim complete corpus reconciliation from a passing link scan.

## 10. Institution and programme boundaries

This public research corpus has a technical GitHub document authority, not automatic normative authority for The Integral Management Society.

When an IMSV body formally adopts a document under its applicable statutes, the institutional record, authenticated exemplar, scope, date and registered reception (*Receptio*) remain under the **IMSV institutional system**. GitHub may reference that decision; it must not create a parallel institutional register or infer adoption from a merge. Canonical research documentation needs no Receptio unless an institutional norm is actually being enacted.

No GitHub link or publication implies approval, validation or adoption by FG-TIDA, ITU, WIPO, a university, funder, industry organization or technology provider.

## 11. Exceptions, conservation and historical citations

Retain superseded sources, review records, submitted packets, frozen tests and negative results for their exact provenance. Historical links may legitimately point to older paths or pinned Git commits. Do not silently rewrite historical records for a current link-style convention.

Record any exception with its scope, source, justification, responsible decision and reference. Avoid a separate administrative log of all commits; issues/PRs and Git history already provide that trail. Use a distinct record only where the semantic decision cannot be inferred from the technical change.

## 12. Bounded rollout and acceptance

- **Wave 0 — effective policy and custody:** preserve predecessor texts, publish this single current policy and audit link, identify protected-source discrepancies. No mass corpus changes.
- **Wave 1 — read-only inventory:** enumerate VNext references; distinguish occurrences, unique edges, source roles and historical citations. Resolve identity ambiguities before labeling violations.
- **Wave 2 — safeguards:** register relevant logical identities, extend the existing check, and configure enforceable review/branch settings proportionately.
- **Wave 3 — approved corrections:** amend only confirmed incompatible mutable canonical links and ownership ambiguities, in small evidence-backed PRs.
- **Wave 4 — conformance closure:** rerun checks, record unresolved exceptions/owner decisions, verify actual GitHub enforcement, and close the follow-up only to its demonstrated scope.

The [dated conformance audit](./governance/DOCUMENT_CONTROL_CONFORMANCE_AUDIT_2026-10-25.md) is the **baseline of actual versus required state** and remains linked from this policy. It is not a certification of scientific results or institutional norms.

## 13. Maintenance

This file is the one active repository-wide document-control policy. CONTRIBUTING and routing READMEs should link here without copying competing control rules. The Corpus Review Procedure governs substantive audit method; scientific and frozen-source manifests retain their own narrow source authority.

Amendments require a scoped GitHub change record and responsible-owner decision where relevant. Git supplies technical modification dates; do not keep a manually updated changelog inside this current policy. Preserve previous approved editions and their reader links.
