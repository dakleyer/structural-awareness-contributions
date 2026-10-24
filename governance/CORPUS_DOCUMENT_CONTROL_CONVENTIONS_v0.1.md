# Corpus document control — identity, status, editions and links

> **Control ID:** DC-GH-01 · **Edition:** v0.1 · **Date:** 24 October 2026  
> **Owner:** Iván Abril Palma · **Prepared with:** Codex (AI) · **Status:** owner-directed repository convention; progressive implementation  
> **Scope:** `dakleyer/structural-awareness-contributions`, including the EA, Regime Awareness, MSCA and FG-TIDA research/application packages.

This procedure identifies which document a reader should rely on, what is still under review, which version is being discussed and how documents may reference one another. It **complements, rather than replaces,** the repository [Document Control](../DOCUMENT_CONTROL.md) and the [Corpus Review Procedure](./CORPUS_REVIEW_PROCEDURE_2026-10-06.md). Existing freeze, preservation, protected-README, external-owner and submission rules continue to govern their own materials. No bulk reclassification, rename, rewrite or link migration is authorized merely by publishing this convention.

## 1. Principle: identity, authority and evidence are different

Keep four questions separate:

1. **Identity and source:** Which logical document owns the subject, and where is its current authoritative *reading* source?
2. **Edition and lifecycle:** Which version and Git revision are being cited? Is it working, under review, frozen or preserved history?
3. **Document role and applicability:** Is it canonical, VNext, optional/contextual, a review/provenance record, evidence or an external submission? Who, if anyone, has adopted it for a specified scope?
4. **Claim status:** Is a statement a definition, research hypothesis, candidate design, test-only observation, established result or an unresolved question?

“Canonical” here means the controlled primary reading reference for the indicated document family and scope. It **does not, by itself, mean scientifically validated, institutionally approved, mandatory, implemented or adopted by FG-TIDA or another body**. A *canonically recorded research hypothesis* remains a hypothesis.

This distinction is informed by The Integral Management Society's consolidated statutes, notably Article 15 on identifiable versioned corpora, authentic exemplars, dependencies and registers of application. It is a **technical convention for this GitHub corpus**, not an assertion that GitHub publication enacts a Society-level decision or satisfies the Society's separate institutional document-and-register procedure.

## 2. Minimum document classes

| Class | Meaning | Reader treatment |
| --- | --- | --- |
| **CANONICAL** | Primary current source for a defined logical subject and scope, whether working or controlled/frozen. | Cite the identified edition; inspect its claim/evidence status. |
| **VNEXT** | One cumulative review/development **shadow** of one logical canonical document. Holds audits, proposals, before/after deltas and recorded decisions. | Consult for ongoing development; not an automatic replacement or normative amendment. |
| **OPTIONAL / CONTEXTUAL** | Additional explanation, exploration, comparison, reading aid or background outside the primary reading route. | Useful for context; cannot silently redefine its canonical sources. |
| **HISTORICAL / PRESERVED** | Earlier editions, frozen snapshots, archived paths or custody records retained for lineage. | Cite with an edition/commit when historical meaning matters; do not silently modernize. |
| **EVIDENCE / EXECUTION** | Fixtures, data, run logs, results, preregistrations, test artefacts and their custody records. | Preserve actual run/state; a passing check does not by itself validate a wider claim. |
| **CONTROL / ROUTER / SUBMISSION** | Procedures/manifests/reader entrances, or an explicitly identified external packet. | Control navigation or provenance only within declared ownership and acceptance scope. |

Classes describe roles, not a single hierarchy of scientific validity. A README can also be a canonical router; a frozen file can be canonical for its own controlled release. Use existing source-specific labels (`Current source state`, `Candidate`, `Test-only evidence`, `Not established`, etc.) where already defined instead of inventing a conflicting vocabulary.

## 3. Link rules

The restriction applies to **canonical documents as sources of links**, not to every document in the repository.

