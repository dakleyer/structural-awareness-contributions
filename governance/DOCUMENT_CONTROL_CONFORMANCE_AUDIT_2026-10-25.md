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
