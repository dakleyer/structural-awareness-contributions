# Document Control — navigation, sitemap and modification rules

> **2 October 2026 — owner-authorized A/B/C/D semantic alignment.** Iván requested minimal corpus-wide definition corrections and links to 00M. No navigation owner, document path, README count, requirement identifier or evidence result is changed. Current protected blobs for this alignment supersede the earlier SHA records: EA router `4e41fc697bb2bd94d1f4dd2b75230937684b8152`; EP router `77d798d21ff8c08585b677258e86337f04bca008`. The [before/after plan and preservation checks](./governance/ABCD_CANONICAL_ALIGNMENT_2026-10-02.md) delimit the changes. Historical exports remain identified as such.

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

## 12. 6 October 2026 — owner-authorized corpus review procedure

**Control addition version:** 2026-10-06.1. Iván requested a preservation-first review method and corrected its name to **VNext**. The [review procedure](./governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) governs the audit conversation, one VNext per logical document, literal before/after proposals and Iván's recorded instructions. The existing [Ecosystem Positioning README](./architectural-contributions/ecosystem-positioning/README.md) receives only a prefixed review note linking that procedure and its sole [README VNext](./architectural-contributions/ecosystem-positioning/README_VNext.md); its previous body is preserved byte-for-byte.

**Current protected EP README blob for this addition:** `9c31f225b5364d0d681df455d6e5d809786470e3`; this dated entry supersedes earlier EP blob records for the current file. **Predecessor EP blob:** `551eb4d55eb0e4efdfe3d81f506da81a1e93e8ab`. Exact predecessors at base commit `b8f935f2a1fbac17f8aac24be60a3e65cd2c2b98` are retained as [EP README snapshot](./governance/preserved-public-snapshots/2026-10-06_EP_README_before_review_setup.md) and [Document Control snapshot](./governance/preserved-public-snapshots/2026-10-06_DOCUMENT_CONTROL_before_review_setup.md). Their historical links retain their original meaning and locations.

Navigation addition: EP README → review procedure + EP README VNext. No existing reading route, programme hierarchy or presentation changes. No README created, removed or renamed; the README count delta is zero. Existing Requirements/04/05/05A vNext deltas remain intact and must be reused, not duplicated. Frozen, signed, submitted, hashed and binary sources receive external review cards rather than internal notes.

This entry records the setup scope; it does not certify a complete corpus audit, substantive proposal approval or technical validation. Verification for this commit checks exact predecessor blobs, additive preservation, changed-path scope, VNext uniqueness and resolution of every added document link. Publication completion requires the branch update and content readback; the AgentSync records that outcome separately.


## 13. 6 October 2026 — separate development strategy; append-only EP README

**Control addition version:** 2026-10-06.2. Iván requested a separate, human-readable development strategy linked from the Ecosystem Positioning README. The [Development Strategy](./architectural-contributions/ecosystem-positioning/DEVELOPMENT_STRATEGY.md) presents proposed priorities, areas for specialist contribution and external research support. It complements the review procedure and technical WORKPLAN; it is not a new canonical specification, operational result or replacement task queue.

**Owner preservation instruction:** until Iván reviews and explicitly authorizes a concrete change, the existing Ecosystem Positioning README and this additional strategy are append-only. Do not delete, replace, reorder, truncate, normalize or reformat prior content. General permission to continue audits or publish additions does not override this restriction. Detailed proposals remain in the appropriate VNext or review record. This dated restriction supersedes any broader reading of earlier incremental-maintenance permissions for these two files.

Only a short strategy-link section is appended at the end of the README. Its prior text is an exact byte prefix. No bot procedure, audit ledger or internal code list is inserted into the public reading section. No README is created or removed, and existing navigation ownership is unchanged.

**Current protected EP README blob for this addition:** `ed97dbe9f34758219863511717c4f237b48bedf3`, superseding the earlier EP blob records for the current file. **Predecessor blob:** `9c31f225b5364d0d681df455d6e5d809786470e3`. Exact predecessors are preserved as [EP README before the strategy link](./governance/preserved-public-snapshots/2026-10-06_EP_README_before_development_strategy.md) and [Document Control before the strategy entry](./governance/preserved-public-snapshots/2026-10-06_DOCUMENT_CONTROL_before_development_strategy.md).


