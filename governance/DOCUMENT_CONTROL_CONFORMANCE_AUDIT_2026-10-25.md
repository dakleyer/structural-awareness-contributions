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

1. **First-audit baseline:** `21e200cd4c9a0558e4ae3669c55f7256c03a005a`, before policy consolidation; 2,401 files and 1,045 Markdown files.
2. **Second-audit source:** `b9499c34e8690acdc9a1d1b6f274895a94c4c4b9`; 2,405 files, 1,048 Markdown files and 103 files named exactly README.md. The consolidation adds four custody/control artifacts, changes seven control paths, and deletes no file. Both complete predecessor texts match their original blobs.
3. **Approved application:** the PR 26 diff against that source, including the seven literal control units, existing review repairs 148–150, reciprocal review reception and this appended assessment. The final whole-tree check keeps the same file set and modes. The [dated inventory](./review/DOCUMENT_CONTROL_VNEXT_LINK_INVENTORY_2026-10-25.json) adds a second-assessment object without replacing any original baseline member. It contains per-occurrence evidence, source profiles, role uncertainties and full parser instructions.

All 1,048 Markdown files are parsed with **marked 17.0.5, GFM enabled**. Link/image tokens, reference-style links, HTML href/src, heading slugs and explicit IDs are checked separately; fenced/inline code is excluded from rendered navigation. Current same-repository main URLs resolve against the tree, as do relative paths and folder README fragments. Pinned historic and external URLs are a separate population: the repaired historical destinations are individually checked, while an exhaustive live external-link crawl is outside this assessment. First-literal line positions carry an explicit uniqueness flag; repeated literals are not assigned invented exact locations.

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

The original inventory reported 2,747 inline VNext links, of which1,565 were in its working subset. A fresh **GFM-token recount of the same21e200 baseline** obtains 2,786/1,600. The working difference is confined to three sources: EP README VNext226 versus227; 01K VNext24 versus10; R01 oracle README VNext39 versus17. The legacy difference is four occurrences. Both methods identify176 working source files. Fifteen reference-style VNext occurrences form a separately excluded population. The difference is a parser/denominator reconciliation, not35 discovered policy violations. The first extractor’s exact implementation was not in its public artifact, so its old scalar counts are preserved as reported rather than rewritten or falsely certified as fully reproduced.

The second inventory publishes the actual GFM method and individual occurrence rows. The same-repository-main URL population is included in “local” for this assessment and separated by locality; the old inventory grouped external-looking URLs differently. Its950 local occurrences must therefore not be compared directly with this assessment’s local count. File, occurrence, distinct-edge, source-count and role-decision measures stay separate.

At the second source cut: **2,788 inline VNext occurrences; 1,596 working; 1,192 legacy;15 reference-style occurrences;177 working source files;74 working filename-hinted VNext files plus the existing benchmark alias.** Local working occurrences: 1,166; distinct local source→target pairs:666; missing local VNext target paths:zero. These are measured graph populations, not75 approved logical pairs or proof of completed substantive passes.

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


## Corpus action and VNext-promotion plan reception — 25 October 2026

