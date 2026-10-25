# DC-GH-01 v1.0 — Document-control conformance audit

**Date:** 25 October 2026 · **Reviewer:** Codex (AI-assisted repository inspection; not independent external certification)  
**Owner of decisions:** Iván Abril Palma · **Policy under test:** [Corpus Document Control — DC-GH-01 v1.0](../DOCUMENT_CONTROL.md)  
**Evidence baseline:** public main commit [21e200cd4c9a0558e4ae3669c55f7256c03a005a](https://github.com/dakleyer/structural-awareness-contributions/commit/21e200cd4c9a0558e4ae3669c55f7256c03a005a), immediately before publication of this consolidated policy and audit. The publication changes documentary controls only; it does not remediate the scientific corpus or VNext graph.  
**Detailed link inventory:** [2026-10-25 JSON baseline](./review/DOCUMENT_CONTROL_VNEXT_LINK_INVENTORY_2026-10-25.json).

## Verdict and assurance boundary

**Partial conformity; NOT corpus-certified.** GitHub already provides commits, exact versions and PR/issue traceability, and the repository contains useful navigation/review/freeze controls. However the required logical-role register, VNext-policy checker and enforceable merge protections are absent; one registered protected router SHA is stale; and confirmed current-router references to foreign VNext-like reviews require classification and correction.

This audit assesses **document-control implementation**, not scientific truth, independent review, IMSV statutory Receptio, freeze parity with Google Drive, external programme adoption, or the quality of the underlying studies.

## Method and population

The public Git tree was enumerated at the pinned baseline. All **1,045 Markdown files** were fetched and searched for inline rendered Markdown links whose destination includes VNext/VNEXT (case-insensitive). Fenced code and basic inline code were excluded from the link count. For working-path analysis, **787 Markdown files** were retained after excluding paths containing old, history, historical, previous-work, archived, or preserved-public-snapshots; the other **258** are reported separately. This is a **path-based subset**, not yet an approved semantic role classification.

The current GitHub tree, nine workflows, documentation-integrity script, contributing rules, corpus review procedure, protected-router histories, EA Canonical Corpus Manifest and the R01 duplicate pairs were inspected. GitHub's native branch record was read for effective protection state.

The link parser counts inline Markdown link occurrences; it does **not** yet include reference-style Markdown, HTML links, bare references, external-link target validation or exhaustive identification of canonicality. It therefore does not certify complete graph conformance. Distinct raw counts from other audits (approximately 120, 180 or 2,525) should not be equated to violations until their denominators and methods are reconciled.

## VNext graph baseline

| Metric | Measured |
| --- | ---: |
| Total Markdown files on main | 1,045 |
| Working-path subset (defined above) | 787 |
| Historical/legacy-path subset | 258 |
| VNext/VNEXT inline Markdown link occurrences, all paths | **2,747** |
| VNext link occurrences, working-path subset | **1,565** |
| VNext link occurrences, legacy subset | 1,182 |
| Working-path source files with at least one VNext reference | 176 |
| Of those, source filenames not containing VNext/VNEXT | 107 |
| Working-path local VNext link occurrences | 950 |
| Working-path external/non-local VNext link occurrences | 615 |
| Distinct local source→target pairs, working subset | 621 |
| Missing local VNext target paths among these 950 occurrences | **0** |
| Files named exactly README.md in the tree | **103** |

**Interpretation:** the large number of VNext references is not an error count. VNext→VNext and contextual→VNext links are expressly allowed. A filename without VNext does not prove a source is canonical; an external pinned historical link may be legitimate. Further role classification and human reading are required.

## Control-by-control findings

| Policy section | State | Evidence / gap |
| --- | --- | --- |
| §1 — One active documentary authority | **Established by this publication; historical coexistence requires reader routing** | Consolidated root policy takes precedence; v0.1 is superseded by a short historical pointer, and its complete original text is preserved as an excluded archive snapshot; substantive review and freeze controls retain their own scoped mandates. |
| §2 — Git technical history | **Available** | Commit timestamps, blobs, changes and GitHub PR/issue history exist. Avoid a second technical changelog. |
| §3 — Identity, roles, maturity | **Partly documented** | Canonical versus validated is distinguished in text, but roles remain inconsistent or unclassified across individual files. |
| §4 — Logical ID register | **Not implemented** | No global governance/DOCUMENT_REGISTRY.yml was present in the audited baseline. The EA CANONICAL_CORPUS_MANIFEST is domain-specific and must not be repurposed silently as this global register. |
| §5 — Canonical/VNext links | **Documented, not enforced; concrete candidates** | See affected routers below. No machine-verifiable global mapping of each current canonical to its own VNext exists. |
| §6 — Navigation ownership | **Partial** | The nine previously named controlled router paths exist, but historical manual README counts (49 and 101) differ from the measured 103. Public-level versus technical-reading-level scopes need distinct explanations. |
| §7 — Review and promotion | **Mechanisms exist, enforcement absent** | Repository uses PR/issue history; a merged technical change is not scientific adoption. Main was reported as unprotected. |
| §8 — Protected-source integrity | **Unresolved discrepancy** | EA entry README has a different current blob than the last recorded protected value; EP entry's latest documented blob matches current. See SHA findings. |
| §9 — CI and policy checks | **Partial** | Existing document-integrity workflow runs on PR/manual trigger and checks Markdown paths, architectural sections and selected presentations; it does not validate canonical→foreign-VNext roles or protected router SHA baselines. |
| §10 — Institutional applicability | **Boundary correctly separated; institutional process not audited here** | IMSV Receptio belongs to IMSV's competent institutional system, not GitHub. No transfer of authority is asserted. |
| §11 — History, freeze and exceptions | **Partial** | Git histories, preserved snapshots, .gitattributes and several study-specific manifests exist; complete frozen-source custody/parity cannot be inferred. |
| §12 — Controlled rollout | **Wave 0 publication only** | No mass VNext migration, full classification or CI enforcement is claimed by publishing this policy. |
| §13 — Maintenance and discoverability | **Addressed in publication** | CONTRIBUTING points to the consolidated root policy and a dated audit is linked from it. |

## Specific nonconformity candidates: controlled routers linking to foreign VNext

The following are **current direct links in editable controlled reader sources**. The named targets use VNext/VNEXT review notation, but final policy-violation classification requires confirming their formal role and any historical/freeze exception in the new register.

| Controlled reader source | Foreign review target(s) found |
| --- | --- |
| [Ecosystem Positioning README](../architectural-contributions/ecosystem-positioning/README.md) | EA Requirements VNEXT review/delta draft |
| [EA entry README](../research/ecosystem-awareness/README.md) | DDS Stage A / Challenge Trajectory Profile VNext |
| [EA baseline README](../research/ecosystem-awareness/baseline/README.md) | Requirements VNEXT review and 04 General Interfaces VNEXT review |
| [EA FG-TIDA README](../research/ecosystem-awareness/fg-tida/README.md) | 05 and 05A interface VNEXT review/delta drafts |

These examples show why direct-link checks are needed. **Do not rewrite these reader routes automatically:** their explanatory meaning and alternate current canonical routes must be preserved, and the VNext-like drafts must first be classified correctly.

## Protected SHA and actual GitHub enforcement

- EA entry router: **last recorded protected blob** in the 2 October control note: 4e41fc697bb2bd94d1f4dd2b75230937684b8152; **observed current blob:** 3ff5c26946b25608cea5cc1c9df8519dc61e1afd. The current file differs from the registered baseline.
- The last EA router edit located in GitHub's file history is [1848357 (10 October)](https://github.com/dakleyer/structural-awareness-contributions/commit/1848357ae9630c6f97067c5071fa309a5d449a50), after several earlier October additions/rewrites. The [e45c825 commit of 20 October](https://github.com/dakleyer/structural-awareness-contributions/commit/e45c8253251a1c7efbdb826e22ddb56521ab2ca4) changed a DDS VNext, **not** this router. The SHA mismatch does not prove that the underlying EA changes were unauthorized.
- Ecosystem Positioning router: observed current blob 9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b, matching the latest 15 October historical entry.
- Ecosystem Positioning Development Strategy: current blob f25aef42574afa9d321b352b3d2b1e1447575556; append-only guard is described historically but no executable baseline check was found.
- The repository's main branch reported **protected: false**, the inspected rulesets list was empty, and no CODEOWNERS file appeared in the conventional locations. Accordingly, current CI failure on push would detect rather than prevent a direct modification. Effective merge-time controls need separate configuration and verification.

**Disposition:** open a human provenance/authorization review of the EA router changes; neither silently accept the observed SHA nor roll back substantive additions on the basis of a stale control field alone.

## Logical identity ambiguity: R01 parallel editions

Under 00G-R01, both extensions/ and feasibility/ hold an RATS_EXTENSION.md, a TECHNOLOGY_EXTENSION_PROTOCOL.md and a VNext beside each. Their Git blobs differ.

The current extensions/ Technology Protocol (documentary v0.4) explicitly describes feasibility/ as a retained edition, whereas the feasibility/ README still routes to its local protocol as a working reference. The two RATS sources also carry closely overlapping canonical wording. These facts require a **logical-identity and lifecycle decision**, not a mechanical deduplication or deletion. If one edition is historic, preserve both its original source and review record; only one current canonical/VNext pair should be active per chosen logical subject. If the scopes truly differ, give them distinct stable logical IDs.

## GitHub Actions verification of the publication (PR #25)

The existing `Documentation integrity` workflow ran on [publication PR #25](https://github.com/dakleyer/structural-awareness-contributions/pull/25), [run 40174825789](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/40174825789), and **failed on four existing relative-link references**, all in two unchanged scientific VNext files:

- `research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md`: two occurrences of a relative link to `./PUBLICATION_MANIFEST.json`.
- `research/ecosystem-awareness/baseline/fixtures/00K-SUITE/README_VNext.md`: relative links to the `00L_A13_AUDITORIA_TRANSVERSAL_PRUEBAS_v0.1.md` and `00L_A14_CORRECCIONES_AUDITORIA_v0.1.md` artifacts under `./00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/`.

Both source files are present unchanged in the pinned baseline `21e200c`; neither was edited in this documentary-control publication. The four active Markdown files altered or introduced by the policy publication add **no broken local links** in the separate publication-specific check. This is a **documented inherited CI failure, not a passing repository-wide check**. The references require a separately scoped, evidence-preserving repair or properly explained exception; publication of this policy does not silently resolve them. These findings are additional to, and not counted among, the 1,565 method-scoped VNext-link occurrences assessed above.

## Priority and next-wave acceptance criteria

**P0 — Integrity and enforceability**

1. Resolve the EA router's recorded-versus-observed SHA through exact owner review; preserve the 2 October and 10 October versions.
2. Decide and configure suitable branch/ruleset protections for controlled documents, and test whether required checks and reviews actually block unauthorized merges.

**P1 — Identification and classification**

3. Populate a small cross-corpus document registry starting with protected routers, the nine controlled navigation owners and active VNext pairs.
4. Resolve the RATS/Technology Protocol parallel-edition ambiguities.
5. Classify the 176 currently identified VNext-link source files by actual documentary role before declaring link violations; retain justified historic/contextual exceptions.

**P2 — Technical checks and corrections**

6. Extend the existing checker for logical uniqueness, foreign VNext from mutable canonical sources, protected SHA and explicit exceptions; keep historical code/documentary evidence out of destructive rewrites.
7. Review the confirmed canonical-router candidate links in bounded PRs, preserving exact current canonical meaning and reader accessibility.

**P3 — Closure**

8. Produce a new pinned post-correction inventory, demonstrate enforcement coverage and identify what remains unchecked.
9. Close the audit's follow-up only to the scope evidenced. Full scientific or institutional certification is expressly outside this control-document exercise.

## Preservation and limitations

The audit is read-only with respect to scientific claims, frozen evidence, canonical technical content, README routing and VNext proposals. Publishing the consolidated policy, its historic predecessor, the CONTRIBUTING pointer, this report and the numerical link inventory **does not execute any scientific promotion or VNext-link correction**. GitHub is the public technical provenance source; existing controlled Drive editions and IMSV institutional records retain their separately declared authority.


## Second conformance audit — 25 October 2026

**Assessment completed; implementation remains partially conformant.** The policy is coherent after the small approved clarifications. Custody, current reading routes and review reception are stronger. The remaining material gaps are the logical-document register, resolution of protected-source authority, six direct foreign-review edges from four controlled routers, and enforceable GitHub safeguards. Those gaps have specific dispositions below.

**Reviewer:** Codex, AI-assisted second assessment in the same conversation. This is a new assessment of the policy and its implementation, not a second independent human certification. **Decision owner:** Iván Abril Palma. His instruction authorizes the small clarifications and this second audit. [PR 26](https://github.com/dakleyer/structural-awareness-contributions/pull/26) contains the complete approved control pairs and the bounded application. Its Git diff records the final changed paths; scientific hypotheses, evidence and institutional status do not advance by this publication.

### Scope, cuts and method

The first assessment above is preserved in full as its dated historical baseline. This second assessment checks all thirteen clauses of [DC-GH-01](../DOCUMENT_CONTROL.md), the actual tree and all Markdown links, then reads the material source/receiver relationships and exceptions needed to interpret the findings. It is a document-control audit, not a repetition or completion claim for the five scientific readings and corpus consolidation prescribed by the substantive review procedure.

Three cuts are distinguished:

1. **First-audit baseline:** `21e200cd4c9a0558e4ae3669c55f7256c03a005a`, before policy consolidation; ,401 files and ,045 Markdown files.
2. **Second-audit source:** `b9499c34e8690acdc9a1d1b6f274895a94c4c4b9`; ,405 files, ,048 Markdown files and 103 files named exactly README.md. The consolidation adds four custody/control artifacts, changes seven control paths, and deletes no file. Both complete predecessor texts match their original blobs.
3. **Approved application:** the PR 26 diff against that source, including the seven literal control units, existing review repairs 148–150, reciprocal review reception and this appended assessment. The final whole-tree check keeps the same file set and modes. The [dated inventory](./review/DOCUMENT_CONTROL_VNEXT_LINK_INVENTORY_2026-10-25.json) adds a second-assessment object without replacing any original baseline member. It contains per-occurrence evidence, source profiles, role uncertainties and full parser instructions.

All ,048 Markdown files are parsed with **marked 17.0.5, GFM enabled**. Link/image tokens, reference-style links, HTML href/src, heading slugs and explicit IDs are checked separately; fenced/inline code is excluded from rendered navigation. Current same-repository main URLs resolve against the tree, as do relative paths and folder README fragments. Pinned historic and external URLs are a separate population: the repaired historical destinations are individually checked, while an exhaustive live external-link crawl is outside this assessment. First-literal line positions carry an explicit uniqueness flag; repeated literals are not assigned invented exact locations.

The inventory’s “working” and “legacy” subsets use the first audit’s path exclusions. They are populations for counting, **not** declarations of canonicality, active review status or authority. The nine navigation owners are supported by the policy and predecessor text. Other source classes remain provisional until their declared logical relations have been adjudicated. A numbered file, a successful path check or the absence of “VNext” in a filename does not decide its role.

### Findings against every policy clause

| Clause | Required relationship | Current evidence and verdict | Disposition |
| --- | --- | --- | --- |
| §1 — Authority and precedence | One current general policy; source-specific freeze and owner restrictions survive | **Conformant at policy level.** Root DC-GH-01 is current; v0.1 is a historical pointer with its exact predecessor retained. Review Procedure, Claim Boundaries and EA Manifest retain distinct substantive/scientific/custody scope. v1.0.1 carries forward the three technical reading levels. | Keep this authority order. The register must receive the protected named-file restrictions; policy consolidation did not repeal them. |
| §2 — Technical provenance | Git revisions/PRs provide technical history; semantic decisions remain distinct | **Available and used.** PR 26 holds the exact units, owner instruction and actual diff. Immutable pre-application links preserve complete retired cards. No institutional receipt or scientific result is inferred from a merge. | Use the PR and pinned source editions; avoid copying a technical changelog into every source. |
| §3 — Identity, role, lifecycle, maturity | Distinct concepts, supported per logical source | **Text coherent; implementation partial.** The hypothesis/canonical distinction agrees with the 24 October Foundation/01A-A01/02A reception. Those records explicitly retain FH-C/FH-E as unvalidated causal/computation hypotheses. Older proposal status is explained by later editorial-adoption receipts rather than treated as evidence of a new proof. | Register scope and lifecycle separately. Do not infer validation from the word “canonical.” |
| §4 — Logical register | One operational path and supported identities, with unknowns explicit | **Not implemented.** `governance/DOCUMENT_REGISTRY.yml` is absent. The policy now names exactly that path in both §§4 and12; Wave1 inventories/adjudicates, Wave2 creates the register. The dated link inventory is evidence, not a substitute registry. | Start with nine owners, three protected sources and current logical pairs; retain unresolved mappings. |
| §5 — Canonical/VNext contract | One active companion; own links allowed, mutable canonical→foreign VNext disallowed | **Partial.** The declared benchmark v0.3 review alias is recognized. Repeated review passes and preserved snapshots are not extra active companions. Six foreign-review edges from four controlled current routers are confirmed by reading target declarations, not just filenames. Two R01 edition families still need logical-owner decisions. | Resolve the six edges through owner-scoped routing changes after protection review; adjudicate R01 scope before any merge, demotion or removal. |
| §6 — Navigation ownership | Stable owners, three canonical technical reading levels, no content loss | **Clarified and preserved in this application.** Nine controlled owners are nine paths, not nine levels. Package/fixture READMEs and the three additional-work sheets remain subordinate/optional. The unchanged gradient card regains an explicit route; 02A and Foundation now receive each other’s review ownership. | Keep exact content and incoming anchors. No file move, rename, hierarchy expansion or deletion is performed. |
| §7 — Review and promotion | Bounded proposal, owner decision, exact incorporation and receiver checks | **Used in this application.** Seven complete literal control pairs were published before incorporation. Repairs148–150 already had complete units, impact/risk/cost and now have Iván’s GO. Their applied cards are retired with compatibility anchors and immutable historical receipts. | Other proposals remain in their prior states. Neither this audit nor a passing check authorizes their execution. |
| §8 — Protection and historical integrity | Approved baseline distinct from observed bytes; exact scoped preservation | **Application preserved; inherited authority discrepancy open.** EA observed blob differs from the 2 October protected record. EP matches its 15 October record; strategy retains its exact current blob. Frozen split sources and quoted historical records are unchanged. | Review the EA historical changes and record the specific accepted successor or correction. Do not reset a SHA or restore an old router automatically. |
| §9 — Checks and effective safeguards | Actual policy/role/SHA checks, with merge enforcement verified | **Partial and unenforced.** Existing workflow checks paths, eight EP section minima and two presentation containers/content minima. It does not check logical roles, foreign companions or protected SHA rules. Main reports unprotected, rulesets are empty and no CODEOWNERS exists. | Extend the existing mechanism after supported mappings; separately authorize and verify settings that can actually block merges. Preserve the inherited CI findings described below. |
| §10 — Institutional boundary | Technical repository authority stays separate from formal adoption | **Coherent within the inspected control/reception records.** Research canonicality, Git merge, FG-TIDA contribution, scientific validation and IMSV Receptio remain different states. | No institutional action is made or certified here. |
| §11 — Exceptions and custody | Historic/frozen meanings retained; narrowly identified exceptions | **Partial.** Two policy predecessors are exact. Four quoted relative-link reports and one split-file fragment have concrete contexts/valid receivers. These are not permission to exclude all VNext or all quotations from checks. | Retain raw historic strings and provide source-context-aware diagnostics. Broader frozen-source parity is governed by its own manifests. |
| §12 — Rollout and acceptance | Inventory before adjudication/enforcement; bounded corrections and qualified closure | **Wave0 clarified; Wave1 evidence expanded; approved review repairs applied.** Global role adjudication, registry, safeguards and canonical-router corrections remain open. Completing this second audit does not complete those waves. | Follow the ordered acceptance actions below; close only demonstrated scopes. |
| §13 — Maintenance | One policy, working reader route, preserved approved editions | **Current policy and reader route corrected.** CONTRIBUTING uses a stable DC-GH-01 label; the policy points directly to this second assessment. The original source-location link makes the preserved predecessor usable without rewriting its relative strings. | Maintain this report as dated assessments, not competing current policies or new VNext per round. |

### Count reconciliation: explain the difference before judging it

The original inventory reported,747 inline VNext links, of which,565 were in its working subset. A fresh **GFM-token recount of the same21e200 baseline** obtains,786/,600. The working difference is confined to three sources: EP README VNext226 versus227; 01K VNext24 versus10; R01 oracle README VNext39 versus17. The legacy difference is four occurrences. Both methods identify176 working source files. Fifteen reference-style VNext occurrences form a separately excluded population. The difference is a parser/denominator reconciliation, not35 discovered policy violations. The first extractor’s exact implementation was not in its public artifact, so its old scalar counts are preserved as reported rather than rewritten or falsely certified as fully reproduced.

The second inventory publishes the actual GFM method and individual occurrence rows. The same-repository-main URL population is included in “local” for this assessment and separated by locality; the old inventory grouped external-looking URLs differently. Its950 local occurrences must therefore not be compared directly with this assessment’s local count. File, occurrence, distinct-edge, source-count and role-decision measures stay separate.

At the second source cut: **,788 inline VNext occurrences,,596 working,,192 legacy;15 reference-style occurrences;177 working source files;74 working filename-hinted VNext files plus the existing benchmark alias.** Local working occurrences:,166; distinct local source→target pairs:666; missing local VNext target paths:zero. These are measured graph populations, not75 approved logical pairs or proof of completed substantive passes.

After the approved application, the full GFM counters and path/fragment diagnostics are recorded in the dated inventory. Repair 148 exposes previously hidden later audit text, so the rendered-link population grows without creating an audit, copying a source or adding a VNext. Repairs 149/150 move historical references from moving main to the exact edition containing the old sections. Increased/decreased counts must be read with those concrete changes.

**Final destination revalidation corrected two prepared pins before incorporation.** The old00N context-size and MSCA B_Cart proposal headings are absent at the initially proposed e59430d edition. Both complete historical sections and rendered heading IDs are present at `5c8024b8e86f01151d204ecc6b568173ffebd8e4`. The two revised complete pairs were published in EP VNext in PR 26 commit `2ff1367ac1b940ee73f46f981b7072525139b19e` before application. Other149/150 destinations were individually verified at e59430d. The older prepared proposal remains visible in pinned history; it is not misreported as already having a valid destination.

### Six confirmed foreign-review edges, with their actual meaning

All nine controlled owner paths exist. Their VNext-labelled rendered links are enumerated in the inventory, including own links, repeats and sources with none. Six foreign edges occur in four owners:

| Current router and source line atb9499 | Target’s explicit declaration | Assessment and next action |
| --- | --- | --- |
| [EP README](../architectural-contributions/ecosystem-positioning/README.md),492 | Requirements delta says “Working review only — not a new Requirements document”; frozen00 remains the canonical requirement source | Foreign review under §5. EP is protected. Preserve the substantive explanation and offer a source-level route with review access through its own companion; exact protected-source change needs a named decision. |
| [EA entry](../research/ecosystem-awareness/README.md),280 | DDS Stage A VNext explicitly owns the Stage A profile, not the EA entry | Foreign review in a development-route list. Reconcile the EA protection baseline first, then maintain access through the EA companion/current DDS source rather than removing the review history. |
| [Baseline index](../research/ecosystem-awareness/baseline/README.md),152 and165 | Requirements and04 deltas explicitly review different frozen/current source units | Two foreign edges; the labels do not promote either delta to canon. Plan a bounded source-route adjustment together with the Requirements/04 reception, preserving visibility of proposed work. |
| [FG-TIDA index](../research/ecosystem-awareness/fg-tida/README.md),44–45 | 05 is a working ideal delta, not an adopted architecture;05A is the dated current-state delta, not a new ideal source | Two foreign edges. Preserve the ideal/current-source distinction and the actual05/05A version/part relationships. Do not redirect both to one general interface or lose their proposal routes. |

EP and EA also repeat their **own** companion link. “Normally once” in §5 is a readability preference, not a second active companion or an automatic authority violation. Root/submissions/fixture owners lacking such labelled links are not failures merely for lacking one; editability/freeze and actual companion availability matter. No current canonical router is edited by this application.

### Protection provenance: what actually changed in EA

The last recorded protected EA blob is `4e41fc697bb2bd94d1f4dd2b75230937684b8152`; the observed current blob is `3ff5c26946b25608cea5cc1c9df8519dc61e1afd`. Comparing those exact blobs shows added review/reduction routes,01K component navigation, DDS method/stage wording and validation/claim-custody routes. The net size increase is4,720bytes; it is **not** an append-only prefix comparison because some earlier paragraphs were edited. This is a description of the delta, not a conclusion that useful source material was lost.

The scoped history locates the 2 October reduction addition (`172582d`),6 October review/DDS/01K entries (`fdb530e`, `b04fb86`, `11fbc6e`, `d56e2e9`, `4a0720a`),7 October DDS routing/terminology (`b204e6e`, `64fa9f3`, `6b62d8d`) and10October evidence/custody routes (`b297e3c`, `1848357`). The final router edit is10October, not the20October DDS-VNext edit. The 2 October recorded hash predates those changes; neither commit messages nor current publication alone supply the missing file-specific acceptance record.

**Required decision:** identify which of those exact EA-router deltas were accepted and whether the observed successor is the approved current baseline, or specify a targeted correction. Preserve both editions and all verified useful routes. This application leaves the observed EA file, the old recorded SHA, EP blob `9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b` and strategy blob `f25aef42574afa9d321b352b3d2b1e1447575556` unchanged. It does not silently bless or roll back EA.

### Logical ownership, versions and review reception

The74 working filename-hinted reviews and the existing benchmark v0.3 alias have their openings and candidate source relations retained in the inventory. Their count is a search population, not an adjudicated active register. The benchmark explicitly says it is already the review of 00D while v0.2 remains canonical; creating another00D VNext would be wrong. Current/historical parts of04/05 and older01B editions similarly cannot be declared new logical sources just because paths differ.

Two R01 families need a substantive identity decision: `extensions/` and `feasibility/` each contain RATS_EXTENSION and TECHNOLOGY_EXTENSION_PROTOCOL with separate, different review/source blobs. The extensions protocol describes feasibility as a retained edition, but feasibility still supplies local study/fixture/workplan context and both RATS sources carry current integration wording. Their contents are not byte duplicates and their evidence is scoped. Decide whether each is a retained edition of one logical unit or a distinct scoped subject. Preserve each source and review until that decision; do not merge the sources or label the reviews independent simply because there are two files.

The 24 October 02A VNext was narrower than the earlier Foundation dossier. It now links the complete 14 October 02A/02B proof-attribution audit retained in 01_FOUNDATIONAL_VNext; Foundation reciprocally identifies 02A’s current source-owned companion. The earlier audit remains full and visible, proposal 100 stays applied, and no competing 02A shadow is created. This resolves reader ambiguity without changing the derivation proof or 02B. The gradient review card is likewise unchanged and linked as optional review history from EP VNext; its temporary loss of an explicit incoming route was navigation loss, not deletion of the underlying source.

### Path, section and historical-source reconciliation

The complete main-tree GFM scan atb9499 sees33 unresolved fragment occurrences:16 in working-path files and17 in preserved/legacy records. The approved repairs resolve the 16 working occurrences: five to the DDS14October plan and eleven to historical review headings. Compatibility anchors on the148–150 application receipts retain the old incoming review-card routes. The full assessment adds no new broken target or fragment and makes no previously reachable file unreachable in the explicit file-edge graph. Folder links and external/pinned routes are reported separately rather than used to overclaim total reachability.

The broad scanner also reports,455 unresolved path occurrences at that source cut.,450 occur in the path-excluded historical population, where relocated source-relative citations retain their original strings. The remaining five require contextual reading:

1. **Two04-review links** to `./PUBLICATION_MANIFEST.json` occur inside retained quoted source units. Their source owner is the04 input-interface contract, with the actual receiver [04_INPUT_INTERFACE_CONTRACT/PUBLICATION_MANIFEST.json](../research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/PUBLICATION_MANIFEST.json). They are bad clicks if interpreted relative to the review directory, not absent manifest files. The adjacent review already explains their owner context.
2. **Two00K-review links** to A13/A14 are in the retained A22 quotation. Their actual receivers are the [A13 audit](../research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A13_AUDITORIA_TRANSVERSAL_PRUEBAS_v0.1.md) and [A14 corrections](../research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md); the following current paragraph already provides working routes. Preserve the literal old quotation.
3. **The fifth report is a split-source boundary.** UC-EA-03 maintenance-freeze part02 ends inside the URL `.../submissions/it`; part03 begins `u-fg-tida/.../02_ANNEX_I_Minimal_Operational_Case.md)`. Concatenating the declared parts reconstructs the complete existing Annex I destination. It is not a missing `submissions/it` source or justification to edit frozen parts. A file-only URL scanner cannot infer that logical split unit. The inventory records the fragments and assembled target.

These explanations do not turn a red repository check green. The existing integrity workflow is still affected by the **four** quoted-relative-reference reports in04/00K. Its narrow exception/diagnostic design must identify the exact quote and source context. Excluding all VNext, all blockquotes or the whole directory would hide genuine mutable navigation errors. The split-source report is a separate GFM diagnostic; it is not among those four CI reports. No checker code or historic source text is changed here.

### Applied small corrections and preservation checks

- **DC-GH-01:** seven complete approved control/CONTRIBUTING units only. One registry path, explicit rollout order, three technical README levels, direct latest-assessment route and a working original-location predecessor link. The previous v1.0 remains in Git; both older custody snapshots remain byte-exact.
- **148:** one separator LF restores the existing DDS historical-source code closer. The complete22,330byte Stage A predecessor remains exactly once as contiguous original bytes; the newly visible later audit text is existing material.
- **149/150:** ten EP and one HF historical hrefs now identify the pinned edition containing their sections. Scientific results, source text and older proposals are unchanged. The complete application cards remain accessible in the immutable pre-application edition; current pending cards are replaced by short applied receipts with their old anchor IDs.
- **Reception:** two reciprocal02A/Foundation appendices and one optional gradient-card route; no source is copied, moved or removed. EP’s already-public complete clarification plan is retained exactly.
- **Verification:** exact source matches, per-operation reverse reconstruction, same tree paths/modes, unchanged protected/scientific/program/result/frozen blobs outside the scoped files, preserved first-audit prefix and inventory baseline members, consistent JSON/CSV states for148–150, full path/fragment comparison and pinned public readback. The final PR/commit supplies the executable provenance of this application; no self-referential “final hash” is inserted into the audit body.

### Priorities, impact, risk and acceptance

| Order | Action and concrete benefit | Expected impact | Risk / effort | Acceptance condition |
| --- | --- | --- | --- | --- |
| **Applied** | Small policy precision and148–150/reception repairs: readable audit history, usable section links and a single register target | High for reader continuity | Low / Low | Exact units, inverse and graph checks; current cards no longer pending |
| **First** | Adjudicate the EA protected successor and the two R01 scope families; prevent a valid current route or distinct evidence profile being mistaken for an unauthorized duplicate | High | High if edited before the decision; low-risk read-only decision preparation / Medium | Exact edition/delta/authority record; current approved SHA or targeted correction named; separate scopes or one retained history justified |
| **First, dependent** | Create the small operational register at the one declared path, beginning with protected sources, nine owners and supported companions | High | Medium / Medium | Stable IDs/roles/lifecycle/protection and decision refs; conflicts and unclassified records explicit; no inferred promotion |
| **Next** | Amend the six confirmed foreign-review router edges while preserving source/proposal access and meaning | High | Medium, including protected sources / Medium | Complete literal pairs in the current owner VNext, accepted protection baseline, receiver/incoming-anchor check and named owner GO |
| **Next** | Extend the existing checker with supported logical relations, exact historical exceptions and protected-source checks | High | Medium / Medium–High | Demonstrate true positives, preserved-source exceptions, failure on conflicting ownership and no blanket VNext exclusion |
| **Next, explicit settings scope** | Configure and test actual merge protections | High | Medium / Medium | Verified settings and required checks/reviews actually reject an inadmissible merge; after-push detection alone is insufficient |
| **After** | Final role-aware conformance rerun and exception/owner closure | High | Low after dependencies / Medium | All above decisions resolved or explicitly bounded; current pinned inventory, actual workflow result and residual coverage stated |

**Current conclusion:** the small clarification/reception work is complete within its approved scope. The general control is useful and internally consistent; the repository remains **partially conformant** because the register, authority reconciliation and enforceable safeguards are unfinished. The next wave is identity and authority adjudication, followed by supported safeguards and six bounded router corrections. It is not a mass rewrite, file cleanup or scientific promotion.