## 14. 6 October 2026 — three corpus reading levels; structural proposals in README VNext

**Control addition version:** 2026-10-06.3. Iván clarified the maintained reading model for the Ecosystem Positioning corpus: **Ecosystem Positioning entry → Awareness entry → technical corpus indexes**, with three reading levels only. Earlier Level-4/global numbering remains historical context and must not be used to expand this corpus's README hierarchy. Existing package/fixture/history READMEs do not automatically constitute extra public navigation levels. No file-count target authorizes deleting or absorbing their unique content.

Any proposed redistribution, move, split/merge, hierarchy change or change of inter-file reading/dependency/ownership relationships belongs in the **owning README's sole VNext**, with corresponding entries in every affected README VNext. The EP [README VNext](./architectural-contributions/ecosystem-positioning/README_VNext.md) holds a joint account when corpus-level organization is affected. A document's own VNext may identify the issue but does not independently authorize changing the file structure. This applies before execution, with source preservation, concrete before/after scope and Iván's decision.

The [work-plan addition](./governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#redistribución-de-archivos-y-tres-niveles-de-readme--instrucción-de-iván) makes this instruction operative. The earlier EP Level-4 proposal is not adopted under the new corpus-level rule; its history is preserved. The public EP README and development strategy retain their append-only guard. This entry modifies review guidance only: no redistribution, rename, deletion, hierarchy implementation, new README navigation node or canonical technical change is executed.


---

## 15. 6 October 2026 — three non-canonical additional-work catalogues

**Control addition version:** 2026-10-06.4. Iván explicitly requested that material outside the canonical reading route be explained and linked as additional work, without modifying the loose documents or starting a new audit of each. The canonical three-level reading model remains: EP → Awareness → technical indexes. The owner's “fourth-level README” wording designates an **optional non-canonical leaf**, not a fourth canonical navigation level.

Exactly three catalogues are used: [EA and cross-cutting work](research/ecosystem-awareness/baseline/non-canonical/README.md) expands the existing non-canonical index; [RA](research/regime-awareness/ADDITIONAL_WORK_README.md) and [MSCA](standards/minimum-sufficient-control/ADDITIONAL_WORK_README.md) are two new auxiliary reading documents. The technical indexes [EA baseline](./research/ecosystem-awareness/baseline/README.md), [EWS](./research/regime-awareness/minimalistic-early-warning-systems/README.md) and [MSCA](./standards/minimum-sufficient-control/README.md) receive only an appended optional-reading link. No canonical owner, route, source or presentation is moved, renamed, demoted or replaced; no old text is removed.

This is an owner-authorized exception for three auxiliary reading sheets only. It does not authorize further README hierarchy proliferation or reduce the protected-README rules. EP README, EA entry-point README and development strategy remain unchanged. Frozen sources, evidence, data, code and binaries are untouched. All originals retain their own authority; catalogue membership does not promote or demote them.

The catalogues identify purpose, current reading relationship, exact duplicates where checked, versions, pointers and fragment presentation. Counts describe the fixed source tree, not completed audits. Canonical sources or material evidence are not excluded because a split part was individually unlinked. Additional documents receive explanation and links rather than a new five-pass audit/VNext by default, per the [latest plan addition](governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#trabajo-fuera-de-la-ruta-principal--lectura-adicional-sin-nuevas-auditorías).

Navigation execution and literal index-link additions are recorded in the existing affected README VNext and EP README VNext. Authentic predecessor blobs are preserved before branch publication; the diff and new links are verified and public text read back.


---

## 16. 6 October 2026 — separate review records for MSCA Role and Composition

**Control addition version:** 2026-10-06.5. Existing canonical Role/Composition sources retain their exact blobs. Their unique VNext are [Role](standards/minimum-sufficient-control/02_ROLE_VNext.md) and [Composition](standards/minimum-sufficient-control/03_COMPOSITION_VNext.md), with external review cards to preserve the originals. The MSCA owner README receives only an appended link to those review notes. No source move, rename, deletion, new README or canonical level is introduced.

The current 01C review records partial producer–consumer findings in both endpoints and the owning README VNext. Candidate 52/53 clarifies qualification of a shared cartographic slice; 54 distinguishes role binding and observed behaviour. Publication of these candidates does not authorize incorporation. Additional-work catalogues, frozen sources, results, code and binaries are preserved.


---

## 17. 6 October 2026 — review records for MSCA kernel, ACC and Gradient

**Control addition version:** 2026-10-06.6. The owner-authorized review now has unique external cards and VNext for [Architecture](standards/minimum-sufficient-control/00_ARCHITECTURE_REVIEW_CARD.md), [ACC lineage](standards/minimum-sufficient-control/01_ACC_REVIEW_CARD.md), [Gradient](architectural-contributions/ecosystem-positioning/01_GRADIENT_REVIEW_CARD.md) and [ACC participation01I](research/ecosystem-awareness/baseline/01I_REVIEW_CARD.md). These are current principal sources/material integrations, not loose-document audit proliferation. Sources retain their exact blobs; no substantive canonical proposal is applied.

The MSCA owner README and EA baseline owner README receive only appended review-card links. Their VNext preserve literal old context and the full navigation additions. EP README VNext relates the new comparison finding and source/consumer proposals. EP canonical README, EA entry-point README, development strategy, canonical specifications, frozen evidence, results, code and binaries remain unchanged. No README created, removed, renamed or reordered; canonical reading levels remain the three already recorded in§14. Existing auxiliary catalogues remain unchanged.

Authenticated predecessor blobs are preserved before adding to existing records. Required verification covers byte-prefix preservation, exact changed scope, new link/anchor resolution and VNext uniqueness. Publication requires head/scope checks and exact public readback. A reference to external research or an inaccessible ITU document does not establish adoption, a performed experiment or authority.

The same publication also records the newly incoming [Human Intelligence 01K review](research/ecosystem-awareness/baseline/01K_REVIEW_CARD.md) and a [partial01J Signalling review](research/ecosystem-awareness/baseline/01J_REVIEW_CARD.md). The canonical source update at `8757ba614c94f962206912d4896c119a18a924fa` is preserved in full. Observed EP source blob is `117324cfaf8cb6978f33f2923f9151479ec1c918`; this observation does not approve an exception to the append-only instruction. The prior source was not a byte-prefix of the concurrent mid-body insertion, and EP README VNext records the pending provenance/authorization check. This review itself does not edit or revert the EP canonical source.


## 26. 12 October 2026 — owner-approved outstanding textual proposals and working successors

Iván explicitly accepts and authorizes applying the outstanding concrete VNext changes. Ecosystem Positioning README receives only the approved final reading clarification; all prior bytes are its exact prefix. **Current protected EP README blob: `9767ec8efb7d3a2875866ea3cd22ebc94882e930`.** This entry supersedes earlier EP blob records. Its predecessor is retained in commit `9fb9421711521decde6843b04914a143a1f04c35`. The protected EA entry README and Development Strategy remain unchanged.

The existing baseline README adds direct links to [Requirements working successor](./research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md) and [UC-EA-03 v0.5 working successor](./research/ecosystem-awareness/baseline/UC-EA-03_v0.5_WORKING_SUCCESSOR.md). Their frozen predecessors remain unchanged and retain their study-contract authority; the approved changes have working successor editions. Existing Requirements and UC-EA-03 VNext own both versions. DDS's existing VNext owns the [checker v0.4 audit candidate](./research/ecosystem-awareness/gate-diagnostic/check_gate_profile_v0.4_audit_candidate.py) and [typed-substitution regression controls](./research/ecosystem-awareness/gate-diagnostic/test_na_substitute_v04.py); v0.2/v0.3 and historical results remain unchanged.

No file is moved, renamed or deleted. No README or VNext is created, and navigation ownership and the three corpus reading levels remain unchanged. The new source/control files implement specific accepted proposals; they are not additional indexes. RA/EA/MSCA, gradient, signals and foundational clarifications are applied as their exact approved passages, with predecessor custody, preserved fragment anchors, scope comparison and readback. Existing audit discussions remain visible; incorporated fiches leave the pending queue. No campaign or external message is launched.


## 27. 12 October 2026 — completed conservative UC-21 / DDS reader migration

Iván authorizes completion with preserved information, original routes and secondary links at the end of the existing indexes. Six approved candidates77–82 update13literal passages in four reader files; every earlier HTTP destination remains available. The existing UC-21 README and EA additional-work leaf receive only optional supporting links at their end. No source file is moved or renamed and no original reading section is removed.

The S5 review packet README and ZIP, present at `2c7f545e2610e154b2e7d11fe827722bbf3c5658` but absent from the pre-application main tree, are restored to their original paths with Git blobs `97ed3f73c478881572bf8a9d5465cc38b0922e87` and `65c202ec81d50bd2681ab4e3ee8ac814a72c4779`. Their original bytes, dates and scope remain intact. The existing EA [additional-work leaf](./research/ecosystem-awareness/baseline/non-canonical/README.md) explains them as historical research-side review material and links the complete packet. This is restoration of an earlier leaf, not a new canonical navigation owner. Raw README count: 100 before, 101 after restoration; controlled owner count and the three corpus reading levels are unchanged.

The protected EP/EA entry READMEs and Development Strategy retain their blobs. Research code, study inputs, freezes, results and binaries remain unchanged; the restored ZIP matches its original SHA256. Existing VNext record applications and remove incorporated fiches. Verification checks original file sets, exact inverses of approved passages, all earlier destinations, supplemented reachability and public readback. The external FG-TIDA entry is separately gated after automatic approval rejection; its body and metadata are unchanged by this migration.

## 28. 13 October 2026 — owner-authorized FLORES DDS development dossier

Iván authorizes an **additive** [campaigns-in-development reader register](./research/ecosystem-awareness/campaigns-in-development/INDEX.md) and machine JSON register (both subordinate to the DDS Canonical Method Index, not independent method authority), plus a full research-side working campaign dossier under [Flores / population → EA](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/CAMPAIGN.md), routed once by the existing DDS Canonical Method Index. The folder contains substantive scientific design, historical criticism and preservation extracts, sources, status and continuation instructions, rather than merely an annex. **Status is NOT_PREREGISTERED / NOT_EXECUTED / NOT_ADJUDICATED**; it does not assert that Flores or other FG-TIDA contributors agreed to or executed a joint campaign.

This record implements **no root dds/ migration, file move, rename, deletion, new README navigation owner, canonical method replacement, science regrading, blind-key publication or change to any original external source**. Protected EA/EP root routers, original baseline files, 00M/00N, source execution, freezes and previous evidence remain in place. The added history files are **source-custody summaries** of earlier reviewed Library sources, NOT complete text renderings and NOT byte-exact PDF/ZIP preservation; full Library export/retrieval was unavailable at publication. The future global campaign consolidation plan still requires its own authorized manifest and parity checks. This index entry and status are additive under the existing Document Control modification rules.


## 29. 13 October 2026 — consolidate detailed Flores supplements into the one registered campaign

A concurrent branch attempted a second owner under FG-TIDA/tests (PR #19); the duplicate PR was **closed unmerged** after the canonical [campaigns-in-development/flores-population-ea](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/CAMPAIGN.md) owner was discovered. Its scientific detail was preserved and incorporated as a [technical subprofile](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/technical/TECHNICAL_INDEX.md) beneath that one existing owner, not by copying a second campaign or altering DDS's method ownership.

The existing campaign master, design, custody, audit, continuation and the campaign directory index gain only **additive cross-links and later factual custody/correction notes**; their previous substantive text and original source files are preserved. The existing CAMPAIGN.json/REGISTRY.json add subcomponent references without creating another campaign entry. No protected canonical EA/EP README, 00M/00N, 04/05/05A, Theme #21, source experiment or frozen test is modified; no new README.md. Both P0–P3 and Q0→Q1 remain candidate alternatives with strong B2 comparison, no original experimental run, no Stage A pass and no implied external consent. Raw historical auditor-only archives remain privately retained, not disclosed as candidate cases.


## 30. 13 October 2026 — CI navigation-only repair for pre-existing 00K-SUITE VNext links

The PR #20 Documentation Integrity check initially failed on two **pre-existing malformed relative links** in `research/ecosystem-awareness/baseline/fixtures/00K-SUITE/README_VNext.md`: its active current-runner and execution-router links included an extra `fixtures/00K-SUITE/` directory, resolving to nonexistent nested paths. The fix changes only those **two Markdown href targets** to `./run_all.py` and `./README.md`; the original paragraph's text, versioned 128/134/379 scientific descriptions, historic fenced quotation, test code, results and frozen records are preserved. This is a separately identified CI reader-link repair, not new Flores evidence, not a changed 00K campaign count, and not a new method/index owner. Original blob in main immediately before repair: `71e380cd76b4ce064af43bb7b11c9448caef1cf4`.

## 30. 13 October 2026 — Flores second audit technical-source reconciliation

The requested full Flores campaign reassessment is documented in [AUDIT_REPORT_2026-10-13](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/AUDIT_REPORT_2026-10-13.md), its [technical integration audit](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/TECHNICAL_INTEGRATION_AUDIT_2026-10-13.md) and the [scientific approach pivot record](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/APPROACH_DRIFT_2026-10-12_13.md). They preserve both the owner-prioritized UC17-08 single-point trial and the separately authored corrected receiving P0→P3 technical candidate **inside one DDS Stage A campaign in development**. The 21 local authored mock consistency checks are not blind native Flores results, and one purported two-world check is tautological and pending meaningful independent contrast. The technical history's obsolete reproduction paths now have an explicit erratum naming the working current paths.

An earlier documentary lack of full source text was addressed by six [complete readable-text Library recoveries](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/history/recovered-text/RECOVERY_MANIFEST.json). A concurrent source authoring runtime reported private ZIP SHA-256 rechecks [in the technical historical ledger](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/technical/HISTORY_AND_REPRODUCTION.md); this auditor did not rerun those binary checks, and the original private ZIPs and reviewer-only oracles are not publicly mirrored. No original Flores/CTGT/UC4 record is moved, no frozen source regraded, no new README owner or physical global dds/ migration implemented. **Status remains documentation/research preparation only; no approved Run Card, B2/EA execution, Stage A acceptance or Stage B/C.**


## 31. 13 October 2026 — durable Flores R2/freeze/R3 owner correction

Iván requests that the prepared Flores research and repeated governing principle live in the actual existing GitHub campaign, rather than remain only in local working bundles. The existing campaign master, continuation, design and register now make the later [R2/freeze/R3 instruction](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/runtime-context/PRINCIPIO_R2_FREEZE_R3_2026-10-13.md) read-first, with all earlier Markdown text preserved. Its [temporal protocol](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/runtime-context/PROTOCOLO_2026-10-13.md), report, formalization, sources, review, public synthetic preflight and reader HTML are one subordinate research component, not another campaign or README navigation owner. Previous JSON primary-trial and pivot values remain in historical fields. Parity in repaired R2 is the expected baseline; full R2 is frozen before an admissible uncovered R3, with general EA requirements fixed ex ante. Prior UC17-08/P0-P3 priorities survive as history/separate controls. This changes documentary research direction, not native producer sources or historical freezes/results, protected routers, DDS stage claims or external contributor acceptance. No move, rename or deletion, no native run and no scientific acceptance are asserted.


## 32. 2026-10-13 — owner-authorized complete Flores organization and version annex

Iván requests a fully organized and traceable campaign in the actual GitHub workspace, with no information deleted or economized. The one existing [Flores campaign](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/CAMPAIGN.md) gains compact current reading surfaces, an exhaustive [version/decision annex](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/VERSIONS_AND_DECISIONS_2026-10-13.md) and [audit trace](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/TRACEABILITY_2026-10-13.md). Each rewritten or annotated prior file is preserved with the identical Git blob and SHA-256 before application in history/versions; the earlier source paths remain. The [control record](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/audit/CAMPAIGN_CONTROL_2026-10-13.json) records scope, every artifact, predecessor, claim/source relation, open issue and immutable source cut. Existing DDS VNext records the concrete owner-authorized change; no extra README or navigation owner is created. Code, data, external sources, private oracles and frozen evidence remain unchanged. Current direction is Theme #21 same temporal claim R2 repaired parity → complete freeze → uncovered material R3, with EA general ex ante. This is documentary organization and author-side structural audit, not scientific adjudication or completion of native execution. Prior unique content, links, judgments and negative findings remain accessible in full, not reconstructed from summaries.


## 33. 14 October 2026 — owner-requested expanded Flores corrective audit

The existing campaign gains an [expanded corrective audit](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/audit/EXPANDED_AUDIT_2026-10-14.md), a pinned predecessor baseline, stricter verifier, adversarial probes and an authored proof-checker successor. The owner asks to expand and resolve audits while preserving complete information. Every replaced record and previous verifier is retained as the identical blob in history/versions; original scientific source, fixture/code/calibration data and mock checker stay unchanged. The existing campaign/README ownership and source freezes do not change. Stage A/B/C promotion, native execution and independent acceptance remain prohibited without their own evidence. The dated source freshness cut and prospective blind/readiness contract close preparation issues without fabricating missing external results or private binaries.


## 34. 15 October 2026 — approved UC-21/DDS literal application and protected EP successor

Iván authorised the reviewed literal plan on 15 October. The [application record](./research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#owner-authorised-application-complete-15-october-2026) identifies 32 local passage replacements in 14 existing documents, the one approved paragraph in the official UC-21 Issue, and the separately approved custody of 48 exact original source-edition files. Their source and step commits are recorded in the existing VNext; no prior file was deleted, moved or renamed and no VNext was created.

**Current protected EP README blob: `9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b`.** Proposal 97 appended only its approved S10 working-successor reading note in commit `413208033cd6b92c9982adc3cfff0fa5161a3995`; every predecessor byte remains the exact prefix. This dated successor supersedes the current-EP certification in section 26, whose `9767ec8efb7d3a2875866ea3cd22ebc94882e930` blob remains the correct 12 October historical edition. The protected EA entry README and Development Strategy remain unchanged by this application.

The maintained reader route is UC-21 → objectives → Challenges → DDS → campaigns and results. The source-edition package is historical custody, not a second current method or case owner. Programs, earlier binaries, results and frozen manifests remain unchanged. The [execution re-audit](./research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#execution-reaudit-15-october-2026) distinguishes completion of this literal application from the still-open historical/material reception work and future per-campaign evidence duties.

## 35. 24 October 2026 — document classes, VNext links and staged control

**Control addition:** [Corpus Document Control Conventions v0.1](./governance/CORPUS_DOCUMENT_CONTROL_CONVENTIONS_v0.1.md), instructed by Iván Abril Palma. It complements this navigation/preservation control with logical identity, editions, status, document roles, source ownership and a progressive migration method. It is a repository-level technical convention, not an assertion of new institutional, external programme or scientific approval.

**Clarified direct-link rule:** a **canonical** document may link to other canonical, optional/contextual, evidential and historical material, but **among VNext documents it may link only to its own single companion VNext** (where a source can be updated under preservation rules). **VNext↔VNext and optional/contextual→VNext links are permitted** and useful for cross-document development. Links do not promote proposals or transfer semantic authority. Frozen sources retain their historical bytes and, where needed, use an authorized external review card/index.

**Initial wave:** only this control addition and the linked convention are published. The reported ~120 VNext references have not been batch-edited or certified; subsequent bounded waves begin with classification by source/target role and historical status. Existing controlled READMEs, canonical scientific claims, historic snapshots, submissions, test evidence, paths and README counts remain unchanged.