Iván directs the [single cross-corpus action/promotion/verification plan](../DOCUMENT_CONTROL.md#14-corpus-action-promotion-and-verification-plan--25-october-2026) to live inside DOCUMENT_CONTROL, linked to this audit. The plan identifies eight selected VNext blocks through three exact receiving-source pairs, operative-control refinements, literal routing pairs, a prospective registry/CODEOWNERS, a unique check and exact proposed protection settings. Publication is the planning step; each incorporation wave receives its own GO. No proposed source, registry, code or GitHub setting is applied in this publication.

**Additional semantic-link finding:** the preceding six named-VNext router edges were a filename-scoped subset. The existing00Dbenchmark v0.3 file explicitly declares itself the benchmark VNext despite lacking VNext in its filename. It adds four foreign-review router occurrences: two inEP, one inEA and one inbaseline. The plan therefore covers ten confirmed foreign-review router occurrences, plus the living05A preface’s direct05review route. This is a role/navigation finding, not four missing files or an adopted benchmark. The frozen05part retains its original historical citations under its own edition.

**Enforcement precondition:** current GitHub checks share the name verify, from application 15368; a future required check must have an unambiguous published name. Existing PR authorship is@dakleyer, so owner-only approval requires a distinct automation author before activation. The action plan provides the actor/check/settings acceptance tests and keeps both constraints visible.

<details>
<summary>Existing review directory for the 75-unit promotion coverage queue</summary>

- [../architectural-contributions/ecosystem-positioning/01_GRADIENT_VNext.md](../architectural-contributions/ecosystem-positioning/01_GRADIENT_VNext.md)
- [../architectural-contributions/ecosystem-positioning/README_VNext.md](../architectural-contributions/ecosystem-positioning/README_VNext.md)
- [ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md](../research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md)
- [ecosystem-awareness/DDS_RESEARCH_BASIS_AND_BENCHMARKING_2026-10-06_VNext.md](../research/ecosystem-awareness/DDS_RESEARCH_BASIS_AND_BENCHMARKING_2026-10-06_VNext.md)
- [ecosystem-awareness/README_VNext.md](../research/ecosystem-awareness/README_VNext.md)
- [ecosystem-awareness/baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1_VNext.md](../research/ecosystem-awareness/baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1_VNext.md)
- [ecosystem-awareness/baseline/00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1_VNext.md](../research/ecosystem-awareness/baseline/00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1_VNext.md)
- [ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md](../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md)
- [ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README_VNext.md](../research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README_VNext.md)
- [ecosystem-awareness/baseline/00M_A01_VNext.md](../research/ecosystem-awareness/baseline/00M_A01_VNext.md)
- [ecosystem-awareness/baseline/00M_VNext.md](../research/ecosystem-awareness/baseline/00M_VNext.md)
- [ecosystem-awareness/baseline/00N_ADDENDUM_VNext.md](../research/ecosystem-awareness/baseline/00N_ADDENDUM_VNext.md)
- [ecosystem-awareness/baseline/00N_VNext.md](../research/ecosystem-awareness/baseline/00N_VNext.md)
- [ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md](../research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md)
- [ecosystem-awareness/baseline/01A_A01_VNext.md](../research/ecosystem-awareness/baseline/01A_A01_VNext.md)
- [ecosystem-awareness/baseline/01A_VNext.md](../research/ecosystem-awareness/baseline/01A_VNext.md)
- [ecosystem-awareness/baseline/01B_VNext.md](../research/ecosystem-awareness/baseline/01B_VNext.md)
- [ecosystem-awareness/baseline/01C_VNext.md](../research/ecosystem-awareness/baseline/01C_VNext.md)
- [ecosystem-awareness/baseline/01D_VNext.md](../research/ecosystem-awareness/baseline/01D_VNext.md)
- [ecosystem-awareness/baseline/01H_VNext.md](../research/ecosystem-awareness/baseline/01H_VNext.md)
- [ecosystem-awareness/baseline/01I_VNext.md](../research/ecosystem-awareness/baseline/01I_VNext.md)
- [ecosystem-awareness/baseline/01J_VNext.md](../research/ecosystem-awareness/baseline/01J_VNext.md)
- [ecosystem-awareness/baseline/01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1_VNext.md](../research/ecosystem-awareness/baseline/01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1_VNext.md)
- [ecosystem-awareness/baseline/01K_VNext.md](../research/ecosystem-awareness/baseline/01K_VNext.md)
- [ecosystem-awareness/baseline/01_FOUNDATIONAL_VNext.md](../research/ecosystem-awareness/baseline/01_FOUNDATIONAL_VNext.md)
- [ecosystem-awareness/baseline/02A_VNext.md](../research/ecosystem-awareness/baseline/02A_VNext.md)
- [ecosystem-awareness/baseline/03_FUNCTIONAL_VNext.md](../research/ecosystem-awareness/baseline/03_FUNCTIONAL_VNext.md)
- [ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md](../research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md)
- [ecosystem-awareness/baseline/README_VNext.md](../research/ecosystem-awareness/baseline/README_VNext.md)
- [ecosystem-awareness/baseline/UC-EA-03_VNext.md](../research/ecosystem-awareness/baseline/UC-EA-03_VNext.md)
- [ecosystem-awareness/baseline/fixtures/00G-HF-ORACLE-v0.4/README_VNext.md](../research/ecosystem-awareness/baseline/fixtures/00G-HF-ORACLE-v0.4/README_VNext.md)
- [ecosystem-awareness/baseline/fixtures/00I-STATEFUL/README_VNext.md](../research/ecosystem-awareness/baseline/fixtures/00I-STATEFUL/README_VNext.md)
- [ecosystem-awareness/baseline/fixtures/00K-SUITE/README_VNext.md](../research/ecosystem-awareness/baseline/fixtures/00K-SUITE/README_VNext.md)
- [ecosystem-awareness/baseline/fixtures/RS-00E-Q1a/README_VNext.md](../research/ecosystem-awareness/baseline/fixtures/RS-00E-Q1a/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/COMPUTABILITY_AND_ORACLE_PLAN_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/COMPUTABILITY_AND_ORACLE_PLAN_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/FENCING_CONFUSED_DEPUTY_EXTENSION_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/FENCING_CONFUSED_DEPUTY_EXTENSION_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/HUMAN_ESCALATION_WHISPERING_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/HUMAN_ESCALATION_WHISPERING_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/RATS_EXTENSION_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/RATS_EXTENSION_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/SPIFFE_SPIRE_EXTENSION_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/SPIFFE_SPIRE_EXTENSION_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/STAMP_STPA_EXTENSION_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/STAMP_STPA_EXTENSION_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/TECHNOLOGY_EXTENSION_PROTOCOL_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/TECHNOLOGY_EXTENSION_PROTOCOL_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/cache-ttl/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/cache-ttl/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/dds-study-completion-v0.1/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/dds-study-completion-v0.1/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/durable-workflows-retries/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/durable-workflows-retries/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/extension-audit-v0.1/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/extension-audit-v0.1/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/hugging-face/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/hugging-face/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/mcp-tool-calling/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/mcp-tool-calling/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/oauth-oidc/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/oauth-oidc/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/observability-response/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/observability-response/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/queues-ack-redelivery/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/queues-ack-redelivery/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/rag/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/rag/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/sql-transactions-idempotency/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/sql-transactions-idempotency/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/extensions/structured-output/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/structured-output/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/feasibility/FENCING_CONFUSED_DEPUTY_EXTENSION_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/FENCING_CONFUSED_DEPUTY_EXTENSION_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/feasibility/RATS_EXTENSION_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/RATS_EXTENSION_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/feasibility/SPIFFE_SPIRE_EXTENSION_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/SPIFFE_SPIRE_EXTENSION_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/feasibility/STAMP_STPA_EXTENSION_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/STAMP_STPA_EXTENSION_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/feasibility/TECHNOLOGY_EXTENSION_PROTOCOL_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/TECHNOLOGY_EXTENSION_PROTOCOL_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/feasibility/dds-study-completion-v0.1/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/dds-study-completion-v0.1/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/feasibility/partial-experiments/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/partial-experiments/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/oracle/README_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README_VNext.md)
- [ecosystem-awareness/baseline/reductions/00G-R01/oracle/UC4_INTEROPERABILITY_PROFILE_VNext.md](../research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/UC4_INTEROPERABILITY_PROFILE_VNext.md)
- [ecosystem-awareness/baseline/traversals/00G-HF-DYNAMIC-REVIEW-v0.1/README_VNext.md](../research/ecosystem-awareness/baseline/traversals/00G-HF-DYNAMIC-REVIEW-v0.1/README_VNext.md)
- [ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md](../research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md)
- [ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md](../research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md)
- [regime-awareness/README_VNext.md](../research/regime-awareness/README_VNext.md)
- [../standards/minimum-sufficient-control/00_ARCHITECTURE_VNext.md](../standards/minimum-sufficient-control/00_ARCHITECTURE_VNext.md)
- [../standards/minimum-sufficient-control/01_ACC_VNext.md](../standards/minimum-sufficient-control/01_ACC_VNext.md)
- [../standards/minimum-sufficient-control/02_ROLE_VNext.md](../standards/minimum-sufficient-control/02_ROLE_VNext.md)
- [../standards/minimum-sufficient-control/03_COMPOSITION_VNext.md](../standards/minimum-sufficient-control/03_COMPOSITION_VNext.md)
- [../standards/minimum-sufficient-control/04_OPERATION_VNext.md](../standards/minimum-sufficient-control/04_OPERATION_VNext.md)
- [../standards/minimum-sufficient-control/README_VNext.md](../standards/minimum-sufficient-control/README_VNext.md)

</details>


## Completed consolidation of the action and VNext-promotion plan — 25 October 2026

The existing [global plan in DOCUMENT_CONTROL](../DOCUMENT_CONTROL.md#1411-completed-review-unit-adjudication--25-october-2026) now gives an individual source/receiver disposition for all 75 candidate reviews, complete current old/new units and bounded decision/evidence packets. It reconciles existing applications rather than inventing 75 new changes. The twelve selected substantive blocks are three Requirements interpretations, two general-interface explanations and seven dated source-state/EA-only interface readings.42 active Contributions pairs and two separately gated external pairs are prepared; none is applied by this publication.

The extended check found concrete gaps in the earlier plan: three owner-source assignments were wrong and ten missing primary bindings were completed (five are DDS_STUDY.md rather than nonexistent README.md); seven physical edition pairs need one declared active continuation; the Requirements promotion packet omitted two operative freeze notices; and the optional HumanTime alternative was stale after 93. The exact corrected pairs and edition differences are now in the same plan. The 04/00K four quotation receivers have a complete bounded checker candidate with 16 focused tests, separate from the 24 future native/semantic acceptance cases.

Fresh officialUC21 reading shows a newer body, updated 25 October 07:58:19UTC, already receiving the direct Contributions route, current source/profile table and subsequent campaign status.144/147 are not safe replay candidates. The official index still lacks 21 and its proposed title needed updating; the unmergedPR22 actually has 54 case files,44/48 original blobs equal and four identified receiving differences. E145R/E146R preserve those distinctions. No official body/comment, source program, frozen result or source edition is changed here.

The plan-level disposition is complete. The original conformance finding remains partial: the registry/identity decisions, actual safeguards and scientific/evidence work are not completed merely by the plan. Earlier audit bodies and their exact sources remain preserved. The same Codex assistant performed this consolidation; no new independent reviewer or sixth-pass completion is claimed.


## Action-plan 1.0 reassessment and 2.0 reception —25 October 2026

**Verdict: the two planning publications preserve their authorized scope; implementation readiness needs the specific corrections below.** Direct Git-tree comparison of2aa0c10→e79cae15→75f5b6bconfirms all 2,405 paths/modes retained, complete policy/audit byte prefixes and 2,401 other entries unchanged across the whole interval. PR 27 changed two files;PR 29 changed four. All 75 review surfaces remain exact. The priorities ledger retains 150 IDs, 151 CSV rows and the original pairs in dated history; 16 JSON records/17 CSV rows were reconciled, with 134 unrelated objects byte-identical. This verifies these two publications, not every earlier corpus edit.

The [action plan2.0 in the same control](../DOCUMENT_CONTROL.md#15-action-plan-20--reassessment-and-next-waves) retains every previous plan/audit section and supplies complete before/after corrections. All 42 literal old spans still match; seven complete control-file blobs advanced by plan appends, so execution must bind the actual head and operative regions. The 72-record proposal binds all 75 review surfaces but 61 source-under-review roles remain provisional, not adjudicated canonical/frozen/contextual classifications.

The original quotation candidate was reproduced against four same-file copy counterexamples: an identical line outside its historical section still received the historical target. Its 16 focused tests did not cover that attack. The old 42 stale checks asserted inequality and must not be described as 42 executed rejection paths. Checker-digest-only cached evidence is insufficient for changed source input. A2-07/08 provides a full-context/occurrence replacement proposal; actual validation results are recorded below. No checker, workflow or native setting is installed by this assessment.

Five report spans contain inherited lost leading digits. Those exact defects are already in2aa0c10, so neither planning merge deleted those digits. The existing public inventory and pinned trees supportA2-06a–e; the evidence values are not recomputed or regraded by repairing their prose. The source-specific 04/05 Areceiving notes are now exact conditional pairs rather than an unspecified future closure instruction.

The first practical low-risk/high-impact choice remains existing 2/6/7, with the current decision-entry and evidence-claim refinements.9 and 41 are separate medium-risk content packets with their explicit review receipts. Requirements identity, capacity alternatives, protected routing and actual enforcement retain their own decisions and dependencies. The 75 review dispositions do not establish completion of the scientific passes, source adoption, native controls or external institutional acceptance. Same Codex assistant; no independent-review claim.


**Verified reassessment evidence:**17 complete new pairs;42 earlier literal spans; two exact inverse packets;71 actual private planning-validator rejections,36 full-context quotation cases and three actual-main receiver-removal/recovery cases. The main fixtures isolate that receiver branch; their unrelated checks are not represented as tested there. The unchanged candidate constants separately retain8 architecture minima/4 references/2 decks. Raw ledger-span comparison confirms134 untouched objects and16 changed objects with original pairs preserved. Parser inputs for all1,048 Markdown sources are bound to the actual tree before the new publication graph run. None of this is an installed enforcement or a native-research claim.


**Publication and receiving-route verification:** the GFM differential over all 1,048 Markdown files finds zero newly broken paths/fragments, zero removed heading IDs and zero newly unreachable files. The separate hypothetical 19-unit packet combines these 17 proposals with existing source units 9/41 so their three review receipts can be checked against the actual receiving headings; it also introduces none of those navigation defects. That is a simulation, not application. Existing frozen/quoted/split-source diagnostics remain in their original scope.


## Action-plan 2.0 application verification — 25 October 2026

Iván authorized execution of the existing 2.0 plan. The packet implements its 17 literal pairs plus existing 2/6/7/9/26/38–41: 26 units across 11 existing files. Source preimages were bound to actual main f8ce4866; all operations are complete before/after units. The policy-edition increment to 1.0.2 and applied/superseded card retirement are explicit dependent operations, not unrelated cleanup. Complete prior files are preserved before mutation and complete proposal cards remain at the immutable pre-application revision.

The 04/05A content and their unique review receivers are incorporated together. Existing 8 architecture minima, 4 references and 2 presentation checks remain in the checker. The quotation candidate now checks full raw contexts, unique section occurrence, exact line counts and real receiver presence. Workflow scope remains PR/manual with read-only contents and the uniquely named job; native protections are not activated.

This receipt closes the 26 literal applications. Role/protection adjudication, protected-source identity choices, the larger exact-wave/role guard, native actor acceptance and scientific evidence tasks remain their actual implementation/deliverable state. Their specification paragraphs are applied; they are not falsely certified as completed by those wording changes. The existing audit and every source-native result retain their claims and original scope.


**Execution verification:** all 26 accepted literal units and each dependent edition/receipt/retirement operation reproduce the expected candidate. Reversing the recorded operations recovers every complete predecessor byte; no unrecorded byte is accepted. The full candidate documentation checker passes 10,347 local routes, eight architecture minima and two canonical decks, with all four required references retained. The 36 quotation-context adversarial cases also pass against the actually amended reviews.

The complete GFM graph introduces no broken route/fragment or newly unreachable file. The one removed heading is the expressly retired duplicated Gradient 61remnant; its exact incoming ID remains as an explicit HTML anchor and its complete card remains pinned. Both maintained 04/05A sources retain their complete original bytes as prefixes. All 2,405 paths/modes remain, with only 11 existing files changed, 2,394 other entries and 70 other review surfaces exact. The 150-entry priorities ledger, 151 CSV rows, protected EP/EA routers, strategy, frozen sources/results and all binaries remain byte-identical. Final exact public readback is required before this application is reported complete.


## Post-implementation document-control audit 2.0 — 25 October 2026

**Assessment:** the repository is **partially conformant** with DC-GH-01 v1.0.2. The authorized implementation is present and preserves its source scope. Document identity, protection decisions and preventive enforcement remain incomplete. The most urgent additional finding is an inherited, still-active workflow that can write the two canonical presentation binaries directly to its checked-out branch.

This is the requested assessment of the repository **after implementation**, following the earlier policy, planning and execution assessments retained above. Reviewer: Codex, AI assistant, same continuing review; no independent human or external certification is claimed. The audited source is [main at 0221c0a9](https://github.com/dakleyer/structural-awareness-contributions/tree/0221c0a9e85a5e456c90e15594be487778baf408), the merge of [PR31](https://github.com/dakleyer/structural-awareness-contributions/pull/31). The comparison baseline is [f8ce4866](https://github.com/dakleyer/structural-awareness-contributions/tree/f8ce4866b6dc61af822198e66e256ca08f08c307), immediately before that implementation. Live branch, ruleset, workflow-state and execution queries were repeated on 25 October; these observations are time-bound settings evidence.

### What was examined and what the verdict means

The assessment reread the actual operative clauses 1–13, current planning/execution entries, CONTRIBUTING, all nine tracked workflow definitions, the deployed documentation verifier, the source/review receptions and the protected-source records. It enumerated the complete 2,405-path Git tree, parsed all 1,048 Markdown files with GFM links/headings/HTML IDs, compared navigation with the pre-implementation tree, and rechecked the 75 existing review candidates against their current sources, openings and source-owned dispositions. It replayed and reversed the complete implementation operation journal against the real merged blobs. Seven isolated adverse documentary cases then tested the deployed verifier's practical boundary.

Those activities evaluate document control and this implementation interval. Parsing all Markdown is not a new scientific reading of every assertion, completion of five/six substantive passes per source, or proof that every historical corpus edit preserved all scientific meaning. Source roles not yet adjudicated remain unclassified. The existing 75-unit population includes historical edition reviews; it is not a count of 75 independent audits or 75 approved current canons.

### Verified improvements and preservation

1. **The implementation reached main.** PR31 is merged; its real 11-file tree matches the recorded candidate. The 26 accepted literal units and their edition/reception/retirement operations reproduce the merged blobs, and inverse reconstruction recovers their complete predecessors. This review found no additional, unrecorded changed byte in that packet.
2. **No file or unrelated source was lost in that interval.** All 2,405 paths and modes remain; 2,394 other tree entries are identical. Both maintained 04/05A source files retain their entire earlier byte sequences as exact prefixes. Protected EP/EA entry routers, the strategy, historical/frozen sources, results and binaries are unchanged by PR31. This preservation result is bounded to f8ce4866 → 0221c0a9.
3. **Actual promotion is distinguishable from research validation.** The 04 source now explains qualification/response clocks and human-result reception. The 05A source receives dated UC-6/H1 evidence and the scoped EA-only interface offer. Their existing reviews acknowledge those additions. They introduce neither a new mandatory EHD-kernel field nor a new executed cross-organization result. The 01A-A01 and 02A opening statuses correctly identify incorporated research hypotheses while leaving causal and computational evidence open.
4. **Applied pending cards were retired with history.** The implementation journal accounts for 26 applied and two superseded control-plan card retirements. Short application receipts retain their headings/summaries and pinned complete original cards. The Gradient61 duplicated heading remnant is gone, while its old incoming HTML ID survives. These authorized retirements removed text from current working queues; they did not erase the earlier Git editions or their audit arguments.
5. **The real documentation job passed.** [Job121210027071](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/40207017095/job/121210027071), from GitHub Actions application15368, completed successfully on the accepted candidate. Its unique name is `Document control verification`; it reports 10,347 local routes, eight architecture section minima and two canonical decks. The current script retains all four required architecture references. Its workflow has explicit `contents: read` and PR/manual triggers.
6. **No new navigation failure was introduced.** The full before/after GFM comparison found zero new missing paths/fragments and zero newly unreachable files in the explicit file-edge graph. The only removed heading is the authorized Gradient61 remnant whose compatibility ID remains. All 75 review surfaces still have an incoming rendered route somewhere in the corpus, and all their mapped source paths exist. An incoming route somewhere is not proof of correct ownership or three-level placement.

### Clause-by-clause assessment against the current policy

| Operative clause | Actual post-implementation state | Assessment and consequence |
|---|---|---|
| **1. Authority, scope and precedence** | One operative DC-GH-01 v1.0.2 entry; review-method, claims and source-freeze authorities remain separately identified. EA's approved/observed discrepancy is still open. | **Partial:** the general precedence is clear; exact protected successor acceptance is not established. |
| **2. GitHub technical change record** | PR31, exact file diffs, immutable source editions and the real workflow result identify the application. Technical publication is kept distinct from scientific adoption. | **Met for this packet.** Historical audit receipts are provenance, not additional operative policies. |
| **3. Identity, role, lifecycle and claim status** | The revised hypothesis openings and maintained 04/05A reading distinguish incorporation from evidence. The proposed registry still has 61 `source-under-review` roles. | **Partial:** useful source-specific distinctions exist; corpus-wide role-dependent decisions cannot yet be enforced. |
| **4. Minimal logical-document register** | `governance/DOCUMENT_REGISTRY.yml` does not exist. The full proposed 72-record candidate is still text inside this control, with 68 proposed continuations plus seven retained reviews. Two source observations are now stale. | **Open:** the proposed mapping is not an installed operational register or accepted role decision. See findings DC2-03/04. |
| **5. Canonical/VNext link contract** | Ten foreign-review occurrences remain in four controlled navigation owners, plus the separately identified living05A→05review route. Benchmarkv0.3 is correctly recognized as a review alias. | **Partial/nonconforming at the confirmed mutable edges:** preserve proposal access and source meaning while resolving those exact routes after their dependencies. |
| **6. Navigation ownership and preservation** | The three canonical reading levels and nine owner paths are stated; no owner, path or file was moved/deleted in PR31. GFM introduced no new disconnection. | **Met for packet preservation; partial for repository role reconciliation.** Package/fixture README counts do not add canonical levels. |
| **7. Review, incorporation and promotion** | A named owner GO, complete literal units, bounded PR, receiving reviews and application receipts exist for the executed packet. Other requirements/profiles remain explicitly pending. | **Met for the incorporated packet; rollout remains open.** No further content is promoted by this assessment. |
| **8. Protected, append-only, frozen and historical sources** | The packet preserved their blobs; EA still differs from its last recorded approved blob. The deployed general checker does not verify protection or append-only constraints. A separate active presentation writer remains. | **Partial, high practical risk:** preservation was verified manually for this wave, but future preventive control is missing. |
| **9. Technical checks and enforcement** | A uniquely named read-only checker is live and successful. No role/exact-wave guard is deployed. `main` is unprotected, required checks are off and the ruleset list is empty. | **Open for prevention:** green CI does not enforce owner decisions or block out-of-scope edits. |
| **10. Institution and programme boundaries** | The operative policy, CONTRIBUTING and accepted additions distinguish inclusion, hypotheses, contributor reports and external adoption. | **Met in the assessed control/application texts.** This is not a new assessment of every institutional claim in the corpus. |
| **11. Exceptions, conservation and historical citations** | The four quotation references use exact original contexts and real receivers; broad VNext exclusions were not introduced. Frozen split-source and relocated snapshot citations retain their bytes. | **Met for checker disposition and card custody; reader limitations remain:** preserved quoted hrefs themselves are not repaired browser clicks. |
| **12. Bounded rollout and acceptance** | The accepted packet is closed to its demonstrated scope. Registry, roles, native controls, protected decisions and later content/evidence packets remain open. | **Partial:** implementation is progressive, as the policy says; overall closure would be premature. |
| **13. Maintenance** | CONTRIBUTING and the root README route to the one policy. Its latest-audit link and the wording of its current planning entry lag the newly applied edition. | **Partial:** small current-entry corrections are justified; avoid another control, index or VNext. |

### DC2-01 — An inherited active workflow can publish canonical presentation binaries

The [presentation-repair workflow at the audited revision](https://github.com/dakleyer/structural-awareness-contributions/blob/0221c0a9e85a5e456c90e15594be487778baf408/.github/workflows/repair-ecosystem-positioning-v12.yml) has `contents: write`, a manual trigger and push triggers on its two repair scripts and workflow. It runs both repair programs, checks that the changed-path set is exactly the two canonical v1.2 PPTX files, commits them as `github-actions[bot]`, and runs `git push`. Its path check limits which files may change; it does not establish accepted before/after bytes, content parity or a fresh owner decision for that run. There is no PR or environment-review gate in that definition.

The live [workflow369026517](https://api.github.com/repos/dakleyer/structural-awareness-contributions/actions/workflows/369026517) reports `active`. Five runs are recorded; the latest returned run, [36417928766](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36417928766), succeeded on 28 September. This is an inherited capability, not a presentation modification caused by PR31 or an execution performed during this audit. A manual run uses its selected ref; a qualifying push uses its checked-out branch. With the observed unprotected main configuration, the definition supplies an uncontrolled publication path if it runs against main with sufficient token permissions.

**Consequence:** the document-control PR/manual check is read-only, but the repository as a whole is not read-only for automation. A later repair can change approved binaries without the ordinary exact-wave reception and could invalidate custody/version references.

**Priority First; expected impact High; change risk Medium; effort Medium.** Prepare an exact owner-approved disposition: retire the obsolete writer or convert it to generation of reviewable outputs with a bounded PR and presentation-specific acceptance. Verify historical editions and current canonical deck identity before any change. Do not run it as a diagnostic or regenerate the decks to test this finding. No workflow setting or binary was changed by this audit.

### DC2-02 — The live checker does less than its future guard specification

The [deployed verifier](https://github.com/dakleyer/structural-awareness-contributions/blob/0221c0a9e85a5e456c90e15594be487778baf408/scripts/check_document_integrity.py#L119) checks parsed relative inline/HTML file existence, eight EP section minima, four reference strings and package/text minima for two decks. It does not read a document register, trusted approved blobs, an accepted exact-wave packet or GitHub approval authority. Its regex does not parse reference-style links; `https:` targets and `#`-only targets are excluded, and a fragment on a relative file URL is discarded before existence checking.

The following tests were actually executed against that script in an isolated documentary tree. All 1,048 Markdown inputs matched the audited main blobs; the two authentic presentation inputs were retained. Other tracked paths were existence placeholders, sufficient only for the checker's file-existence questions. The independent native CI result above covers the real complete checkout. Each test changed one private input, ran the whole checker, then restored that input byte-for-byte. No repository source, branch setting, scientific runner or external system was changed by these tests.

| Isolated case | Expected document-control outcome | Actual deployed-checker result |
|---|---|---|
| Add `[Audit test](./__audit_missing__.md)` to baseline README | Reject missing local file | **FAIL**, correctly identifies the missing path |
| Add `[Audit test](#__audit_missing_heading__)` to that README | Reject nonexistent live section | **PASS**; fragment is not assessed |
| Add `[Audit test][audit-missing]` and definition `[audit-missing]: ./__audit_missing__.md` | Reject missing reference-style target | **PASS**; this syntax is not parsed |
| Add a same-repository absolute `https://github.com/dakleyer/structural-awareness-contributions/blob/main/__audit_missing__.md` link | Reject missing current-repository file | **PASS**; treated as external HTTPS |
| Add baseline's direct link to `./00M_VNext.md` | Report a new foreign-review edge from a canonical router | **PASS**; 10,348 existing local routes are counted |
| Change the first EP heading prefix from `# ` to `# Audit ` while leaving the eight required sections intact | Report changed specially protected source | **PASS**; no approved-blob comparison exists |
| Insert a paragraph after EP's first blank line, within its earlier content rather than at the end | Reject failure of an append-only rule when applicable | **PASS**; no predecessor-prefix check exists |

These are six demonstrated coverage gaps, not six newly corrupted published files. The first case shows that the original local-file test still works. The quotation-context improvement is also real; its earlier 36 targeted cases are a different test set and are not counted as these seven tests or as native actor acceptance.

Live [main metadata](https://api.github.com/repos/dakleyer/structural-awareness-contributions/branches/main) reports `protected: false`, required checks off, empty check contexts/checks; [rulesets](https://api.github.com/repos/dakleyer/structural-awareness-contributions/rulesets) returns `[]`. `.github/CODEOWNERS` is absent. PR31 author and merger are both `dakleyer`; this does not supply a distinct owner reviewer. No adverse real-actor merge was attempted here.

**Priority First, after valid identity/protection inputs; impact High; risk Medium–High; effort High.** Implement and test the existing specified guard, including these parser/protection cases, rather than relabeling the present checker as complete. Establish a viable distinct author/reviewer route, trusted check identity and native denial/recovery tests before activating mandatory protections. Do not enable an owner-only approval rule that leaves the sole PR author unable to obtain the required review.

### DC2-03 — Identity coverage is proposed, not operational

The complete proposed registry has 72 records: 61 `source-under-review`, eight `canonical-router`, one `canonical`, one `fixture-index` and one `strategy`. These are planning roles, not a new global classification decision. The seven retained review editions are linked within proposed logical continuations. The current tree has 74 working filename-hinted review files plus the existing benchmarkv0.3 alias; their filenames alone do not establish roles or active uniqueness.

The 75 source-owned dispositions still point to existing sources, and every review has an incoming rendered route. No new VNext or VNext-of-VNext was created in the implementation. However, the two R01 families and the other retained-edition relationships cannot be certified as single-active current mappings until their proposed lifecycle/continuation decisions are accepted. Shared earlier Foundation/02A evidence remains historical dependency review, not a second new independent 02A audit.

**Priority First; impact High; risk Medium; effort Medium–High.** Adjudicate protected sources and the sources/receivers of the next change wave first; retain unsupported roles as unknown. Then install one small register at the declared path, with supported ownership, editions, parts and protection. Do not create another review for each part/edition or make all 61 records canonical by a bulk label.

### DC2-04 — Two observations in the proposed full registry are now stale

The [complete replacement registry candidate](https://github.com/dakleyer/structural-awareness-contributions/blob/0221c0a9e85a5e456c90e15594be487778baf408/DOCUMENT_CONTROL.md#complete-replacement-registry-candidate--still-not-installed) predates the now-applied 04/05A promotions. Comparing every candidate record's observed source blob against the audited tree finds exactly these two changes:

| Proposed registry source | Candidate `observed_blob` | Actual source at audited main |
|---|---|---|
| 04 general functional interfaces v0.5 integrated | `30e492c671efed802f7b881ed67e9f4dcd4bb079` | `02f4c9712d1b4be76a7c18a98452ee133a069661` |
| 05A current-state bridge v0.1 | `71abf26cd885d8567ca7d87dfcb4e44a2a5709d5` | `ea94ba9dbc63da8e8708455cab543e58b960f102` |

The changes are the authorized additive receptions, not loss or unexplained source drift. The old candidate remains legitimate history. Installing it verbatim would supply out-of-date observations to a future guard. Its source roles also remain provisional; the new blob observations would not resolve that independent decision.

**Priority First before installation; impact High for a valid guard baseline; risk Low for an evidence-backed proposal refresh; effort Low–Medium including receiving-source verification.** Prepare a successor candidate against the actual execution head and receipt, retaining the dated earlier candidate. Do not reset special *approved* SHAs to observations: those authority decisions are different fields and evidence.

### DC2-05 — EA's protected successor remains unresolved

The last recorded approved EA entry blob remains `4e41fc697bb2bd94d1f4dd2b75230937684b8152`; the observed entry is still `3ff5c26946b25608cea5cc1c9df8519dc61e1afd`. Their difference predates PR31. EP remains `9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b`, and the append-only strategy remains `f25aef42574afa9d321b352b3d2b1e1447575556`. PR31 preserves all three observed sources.

**Priority First; impact High; risk High if corrected without an authority decision, Low for preparation of the exact decision; effort Medium.** Use the existing historical delta analysis to obtain acceptance of the named EA successor or an exact targeted correction. Neither the current useful routes nor the older approved baseline should be discarded as an administrative shortcut. No reset, rollback or blanket approval follows from this audit.

### DC2-06 — Confirmed foreign-review routes still contradict the target contract

Fresh GFM inspection, including the benchmark alias, finds **ten occurrences / nine distinct source–target edges / four controlled owners**:

| Current owner | Foreign-review targets | Occurrences |
|---|---|---|
| EP entry | Requirements review; benchmarkv0.3 review twice | 3 |
| EA entry | benchmarkv0.3 review; DDS owning review | 2 |
| EA baseline index | Requirements review;04review;benchmarkv0.3 review | 3 |
| EA FG-TIDA index |05review;05Areview | 2 |

The living05A preface additionally links directly to05review; its own05Areview link is valid. The frozen05part retains its historical citations and is not retrofitted to the mutable-source rule. Own-companion repetitions in EP/EA are a readability question, not a second active VNext. Cross-VNext and contextual-to-VNext links remain allowed. Thus the 1,778 rendered references to these 75 review targets from 220 source paths are **not** 1,778 violations.

**Priority Next after content/identity gates; impact High for reader authority; risk Medium, High on protected routers without their decision; effort Medium.** Reuse the existing complete units18–25 and their dependencies. Route the reader to the incorporated/current source and retain review access through that source or a contextual route. Requirements promotion remains an atomic content/identity/consumer packet; do not replace its link in isolation or pretend a proposed working successor is already the adopted canon. EP's append-only restriction and EA's approved-successor decision still govern their exact treatment.

### DC2-07 — Four preserved quoted links are explained, not repaired as browser clicks

The current raw GFM graph reports 3,455 missing-file and 17 missing-fragment occurrences. Of the missing-file reports, 3,450 are in preserved/legacy-path records with original source-relative strings. All 17 fragment reports are in that historical population. These raw counts are not counts of broken current canonical routes.

The five reports outside that population are unchanged: two manifest references inside the04review quotation, A13/A14 inside the00Kreview quotation, and the partial UC-EA-03 URL at the frozen part02/part03 boundary. The exact-context verifier resolves the four quotation references to existing original receivers; ordered concatenation reconstructs the fifth destination. Existing nearby live routes supply the readable alternatives. This is why the native check can correctly pass without changing frozen/quoted text.

A literal click inside either retained quotation can still resolve relative to the review's directory and fail. The checker now understands provenance; the browser does not. Keep that reader limitation distinct from absent evidence, an undiscovered fifth CI failure, or a claim that every visible historical link now works.

**Priority Next for live explanatory routes only; impact Medium; risk Low; effort Low–Medium.** Preserve the original quote and expose the original-location/receiver link clearly beside it where needed. Do not edit the frozen split parts, rewrite thousands of custody strings or exclude all review files to make a scan green.

### DC2-08 — The current entry still contains stale status language

The operative header correctly says v1.0.2 and section16 records the accepted implementation. However, section15 still calls itself the **current planning entry** and says, literally, “The operative policy remains DC-GH-01v1.0.1.” The header's “Latest conformity audit” link still leads to the older second-assessment section. The EP VNext opening also retains the 6October statement that an hourly continuation is scheduled, although Iván subsequently canceled that continuation. These are current-reader ambiguities in preserved cumulative documents, not evidence that the timer has restarted or that the applied packet is pending again.

DOCUMENT_CONTROL is now 395,203bytes/3,927lines; its operative clauses occupy 18,479bytes/136lines. Most of the file is the owner-requested complete plan, candidates and evidence history. Keeping those units is justified, but a reader needs one short unambiguous current entry, current adopted edition, live outstanding work and direct latest-assessment link. A second control or wholesale rewrite would make ownership worse.

**Priority First for a small status-only wave; impact Medium–High for usability; risk Low; effort Low including literal/context checks.** Prepare bounded current-entry corrections in the existing documents, retain the dated historical facts and original cards, and point to section16.2 and this assessment. This audit publication itself appends only to the existing audit; it does not revise those source entries or reinstate scheduling.

### Prioritized follow-through and closure tests

| Order | Concrete next result | Expected benefit / impact | Risk / effort | Evidence required before closure |
|---|---|---|---|---|
| **First** | Decide the inherited automatic canonical-deck writer's disposition (DC2-01) | High: remove a publication path outside the accepted-wave process | Medium / Medium | Exact workflow disposition, current deck/custody baseline and reviewable-output path; no unsolicited binary regeneration |
| **First** | Prepare EA successor and material role/edition decisions (DC2-03/05) | High: reliable protection and companion ownership | Medium–High if applied prematurely / Medium–High | Named source/edition/owner decisions with unresolved roles visible |
| **First, small textual wave** | Refresh the two candidate observations and the few current-entry statements (DC2-04/08) | High for guard inputs; Medium–High for human navigation | Low / Low–Medium | Literal old/new pairs, actual source blobs, accepted receipts, unchanged history and no automatic role/SHA approval |
| **Next, dependent** | Install supported registry and implement the existing exact-wave/role/parser/protection guard (DC2-02/03) | High: reject wrong target, stale source and unauthorized scope | Medium–High / High | Trusted base/head/decision inputs; valid controls and adverse cases fail/pass as specified; no self-authorizing metadata |
| **Next, dependent** | Establish and prove native merge protection (DC2-02) | High: prevent rather than merely report inadmissible merges | Medium / Medium–High | Distinct feasible author/reviewer route, identifiable trusted check, actual denial and authorized-recovery evidence |
| **Next after reception** | Resolve the confirmed foreign-review reader routes and necessary quotation explanations (DC2-06/07) | High for authority/navigation; Medium for historical-click clarity | Medium on routers, Low on explanation / Medium | Content and consumers first; protected-source GO; source/review access and incoming anchors retained |
| **After** | Repeat the actual-state audit and close only demonstrated clauses | High: a truthful remaining-work boundary | Low after dependencies / Medium | Current tree, accepted role/protection data, native behavior, scoped source parity and public readback |

The proposed Requirements packet, HumanTime alternative, remaining source-profile decisions and H06/benchmark/R01/FH research work retain their existing scope and gates in the one action plan. They are not failed executions of the 26-unit packet or newly authorized experiments. A useful future wave must name its specific passages/settings and receiving documents; this assessment supplies priorities and acceptance evidence, not blanket implementation authority.

**Final assessment:** the executed wave improved actual reading, review reception, historical-context checking and traceable retirement. Its preservation and scope checks hold. Repository-wide document control remains incomplete chiefly because preventive controls and supported identity/protection data are absent. Address the inherited binary-writing workflow, accepted source identities and the real guard/native settings before declaring conformance closure. This additional audit is published in the existing audit file, preserving all preceding audit content and every other repository path/blob.


## Action-plan 3.0 reception — 25 October 2026

The owner-requested [action-plan3.0](../DOCUMENT_CONTROL.md#17-action-plan-30--simple-improvements-after-audit-20) responds to the post-implementation audit2.0. It prepares eight small first-wave source pairs, their application receipt, and one separately selectable workflow conversion. Every pair includes the complete old and proposed text, source, reason, impact, risk, effort, dependencies and verification. The current policy, programs, workflow, source roles and canonical content are unchanged by this planning publication. Implementation awaits Iván’s named wave GO.

## First-wave action-plan 3.0 application — 25 October 2026

**Applied:** AP3-01–AP3-08. The accepted maintenance edition, latest-audit route, current/historical planning entries, cancelled-continuation status, two-source observation reconciliation, contributor acceptance instruction and verifier coverage line are incorporated. The underlying verification algorithms, source classifications, approved-protection values, canonical research sources, programs, results and presentation binaries retain their earlier meanings and bytes outside those named units.

The implementation PR records the exact accepted wave, whole-tree diff, reverse reconstruction, actual job result and public readback. Applied cards are retired from the pending queue with their original anchors and complete immutable pre-application history. AP3-09 remains a separate unexecuted workflow decision. Registry installation, role/protection adjudication, fragment/reference-style/HTTPS checks and native merge safeguards remain the explicit later tasks in the audit; this first wave closes only its accepted maintenance units.


**Closure reception — 26 October 2026.** The eight source pairs were applied on25October through PR34. This reception preserves the intervening repository publications through `ce54b960c7ef3c0d9127e791a467b798d9566de7`: 192 added paths, 17 modified existing paths and 0 removed paths. In particular, the later historical-source-route verifier/manifest and expanded existing CI regressions are retained. The two document-control closure files are checked against this current baseline; the original eight-operation verification remains bound to its25October application, rather than being attributed to later contributors.
