# Document Control — navigation, sitemap and modification rules

**Version:** 1.1  
**Control date:** 28 September 2026  
**Owner:** Iván Abril  
**Scope:** public navigation, README governance, routing integrity, canonical presentations, document moves/renames and editor/bot maintenance rules for `dakleyer/structural-awareness-contributions`.

> **Mandatory maintenance rule.** Any editor, bot or contributor that changes repository navigation, moves or renames a routed document, creates or removes a README, changes a corpus entry path, or changes a canonical presentation **must read this file first, verify the sitemap after the change, and update this file when the controlled structure changes**.

This file is a control artefact, not a public reading level. The canonical public entry remains [dakleyer/dakleyer](https://github.com/dakleyer/dakleyer).

---

## 1. Navigation model

The public information architecture is human-first:

```text
LEVEL 1 — canonical initial entry
https://github.com/dakleyer/dakleyer
        ↓
LEVEL 2 — Structural Awareness Programme
https://github.com/dakleyer/structural-awareness-contributions
        ↓
LEVEL 3 — four human programme routes
Mathematical Contributions
Field Notes / Research Series
Field Practice / Engineering
Architectural Contributions / pre-standardization
        ↓
LEVEL 4 — current architectural contribution
Ecosystem Positioning
        ↓
maintained technical gates / evidence / benchmark / public application routes
```

### Level 1 — canonical initial entry

- [Iván Abril Palma / profile repository](https://github.com/dakleyer/dakleyer)
- Purpose: identify the architect, explain Tegrity.AI as the platform, and route public technical work.

### Level 2 — Structural Awareness Programme

- [Structural Awareness Programme](./README.md)
- Purpose: explain the complete programme to a human reader and route into its four parts.
- The Level-2 README must preserve the four-part programme explanation:
  1. **Mathematical Contributions** — ResearchGate/publication route.
  2. **Field Notes / Research Series** — Tegrity.AI explanatory series and Field Notes.
  3. **Field Practice / Engineering** — Phylons, xSeil and Mobility Operating System / Car Evolution.
  4. **Architectural Contributions / pre-standardization** — current architecture contributions; presently Ecosystem Positioning.
- It may link directly to the defining public sources for those four parts and to the canonical Ecosystem Positioning presentation.
- It must not become a detailed technical file index or duplicate the internal document lists owned by technical corpus routers.
- **Every current or future Level-2 README must contain a direct link to this `DOCUMENT_CONTROL.md` and instruct editors/bots to verify and update it whenever navigation changes.**

### Level 3 — four human programme routes

1. **Mathematical Contributions** — public formal/publication route through ResearchGate.
2. **Field Notes / Research Series** — public explanatory research through Tegrity.AI series and Field Notes.
3. **Field Practice / Engineering** — public engineering route through Phylons, xSeil and Mobility Operating System / Car Evolution.
4. **Architectural Contributions / pre-standardization** — current contribution route through [Ecosystem Positioning](./architectural-contributions/ecosystem-positioning/README.md).

### Level 4 — Ecosystem Positioning technical gates

The Ecosystem Positioning contribution routes to three maintained technical corpora:

1. [Ecosystem Awareness — entry-point router](./research/ecosystem-awareness/README.md)
2. [Regime Awareness — corpus index](./research/regime-awareness/README.md)
3. [Minimum Sufficient Control / MSCA — corpus index](./standards/minimum-sufficient-control/README.md)

Its canonical presentation also links upward to the Structural Awareness Programme and directly to the benchmark and public application references used by the architecture.

Applied-research records and public submissions remain reachable supporting routes, but they are not additional top-level parts of Structural Awareness.

---

## 2. Controlled README count

### Current transitional state

At the current control date, the repository contains **49 README files**. Most of the increase is deliberate local package/fixture documentation (including the 00K executable ablation family), not new top-level navigation nodes. The controlled-navigation target below remains separate from the raw README count.

### Target controlled state

The approved navigation target remains **9 controlled README files**. Local executable-package READMEs may exist below a controlled corpus when they document a runnable fixture/package and are not treated as additional programme-level navigation nodes:

1. `README.md` — Structural Awareness Programme.
2. `architectural-contributions/ecosystem-positioning/README.md` — Ecosystem Positioning architectural contribution landing page.
3. `research/ecosystem-awareness/README.md` — Ecosystem Awareness router.
4. `research/ecosystem-awareness/baseline/README.md` — canonical EA corpus.
5. `research/ecosystem-awareness/fg-tida/README.md` — FG-TIDA application package.
6. `research/ecosystem-awareness/baseline/fixtures/RS-00E-Q1a/README.md` — operative fixture-family index.

**00K package READMEs are local execution documentation, not additional controlled navigation owners.** Their stable public route is owned by the canonical EA corpus and [00K-A17 Documentation, Reproducibility & Proof Map](./research/ecosystem-awareness/baseline/00K_A17_DOCUMENTATION_REPRODUCIBILITY_AND_PROOF_MAP_v0.1.md).
7. `research/regime-awareness/README.md` — Regime Awareness corpus.
8. `standards/minimum-sufficient-control/README.md` — MSCA corpus.
9. `submissions/README.md` — public submissions router.

The remaining README files are **transitional** until their unique content is either:
- absorbed into one of the controlled READMEs;
- renamed to a function-specific document such as `PROJECT.md`, `PACKAGE_MANIFEST.md`, `SUBMISSION_MANIFEST.md`, `CONTRIBUTIONS_INDEX.md` or `NON_CANONICAL_MANIFEST.md`; or
- removed only after all unique information and inbound references have been preserved.

**Never delete a README simply to reduce the count.** The count is reduced only after content and links have been migrated safely.

---

## 3. Protected routers

The following files are explicitly protected by owner instruction:

### Ecosystem Awareness README

`research/ecosystem-awareness/README.md`

**Protected content SHA at control date:**  
`355aa53f088e502993abc8e1ebd9d10e463b509b`

Rule:

- Do not edit, reformat, reorder, rename or normalize this file without explicit new instruction from Iván Abril.
- Maintenance work must route around it.
- If a future explicit instruction authorizes a change, update both the protected SHA and this section immediately.
- **23 September 2026 owner-authorized maintenance:** routed the protected EA entry point to the current 01J signalling successor and reconciled delta/agentic-gradient terminology.
- **23 September 2026 owner-authorized hierarchy reconciliation:** clarified that EA is one of the three maintained technical gates of Ecosystem Positioning.
- **27 September 2026 completeness-review proposal:** the owner requested a renewed completeness/link/coherence review of the EP and EA READMEs, with GitHub as the canonical source. The proposal updates published execution routes and stale dashboard status, retains every prior link and section, and aligns this recorded blob SHA with the proposed EA router. The canonical evidence files are unchanged. Before this proposal, the recorded SHA was stale: published EA at `7775828` had blob `5f7db8204bac312b53fe0f1681e35f2055b5ad05`.

### Ecosystem Positioning README

`architectural-contributions/ecosystem-positioning/README.md`

**Current protected content SHA — 29 September 2026 minor evaluator maintenance:**  
`035ba43ef0e78179cf06908e8e8b2a5ecda233cb`

This entry supersedes the earlier SHA entries below. Added one link to the targeted input-validation maintenance record under the existing follow-up route. Prior router text, Word documents and historical result files are preserved. The corrected evaluator retains its previous version in Git history. Navigation ownership and README counts are unchanged.

**Current protected content SHA — 29 September 2026 follow-up audit 0.4.1:**  
`91780f8381923d32e75356bc9a70de696dcc3dc7`

This entry supersedes the earlier SHA entries below. Added links to the preserved-document update 0.4.1 and follow-up input/assumption checks under the same document route. All prior README and control text, evidence files and document versions remain unchanged. No navigation owner or README count changes.

**Latest protected content SHA — 29 September 2026 owner-authorized audit extension:**  
`b7cf618b7b05c4ce3d53e00534aa7edbb40b4f53`

This latest SHA supersedes both earlier protected SHA entries below. Added the traceability audit update 0.4 and its executable evidence package under the existing `documents/2026-09-29/` route. All prior README and Document Control text, the original three Word files and the protected technical corpora remain unchanged. No README is created or removed; the navigation owner and counts remain unchanged.

**Protected content SHA at control date:**  
`13cf9ceeea232eb318e9ae5dae4f16625f931fa2`

**Current protected content SHA — 29 September 2026 owner-authorized additive publication:**  
`7d09f4cc758c4d49f14a1b9eeade0cd0d5172e0c`

This current SHA supersedes the control-date SHA above. The complete prior Ecosystem Positioning README is preserved verbatim, with one added section routing to the hypothesis protocol, audited traceability bridge and original explanatory antecedent. The three Word documents are published unchanged; the two working drafts govern the sufficiency interpretation. No existing document, section or reading route is removed.

Rule:

- Preserve this file as the complete Level-4 human landing page and evidence router for Ecosystem Positioning.
- Incremental source-supported updates to links, evidence status and claim boundaries are allowed only when they preserve the existing substantive sections and reading routes, unless Iván Abril explicitly authorizes a structural rewrite.
- A presentation-link update must never replace, truncate or regenerate the substantive README body.
- If an authorized change modifies this file, update the protected SHA in this section immediately.
- **28 September 2026 owner-authorized restoration:** restored the complete last-intact README body after the accidental 27 September truncation, preserved the corrected Stage-0/00L and A22/A23 evidence boundaries, pointed the two public PowerPoint routes to the visually reviewed v1.2 decks, removed Ward Discussion v2 and legacy combined presentation links from the canonical README route, and aligned DBC wording with its “Not a ranking” boundary. The preserved pre-truncation blob was `74acdb87e97e41f1dbdfb09c853a670b9fbca02c`.

The current Regime Awareness and MSCA READMEs are also maintained as preserved technical corpus entry points. Navigation changes should route to them rather than rewriting them unless the owner explicitly requests a content change.

---

## 4. General sitemap

```text
dakleyer/dakleyer
└── structural-awareness-contributions/
    ├── README.md                              [STRUCTURAL AWARENESS PROGRAMME]
    ├── DOCUMENT_CONTROL.md
    │
    ├── architectural-contributions/
    │   └── ecosystem-positioning/
    │       └── README.md                      [ARCHITECTURAL CONTRIBUTION]
    │
    ├── presentations/
    │   └── ecosystem-positioning/
    │       ├── Ecosystem_Positioning_Requirements_Evidence_Canonical_v1.2.pptx
    │       ├── Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx
    │       └── PRESENTATION_MANIFEST.md          [older/working artefacts preserved per manifest]
    │
    ├── research/
    │   ├── ecosystem-awareness/
    │   │   ├── README.md                      [PROTECTED ROUTER]
    │   │   ├── baseline/
    │   │   │   ├── README.md                  [CANONICAL EA CORPUS]
    │   │   │   ├── architecture / theory / benchmark / validation
    │   │   │   ├── fixtures/
    │   │   │   │   └── RS-00E-Q1a/
    │   │   │   │       └── README.md          [OPERATIVE FIXTURE INDEX]
    │   │   │   └── historical / non-canonical material
    │   │   └── fg-tida/
    │   │       ├── README.md                  [APPLICATION PACKAGE]
    │   │       ├── charter/
    │   │       ├── specifications/
    │   │       ├── interfaces/
    │   │       ├── cases/
    │   │       ├── tests/
    │   │       └── provenance/
    │   │
    │   └── regime-awareness/
    │       └── README.md                      [CORPUS ROUTER]
    │
    ├── standards/
    │   └── minimum-sufficient-control/
    │       └── README.md                      [CORPUS ROUTER]
    │
    ├── applied-research/
    │   └── cost-of-clarity-rup/
    │       └── README.md                      [TRANSITIONAL; target PROJECT.md]
    │
    └── submissions/
        ├── README.md                          [SUBMISSIONS ROUTER]
        └── institution/package records
```

This sitemap describes navigation ownership, not every file in the repository.

**29 September 2026 supporting-document route:** `architectural-contributions/ecosystem-positioning/documents/2026-09-29/` contains the three preserved Word documents, owned and linked by the existing Ecosystem Positioning README. This adds no README or independent router; the raw README count and controlled-navigation target are unchanged.

---

## 4A. Human-readable public information architecture

**Primary rule:** public README files are written for human readers first.

Every routed public README must answer, in ordinary language and before presenting navigation:

1. **Where am I?**
2. **What is this?**
3. **Why does it exist / what problem does it solve?**
4. **How does it relate to the surrounding programme without duplicating it?**
5. **Where should I go next for the question I actually have?**

A README must not be reduced to a sitemap, path table, index-of-indexes or bot-oriented routing contract if doing so removes the explanatory content that makes the work intelligible.

Maintenance metadata, canonical path rules, controlled README counts and migration procedures belong in this `DOCUMENT_CONTROL.md`, not in place of the substantive human explanation.

When simplifying a README, an editor must preserve its intellectual narrative, definitions, distinctions, relationships and evidence boundaries. Navigation should support the explanation rather than replace it.

### Structural Awareness Level-2 content rule

The repository root README is not merely a router. It is the human explanation of the programme and must continue to present **four stable parts**:

1. **Mathematical Contributions** — ResearchGate/publication route.
2. **Field Notes / Research Series** — explanatory research such as Cost of Clarity, Human Intelligence Debt, Attribution Gap, Informational Friction and related series.
3. **Field Practice / Engineering** — Phylons, xSeil and Mobility Operating System / Car Evolution.
4. **Architectural Contributions / pre-standardization** — the architecture contribution layer. The current maintained contribution is **Ecosystem Positioning**, with the canonical presentation and maintained gates to Ecosystem Awareness, Regime Awareness and MSCA.

An editor must not replace those four explanatory parts with a generic sitemap, a table of folders or a list of README files.

**Consistency rule:** if two public READMEs describe the same concept, they must not silently assign it different meanings. One page may be more detailed than another, but the conceptual relationship must remain compatible with the owning corpus.

---

## 5. Modification rules

### Rule 1 — preserve the cascade

Every public content item must be reachable through a human-readable programme path.

For the current architectural contribution the canonical cascade is:

`dakleyer/dakleyer → Structural Awareness Programme → Architectural Contributions / pre-standardization → Ecosystem Positioning → technical gate / evidence`

Cross-links may provide shortcuts, but they do not replace this canonical route.

### Rule 2 — root links explain; they do not duplicate corpora

The Level-2 repository README may link directly to the defining sources for its four human programme parts and to the canonical Ecosystem Positioning presentation. It must not duplicate the internal document indexes owned by EA, Regime Awareness, MSCA or other routed corpora.

### Rule 3 — one navigation owner per content family

Each document family has one primary router. Other corpora may link to the family as a cross-reference, but should not reproduce its internal index.

### Rule 4 — cross-corpus references do not create ownership

EA, Regime Awareness, MSCA, applied research and submissions retain separate semantic and evidential ownership. An interface link does not merge corpora or transfer validation.

### Rule 5 — canonical versus unique non-canonical content

Non-canonical does **not** mean disposable.

- Canonical current material remains in the routed reading tree.
- Unique historical, evidential, procedural or non-canonical material must remain preserved and reachable, but may live outside the canonical reading tree in a clearly named manifest/archive/provenance document.
- Redundant navigation text may be absorbed into its parent and removed only after verification.

### Rule 6 — README is reserved for real navigation nodes

New `README.md` files should be created only when a directory genuinely needs to act as a stable routed entry.

The Ecosystem Positioning README is a legitimate controlled node because it is the human landing page for an Architectural Contribution and routes to the canonical presentation and three technical gates.

Prefer purpose-specific names for non-router artefacts:

- `PROJECT.md`
- `PACKAGE_MANIFEST.md`
- `SUBMISSION_MANIFEST.md`
- `CONTRIBUTIONS_INDEX.md`
- `NON_CANONICAL_MANIFEST.md`
- `STATUS.md`
- `PROVENANCE.md`

### Rule 7 — renames and moves are transactional

For every rename or move:

1. create the destination first;
2. preserve the full substantive content;
3. search globally for every inbound reference to the old path;
4. update all inbound references;
5. verify the new path;
6. verify zero remaining live references to the old path;
7. only then remove the old file;
8. update this Document Control file if the sitemap, controlled README count or routing rule changed.

Do not perform destructive cleanup first.

### Rule 8 — preserve claim boundaries

A move, rename or consolidation must not silently remove:
- version/status statements;
- adoption/endorsement disclaimers;
- source identity;
- provenance;
- hashes or receipt status;
- canonical/non-canonical distinctions;
- external-owner boundaries.

### Rule 9 — preserve exact file identity where required

Frozen, submitted, pre-registered, hashed or externally cited artefacts should not be rewritten merely to improve style. Prefer wrapper/index updates around preserved evidence.

### Rule 10 — editor/bot changes must be auditable

Navigation-changing commits should say what was changed and why. Avoid opaque messages such as “cleanup”.

---

## 6. Required editor / bot checklist

Before changing navigation or document placement:

- [ ] Read this `DOCUMENT_CONTROL.md`.
- [ ] Identify the primary owning router.
- [ ] Check whether the target file is canonical, frozen, submitted, unique non-canonical or purely redundant.
- [ ] Check whether either protected README (Ecosystem Awareness or Ecosystem Positioning) would be affected.
- [ ] Search for inbound links to any path being moved, renamed or removed.
- [ ] Preserve claim/status/provenance text.

After the change:

- [ ] Verify Level 1 → Level 2 → Level 3 reachability; for Architectural Contributions, also verify the Ecosystem Positioning landing page and technical gates.
- [ ] Verify the Level-2 root still explains the four programme parts rather than duplicating corpus-internal indexes.
- [ ] Verify all changed relative links resolve.
- [ ] Search for the old path and confirm no unintended live references remain.
- [ ] Confirm no unique text was lost.
- [ ] Recount README files if any README was created/removed/renamed.
- [ ] Confirm the protected EA and Ecosystem Positioning README SHAs are unchanged unless owner authorization explicitly allowed a change.
- [ ] Update the sitemap and controlled README count in this file if necessary.
- [ ] Update any affected parent router.
- [ ] If a canonical presentation changed, verify PPTX/PDF parity and all required hyperlinks.
- [ ] State explicitly in the commit message that document control and navigation were verified.

---

## 7. Current consolidation rule

The current approved consolidation objective is to maintain **9 controlled README files without losing content**, from an initial consolidation baseline of 22 README files; the current raw count is recorded in §2.

The reduction must follow the case-by-case audit already established:

- keep genuine corpus/router READMEs;
- keep the Ecosystem Positioning architectural contribution README as a legitimate human landing page;
- absorb small local router text into its parent;
- rename unique non-router documents to purpose-specific names;
- preserve unique non-canonical material outside the canonical reading tree;
- migrate inbound links before deletion.

Until each migration is completed, the transitional README remains valid and must not be removed.

---

## 8. Naming and presentation consistency

Use stable public names in reader-facing text. Where an older filename must remain for provenance or because a protected router still links it, distinguish:

- **public/current display name**, and
- **legacy/preserved filename or identifier**.

Do not rename frozen evidence solely to improve presentation if that would weaken traceability.

---

## 8A. Canonical presentations

Canonical presentations are first-class controlled artefacts.

For Ecosystem Positioning, the **two public PowerPoint entry routes** are:

- `presentations/ecosystem-positioning/Ecosystem_Positioning_Requirements_Evidence_Canonical_v1.2.pptx` — requirements, evidence and validation entry.
- `presentations/ecosystem-positioning/Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx` — architecture and implementation entry.
- `presentations/ecosystem-positioning/PRESENTATION_MANIFEST.md` — status, provenance and routing contract.

The combined editable presentation, historical PDF snapshots and Ward Discussion decks remain preserved artefacts governed by the manifest, but they are **not additional canonical PowerPoint entries in the Ecosystem Positioning README**.

Rules:

1. GitHub is the canonical public version-control location for the presentation artefacts.
2. The Ecosystem Positioning README exposes exactly the two current split PowerPoint entry routes above; working, historical or owner-only presentation artefacts remain reachable through the manifest when needed.
3. A visual-only presentation revision must not silently alter architecture, requirements or evidence claims; the manifest records whether a revision is visual or substantive.
4. The public decks must link upward to the Structural Awareness Programme README.
5. Their maintained technical gates must link to the GitHub READMEs for Ecosystem Awareness, Regime Awareness and MSCA.
6. A presentation may link directly to benchmark or standards-facing references where they are part of the architecture, but it must not create a competing parent router.
7. Historical and milestone presentation states remain preserved for provenance without being promoted into additional primary README links.
8. The Structural Awareness README and `architectural-contributions/ecosystem-positioning/README.md` must expose clear direct routes to the current public presentation entry points.
9. Presentation navigation changes must preserve the substantive Ecosystem Positioning README; link maintenance is never grounds for regenerating or truncating the router.

---

## 9. Maintenance trigger

This file **must be reviewed and, where necessary, updated** whenever any of the following occurs:

- a README is created, deleted, renamed or demoted;
- a Level-1, Level-2, Level-3 or architectural contribution route changes;
- a corpus is split or merged;
- a canonical document changes path;
- a canonical presentation changes path or routing contract;
- a new public submission package is introduced;
- a protected-file rule changes;
- a new navigation convention is adopted;
- the controlled README count changes.

If none of those occur, routine edits inside an already routed document do not require a Document Control revision.

---

## 10. Control principle

The repository should remain understandable to a new human editor or automated agent without reconstructing historical conversations.

The control objective is:

> **one canonical entry, four understandable programme routes, explicit architectural contribution ownership, preserved evidence, and no destructive navigation cleanup without traceable migration.**

## 11. 30 September 2026 owner-authorized 04 input-contract publication

The existing EA baseline index owns the new supporting route `research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/`. The current 04 document links directly to the complete input-contract v0.4 reader, its unchanged Word copy and classification assets; the existing 04 vNext Delta records the open integration work. The package is a working starting point within 04, not a replacement of the integrated baseline or a new programme-level router.

No README is created, removed or renamed. No existing section or reading route is removed. The protected EA and Ecosystem Positioning READMEs, root programme narrative, historical 04 split sources and canonical presentations remain unchanged. Document control and navigation are verified by the repository integrity check, additive-change checks and package content/hash checks. H06 remains an explicit integration task.