| Source document | Links to its own VNext | Links to other VNext | Links to other canonical documents | Links to optional/contextual or historical sources |
| --- | --- | --- | --- | --- |
| **Canonical** | **Yes — one explicit direct link** when the source can be safely updated | **No** | Yes | Yes |
| **VNext** | **Not applicable — no VNext of a VNext** | **Yes** | Yes | Yes |
| **Optional / contextual** | Yes | **Yes** | Yes | Yes |
| **Historical / frozen** | Preserve the edition as it was; do not impose retrospective changes | Preserve historical references | Preserve historical references | Preserve historical references |

Detailed rules:

- A canonical document may link to other canons, optional or contextual texts, research notes, evidence, history and external sources. **Among VNext files, it links only to the VNext it owns, directly and normally once**, preferably in a short opening review notice.
- A VNext may link to **other VNext files**: cross-document research, reciprocal findings and a developing next corpus require this. Such links do not promote the receiving proposal into any canon.
- Optional/contextual documents may link directly to VNext files when that is the relevant analysis. Mark the target as *review/proposal* when the distinction matters to the reader.
- A VNext is paired with **one logical canonical owner**. Repeated review passes accumulate in that same VNext; do not create a VNext of a VNext.
- **Controlled/frozen, signed, submitted, pre-registered or hashed originals must not be edited just to add the review notice.** Where necessary, the authorized canonical owner index or review card provides the route, without rewriting the original.
- No link alone creates approval, validates evidence, transfers semantic ownership or imports an external programme's authority.
- In active prose, cite the canonical source for **current semantics**. If a specific claim exists only in VNext, state that it is *proposed/under review* and cite its actual review source where this document class permits. Do not imply that the canonical text already contains it.
- Historical citations may point to a preserved path or **pinned commit** when reproducing what an earlier edition actually said. Do not reinterpret those links as current directions.

### Example: allowed and disallowed

**Canonical 01B (allowed):** `[01B VNext](./01B_VNext.md)` and `[01C canonical](./01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md)`.

**Canonical 01B (not allowed):** a direct link to `01C_VNext.md`; point instead to 01C's canonical source, with a plain-language note if its additional review matters.

**01B VNext (allowed):** `[01C VNext](./01C_VNext.md)` for a reciprocal review; also link to the 01C canonical source to identify the authoritative current semantics.

**Optional comparison (allowed):** direct links to both `01B_VNext.md` and `01C_VNext.md`, labeled as proposals or review records rather than adopted interfaces.

## 4. Minimal metadata and notation

Existing descriptive filenames, numbering and stable external citations remain valid. **Do not rename files or backfill every source** to introduce this convention. For new or substantially touched living documents, record the fields that materially disambiguate use:

| Field | Purpose | Example |
| --- | --- | --- |
| Logical ID / family | Stable identity distinct from path or edition | `EA:01B` (notation example, not a retroactive renaming) |
| Title / role | Human-readable subject and class | `EA/MSCA Interface Annex · CANONICAL` |
| Edition / state | Version plus working, review, frozen or preserved status | `v0.2 · working` |
| Semantic owner / maintainer | Who governs this claim set or document family | `EA document owner` |
| Source path and Git revision | Exact edition for evidence or historical citation | repository path + commit SHA |
| Companion / dependencies | Canonical↔own VNext; typed source/consumer relations | `01B ↔ 01B_VNext` |
| Decision / applicability | Recorded authorization, scope/date and any exclusions | `approved editorial change` or `proposal only` |
| Evidence / claim boundary | What it establishes and what it does not | `research hypothesis; not experimentally confirmed` |
| Sensitivity / language | Public/internal/controlled, language or translation status when material | `public · English` |

For an editable Markdown document, a **small visible note** may suffice, rather than a large mandatory YAML block:

> **Document control:** `EA:01B` · **Role:** Canonical working · **Edition:** v0.2 · **Owner:** EA · **Review:** [own VNext](01B_VNext.md) (example for a file located alongside its VNext).

For a VNext, identify the canonical source it shadows, its draft/review status, the real reviewer(s), the date and the scope of each review pass. When useful, issue/PR labels may mirror the documented role (for example, `doc:canonical`, `doc:vnext`, `doc:context`, `change:editorial`, `change:substantive`); **these are suggested future labels, not labels created by this edition**. An issue label, branch name, path suffix or passing CI badge never determines adoption by itself. For historic or binary files, use an external register/review card instead of modifying protected bytes. Machine-readable inventories/checks may be added later; they must not displace human-readable explanations.

## 5. Changes, promotion and provenance

1. **Review:** record source passage, reviewer and date, claim/evidence limitations, cross-document effects and a literal before/after proposal in the owning VNext where applicable.
2. **Decision:** the responsible owner expressly accepts, rejects or defers each substantive or structure-changing proposal for a stated scope. An AI review, link change, Git commit or merge is not independent scientific validation.
3. **Incorporation:** edit only the approved living canonical target(s), with preservation of earlier claims, definitions, historical releases, anchors and external statuses. A research hypothesis may be promoted as a **canonical hypothesis**, not as a demonstrated causal or compute result.
4. **Trace:** record changed paths, reason, decision reference, version/Git commit and affected readers; update the relevant register or router only when needed.
5. **Verification:** inspect actual semantic diff, protected-file integrity, source→consumer meaning, relevant links and rendered/readable result. Preserve original experimental data, negative results and frozen editions.

Git history is the public change and provenance mechanism for this repository, not a substitute for an institutional adoption record or a controlled Google Drive revision where one remains authoritative. Maintain exact SHA references when legal, scientific, release or external-citation integrity depends on them.

## 6. Rollout by bounded waves

**Wave 0 — control baseline (this edition).** Publish this convention and a pointer from the existing `DOCUMENT_CONTROL.md`. Do not rename, relocate or rewrite documents; do not change the technical corpus's claims or its VNext graph.

**Wave 1 — inventory and triage (read-only).** Enumerate the reported ~120 direct VNext references and classify each by *source role*, *target owner*, *live versus historical* and *semantic purpose*. Count link occurrences separately from distinct files and proposed edits. Identify ambiguous ownership and cases that require a human reading.

**Wave 2 — canonical-origin corrections.** Only for current, editable canonical sources, review direct links to **foreign** VNext. Where appropriate, route to the foreign canon and describe pending review without falsely attributing a proposal to the canon. Preserve links to each document's *own* VNext. Obtain exact owner approval before edits constrained by protected routes, freezes or substantive interpretation.

**Wave 3 — contextual clarity.** Leave lawful VNext↔VNext and optional/contextual→VNext links intact. Improve only misleading labels, broken paths, incomplete statuses or ownership ambiguity, in bounded reviewed sets. Do not treat every cross-reference as an error.

**Wave 4 — light automation and closure.** Add a report/CI check for mutable canonical→foreign-VNext direct links, missing own-companion routes where required, broken paths and duplicate logical VNext. Exclude frozen/pinned historical revisions from prospective enforcement. Record exceptions with owners and dates; do not declare “corpus reconciled” on the strength of link checks alone.

For each wave: agree the file set first, preserve the predecessor Git revision, produce exact before/after changes, verify source integrity and record what was *not* changed. A wave may be limited to one family or a small group of documents.

## 7. Conflict resolution

The existing repository `DOCUMENT_CONTROL.md` remains the primary navigation/preservation control. This companion describes document classes, editions and link permissions. The Corpus Review Procedure remains the method for substantive audits and reciprocal findings; **its invitation to link the same finding between VNext files is compatible with this convention**, because the prohibition concerns only *canonical-origin* links to **foreign** VNext.

If an earlier conversation or generic cleanup instruction can be read as forbidding all VNext cross-links, that restriction is superseded here by Iván's clarification of 24 October 2026. Where an existing frozen source or programme-specific rule conflicts with a generic suggestion in this file, preserve the source, record the conflict and request an explicit owner decision; do not silently overwrite the older document.

This is an **initial, proportionate GitHub document-control convention**. It establishes a readable source-of-truth model and a staged migration method; it does not certify that all existing links, reviews or records already comply.
